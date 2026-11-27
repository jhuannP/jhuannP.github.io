/* Física III para IME · Capítulo I · Força magnética
   Widgets: w-seletor, w-ciclo, w-fluxo, w-ima. Usa window.F3 (core.js). */
(function(){
"use strict";
var F = window.F3;
function el(id){ return document.getElementById(id); }
function btnGroup(root, attr, cb){
  var bs = root.querySelectorAll('['+attr+']');
  bs.forEach(function(b){ b.addEventListener('click', function(){
    bs.forEach(function(o){ o.classList.toggle('on', o===b); }); cb(b.getAttribute(attr)); }); });
}

/* =====================================================================
   W1 · Seletor de velocidades
   v = v î, B = −B k̂ (⊗), placa + em cima ⇒ E = −E ĵ.
   F_y = q(−E + vB). Unidades: v em 10^5 m/s, E em 10^4 V/m, B em T.
   ===================================================================== */
(function(){
  var root = el('w-seletor'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var sq = 1, mix = false, parts = [], marks = [], spawn = 0, passed = 0, blocked = 0;
  F.bind(root, S, function(){ passed = 0; blocked = 0; marks = []; });
  btnGroup(root, 'data-q', function(v){ sq = +v; passed = 0; blocked = 0; marks = []; parts = []; });
  var mixBtn = root.querySelector('[data-act=mix]');
  mixBtn.addEventListener('click', function(){ mix = !mix; mixBtn.classList.toggle('on', mix); passed = 0; blocked = 0; marks = []; });
  var KAPPA = 240; // px/s² por unidade de (vB − E/10) [10^5 V/m]

  F.loop(root, function(dt){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h;
    var v0 = S.v, E = S.E, B = S.B;
    F.setOut(root,'v', F.fmt(v0,1)+'×10⁵ m/s'); F.setOut(root,'E', F.fmt(E,1)+'×10⁴ V/m'); F.setOut(root,'B', F.fmt(B,2)+' T');
    var x0 = Math.max(70, w*0.14), x1 = w - Math.max(90, w*0.16), cy = h*0.5, gap = Math.min(80, h*0.27);
    var yTop = cy - gap, yBot = cy + gap, slitX = x1 + 30, slitH = 9;

    // dinâmica
    if(dt > 0){
      spawn -= dt;
      if(spawn <= 0){ spawn = mix ? 0.12 : 0.28;
        var vv = mix ? v0*(0.55 + 0.9*Math.random()) : v0;
        parts.push({x: 12, y: cy, vy: 0, v: vv, alive: true}); }
      parts.forEach(function(p){
        if(!p.alive) return;
        var vx = 60 + 45*p.v;
        var inside = p.x > x0 && p.x < x1;
        if(inside){ var net = sq*(p.v*B - E/10); p.vy += -KAPPA*net*dt; } // math y para cima ⇒ tela y para baixo
        p.x += vx*dt; p.y += p.vy*dt;
        if(inside && (p.y < yTop+3 || p.y > yBot-3)){ p.alive = false; blocked++; marks.push({x:p.x, y: p.y<cy? yTop+3 : yBot-3, t:2}); }
        if(p.alive && p.x >= slitX && p.x - vx*dt < slitX){ if(Math.abs(p.y-cy) > slitH){ p.alive = false; blocked++; marks.push({x:slitX, y:p.y, t:2}); } else passed++; }
        if(p.x > w+10) p.alive = false;
      });
      parts = parts.filter(function(p){ return p.alive; });
      marks.forEach(function(m){ m.t -= dt; }); marks = marks.filter(function(m){ return m.t > 0; });
      if(marks.length > 60) marks.splice(0, marks.length-60);
    }

    // desenho
    ctx.clearRect(0,0,w,h);
    // B ⊗ na região das placas
    for(var gx = x0+18; gx < x1; gx += 36) for(var gy = yTop+18; gy < yBot; gy += 30) F.crossIn(ctx, gx, gy, 5, c.B);
    // placas
    ctx.fillStyle = c.E; ctx.fillRect(x0, yTop-8, x1-x0, 6); ctx.fillStyle = c.muted; ctx.fillRect(x0, yBot+2, x1-x0, 6);
    F.label(ctx, '+ + + + + + +', (x0+x1)/2, yTop-18, c.E, 13, 'center');
    F.label(ctx, '− − − − − − −', (x0+x1)/2, yBot+20, c.muted, 13, 'center');
    F.arrow(ctx, x0-26, yTop+6, x0-26, yTop+46, c.E, 2, 8); F.label(ctx, 'E', x0-40, yTop+26, c.E, 14, 'center');
    F.label(ctx, 'B ⊗', x1-6, yTop+12, c.B, 13, 'right');
    // fenda
    ctx.fillStyle = c.ink; ctx.fillRect(slitX-2, 8, 4, cy-slitH-8); ctx.fillRect(slitX-2, cy+slitH, 4, h-cy-slitH-8);
    F.label(ctx, 'fenda', slitX+8, cy-slitH-14, c.muted, 11);
    // fonte
    ctx.fillStyle = c.grid; ctx.fillRect(2, cy-12, 14, 24);
    // partículas
    parts.forEach(function(p){
      var col = sq > 0 ? c.S : c.neg;
      if(mix){ var d = p.v/v0; col = d < 0.95 ? c.E : (d > 1.05 ? c.B : c.ok); }
      ctx.fillStyle = col; ctx.beginPath(); ctx.arc(p.x, p.y, 3.2, 0, 7); ctx.fill();
    });
    marks.forEach(function(m){ ctx.globalAlpha = Math.max(0, m.t/2); ctx.fillStyle = c.neg; ctx.beginPath(); ctx.arc(m.x, m.y, 4, 0, 7); ctx.fill(); });
    ctx.globalAlpha = 1;
    // diagrama de forças numa carga de prova (canto)
    var px = x0 + (x1-x0)*0.5, py = cy, sc = 26;
    var Fe = sq*E/10, Fm = sq*v0*B; // componente y (para cima +) de cada força: Fe = −qE (E para baixo) ⇒ sinal abaixo
    var feY = -Fe, fmY = Fm; // y matemático
    if(!mix){
      F.arrow(ctx, px-10, py, px-10, py - fmY*sc*1.2, c.B, 2.5, 8);
      F.arrow(ctx, px+10, py, px+10, py - feY*sc*1.2, c.E, 2.5, 8);
      F.label(ctx, 'F_m', px-16, py - fmY*sc*1.2 - (fmY>0?8:-8), c.B, 11, 'right');
      F.label(ctx, 'F_e', px+16, py - feY*sc*1.2 - (feY>0?8:-8), c.E, 11, 'left');
    }
    // legenda
    if(mix){ F.label(ctx,'lentas', 8, h-12, c.E, 11); F.label(ctx,'v ≈ E/B', 60, h-12, c.ok, 11); F.label(ctx,'rápidas', 122, h-12, c.B, 11); }
    var vsel = (E*1e4)/B; // m/s
    var bal = vsel > 0 && Math.abs(v0*1e5 - vsel)/vsel < 0.03;
    out.innerHTML = '<span>E/B = <b>'+F.sci(vsel,2)+' m/s</b></span><span>v = <b>'+F.sci(v0*1e5,2)+' m/s</b></span>'+
      '<span>|F_m|/|F_e| = vB/E = <b class="hl">'+(E > 0.01 ? F.fmt((v0*1e5*B)/(E*1e4),2) : '∞ (sem E)')+'</b></span>'+
      '<span>'+(mix ? 'passaram: <b>'+passed+'</b> · barradas: <b>'+blocked+'</b>' : (bal ? '<b class="hl">equilíbrio: passa reto</b>' : (sq*(v0*B - E/10) > 0 ? 'magnético vence: desvia para cima' : 'elétrico vence: desvia para baixo')))+'</span>';
  });
})();

/* =====================================================================
   W2 · Partícula em campo uniforme (círculo / hélice)
   B = Bz k̂ com Bz = −B (⊗) ou +B (⊙). ω⃗ = −(q/m) B⃗.
   ===================================================================== */
(function(){
  var root = el('w-ciclo'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var P = { p:{n:'próton', q:1.602e-19, m:1.673e-27}, e:{n:'elétron', q:-1.602e-19, m:9.109e-31}, a:{n:'alfa', q:3.204e-19, m:6.645e-27} };
  var part = P.p, bsign = -1, psi = 0, z3 = 0, trail = [], trail3 = [];
  function reset(){ trail = []; trail3 = []; z3 = 0; psi = 0; }
  F.bind(root, S, reset);
  btnGroup(root, 'data-p', function(k){ part = P[k]; reset(); });
  btnGroup(root, 'data-bs', function(k){ bsign = k === 'in' ? -1 : 1; reset(); });
  root.querySelector('[data-act=reset]').addEventListener('click', reset);

  F.loop(root, function(dt){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h;
    var v = S.v*1e5, B = S.B, al = S.a*Math.PI/180;
    F.setOut(root,'v', F.fmt(S.v,1)+'×10⁵ m/s'); F.setOut(root,'B', F.fmt(B,2)+' T'); F.setOut(root,'a', S.a+'°');
    var aq = Math.abs(part.q), vperp = v*Math.sin(al), vpar = v*Math.cos(al);
    var r = part.m*vperp/(aq*B), om = aq*B/part.m, T = 2*Math.PI/om, pitch = vpar*T;
    var sense = -Math.sign(part.q)*bsign; // sinal de ω_z: +1 anti-horário
    var rRef = part.m*1e6/(aq*0.5);       // raio de referência (v=10×10⁵, B=0,5, 90°)

    var wide = w > 560, Lw = wide ? w*0.58 : w, cx = Lw/2, cy = h/2;
    var Rbase = Math.min(h, Lw)*0.26, R = Math.min(Rbase*r/rRef, Math.min(h, Lw)*0.46);
    var wv = (2*Math.PI/3)*(B/0.5); // velocidade angular visual
    psi += sense*wv*dt;
    var X = cx + R*Math.cos(psi), Y = cy - R*Math.sin(psi);
    if(dt > 0){ trail.push([X,Y]); if(trail.length > 260) trail.shift(); }

    ctx.clearRect(0,0,w,h);
    // fundo de B
    for(var gx = 22; gx < Lw; gx += 40) for(var gy = 22; gy < h; gy += 40){
      if(bsign < 0) F.crossIn(ctx, gx, gy, 4.5, c.grid); else F.dotOut(ctx, gx, gy, 4.5, c.grid);
    }
    F.label(ctx, bsign < 0 ? 'B = −B k̂ (⊗)' : 'B = +B k̂ (⊙)', 10, 14, c.B, 12.5);
    // órbita e rastro
    ctx.strokeStyle = c.grid; ctx.setLineDash([4,4]); ctx.lineWidth = 1; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7); ctx.stroke(); ctx.setLineDash([]);
    ctx.strokeStyle = c.S; ctx.lineWidth = 2; ctx.beginPath();
    trail.forEach(function(p,i){ i ? ctx.lineTo(p[0],p[1]) : ctx.moveTo(p[0],p[1]); }); ctx.stroke();
    ctx.fillStyle = c.muted; ctx.beginPath(); ctx.arc(cx, cy, 2.5, 0, 7); ctx.fill();
    // v e F calculados por produto vetorial (matemático, y para cima)
    var vx = -sense*Math.sin(psi), vy = sense*Math.cos(psi);      // direção de v⊥
    var Fx = Math.sign(part.q)*(vy*bsign), Fy = Math.sign(part.q)*(-vx*bsign); // q v×B, B=(0,0,bsign)
    var La = 46;
    F.arrow(ctx, X, Y, X + vx*La, Y - vy*La, c.ok, 2.8, 10);
    F.arrow(ctx, X, Y, X + Fx*La*0.8, Y - Fy*La*0.8, c.E, 2.8, 10);
    F.label(ctx, 'v', X + vx*(La+10), Y - vy*(La+10), c.ok, 14, 'center', '600');
    F.label(ctx, 'F', X + Fx*(La*0.8+10), Y - Fy*(La*0.8+10), c.E, 14, 'center', '600');
    ctx.fillStyle = part.q > 0 ? c.S : c.neg; ctx.beginPath(); ctx.arc(X, Y, 7, 0, 7); ctx.fill();
    F.label(ctx, part.q > 0 ? '+' : '−', X, Y+0.5, c.bg, 12, 'center', '600');
    F.label(ctx, sense > 0 ? 'gira anti-horário' : 'gira horário', 10, h-14, c.muted, 12);

    // painel 3D
    if(wide){
      var x0 = Lw + 10, pw = w - x0 - 10, base = h - 30, H3 = h - 70, cx3 = x0 + pw/2;
      ctx.strokeStyle = c.grid; ctx.lineWidth = 1; ctx.strokeRect(x0, 10, pw, h-20);
      var k3 = Math.min(1, (pw*0.36)/Math.max(R,1)), R3 = R*k3;
      var vparVis = (Math.cos(al)/Math.max(Math.sin(al),1e-3))*R*wv*k3;
      if(dt > 0){ z3 += vparVis*dt; if(z3 > H3){ z3 = 0; trail3 = []; } }
      function P3(px,py,pz){ return [cx3 + px, base - pz - 0.35*py]; }
      // eixo de B
      F.arrow(ctx, x0+18, bsign>0 ? base : 30, x0+18, bsign>0 ? 30 : base, c.B, 2, 9);
      F.label(ctx, 'B', x0+30, bsign>0 ? 34 : base-4, c.B, 13);
      var p3 = P3(R3*Math.cos(psi), R3*Math.sin(psi), z3);
      if(dt > 0){ trail3.push(p3); if(trail3.length > 900) trail3.shift(); }
      ctx.strokeStyle = c.S; ctx.lineWidth = 1.8; ctx.beginPath();
      trail3.forEach(function(p,i){ i ? ctx.lineTo(p[0],p[1]) : ctx.moveTo(p[0],p[1]); }); ctx.stroke();
      ctx.fillStyle = part.q > 0 ? c.S : c.neg; ctx.beginPath(); ctx.arc(p3[0], p3[1], 5, 0, 7); ctx.fill();
      F.label(ctx, S.a >= 89.5 ? 'círculo (v ⟂ B)' : 'hélice', cx3, 24, c.ink, 12.5, 'center');
      F.label(ctx, 'perspectiva', x0+pw-8, h-18, c.muted, 11, 'right');
    }
    var K = 0.5*part.m*v*v;
    out.innerHTML = '<span>'+part.n+': r = mv⊥/|q|B = <b class="hl">'+F.sci(r,2)+' m</b></span>'+
      '<span>ω = |q|B/m = <b>'+F.sci(om,2)+' rad/s</b></span><span>f = <b>'+F.sci(om/(2*Math.PI),2)+' Hz</b></span>'+
      '<span>T = <b>'+F.sci(T,2)+' s</b></span><span>passo = v∥T = <b>'+(pitch < 1e-12 ? '0' : F.sci(pitch,2))+' m</b></span>'+
      '<span>K = ½mv² = <b>'+F.sci(K,2)+' J</b> (constante)</span><span>P = F·v = <b class="hl">0</b></span>';
  });
})();

/* =====================================================================
   W3 · Fluxo numa espira que gira: Φ = B S cos θ
   Mundo: x para a direita (B), y para cima, z para fora. n̂ = (cos θ, 0, sin θ).
   ===================================================================== */
(function(){
  var root = el('w-fluxo'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var spin = false, th = 30*Math.PI/180;
  var slider = root.querySelector('input[data-k=th]');
  F.bind(root, S, function(k){ if(k === 'th'){ th = S.th*Math.PI/180; spin = false; sb.classList.remove('on'); } });
  var sb = root.querySelector('[data-act=spin]');
  sb.addEventListener('click', function(){ spin = !spin; sb.classList.toggle('on', spin); });
  var yaw = 0.55, pit = 0.32;

  F.loop(root, function(dt){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h;
    if(spin){ th += 1.1*dt; th %= 2*Math.PI; slider.value = Math.round(th*180/Math.PI); }
    var B = S.B, A = S.S, deg = ((th*180/Math.PI)%360+360)%360;
    F.setOut(root,'th', F.fmt(deg,0)+'°'); F.setOut(root,'B', F.fmt(B,1)+' T'); F.setOut(root,'S', F.fmt(A,2)+' m²');
    ctx.clearRect(0,0,w,h);
    var wide = w > 520, Lw = wide ? w*0.58 : w, ox = Lw/2, oy = h/2 + 6, sc = Math.min(Lw, h)*0.2;
    function P(x,y,z){ var x1 = x*Math.cos(yaw) + z*Math.sin(yaw), z1 = -x*Math.sin(yaw) + z*Math.cos(yaw);
      var y2 = y*Math.cos(pit) - z1*Math.sin(pit); return [ox + x1*sc, oy - y2*sc]; }
    var s = 1.9*Math.sqrt(A), n = [Math.cos(th), 0, Math.sin(th)], u = [-Math.sin(th), 0, Math.cos(th)];
    // linhas de campo (grade em y,z)
    var through = 0, total = 0;
    var lines = [];
    for(var yy = -1.5; yy <= 1.51; yy += 0.5) for(var zz = -1.5; zz <= 1.51; zz += 0.5){
      total++;
      var hit = false, tHit = 0;
      if(Math.abs(n[0]) > 1e-6){ tHit = -zz*n[2]/n[0]; var uu = u[0]*tHit + u[2]*zz, vv = yy;
        if(Math.abs(uu) < s/2 && Math.abs(vv) < s/2 && Math.abs(tHit) < 2.4) hit = true; }
      if(hit) through++;
      lines.push({y:yy, z:zz, hit:hit, t:tHit});
    }
    // desenha linhas de trás para frente (aprox.: z crescente)
    lines.sort(function(a,b){ return a.z - b.z; });
    function drawLine(L, part){
      var a0 = -2.6, a1 = 2.6, from = part === 0 ? a0 : L.t, to = part === 0 ? (L.hit ? L.t : a1) : a1;
      var p0 = P(from, L.y, L.z), p1 = P(to, L.y, L.z);
      ctx.globalAlpha = L.hit ? 0.95 : 0.28;
      if(part === 1 || !L.hit) F.arrow(ctx, p0[0], p0[1], p1[0], p1[1], L.hit ? c.S : c.B, L.hit ? 1.8 : 1.2, 7);
      else { ctx.strokeStyle = c.S; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.moveTo(p0[0],p0[1]); ctx.lineTo(p1[0],p1[1]); ctx.stroke(); }
      ctx.globalAlpha = 1;
    }
    lines.forEach(function(L){ drawLine(L, 0); });
    // espira
    var corners = [[-1,-1],[1,-1],[1,1],[-1,1]].map(function(q){ var a = q[0]*s/2, b = q[1]*s/2; return P(u[0]*a, b, u[2]*a); });
    var flux = B*A*Math.cos(th);
    ctx.fillStyle = flux >= 0 ? 'rgba(110,231,183,.22)' : 'rgba(255,107,138,.22)';
    ctx.strokeStyle = c.E; ctx.lineWidth = 3; ctx.beginPath();
    corners.forEach(function(p,i){ i ? ctx.lineTo(p[0],p[1]) : ctx.moveTo(p[0],p[1]); }); ctx.closePath(); ctx.fill(); ctx.stroke();
    lines.forEach(function(L){ if(L.hit) drawLine(L, 1); });
    var o = P(0,0,0), nt = P(n[0]*1.3, 0, n[2]*1.3);
    F.arrow(ctx, o[0], o[1], nt[0], nt[1], c.ok, 3, 11); F.label(ctx, 'n̂', nt[0]+8, nt[1]-8, c.ok, 15, 'left', '600');
    F.label(ctx, 'B →', 10, 16, c.B, 13);
    // gráfico
    if(wide){
      var bx = Lw + 18, bw = w - bx - 14, by = 30, bh = h - 70;
      var Pl = F.plot(ctx, {x:bx, y:by, w:bw, h:bh}, [0, 360], [-2.1, 2.1], c, {xl:'θ (graus)', yl:'Φ (Wb)'});
      F.curve(ctx, function(x){ return B*A*Math.cos(x*Math.PI/180); }, 0, 360, Pl, c.S, 2);
      [90,180,270].forEach(function(d){ F.label(ctx, d+'°', Pl.X(d), by+bh+12, c.muted, 10, 'center'); });
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(Pl.X(deg), Pl.Y(flux), 5, 0, 7); ctx.fill();
    }
    out.innerHTML = '<span>Φ = B S cos θ = <b class="hl">'+F.fmt(flux,3)+' Wb</b></span><span>linhas que atravessam: <b>'+through+'</b> de '+total+'</span>'+
      '<span>'+(Math.abs(Math.cos(th)) < 0.03 ? 'espira de lado: Φ ≈ 0' : (flux > 0 ? 'n̂ a favor de B: Φ > 0' : 'n̂ contra B: Φ < 0'))+'</span>';
  });
})();

/* =====================================================================
   W4 · Ímã em barra (modelo de correntes de superfície), bússola e curva fechada
   Campo 2D de fios: B = Σ s ẑ×d/(|d|²+ε²), divergência nula.
   ===================================================================== */
(function(){
  var root = el('w-ima'); if(!root) return;
  var cv = root.querySelector('canvas'), st = new F.Stage(cv), S = {}, out = root.querySelector('.w-readout');
  cv.style.touchAction = 'none';
  var pol = 1, gauss = true, wires = [], lines = [], keyW = 0, comp = null, gc = null, needle = 0, needleW = 0, drag = null;
  F.bind(root, S);
  var gb = root.querySelector('[data-act=gauss]');
  gb.addEventListener('click', function(){ gauss = !gauss; gb.classList.toggle('on', gauss); });
  root.querySelector('[data-act=flip]').addEventListener('click', function(){ pol = -pol; keyW = 0; });
  root.querySelector('[data-act=reset]').addEventListener('click', function(){ comp = null; gc = null; });

  function geom(){ var w = st.w, h = st.h; var L = Math.min(w*0.34, 230), H = 44; return {cx:w/2, cy:h/2, L:L, H:H}; }
  function build(){
    var g = geom(), N = 34; wires = [];
    for(var i = 0; i < N; i++){ var x = g.cx - g.L/2 + (i+0.5)*g.L/N;
      wires.push([x, g.cy - g.H/2,  pol]);   // parede de cima (tela): corrente saindo se pol=+1
      wires.push([x, g.cy + g.H/2, -pol]); }
    // traçar linhas a partir de sementes no meio do ímã
    lines = [];
    var ns = 11;
    for(var k = 0; k < ns; k++){
      var sy = g.cy - g.H*0.4 + g.H*0.8*k/(ns-1);
      var fw = trace(g.cx, sy, 1), closed = fw.closed;
      var pts = fw.pts;
      if(!closed){ var bw = trace(g.cx, sy, -1); pts = bw.pts.reverse().concat(pts); }
      lines.push(pts);
    }
    keyW = st.w;
  }
  // campo em coordenadas de tela (y para baixo). s>0: corrente saindo da tela.
  function field(px, py){
    var bx = 0, by = 0, e2 = 9;
    for(var i = 0; i < wires.length; i++){ var q = wires[i], dx = px - q[0], dyM = -(py - q[1]);
      var r2 = dx*dx + dyM*dyM + e2, s = q[2]/r2; bx += s*(-dyM); by += s*dx; }
    return [bx, -by];
  }
  function trace(x, y, dir){
    var pts = [[x,y]], hstep = 3, w = st.w, h = st.h, x0 = x, y0 = y;
    for(var n = 0; n < 2600; n++){
      var b = field(x,y), m = Math.hypot(b[0],b[1]) || 1e-9;
      var mx = x + dir*0.5*hstep*b[0]/m, my = y + dir*0.5*hstep*b[1]/m;
      b = field(mx,my); m = Math.hypot(b[0],b[1]) || 1e-9;
      x += dir*hstep*b[0]/m; y += dir*hstep*b[1]/m;
      pts.push([x,y]);
      if(x < -60 || x > w+60 || y < -60 || y > h+60) return {pts:pts, closed:false};
      if(n > 40 && Math.hypot(x-x0, y-y0) < 3.2){ pts.push([x0,y0]); return {pts:pts, closed:true}; }
    }
    return {pts:pts, closed:false};
  }
  function pos(e){ var r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
  cv.addEventListener('pointerdown', function(e){
    if(!comp || !gc) return;
    var p = pos(e), dc = Math.hypot(p[0]-comp[0], p[1]-comp[1]);
    var dgIn = gauss ? Math.hypot(p[0]-gc[0], p[1]-gc[1]) : 1e9;
    if(dc >= 34 && gauss && dgIn < S.R + 16) drag = {k:'g', off:[gc[0]-p[0], gc[1]-p[1]]};
    else { drag = {k:'c', off:[0,0]}; comp = p; }
    try{ cv.setPointerCapture(e.pointerId); }catch(err){}
  });
  cv.addEventListener('pointermove', function(e){ if(!drag) return; var p = pos(e);
    if(drag.k === 'c') comp = p; else gc = [p[0]+drag.off[0], p[1]+drag.off[1]]; });
  function end(){ drag = null; }
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);

  F.loop(root, function(dt){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h, g = geom();
    if(keyW !== w) build();
    if(!comp) comp = [g.cx + g.L*0.15, g.cy - g.H*2.4];
    if(!gc) gc = [g.cx + g.L/2, g.cy];
    F.setOut(root, 'R', S.R + ' px');
    ctx.clearRect(0,0,w,h);
    // linhas
    ctx.strokeStyle = c.B; ctx.lineWidth = 1.4; ctx.globalAlpha = 0.75;
    lines.forEach(function(pts){ ctx.beginPath(); pts.forEach(function(p,i){ i ? ctx.lineTo(p[0],p[1]) : ctx.moveTo(p[0],p[1]); }); ctx.stroke(); });
    ctx.globalAlpha = 1;
    // pontas de seta nas linhas
    lines.forEach(function(pts){
      var acc = 0;
      for(var i = 1; i < pts.length; i++){ acc += Math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]);
        if(acc > 110){ acc = 0; var a = pts[i-1], b = pts[i];
          if(a[0] > 0 && a[0] < w && a[1] > 0 && a[1] < h && !(Math.abs(a[0]-g.cx) < g.L/2 && Math.abs(a[1]-g.cy) < g.H/2))
            F.arrow(ctx, a[0] - (b[0]-a[0])*2, a[1] - (b[1]-a[1])*2, b[0], b[1], c.B, 1.4, 8); } }
    });
    // ímã
    var nRight = pol > 0;
    ctx.fillStyle = nRight ? '#3b82f6' : '#e5484d'; ctx.fillRect(g.cx - g.L/2, g.cy - g.H/2, g.L/2, g.H);
    ctx.fillStyle = nRight ? '#e5484d' : '#3b82f6'; ctx.fillRect(g.cx, g.cy - g.H/2, g.L/2, g.H);
    F.label(ctx, nRight ? 'S' : 'N', g.cx - g.L/4, g.cy, '#fff', 18, 'center', '600');
    F.label(ctx, nRight ? 'N' : 'S', g.cx + g.L/4, g.cy, '#fff', 18, 'center', '600');
    // curva fechada e fluxo
    var fout = 0, fin = 0;
    if(gauss){
      var R = S.R, N = 480, dl = 2*Math.PI*R/N;
      for(var i = 0; i < N; i++){ var a = (i+0.5)/N*2*Math.PI, nx = Math.cos(a), ny = Math.sin(a);
        var b = field(gc[0] + R*nx, gc[1] + R*ny), bn = (b[0]*nx + b[1]*ny)*dl;
        if(bn > 0) fout += bn; else fin += bn; }
      ctx.strokeStyle = c.S; ctx.lineWidth = 2; ctx.setLineDash([6,5]); ctx.beginPath(); ctx.arc(gc[0], gc[1], R, 0, 7); ctx.stroke(); ctx.setLineDash([]);
      for(i = 0; i < 12; i++){ a = i/12*2*Math.PI; var qx = gc[0] + R*Math.cos(a), qy = gc[1] + R*Math.sin(a); b = field(qx,qy);
        var bn2 = b[0]*Math.cos(a) + b[1]*Math.sin(a), bm = Math.hypot(b[0],b[1]) || 1;
        var L = 16*Math.max(-1, Math.min(1, bn2/bm));
        if(Math.abs(L) > 2) F.arrow(ctx, qx, qy, qx + L*Math.cos(a), qy + L*Math.sin(a), bn2 > 0 ? c.ok : c.neg, 2, 6); }
    }
    // bússola
    var bc = field(comp[0], comp[1]), target = Math.atan2(bc[1], bc[0]);
    var d = Math.atan2(Math.sin(target-needle), Math.cos(target-needle));
    if(F.reduce) needle = target; else { needleW += (28*Math.sin(d) - 4.5*needleW)*dt; needle += needleW*dt; }
    ctx.fillStyle = 'rgba(255,255,255,.08)'; ctx.strokeStyle = c.ink; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(comp[0], comp[1], 24, 0, 7); ctx.fill(); ctx.stroke();
    var cx = Math.cos(needle), sy = Math.sin(needle);
    ctx.fillStyle = '#e5484d'; ctx.beginPath(); ctx.moveTo(comp[0] + cx*20, comp[1] + sy*20); ctx.lineTo(comp[0] - sy*4, comp[1] + cx*4); ctx.lineTo(comp[0] + sy*4, comp[1] - cx*4); ctx.closePath(); ctx.fill();
    ctx.fillStyle = c.muted; ctx.beginPath(); ctx.moveTo(comp[0] - cx*20, comp[1] - sy*20); ctx.lineTo(comp[0] - sy*4, comp[1] + cx*4); ctx.lineTo(comp[0] + sy*4, comp[1] - cx*4); ctx.closePath(); ctx.fill();
    F.label(ctx, 'arraste a bússola' + (gauss ? ' e a curva' : ''), 10, h-14, c.muted, 12);
    // leitura
    var ref = 0; (function(){ var b = field(g.cx, g.cy); ref = Math.hypot(b[0],b[1])*g.H; })();
    var nPole = [g.cx + pol*g.L/2, g.cy], sPole = [g.cx - pol*g.L/2, g.cy];
    var inN = gauss && Math.hypot(nPole[0]-gc[0], nPole[1]-gc[1]) < S.R, inS = gauss && Math.hypot(sPole[0]-gc[0], sPole[1]-gc[1]) < S.R;
    var txt = '<span>bússola: B aponta a <b>'+F.fmt(((-target*180/Math.PI)%360+360)%360,0)+'°</b> do eixo x</span>';
    if(gauss){
      txt += '<span>fluxo que sai: <b>'+F.fmt(fout/ref,2)+'</b></span><span>fluxo que entra: <b>'+F.fmt(-fin/ref,2)+'</b></span>'+
        '<span>total ∮B·dS = <b class="hl">'+F.fmt((fout+fin)/ref,2)+'</b></span>'+
        '<span>'+(inN && !inS ? 'envolve só o polo N: mesmo assim, zero' : (inS && !inN ? 'envolve só o polo S: mesmo assim, zero' : (inN && inS ? 'envolve o ímã inteiro' : 'não envolve nenhum polo')))+'</span>'+
        '<span>(unidades: fluxo dentro do ímã = 1)</span>';
    }
    out.innerHTML = txt;
  });
})();

})();
