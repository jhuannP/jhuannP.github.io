/* Widget: extinção em função da latitude galáctica (AGA0299, Cap. 2)
   Camada fina plano-paralela de poeira: A(b) = A0 · csc b, A0 = 0,21 mag. */
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

  var A0 = 0.21;                       // extinção no polo (mag), valor dos slides
  var RAD = Math.PI / 180;
  function Ab(b) { return A0 / Math.sin(b * RAD); }

  AGA.widgets['extincao-latitude'] = function (root) {
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Extinção e latitude galáctica');
    el('p', 'w-caption', hd,
      'Modelo de camada fina plano-paralela de poeira, com o Sol no plano médio. Para um objeto fora da Galáxia, ' +
      'o caminho dentro da camada é h · csc b, logo A(b) = A₀ · csc b = A₀ / sen b, com A₀ ≈ 0,21 mag (extinção no polo, valor dos slides). ' +
      'Quando b → 0 o caminho diverge e A “explode”; na prática a poeira é irregular e o disco é finito, ' +
      'então o modelo só serve para |b| ≳ 10°. Os fótons animados perdem brilho segundo 10<sup>−0,4 A</sup>.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Camada de poeira atravessada pela linha de visada e gráfico de A contra b');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null, tFot = 0;

    var gb = slider(ctl, 'Latitude b', 2, 90, 0.5, 30, function (v) { return fmt(v, 1) + '°'; }, draw);
    var btn = el('button', 'w-btn', ctl);
    btn.type = 'button';

    // textura fixa: estrelas do disco e grãos de poeira (coordenadas normalizadas)
    var rnd = mulberry32(7), ESTR = [], POE = [];
    for (var k = 0; k < 140; k++) ESTR.push([rnd(), (rnd() + rnd() + rnd() - 1.5) / 1.5, 0.4 + rnd() * 0.6]);
    for (k = 0; k < 220; k++) POE.push([rnd(), rnd() * 2 - 1, rnd()]);

    function layout(W, H) {
      if (W >= 560) return { lado: { x: 0, y: 0, w: W * 0.52, h: H }, graf: { x: W * 0.52, y: 0, w: W * 0.48, h: H } };
      var h1 = Math.round(H * 0.47);
      return { lado: { x: 0, y: 0, w: W, h: h1 }, graf: { x: 0, y: h1, w: W, h: H - h1 } };
    }

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var b = gb(), sb = Math.sin(b * RAD), cb = Math.cos(b * RAD);
      var A = Ab(b), T = Math.pow(10, -0.4 * A);
      var L = layout(W, H);

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      // ----- vista lateral -----
      var r = L.lado;
      var yc = r.y + r.h * 0.7, hh = Math.max(10, r.h * 0.075);
      var xs = r.x + r.w * 0.12;
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('Vista lateral do disco', r.x + 12, r.y + 8);
      // estrelas do disco (mais espesso que a poeira)
      ctx.fillStyle = c.star;
      ESTR.forEach(function (e) {
        ctx.globalAlpha = 0.25 + 0.45 * e[2];
        ctx.fillRect(r.x + e[0] * r.w, yc + e[1] * hh * 2.4, 1.5, 1.5);
      });
      // camada de poeira
      var gp = ctx.createLinearGradient(0, yc - hh, 0, yc + hh);
      gp.addColorStop(0, 'rgba(0,0,0,0)');
      gp.addColorStop(0.5, c.warm);
      gp.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.globalAlpha = 0.28; ctx.fillStyle = gp;
      ctx.fillRect(r.x, yc - hh, r.w, 2 * hh);
      ctx.fillStyle = c.warm;
      POE.forEach(function (p) {
        ctx.globalAlpha = 0.15 + 0.35 * p[2] * (1 - Math.abs(p[1]));
        ctx.fillRect(r.x + p[0] * r.w, yc + p[1] * hh, 1.2, 1.2);
      });
      ctx.globalAlpha = 0.6; ctx.strokeStyle = c.warm; ctx.setLineDash([2, 4]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(r.x, yc - hh); ctx.lineTo(r.x + r.w, yc - hh); ctx.moveTo(r.x, yc + hh); ctx.lineTo(r.x + r.w, yc + hh); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;
      ctx.fillStyle = c.muted; ctx.font = '11px ' + ff; ctx.textAlign = 'right'; ctx.textBaseline = 'top';
      ctx.fillText('camada de poeira (espessura 2h)', r.x + r.w - 8, yc + hh + 6);
      // cota h
      var xh = r.x + r.w - 14;
      ctx.strokeStyle = c.muted; ctx.beginPath(); ctx.moveTo(xh, yc); ctx.lineTo(xh, yc - hh); ctx.stroke();
      ctx.textBaseline = 'middle'; ctx.fillText('h', xh - 4, yc - hh / 2);

      // linha de visada
      var t1 = hh / sb;                                     // saída da camada
      var tTop = (yc - (r.y + 34)) / sb;
      var tDir = (r.x + r.w - 8 - xs) / Math.max(cb, 1e-6);
      var tEnd = Math.min(tTop, tDir);
      var tin = Math.min(t1, tEnd);
      function P(t) { return [xs + t * cb, yc - t * sb]; }
      var pIn = P(tin), pEnd = P(tEnd);
      ctx.lineCap = 'round';
      if (tEnd > t1) {
        ctx.strokeStyle = c.accent2; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(pIn[0], pIn[1]); ctx.lineTo(pEnd[0], pEnd[1]); ctx.stroke();
        ctx.setLineDash([]);
      }
      ctx.strokeStyle = c.warm; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(xs, yc); ctx.lineTo(pIn[0], pIn[1]); ctx.stroke();
      ctx.lineCap = 'butt';
      // galáxia de fundo no fim da linha
      if (tEnd >= tTop - 0.5) {
        ctx.save(); ctx.translate(pEnd[0], pEnd[1] - 4); ctx.rotate(-0.4);
        var gg = ctx.createRadialGradient(0, 0, 0, 0, 0, 11);
        gg.addColorStop(0, c.star); gg.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.scale(1, 0.45); ctx.fillStyle = gg;
        ctx.beginPath(); ctx.arc(0, 0, 11, 0, 2 * Math.PI); ctx.fill();
        ctx.restore();
        ctx.fillStyle = c.muted; ctx.font = '11px ' + ff; ctx.textBaseline = 'bottom';
        ctx.textAlign = pEnd[0] > r.x + r.w * 0.7 ? 'right' : 'left';
        ctx.fillText('galáxia de fundo', pEnd[0] + (ctx.textAlign === 'right' ? -14 : 14), pEnd[1] - 2);
      } else {
        ctx.fillStyle = c.accent2; ctx.font = '12px ' + ff; ctx.textAlign = 'right'; ctx.textBaseline = 'bottom';
        ctx.fillText('→ ∞', r.x + r.w - 6, pEnd[1] - 4);
      }
      // fótons vindo da fonte até o Sol, perdendo brilho na camada
      ctx.fillStyle = c.star;
      for (var n = 0; n < 7; n++) {
        var sfr = (tFot + n / 7) % 1;
        var t = tEnd * (1 - sfr);
        var tr = t < t1 ? Math.pow(10, -0.4 * A0 * (t1 - t) / hh) : 1;
        var pp = P(t);
        ctx.globalAlpha = clamp(tr, 0.06, 1);
        ctx.beginPath(); ctx.arc(pp[0], pp[1], 2.6, 0, 2 * Math.PI); ctx.fill();
      }
      ctx.globalAlpha = 1;
      // ângulo b
      ctx.strokeStyle = c.ink; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(xs, yc, 30, -b * RAD, 0); ctx.stroke();
      ctx.fillStyle = c.ink; ctx.font = '12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      var am = -b * RAD / 2;
      ctx.fillText('b', xs + 36 * Math.cos(am), yc + 36 * Math.sin(am));
      // Sol
      ctx.fillStyle = c.warm;
      ctx.beginPath(); ctx.arc(xs, yc, 5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.bg; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = c.ink; ctx.font = '11px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      ctx.fillText('Sol', xs, yc + hh + 6);
      // rótulo do caminho na camada
      ctx.fillStyle = c.warm; ctx.font = '11.5px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      var lab = 'caminho = h·csc b = ' + sig(1 / sb) + ' h';
      ctx.fillText(lab, r.x + 12, r.y + 40);

      // ----- gráfico A × b -----
      var q = painel(L.graf, [28, 14, 38, 50], [0, 90], [0, 6.5]);
      eixos(ctx, q, c, ff,
        [[0, '0°'], [15, '15°'], [30, '30°'], [45, '45°'], [60, '60°'], [75, '75°'], [90, '90°']],
        [[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']],
        'latitude b', 'A (mag)');
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('A(b) = A₀ csc b', q.x, q.y - 8);
      // região onde o modelo é ruim
      ctx.fillStyle = c.warm; ctx.globalAlpha = 0.1;
      ctx.fillRect(q.X(0), q.y, q.X(10) - q.X(0), q.h);
      ctx.globalAlpha = 1;
      ctx.save(); ctx.translate(q.X(5), q.y + q.h - 6); ctx.rotate(-Math.PI / 2);
      ctx.fillStyle = c.warm; ctx.font = '10px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      ctx.fillText('modelo ruim', 0, 0);
      ctx.restore();
      // assíntota A0
      ctx.setLineDash([4, 4]); ctx.strokeStyle = c.muted; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(q.x, q.Y(A0)); ctx.lineTo(q.x + q.w, q.Y(A0)); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = c.muted; ctx.font = '10.5px ' + ff; ctx.textAlign = 'right'; ctx.textBaseline = 'bottom';
      ctx.fillText('A₀ = 0,21 mag (polo)', q.x + q.w - 4, q.Y(A0) - 3);
      // curva
      ctx.save(); ctx.beginPath(); ctx.rect(q.x, q.y, q.w, q.h); ctx.clip();
      ctx.strokeStyle = c.accent2; ctx.lineWidth = 2.2;
      ctx.beginPath();
      for (var bb = 2, first = true; bb <= 90.001; bb += 0.25) {
        var X = q.X(bb), Y = q.Y(Ab(bb));
        if (first) { ctx.moveTo(X, Y); first = false; } else ctx.lineTo(X, Y);
      }
      ctx.stroke();
      ctx.restore();
      // ponto atual
      var px = q.X(b), py = q.Y(Math.min(A, 6.5));
      ctx.setLineDash([3, 3]); ctx.strokeStyle = c.warm; ctx.globalAlpha = 0.7;
      ctx.beginPath(); ctx.moveTo(px, q.y + q.h); ctx.lineTo(px, py); ctx.lineTo(q.x, py); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;
      ctx.fillStyle = c.warm;
      ctx.beginPath(); ctx.arc(px, py, 5.5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.bg; ctx.lineWidth = 1.5; ctx.stroke();

      ro.innerHTML =
        '<div>b = <b>' + fmt(b, 1) + '°</b>, csc b = 1/sen b = ' + sig(1 / sb) + '</div>' +
        '<div>A(b) = 0,21 × ' + sig(1 / sb) + ' = <b>' + fmt(A, 2) + ' mag</b></div>' +
        '<div>Fração do fluxo transmitida: 10<sup>−0,4 A</sup> = <b>' + sig(100 * T) + ' %</b>' +
        (b < 10 ? ' — perto do plano o modelo é pouco confiável (poeira irregular, disco finito); use mapas de poeira' : '') + '</div>';
    }

    cv = canvasResponsivo(root, canvas, function (w) {
      return w >= 560 ? clamp(w * 0.5, 260, 460) : clamp(w * 1.05, 260, 460);
    }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
    animacao(root, btn, function (dt) {
      tFot = (tFot + dt * 0.12) % 1;
      draw();
    });
  };
})();
