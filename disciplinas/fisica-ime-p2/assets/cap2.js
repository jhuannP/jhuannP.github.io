/* Física III para IME · Capítulo II · Torque e dipolo magnético
   Widgets: w-fio, w-ex23, w-loop, w-corte, w-loops. Usa window.F3 (core.js). */
(function(){
"use strict";
var F = window.F3;
function el(id){ return document.getElementById(id); }
function btnGroup(root, attr, cb){
  var bs = root.querySelectorAll('['+attr+']');
  bs.forEach(function(b){ b.addEventListener('click', function(){
    bs.forEach(function(o){ o.classList.toggle('on', o===b); }); cb(b.getAttribute(attr)); }); });
}
function vec(x,y){ return '('+F.fmt(x,3)+' î '+(y<0?'− ':'+ ')+F.fmt(Math.abs(y),3)+' ĵ)'; }

/* =====================================================================
   W1 · Força em fios: dF = i dl × B, B = −B k̂ (⊗)
   dl × (−B k̂) = B(−dl_y, dl_x): dl girado de +90°.
   ===================================================================== */
(function(){
  var root = el('w-fio'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var shape = 'reto';
  F.bind(root, S);
  btnGroup(root, 'data-shape', function(k){ shape = k; });
  function path(L){
    var p = [], i, n = 80;
    if(shape === 'reto'){ for(i = 0; i <= n; i++) p.push([-L/2 + L*i/n, 0]); }
    else if(shape === 'semi'){ for(i = 0; i <= n; i++){ var th = Math.PI*(1 - i/n); p.push([L/2*Math.cos(th), L/2*Math.sin(th)]); } }
    else if(shape === 'zig'){ var V = [[-L/2,0],[-L/4,0.3*L],[0,-0.2*L],[L/4,0.35*L],[L/2,0]];
      for(var k = 0; k < V.length-1; k++) for(i = 0; i < 20; i++){ var f = i/20; p.push([V[k][0]+(V[k+1][0]-V[k][0])*f, V[k][1]+(V[k+1][1]-V[k][1])*f]); }
      p.push(V[V.length-1]); }
    else { for(i = 0; i <= n; i++){ var a = 2*Math.PI*i/n; p.push([L/2*Math.cos(a), L/2*Math.sin(a)]); } }
    return p;
  }
  F.loop(root, function(dt, t){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h, I = S.I, B = S.B, L = S.L;
    F.setOut(root,'I', F.fmt(I,1)+' A'); F.setOut(root,'B', F.fmt(B,2)+' T'); F.setOut(root,'L', F.fmt(L,2)+' m');
    ctx.clearRect(0,0,w,h);
    for(var gx = 20; gx < w; gx += 38) for(var gy = 20; gy < h; gy += 38) F.crossIn(ctx, gx, gy, 4.5, c.grid);
    F.label(ctx, 'B = −B k̂ (⊗)', 10, 14, c.B, 12.5);
    var sc = Math.min(w*0.8, h-70), cx = w/2, cy = shape === 'loop' ? h/2 : h*0.62;
    function S2(p){ return [cx + p[0]*sc, cy - p[1]*sc]; }
    var p = path(L), Fx = 0, Fy = 0, len = 0, cum = [0];
    for(var i = 1; i < p.length; i++){ var dx = p[i][0]-p[i-1][0], dy = p[i][1]-p[i-1][1];
      Fx += I*B*(-dy); Fy += I*B*dx; len += Math.hypot(dx,dy); cum.push(len); }
    // fio
    ctx.strokeStyle = c.E; ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.beginPath();
    p.forEach(function(q,k){ var s = S2(q); k ? ctx.lineTo(s[0],s[1]) : ctx.moveTo(s[0],s[1]); }); ctx.stroke();
    if(shape !== 'loop'){ var a0 = S2(p[0]), a1 = S2(p[p.length-1]);
      ctx.fillStyle = c.ink; [a0,a1].forEach(function(s){ ctx.beginPath(); ctx.arc(s[0],s[1],5,0,7); ctx.fill(); });
      F.label(ctx,'A', a0[0]-12, a0[1]+14, c.ink, 13, 'center'); F.label(ctx,'B', a1[0]+12, a1[1]+14, c.ink, 13, 'center');
      ctx.setLineDash([4,4]); ctx.strokeStyle = c.muted; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a0[0],a0[1]+22); ctx.lineTo(a1[0],a1[1]+22); ctx.stroke(); ctx.setLineDash([]);
      F.label(ctx,'L_AB', (a0[0]+a1[0])/2, a0[1]+32, c.muted, 11, 'center'); }
    // pontinhos de corrente
    ctx.fillStyle = c.S; var nd = Math.max(8, Math.round(len*sc/26));
    for(var d = 0; d < nd; d++){ var sp = ((d/nd)*len + t*0.12*len) % len, k2 = 1; while(k2 < cum.length-1 && cum[k2] < sp) k2++;
      var f0 = (sp - cum[k2-1])/((cum[k2]-cum[k2-1])||1), q0 = p[k2-1], q1 = p[k2];
      var s2 = S2([q0[0]+(q1[0]-q0[0])*f0, q0[1]+(q1[1]-q0[1])*f0]); ctx.beginPath(); ctx.arc(s2[0], s2[1], 2.8, 0, 7); ctx.fill(); }
    // dF em ~14 pontos
    var na = 14, aL = Math.min(34, 10 + 24*(I*B)/0.8);
    for(var j = 0; j < na; j++){ var u = (j+0.5)/na*len, m = 1; while(m < cum.length-1 && cum[m] < u) m++;
      var e0 = p[m-1], e1 = p[m], ddx = e1[0]-e0[0], ddy = e1[1]-e0[1], dl = Math.hypot(ddx,ddy)||1;
      var ff = (u - cum[m-1])/((cum[m]-cum[m-1])||1), base = S2([e0[0]+ddx*ff, e0[1]+ddy*ff]);
      var nx = -ddy/dl, ny = ddx/dl; // direção de dF (matemática)
      F.arrow(ctx, base[0], base[1], base[0] + nx*aL, base[1] - ny*aL, c.B, 1.6, 6); }
    // força total
    var Fm = Math.hypot(Fx, Fy);
    var cen = S2([0, shape === 'loop' ? 0 : (shape === 'reto' ? 0 : 0.15*L)]);
    if(Fm > 1e-6){ var Ln = Math.min(130, 55*Math.sqrt(Fm/0.4)); F.arrow(ctx, cen[0], cen[1], cen[0] + Fx/Fm*Ln, cen[1] - Fy/Fm*Ln, c.ok, 4, 13);
      F.label(ctx, 'F total', cen[0] + Fx/Fm*Ln + 8, cen[1] - Fy/Fm*Ln, c.ok, 13, 'left', '600'); }
    else F.label(ctx, 'F total = 0', cen[0], cen[1], c.ok, 14, 'center', '600');
    var LAB = shape === 'loop' ? [0,0] : [L, 0];
    var Fform = [I*B*(-LAB[1]), I*B*LAB[0]];
    out.innerHTML = '<span>comprimento do fio = <b>'+F.fmt(len,3)+' m</b></span>'+
      '<span>Σ i dl×B (numérico) = <b class="hl">'+F.fmt(Fy,3)+' ĵ N</b>'+(Math.abs(Fx) > 1e-4 ? ' + '+F.fmt(Fx,3)+' î' : '')+'</span>'+
      '<span>i L_AB × B = <b>'+F.fmt(Fform[1],3)+' ĵ N</b></span>'+
      '<span>'+(shape === 'loop' ? 'caminho fechado: ∮dl = 0 ⇒ F = 0' : 'só as pontas importam')+'</span>';
  });
})();

/* =====================================================================
   W2 · Exercício 23 em 3D
   l1 = a(cosφ, sinφ, 0), l2 = b k̂, l3 = −l1, l4 = −b k̂; B = B ĵ.
   F1 = iaB cosφ k̂, F3 = −F1, F2 = −ibB î, F4 = +ibB î; τ = iabB sinφ k̂; n̂ = (sinφ, −cosφ, 0).
   ===================================================================== */
(function(){
  var root = el('w-ex23'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var a = 0.30, b = 0.20, phi = 50*Math.PI/180, om = 0, free = false;
  var slider = root.querySelector('input[data-k=phi]'), rb = root.querySelector('[data-act=release]');
  F.bind(root, S, function(k){ if(k === 'phi'){ phi = S.phi*Math.PI/180; free = false; om = 0; rb.classList.remove('on'); rb.textContent = 'Soltar a espira'; } });
  rb.addEventListener('click', function(){ free = !free; om = 0; rb.classList.toggle('on', free); rb.textContent = free ? 'Segurar a espira' : 'Soltar a espira'; });

  F.loop(root, function(dt){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h, I = S.I, B = S.B;
    if(free && dt > 0){ for(var k = 0; k < 4; k++){ var acc = 10*I*B*Math.sin(phi) - 1.0*om; om += acc*dt/4; phi += om*dt/4; } }
    var deg = ((phi*180/Math.PI)%360+360)%360; if(free) slider.value = Math.round(deg);
    F.setOut(root,'phi', F.fmt(deg,0)+'°'); F.setOut(root,'I', F.fmt(I,1)+' A'); F.setOut(root,'B', F.fmt(B,2)+' T');
    ctx.clearRect(0,0,w,h);
    var sc = Math.min(w*0.55, h*0.9)/0.5, ox = w*0.42, oy = h*0.66;
    function P(x,y,z){ return [ox + sc*(y - 0.55*x), oy - sc*(z - 0.45*x)]; }
    var cs = Math.cos(phi), sn = Math.sin(phi);
    // campo B (ĵ)
    ctx.globalAlpha = 0.35;
    [[-0.1,0.05],[0.2,0.25],[-0.25,0.3],[0.15,-0.02]].forEach(function(q){ var p0 = P(q[0], -0.42, q[1]), p1 = P(q[0], 0.48, q[1]); F.arrow(ctx, p0[0], p0[1], p1[0], p1[1], c.B, 1.4, 8); });
    ctx.globalAlpha = 1;
    // eixos
    var O = P(0,0,0), X = P(0.42,0,0), Y = P(0,0.42,0), Z = P(0,0,0.34);
    F.arrow(ctx, O[0],O[1], X[0],X[1], c.muted, 1.2, 7); F.arrow(ctx, O[0],O[1], Y[0],Y[1], c.muted, 1.2, 7); F.arrow(ctx, O[0],O[1], Z[0],Z[1], c.muted, 1.2, 7);
    F.label(ctx,'x', X[0]-10, X[1]+4, c.muted, 13, 'center'); F.label(ctx,'y', Y[0]+10, Y[1], c.muted, 13); F.label(ctx,'z', Z[0]+8, Z[1], c.muted, 13);
    F.label(ctx,'B = B ĵ', w-12, 16, c.B, 13, 'right');
    // vértices
    var V0 = [0,0,0], V1 = [a*cs, a*sn, 0], V2 = [a*cs, a*sn, b], V3 = [0,0,b];
    var Vs = [V0,V1,V2,V3].map(function(v){ return P(v[0],v[1],v[2]); });
    ctx.fillStyle = 'rgba(255,154,77,.12)'; ctx.beginPath(); Vs.forEach(function(s,i){ i ? ctx.lineTo(s[0],s[1]) : ctx.moveTo(s[0],s[1]); }); ctx.closePath(); ctx.fill();
    ctx.strokeStyle = c.E; ctx.lineWidth = 3.5; ctx.stroke();
    // corrente: setinhas no meio de cada lado, rótulos 1..4
    var mids = [], dirs = [];
    for(var s = 0; s < 4; s++){ var A = [V0,V1,V2,V3][s], Bv = [V0,V1,V2,V3][(s+1)%4];
      var M = [(A[0]+Bv[0])/2, (A[1]+Bv[1])/2, (A[2]+Bv[2])/2]; mids.push(M);
      var pa = P(A[0],A[1],A[2]), pb = P(Bv[0],Bv[1],Bv[2]), pm = P(M[0],M[1],M[2]);
      var dx = pb[0]-pa[0], dy = pb[1]-pa[1], dl = Math.hypot(dx,dy)||1; dirs.push([dx/dl, dy/dl]);
      F.arrow(ctx, pm[0]-dx/dl*9, pm[1]-dy/dl*9, pm[0]+dx/dl*9, pm[1]+dy/dl*9, c.S, 2.5, 9);
      F.label(ctx, String(s+1), pm[0] - dy/dl*16, pm[1] + dx/dl*16, c.ink, 13, 'center', '600'); }
    // forças
    var Fs = [[0,0,I*a*B*cs],[-I*b*B,0,0],[0,0,-I*a*B*cs],[I*b*B,0,0]], Fref = 2*0.3*0.5;
    Fs.forEach(function(Fv, s){ var m = Math.hypot(Fv[0],Fv[1],Fv[2]); if(m < 1e-6) return;
      var Lw = Math.min(0.2, 0.09*m/Fref), M = mids[s], p0 = P(M[0],M[1],M[2]), p1 = P(M[0]+Fv[0]/m*Lw, M[1]+Fv[1]/m*Lw, M[2]+Fv[2]/m*Lw);
      F.arrow(ctx, p0[0],p0[1], p1[0],p1[1], c.B, 3, 10); F.label(ctx, 'F'+(s+1), p1[0]+8, p1[1]-6, c.B, 13, 'left', '600'); });
    // CM, n̂ e τ
    var CM = [a*cs/2, a*sn/2, b/2], pc = P(CM[0],CM[1],CM[2]);
    ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(pc[0], pc[1], 3.5, 0, 7); ctx.fill(); F.label(ctx,'CM', pc[0]+7, pc[1]+10, c.ink, 11);
    var pn = P(CM[0]+0.14*sn, CM[1]-0.14*cs, CM[2]); F.arrow(ctx, pc[0],pc[1], pn[0],pn[1], c.ok, 3, 11); F.label(ctx,'n̂', pn[0]+6, pn[1]-8, c.ok, 15, 'left', '600');
    var tau = I*a*b*B*sn, tL = 0.16*tau/(2*0.3*0.2*0.5);
    if(Math.abs(tau) > 1e-5){ var pt = P(CM[0],CM[1],CM[2]+Math.max(-0.2,Math.min(0.2,tL))); F.arrow(ctx, pc[0],pc[1], pt[0],pt[1], c.neg, 3.5, 11); F.label(ctx,'τ', pt[0]+8, pt[1], c.neg, 15, 'left', '600'); }
    // ângulo φ no plano xy
    ctx.strokeStyle = c.muted; ctx.lineWidth = 1.2; ctx.beginPath();
    for(var i2 = 0; i2 <= 30; i2++){ var an = phi*i2/30, q = P(0.08*Math.cos(an), 0.08*Math.sin(an), 0); i2 ? ctx.lineTo(q[0],q[1]) : ctx.moveTo(q[0],q[1]); } ctx.stroke();
    var qa = P(0.11*Math.cos(phi/2), 0.11*Math.sin(phi/2), 0); F.label(ctx,'φ', qa[0], qa[1]+6, c.muted, 13, 'center');
    var U = I*a*b*B*cs; // U = −m·B = −iab(−cosφ)B
    out.innerHTML = '<span>F1 = iaB cosφ k̂ = <b>'+F.fmt(I*a*B*cs,3)+' k̂ N</b></span><span>F3 = <b>'+F.fmt(-I*a*B*cs,3)+' k̂ N</b></span>'+
      '<span>F2 = −ibB î = <b>'+F.fmt(-I*b*B,3)+' î N</b></span><span>F4 = <b>+'+F.fmt(I*b*B,3)+' î N</b></span>'+
      '<span>n̂ = <b>'+vec(sn,-cs)+'</b></span><span>τ = iabB sen φ k̂ = <b class="hl">'+F.fmt(tau,4)+' k̂ N·m</b></span>'+
      '<span>U = −m·B = iabB cos φ = <b>'+F.fmt(U,4)+' J</b></span>';
  });
})();

/* =====================================================================
   W3 · Espira de perfil: torque, U(θ) e comutador (motor CC)
   θ = ângulo de m em relação a B (B para a direita). τ = −mB sen θ.
   ===================================================================== */
(function(){
  var root = el('w-loop'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), S = {}, out = root.querySelector('.w-readout');
  var phi = 70*Math.PI/180, om = 0, free = false, motor = false, flips = 0;
  var slider = root.querySelector('input[data-k=phi]');
  var relBtn = root.querySelector('[data-act=release]'), motBtn = root.querySelector('[data-act=motor]');
  function setFree(v){ free = v; relBtn.classList.toggle('on', free && !motor); relBtn.textContent = free && !motor ? 'Segurar a espira' : 'Soltar a espira'; }
  F.bind(root, S, function(k){ if(k === 'phi'){ setFree(false); motor = false; motBtn.classList.remove('on'); om = 0; phi = S.phi*Math.PI/180; } });
  relBtn.addEventListener('click', function(){ motor = false; motBtn.classList.remove('on'); om = 0; setFree(!free); });
  root.querySelector('[data-act=flip]').addEventListener('click', function(){ phi += Math.PI; });
  motBtn.addEventListener('click', function(){ motor = !motor; motBtn.classList.toggle('on', motor); flips = 0; setFree(motor); });

  F.loop(root, function(dt){
    var mu = S.I*1, Bv = S.B;
    if(free && dt > 0){
      for(var k = 0; k < 4; k++){
        if(motor && Math.sin(phi) > 0){ phi += Math.PI; flips++; } // comutador: mantém τ > 0 (anti-horário)
        var acc = -(mu*Bv*6)*Math.sin(phi) - (motor ? 0.5 : 1.1)*om; om += acc*dt/4; phi += om*dt/4; }
    }
    var pd = ((phi*180/Math.PI)%360+360)%360; if(free) slider.value = Math.round(pd);
    F.setOut(root,'phi', F.fmt(pd,0)+'°'); F.setOut(root,'I', F.fmt(S.I,1)+' A'); F.setOut(root,'B', F.fmt(Bv,1)+' T');
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h; ctx.clearRect(0,0,w,h);
    var gx = Math.min(w*0.62, w-170), cx = gx*0.5 + 10, cy = h/2;
    ctx.globalAlpha = 0.55; for(var y = 26; y < h; y += 34) F.arrow(ctx, 14, y, gx-6, y, c.B, 1.2, 7); ctx.globalAlpha = 1;
    F.label(ctx, 'B', gx-20, 16, c.B, 15, 'right');
    var L = Math.min(h*0.62, gx*0.6), s = Math.sin(phi), co = Math.cos(phi);
    var tx = -s, ty = co;
    var x1 = cx + tx*L/2, y1 = cy - ty*L/2, x2 = cx - tx*L/2, y2 = cy + ty*L/2;
    ctx.strokeStyle = c.E; ctx.lineWidth = 7; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.stroke();
    F.dotOut(ctx, x1, y1, 11, c.ink); F.crossIn(ctx, x2, y2, 11, c.ink);
    var Fl = 34*S.I*Bv/1.5;
    F.arrow(ctx, x1, y1-14, x1, y1-14-Fl, c.S, 2.5); F.arrow(ctx, x2, y2+14, x2, y2+14+Fl, c.S, 2.5);
    var mL = L*0.55*Math.min(1.4, 0.6 + S.I/2.5);
    F.arrow(ctx, cx, cy, cx + co*mL, cy - s*mL, c.ok, 3.5, 12); F.label(ctx, 'm', cx + co*(mL+16), cy - s*(mL+16), c.ok, 16, 'center', '600');
    var pp = ((phi%(2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
    ctx.strokeStyle = c.muted; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(cx, cy, 26, 0, -pp, true); ctx.stroke();
    F.label(ctx, 'θ', cx + 34*Math.cos(pp/2), cy - 34*Math.sin(pp/2), c.muted, 13, 'center');
    var px0 = gx + 20, pw = w - px0 - 14, py0 = 30, ph = h - 70;
    if(pw > 90){
      var Pl = F.plot(ctx, {x:px0, y:py0, w:pw, h:ph}, [0, 2*Math.PI], [-1.2, 1.2], c, {});
      F.curve(ctx, function(a){ return -Math.cos(a); }, 0, 2*Math.PI, Pl, c.E, 2);
      F.curve(ctx, function(a){ return motor ? Math.abs(Math.sin(a)) : -Math.sin(a); }, 0, 2*Math.PI, Pl, c.S, 1.6, [4,4]);
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(Pl.X(pp), Pl.Y(-Math.cos(pp)), 5, 0, 7); ctx.fill();
      F.label(ctx, 'U/mB = −cos θ', px0, py0-14, c.E, 12);
      F.label(ctx, motor ? 'τ/mB com comutador (tracejado)' : 'τ/mB = −sen θ (tracejado)', px0, h-22, c.S, 12);
      F.label(ctx, '0', px0, py0+ph+10, c.muted, 11); F.label(ctx, 'π', px0+pw/2, py0+ph+10, c.muted, 11, 'center'); F.label(ctx, '2π', px0+pw, py0+ph+10, c.muted, 11, 'right');
    }
    var tau = -mu*Bv*Math.sin(phi), U = -mu*Bv*Math.cos(phi);
    out.innerHTML = '<span>m = iS = <b>'+F.fmt(mu,2)+' A·m²</b> (S = 1 m²)</span>'+
      '<span>|τ| = mB sen θ = <b class="hl">'+F.fmt(Math.abs(tau),2)+' N·m</b> ('+(Math.abs(tau) < 1e-3 ? 'nenhum giro' : tau < 0 ? 'gira p/ horário' : 'gira p/ anti-horário')+')</span>'+
      '<span>U = −mB cos θ = <b class="hl">'+F.fmt(U,2)+' J</b></span>'+
      (motor ? '<span>comutador inverteu a corrente <b>'+flips+'</b> vezes · ω ≈ <b>'+F.fmt(Math.abs(om),1)+' rad/s</b></span>' : '');
  });
})();

/* =====================================================================
   W4 · Corte o ímã: pedaços modelados por correntes de superfície (2D)
   ===================================================================== */
(function(){
  var root = el('w-corte'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), out = root.querySelector('.w-readout');
  var n = 1, wires = [], lines = [], keyW = 0, keyN = 0, pieces = [];
  root.querySelector('[data-act=cut]').addEventListener('click', function(){ if(n < 8) n *= 2; });
  root.querySelector('[data-act=join]').addEventListener('click', function(){ n = 1; });
  function field(px, py){
    var bx = 0, by = 0;
    for(var i = 0; i < wires.length; i++){ var q = wires[i], dx = px - q[0], dyM = -(py - q[1]), r2 = dx*dx + dyM*dyM + 9, s = q[2]/r2;
      bx += s*(-dyM); by += s*dx; }
    return [bx, -by];
  }
  function trace(x, y, dir){
    var pts = [[x,y]], hs = 3, w = st.w, h = st.h, x0 = x, y0 = y;
    for(var k = 0; k < 2400; k++){
      var b = field(x,y), m = Math.hypot(b[0],b[1]) || 1e-9, mx = x + dir*0.5*hs*b[0]/m, my = y + dir*0.5*hs*b[1]/m;
      b = field(mx,my); m = Math.hypot(b[0],b[1]) || 1e-9; x += dir*hs*b[0]/m; y += dir*hs*b[1]/m; pts.push([x,y]);
      if(x < -60 || x > w+60 || y < -60 || y > h+60) return {pts:pts, closed:false};
      if(k > 30 && Math.hypot(x-x0, y-y0) < 3.2){ pts.push([x0,y0]); return {pts:pts, closed:true}; }
    }
    return {pts:pts, closed:false};
  }
  function build(){
    var w = st.w, h = st.h, L = Math.min(w*0.5, 340), H = 40, gap = n > 1 ? Math.min(26, (w*0.85 - L)/(n-1)) : 0;
    var tot = L + (n-1)*gap, len = L/n, x = w/2 - tot/2, cy = h/2;
    pieces = []; wires = [];
    var per = Math.max(6, Math.round(36/n));
    for(var p = 0; p < n; p++){ pieces.push([x, x+len]);
      for(var i = 0; i < per; i++){ var xx = x + (i+0.5)*len/per; wires.push([xx, cy-H/2, 1]); wires.push([xx, cy+H/2, -1]); }
      x += len + gap; }
    lines = [];
    var seedsPer = n === 1 ? 11 : (n === 2 ? 6 : (n === 4 ? 4 : 3));
    pieces.forEach(function(pc){ var sx = (pc[0]+pc[1])/2;
      for(var k = 0; k < seedsPer; k++){ var sy = cy - H*0.4 + H*0.8*(seedsPer === 1 ? 0.5 : k/(seedsPer-1));
        var fw = trace(sx, sy, 1), pts = fw.pts; if(!fw.closed){ pts = trace(sx, sy, -1).pts.reverse().concat(pts); } lines.push(pts); } });
    keyW = w; keyN = n;
    return {H:H, cy:cy};
  }
  var G = null;
  F.loop(root, function(){
    var c = F.W(), ctx = st.ctx, w = st.w, h = st.h;
    if(keyW !== w || keyN !== n) G = build();
    ctx.clearRect(0,0,w,h);
    ctx.strokeStyle = c.B; ctx.lineWidth = 1.3; ctx.globalAlpha = 0.75;
    lines.forEach(function(pts){ ctx.beginPath(); pts.forEach(function(p,i){ i ? ctx.lineTo(p[0],p[1]) : ctx.moveTo(p[0],p[1]); }); ctx.stroke(); });
    ctx.globalAlpha = 1;
    lines.forEach(function(pts){ var acc = 0;
      for(var i = 1; i < pts.length; i++){ acc += Math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]);
        if(acc > 100){ acc = 0; var a = pts[i-1], b = pts[i], inside = false;
          pieces.forEach(function(pc){ if(a[0] > pc[0] && a[0] < pc[1] && Math.abs(a[1]-G.cy) < G.H/2) inside = true; });
          if(!inside && a[0] > 0 && a[0] < w && a[1] > 0 && a[1] < h) F.arrow(ctx, a[0]-(b[0]-a[0])*2, a[1]-(b[1]-a[1])*2, b[0], b[1], c.B, 1.3, 8); } } });
    pieces.forEach(function(pc){ var mid = (pc[0]+pc[1])/2, lw = pc[1]-pc[0];
      ctx.fillStyle = '#3b82f6'; ctx.fillRect(pc[0], G.cy-G.H/2, lw/2, G.H);
      ctx.fillStyle = '#e5484d'; ctx.fillRect(mid, G.cy-G.H/2, lw/2, G.H);
      var fs = lw > 60 ? 16 : 12;
      F.label(ctx, 'S', pc[0]+lw/4, G.cy, '#fff', fs, 'center', '600'); F.label(ctx, 'N', mid+lw/4, G.cy, '#fff', fs, 'center', '600'); });
    out.innerHTML = '<span>pedaços: <b>'+n+'</b></span><span>polos N: <b>'+n+'</b> · polos S: <b>'+n+'</b></span><span>polo isolado: <b class="hl">nenhum</b></span><span>∮B·dS = 0 para qualquer pedaço</span>';
  });
})();

/* =====================================================================
   W5 · As quatro espiras do simulado (Exercício 1)
   ===================================================================== */
(function(){
  var root = el('w-loops'); if(!root) return;
  var st = new F.Stage(root.querySelector('canvas')), out = root.querySelector('.w-readout');
  var shapes = [
    {n:'A', type:'poly', pts:[[1.5,3],[4.5,3],[4.5,9],[1.5,9]], dir:1},
    {n:'B', type:'circ', c:[7.5,4.5], r:1.5, dir:-1},
    {n:'C', type:'poly', pts:[[7.5,9],[13.5,9],[12,13.5],[9,13.5]], dir:1},
    {n:'D', type:'poly', pts:[[10.5,7.5],[12,1.5],[13.5,7.5]], dir:1}
  ];
  var init = shapes.map(function(s){ return s.dir; }), Bdir = 'x';
  function area(s){ if(s.type === 'circ') return Math.PI*s.r*s.r; var a = 0, p = s.pts; for(var i = 0; i < p.length; i++){ var q = p[(i+1)%p.length]; a += p[i][0]*q[1] - q[0]*p[i][1]; } return Math.abs(a)/2; }
  function geom(){ var w = st.w, h = st.h, sz = Math.min(h-40, w-60); return {ox:(w-sz)/2+10, oy:20, u:sz/15}; }
  function toS(g,x,y){ return [g.ox + x*g.u, g.oy + (15-y)*g.u]; }
  function inside(s,x,y){ if(s.type === 'circ') return Math.hypot(x-s.c[0], y-s.c[1]) < s.r; var p = s.pts, ins = false;
    for(var i = 0, j = p.length-1; i < p.length; j = i++){ if(((p[i][1] > y) !== (p[j][1] > y)) && (x < (p[j][0]-p[i][0])*(y-p[i][1])/(p[j][1]-p[i][1]) + p[i][0])) ins = !ins; } return ins; }
  st.c.addEventListener('click', function(e){ var r = st.c.getBoundingClientRect(), g = geom(); var x = (e.clientX-r.left-g.ox)/g.u, y = 15-(e.clientY-r.top-g.oy)/g.u; shapes.forEach(function(s){ if(inside(s,x,y)) s.dir = -s.dir; }); });
  st.c.style.cursor = 'pointer';
  root.querySelectorAll('[data-b]').forEach(function(b){ b.addEventListener('click', function(){ Bdir = b.dataset.b; root.querySelectorAll('[data-b]').forEach(function(o){ o.classList.toggle('on', o === b); }); }); });
  root.querySelector('[data-act=reset]').addEventListener('click', function(){ shapes.forEach(function(s,i){ s.dir = init[i]; }); root.querySelector('[data-b=x]').click(); });

  F.loop(root, function(dt, t){
    var c = F.W(), ctx = st.ctx, g = geom(); ctx.clearRect(0,0,st.w,st.h);
    ctx.strokeStyle = c.grid; ctx.lineWidth = 1;
    for(var i = 0; i <= 10; i++){ var a = toS(g,i*1.5,0), b = toS(g,i*1.5,15); ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(b[0],b[1]); ctx.stroke();
      a = toS(g,0,i*1.5); b = toS(g,15,i*1.5); ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(b[0],b[1]); ctx.stroke(); }
    for(i = 0; i <= 15; i += 3){ var p = toS(g,i,0); F.label(ctx, String(i), p[0], p[1]+10, c.muted, 10, 'center'); p = toS(g,0,i); F.label(ctx, String(i), p[0]-6, p[1], c.muted, 10, 'right'); }
    var bx = st.w-58, by = 34;
    if(Bdir === 'x') F.arrow(ctx, bx-26, by, bx+26, by, c.B, 3); else if(Bdir === 'y') F.arrow(ctx, bx, by+22, bx, by-22, c.B, 3); else F.dotOut(ctx, bx, by, 14, c.B);
    F.label(ctx, 'B', bx, by+34, c.B, 14, 'center');
    var sumMu = 0;
    shapes.forEach(function(s){
      var A = area(s); sumMu += s.dir*A;
      ctx.lineWidth = 2.6; ctx.strokeStyle = c.E; ctx.fillStyle = s.dir > 0 ? 'rgba(110,231,183,.12)' : 'rgba(255,154,77,.14)';
      ctx.beginPath();
      if(s.type === 'circ'){ var cc = toS(g,s.c[0],s.c[1]); ctx.arc(cc[0], cc[1], s.r*g.u, 0, 7); }
      else s.pts.forEach(function(q,k){ var P = toS(g,q[0],q[1]); k ? ctx.lineTo(P[0],P[1]) : ctx.moveTo(P[0],P[1]); });
      ctx.closePath(); ctx.fill(); ctx.stroke();
      var per = [], pts = [], k;
      if(s.type === 'circ'){ for(k = 0; k <= 60; k++){ var an = k/60*2*Math.PI; pts.push([s.c[0]+s.r*Math.cos(an), s.c[1]+s.r*Math.sin(an)]); } }
      else { pts = s.pts.slice(); var sa = 0; for(k = 0; k < pts.length; k++){ var q = pts[(k+1)%pts.length]; sa += pts[k][0]*q[1] - q[0]*pts[k][1]; } if(sa < 0) pts.reverse(); pts.push(pts[0]); }
      var tot = 0; for(k = 1; k < pts.length; k++){ tot += Math.hypot(pts[k][0]-pts[k-1][0], pts[k][1]-pts[k-1][1]); per.push(tot); }
      var nd = Math.max(6, Math.round(tot/1.6));
      ctx.fillStyle = c.S;
      for(var d = 0; d < nd; d++){ var sPos = ((d/nd)*tot + s.dir*t*1.4) % tot; if(sPos < 0) sPos += tot; var seg = 0; while(per[seg] < sPos) seg++;
        var s0 = seg ? per[seg-1] : 0, f = (sPos-s0)/(per[seg]-s0), P0 = pts[seg], P1 = pts[seg+1];
        var XY = toS(g, P0[0]+(P1[0]-P0[0])*f, P0[1]+(P1[1]-P0[1])*f); ctx.beginPath(); ctx.arc(XY[0], XY[1], 2.6, 0, 7); ctx.fill(); }
      var cen = s.type === 'circ' ? s.c : s.pts.reduce(function(a,q){ return [a[0]+q[0]/s.pts.length, a[1]+q[1]/s.pts.length]; }, [0,0]);
      var C = toS(g, cen[0], cen[1]);
      F.label(ctx, s.n, C[0], C[1]-9, c.ink, 15, 'center', '600');
      F.label(ctx, (s.dir > 0 ? '⟲ +k̂' : '⟳ −k̂')+'  '+F.fmt(A,2)+' m²', C[0], C[1]+9, s.dir > 0 ? c.ok : c.E, 11, 'center');
    });
    var muZ = 1*sumMu, B = 1, txt;
    if(Bdir === 'x') txt = 'τ = m_z B (k̂×î) = <b class="hl">'+F.fmt(muZ*B,2)+' ĵ N·m</b></span><span>U = −m·B = <b class="hl">0 J</b> (m ⟂ B)';
    else if(Bdir === 'y') txt = 'τ = m_z B (k̂×ĵ) = <b class="hl">'+F.fmt(-muZ*B,2)+' î N·m</b></span><span>U = <b class="hl">0 J</b> (m ⟂ B)';
    else txt = 'τ = m_z B (k̂×k̂) = <b class="hl">0</b></span><span>U = −m_z B = <b class="hl">'+F.fmt(-muZ*B,2)+' J</b> (agora m ∥ B)';
    out.innerHTML = '<span>Σ m_z = I·(±S) = <b>'+F.fmt(muZ,2)+' A·m²</b></span><span>'+txt+'</span>';
  });
})();

})();
