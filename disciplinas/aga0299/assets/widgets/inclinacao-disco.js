/* Widget: inclinação de um disco galáctico (AGA0299, Cap. 3)
   Disco fino: b/a = cos i. Com espessura intrínseca q0 (esferoide oblato):
   q² = cos²i (1 − q0²) + q0²  ⇔  cos²i = (q² − q0²)/(1 − q0²). */
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

  // ---------- galáxia procedural (unidades: raio do disco = 1) ----------
  // tipo: 0 = bojo, 1 = disco velho, 2 = braço (estrelas jovens), 3 = região HII
  function geraGalaxia() {
    var rnd = mulberry32(2024), S = [];
    var pitch = 14 * RAD, k = 1 / Math.tan(pitch), r0 = 0.12;
    function zu() { return rnd() + rnd() - 1; }          // distribuição triangular em [−1, 1]
    var n, r, th;
    // bojo esferoidal
    for (n = 0; n < 380; n++) {
      var x = gauss(rnd) * 0.085, y = gauss(rnd) * 0.085, z = gauss(rnd) * 0.07;
      S.push({ r: Math.sqrt(x * x + y * y), th: Math.atan2(y, x), z: z, zu: 0, tipo: 0, s: 0.9 + rnd() * 0.8, a: 0.35 + rnd() * 0.5 });
    }
    // disco: estrelas entre os braços
    for (n = 0; n < 1100; n++) {
      do { r = -Math.log(1 - rnd()) * 0.33; } while (r > 1 || r < 0.05);
      S.push({ r: r, th: rnd() * 2 * Math.PI, z: 0, zu: zu(), tipo: 1, s: 0.8 + rnd() * 0.7, a: 0.25 + rnd() * 0.4 });
    }
    // braços espirais logarítmicos (2 braços)
    for (n = 0; n < 1500; n++) {
      do { r = r0 + (-Math.log(1 - rnd()) * 0.38); } while (r > 1);
      th = (n % 2) * Math.PI + k * Math.log(r / r0) + gauss(rnd) * 0.2;
      S.push({ r: r * (1 + gauss(rnd) * 0.03), th: th, z: 0, zu: zu() * 0.6, tipo: 2, s: 0.9 + rnd() * 0.9, a: 0.35 + rnd() * 0.55 });
    }
    // regiões HII ao longo dos braços
    for (n = 0; n < 70; n++) {
      do { r = 0.25 + rnd() * 0.7; } while (r > 1);
      th = (n % 2) * Math.PI + k * Math.log(r / r0) + gauss(rnd) * 0.1;
      S.push({ r: r, th: th, z: 0, zu: zu() * 0.3, tipo: 3, s: 1.8 + rnd() * 1.6, a: 0.5 + rnd() * 0.4 });
    }
    return S;
  }
  var GAL = null;

  AGA.widgets['inclinacao-disco'] = function (root) {
    if (!GAL) GAL = geraGalaxia();
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Inclinação de um disco galáctico');
    el('p', 'w-caption', hd,
      'Disco circular visto com inclinação i (0° = de frente, 90° = de perfil). Disco infinitamente fino: q = b/a = cos i. ' +
      'Com espessura intrínseca q₀ (esferoide oblato): q² = cos²i (1 − q₀²) + q₀², ou seja, cos²i = (q² − q₀²)/(1 − q₀²). ' +
      'Para espirais usa-se tipicamente q₀ ≈ 0,1–0,2. A galáxia (braços logarítmicos, bojo, regiões HII) é procedural e ilustrativa.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Disco espiral girando, visto com a inclinação escolhida');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null, giro = 0;

    var gi = slider(ctl, 'Inclinação i', 0, 90, 0.5, 55, function (v) { return fmt(v, 1) + '°'; }, draw);
    var gq0 = slider(ctl, 'Espessura q₀', 0, 0.3, 0.005, 0.15, function (v) { return fmt(v, 3); }, draw);
    var btn = el('button', 'w-btn', ctl);
    btn.type = 'button';

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var iDeg = gi(), q0 = gq0(), ci = Math.cos(iDeg * RAD), si = Math.sin(iDeg * RAD);
      var q = Math.sqrt(ci * ci * (1 - q0 * q0) + q0 * q0);       // b/a observado
      var iFino = Math.acos(clamp(q, 0, 1)) / RAD;                  // supondo disco fino
      var iCorr = Math.acos(Math.sqrt(clamp((q * q - q0 * q0) / (1 - q0 * q0), 0, 1))) / RAD;
      var cS = rgb(c.star), cA = rgb(c.accent2), cW = rgb(c.warm);

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      var cx = W * 0.43, cy = H * 0.52;
      var s = Math.min(W * 0.36, H * 0.42);

      // brilho difuso do disco e do bojo
      ctx.save(); ctx.translate(cx, cy); ctx.scale(1, Math.max(q, 0.02));
      var gd = ctx.createRadialGradient(0, 0, 0, 0, 0, s * 1.02);
      gd.addColorStop(0, mix(cS, cA, 0.3, 0.32)); gd.addColorStop(0.5, mix(cS, cA, 0.6, 0.1)); gd.addColorStop(1, mix(cS, cA, 1, 0));
      ctx.fillStyle = gd; ctx.beginPath(); ctx.arc(0, 0, s * 1.02, 0, 2 * Math.PI); ctx.fill();
      ctx.restore();
      var gb = ctx.createRadialGradient(cx, cy, 0, cx, cy, s * 0.26);
      gb.addColorStop(0, mix(cS, [255, 255, 255], 0.4, 0.85)); gb.addColorStop(1, mix(cS, cS, 0, 0));
      ctx.fillStyle = gb; ctx.beginPath(); ctx.arc(cx, cy, s * 0.26, 0, 2 * Math.PI); ctx.fill();

      // estrelas: rotação no plano (giro) + inclinação em torno do eixo x da tela
      var corT = [c.star, mix(cS, cA, 0.35), mix(cA, cS, 0.25), mix(cW, [255, 120, 160], 0.35)];
      for (var k = 0; k < GAL.length; k++) {
        var e = GAL[k];
        var th = e.th + giro * (e.tipo === 0 ? 0.6 : 1);
        var x = e.r * Math.cos(th), y = e.r * Math.sin(th);
        var z = e.tipo === 0 ? e.z : q0 * Math.sqrt(Math.max(0, 1 - e.r * e.r)) * e.zu;
        var X = cx + s * x;
        var Y = cy - s * (y * ci - z * si);
        ctx.globalAlpha = e.a;
        ctx.fillStyle = corT[e.tipo];
        var sz = e.s;
        if (e.tipo === 3) {
          ctx.globalAlpha = e.a * 0.55;
          ctx.beginPath(); ctx.arc(X, Y, sz, 0, 2 * Math.PI); ctx.fill();
        } else ctx.fillRect(X - sz / 2, Y - sz / 2, sz, sz);
      }
      ctx.globalAlpha = 1;

      // faixa de poeira quando quase de perfil
      if (iDeg > 60 && q0 > 0.005) {
        var al = Math.pow((iDeg - 60) / 30, 2) * clamp(q0 / 0.05, 0, 1) * 0.75;
        // elipse escura achatada, levemente deslocada para o lado próximo do disco
        ctx.save(); ctx.translate(cx, cy - s * 0.04 * ci); ctx.scale(1, Math.max(0.004, q0 * 0.3 + 0.06 * ci));
        var gl = ctx.createRadialGradient(0, 0, s * 0.2, 0, 0, s * 0.98);
        gl.addColorStop(0, c.bg); gl.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.globalAlpha = al; ctx.fillStyle = gl;
        ctx.beginPath(); ctx.arc(0, 0, s * 0.98, 0, 2 * Math.PI); ctx.fill();
        ctx.restore(); ctx.globalAlpha = 1;
      }

      // isofota externa ajustada (elipse a, b) e eixos
      var a = s * 1.03, bb = a * q;
      ctx.strokeStyle = c.accent; ctx.lineWidth = 1.5; ctx.setLineDash([6, 5]);
      ctx.beginPath(); ctx.ellipse(cx, cy, a, Math.max(bb, 0.5), 0, 0, 2 * Math.PI); ctx.stroke();
      ctx.setLineDash([]);
      ctx.strokeStyle = c.ink; ctx.globalAlpha = 0.65; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx - a, cy); ctx.lineTo(cx + a, cy); ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - bb); ctx.stroke();
      ctx.globalAlpha = 1;
      ctx.fillStyle = c.ink; ctx.font = '12px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      ctx.fillText('a', cx + a / 2, cy + 4);
      ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      if (bb > 12) ctx.fillText('b', cx + 5, cy - bb / 2);

      // ícone: geometria da visada (de lado)
      var bw = Math.min(110, W * 0.26), bh = Math.min(96, H * 0.3);
      var bx = W - bw - 10, by = 10, icx = bx + bw * 0.42, icy = by + bh * 0.56, L = Math.min(bw, bh) * 0.36;
      ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.5; ctx.lineWidth = 1;
      ctx.strokeRect(bx + 0.5, by + 0.5, bw, bh);
      ctx.globalAlpha = 1;
      ctx.fillStyle = c.muted; ctx.font = '10px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('vista de lado', bx + 5, by + 4);
      // linha de visada até o observador (à direita)
      ctx.strokeStyle = c.accent2; ctx.fillStyle = c.accent2;
      ctx.beginPath(); ctx.moveTo(icx, icy); ctx.lineTo(bx + bw - 6, icy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(bx + bw - 4, icy); ctx.lineTo(bx + bw - 10, icy - 4); ctx.lineTo(bx + bw - 10, icy + 4); ctx.closePath(); ctx.fill();
      ctx.font = '9.5px ' + ff; ctx.textAlign = 'right'; ctx.textBaseline = 'top';
      ctx.fillText('obs.', bx + bw - 4, icy + 5);
      // disco (segmento) e normal
      var dx = si, dy = -ci;                     // direção do disco na tela
      ctx.strokeStyle = c.star; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(icx - dx * L, icy - dy * L); ctx.lineTo(icx + dx * L, icy + dy * L); ctx.stroke();
      var nx = ci, ny = -si;                     // normal ao disco
      ctx.strokeStyle = c.warm; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(icx, icy); ctx.lineTo(icx + nx * L * 0.9, icy + ny * L * 0.9); ctx.stroke();
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(icx, icy, L * 0.45, -iDeg * RAD, 0); ctx.stroke();
      ctx.fillStyle = c.warm; ctx.font = '11px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
      var am = -iDeg * RAD / 2;
      ctx.fillText('i', icx + L * 0.6 * Math.cos(am) + 1, icy + L * 0.6 * Math.sin(am));

      // texto no canvas
      ctx.fillStyle = c.ink; ctx.font = '600 13px ' + ff; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
      ctx.fillText('q = b/a = ' + fmt(q, 3), 12, H - 12);

      ro.innerHTML =
        '<div>Inclinação real i = <b>' + fmt(iDeg, 1) + '°</b>, q₀ = ' + fmt(q0, 3) + ' ⇒ q = b/a observado = <b>' + fmt(q, 3) + '</b></div>' +
        '<div>i inferida supondo disco fino (cos i = q): <b>' + fmt(iFino, 1) + '°</b>' +
        (Math.abs(iFino - iDeg) > 0.05 ? ' (erro ' + fmt(iFino - iDeg, 1) + '°)' : '') + '</div>' +
        '<div>i inferida com q₀ = ' + fmt(q0, 3) + ': cos²i = (q² − q₀²)/(1 − q₀²) ⇒ <b>' + fmt(iCorr, 1) + '°</b></div>' +
        (q0 > 0 && iDeg > 85 ? '<div>Perto de 90°, q → q₀: pequenas incertezas em q ou q₀ geram grandes erros em i.</div>' : '');
    }

    cv = canvasResponsivo(root, canvas, function (w) { return clamp(w * 0.56, 260, 460); }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
    animacao(root, btn, function (dt) {
      giro += dt * 0.25;
      draw();
    });
  };
})();
