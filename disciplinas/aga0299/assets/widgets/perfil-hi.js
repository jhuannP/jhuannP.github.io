/* Widget: perfil de 21 cm de duplo pico (AGA0299, Cap. 3)
   v_obs = V(R) sen i cos φ + ruído (σ ≈ 10 km/s); V_rot ≈ W / (2 sen i). */
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
      ctx.translate(p.x - 34, p.y + p.h / 2); ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; ctx.fillText(yl, 0, 0);
    }
    ctx.restore();
  }
  function mulberry32(a) {
    return function () {
      a |= 0; a = a + 0x6D2B79F5 | 0;
      var t = Math.imul(a ^ a >>> 15, 1 | a);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }
  function gauss(r) { var u = 1 - r(), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }

  var RAD = Math.PI / 180;
  var SIGMA = 10;               // dispersão de velocidades do gás (km/s)
  var RC = 0.07;                // raio de “virada” da curva de rotação (fração do raio do disco)
  var NPAR = 40000, NDISCO = 2600;
  var VMIN = -500, DV = 2, NB = 500;
  var XMAX = 420;               // eixo de velocidades do gráfico (km/s)

  // parcelas de gás: área uniforme (Σ_HI ≈ constante) entre R = 0,05 e 1
  var PR = new Float32Array(NPAR), PF = new Float32Array(NPAR), PG = new Float32Array(NPAR);
  (function () {
    var rnd = mulberry32(21), r2 = 0.05 * 0.05;
    for (var k = 0; k < NPAR; k++) {
      PR[k] = Math.sqrt(r2 + rnd() * (1 - r2));
      PF[k] = rnd() * 2 * Math.PI;
      PG[k] = gauss(rnd);
    }
  })();
  // curva de rotação: sobe rápido e fica plana
  function Vc(R, Vrot) { return Vrot * (1 - Math.exp(-R / RC)); }

  // histograma suavizado (núcleo gaussiano de 4 km/s) das velocidades de linha de visada
  function perfil(Vrot, sini) {
    var h = new Float64Array(NB), k, j;
    for (k = 0; k < NPAR; k++) {
      var v = Vc(PR[k], Vrot) * sini * Math.cos(PF[k]) + SIGMA * PG[k];
      var b = Math.floor((v - VMIN) / DV);
      if (b >= 0 && b < NB) h[b]++;
    }
    var sk = 4 / DV, nk = Math.ceil(3 * sk), w = [], ws = 0;
    for (j = -nk; j <= nk; j++) { var x = Math.exp(-0.5 * j * j / (sk * sk)); w.push(x); ws += x; }
    var s = new Float64Array(NB), pk = 0;
    for (k = 0; k < NB; k++) {
      var acc = 0;
      for (j = -nk; j <= nk; j++) { var kk = k + j; if (kk >= 0 && kk < NB) acc += h[kk] * w[j + nk]; }
      s[k] = acc / ws;
      if (s[k] > pk) pk = s[k];
    }
    for (k = 0; k < NB; k++) s[k] /= pk;       // normaliza ao pico
    return s;
  }
  function vb(k) { return VMIN + (k + 0.5) * DV; }
  // largura a uma fração f do pico, medida das bordas para dentro (interpolação linear)
  function largura(s, f) {
    var k, vL = NaN, vR = NaN;
    for (k = 1; k < NB; k++) if (s[k] >= f) { vL = vb(k - 1) + (f - s[k - 1]) / (s[k] - s[k - 1]) * DV; break; }
    for (k = NB - 2; k >= 0; k--) if (s[k] >= f) { vR = vb(k) + (s[k] - f) / (s[k] - s[k + 1]) * DV; break; }
    return { vL: vL, vR: vR, W: vR - vL };
  }

  AGA.widgets['perfil-hi'] = function (root) {
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Perfil de HI em 21 cm: o “chifre duplo”');
    el('p', 'w-caption', hd,
      'Gás HI num disco fino com curva de rotação plana (V(R) = V<sub>rot</sub>(1 − e<sup>−R/0,07R<sub>máx</sub></sup>), plana fora do núcleo). ' +
      'Cada parcela contribui com v = V(R) sen i cos φ + ruído gaussiano (σ ≈ 10 km/s; φ medido a partir do eixo maior). ' +
      'Como dv/dφ → 0 perto de φ = 0° e 180°, muitas parcelas se acumulam em ±V<sub>rot</sub> sen i: os dois picos. ' +
      'Da largura W (a 50 % ou 20 % do pico): V<sub>rot</sub> ≈ W / (2 sen i). Simplificações: gás opticamente fino, Σ<sub>HI</sub> uniforme, ' +
      'velocidades no referencial da galáxia (sem velocidade sistêmica) e sem correção do alargamento por turbulência.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Disco de gás colorido por velocidade e perfil de linha de 21 cm');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null, tempo = 0, frac = 0.5, cache = { key: '' };

    var gV = slider(ctl, 'V_rot', 80, 350, 1, 200, function (v) { return fmt(v, 0) + ' km/s'; }, draw);
    var gI = slider(ctl, 'Inclinação i', 10, 90, 0.5, 60, function (v) { return fmt(v, 1) + '°'; }, draw);
    var bW = el('button', 'w-btn', ctl);
    bW.type = 'button';
    bW.textContent = 'Medir em 20 % do pico';
    bW.addEventListener('click', function () {
      frac = frac === 0.5 ? 0.2 : 0.5;
      bW.textContent = frac === 0.5 ? 'Medir em 20 % do pico' : 'Medir em 50 % do pico';
      draw();
    });
    var btn = el('button', 'w-btn', ctl);
    btn.type = 'button';

    function layout(W, H) {
      if (W >= 560) return { disco: { x: 0, y: 0, w: W * 0.42, h: H }, graf: { x: W * 0.42, y: 0, w: W * 0.58, h: H } };
      var h1 = Math.round(H * 0.5);
      return { disco: { x: 0, y: 0, w: W, h: h1 }, graf: { x: 0, y: h1, w: W, h: H - h1 } };
    }

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var Vrot = gV(), iDeg = gI(), si = Math.sin(iDeg * RAD), ci = Math.cos(iDeg * RAD);
      var key = Vrot + '|' + iDeg;
      if (cache.key !== key) { cache.key = key; cache.s = perfil(Vrot, si); }
      var s = cache.s;
      var w50 = largura(s, 0.5), w20 = largura(s, 0.2), wm = frac === 0.5 ? w50 : w20;
      var Vrec = wm.W / (2 * si);
      var L = layout(W, H);

      // paleta: aproximando (azul) → neutro → afastando (laranja)
      var cA = rgb(c.accent), cN = rgb(c.muted), cW = rgb(c.warm), PAL = [];
      for (var k = 0; k <= 40; k++) {
        var t = k / 20 - 1;
        PAL.push(t < 0 ? mix(cN, cA, -t) : mix(cN, cW, t));
      }
      function corV(v) { return PAL[Math.round((clamp(v / 300, -1, 1) + 1) * 20)]; }

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      // ----- disco inclinado colorido pela velocidade de linha de visada -----
      var r = L.disco, cx = r.x + r.w / 2, cy = r.y + r.h * 0.53;
      var sc = Math.min(r.w * 0.44, r.h * 0.42);
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('Disco de HI (i = ' + fmt(iDeg, 0) + '°)', r.x + 12, r.y + 8);
      ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.5; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.ellipse(cx, cy, sc * 1.02, Math.max(0.5, sc * 1.02 * ci), 0, 0, 2 * Math.PI); ctx.stroke();
      ctx.setLineDash([3, 4]);
      ctx.beginPath(); ctx.moveTo(cx - sc * 1.1, cy); ctx.lineTo(cx + sc * 1.1, cy); ctx.stroke();
      ctx.setLineDash([]);
      ctx.globalAlpha = 0.75;
      for (k = 0; k < NDISCO; k++) {
        var R = PR[k], V = Vc(R, Vrot);
        var ph = PF[k] + tempo * 0.5 * (V / Vrot) / R;   // rotação diferencial (V constante ⇒ Ω ∝ 1/R)
        var cph = Math.cos(ph);
        var vlos = V * si * cph;
        var X = cx + sc * R * cph, Y = cy - sc * R * Math.sin(ph) * ci;
        ctx.fillStyle = corV(vlos);
        ctx.fillRect(X - 0.9, Y - 0.9, 1.8, 1.8);
      }
      ctx.globalAlpha = 1;
      ctx.font = '11px ' + ff; ctx.textBaseline = 'top';
      ctx.textAlign = 'left'; ctx.fillStyle = c.accent;
      ctx.fillText('aproxima (v < 0)', r.x + 8, r.y + r.h - 20);
      ctx.textAlign = 'right'; ctx.fillStyle = c.warm;
      ctx.fillText('afasta (v > 0)', r.x + r.w - 8, r.y + r.h - 20);

      // ----- perfil de linha -----
      var q = painel(L.graf, [28, 14, 38, 50], [-XMAX, XMAX], [0, 1.12]);
      eixos(ctx, q, c, ff,
        [[-400, '−400'], [-200, '−200'], [0, '0'], [200, '200'], [400, '400']],
        [[0, '0'], [0.5, '0,5'], [1, '1']],
        'v (km/s)', 'S / S_pico');
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('Perfil de 21 cm (simulado)', q.x, q.y - 8);
      // barras coloridas pela velocidade
      var bw = Math.max(1, q.X(DV) - q.X(0) + 0.4);
      ctx.globalAlpha = 0.55;
      for (k = 0; k < NB; k++) {
        var v = vb(k);
        if (v < -XMAX || v > XMAX || s[k] < 0.004) continue;
        ctx.fillStyle = corV(v);
        var y0 = q.Y(s[k]);
        ctx.fillRect(q.X(v) - bw / 2, y0, bw, q.y + q.h - y0);
      }
      ctx.globalAlpha = 1;
      ctx.strokeStyle = c.ink; ctx.lineWidth = 1.6;
      ctx.beginPath();
      var ini = true;
      for (k = 0; k < NB; k++) {
        v = vb(k);
        if (v < -XMAX || v > XMAX) continue;
        if (ini) { ctx.moveTo(q.X(v), q.Y(s[k])); ini = false; } else ctx.lineTo(q.X(v), q.Y(s[k]));
      }
      ctx.stroke();
      // ±V_rot sen i (valor verdadeiro)
      var vt = Vrot * si;
      ctx.strokeStyle = c.muted; ctx.setLineDash([2, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(q.X(-vt), q.y); ctx.lineTo(q.X(-vt), q.y + q.h); ctx.moveTo(q.X(vt), q.y); ctx.lineTo(q.X(vt), q.y + q.h); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = c.muted; ctx.font = '10px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('±V sen i', q.X(vt) + 3, q.y + 3);
      // nível de medida e largura W
      var yf = q.Y(frac);
      ctx.strokeStyle = c.accent2; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(q.x, yf); ctx.lineTo(q.x + q.w, yf); ctx.stroke();
      ctx.setLineDash([]);
      if (isFinite(wm.W)) {
        var xl = q.X(wm.vL), xr = q.X(wm.vR);
        ctx.lineWidth = 1.8; ctx.strokeStyle = c.accent2; ctx.fillStyle = c.accent2;
        ctx.beginPath(); ctx.moveTo(xl, yf); ctx.lineTo(xr, yf); ctx.stroke();
        [[xl, 1], [xr, -1]].forEach(function (p) {
          ctx.beginPath(); ctx.moveTo(p[0], yf); ctx.lineTo(p[0] + 7 * p[1], yf - 4); ctx.lineTo(p[0] + 7 * p[1], yf + 4); ctx.closePath(); ctx.fill();
          ctx.beginPath(); ctx.arc(p[0], yf, 3, 0, 2 * Math.PI); ctx.fill();
        });
        ctx.font = '600 11.5px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
        ctx.fillText('W' + (frac === 0.5 ? '50' : '20') + ' = ' + fmt(wm.W, 0) + ' km/s', (xl + xr) / 2, yf - 6);
      }

      var err = (Vrec / Vrot - 1) * 100;
      ro.innerHTML =
        '<div>V<sub>rot</sub> sen i = ' + fmt(vt, 1) + ' km/s ⇒ 2 V<sub>rot</sub> sen i = ' + fmt(2 * vt, 0) + ' km/s</div>' +
        '<div>W<sub>50</sub> = ' + fmt(w50.W, 0) + ' km/s; W<sub>20</sub> = ' + fmt(w20.W, 0) + ' km/s</div>' +
        '<div>V<sub>rot</sub> recuperada = W' + (frac === 0.5 ? '₅₀' : '₂₀') + ' / (2 sen i) = <b>' + fmt(Vrec, 0) + ' km/s</b> (real: ' + fmt(Vrot, 0) +
        ' km/s; desvio ' + (err >= 0 ? '+' : '') + fmt(err, 1) + ' %)</div>' +
        (vt < 3 * SIGMA ? '<div>V sen i é comparável à dispersão: o perfil perde os dois picos e a estimativa fica ruim (galáxias quase de frente são evitadas).</div>' : '');
    }

    cv = canvasResponsivo(root, canvas, function (w) {
      return w >= 560 ? clamp(w * 0.5, 260, 460) : clamp(w * 1.05, 260, 460);
    }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
    animacao(root, btn, function (dt) {
      tempo += dt;
      draw();
    });
  };
})();
