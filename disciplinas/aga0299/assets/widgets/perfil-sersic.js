/* Widget: perfil de Sérsic (AGA0299, Caps. 3–5)
   I(R) = Ie exp{−b_n[(R/Re)^(1/n) − 1]};  μ(R) = μe + (2,5 b_n / ln 10)[(R/Re)^(1/n) − 1]
   b_n ≈ 2n − 1/3 + 4/(405n) + 46/(25515n²)  (Ciotti & Bertin 1999). */
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
  var _cx = document.createElement('canvas').getContext('2d');
  function rgb(c) {
    _cx.fillStyle = '#000'; _cx.fillStyle = c;
    var s = String(_cx.fillStyle);
    if (s.charAt(0) === '#') return [parseInt(s.substr(1, 2), 16), parseInt(s.substr(3, 2), 16), parseInt(s.substr(5, 2), 16)];
    var m = s.match(/[\d.]+/g) || [0, 0, 0];
    return [+m[0], +m[1], +m[2]];
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
      ctx.translate(p.x - 36, p.y + p.h / 2); ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; ctx.fillText(yl, 0, 0);
    }
    ctx.restore();
  }

  // ---------- física ----------
  function bn(n) { return 2 * n - 1 / 3 + 4 / (405 * n) + 46 / (25515 * n * n); }
  function mu(R, n, Re, mue) {
    return mue + 2.5 * bn(n) / Math.LN10 * (Math.pow(R / Re, 1 / n) - 1);
  }
  // ln Γ(z) por Lanczos (z > 0)
  function lnGamma(z) {
    var g = 7, C = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313,
      -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
    if (z < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * z)) - lnGamma(1 - z);
    z -= 1;
    var x = C[0];
    for (var i = 1; i < g + 2; i++) x += C[i] / (z + i);
    var t = z + g + 0.5;
    return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
  }
  // magnitude total (isofotas circulares): L = 2π n Re² Ie e^{b} Γ(2n) / b^{2n}
  function mTotal(n, Re, mue) {
    var b = bn(n);
    var lnF = Math.log(2 * Math.PI * n * Re * Re) + b + lnGamma(2 * n) - 2 * n * Math.log(b);
    return mue - 2.5 * lnF / Math.LN10;
  }

  var RMAX = 40;                    // arcsec (eixo e campo da imagem: ±RMAX)
  var MU_TOP = 14, MU_BOT = 30;     // faixa de μ no gráfico (mag/arcsec²)
  var MU_CLARO = 15, MU_ESCURO = 27; // faixa de μ mapeada na imagem
  var NIMG = 128;

  AGA.widgets['perfil-sersic'] = function (root) {
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Perfil de Sérsic');
    el('p', 'w-caption', hd,
      'I(R) = I<sub>e</sub> exp{−b<sub>n</sub> [(R/R<sub>e</sub>)<sup>1/n</sup> − 1]}, em magnitudes: ' +
      'μ(R) = μ<sub>e</sub> + (2,5 b<sub>n</sub> / ln 10) [(R/R<sub>e</sub>)<sup>1/n</sup> − 1], com ' +
      'b<sub>n</sub> ≈ 2n − 1/3 + 4/(405n) + 46/(25515n²), escolhido para que R<sub>e</sub> contenha metade da luz. ' +
      'n = 1: disco exponencial (reta em μ × R); n = 4: de Vaucouleurs (reta em μ × R<sup>1/4</sup>). ' +
      'Brilho maior para cima. A imagem ao lado é sintética, em escala logarítmica (μ de 15 a 27 mag/arcsec²), com isofotas circulares.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Perfil de brilho superficial de Sérsic e imagem sintética da galáxia');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null, quarta = false;

    var gn = slider(ctl, 'Índice n', 0.5, 8, 0.05, 4, function (v) { return fmt(v, 2); }, draw);
    var gR = slider(ctl, 'Rₑ (raio efetivo)', 1, 15, 0.1, 6, function (v) { return fmt(v, 1) + '″'; }, draw);
    var gm = slider(ctl, 'μₑ', 18, 24, 0.05, 21, function (v) { return fmt(v, 2) + ' mag/arcsec²'; }, draw);
    var bx = el('button', 'w-btn', ctl);
    bx.type = 'button';
    bx.textContent = 'Eixo: R → R^(1/4)';
    bx.addEventListener('click', function () {
      quarta = !quarta;
      bx.textContent = quarta ? 'Eixo: R^(1/4) → R' : 'Eixo: R → R^(1/4)';
      draw();
    });
    // imagem fora da tela (recalculada quando os parâmetros mudam)
    var off = document.createElement('canvas');
    off.width = NIMG; off.height = NIMG;
    var octx = off.getContext('2d'), img = octx.createImageData(NIMG, NIMG), chave = '';

    function layout(W, H) {
      if (W >= 560) return { graf: { x: 0, y: 0, w: W * 0.6, h: H }, img: { x: W * 0.6, y: 0, w: W * 0.4, h: H } };
      var h1 = Math.round(H * 0.56);
      return { graf: { x: 0, y: 0, w: W, h: h1 }, img: { x: 0, y: h1, w: W, h: H - h1 } };
    }

    // mapa de cores: fundo → azul → ciano → cor de estrela
    function rampa(c) {
      var st = [[0, rgb(c.bg)], [0.35, rgb(c.accent)], [0.7, rgb(c.accent2)], [1, rgb(c.star)]];
      var tab = new Uint8ClampedArray(256 * 3);
      for (var k = 0; k < 256; k++) {
        var t = k / 255, j = 0;
        while (j < st.length - 2 && t > st[j + 1][0]) j++;
        var u = (t - st[j][0]) / (st[j + 1][0] - st[j][0]);
        for (var ch = 0; ch < 3; ch++) tab[k * 3 + ch] = st[j][1][ch] + (st[j + 1][1][ch] - st[j][1][ch]) * u;
      }
      return tab;
    }

    function geraImagem(c, n, Re, mue) {
      var tab = rampa(c), d = img.data, b = bn(n), kfac = 2.5 * b / Math.LN10;
      for (var y = 0; y < NIMG; y++) {
        for (var x = 0; x < NIMG; x++) {
          var X = ((x + 0.5) / NIMG * 2 - 1) * RMAX, Y = ((y + 0.5) / NIMG * 2 - 1) * RMAX;
          var R = Math.sqrt(X * X + Y * Y);
          var m = mue + kfac * (Math.pow(R / Re, 1 / n) - 1);
          var v = clamp((MU_ESCURO - m) / (MU_ESCURO - MU_CLARO), 0, 1);
          var idx = Math.round(Math.pow(v, 0.9) * 255) * 3, o = (y * NIMG + x) * 4;
          d[o] = tab[idx]; d[o + 1] = tab[idx + 1]; d[o + 2] = tab[idx + 2]; d[o + 3] = 255;
        }
      }
      octx.putImageData(img, 0, 0);
    }

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var n = gn(), Re = gR(), mue = gm(), b = bn(n);
      var mu0 = mue - 2.5 * b / Math.LN10;
      var L = layout(W, H);

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      // ----- gráfico μ(R) -----
      var umax = quarta ? Math.pow(RMAX, 0.25) : RMAX;
      var q = painel(L.graf, [28, 16, 38, 54], [0, umax], [MU_BOT, MU_TOP]);
      var xt = quarta
        ? [[0, '0'], [0.5, '0,5'], [1, '1'], [1.5, '1,5'], [2, '2'], [2.5, '2,5']]
        : [[0, '0'], [10, '10'], [20, '20'], [30, '30'], [40, '40']];
      var yt = [];
      for (var mm = 16; mm <= 30; mm += 2) yt.push([mm, String(mm)]);
      eixos(ctx, q, c, ff, xt, yt, quarta ? 'R^(1/4)  (R em arcsec)' : 'R (arcsec)', 'μ (mag/arcsec²)');
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('Brilho superficial μ(R)', q.x, q.y - 8);

      function curva(nn, cor, larg, tracejado) {
        ctx.save();
        ctx.beginPath(); ctx.rect(q.x, q.y, q.w, q.h); ctx.clip();
        ctx.strokeStyle = cor; ctx.lineWidth = larg; ctx.setLineDash(tracejado ? [6, 5] : []);
        ctx.beginPath();
        for (var k = 0; k <= 300; k++) {
          var u = umax * k / 300, R = quarta ? Math.pow(u, 4) : u;
          var Y = q.Y(clamp(mu(R, nn, Re, mue), MU_TOP - 5, MU_BOT + 5));
          if (k) ctx.lineTo(q.X(u), Y); else ctx.moveTo(q.X(u), Y);
        }
        ctx.stroke();
        ctx.restore();
        // rótulo no fim da curva
        var yEnd = q.Y(clamp(mu(RMAX, nn, Re, mue), MU_TOP, MU_BOT));
        return yEnd;
      }
      ctx.globalAlpha = 0.7;
      var y1 = curva(1, c.muted, 1.4, true);
      var y4 = curva(4, c.warm, 1.4, true);
      ctx.globalAlpha = 1;
      curva(n, c.accent2, 2.6, false);
      ctx.font = '10.5px ' + ff; ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      if (Math.abs(y1 - y4) < 12) { y1 -= 6; y4 += 6; }
      ctx.fillStyle = c.muted; ctx.fillText('n = 1', q.x + q.w - 4, clamp(y1 - 8, q.y + 8, q.y + q.h - 8));
      ctx.fillStyle = c.warm; ctx.fillText('n = 4', q.x + q.w - 4, clamp(y4 + 8, q.y + 8, q.y + q.h - 8));
      // ponto (Re, μe)
      var pxe = q.X(quarta ? Math.pow(Re, 0.25) : Re), pye = q.Y(mue);
      ctx.setLineDash([3, 3]); ctx.strokeStyle = c.ink; ctx.globalAlpha = 0.5; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(pxe, q.y + q.h); ctx.lineTo(pxe, pye); ctx.lineTo(q.x, pye); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;
      ctx.fillStyle = c.accent2;
      ctx.beginPath(); ctx.arc(pxe, pye, 5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.bg; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = c.ink; ctx.font = '11px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('(Rₑ, μₑ)', pxe + 7, pye + 4);
      if (mu0 < MU_TOP) {
        ctx.fillStyle = c.muted; ctx.font = '10.5px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        ctx.fillText('↑ μ₀ = ' + fmt(mu0, 1) + ' (fora da escala)', q.x + 6, q.y + 4);
      }

      // ----- imagem sintética -----
      var key = n + '|' + Re + '|' + mue + '|' + c.bg + c.accent + c.accent2 + c.star;
      if (key !== chave) { chave = key; geraImagem(c, n, Re, mue); }
      var r = L.img;
      var lado = Math.min(r.w - 24, r.h - 44);
      var ix = r.x + (r.w - lado) / 2, iy = r.y + 26 + (r.h - 44 - lado) / 2;
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      ctx.fillText('Imagem sintética (escala log)', r.x + r.w / 2, iy - 6);
      ctx.imageSmoothingEnabled = true;
      ctx.drawImage(off, ix, iy, lado, lado);
      ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.6; ctx.lineWidth = 1;
      ctx.strokeRect(ix + 0.5, iy + 0.5, lado - 1, lado - 1);
      ctx.globalAlpha = 1;
      // círculo de Re e barra de escala
      var pxPorAs = lado / (2 * RMAX);
      ctx.save(); ctx.beginPath(); ctx.rect(ix, iy, lado, lado); ctx.clip();
      ctx.setLineDash([4, 4]); ctx.strokeStyle = c.warm; ctx.lineWidth = 1.3;
      ctx.beginPath(); ctx.arc(ix + lado / 2, iy + lado / 2, Re * pxPorAs, 0, 2 * Math.PI); ctx.stroke();
      ctx.restore();
      ctx.setLineDash([]);
      ctx.fillStyle = c.warm; ctx.font = '11px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('Rₑ', ix + lado / 2 + Re * pxPorAs * 0.72 + 3, iy + lado / 2 + Re * pxPorAs * 0.72);
      var sb = 10 * pxPorAs, sx = ix + 8, sy = iy + lado - 10;
      ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(sx + sb, sy); ctx.stroke();
      ctx.fillStyle = c.ink; ctx.textBaseline = 'bottom';
      ctx.fillText('10″', sx, sy - 3);

      var mt = mTotal(n, Re, mue);
      ro.innerHTML =
        '<div>n = <b>' + fmt(n, 2) + '</b> ⇒ b<sub>n</sub> = <b>' + fmt(b, 3) + '</b>; I<sub>0</sub>/I<sub>e</sub> = e<sup>b<sub>n</sub></sup> = ' +
        Number(Math.exp(b).toPrecision(3)).toLocaleString('pt-BR') + '</div>' +
        '<div>μ<sub>0</sub> = μ<sub>e</sub> − 2,5 b<sub>n</sub>/ln 10 = <b>' + fmt(mu0, 2) + ' mag/arcsec²</b> (centro)</div>' +
        '<div>Magnitude total (isofotas circulares): m = μ<sub>e</sub> − 2,5 log[2π n R<sub>e</sub>² e<sup>b<sub>n</sub></sup> Γ(2n)/b<sub>n</sub><sup>2n</sup>] = <b>' + fmt(mt, 2) + ' mag</b></div>' +
        (Math.abs(n - 1) < 0.03 ? '<div>n ≈ 1: perfil exponencial de disco.</div>' : '') +
        (Math.abs(n - 4) < 0.03 ? '<div>n ≈ 4: perfil de de Vaucouleurs (b₄ ≈ 7,67), típico de elípticas e bojos clássicos.</div>' : '');
    }

    cv = canvasResponsivo(root, canvas, function (w) {
      return w >= 560 ? clamp(w * 0.5, 260, 460) : clamp(w * 1.2, 260, 460);
    }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
  };
})();
