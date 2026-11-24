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
  // Faber–Jackson (L ∝ σ⁴) e Plano Fundamental das elípticas, com amostras sintéticas.
  var A_PF = 1.24, B_PF = 0.33, C_PF = -8.895;   // log Re[kpc] = 1,24 log σ + 0,33 ⟨μ⟩e − 8,895 (ilustrativo, Jørgensen et al. 1996)
  var LOGL0 = 10.3, SIG0 = 200;                  // L_V ≈ 2 × 10¹⁰ L☉ (σ/200 km/s)⁴ (normalização ilustrativa)

  function gerador(semente) {
    var s = semente;
    function u() { s = (s * 16807) % 2147483647; return s / 2147483647; }
    return {
      u: u,
      n: function () { // normal padrão (Box–Muller)
        var a = Math.max(1e-12, u()), b = u();
        return Math.sqrt(-2 * Math.log(a)) * Math.cos(2 * Math.PI * b);
      }
    };
  }

  // Amostra Faber–Jackson
  var FJ = (function () {
    var g = gerador(2024), pts = [];
    for (var i = 0; i < 160; i++) {
      var ls = 1.85 + 0.7 * Math.pow(g.u(), 0.8);
      pts.push({ x: ls, y: LOGL0 + 4 * (ls - Math.log10(SIG0)) + 0.22 * g.n() });
    }
    return pts;
  })();

  // Amostra do Plano Fundamental: (log σ, ⟨μ⟩e, log Re)
  var PF = (function () {
    var g = gerador(4242), pts = [];
    for (var i = 0; i < 220; i++) {
      var ls = 1.95 + 0.55 * g.u();
      var mu = 19.6 + 0.75 * g.n() + 1.2 * (ls - 2.2);
      var lr = A_PF * ls + B_PF * mu + C_PF + 0.07 * g.n();
      pts.push({ s: ls, m: mu, r: lr });
    }
    // padronização das variáveis para a projeção
    function est(k) {
      var m = 0, v = 0;
      pts.forEach(function (p) { m += p[k]; }); m /= pts.length;
      pts.forEach(function (p) { v += (p[k] - m) * (p[k] - m); }); v = Math.sqrt(v / pts.length);
      return { m: m, s: v };
    }
    var es = est('s'), em = est('m'), er = est('r');
    pts.forEach(function (p) { p.X = (p.s - es.m) / es.s; p.Y = (p.m - em.m) / em.s; });
    // ângulo em que o plano é visto exatamente de lado (gradiente do plano na direção horizontal)
    var thEdge = Math.atan2(B_PF * em.s, A_PF * es.s);
    return { pts: pts, es: es, em: em, er: er, thEdge: thEdge };
  })();

  function regressao(xs, ys) {
    var n = xs.length, mx = 0, my = 0, sxx = 0, sxy = 0, res = 0;
    for (var i = 0; i < n; i++) { mx += xs[i]; my += ys[i]; }
    mx /= n; my /= n;
    for (i = 0; i < n; i++) { sxx += (xs[i] - mx) * (xs[i] - mx); sxy += (xs[i] - mx) * (ys[i] - my); }
    var b = sxy / sxx, a = my - b * mx;
    for (i = 0; i < n; i++) { var d = ys[i] - (a + b * xs[i]); res += d * d; }
    return { a: a, b: b, rms: Math.sqrt(res / n) };
  }

  window.AGA.widgets['faber-jackson-plano'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">Faber–Jackson e o Plano Fundamental</h4>' +
      '<p class="w-caption">Elípticas são sustentadas por dispersão de velocidades σ. A relação de Faber–Jackson, L ∝ σ⁴, ' +
      'tem espalhamento grande; incluindo o brilho superficial médio ⟨μ⟩e as galáxias caem num plano: ' +
      'log R<sub>e</sub> = a log σ + b ⟨μ⟩e + c, com a ≈ 1,24 e b ≈ 0,33 (Jørgensen et al. 1996). Dados sintéticos, ilustrativos.</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Diagrama de luminosidade contra dispersão de velocidades de elípticas e projeção girável do Plano Fundamental.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    var modo = 'fj';
    var btnModo = botao(ctrl, '', function () { modo = modo === 'fj' ? 'pf' : 'fj'; atualizarModo(); desenhar(); });
    var gFJ = el('div'), gPF = el('div');
    ctrl.appendChild(gFJ); ctrl.appendChild(gPF);
    var sSig = slider(gFJ, { nome: 'σ da galáxia', min: 60, max: 400, step: 1, valor: 200, fmt: function (v) { return num(v, 0) + ' km/s'; }, aoMudar: function () { desenhar(); } });
    var sAng = slider(gPF, { nome: 'Ângulo de visada θ', min: 0, max: 180, step: 0.5, valor: 0, fmt: function (v) { return num(v, 1) + '°'; }, aoMudar: function () { desenhar(); } });
    botao(gPF, 'Ver o plano de lado', function () { sAng.set(PF.thEdge * 180 / Math.PI); desenhar(); });
    botao(gPF, 'Ver de frente (θ = 0)', function () { sAng.set(0); desenhar(); });

    function atualizarModo() {
      btnModo.textContent = modo === 'fj' ? 'Mostrar o Plano Fundamental →' : '← Voltar a Faber–Jackson';
      gFJ.style.display = modo === 'fj' ? 'contents' : 'none';
      gPF.style.display = modo === 'pf' ? 'contents' : 'none';
    }
    atualizarModo();

    var st = montarCanvas(root, canvas, function (w) { return limitar(w * 0.58, 260, 460); }, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    function eixos(ctx, c, box, xr, yr, xlab, ylab, passoX, passoY, dx, dy) {
      var pequeno = box.w < 380;
      fonte(ctx, root, pequeno ? 10 : 11);
      ctx.lineWidth = 1;
      ctx.fillStyle = c.muted;
      function X(x) { return box.x + box.w * (x - xr[0]) / (xr[1] - xr[0]); }
      function Y(y) { return box.y + box.h * (1 - (y - yr[0]) / (yr[1] - yr[0])); }
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      for (var x = Math.ceil(xr[0] / passoX - 1e-9) * passoX; x <= xr[1] + 1e-9; x += passoX) {
        ctx.strokeStyle = rgba(c.muted, 0.16);
        ctx.beginPath(); ctx.moveTo(X(x), box.y); ctx.lineTo(X(x), box.y + box.h); ctx.stroke();
        ctx.fillText(num(x, dx), X(x), box.y + box.h + 4);
      }
      ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
      for (var y = Math.ceil(yr[0] / passoY - 1e-9) * passoY; y <= yr[1] + 1e-9; y += passoY) {
        ctx.strokeStyle = rgba(c.muted, 0.16);
        ctx.beginPath(); ctx.moveTo(box.x, Y(y)); ctx.lineTo(box.x + box.w, Y(y)); ctx.stroke();
        ctx.fillText(num(y, dy), box.x - 5, Y(y));
      }
      ctx.strokeStyle = rgba(c.muted, 0.6); ctx.strokeRect(box.x, box.y, box.w, box.h);
      ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      ctx.fillText(xlab, box.x + box.w / 2, box.y + box.h + (pequeno ? 30 : 34));
      ctx.save(); ctx.translate(box.x - (pequeno ? 34 : 40), box.y + box.h / 2); ctx.rotate(-Math.PI / 2);
      ctx.textBaseline = 'middle'; ctx.fillText(ylab, 0, 0); ctx.restore();
      return { X: X, Y: Y };
    }

    function desenharFJ(ctx, c, W, H) {
      var pequeno = W < 480;
      var box = { x: pequeno ? 48 : 58, y: 12, w: 0, h: 0 };
      box.w = W - box.x - 12; box.h = H - box.y - (pequeno ? 40 : 44);
      var xr = [1.7, 2.7], yr = [8, 12];
      var ax = eixos(ctx, c, box, xr, yr, 'log σ (km/s)', 'log L_V (L☉)', 0.2, 0.5, 1, 1);
      ctx.save(); ctx.beginPath(); ctx.rect(box.x, box.y, box.w, box.h); ctx.clip();

      // faixa de ±1 desvio-padrão e reta L ∝ σ⁴
      var fit = regressao(FJ.map(function (p) { return p.x; }), FJ.map(function (p) { return p.y; }));
      function lin(x) { return LOGL0 + 4 * (x - Math.log10(SIG0)); }
      ctx.fillStyle = rgba(c.accent, 0.12);
      ctx.beginPath();
      ctx.moveTo(ax.X(xr[0]), ax.Y(lin(xr[0]) + 0.22)); ctx.lineTo(ax.X(xr[1]), ax.Y(lin(xr[1]) + 0.22));
      ctx.lineTo(ax.X(xr[1]), ax.Y(lin(xr[1]) - 0.22)); ctx.lineTo(ax.X(xr[0]), ax.Y(lin(xr[0]) - 0.22));
      ctx.closePath(); ctx.fill();
      FJ.forEach(function (p) {
        ctx.fillStyle = rgba(c.star, 0.75);
        ctx.beginPath(); ctx.arc(ax.X(p.x), ax.Y(p.y), 2.4, 0, 2 * Math.PI); ctx.fill();
      });
      ctx.strokeStyle = c.accent; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(ax.X(xr[0]), ax.Y(lin(xr[0]))); ctx.lineTo(ax.X(xr[1]), ax.Y(lin(xr[1]))); ctx.stroke();

      // galáxia escolhida
      var sg = sSig.v(), lx = Math.log10(sg), ly = lin(lx);
      ctx.strokeStyle = rgba(c.warm, 0.8); ctx.setLineDash([4, 4]); ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(ax.X(lx), box.y + box.h); ctx.lineTo(ax.X(lx), ax.Y(ly)); ctx.lineTo(box.x, ax.Y(ly)); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = c.warm; ctx.beginPath(); ctx.arc(ax.X(lx), ax.Y(ly), 6, 0, 2 * Math.PI); ctx.fill();
      ctx.restore();

      fonte(ctx, root, pequeno ? 11 : 12, '600');
      ctx.fillStyle = c.accent; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('L ∝ σ⁴', box.x + 10, box.y + 8);

      var L = Math.pow(10, ly), MV = 4.83 - 2.5 * ly;
      readout.innerHTML =
        '<div>σ = <b>' + num(sg, 0) + ' km/s</b> → L<sub>V</sub> ≈ <b>' + sci(L, 2) + ' L☉</b> (M<sub>V</sub> ≈ ' + num(MV, 1) + ') ' +
        '&nbsp;·&nbsp; faixa típica (±0,22 dex): ' + sci(L / Math.pow(10, 0.22), 1) + ' – ' + sci(L * Math.pow(10, 0.22), 1) + ' L☉</div>' +
        '<div>Relação usada: L<sub>V</sub> ≈ 2 × 10¹⁰ L☉ (σ/200 km/s)⁴. Dobrar σ multiplica L por 2⁴ = 16. ' +
        'Inclinação ajustada aos pontos: <b>' + num(fit.b, 2) + '</b>; espalhamento ≈ ' + num(fit.rms, 2) + ' dex em L.</div>';
    }

    function desenharPF(ctx, c, W, H) {
      var pequeno = W < 480;
      var th = sAng.v() * Math.PI / 180, ct = Math.cos(th), sn = Math.sin(th);
      var pts = PF.pts;
      var hs = pts.map(function (p) { return ct * p.X + sn * p.Y; });
      var rs = pts.map(function (p) { return p.r; });
      var fit = regressao(hs, rs);
      var edge = regressao(pts.map(function (p) { return Math.cos(PF.thEdge) * p.X + Math.sin(PF.thEdge) * p.Y; }), rs);

      var box = { x: pequeno ? 48 : 58, y: 12, w: 0, h: 0 };
      box.w = W - box.x - 12; box.h = H - box.y - (pequeno ? 40 : 44);
      var yr = [PF.er.m - 3.2 * PF.er.s, PF.er.m + 3.2 * PF.er.s];
      var ax = eixos(ctx, c, box, [-3, 3], yr, 'cos θ · log σ + sen θ · ⟨μ⟩e  (ambos padronizados)', 'log Re (kpc)', 1, 0.2, 0, 1);
      ctx.save(); ctx.beginPath(); ctx.rect(box.x, box.y, box.w, box.h); ctx.clip();
      for (var i = 0; i < pts.length; i++) {
        // cor pela profundidade (coordenada perpendicular à visada), dá noção de 3D
        var prof = -sn * pts[i].X + ct * pts[i].Y;
        ctx.fillStyle = rgba(prof > 0 ? c.accent2 : c.star, 0.45 + 0.12 * Math.min(3, Math.abs(prof)));
        ctx.beginPath(); ctx.arc(ax.X(hs[i]), ax.Y(rs[i]), 2.5, 0, 2 * Math.PI); ctx.fill();
      }
      ctx.strokeStyle = c.warm; ctx.lineWidth = 1.8;
      ctx.beginPath(); ctx.moveTo(ax.X(-3), ax.Y(fit.a - 3 * fit.b)); ctx.lineTo(ax.X(3), ax.Y(fit.a + 3 * fit.b)); ctx.stroke();
      ctx.restore();

      // bússola: projeção dos eixos log σ e ⟨μ⟩e na tela
      var L = 24, bx = box.x + box.w - L - 46, by = box.y + box.h - 30;
      fonte(ctx, root, 10);
      ctx.lineWidth = 2; ctx.textBaseline = 'middle'; ctx.textAlign = 'left';
      ctx.strokeStyle = c.accent; ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx + L * ct, by); ctx.stroke();
      ctx.fillStyle = c.accent; ctx.fillText('log σ', bx + Math.max(L * ct, 0) + 4, by - 8);
      ctx.strokeStyle = c.accent2; ctx.beginPath(); ctx.moveTo(bx, by + 3); ctx.lineTo(bx + L * sn, by + 3); ctx.stroke();
      ctx.fillStyle = c.accent2; ctx.fillText('⟨μ⟩e', bx + Math.max(L * sn, 0) + 4, by + 9);

      var deLado = Math.abs(th - PF.thEdge) < 0.02;
      fonte(ctx, root, pequeno ? 11 : 12, '600');
      ctx.fillStyle = deLado ? c.warm : c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText(deLado ? 'Plano visto de lado: nuvem fina' : 'Projeção girável do Plano Fundamental', box.x + 10, box.y + 8);

      readout.innerHTML =
        '<div>θ = <b>' + num(sAng.v(), 1) + '°</b> (θ = 0: log Re × log σ; θ = 90°: log Re × ⟨μ⟩e; de lado: θ ≈ ' + num(PF.thEdge * 180 / Math.PI, 1) + '°)</div>' +
        '<div>Espalhamento em log Re em torno da melhor reta nesta projeção: <b>' + num(fit.rms, 3) + ' dex</b> ' +
        '(mínimo, de lado: ' + num(edge.rms, 3) + ' dex ≈ ' + num((Math.pow(10, edge.rms) - 1) * 100, 0) + '% em Re).</div>' +
        '<div>Plano: log Re = 1,24 log σ + 0,33 ⟨μ⟩e − 8,895 (Re em kpc, σ em km/s, ⟨μ⟩e em mag/arcsec²). ' +
        'O coeficiente 0,33 em μ equivale a −0,82 log ⟨I⟩e. Projeção ortográfica girando em torno do eixo log Re; cor indica a profundidade.</div>';
    }

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores();
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);
      if (modo === 'fj') desenharFJ(ctx, c, W, H); else desenharPF(ctx, c, W, H);
    }
    desenhar();
  };
})();
