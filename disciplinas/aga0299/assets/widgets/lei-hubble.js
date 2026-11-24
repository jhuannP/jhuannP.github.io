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
  // Lei de Hubble: expansão homogênea vista de qualquer galáxia.
  var PASSO = 8, NG = 12, JIT = 2.6;   // grade comóvel: espaçamento 8 Mpc, índices −12…12
  var MEIA_VISTA = 42;                // meia-largura do campo mostrado (Mpc físicos)
  var DMAX = 60, VMAX = 6000;         // eixos do gráfico v × d
  var A_MAX = 1.6;                    // a(t) recomeça ao atingir este fator

  window.AGA.widgets['lei-hubble'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">Lei de Hubble: todo observador vê o mesmo</h4>' +
      '<p class="w-caption">Numa expansão homogênea e isotrópica todas as distâncias crescem pelo mesmo fator a(t): ' +
      'd(t) = a(t)·d₀. Daí v = (ȧ/a)·d = H·d — a velocidade de recessão é proporcional à distância. ' +
      '<b>Clique em qualquer galáxia</b> para torná-la a “nossa”: o padrão de vetores é idêntico, não há centro. ' +
      'Tempo de Hubble t<sub>H</sub> = 1/H₀ = 977,8/H₀ Gyr (H₀ em km/s/Mpc).</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.style.cursor = 'pointer';
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Galáxias numa grade em expansão com vetores de recessão a partir da galáxia escolhida, e gráfico de velocidade contra distância.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    // galáxias: posição comóvel + velocidade peculiar fixa (km/s)
    var gal = [], s = 99;
    function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    function gauss() { return Math.sqrt(-2 * Math.log(Math.max(1e-12, rnd()))) * Math.cos(2 * Math.PI * rnd()); }
    for (var i = -NG; i <= NG; i++) {
      for (var j = -NG; j <= NG; j++) {
        gal.push({
          x: i * PASSO + (i || j ? (rnd() - 0.5) * 2 * JIT : 0),
          y: j * PASSO + (i || j ? (rnd() - 0.5) * 2 * JIT : 0),
          px: 220 * gauss(), py: 220 * gauss(),
          tam: 0.8 + 0.7 * rnd(), ang: Math.PI * rnd()
        });
      }
    }
    var ref = Math.floor(gal.length / 2);   // galáxia central da grade
    var tGyr = 0;                            // tempo desde a(0) = 1
    var pec = false;

    var btnPlay = el('button', 'w-btn'); btnPlay.type = 'button'; ctrl.appendChild(btnPlay);
    botao(ctrl, '↺ Reiniciar', function () { tGyr = 0; desenhar(); });
    var sH = slider(ctrl, { nome: 'H₀', min: 50, max: 100, step: 1, valor: 70, fmt: function (v) { return num(v, 0) + ' km/s/Mpc'; }, aoMudar: function () { desenhar(); } });
    var btnPec = botao(ctrl, '', function () { pec = !pec; rotuloPec(); desenhar(); });
    function rotuloPec() { btnPec.textContent = pec ? 'Velocidades peculiares: ligadas' : 'Velocidades peculiares: desligadas'; }
    rotuloPec();

    function tH() { return 977.8 / sH.v(); }            // Gyr
    function fatorA() { return Math.exp(tGyr / tH()); } // H constante ⇒ a = exp(t/t_H)

    function alturaFn(w) { return w < 560 ? limitar(w * 1.3, 260, 460) : limitar(w * 0.5, 260, 460); }
    var geo = null;
    var st = montarCanvas(root, canvas, alturaFn, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    // posição física relativa à galáxia de referência (Mpc) e velocidade relativa (km/s)
    // caixa periódica: o universo não tem borda nem centro
    var CAIXA = (2 * NG + 1) * PASSO;
    function envolver(u) { return u - CAIXA * Math.round(u / CAIXA); }
    function relativo(g, a, H0) {
      var r0 = gal[ref];
      var dx = a * envolver(g.x - r0.x), dy = a * envolver(g.y - r0.y);
      var vx = H0 * dx, vy = H0 * dy;
      if (pec) { vx += g.px - r0.px; vy += g.py - r0.py; }
      return { dx: dx, dy: dy, vx: vx, vy: vy };
    }

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores();
      var pequeno = W < 480;
      var lado = W >= 560;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);
      var a = fatorA(), H0 = sH.v();

      /* --- painel do céu --- */
      var cw = lado ? Math.min(W / 2, H) : W, chh = lado ? H : H * 0.55;
      var cx = cw / 2, cy = chh / 2;
      var esc = (Math.min(cw, chh) / 2 - 6) / MEIA_VISTA;      // px por Mpc
      var kv = (Math.min(cw, chh) / 2) * 0.3 / (100 * MEIA_VISTA); // px por km/s
      geo = { cx: cx, cy: cy, esc: esc, a: a, w: cw, h: chh };
      ctx.save();
      ctx.beginPath(); ctx.rect(0, 0, cw, chh); ctx.clip();
      ctx.fillStyle = rgba(c.accent, 0.04); ctx.fillRect(0, 0, cw, chh);
      // círculos de distância a partir da galáxia de referência
      ctx.strokeStyle = rgba(c.muted, 0.18); ctx.lineWidth = 1;
      fonte(ctx, root, 9);
      ctx.fillStyle = rgba(c.muted, 0.8); ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      [20, 40].forEach(function (d) {
        ctx.beginPath(); ctx.arc(cx, cy, d * esc, 0, 2 * Math.PI); ctx.stroke();
        ctx.fillText(d + ' Mpc', cx + d * esc * 0.71 + 2, cy - d * esc * 0.71);
      });
      var pts = [];
      gal.forEach(function (g, k) {
        var q = relativo(g, a, H0);
        var x = cx + q.dx * esc, y = cy - q.dy * esc;
        if (x < -10 || x > cw + 10 || y < -10 || y > chh + 10) return;
        var d = Math.sqrt(q.dx * q.dx + q.dy * q.dy);
        if (k !== ref) {
          // vetor de recessão
          var ex = x + q.vx * kv, ey = y - q.vy * kv;
          ctx.strokeStyle = rgba(c.accent2, 0.75); ctx.lineWidth = 1.2;
          ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(ex, ey); ctx.stroke();
          var an = Math.atan2(ey - y, ex - x), hl = Math.min(5, 0.4 * Math.hypot(ex - x, ey - y));
          ctx.fillStyle = rgba(c.accent2, 0.75);
          ctx.beginPath(); ctx.moveTo(ex, ey);
          ctx.lineTo(ex - hl * Math.cos(an - 0.45), ey - hl * Math.sin(an - 0.45));
          ctx.lineTo(ex - hl * Math.cos(an + 0.45), ey - hl * Math.sin(an + 0.45));
          ctx.closePath(); ctx.fill();
          if (d <= DMAX && d > 0) pts.push({ d: d, v: (q.dx * q.vx + q.dy * q.vy) / d });
        }
        // galáxia: elipse pequena
        ctx.fillStyle = k === ref ? c.warm : rgba(c.star, 0.92);
        ctx.beginPath();
        ctx.ellipse(x, y, (k === ref ? 5 : 2.6) * g.tam, (k === ref ? 5 : 1.6) * g.tam, g.ang, 0, 2 * Math.PI);
        ctx.fill();
      });
      ctx.strokeStyle = c.warm; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(cx, cy, 9, 0, 2 * Math.PI); ctx.stroke();
      ctx.restore();
      fonte(ctx, root, pequeno ? 10 : 11, '600');
      ctx.fillStyle = c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('a(t) = ' + num(a, 3) + '   t = ' + num(tGyr, 2) + ' Gyr', 8, 6);

      /* --- gráfico v × d --- */
      var gx0 = lado ? cw : 0, gy0 = lado ? 0 : chh, gw = W - gx0, gh = H - gy0;
      var box = { x: gx0 + (pequeno ? 46 : 56), y: gy0 + 14, w: 0, h: 0 };
      box.w = gx0 + gw - box.x - 12; box.h = gy0 + gh - box.y - (pequeno ? 36 : 40);
      function X(d) { return box.x + box.w * d / DMAX; }
      function Y(v) { return box.y + box.h * (1 - v / VMAX); }
      fonte(ctx, root, pequeno ? 9 : 10);
      ctx.lineWidth = 1; ctx.fillStyle = c.muted;
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (var dd = 0; dd <= DMAX; dd += 10) {
        ctx.strokeStyle = rgba(c.muted, 0.16);
        ctx.beginPath(); ctx.moveTo(X(dd), box.y); ctx.lineTo(X(dd), box.y + box.h); ctx.stroke();
        ctx.fillText(String(dd), X(dd), box.y + box.h + 3);
      }
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      for (var vv = 0; vv <= VMAX; vv += 1000) {
        ctx.strokeStyle = rgba(c.muted, 0.16);
        ctx.beginPath(); ctx.moveTo(box.x, Y(vv)); ctx.lineTo(box.x + box.w, Y(vv)); ctx.stroke();
        ctx.fillText(num(vv, 0), box.x - 4, Y(vv));
      }
      ctx.strokeStyle = rgba(c.muted, 0.6); ctx.strokeRect(box.x, box.y, box.w, box.h);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      ctx.fillText('d (Mpc)', box.x + box.w / 2, box.y + box.h + (pequeno ? 30 : 34));
      ctx.save(); ctx.translate(box.x - (pequeno ? 38 : 46), box.y + box.h / 2); ctx.rotate(-Math.PI / 2);
      ctx.textBaseline = 'middle'; ctx.fillText('v (km/s)', 0, 0); ctx.restore();

      ctx.save(); ctx.beginPath(); ctx.rect(box.x, box.y, box.w, box.h); ctx.clip();
      ctx.strokeStyle = c.warm; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(DMAX), Y(H0 * DMAX)); ctx.stroke();
      pts.forEach(function (p) {
        ctx.fillStyle = rgba(c.accent2, 0.85);
        ctx.beginPath(); ctx.arc(X(p.d), Y(p.v), 2.3, 0, 2 * Math.PI); ctx.fill();
      });
      ctx.restore();
      fonte(ctx, root, pequeno ? 10 : 11, '600');
      ctx.fillStyle = c.warm; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('inclinação = H₀ = ' + num(H0, 0) + ' km/s/Mpc', box.x + 8, box.y + 6);

      var g0 = gal[ref];
      readout.innerHTML =
        '<div>H₀ = <b>' + num(H0, 0) + ' km/s/Mpc</b> → tempo de Hubble 1/H₀ = 977,8/H₀ = <b>' + num(tH(), 2) + ' Gyr</b></div>' +
        '<div>Exemplo: uma galáxia a 30 Mpc se afasta a v = H₀·d = ' + num(H0 * 30, 0) + ' km/s (z ≈ v/c ≈ ' + num(H0 * 30 / 299792.458, 4) + ')</div>' +
        '<div>Observador: galáxia na posição comóvel (' + num(g0.x, 0) + ', ' + num(g0.y, 0) + ') Mpc (caixa periódica de ' + num(CAIXA, 0) + ' Mpc). ' +
        (pec ? 'Com velocidades peculiares (~220 km/s por componente) os pontos se espalham em torno da reta, sobretudo perto.' : 'Sem velocidades peculiares todos os pontos caem exatamente na reta.') + '</div>' +
        '<div>Simplificação: H constante no tempo (a = e<sup>t/t<sub>H</sub></sup>), só para a animação; o fator a recomeça em ' + num(A_MAX, 1) + '.</div>';
    }

    canvas.addEventListener('click', function (ev) {
      if (!geo) return;
      var rc = canvas.getBoundingClientRect();
      var mx = ev.clientX - rc.left, my = ev.clientY - rc.top;
      if (mx > geo.w || my > geo.h) return;
      var r0 = gal[ref], melhor = -1, dmin = 18 * 18;
      gal.forEach(function (g, k) {
        var x = geo.cx + geo.a * envolver(g.x - r0.x) * geo.esc, y = geo.cy - geo.a * envolver(g.y - r0.y) * geo.esc;
        var d2 = (x - mx) * (x - mx) + (y - my) * (y - my);
        if (d2 < dmin) { dmin = d2; melhor = k; }
      });
      if (melhor >= 0) { ref = melhor; desenhar(); }
    });

    animador(root, btnPlay, function (dt) {
      tGyr += dt * 0.8;                       // 0,8 Gyr por segundo de animação
      if (fatorA() > A_MAX) tGyr = 0;
      desenhar();
    });
    desenhar();
  };
})();
