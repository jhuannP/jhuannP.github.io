/* AGA0299 · notas de aula — comportamento comum: tema, KaTeX, sumário e widgets. */
(function () {
  "use strict";
  var raiz = document.documentElement;
  var reduz = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- tema claro/escuro ---- */
  var botao = document.querySelector(".theme-toggle");
  if (botao) {
    botao.addEventListener("click", function () {
      var escuro = raiz.dataset.theme
        ? raiz.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      raiz.dataset.theme = escuro ? "light" : "dark";
      try { localStorage.setItem("aga-tema", raiz.dataset.theme); } catch (e) {}
      window.dispatchEvent(new Event("aga-tema"));
    });
  }

  /* ---- matemática ---- */
  function renderMath() {
    if (!window.renderMathInElement) return;
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false }
      ],
      macros: { "\\un": "\\,\\mathrm{#1}", "\\dd": "#1" },
      throwOnError: false,
      ignoredClasses: ["widget"]
    });
  }

  /* ---- sumário: destaca o módulo visível ---- */
  function tocAtivo() {
    var links = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
    if (!links.length || !("IntersectionObserver" in window)) return;
    var porId = {};
    links.forEach(function (a) { porId[a.getAttribute("href").slice(1)] = a; });
    var obs = new IntersectionObserver(function (ents) {
      ents.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.remove("on"); });
          var a = porId[e.target.id];
          if (a) a.classList.add("on");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll(".modulo[id]").forEach(function (m) { obs.observe(m); });
  }

  /* ---- widgets ---- */
  function montarWidgets() {
    var reg = (window.AGA && window.AGA.widgets) || {};
    document.querySelectorAll(".widget[data-widget]").forEach(function (el) {
      var f = reg[el.dataset.widget];
      if (!f) return;
      try { f(el); } catch (e) {
        el.innerHTML = '<p class="w-caption">Não foi possível carregar esta simulação.</p>';
        if (window.console) console.error("widget", el.dataset.widget, e);
      }
    });
  }

  /* ---- galáxia da capa: espiral cinemática de Lindblad ---- */
  function galaxia() {
    var cv = document.querySelector(".hero-canvas");
    if (!cv) return;
    var ctx = cv.getContext("2d");
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, estrelas = [], fundo = [];
    var N = 4200;

    function semente(n) { var s = n; return function () { s = (s * 16807) % 2147483647; return s / 2147483647; }; }

    function montar() {
      var r = cv.getBoundingClientRect();
      W = r.width; H = r.height;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var rnd = semente(7);
      estrelas = [];
      for (var i = 0; i < N; i++) {
        // raio do centro guia com perfil ~exponencial
        var R = 0.06 + (-Math.log(1 - rnd() * 0.97)) * 0.3;
        if (R > 1.05) R = 0.2 + rnd() * 0.85;
        var e = 0.26 + rnd() * 0.06;       // excentricidade da oval
        estrelas.push({
          R: R,
          e: e,
          fase: rnd() * Math.PI * 2,        // posição ao longo da oval
          giro: 2.6 * Math.log(R + 0.04),   // orientação cresce com o raio -> dois braços
          tam: rnd() < 0.08 ? 1.6 : 0.6 + rnd() * 0.8,
          cor: rnd(),
          brilho: 0.35 + rnd() * 0.65
        });
      }
      fundo = [];
      for (var k = 0; k < 220; k++) fundo.push([rnd() * W, rnd() * H, rnd() * 0.9 + 0.2, rnd()]);
    }

    var t = 0, ultimo = 0, rodando = !reduz, visivel = true;
    function quadro(ts) {
      if (!ultimo) ultimo = ts;
      var dt = Math.min(0.05, (ts - ultimo) / 1000); ultimo = ts;
      if (rodando && visivel) t += dt;
      desenhar();
      if (rodando && visivel) requestAnimationFrame(quadro); else ultimo = 0;
    }

    function desenhar() {
      ctx.clearRect(0, 0, W, H);
      for (var k = 0; k < fundo.length; k++) {
        var f = fundo[k];
        ctx.fillStyle = "rgba(220,230,255," + (0.25 + 0.35 * Math.sin(t * 1.3 + f[3] * 9) * f[3]).toFixed(3) + ")";
        ctx.fillRect(f[0], f[1], f[2], f[2]);
      }
      var cx = W > 900 ? W * 0.68 : W * 0.5;
      var cy = H * 0.5;
      var esc = Math.min(W, H) * (W > 900 ? 0.6 : 0.5);
      ctx.globalAlpha = W > 900 ? 1 : 0.7;
      var inc = 0.55;                         // achatamento por inclinação
      var pa = -0.35;                          // ângulo de posição
      var Op = 0.11 * t;                       // padrão gira rígido com Ωp
      var cpa = Math.cos(pa), spa = Math.sin(pa);
      // bojo
      var g = ctx.createRadialGradient(cx, cy, 0, cx, cy, esc * 0.22);
      g.addColorStop(0, "rgba(255,244,220,0.95)");
      g.addColorStop(0.35, "rgba(255,214,160,0.35)");
      g.addColorStop(1, "rgba(255,214,160,0)");
      ctx.fillStyle = g;
      ctx.beginPath(); ctx.ellipse(cx, cy, esc * 0.24, esc * 0.24 * (0.6 + inc * 0.4), pa, 0, Math.PI * 2); ctx.fill();
      ctx.globalCompositeOperation = "lighter";
      for (var i = 0; i < estrelas.length; i++) {
        var s = estrelas[i];
        // estrela percorre a oval (no referencial girante) com velocidade ~ κ/2
        var w = 0.9 / Math.max(s.R, 0.12);
        var u = s.fase + t * w * 0.18;
        // oval com dois lóbulos: raio varia com cos 2u (ressonância 1:2)
        var rr = s.R * (1 - s.e * Math.cos(2 * u));
        var ang = u + s.giro + Op;
        var x = rr * Math.cos(ang), y = rr * Math.sin(ang) * inc;
        var X = cx + esc * (x * cpa - y * spa);
        var Y = cy + esc * (x * spa + y * cpa);
        var azul = s.cor < 0.55 && s.R > 0.25;
        var a = s.brilho * (s.R < 0.15 ? 0.5 : 0.85);
        ctx.fillStyle = azul ? "rgba(150,190,255," + a + ")" : (s.cor < 0.8 ? "rgba(255,240,220," + a + ")" : "rgba(255,190,150," + a + ")");
        ctx.fillRect(X, Y, s.tam, s.tam);
      }
      ctx.globalCompositeOperation = "source-over";
      ctx.globalAlpha = 1;
    }

    montar(); desenhar();
    if ("ResizeObserver" in window) new ResizeObserver(function () { montar(); desenhar(); }).observe(cv);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (e) {
        visivel = e[0].isIntersecting;
        if (visivel && rodando) requestAnimationFrame(quadro);
      }).observe(cv);
    }
    if (rodando) requestAnimationFrame(quadro);
  }

  function iniciar() { renderMath(); tocAtivo(); montarWidgets(); galaxia(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
