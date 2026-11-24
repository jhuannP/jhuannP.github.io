/* Widget: módulo de distância com extinção (AGA0299, Caps. 1–2)
   d = 10^((m − M − A + 5)/5) pc, régua logarítmica de 1 pc a 100 Mpc. */
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
  // cores do tema (lidas a cada redesenho)
  function cores() {
    var cs = getComputedStyle(document.documentElement);
    function g(n, f) { var v = cs.getPropertyValue(n).trim(); return v || f; }
    return {
      bg: g('--w-bg', '#0b1530'), ink: g('--w-ink', '#e8eefc'), muted: g('--w-muted', '#8796b8'),
      accent: g('--w-accent', '#4d8bff'), accent2: g('--w-accent-2', '#5fd4ff'),
      warm: g('--w-warm', '#ff9f43'), star: g('--w-star', '#fff6e0')
    };
  }
  // número com vírgula decimal e sinal de menos tipográfico
  function fmt(x, d) {
    if (!isFinite(x)) return '—';
    var s = Math.abs(x).toFixed(d).replace('.', ',');
    return (x < 0 && /[1-9]/.test(s) ? '−' : '') + s;
  }
  // 3 algarismos significativos em pt-BR
  function sig(x) {
    return Number(x.toPrecision(3)).toLocaleString('pt-BR', { maximumSignificantDigits: 3 });
  }
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
  // canvas que acompanha a largura do root, com devicePixelRatio
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
  // redesenha quando o tema claro/escuro muda
  function observaTema(cb) {
    try {
      var mo = new MutationObserver(cb);
      mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme', 'style'] });
      if (document.body) mo.observe(document.body, { attributes: true, attributeFilter: ['class', 'data-theme'] });
      if (window.matchMedia) {
        var mq = window.matchMedia('(prefers-color-scheme: dark)');
        if (mq.addEventListener) mq.addEventListener('change', cb); else if (mq.addListener) mq.addListener(cb);
      }
    } catch (e) { /* sem suporte: ignora */ }
  }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }

  // distância formatada na unidade mais natural
  function fmtDist(d) {
    if (d < 1e3) return sig(d) + ' pc';
    if (d < 1e6) return sig(d / 1e3) + ' kpc';
    return sig(d / 1e6) + ' Mpc';
  }

  // objetos de referência (distâncias aproximadas)
  var REFS = [
    { nome: 'α Cen', d: 1.3, txt: '1,3 pc', lado: -1, nivel: 0 },
    { nome: 'Centro Gal.', d: 8e3, txt: '~8 kpc', lado: -1, nivel: 0 },
    { nome: 'LMC', d: 5e4, txt: '50 kpc', lado: 1, nivel: 0 },
    { nome: 'M31', d: 7.7e5, txt: '~770 kpc', lado: -1, nivel: 1 },
    { nome: 'Virgo', d: 1.6e7, txt: '~16 Mpc', lado: 1, nivel: 1 }
  ];
  var DECADAS = ['1 pc', '10 pc', '100 pc', '1 kpc', '10 kpc', '100 kpc', '1 Mpc', '10 Mpc', '100 Mpc'];

  AGA.widgets['modulo-distancia'] = function (root) {
    root.innerHTML = '';
    var hd = el('div', 'w-head', root);
    el('h4', 'w-title', hd, 'Módulo de distância e extinção');
    el('p', 'w-caption', hd,
      'm − M = 5 log₁₀(d / 10 pc) + A &nbsp;⇒&nbsp; d = 10<sup>(m − M − A + 5)/5</sup> pc. ' +
      'A extinção A (mag) apaga a luz; se for ignorada, o objeto parece mais distante por um fator 10<sup>A/5</sup>. ' +
      'Régua logarítmica de 1 pc a 100 Mpc; distâncias de referência aproximadas.');
    var canvas = el('canvas', 'w-canvas', root);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Régua logarítmica de distâncias com o ponto calculado');
    var ctl = el('div', 'w-controls', root);
    var ro = el('div', 'w-readout', root);
    var cv = null;

    var gm = slider(ctl, 'm (aparente)', -2, 26, 0.1, 15, function (v) { return fmt(v, 1) + ' mag'; }, draw);
    var gM = slider(ctl, 'M (absoluta)', -10, 16, 0.1, -3, function (v) { return fmt(v, 1) + ' mag'; }, draw);
    var gA = slider(ctl, 'A (extinção)', 0, 5, 0.05, 1, function (v) { return fmt(v, 2) + ' mag'; }, draw);

    function draw() {
      if (!cv) return;
      var c = cores(), ctx = cv.ctx, W = cv.w, H = cv.h;
      var ff = getComputedStyle(root).fontFamily || 'system-ui, sans-serif';
      var m = gm(), M = gM(), A = gA();
      var mu = m - M;                 // módulo de distância aparente
      var mu0 = mu - A;               // módulo corrigido de extinção
      var d = Math.pow(10, (mu0 + 5) / 5);
      var d0 = Math.pow(10, (mu + 5) / 5);   // ignorando A
      var fator = Math.pow(10, A / 5);

      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      var pad = Math.max(18, W * 0.05), x0 = pad, x1 = W - pad;
      var yR = Math.round(H * 0.52);
      function X(dd) { return x0 + (Math.log(dd) / Math.LN10 / 8) * (x1 - x0); }

      // título dentro do canvas
      ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillStyle = c.ink; ctx.font = '600 ' + (W < 480 ? 16 : 20) + 'px ' + ff;
      ctx.fillText('d = ' + fmtDist(d), pad, 12);
      ctx.font = '12px ' + ff; ctx.fillStyle = c.warm;
      ctx.fillText('ignorando A: ' + fmtDist(d0) + '  (×' + sig(fator) + ')', pad, 12 + (W < 480 ? 22 : 27));

      // barra da régua
      var gr = ctx.createLinearGradient(x0, 0, x1, 0);
      gr.addColorStop(0, c.accent2); gr.addColorStop(1, c.accent);
      ctx.globalAlpha = 0.35; ctx.fillStyle = gr;
      ctx.fillRect(x0, yR - 3, x1 - x0, 6);
      ctx.globalAlpha = 1;

      // marcas de década e intermediárias
      ctx.strokeStyle = c.muted; ctx.lineWidth = 1;
      ctx.beginPath();
      for (var k = 0; k <= 8; k++) {
        var xk = Math.round(X(Math.pow(10, k))) + 0.5;
        ctx.moveTo(xk, yR - 9); ctx.lineTo(xk, yR + 9);
        if (k < 8) for (var j = 2; j <= 9; j++) {
          var xj = Math.round(X(j * Math.pow(10, k))) + 0.5;
          ctx.moveTo(xj, yR - 3); ctx.lineTo(xj, yR + 3);
        }
      }
      ctx.stroke();
      ctx.fillStyle = c.muted; ctx.font = '11px ' + ff; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (k = 0; k <= 8; k++) {
        if (W < 520 && k % 2) continue;
        var dw = ctx.measureText(DECADAS[k]).width / 2 + 2;
        ctx.fillText(DECADAS[k], clamp(X(Math.pow(10, k)), dw, W - dw), yR + 12);
      }

      // objetos de referência (acima ou abaixo da régua)
      REFS.forEach(function (r) {
        var x = X(r.d);
        var yT = r.lado < 0 ? yR - 34 - r.nivel * 20 : yR + 34 + r.nivel * 18;
        ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.7;
        ctx.beginPath(); ctx.moveTo(x, yR + r.lado * 5); ctx.lineTo(x, r.lado < 0 ? yT + 4 : yT - 2); ctx.stroke();
        ctx.globalAlpha = 1;
        ctx.fillStyle = c.star;
        ctx.beginPath(); ctx.arc(x, yR, 3, 0, 2 * Math.PI); ctx.fill();
        ctx.font = '11.5px ' + ff;
        var t = r.nome + ' (' + r.txt + ')';
        var tw = ctx.measureText(t).width;
        var tx = clamp(x - tw / 2, 2, W - 2 - tw);
        ctx.textAlign = 'left'; ctx.textBaseline = r.lado < 0 ? 'bottom' : 'top';
        ctx.fillStyle = c.ink;
        ctx.fillText(t, tx, yT);
      });

      // pontos calculados (com e sem extinção)
      var LMIN = 1, LMAX = 1e8;
      function marca(dd, cor, cheio) {
        var fora = dd < LMIN ? -1 : dd > LMAX ? 1 : 0;
        var x = X(clamp(dd, LMIN, LMAX));
        ctx.save();
        if (fora) {
          ctx.fillStyle = cor;
          ctx.beginPath();
          ctx.moveTo(x + fora * 10, yR); ctx.lineTo(x, yR - 7); ctx.lineTo(x, yR + 7); ctx.closePath();
          ctx.fill();
        } else {
          var g = ctx.createRadialGradient(x, yR, 0, x, yR, 16);
          g.addColorStop(0, cor); g.addColorStop(1, 'rgba(0,0,0,0)');
          ctx.globalAlpha = 0.45; ctx.fillStyle = g;
          ctx.beginPath(); ctx.arc(x, yR, 16, 0, 2 * Math.PI); ctx.fill();
          ctx.globalAlpha = 1;
          ctx.beginPath(); ctx.arc(x, yR, 6, 0, 2 * Math.PI);
          if (cheio) { ctx.fillStyle = cor; ctx.fill(); }
          ctx.lineWidth = 2; ctx.strokeStyle = cor; ctx.stroke();
        }
        ctx.restore();
        return x;
      }
      var xa = marca(d0, c.warm, false);
      var xd = marca(d, c.accent2, true);

      // seta do erro cometido ao ignorar A
      var yS = H - 34;
      ctx.strokeStyle = c.muted; ctx.globalAlpha = 0.5; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(xd, yR + 8); ctx.lineTo(xd, yS); ctx.moveTo(xa, yR + 8); ctx.lineTo(xa, yS); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = 1;
      if (Math.abs(xa - xd) > 4) {
        ctx.strokeStyle = c.warm; ctx.fillStyle = c.warm; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(xd, yS); ctx.lineTo(xa, yS); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(xa, yS); ctx.lineTo(xa - 7, yS - 4); ctx.lineTo(xa - 7, yS + 4); ctx.closePath(); ctx.fill();
      }
      ctx.font = '11.5px ' + ff; ctx.textBaseline = 'top';
      var rot = A > 0 ? 'erro ao ignorar A: ×' + sig(fator) : 'sem extinção';
      var rw = ctx.measureText(rot).width;
      ctx.textAlign = 'left';
      ctx.fillText(rot, clamp((xa + xd) / 2 - rw / 2, 2, W - 2 - rw), yS + 6);
      ctx.fillStyle = c.accent2; ctx.textBaseline = 'bottom';
      var lw = ctx.measureText('d').width;
      ctx.fillText('d', clamp(xd - lw - 4, 2, W - 10), yS - 3);

      // leitura numérica
      ro.innerHTML =
        '<div>μ = m − M = <b>' + fmt(mu, 2) + '</b> mag; μ₀ = m − M − A = <b>' + fmt(mu0, 2) + '</b> mag</div>' +
        '<div>d = <b>' + sig(d) + ' pc</b> = ' + sig(d / 1e3) + ' kpc = ' + sig(d / 1e6) + ' Mpc</div>' +
        '<div>Ignorando A: d = ' + fmtDist(d0) + ' — superestimada por ×' + sig(fator) +
        ' (+' + sig((fator - 1) * 100) + ' %)</div>';
    }

    cv = canvasResponsivo(root, canvas, function (w) { return clamp(w * 0.42, 260, 460); }, draw);
    cv.ajusta();
    draw();
    observaTema(draw);
  };
})();
