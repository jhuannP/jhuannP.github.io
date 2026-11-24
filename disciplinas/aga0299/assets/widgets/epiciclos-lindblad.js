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
  // Aproximação epicíclica e ondas cinemáticas de Lindblad.
  // Unidades adimensionais: Rg = 1, Ω = 1 (curva plana ⇒ κ = √2 Ω).
  var OM = 1, KAPPA = Math.SQRT2, RG = 1, XAMP = 0.16;
  var ILR = OM - KAPPA / 2, OLR = OM + KAPPA / 2;

  // posição no referencial inercial (r, φ) para a órbita de teste
  function orbita(t) {
    var r = RG + XAMP * Math.cos(KAPPA * t);
    var f = OM * t - (2 * OM / (KAPPA * RG)) * XAMP * Math.sin(KAPPA * t);
    return [r, f];
  }

  // identifica se (Ω − Ωp)/κ é racional simples ⇒ órbita fechada no referencial girante
  function classificar(q) {
    var casos = [
      [0, 'Corotação (Ωp = Ω): a estrela descreve o epiciclo, uma elipse fechada em torno do centro-guia (sentido retrógrado).'],
      [0.5, 'Ressonância interna de Lindblad (Ωp = Ω − κ/2): elipse fechada centrada no centro galáctico (oval m = 2).'],
      [-0.5, 'Ressonância externa de Lindblad (Ωp = Ω + κ/2): oval m = 2 fechado, percorrido no sentido retrógrado.'],
      [0.25, 'Ressonância 4:1 (Ωp = Ω − κ/4): figura fechada com 4 lóbulos.'],
      [-0.25, 'Ressonância 4:1 externa (Ωp = Ω + κ/4): figura fechada com 4 lóbulos.'],
      [1, 'Ωp = Ω − κ: figura fechada m = 1 (um laço por volta).'],
      [1 / 3, 'Ressonância 3:1 (Ωp = Ω − κ/3): figura fechada com 3 lóbulos.'],
      [-1 / 3, 'Ressonância 3:1 externa (Ωp = Ω + κ/3): figura fechada com 3 lóbulos.']
    ];
    for (var i = 0; i < casos.length; i++) if (Math.abs(q - casos[i][0]) < 0.004) return { fecha: true, txt: casos[i][1] };
    return { fecha: false, txt: 'Fora de ressonância: (Ω − Ωp)/κ não é uma fração simples e a órbita não fecha — forma uma roseta.' };
  }

  window.AGA.widgets['epiciclos-lindblad'] = function (root) {
    root.innerHTML = '';
    var head = el('div', 'w-head',
      '<h4 class="w-title">Epiciclos, ressonâncias e a espiral cinemática de Lindblad</h4>' +
      '<p class="w-caption">Órbita quase circular na aproximação epicíclica: r = R<sub>g</sub> + X cos(κt), ' +
      'φ = Ωt − (2Ω/κR<sub>g</sub>) X sen(κt). Com curva plana, κ = √2 Ω, logo κ/Ω é irracional e a órbita é uma roseta aberta no referencial inercial. ' +
      'Num referencial que gira com Ωp a órbita só fecha quando (Ω − Ωp)/κ é uma fração simples; para Ωp = Ω − κ/2 ela vira uma elipse centrada no centro galáctico.</p>');
    var canvas = el('canvas', 'w-canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Órbita epicíclica nos referenciais inercial e girante, e montagem de uma espiral cinemática com órbitas elípticas aninhadas.');
    var ctrl = el('div', 'w-controls');
    var readout = el('div', 'w-readout');
    root.appendChild(head); root.appendChild(canvas); root.appendChild(ctrl); root.appendChild(readout);

    var modo = 'orbita';   // 'orbita' | 'espiral'
    var t = 0;
    var inercial = false;   // no modo espiral: mostrar no referencial inercial?

    var btnPlay = el('button', 'w-btn'); btnPlay.type = 'button'; ctrl.appendChild(btnPlay);
    var btnModo = botao(ctrl, '', function () { modo = modo === 'orbita' ? 'espiral' : 'orbita'; t = 0; atualizarModo(); desenhar(); });

    // controles do modo órbita
    var grpOrb = el('div');
    grpOrb.style.display = 'contents';
    ctrl.appendChild(grpOrb);
    var sOp = slider(grpOrb, {
      nome: 'Ωp / Ω', min: -0.2, max: 2, step: 0.001, valor: 0.6, marcas: [ILR.toFixed(3), '1', OLR.toFixed(3)],
      fmt: function (v) { return num(v, 3); }, aoMudar: function () { desenhar(); }
    });
    botao(grpOrb, 'Ω − κ/2', function () { sOp.set(ILR); desenhar(); });
    botao(grpOrb, 'Ω', function () { sOp.set(OM); desenhar(); });
    botao(grpOrb, 'Ω + κ/2', function () { sOp.set(OLR); desenhar(); });

    // controles do modo espiral
    var grpEsp = el('div');
    grpEsp.style.display = 'contents';
    ctrl.appendChild(grpEsp);
    var sTw = slider(grpEsp, { nome: 'Defasagem total das elipses', min: 0, max: 240, step: 1, valor: 110, fmt: function (v) { return num(v, 0) + '°'; }, aoMudar: function () { desenhar(); } });
    var btnRef = botao(grpEsp, '', function () { inercial = !inercial; rotuloRef(); desenhar(); });
    function rotuloRef() { btnRef.textContent = inercial ? 'Referencial: inercial (trocar)' : 'Referencial: girando com o padrão (trocar)'; }
    rotuloRef();

    function atualizarModo() {
      btnModo.textContent = modo === 'orbita' ? '🌀 Montar espiral cinemática' : '← Voltar à órbita única';
      grpOrb.style.display = modo === 'orbita' ? 'contents' : 'none';
      grpEsp.style.display = modo === 'espiral' ? 'contents' : 'none';
    }
    atualizarModo();

    // órbitas da espiral cinemática: anéis com Rg crescente, mesma excentricidade relativa
    var NANEIS = 26, NEST = 26, EPS = 0.2;
    var aneis = [];
    for (var i = 0; i < NANEIS; i++) aneis.push(0.28 + 0.72 * i / (NANEIS - 1));
    var OMP_PADRAO = (OM - KAPPA / 2) / 0.64;   // Ω − κ/2 de um anel intermediário (Rg ≈ 0,64), usado para girar o padrão

    function alturaFn(w) { return w < 560 ? limitar(w * 1.22, 260, 460) : limitar(w * 0.5, 260, 460); }
    var st = montarCanvas(root, canvas, alturaFn, function () { desenhar(); });
    observarTema(function () { desenhar(); });

    function painel(ctx, c, x0, y0, w, h, titulo) {
      ctx.fillStyle = rgba(c.accent, 0.05); ctx.fillRect(x0 + 2, y0 + 2, w - 4, h - 4);
      ctx.strokeStyle = rgba(c.muted, 0.35); ctx.lineWidth = 1; ctx.strokeRect(x0 + 2.5, y0 + 2.5, w - 5, h - 5);
      fonte(ctx, root, w < 260 ? 10 : 12, '600');
      ctx.fillStyle = c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText(titulo, x0 + 10, y0 + 9);
    }

    // desenha a trajetória dos últimos 'span' unidades de tempo com rastro que esmaece
    function rastro(ctx, cor, pos, t1, span, n) {
      var blocos = 8;
      for (var b = 0; b < blocos; b++) {
        ctx.beginPath();
        var ini = t1 - span + span * b / blocos, fim = t1 - span + span * (b + 1) / blocos;
        for (var k = 0; k <= n / blocos; k++) {
          var tt = ini + (fim - ini) * k / (n / blocos);
          var p = pos(tt);
          if (k === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
        }
        ctx.strokeStyle = rgba(cor, 0.12 + 0.8 * (b + 1) / blocos);
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }

    function desenharOrbita(ctx, c, W, H) {
      var lado = W >= 560;
      var pw = lado ? W / 2 : W, ph = lado ? H : H / 2;
      var omp = sOp.v();
      var periodoR = 2 * Math.PI / KAPPA;
      var span = 9 * periodoR;

      [0, 1].forEach(function (k) {
        var x0 = lado ? k * pw : 0, y0 = lado ? 0 : k * ph;
        painel(ctx, c, x0, y0, pw, ph, k === 0 ? 'Referencial inercial' : 'Referencial girando com Ωp');
        var cx = x0 + pw / 2, cy = y0 + ph / 2 + 8;
        var esc = (Math.min(pw, ph - 26) / 2 - 10) / (RG + XAMP + 0.05);
        var rot = k === 0 ? 0 : omp;   // referencial girante subtrai Ωp t
        function pos(tt) {
          var o = orbita(tt);
          var f = o[1] - rot * tt;
          return [cx + o[0] * Math.cos(f) * esc, cy - o[0] * Math.sin(f) * esc];
        }
        // círculo-guia e centro
        ctx.strokeStyle = rgba(c.muted, 0.35); ctx.setLineDash([4, 5]); ctx.lineWidth = 1;
        ctx.beginPath(); ctx.arc(cx, cy, RG * esc, 0, 2 * Math.PI); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = c.star; ctx.beginPath(); ctx.arc(cx, cy, 3, 0, 2 * Math.PI); ctx.fill();

        rastro(ctx, k === 0 ? c.accent2 : c.warm, pos, t, span, 720);

        // centro-guia (gira a Ω − rot)
        var fg = (OM - rot) * t;
        ctx.strokeStyle = rgba(c.muted, 0.9); ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.arc(cx + RG * Math.cos(fg) * esc, cy - RG * Math.sin(fg) * esc, 3.5, 0, 2 * Math.PI); ctx.stroke();
        // estrela
        var p = pos(t);
        var g = ctx.createRadialGradient(p[0], p[1], 0, p[0], p[1], 9);
        g.addColorStop(0, c.star); g.addColorStop(1, rgba(c.star, 0));
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p[0], p[1], 9, 0, 2 * Math.PI); ctx.fill();
        ctx.fillStyle = c.star; ctx.beginPath(); ctx.arc(p[0], p[1], 2.8, 0, 2 * Math.PI); ctx.fill();
      });

      var q = (OM - omp) / KAPPA, cl = classificar(q);
      readout.innerHTML =
        '<div>Ωp = <b>' + num(omp, 3) + ' Ω</b> &nbsp;·&nbsp; κ = √2 Ω ≈ 1,414 Ω &nbsp;·&nbsp; ' +
        'marcas: Ω − κ/2 ≈ ' + num(ILR, 3) + ' Ω, Ω = 1, Ω + κ/2 ≈ ' + num(OLR, 3) + ' Ω</div>' +
        '<div>(Ω − Ωp)/κ = <b>' + num(q, 3) + '</b> → ' + (cl.fecha ? '<b>fecha</b>. ' : '') + cl.txt + '</div>' +
        '<div>Círculo tracejado: órbita circular de raio R<sub>g</sub>; anel vazio: centro-guia, que gira com Ω. Rastro: últimas 9 oscilações radiais.</div>';
    }

    function desenharEspiral(ctx, c, W, H) {
      var cx = W / 2, cy = H / 2;
      var rmax = 1 + EPS + 0.02;
      var esc = (Math.min(W, H) / 2 - 12) / rmax;
      var tw = sTw.v() * Math.PI / 180;
      var giro = inercial ? OMP_PADRAO * t : 0;    // o padrão gira rigidamente com Ωp

      ctx.fillStyle = c.star; ctx.beginPath(); ctx.arc(cx, cy, 3, 0, 2 * Math.PI); ctx.fill();

      aneis.forEach(function (rg, i) {
        var om = OM / rg, ka = KAPPA * om;       // curva plana: Ω ∝ 1/R, κ = √2 Ω
        var f0 = tw * i / (NANEIS - 1) + giro;   // orientação do eixo maior cresce com o raio
        // elipse (oval m = 2) no referencial que gira com Ω − κ/2 do próprio anel
        function ponto(u) {
          var r = rg * (1 + EPS * Math.cos(2 * u));
          var f = f0 + u - Math.SQRT2 * EPS * Math.sin(2 * u);
          return [cx + r * Math.cos(f) * esc, cy - r * Math.sin(f) * esc];
        }
        ctx.beginPath();
        for (var k = 0; k <= 120; k++) {
          var pp = ponto(2 * Math.PI * k / 120);
          if (k === 0) ctx.moveTo(pp[0], pp[1]); else ctx.lineTo(pp[0], pp[1]);
        }
        ctx.strokeStyle = rgba(c.accent2, 0.42); ctx.lineWidth = 1.1; ctx.stroke();

        // estrelas percorrem a elipse: u avança a (Ω − Ωp) = κ/2 no referencial do padrão;
        // no referencial inercial somamos a rotação do padrão (já incluída em f0 via 'giro')
        for (var j = 0; j < NEST; j++) {
          var u = 2 * Math.PI * j / NEST + 0.5 * ka * t;
          var p = ponto(u);
          ctx.fillStyle = rgba(c.star, 0.9);
          ctx.beginPath(); ctx.arc(p[0], p[1], 1.7, 0, 2 * Math.PI); ctx.fill();
        }
      });

      fonte(ctx, root, W < 420 ? 10 : 12, '600');
      ctx.fillStyle = c.ink; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText(inercial ? 'Referencial inercial: o padrão gira rigidamente' : 'Referencial girando com Ωp = Ω − κ/2', 10, 8);

      readout.innerHTML =
        '<div>' + NANEIS + ' órbitas fechadas (ovais m = 2 do referencial Ω − κ/2), cada uma girada em relação à anterior; ' +
        'defasagem total de ' + num(sTw.v(), 0) + '° entre a mais interna e a mais externa.</div>' +
        '<div>Onde as elipses se aproximam as estrelas se adensam: surgem dois braços. As estrelas atravessam os braços — ' +
        'como carros num engarrafamento, o adensamento é um <b>padrão</b>, não sempre o mesmo material.</div>' +
        '<div>Simplificação: com curva plana, Ω − κ/2 ≈ 0,29 V/R ainda varia com R, mas muito mais devagar que Ω; ' +
        'aqui o padrão inteiro gira com um único Ωp (o de um anel intermediário). Tempo da animação em unidades arbitrárias.</div>';
    }

    function desenhar() {
      if (!st || !st.w) return;
      var ctx = st.ctx, W = st.w, H = st.h, c = cores();
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);
      if (modo === 'orbita') desenharOrbita(ctx, c, W, H); else desenharEspiral(ctx, c, W, H);
    }

    animador(root, btnPlay, function (dt) {
      t += dt * (modo === 'orbita' ? 1.6 : 0.6);
      desenhar();
    });
    desenhar();
  };
})();
