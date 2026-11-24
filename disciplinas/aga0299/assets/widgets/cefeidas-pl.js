/* Widget: cefeida pulsante + relação período–luminosidade (AGA0299, Cap. 1)
   M_V ≈ −2,43 (log P − 1) − 4,05 (Benedict et al. 2007, calibração ilustrativa). */
(function () {
  'use strict';
  window.AGA = window.AGA || { widgets: {} };
  AGA.widgets = AGA.widgets || {};

  // ---------- utilidades comuns ----------
  function el(tag, cls, parent, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    if (parent) parent.appendChild(e);
    return e;
  }
  function cores() {
    var cs = getComputedStyle(document.documentElement);
    function g(n, f) { var v = cs.getPropertyValue(n).trim(); return v || f; }
    return {
      bg: g('--w-bg', '#0b1530'), ink: g('--w-ink', '#e8eefc'), muted: g('--w-muted', '#8796b8'),
      accent: g('--w-accent', '#4d8bff'), accent2: g('--w-accent-2', '#5fd4ff'),
      warm: g('--w-warm', '#ff9f43'), star: g('--w-star', '#fff6e0')
    };
  }
  function fmt(x, d) {
    if (!isFinite(x)) return '—';
    var s = Math.abs(x).toFixed(d).replace('.', ',');
    return (x < 0 && /[1-9]/.test(s) ? '−' : '') + s;
  }
  function sig(x) {
    return Number(x.toPrecision(3)).toLocaleString('pt-BR', { maximumSignificantDigits: 3 });
  }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function slider(parent, rotulo, min, max, step, val, formato, cb) {
    var lab = el('label', 'w-control', parent);
    var sp = el('span', null, lab);
    sp.appendChild(document.createTextNode(rotulo + ' '));
    var out = el('output', null, sp);
    var inp = el('input', null, lab);
    inp.type = 'range'; inp.min = min; inp.max = max; inp.step = step; inp.value = val;
    function upd() { out.textContent = formato(+inp.value); }
    inp.addEventListener('input', function () { upd(); cb(); });
    upd();
    return function () { return +inp.value; };
  }
  function canvasResponsivo(root, canvas, altura, redesenha) {
    var st = { w: 0, h: 0, dpr: 1, ctx: canvas.getContext('2d') };
    canvas.style.display = 'block';
    canvas.style.width = '100%';
    function ajusta() {
      var w = Math.round(canvas.clientWidth || root.clientWidth || 0);
      if (!w) { if (st.w) return; w = 600; }
      var dpr = window.devicePixelRatio || 1;
      if (w === st.w && dpr === st.dpr && st.h) return;
      var h = Math.round(altura(w));
      canvas.style.height = h + 'px';
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      st.w = w; st.h = h; st.dpr = dpr;
      st.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      redesenha();
    }
    if (window.ResizeObserver) new ResizeObserver(ajusta).observe(root);
    else window.addEventListener('resize', ajusta);
    st.ajusta = ajusta;
    return st;
  }
  function observaTema(cb) {
    try {
      var mo = new MutationObserver(cb);
      mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme', 'style'] });
      if (document.body) mo.observe(document.body, { attributes: true, attributeFilter: ['class', 'data-theme'] });
      if (window.matchMedia) {
        var mq = window.matchMedia('(prefers-color-scheme: dark)');
        if (mq.addEventListener) mq.addEventListener('change', cb); else if (mq.addListener) mq.addListener(cb);
      }
    } catch (e) { /* ignora */ }
  }
  // laço de animação: pausa fora da tela e respeita prefers-reduced-motion
  function animacao(root, botao, passo) {
    var reduz = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var tocando = !reduz, visivel = true, raf = 0, ultimo = 0;
    function rotulo() {
      botao.textContent = tocando ? '⏸ Pausar' : '▶ Animar';
      botao.setAttribute('aria-pressed', tocando ? 'true' : 'false');
    }
    function quadro(t) {
      raf = 0;
      if (!tocando || !visivel) return;
      var dt = ultimo ? Math.min(0.05, (t - ultimo) / 1000) : 0;
      ultimo = t;
      passo(dt);
      raf = requestAnimationFrame(quadro);
    }
    function liga() { if (!raf && tocando && visivel) { ultimo = 0; raf = requestAnimationFrame(quadro); } }
    botao.addEventListener('click', function () { tocando = !tocando; rotulo(); liga(); });
    if (window.IntersectionObserver) {
      new IntersectionObserver(function (es) { visivel = es[0].isIntersecting; liga(); }).observe(root);
    }
    rotulo(); liga();
  }
  var _cx = document.createElement('canvas').getContext('2d');
  function rgb(c) {
    _cx.fillStyle = '#000'; _cx.fillStyle = c;
    var s = String(_cx.fillStyle);
    if (s.charAt(0) === '#') return [parseInt(s.substr(1, 2), 16), parseInt(s.substr(3, 2), 16), parseInt(s.substr(5, 2), 16)];
    var m = s.match(/[\d.]+/g) || [0, 0, 0];
    return [+m[0], +m[1], +m[2]];
  }
  function mix(a, b, t, al) {
    var r = Math.round(a[0] + (b[0] - a[0]) * t), g = Math.round(a[1] + (b[1] - a[1]) * t), bb = Math.round(a[2] + (b[2] - a[2]) * t);
    return al == null ? 'rgb(' + r + ',' + g + ',' + bb + ')' : 'rgba(' + r + ',' + g + ',' + bb + ',' + al + ')';
  }
  // painel de gráfico: m = [topo, direita, base, esquerda]
  function painel(r, m, xr, yr) {
    var p = { x: r.x + m[3], y: r.y + m[0], w: r.w - m[1] - m[3], h: r.h - m[0] - m[2] };
    p.X = function (v) { return p.x + (v - xr[0]) / (xr[1] - xr[0]) * p.w; };
    p.Y = function (v) { return p.y + p.h - (v - yr[0]) / (yr[1] - yr[0]) * p.h; };
    return p;
  }
  function eixos(ctx, p, c, ff, xt, yt, xl, yl) {
    ctx.save();
    ctx.lineWidth = 1; ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.2;
    ctx.beginPath();
    xt.forEach(function (t) { var x = Math.round(p.X(t[0])) + 0.5; ctx.moveTo(x, p.y); ctx.lineTo(x, p.y + p.h); });
    yt.forEach(function (t) { var y = Math.round(p.Y(t[0])) + 0.5; ctx.moveTo(p.x, y); ctx.lineTo(p.x + p.w, y); });
    ctx.stroke();
    ctx.globalAlpha = 0.8;
    ctx.strokeRect(Math.round(p.x) + 0.5, Math.round(p.y) + 0.5, Math.round(p.w), Math.round(p.h));
    ctx.globalAlpha = 1; ctx.fillStyle = c.muted; ctx.font = '11px ' + ff;
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    xt.forEach(function (t) { ctx.fillText(t[1], p.X(t[0]), p.y + p.h + 4); });
    ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
    yt.forEach(function (t) { ctx.fillText(t[1], p.x - 5, p.Y(t[0])); });
    ctx.fillStyle = c.ink; ctx.font = '11.5px ' + ff;
    if (xl) { ctx.textAlign = 'center'; ctx.textBaseline = 'top'; ctx.fillText(xl, p.x + p.w / 2, p.y + p.h + 18); }
    if (yl) {
      ctx.translate(p.x - 36, p.y + p.h / 2); ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; ctx.fillText(yl, 0, 0);
    }
    ctx.restore();
  }

  // ---------- física ----------
  function MV(P) { return -2.43 * (Math.log(P) / Math.LN10 - 1) - 4.05; }
  // forma esquemática da curva de luz: subida rápida (15 % do ciclo), descida lenta
  function forma(ph) {
    ph -= Math.floor(ph);
    if (ph < 0.85) return 0.5 * (1 + Math.cos(Math.PI * ph / 0.85));
    return 0.5 * (1 - Math.cos(Math.PI * (ph - 0.85) / 0.15));
  }
  // amplitude ilustrativa em V (cresce com o período)
  function amp(P) { return 0.45 + 0.35 * Math.log(P) / Math.LN10; }
  // duração (s) de um ciclo na animação
  function Tanim(P) { return 1.6 + 0.04 * P; }

  AGA.widgets['cefeidas-pl'] = function (root) {
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Cefeidas: período, luminosidade e distância');
    el('p', 'w-caption', hd,
      'Cefeidas clássicas pulsam radialmente; o período P cresce com a luminosidade (lei de Leavitt). ' +
      'Calibração ilustrativa na banda V: M<sub>V</sub> ≈ −2,43 (log P − 1) − 4,05 (Benedict et al. 2007). ' +
      'Com a magnitude média observada ⟨m⟩: d = 10<sup>(⟨m⟩ − M<sub>V</sub> + 5)/5</sup> pc (sem extinção). ' +
      'Forma e amplitude da curva de luz são esquemáticas; a animação comprime P dias em poucos segundos.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Estrela pulsante, curva de luz e diagrama período–luminosidade');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null, fase = 0;

    var gP = slider(ctl, 'Período P', 1, 50, 0.1, 10, function (v) { return fmt(v, 1) + ' d'; }, draw);
    var gm = slider(ctl, '⟨m⟩ observada', 2, 20, 0.05, 12, function (v) { return fmt(v, 2) + ' mag'; }, draw);
    var btn = el('button', 'w-btn', ctl);
    btn.type = 'button';

    function layout(W, H) {
      if (W >= 560) {
        var a = W * 0.22, b = W * 0.42;
        return { star: { x: 0, y: 0, w: a, h: H }, lc: { x: a, y: 0, w: b, h: H }, pl: { x: a + b, y: 0, w: W - a - b, h: H } };
      }
      var h1 = Math.round(H * 0.47);
      return { star: { x: 0, y: 0, w: W * 0.32, h: h1 }, lc: { x: W * 0.32, y: 0, w: W * 0.68, h: h1 }, pl: { x: 0, y: h1, w: W, h: H - h1 } };
    }

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var P = gP(), mbar = gm(), logP = Math.log(P) / Math.LN10;
      var Mv = MV(P), A = amp(P);
      var mu = mbar - Mv, d = Math.pow(10, (mu + 5) / 5);
      var L = layout(W, H);
      var cW = rgb(c.warm), cS = rgb(c.star);

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      // --- estrela pulsante ---
      var s = L.star, cx = s.x + s.w / 2, cy = s.y + s.h * 0.48;
      var g = forma(fase);
      var dm = A * (0.5 - g);                       // m(t) − ⟨m⟩
      var I = Math.pow(10, -0.4 * dm);              // fluxo relativo
      var R0 = 0.26 * Math.min(s.w, s.h);
      var r = R0 * (1 - 0.07 * Math.cos(2 * Math.PI * (fase + 0.05)));  // raio mínimo pouco antes do máximo de luz
      var tcol = clamp((I - 0.62) / 0.95, 0, 1);
      var col = mix(cW, cS, tcol);
      var halo = ctx.createRadialGradient(cx, cy, r * 0.6, cx, cy, r * (1.7 + 0.7 * I));
      halo.addColorStop(0, mix(cW, cS, tcol, 0.55 * clamp(I, 0.4, 1.6) / 1.6));
      halo.addColorStop(1, mix(cW, cS, tcol, 0));
      ctx.fillStyle = halo;
      ctx.beginPath(); ctx.arc(cx, cy, r * (1.7 + 0.7 * I), 0, 2 * Math.PI); ctx.fill();
      var nucleo = ctx.createRadialGradient(cx - r * 0.25, cy - r * 0.25, r * 0.1, cx, cy, r);
      nucleo.addColorStop(0, mix(cS, [255, 255, 255], 0.6));
      nucleo.addColorStop(1, col);
      ctx.fillStyle = nucleo;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2 * Math.PI); ctx.fill();
      ctx.fillStyle = c.muted; ctx.font = '11px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      ctx.fillText('fase ' + fmt(fase % 1, 2), cx, s.y + s.h - 34);
      ctx.fillText('m = ' + fmt(mbar + dm, 2), cx, s.y + s.h - 20);

      // --- curva de luz (duas fases) ---
      var yTop = mbar - A / 2 - 0.15, yBot = mbar + A / 2 + 0.15;
      var p = painel(L.lc, [26, 12, 36, 52], [0, 2], [yBot, yTop]);
      eixos(ctx, p, c, ff,
        [[0, '0'], [0.5, fmt(P / 2, 1)], [1, fmt(P, 1)], [1.5, fmt(1.5 * P, 1)], [2, fmt(2 * P, 1)]],
        [[mbar - A / 2, fmt(mbar - A / 2, 1)], [mbar, fmt(mbar, 1)], [mbar + A / 2, fmt(mbar + A / 2, 1)]],
        't (dias)', 'V (mag)');
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('Curva de luz', p.x, p.y - 6);
      function mag(ph) { return mbar + A * (0.5 - forma(ph)); }
      ctx.save();
      ctx.beginPath(); ctx.rect(p.x, p.y, p.w, p.h); ctx.clip();
      ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.35; ctx.lineWidth = 1.2;
      ctx.beginPath();
      for (var k = 0; k <= 240; k++) { var ph = 2 * k / 240; var X = p.X(ph), Y = p.Y(mag(ph)); if (k) ctx.lineTo(X, Y); else ctx.moveTo(X, Y); }
      ctx.stroke();
      ctx.globalAlpha = 1; ctx.strokeStyle = c.accent2; ctx.lineWidth = 2.2;
      ctx.beginPath();
      var nT = Math.max(1, Math.round(120 * fase));
      for (k = 0; k <= nT; k++) { ph = fase * k / nT; X = p.X(ph); Y = p.Y(mag(ph)); if (k) ctx.lineTo(X, Y); else ctx.moveTo(X, Y); }
      ctx.stroke();
      ctx.fillStyle = c.warm;
      ctx.beginPath(); ctx.arc(p.X(fase), p.Y(mag(fase)), 4.5, 0, 2 * Math.PI); ctx.fill();
      ctx.restore();
      // linha da média
      ctx.setLineDash([4, 4]); ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.6;
      ctx.beginPath(); ctx.moveTo(p.x, p.Y(mbar)); ctx.lineTo(p.x + p.w, p.Y(mbar)); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;

      // --- diagrama período–luminosidade ---
      var q = painel(L.pl, [26, 12, 36, 52], [0, 1.8], [-1, -6.5]);
      eixos(ctx, q, c, ff,
        [[0, '0'], [0.5, '0,5'], [1, '1'], [1.5, '1,5']],
        [[-2, '−2'], [-3, '−3'], [-4, '−4'], [-5, '−5'], [-6, '−6']],
        'log P (P em dias)', 'M_V (mag)');
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('Período–luminosidade', q.x, q.y - 6);
      // faixa ilustrativa de ±0,2 mag (largura da faixa de instabilidade)
      ctx.fillStyle = c.accent; ctx.globalAlpha = 0.14;
      ctx.beginPath();
      ctx.moveTo(q.X(0), q.Y(MV(1) - 0.2)); ctx.lineTo(q.X(1.8), q.Y(MV(Math.pow(10, 1.8)) - 0.2));
      ctx.lineTo(q.X(1.8), q.Y(MV(Math.pow(10, 1.8)) + 0.2)); ctx.lineTo(q.X(0), q.Y(MV(1) + 0.2));
      ctx.closePath(); ctx.fill();
      ctx.globalAlpha = 1; ctx.strokeStyle = c.accent; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(q.X(0), q.Y(MV(1))); ctx.lineTo(q.X(1.8), q.Y(MV(Math.pow(10, 1.8)))); ctx.stroke();
      ctx.fillStyle = c.muted; ctx.font = '10.5px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('M_V = −2,43 (log P − 1)', q.x + 6, q.y + 6);
      ctx.fillText('        − 4,05', q.x + 6, q.y + 20);
      // ponto atual e guias
      var px = q.X(logP), py = q.Y(Mv);
      ctx.setLineDash([3, 3]); ctx.strokeStyle = c.warm; ctx.globalAlpha = 0.7; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(px, q.y + q.h); ctx.lineTo(px, py); ctx.lineTo(q.x, py); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;
      ctx.fillStyle = c.warm;
      ctx.beginPath(); ctx.arc(px, py, 5.5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.bg; ctx.lineWidth = 1.5; ctx.stroke();

      ro.innerHTML =
        '<div>P = <b>' + fmt(P, 1) + ' d</b>, log P = ' + fmt(logP, 3) + ' ⇒ M<sub>V</sub> = <b>' + fmt(Mv, 2) + ' mag</b></div>' +
        '<div>μ = ⟨m⟩ − M<sub>V</sub> = ' + fmt(mu, 2) + ' mag ⇒ d = <b>' + (d < 1e6 ? sig(d / 1e3) + ' kpc' : sig(d / 1e6) + ' Mpc') + '</b> (' + sig(d) + ' pc)</div>' +
        '<div>Amplitude ilustrativa ΔV ≈ ' + fmt(A, 2) + ' mag; na animação, 1 ciclo ≈ ' + fmt(Tanim(P), 1) + ' s ↔ ' + fmt(P, 1) + ' dias</div>';
    }

    cv = canvasResponsivo(root, canvas, function (w) {
      return w >= 560 ? clamp(w * 0.42, 260, 460) : clamp(w * 1.0, 260, 460);
    }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
    animacao(root, btn, function (dt) {
      fase += dt / Tanim(gP());
      if (fase >= 2) fase -= 2;
      draw();
    });
  };
})();
