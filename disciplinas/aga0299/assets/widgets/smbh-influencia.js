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
  // Buraco negro supermassivo: raio de Schwarzschild, raio de influência e resolução angular.
  var G_SI = 6.674e-11, C_SI = 2.998e8, MSOL = 1.989e30, UA = 1.496e11, PC = 3.0857e16;
  var G_PC = 4.301e-3;          // pc (km/s)² M☉⁻¹
  var ARCSEC = 206264.8;        // segundos de arco por radiano
  var RES_OA = 0.1, RES_HST = 0.05;   // resolução angular (″)
  var LOG_LO = -8, LOG_HI = 4;  // faixa da escala logarítmica (pc)

  window.AGA.widgets['smbh-influencia'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">Dá para ver a esfera de influência do buraco negro?</h4>' +
      '<p class="w-caption">Raio de Schwarzschild R<sub>s</sub> = 2GM/c²; raio de influência r<sub>inf</sub> = GM/σ² ' +
      '(onde o potencial do buraco negro domina sobre o das estrelas); tamanho angular θ = r<sub>inf</sub>/D. ' +
      'Critério simplificado: a dinâmica do buraco negro é mensurável se θ for maior que a resolução — ' +
      '0,1″ (infravermelho com óptica adaptativa) ou 0,05″ (HST). O desenho usa escala <b>logarítmica</b> nos raios.</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Esquema em escala logarítmica do raio de Schwarzschild, do raio de influência e da resolução angular, e painel com o tamanho aparente no céu.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    var redes = function () { desenhar(); };
    var sM = slider(ctrl, { nome: 'Massa M', min: 6, max: 10, step: 0.01, valor: 9, fmt: function (v) { return sci(Math.pow(10, v), 2) + ' M☉'; }, aoMudar: redes });
    var sS = slider(ctrl, { nome: 'Dispersão σ', min: 100, max: 400, step: 1, valor: 300, fmt: function (v) { return num(v, 0) + ' km/s'; }, aoMudar: redes });
    var sD = slider(ctrl, { nome: 'Distância D', min: 0, max: 2, step: 0.005, valor: 1, fmt: function (v) { return num(Math.pow(10, v), Math.pow(10, v) < 10 ? 2 : 1) + ' Mpc'; }, aoMudar: redes });
    botao(ctrl, 'Exemplo da prova (10⁹ M☉, 300 km/s, 10 Mpc)', function () { sM.set(9); sS.set(300); sD.set(1); desenhar(); });
    botao(ctrl, 'M pela relação M–σ', function () {
      // McConnell & Ma (2013): log(M/M☉) = 8,32 + 5,64 log(σ/200 km/s)
      sM.set(limitar(8.32 + 5.64 * Math.log10(sS.v() / 200), 6, 10)); desenhar();
    });

    var st = montarCanvas(root, canvas, function (w) { return limitar(w * 0.62, 280, 460); }, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    function calc() {
      var M = Math.pow(10, sM.v()), sig = sS.v(), Dmpc = Math.pow(10, sD.v()), Dpc = Dmpc * 1e6;
      var rsM = 2 * G_SI * M * MSOL / (C_SI * C_SI);
      var rs = { ua: rsM / UA, pc: rsM / PC };
      var rinf = G_PC * M / (sig * sig);           // pc
      var th = rinf / Dpc * ARCSEC;                 // ″
      return {
        M: M, sig: sig, Dmpc: Dmpc, Dpc: Dpc, rs: rs, rinf: rinf, th: th,
        thRs: rs.pc / Dpc * ARCSEC * 1e6,           // μas
        resOA: RES_OA / ARCSEC * Dpc, resHST: RES_HST / ARCSEC * Dpc   // tamanho físico do elemento de resolução (pc)
      };
    }

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores(), k = calc();
      // horizonte de eventos: preto (variável opcional --w-hole)
      var preto = getComputedStyle(document.documentElement).getPropertyValue('--w-hole').trim() || '#000';
      var pequeno = W < 480;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);

      var hRegua = 52, hTopo = H - hRegua;
      var lado = Math.min(hTopo, W * 0.58);
      var temCeu = W - lado >= 130;
      if (!temCeu) lado = Math.min(hTopo, W);

      /* --- esquema logarítmico: círculos concêntricos --- */
      var cx = temCeu ? lado / 2 + 4 : W / 2, cy = hTopo / 2 + 4;
      var Rmax = lado / 2 - 10;
      function raio(rpc) { return Rmax * limitar((Math.log10(rpc) - LOG_LO) / (LOG_HI - LOG_LO), 0, 1); }

      // décadas de referência
      ctx.lineWidth = 1;
      for (var d = LOG_LO + 1; d <= LOG_HI; d++) {
        ctx.strokeStyle = rgba(c.muted, d % 2 === 0 ? 0.22 : 0.1);
        ctx.beginPath(); ctx.arc(cx, cy, raio(Math.pow(10, d)), 0, 2 * Math.PI); ctx.stroke();
      }
      // esfera de influência (estrelas)
      var rI = raio(k.rinf);
      var gI = ctx.createRadialGradient(cx, cy, 0, cx, cy, Math.max(1, rI));
      gI.addColorStop(0, rgba(c.accent2, 0.05)); gI.addColorStop(1, rgba(c.accent2, 0.28));
      ctx.fillStyle = gI; ctx.beginPath(); ctx.arc(cx, cy, rI, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.accent2; ctx.lineWidth = 2; ctx.stroke();
      // elementos de resolução (tamanho físico na distância D)
      [[k.resHST, c.warm, [5, 4]], [k.resOA, c.star, [2, 4]]].forEach(function (q) {
        ctx.strokeStyle = q[1]; ctx.lineWidth = 1.6; ctx.setLineDash(q[2]);
        ctx.beginPath(); ctx.arc(cx, cy, raio(q[0]), 0, 2 * Math.PI); ctx.stroke();
      });
      ctx.setLineDash([]);
      // horizonte
      var rS = Math.max(2.5, raio(k.rs.pc));
      ctx.fillStyle = preto;
      ctx.beginPath(); ctx.arc(cx, cy, rS, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = c.warm; ctx.lineWidth = 1.5; ctx.stroke();

      fonte(ctx, root, pequeno ? 10 : 11, '600');
      ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillStyle = c.ink;
      ctx.fillText('Núcleo (escala log)', 8, 6);
      fonte(ctx, root, 10);
      ctx.fillStyle = c.muted;
      ctx.fillText('cada anel = ×10 em raio', 8, pequeno ? 20 : 22);

      /* --- painel do céu (escala linear em ″) --- */
      if (temCeu) {
        var x0 = lado + 12, pw = W - x0 - 8, ph = hTopo - 8;
        ctx.fillStyle = rgba(c.accent, 0.05); ctx.fillRect(x0, 4, pw, ph);
        ctx.strokeStyle = rgba(c.muted, 0.35); ctx.lineWidth = 1; ctx.strokeRect(x0 + 0.5, 4.5, pw - 1, ph - 1);
        var scx = x0 + pw / 2, scy = 4 + ph / 2 + 8;
        var meia = Math.max(k.th, RES_OA) * 1.25;          // meia-largura do campo (″)
        var pxs = (Math.min(pw, ph - 30) / 2) / meia;       // px por ″
        // disco de influência
        ctx.fillStyle = rgba(c.accent2, 0.25);
        ctx.beginPath(); ctx.arc(scx, scy, Math.max(0.8, k.th * pxs), 0, 2 * Math.PI); ctx.fill();
        ctx.strokeStyle = c.accent2; ctx.lineWidth = 2; ctx.stroke();
        // resoluções
        [[RES_HST, c.warm, [5, 4]], [RES_OA, c.star, [2, 4]]].forEach(function (q) {
          ctx.strokeStyle = q[1]; ctx.lineWidth = 1.6; ctx.setLineDash(q[2]);
          ctx.beginPath(); ctx.arc(scx, scy, q[0] * pxs, 0, 2 * Math.PI); ctx.stroke();
        });
        ctx.setLineDash([]);
        // barra de escala
        var barra = meia > 2 ? 1 : (meia > 0.5 ? 0.2 : 0.05);
        ctx.strokeStyle = c.ink; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(x0 + 10, 4 + ph - 12); ctx.lineTo(x0 + 10 + barra * pxs, 4 + ph - 12); ctx.stroke();
        fonte(ctx, root, 10);
        ctx.fillStyle = c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'bottom';
        ctx.fillText(num(barra, 2) + '″', x0 + 14 + barra * pxs, 4 + ph - 6);
        fonte(ctx, root, pequeno ? 10 : 11, '600');
        ctx.textBaseline = 'top';
        ctx.fillText('No céu (escala linear)', x0 + 8, 10);
        fonte(ctx, root, 10);
        [['— esfera de influência', c.accent2], ['- - HST 0,05″', c.warm], ['··· OA 0,1″', c.star]].forEach(function (q, i) {
          ctx.fillStyle = q[1]; ctx.fillText(q[0], x0 + 8, 26 + 13 * i);
        });
      }

      /* --- régua logarítmica --- */
      var rx0 = 14, rx1 = W - 14, ry = hTopo + 18;
      function RX(rpc) { return rx0 + (rx1 - rx0) * limitar((Math.log10(rpc) - LOG_LO) / (LOG_HI - LOG_LO), 0, 1); }
      ctx.strokeStyle = rgba(c.muted, 0.8); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(rx0, ry); ctx.lineTo(rx1, ry); ctx.stroke();
      fonte(ctx, root, 9);
      ctx.fillStyle = c.muted; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (var e = LOG_LO; e <= LOG_HI; e++) {
        var xx = RX(Math.pow(10, e));
        ctx.beginPath(); ctx.moveTo(xx, ry - 3); ctx.lineTo(xx, ry + 3); ctx.stroke();
        if (!pequeno || e % 2 === 0) ctx.fillText('10' + expo(e), xx, ry + 5);
      }
      ctx.textAlign = 'right';
      ctx.fillText('pc', rx1, ry + 19);
      var marcas = [[k.rs.pc, preto, c.warm, 'Rₛ'], [k.resHST, c.warm, null, '0,05″'], [k.resOA, c.star, null, '0,1″'], [k.rinf, c.accent2, null, 'r_inf']];
      fonte(ctx, root, 10, '600');
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      marcas.forEach(function (m, i) {
        var mx = RX(m[0]);
        ctx.fillStyle = m[1]; ctx.beginPath(); ctx.arc(mx, ry, 4.5, 0, 2 * Math.PI); ctx.fill();
        if (m[2]) { ctx.strokeStyle = m[2]; ctx.lineWidth = 1.5; ctx.stroke(); }
        ctx.fillStyle = m[2] || m[1];
        ctx.fillText(m[3], mx, ry - 6 - (i === 2 ? 10 : 0));
      });

      /* --- leituras --- */
      function veredito(res) {
        return k.th > res ? '<b>resolvível</b> (θ/res = ' + num(k.th / res, 1) + ')' : '<b>não resolvível</b> (θ/res = ' + num(k.th / res, 2) + ')';
      }
      readout.innerHTML =
        '<div>R<sub>s</sub> = 2GM/c² = <b>' + fmt(k.rs.ua, 2) + ' UA</b> = ' + sci(k.rs.pc, 2) + ' pc ' +
        '(no céu: ' + fmt(k.thRs, 2) + ' μas)</div>' +
        '<div>r<sub>inf</sub> = GM/σ² = <b>' + fmt(k.rinf, 2) + ' pc</b> &nbsp;·&nbsp; θ = r<sub>inf</sub>/D = <b>' + fmt(k.th, 3) + '″</b></div>' +
        '<div>Óptica adaptativa (0,1″ ↔ ' + fmt(k.resOA, 2) + ' pc em D): ' + veredito(RES_OA) +
        ' &nbsp;·&nbsp; HST (0,05″ ↔ ' + fmt(k.resHST, 2) + ' pc): ' + veredito(RES_HST) + '</div>' +
        '<div>G = 4,30 × 10⁻³ pc (km/s)² M☉⁻¹; 1 rad = 206 265″. r<sub>inf</sub>/R<sub>s</sub> = c²/(2σ²) ≈ ' + sci(k.rinf / k.rs.pc, 1) +
        ' — independe de M. A relação M–σ usada no botão: log(M/M☉) = 8,32 + 5,64 log(σ/200 km/s) (McConnell & Ma 2013).</div>';
    }
    desenhar();
  };
})();
