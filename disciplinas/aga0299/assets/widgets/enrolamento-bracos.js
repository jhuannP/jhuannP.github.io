(function () {
  'use strict';
  window.AGA = window.AGA || { widgets: {} };
  window.AGA.widgets = window.AGA.widgets || {};

  /* ---------- utilitários locais (cada widget é autocontido) ---------- */
  var SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };

  // Lê as cores do tema a cada redesenho (tema claro/escuro).
  function cores() {
    var cs = getComputedStyle(document.documentElement);
    function g(n, f) { var v = cs.getPropertyValue(n).trim(); return v || f; }
    return {
      bg: g('--w-bg', '#0b1530'), ink: g('--w-ink', '#e8eefc'), muted: g('--w-muted', '#8796b8'),
      accent: g('--w-accent', '#4d8bff'), accent2: g('--w-accent-2', '#5fd4ff'),
      warm: g('--w-warm', '#ff9f43'), star: g('--w-star', '#fff6e0')
    };
  }

  // Converte qualquer cor CSS em rgba com transparência a.
  var _cv = null;
  function rgba(c, a) {
    if (!_cv) _cv = document.createElement('canvas').getContext('2d');
    _cv.fillStyle = '#000'; _cv.fillStyle = c;
    var s = String(_cv.fillStyle);
    if (s.charAt(0) === '#') {
      var n = parseInt(s.slice(1), 16);
      return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')';
    }
    var m = s.match(/[\d.]+/g);
    if (m && m.length >= 3) return 'rgba(' + m[0] + ',' + m[1] + ',' + m[2] + ',' + (a * (m.length > 3 ? +m[3] : 1)) + ')';
    return c;
  }

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  function num(x, d) {
    if (Math.abs(x) < 0.5 * Math.pow(10, -d)) x = 0;   // evita “−0,0”
    return x.toLocaleString('pt-BR', { minimumFractionDigits: d, maximumFractionDigits: d });
  }
  function expo(e) { return String(e).split('').map(function (c) { return SUP[c] || c; }).join(''); }
  // Notação científica com expoente sobrescrito: 4,30 × 10⁻⁶
  function sci(x, d) {
    if (!isFinite(x)) return '—';
    if (x === 0) return '0';
    d = d == null ? 2 : d;
    var e = Math.floor(Math.log10(Math.abs(x)));
    var m = x / Math.pow(10, e);
    if (Math.abs(+m.toFixed(d)) >= 10) { m /= 10; e += 1; }
    return num(m, d) + ' × 10' + expo(e);
  }
  // Escolhe notação decimal ou científica conforme a ordem de grandeza.
  function fmt(x, d) {
    var a = Math.abs(x);
    if (a !== 0 && (a < 1e-2 || a >= 1e5)) return sci(x, d);
    return num(x, d == null ? 2 : d);
  }

  // Slider no padrão do site: <label class="w-control"><span>Nome <output/></span><input type="range"></label>
  function slider(parent, o) {
    var lab = el('label', 'w-control');
    var sp = el('span');
    sp.appendChild(document.createTextNode(o.nome + ' '));
    var out = el('output');
    sp.appendChild(out);
    lab.appendChild(sp);
    var inp = el('input');
    inp.type = 'range'; inp.min = o.min; inp.max = o.max; inp.step = o.step; inp.value = o.valor;
    if (o.marcas) {
      var id = 'dl-' + Math.random().toString(36).slice(2);
      var dl = el('datalist');
      dl.id = id;
      o.marcas.forEach(function (v) { var op = el('option'); op.value = v; dl.appendChild(op); });
      lab.appendChild(dl);
      inp.setAttribute('list', id);
    }
    lab.appendChild(inp);
    parent.appendChild(lab);
    var s = {
      input: inp, label: lab,
      v: function () { return parseFloat(inp.value); },
      set: function (v) { inp.value = v; s.mostra(); },
      mostra: function () { out.textContent = o.fmt ? o.fmt(s.v()) : String(s.v()); }
    };
    inp.addEventListener('input', function () { s.mostra(); if (o.aoMudar) o.aoMudar(s.v()); });
    s.mostra();
    return s;
  }

  function botao(parent, texto, fn) {
    var b = el('button', 'w-btn');
    b.type = 'button';
    b.textContent = texto;
    b.addEventListener('click', fn);
    parent.appendChild(b);
    return b;
  }

  // Canvas responsivo: largura do root, altura via alturaFn(w), escala por devicePixelRatio.
  function montarCanvas(root, canvas, alturaFn, desenhar) {
    var ctx = canvas.getContext('2d');
    var st = { w: 0, h: 0, ctx: ctx, dpr: 1 };
    function ajustar() {
      var cs = getComputedStyle(root);
      var w = root.clientWidth - (parseFloat(cs.paddingLeft) || 0) - (parseFloat(cs.paddingRight) || 0);
      w = Math.max(240, Math.floor(w || 600));
      var h = Math.round(alturaFn(w));
      var dpr = window.devicePixelRatio || 1;
      if (w === st.w && h === st.h && dpr === st.dpr) return;
      canvas.style.width = w + 'px';
      canvas.style.height = h + 'px';
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      st.w = w; st.h = h; st.dpr = dpr;
      desenhar();
    }
    if (typeof ResizeObserver !== 'undefined') new ResizeObserver(ajustar).observe(root);
    else window.addEventListener('resize', ajustar);
    ajustar();
    st.ajustar = ajustar;
    return st;
  }

  function limitar(x, a, b) { return Math.max(a, Math.min(b, x)); }

  // Redesenha quando o tema muda (classe/atributo no <html>/<body> ou preferência do sistema).
  function observarTema(fn) {
    try {
      var mo = new MutationObserver(function () { fn(); });
      var opt = { attributes: true, attributeFilter: ['class', 'data-theme', 'style'] };
      mo.observe(document.documentElement, opt);
      if (document.body) mo.observe(document.body, opt);
    } catch (e) { /* sem suporte */ }
    if (window.matchMedia) {
      var mq = window.matchMedia('(prefers-color-scheme: dark)');
      if (mq.addEventListener) mq.addEventListener('change', fn);
      else if (mq.addListener) mq.addListener(fn);
    }
  }

  // Laço de animação: pausa fora da tela, respeita prefers-reduced-motion, botão ▶/⏸.
  function animador(root, btn, passo) {
    var reduz = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
    var st = { tocando: !reduz, visivel: true, raf: 0, t0: 0 };
    function loop(t) {
      st.raf = 0;
      var dt = st.t0 ? Math.min(0.1, (t - st.t0) / 1000) : 0;
      st.t0 = t;
      passo(dt);
      agendar();
    }
    function agendar() { if (st.tocando && st.visivel && !st.raf) st.raf = requestAnimationFrame(loop); }
    function parar() { if (st.raf) cancelAnimationFrame(st.raf); st.raf = 0; st.t0 = 0; }
    function rotulo() {
      btn.textContent = st.tocando ? '⏸ Pausar' : '▶ Animar';
      btn.setAttribute('aria-pressed', st.tocando ? 'true' : 'false');
    }
    btn.addEventListener('click', function () {
      st.tocando = !st.tocando;
      rotulo();
      if (st.tocando) agendar(); else parar();
    });
    if (typeof IntersectionObserver !== 'undefined') {
      new IntersectionObserver(function (es) {
        st.visivel = es[0].isIntersecting;
        if (st.visivel) agendar(); else parar();
      }).observe(root);
    }
    rotulo();
    agendar();
    return st;
  }

  function fonte(ctx, root, px, peso) {
    var fam = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
    ctx.font = (peso ? peso + ' ' : '') + px + 'px ' + fam;
  }

  /* ---------- widget ---------- */
  // Dilema do enrolamento: braço material sob rotação diferencial (curva plana) vs. corpo rígido.
  var V = 220;              // km/s
  var KPC_KMS_GYR = 0.9778; // 1 kpc/(km/s) ≈ 0,978 Gyr
  var RMIN = 1, RMAX = 15;  // kpc
  var R_RIGIDO = 8;         // no modo rígido, Ω = V/8 kpc para todos
  var MARCADOS = [{ n: 'A', r: 2 }, { n: 'B', r: 5 }, { n: 'C', r: 9 }, { n: 'D', r: 14 }];

  window.AGA.widgets['enrolamento-bracos'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">O dilema do enrolamento</h4>' +
      '<p class="w-caption">Estrelas começam alinhadas num braço radial. Com curva de rotação plana (V = 220 km/s), ' +
      'Ω = V/r e o período T = 2πr/V cresce com o raio: a estrela interna A completa muitas voltas enquanto a externa D completa poucas, ' +
      'e o braço se enrola em ~10⁸ anos. Em rotação de corpo rígido (Ω constante) o braço nunca se deforma. ' +
      'Conversão: 1 kpc/(km/s) ≈ 0,978 Gyr.</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Disco galáctico visto de cima com um braço de estrelas se enrolando pela rotação diferencial.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    var t = 0;          // tempo em kpc/(km/s)
    var rigido = false;

    var btnPlay = el('button', 'w-btn'); btnPlay.type = 'button'; ctrl.appendChild(btnPlay);
    botao(ctrl, '↺ Reiniciar', function () { t = 0; desenhar(); });
    var btnModo = botao(ctrl, '', function () { rigido = !rigido; t = 0; rotuloModo(); desenhar(); });
    function rotuloModo() { btnModo.textContent = rigido ? 'Modo: corpo rígido (trocar)' : 'Modo: curva plana (trocar)'; }
    rotuloModo();
    var sVel = slider(ctrl, { nome: 'Velocidade da simulação', min: 5, max: 400, step: 5, valor: 60, fmt: function (v) { return num(v, 0) + ' Myr/s'; } });

    // estrelas de fundo (posições fixas aleatórias, giram com a mesma lei)
    var fundo = [], s = 777;
    function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    for (var i = 0; i < 420; i++) {
      var rr = RMIN + (RMAX + 1 - RMIN) * Math.sqrt(rnd());
      fundo.push({ r: rr, f: 2 * Math.PI * rnd(), b: 0.25 + 0.5 * rnd() });
    }

    function omega(r) { return rigido ? V / R_RIGIDO : V / r; }   // km/s/kpc
    function phi(r) { return Math.PI / 2 + omega(r) * t; }

    var st = montarCanvas(root, canvas, function (w) { return limitar(w < 480 ? w * 0.95 : w * 0.62, 260, 460); }, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores();
      var pequeno = W < 480;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2, esc = (Math.min(W, H) / 2 - 16) / RMAX;
      function P(r, f) { return [cx + r * Math.cos(f) * esc, cy - r * Math.sin(f) * esc]; }

      // brilho difuso do disco
      var gr = ctx.createRadialGradient(cx, cy, 0, cx, cy, RMAX * esc);
      gr.addColorStop(0, rgba(c.star, 0.35)); gr.addColorStop(0.15, rgba(c.accent, 0.12)); gr.addColorStop(1, rgba(c.accent, 0));
      ctx.fillStyle = gr; ctx.beginPath(); ctx.arc(cx, cy, RMAX * esc, 0, 2 * Math.PI); ctx.fill();

      // anéis de referência
      fonte(ctx, root, 10);
      ctx.strokeStyle = rgba(c.muted, 0.25); ctx.lineWidth = 1; ctx.fillStyle = rgba(c.muted, 0.8);
      ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      [5, 10, 15].forEach(function (r) {
        ctx.beginPath(); ctx.arc(cx, cy, r * esc, 0, 2 * Math.PI); ctx.stroke();
        ctx.fillText(r + ' kpc', cx + r * esc * 0.707 + 2, cy + r * esc * 0.707 - 2);
      });

      // estrelas de fundo
      fundo.forEach(function (q) {
        var p = P(q.r, q.f + omega(q.r) * t);
        ctx.fillStyle = rgba(c.star, q.b * 0.6);
        ctx.fillRect(p[0] - 0.7, p[1] - 0.7, 1.4, 1.4);
      });

      // o braço: curva contínua por 400 raios
      ctx.beginPath();
      for (var k = 0; k <= 400; k++) {
        var r = RMIN + (RMAX - RMIN) * k / 400;
        var p = P(r, phi(r));
        if (k === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.strokeStyle = rgba(c.accent2, 0.25); ctx.lineWidth = 7; ctx.stroke();
      ctx.strokeStyle = rgba(c.accent2, 0.85); ctx.lineWidth = 1.6; ctx.stroke();

      // estrelas do braço
      for (var j = 0; j < 40; j++) {
        var rj = RMIN + (RMAX - RMIN) * j / 39;
        var pj = P(rj, phi(rj));
        ctx.fillStyle = c.star;
        ctx.beginPath(); ctx.arc(pj[0], pj[1], 1.8, 0, 2 * Math.PI); ctx.fill();
      }
      // estrelas marcadas A–D
      fonte(ctx, root, pequeno ? 11 : 12, '600');
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      MARCADOS.forEach(function (m) {
        var pm = P(m.r, phi(m.r));
        ctx.fillStyle = c.warm;
        ctx.beginPath(); ctx.arc(pm[0], pm[1], 4.5, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = c.ink;
        var pl = P(m.r + 0.9, phi(m.r) + 0.12);
        ctx.fillText(m.n, pl[0], pl[1]);
      });
      // centro
      ctx.fillStyle = c.star; ctx.beginPath(); ctx.arc(cx, cy, 3, 0, 2 * Math.PI); ctx.fill();

      // rótulo de tempo no canvas
      var tGyr = t * KPC_KMS_GYR;
      fonte(ctx, root, pequeno ? 12 : 14, '600');
      ctx.fillStyle = c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('t = ' + num(tGyr, 3) + ' Gyr', 10, 8);
      fonte(ctx, root, pequeno ? 10 : 11);
      ctx.fillStyle = c.muted;
      ctx.fillText(rigido ? 'Ω = constante' : 'curva plana: Ω = V/r', 10, pequeno ? 26 : 28);

      // leituras
      var voltasA = omega(2) * t / (2 * Math.PI), voltasD = omega(14) * t / (2 * Math.PI);
      var TA = 2 * Math.PI * 2 / (rigido ? 2 * V / R_RIGIDO : V) * KPC_KMS_GYR * 1000;   // Myr
      var TD = 2 * Math.PI * 14 / (rigido ? 14 * V / R_RIGIDO : V) * KPC_KMS_GYR * 1000;
      var pitch = (rigido || t === 0) ? 90 : Math.atan(8 / (V * t)) * 180 / Math.PI;
      readout.innerHTML =
        '<div>Tempo: <b>' + num(tGyr, 3) + ' Gyr</b> (' + num(tGyr * 1000, 0) + ' Myr)</div>' +
        '<div>Estrela A (r = 2 kpc): T = ' + num(TA, 0) + ' Myr, <b>' + num(voltasA, 2) + ' voltas</b> &nbsp;·&nbsp; ' +
        'Estrela D (r = 14 kpc): T = ' + num(TD, 0) + ' Myr, <b>' + num(voltasD, 2) + ' voltas</b></div>' +
        '<div>Diferença: ' + num(voltasA - voltasD, 2) + ' voltas &nbsp;·&nbsp; ângulo de inclinação do braço em r = 8 kpc: ' +
        (rigido ? '<b>90° (permanece radial)</b>' : '<b>' + num(pitch, 1) + '°</b> (tg i = r/(Vt)); braços reais têm i ~ 10°–30°') + '</div>';
    }

    animador(root, btnPlay, function (dt) {
      t += dt * sVel.v() / 1000 / KPC_KMS_GYR;
      desenhar();
    });
    desenhar();
  };
})();
