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
  // Curva de rotação de uma espiral: bojo (Hernquist) + disco exponencial (Freeman) + halo isotérmico com núcleo.
  var G = 4.30e-6;          // kpc (km/s)² M☉⁻¹
  var A_BOJO = 0.6;         // raio de escala do bojo de Hernquist (kpc)
  var RMAX = 30;            // kpc

  /* Funções de Bessel modificadas — aproximações polinomiais de Abramowitz & Stegun (9.8.1–9.8.8). */
  function besselI0(x) {
    var ax = Math.abs(x), t, t2;
    if (ax <= 3.75) {
      t = x / 3.75; t2 = t * t;
      return 1 + t2 * (3.5156229 + t2 * (3.0899424 + t2 * (1.2067492 + t2 * (0.2659732 + t2 * (0.0360768 + t2 * 0.0045813)))));
    }
    t = 3.75 / ax;
    return (Math.exp(ax) / Math.sqrt(ax)) * (0.39894228 + t * (0.01328592 + t * (0.00225319 + t * (-0.00157565 + t * (0.00916281 +
      t * (-0.02057706 + t * (0.02635537 + t * (-0.01647633 + t * 0.00392377))))))));
  }
  function besselI1(x) {
    var ax = Math.abs(x), t, t2, r;
    if (ax <= 3.75) {
      t = x / 3.75; t2 = t * t;
      return x * (0.5 + t2 * (0.87890594 + t2 * (0.51498869 + t2 * (0.15084934 + t2 * (0.02658733 + t2 * (0.00301532 + t2 * 0.00032411))))));
    }
    t = 3.75 / ax;
    r = (Math.exp(ax) / Math.sqrt(ax)) * (0.39894228 + t * (-0.03988024 + t * (-0.00362018 + t * (0.00163801 + t * (-0.01031555 +
      t * (0.02282967 + t * (-0.02895312 + t * (0.01787654 - t * 0.00420059))))))));
    return x < 0 ? -r : r;
  }
  function besselK0(x) {
    var u, t;
    if (x <= 2) {
      u = x * x / 4;
      return -Math.log(x / 2) * besselI0(x) + (-0.57721566 + u * (0.42278420 + u * (0.23069756 + u * (0.03488590 +
        u * (0.00262698 + u * (0.00010750 + u * 0.0000074))))));
    }
    t = 2 / x;
    return (Math.exp(-x) / Math.sqrt(x)) * (1.25331414 + t * (-0.07832358 + t * (0.02189568 + t * (-0.01062446 +
      t * (0.00587872 + t * (-0.00251540 + t * 0.00053208))))));
  }
  function besselK1(x) {
    var u, t;
    if (x <= 2) {
      u = x * x / 4;
      return Math.log(x / 2) * besselI1(x) + (1 / x) * (1 + u * (0.15443144 + u * (-0.67278579 + u * (-0.18156897 +
        u * (-0.01919402 + u * (-0.00110404 - u * 0.00004686))))));
    }
    t = 2 / x;
    return (Math.exp(-x) / Math.sqrt(x)) * (1.25331414 + t * (0.23498619 + t * (-0.03655620 + t * (0.01504268 +
      t * (-0.00780353 + t * (0.00325614 - t * 0.00068245))))));
  }

  // V² de cada componente (km/s)², r em kpc
  function v2Bojo(r, Mb) { return G * Mb * r / ((r + A_BOJO) * (r + A_BOJO)); }
  function v2Disco(r, Md, Rd) {
    if (r <= 0) return 0;
    var y = r / (2 * Rd);
    // Freeman (1970): V² = 4πGΣ₀Rd y²[I₀K₀ − I₁K₁], com Σ₀ = Md/(2πRd²)
    return 2 * G * Md / Rd * y * y * (besselI0(y) * besselK0(y) - besselI1(y) * besselK1(y));
  }
  function v2Halo(r, Vinf, rc) {
    if (r <= 0) return 0;
    return Vinf * Vinf * (1 - (rc / r) * Math.atan(r / rc));
  }
  // Massa visível contida (bojo esférico + disco cilíndrico), só para comparação
  function mVisivel(r, p) {
    var mb = p.Mb * r * r / ((r + A_BOJO) * (r + A_BOJO));
    var md = p.Md * (1 - (1 + r / p.Rd) * Math.exp(-r / p.Rd));
    return mb + md;
  }

  function modelo(r, p) {
    var b = v2Bojo(r, p.Mb), d = v2Disco(r, p.Md, p.Rd), h = v2Halo(r, p.Vinf, p.rc);
    return { b: b, d: d, h: h, vis: b + d, tot: b + d + h };
  }

  // Pontos "observados" de 21 cm (ilustrativos): gerados uma vez a partir de um modelo de referência + ruído fixo.
  var REF = { Mb: 1e10, Md: 5e10, Rd: 3, Vinf: 200, rc: 5 };
  var OBS = (function () {
    var s = 12345, pts = [];
    function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    for (var r = 2; r <= 29; r += 1.8) {
      var v = Math.sqrt(modelo(r, REF).tot);
      var g = (rnd() + rnd() + rnd() - 1.5) * 1.6;   // ~ gaussiana
      var err = 6 + 6 * rnd() + (r > 20 ? 4 : 0);
      pts.push({ r: r, v: v + g * err * 0.8, e: err });
    }
    return pts;
  })();

  window.AGA.widgets['curva-rotacao'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">Curva de rotação: bojo + disco + halo</h4>' +
      '<p class="w-caption">As componentes somam <b>V², não V</b>: V² = V²<sub>bojo</sub> + V²<sub>disco</sub> + V²<sub>halo</sub>. ' +
      'Bojo de Hernquist V² = GM<sub>b</sub>r/(r+a)² (a = 0,6 kpc); disco exponencial de Freeman V² = 4πGΣ₀R<sub>d</sub>y²[I₀K₀ − I₁K₁], y = r/2R<sub>d</sub>; ' +
      'halo isotérmico com núcleo V²<sub>h</sub> = V∞²[1 − (r<sub>c</sub>/r)·arctg(r/r<sub>c</sub>)]. A curva tracejada é o que se esperaria só com a matéria visível ' +
      '(cai de forma kepleriana, V ∝ r<sup>−1/2</sup>, longe do centro). Os pontos de 21 cm são ilustrativos: tente ajustá-los.</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Gráfico da velocidade de rotação em função do raio, com as componentes bojo, disco, halo e total.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    var redesenhar = function () { desenhar(); };
    var sMb = slider(ctrl, { nome: 'Massa do bojo', min: 9, max: 10.8, step: 0.01, valor: 10, fmt: function (v) { return sci(Math.pow(10, v), 1) + ' M☉'; }, aoMudar: redesenhar });
    var sMd = slider(ctrl, { nome: 'Massa do disco', min: 9.5, max: 11.3, step: 0.01, valor: Math.log10(5e10), fmt: function (v) { return sci(Math.pow(10, v), 1) + ' M☉'; }, aoMudar: redesenhar });
    var sRd = slider(ctrl, { nome: 'Escala do disco Rd', min: 1, max: 6, step: 0.1, valor: 3, fmt: function (v) { return num(v, 1) + ' kpc'; }, aoMudar: redesenhar });
    var sV = slider(ctrl, { nome: 'Halo: V∞', min: 0, max: 300, step: 5, valor: 200, fmt: function (v) { return num(v, 0) + ' km/s'; }, aoMudar: redesenhar });
    var sRc = slider(ctrl, { nome: 'Halo: núcleo rc', min: 0.5, max: 15, step: 0.1, valor: 5, fmt: function (v) { return num(v, 1) + ' kpc'; }, aoMudar: redesenhar });
    var sR = slider(ctrl, { nome: 'Raio para M(<r)', min: 1, max: 30, step: 0.5, valor: 15, fmt: function (v) { return num(v, 1) + ' kpc'; }, aoMudar: redesenhar });
    botao(ctrl, 'Restaurar valores', function () {
      sMb.set(10); sMd.set(Math.log10(5e10)); sRd.set(3); sV.set(200); sRc.set(5); sR.set(15); desenhar();
    });

    var st = montarCanvas(root, canvas, function (w) { return limitar(w * 0.56, 260, 460); }, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    function params() {
      return { Mb: Math.pow(10, sMb.v()), Md: Math.pow(10, sMd.v()), Rd: sRd.v(), Vinf: sV.v(), rc: sRc.v() };
    }

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores(), p = params();
      var pequeno = W < 480;
      var mL = pequeno ? 40 : 50, mR = 12, mT = 12, mB = pequeno ? 34 : 38;
      var pw = W - mL - mR, ph = H - mT - mB;

      // amostragem das curvas
      var N = 240, curvas = [], vmax = 0;
      for (var i = 0; i <= N; i++) {
        var r = RMAX * i / N;
        var m = modelo(r, p);
        curvas.push({ r: r, m: m });
        vmax = Math.max(vmax, Math.sqrt(m.tot));
      }
      OBS.forEach(function (o) { vmax = Math.max(vmax, o.v + o.e); });
      var VMAX = Math.max(300, Math.ceil(vmax * 1.08 / 50) * 50);
      function X(r) { return mL + pw * r / RMAX; }
      function Y(v) { return mT + ph * (1 - v / VMAX); }

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      // grade e eixos
      fonte(ctx, root, pequeno ? 10 : 11);
      ctx.lineWidth = 1;
      ctx.strokeStyle = rgba(c.muted, 0.18);
      ctx.fillStyle = c.muted;
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (var rx = 0; rx <= RMAX; rx += 5) {
        ctx.beginPath(); ctx.moveTo(X(rx), mT); ctx.lineTo(X(rx), mT + ph); ctx.stroke();
        ctx.fillText(String(rx), X(rx), mT + ph + 4);
      }
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      for (var vy = 0; vy <= VMAX; vy += 50) {
        ctx.beginPath(); ctx.moveTo(mL, Y(vy)); ctx.lineTo(mL + pw, Y(vy)); ctx.stroke();
        if (vy % 100 === 0 || !pequeno) ctx.fillText(String(vy), mL - 5, Y(vy));
      }
      ctx.strokeStyle = rgba(c.muted, 0.6);
      ctx.strokeRect(mL, mT, pw, ph);
      ctx.fillStyle = c.muted;
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      ctx.fillText('r (kpc)', mL + pw / 2, H - 2);
      ctx.save(); ctx.translate(11, mT + ph / 2); ctx.rotate(-Math.PI / 2);
      ctx.textBaseline = 'middle'; ctx.fillText('V (km/s)', 0, 0); ctx.restore();

      function curva(campo, cor, larg, tracejado) {
        ctx.beginPath();
        for (var k = 0; k < curvas.length; k++) {
          var v = Math.sqrt(Math.max(0, curvas[k].m[campo]));
          var x = X(curvas[k].r), y = Y(v);
          if (k === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.strokeStyle = cor; ctx.lineWidth = larg;
        ctx.setLineDash(tracejado || []);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      ctx.save();
      ctx.beginPath(); ctx.rect(mL, mT, pw, ph); ctx.clip();
      curva('vis', rgba(c.ink, 0.75), 1.6, [6, 5]);
      curva('b', c.warm, 1.8);
      curva('d', c.accent, 1.8);
      curva('h', c.accent2, 1.8);
      curva('tot', c.star, 3);

      // pontos de 21 cm
      OBS.forEach(function (o) {
        ctx.strokeStyle = rgba(c.ink, 0.8); ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(X(o.r), Y(o.v - o.e)); ctx.lineTo(X(o.r), Y(o.v + o.e)); ctx.stroke();
        ctx.fillStyle = c.bg;
        ctx.beginPath(); ctx.arc(X(o.r), Y(o.v), 3.6, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      });

      // marcador do raio escolhido
      var rs = sR.v(), ms = modelo(rs, p), vs = Math.sqrt(ms.tot);
      ctx.strokeStyle = rgba(c.warm, 0.7); ctx.setLineDash([3, 4]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(X(rs), mT); ctx.lineTo(X(rs), mT + ph); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = c.warm;
      ctx.beginPath(); ctx.arc(X(rs), Y(vs), 5, 0, 2 * Math.PI); ctx.fill();
      ctx.restore();

      // legenda
      var itens = [
        ['Total', c.star, 3, null], ['Bojo', c.warm, 2, null], ['Disco', c.accent, 2, null],
        ['Halo', c.accent2, 2, null], [pequeno ? 'Só visível' : 'Só matéria visível', rgba(c.ink, 0.75), 1.6, [6, 5]]
      ];
      fonte(ctx, root, pequeno ? 10 : 11);
      var lw = pequeno ? 96 : 132, lh = 15, lx = mL + pw - lw - 6, ly = mT + 6;
      ctx.fillStyle = rgba(c.bg, 0.82);
      ctx.fillRect(lx - 4, ly - 4, lw + 4, lh * (itens.length + 1) + 6);
      ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      itens.forEach(function (it, k) {
        var yy = ly + lh * k + 6;
        ctx.strokeStyle = it[1]; ctx.lineWidth = it[2]; ctx.setLineDash(it[3] || []);
        ctx.beginPath(); ctx.moveTo(lx, yy); ctx.lineTo(lx + 20, yy); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = c.ink; ctx.fillText(it[0], lx + 26, yy);
      });
      var yo = ly + lh * itens.length + 6;
      ctx.strokeStyle = rgba(c.ink, 0.8); ctx.fillStyle = c.bg; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.arc(lx + 10, yo, 3.6, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
      ctx.fillStyle = c.ink; ctx.fillText('21 cm (ilustr.)', lx + 26, yo);

      // leituras
      var Mdin = ms.tot * rs / G;
      var Mvis = mVisivel(rs, p);
      var chi = 0;
      OBS.forEach(function (o) { var d = (Math.sqrt(modelo(o.r, p).tot) - o.v) / o.e; chi += d * d; });
      chi /= Math.max(1, OBS.length - 5);
      readout.innerHTML =
        '<div>Em r = <b>' + num(rs, 1) + ' kpc</b>: V = <b>' + num(vs, 0) + ' km/s</b> ' +
        '(bojo ' + num(Math.sqrt(ms.b), 0) + ', disco ' + num(Math.sqrt(ms.d), 0) + ', halo ' + num(Math.sqrt(ms.h), 0) + ' km/s)</div>' +
        '<div>M(&lt;r) = V²r/G ≈ <b>' + sci(Mdin, 2) + ' M☉</b> &nbsp;·&nbsp; massa visível contida ≈ ' + sci(Mvis, 2) + ' M☉ ' +
        '&nbsp;·&nbsp; fração não visível ≈ <b>' + num(Math.max(0, 1 - Mvis / Mdin) * 100, 0) + '%</b></div>' +
        '<div>χ² reduzido em relação aos pontos de 21 cm: <b>' + num(chi, 2) + '</b></div>' +
        '<div class="w-note">Aviso: M(&lt;r) = V²r/G vale exatamente só para distribuição esférica; para um disco achatado é uma aproximação ' +
        '(erro de algumas dezenas de por cento). G = 4,30 × 10⁻⁶ kpc (km/s)² M☉⁻¹.</div>';
    }
    desenhar();
  };
})();
