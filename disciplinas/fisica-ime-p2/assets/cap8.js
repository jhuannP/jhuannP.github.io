/* Física III para IME · Capítulo VIII · Maxwell e ondas
   Widgets: w-desloc (corrente de deslocamento), w-ondaeq (equação de onda),
            w-wave (onda EM 3D com escolha de k e E), w-micro (micro-ondas e chocolate). */
(function(){
"use strict";
var F3=window.F3; if(!F3) return;
function $(root,s){ return root.querySelector(s); }

/* ====================== w-desloc: capacitor carregando ====================== */
(function(){
  var root=document.getElementById('w-desloc'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), sp=new F3.Stage(cvs[1]), S={}, out=$(root,'.w-readout');
  var t=0, paused=false, surf=1, flow=0, aPlate=0.05; /* raio das placas (m), só para o cálculo de B */
  F3.bind(root,S,function(){ t=0; });
  $(root,'[data-act=reset]').onclick=function(){ t=0; flow=0; };
  var pb=$(root,'[data-act=pause]'); pb.onclick=function(){ paused=!paused; pb.classList.toggle('on',paused); pb.textContent=paused?'Continuar':'Pausar'; };
  var b1=$(root,'[data-act=s1]'), b2=$(root,'[data-act=s2]');
  b1.onclick=function(){ surf=1; b1.classList.add('on'); b2.classList.remove('on'); };
  b2.onclick=function(){ surf=2; b2.classList.add('on'); b1.classList.remove('on'); };

  F3.loop(root,function(dt){
    var R=S.R*1e3, C=S.C*1e-6, emf=S.emf, tau=R*C, i0=emf/R, Q=C*emf;
    if(!paused && t<7*tau) t+=dt;
    if(F3.reduce && t===0) t=0.8*tau; /* sem animação: mostra um instante intermediário */
    var ex=Math.exp(-t/tau), i=i0*ex, q=Q*(1-ex), fr=i/i0, qf=q/Q;
    F3.setOut(root,'emf',F3.fmt(emf,1)+' V'); F3.setOut(root,'R',F3.fmt(S.R,1)+' kΩ'); F3.setOut(root,'C',F3.fmt(S.C,0)+' μF');

    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var y0=150, ph=50, yb=h-22, xl=24, xr=w-24, xm=xl+(xr-xl)*0.64, xp1=xm-18, xp2=xm+18, xa=(xl+xp1)/2+6, ry=44;
    /* fios */
    ctx.strokeStyle=c.muted; ctx.lineWidth=3; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(xp1,y0); ctx.lineTo(xl,y0); ctx.lineTo(xl,yb); ctx.lineTo(xr,yb); ctx.lineTo(xr,y0); ctx.lineTo(xp2,y0); ctx.stroke();
    /* bateria no lado esquerdo (+ em cima) */
    var by=(y0+yb)/2+10; ctx.fillStyle=c.bg; ctx.fillRect(xl-14,by-9,28,18);
    ctx.strokeStyle=c.ink; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(xl-14,by-6); ctx.lineTo(xl+14,by-6); ctx.stroke();
    ctx.lineWidth=5; ctx.beginPath(); ctx.moveTo(xl-7,by+6); ctx.lineTo(xl+7,by+6); ctx.stroke();
    F3.label(ctx,'+',xl+18,by-12,c.ink,13); F3.label(ctx,'ε',xl+18,by+8,c.ink,13);
    /* resistor no lado direito */
    var rr=(y0+yb)/2+10; ctx.fillStyle=c.bg; ctx.fillRect(xr-10,rr-24,20,48);
    ctx.strokeStyle=c.ink; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(xr,rr-24);
    for(var k=0;k<6;k++) ctx.lineTo(xr+(k%2?-8:8),rr-20+k*8); ctx.lineTo(xr,rr+24); ctx.stroke();
    F3.label(ctx,'R',xr-14,rr,c.ink,13,'right');
    /* placas */
    ctx.fillStyle=c.E; ctx.fillRect(xp1-5,y0-ph,5,2*ph); ctx.fillStyle=c.B; ctx.fillRect(xp2,y0-ph,5,2*ph);
    var nq=Math.round(qf*6);
    for(k=0;k<nq;k++){ var yy=y0-ph+10+k*(2*ph-20)/5; F3.label(ctx,'+',xp1-14,yy,c.E,12,'center'); F3.label(ctx,'−',xp2+14,yy,c.B,13,'center'); }
    /* campo E entre as placas (cresce com q) */
    var nE=Math.round(qf*5);
    for(k=0;k<nE;k++){ var ye=y0-ph+12+k*(2*ph-24)/4; F3.arrow(ctx,xp1+3,ye,xp2-3,ye,c.E,1.2+1.4*qf,6); }
    /* corrente de condução: pontos andando no circuito */
    flow+=dt*140*fr;
    var path=[[xp2,y0],[xr,y0],[xr,yb],[xl,yb],[xl,y0],[xp1,y0]], segL=[], L=0;
    for(k=0;k<path.length-1;k++){ var d=Math.hypot(path[k+1][0]-path[k][0],path[k+1][1]-path[k][1]); segL.push(d); L+=d; }
    ctx.fillStyle=c.S;
    for(var s=flow%24; s<L; s+=24){ var r=s, j=0; while(j<segL.length-1 && r>segL[j]){ r-=segL[j]; j++; }
      var u=Math.min(1,r/segL[j]), px=path[j][0]+(path[j+1][0]-path[j][0])*u, py=path[j][1]+(path[j+1][1]-path[j][1])*u;
      ctx.globalAlpha=0.25+0.75*fr; ctx.beginPath(); ctx.arc(px,py,2.6,0,7); ctx.fill(); }
    ctx.globalAlpha=1;
    /* caminho de Ampère C (em volta do fio) e a superfície escolhida */
    ctx.save(); ctx.globalAlpha=0.22; ctx.fillStyle=surf===1?c.ok:c.S; ctx.beginPath();
    if(surf===1){ ctx.ellipse(xa,y0,8,ry,0,0,7); }
    else { ctx.moveTo(xa,y0-ry); ctx.bezierCurveTo(xa+30,y0-ry-4,xm-8,y0-ph+2,xm,y0-ph+8); ctx.lineTo(xm,y0+ph-8); ctx.bezierCurveTo(xm-8,y0+ph-2,xa+30,y0+ry+4,xa,y0+ry); ctx.closePath(); }
    ctx.fill(); ctx.restore();
    ctx.strokeStyle=c.ink; ctx.lineWidth=2; ctx.beginPath(); ctx.ellipse(xa,y0,8,ry,0,0,7); ctx.stroke();
    F3.label(ctx,'C',xa-12,y0-ry+4,c.ink,12,'right');
    if(fr>0.03 && xa-xl>44){ F3.arrow(ctx,xl+8,y0-12,xa-14,y0-12,c.S,2,7); F3.label(ctx,'i',(xl+xa)/2-3,y0-24,c.S,13,'center'); }
    /* B tangente ao caminho C (por i) e em volta do vão (por i_d): mesmo tamanho */
    var rb=3+9*fr;
    if(fr>0.02){
      F3.dotOut(ctx,xa,y0-ry,rb,c.B); F3.crossIn(ctx,xa,y0+ry,rb,c.B);
      F3.dotOut(ctx,xm,y0-ph-18,rb,c.B); F3.crossIn(ctx,xm,y0+ph+18,rb,c.B);
    }
    F3.label(ctx,'B em C',xa,y0+ry+22,c.B,11,'center'); F3.label(ctx,'B no vão',xm,y0+ph+40,c.B,11,'center');
    var cs=surf===1?c.ok:c.S;
    F3.label(ctx,surf===1?'S₁ (plana): furada pelo fio → conta i':'S₂ (bolsa): entre as placas → conta i_d',10,14,cs,12);
    F3.label(ctx,'i = '+F3.fmt(i*1e3,3)+' mA   i_d = '+F3.fmt(i*1e3,3)+' mA',10,31,c.ink,12);
    F3.label(ctx,'∮B·dl em C = μ₀ i (S₁) = μ₀ i_d (S₂)',10,48,c.muted,11);
    if(w>460) F3.label(ctx,'t = '+F3.fmt(t,2)+' s',w-12,14,c.ink,12,'right');

    /* gráfico i(t), i_d(t), q(t) */
    var g=sp.ctx, gw=sp.w, gh=sp.h; g.clearRect(0,0,gw,gh);
    var P=F3.plot(g,{x:46,y:20,w:gw-60,h:gh-46},[0,6],[0,1.05],c,{xl:'t / τ',yl:'fração do máximo'});
    F3.curve(g,function(x){return Math.exp(-x);},0,6,P,c.ok,2.6);
    F3.curve(g,function(x){return Math.exp(-x);},0,6,P,c.S,2,[6,6]);
    F3.curve(g,function(x){return 1-Math.exp(-x);},0,6,P,c.E,2);
    var xt=Math.min(6,t/tau); g.strokeStyle=c.ink; g.lineWidth=1; g.beginPath(); g.moveTo(P.X(xt),P.Y(0)); g.lineTo(P.X(xt),P.Y(1.05)); g.stroke();
    F3.label(g,'i (fio)',P.X(0.2),P.Y(0.97),c.ok,11); F3.label(g,'i_d (tracejada) = i',P.X(1.1),P.Y(0.45),c.S,11);
    F3.label(g,'q / Q',P.X(4.6),P.Y(0.88),c.E,11);

    var Bedge=F3.MU0*i/(2*Math.PI*aPlate), dEdt=i/(F3.EPS0*Math.PI*aPlate*aPlate);
    out.innerHTML='<span>t = <b>'+F3.fmt(t,2)+' s</b></span><span>τ = RC = <b>'+F3.fmt(tau,2)+' s</b></span><span>q = <b>'+F3.fmt(q*1e6,0)+' μC</b></span><span>i = (ε/R)e^(−t/τ) = <b class="hl">'+F3.fmt(i*1e3,3)+' mA</b></span><span>i_d = ε₀ dΦ_E/dt = <b class="hl">'+F3.fmt(i*1e3,3)+' mA</b></span><span>B na borda (placas de raio 5 cm) = μ₀i/2πa = <b>'+(Bedge>0?F3.sci(Bedge,2):'0')+' T</b></span><span>dE/dt = <b>'+(dEdt>0?F3.sci(dEdt,2):'0')+' V/(m·s)</b></span>';
  });
})();

/* ====================== w-ondaeq: explorador da equação de onda ====================== */
(function(){
  var root=document.getElementById('w-ondaeq'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), s1=new F3.Stage(cvs[0]), s2=new F3.Stage(cvs[1]), S={}, out=$(root,'.w-readout');
  var tn=0, paused=false, dir=1, ymax=8, rate; /* rate: ns simulados por segundo real (câmera lenta) */
  F3.bind(root,S);
  var db=$(root,'[data-act=dir]'); db.onclick=function(){ dir=-dir; db.textContent=dir>0?'Sentido: +y, cos(ky − ωt)':'Sentido: −y, cos(ky + ωt)'; };
  var pb=$(root,'[data-act=pause]'); pb.onclick=function(){ paused=!paused; pb.classList.toggle('on',paused); pb.textContent=paused?'Continuar':'Pausar'; };
  $(root,'[data-act=ex37]').onclick=function(){ F3.setRange(root,'lam',3,S); F3.setRange(root,'vc',1,S); if(dir<0) db.onclick(); };

  F3.loop(root,function(dt){
    var lam=S.lam, v=S.vc*F3.C, T=lam/v*1e9 /* ns */, k=2*Math.PI/lam, w=2*Math.PI/T /* rad/ns */;
    rate=T/2.5; /* ~2,5 s reais por período, para qualquer λ */
    if(!paused) tn+=dt*rate;
    var y0=S.y0, E=function(y,tt){ return Math.cos(k*y-dir*w*tt); };
    F3.setOut(root,'lam',F3.fmt(lam,1)+' m'); F3.setOut(root,'vc',F3.fmt(S.vc,2)); F3.setOut(root,'y0',F3.fmt(y0,1)+' m');
    var c=F3.W();
    /* foto: E vs y */
    var ctx=s1.ctx; ctx.clearRect(0,0,s1.w,s1.h);
    var P=F3.plot(ctx,{x:40,y:26,w:s1.w-56,h:s1.h-56},[0,ymax],[-1.25,1.25],c,{xl:'y (m)',yl:'E/E₀ · foto t = '+F3.fmt(tn,1)+' ns · '+(dir>0?'→ +y':'← −y')});
    F3.curve(ctx,function(y){return E(y,tn);},0,ymax,P,c.E,2.4);
    for(var m=0;m<ymax;m++){ if(P.X(m)>s1.w-16-40) continue; F3.label(ctx,String(m),P.X(m),P.Y(-1.25)+11,c.muted,10,'center'); }
    ctx.setLineDash([4,4]); ctx.strokeStyle=c.ok; ctx.lineWidth=1.2; ctx.beginPath(); ctx.moveTo(P.X(y0),P.Y(1.25)); ctx.lineTo(P.X(y0),P.Y(-1.25)); ctx.stroke(); ctx.setLineDash([]);
    F3.label(ctx,'y₀',P.X(y0)+4,P.Y(-1.1),c.ok,11);
    /* crista acompanhada: fase 0 → y = dir*(ω/k)t, reduzida ao intervalo */
    var yc=dir*(w/k)*tn; yc=((yc%lam)+lam)%lam; while(yc+lam<=ymax*0.45) yc+=lam;
    if(yc<=ymax){ ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(yc),P.Y(1),5,0,7); ctx.fill(); }
    /* marca de λ entre duas cristas */
    var ya=yc-lam>=0?yc-lam:yc, yb2=ya+lam;
    if(yb2<=ymax){ var yy=P.Y(1.12); F3.arrow(ctx,(P.X(ya)+P.X(yb2))/2,yy,P.X(ya),yy,c.ink,1.2,6); F3.arrow(ctx,(P.X(ya)+P.X(yb2))/2,yy,P.X(yb2),yy,c.ink,1.2,6); F3.label(ctx,'λ',(P.X(ya)+P.X(yb2))/2,yy-9,c.ink,12,'center'); }
    

    /* filme: E vs t em y0 */
    var g=s2.ctx; g.clearRect(0,0,s2.w,s2.h);
    var Tw=3*T, t0=tn-Tw; /* janela: últimos 3 períodos */
    var Q=F3.plot(g,{x:40,y:26,w:s2.w-56,h:s2.h-56},[t0,tn],[-1.25,1.25],c,{xl:'t (ns), últimos 3 períodos',yl:'E/E₀ no ponto y₀'});
    F3.curve(g,function(tt){return E(y0,tt);},t0,tn,Q,c.B,2.4);
    g.fillStyle=c.ok; g.beginPath(); g.arc(Q.X(tn),Q.Y(E(y0,tn)),4.5,0,7); g.fill();
    /* marca de T: duas cristas mais recentes */
    /* instante de uma crista em y0: fase ky0 − dir·ω·t = 2πn */
    var tc=(k*y0-2*Math.PI*Math.round((k*y0-dir*w*tn)/(2*Math.PI)))*dir/w;
    while(tc>tn) tc-=T; while(tc+T<=tn) tc+=T;
    if(tc-T>=t0){ var ty=Q.Y(1.12); F3.arrow(g,(Q.X(tc-T)+Q.X(tc))/2,ty,Q.X(tc-T),ty,c.ink,1.2,6); F3.arrow(g,(Q.X(tc-T)+Q.X(tc))/2,ty,Q.X(tc),ty,c.ink,1.2,6); F3.label(g,'T',(Q.X(tc-T)+Q.X(tc))/2,ty-9,c.ink,12,'center'); }

    /* conferência numérica da equação de onda em (y0, tn) */
    var hy=1e-3*lam, ht=1e-3*T, e0=E(y0,tn);
    var d2y=(E(y0+hy,tn)-2*e0+E(y0-hy,tn))/(hy*hy); /* m⁻² */
    var d2t=(E(y0,tn+ht)-2*e0+E(y0,tn-ht))/(ht*ht)*1e18; /* s⁻² */
    var rhs=d2t/(v*v);
    out.innerHTML='<span>λ = <b>'+F3.fmt(lam,2)+' m</b></span><span>T = <b>'+F3.fmt(T,2)+' ns</b></span><span>f = 1/T = <b>'+F3.fmt(1e3/T,1)+' MHz</b></span><span>v = λ/T = <b class="hl">'+F3.sci(v,3)+' m/s</b></span><span>ω/k = <b class="hl">'+F3.sci(w*1e9/k,3)+' m/s</b></span><span>∂²E/∂y² = <b>'+F3.fmt(d2y,3)+' m⁻²</b></span><span>(1/v²)∂²E/∂t² = <b>'+F3.fmt(rhs,3)+' m⁻²</b></span>';
  });
})();

/* ====================== w-wave: onda EM 3D com escolha de k̂ e E ====================== */
(function(){
  var root=document.getElementById('w-wave'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), sp=new F3.Stage(cvs[1]), S={}, out=$(root,'.w-readout');
  var paused=false, ph=0;
  var AX={'+x':[1,0,0],'-x':[-1,0,0],'+y':[0,1,0],'-y':[0,-1,0],'+z':[0,0,1],'-z':[0,0,-1]};
  var VER={x:'î',y:'ĵ',z:'k̂'};
  var selK=$(root,'select[data-sel=k]'), selE=$(root,'select[data-sel=e]'), note='';
  F3.bind(root,S);
  function cross(a,b){ return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]; }
  function name(v){ var ax=v[0]?'x':(v[1]?'y':'z'), s=v[0]+v[1]+v[2]; return (s<0?'−':'+')+VER[ax]; }
  function fix(changed){
    var k=AX[selK.value], e=AX[selE.value];
    if(Math.abs(k[0]*e[0]+k[1]*e[1]+k[2]*e[2])>0.5){
      /* E paralelo a k não é onda transversal: escolhe o primeiro eixo perpendicular */
      var opts=['+x','+y','+z']; for(var i=0;i<3;i++){ var o=AX[opts[i]]; if(Math.abs(o[0]*k[0]+o[1]*k[1]+o[2]*k[2])<0.5){ selE.value=opts[i]; break; } }
      note=changed==='e'?'E não pode ser paralelo a k̂ (onda transversal): ajustei E.':'E ficaria paralelo a k̂: ajustei E para um eixo perpendicular.';
    } else note='';
  }
  selK.addEventListener('change',function(){ fix('k'); });
  selE.addEventListener('change',function(){ fix('e'); });
  var pb=$(root,'[data-act=pause]'); pb.onclick=function(){ paused=!paused; pb.classList.toggle('on',paused); pb.textContent=paused?'Continuar':'Pausar'; };
  $(root,'[data-act=exam]').onclick=function(){ selK.value='+z'; selE.value='-y'; F3.setRange(root,'B0',-8,S); F3.setRange(root,'f',8,S); note='Exercício 3 do simulado: B = (10⁻⁸ T) cos(kz − ωt) î, f = 100 MHz.'; };
  $(root,'[data-act=ex37]').onclick=function(){ selK.value='+y'; selE.value='+x'; note='Exercício 37: E = E₀ cos(ky − ωt) x̂ → B em −ẑ, S em +ŷ.'; };
  var mu0=F3.MU0, c0=F3.C;

  F3.loop(root,function(dt){
    if(!paused) ph+=dt*2.2;
    var kv=AX[selK.value], ev=AX[selE.value], bv=cross(kv,ev), sg=kv[0]+kv[1]+kv[2], axk=kv[0]?'x':(kv[1]?'y':'z');
    var B0=Math.pow(10,S.B0), f=Math.pow(10,S.f), E0=c0*B0, Smax=E0*B0/mu0, I=Smax/2, lam=c0/f, kk=2*Math.PI/lam, w0=2*Math.PI*f;
    F3.setOut(root,'B0',F3.sci(B0,2)+' T'); F3.setOut(root,'f',(f>=1e9?F3.fmt(f/1e9,2)+' GHz':F3.fmt(f/1e6,1)+' MHz')); F3.setOut(root,'yaw',S.yaw+'°');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var yaw=S.yaw*Math.PI/180, pitch=0.38, sc=Math.min(w/9.5,h/5), ox=w/2, oy=h/2+12;
    function P(x,y,z){ var x1=x*Math.cos(yaw)+z*Math.sin(yaw), z1=-x*Math.sin(yaw)+z*Math.cos(yaw); var y2=y*Math.cos(pitch)-z1*Math.sin(pitch); return [ox+x1*sc, oy-y2*sc]; }
    function Pv(v,s){ return P(v[0]*s,v[1]*s,v[2]*s); }
    var Z=4.0, A=1.3;
    /* eixos x, y, z */
    [['x',[1,0,0]],['y',[0,1,0]],['z',[0,0,1]]].forEach(function(a){ var p1=Pv(a[1],-0.3), p2=Pv(a[1],2.1); F3.arrow(ctx,p1[0],p1[1],p2[0],p2[1],c.muted,1.2,7); F3.label(ctx,a[0],p2[0]+5,p2[1]-7,c.muted,12); });
    /* eixo de propagação */
    var q1=Pv(kv,-Z), q2=Pv(kv,Z+0.5); ctx.strokeStyle=c.grid; ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(q1[0],q1[1]); ctx.lineTo(q2[0],q2[1]); ctx.stroke();
    function val(s){ var q=sg*s; return Math.cos(Math.PI*q/(Z/2)-sg*ph); } /* cos(k·q ∓ ωt), q = coordenada no eixo */
    function pass(vec,col){
      var N=48, i, s, v, b, e;
      ctx.strokeStyle=col; ctx.globalAlpha=0.5; ctx.lineWidth=1.3;
      for(i=0;i<=N;i++){ s=-Z+2*Z*i/N; v=val(s); b=Pv(kv,s); e=P(kv[0]*s+vec[0]*A*v, kv[1]*s+vec[1]*A*v, kv[2]*s+vec[2]*A*v); ctx.beginPath(); ctx.moveTo(b[0],b[1]); ctx.lineTo(e[0],e[1]); ctx.stroke(); }
      ctx.globalAlpha=1; ctx.lineWidth=2.6; ctx.beginPath();
      for(i=0;i<=160;i++){ s=-Z+2*Z*i/160; v=val(s); e=P(kv[0]*s+vec[0]*A*v, kv[1]*s+vec[1]*A*v, kv[2]*s+vec[2]*A*v); i?ctx.lineTo(e[0],e[1]):ctx.moveTo(e[0],e[1]); }
      ctx.stroke();
    }
    pass(bv,c.B); pass(ev,c.E);
    /* Poynting ao longo de k̂ */
    for(var j=0;j<6;j++){ var s0=-Z+0.4+j*(2*Z-0.8)/5, vv=val(s0), L=0.75*vv*vv; if(L>0.05){ var a1=Pv(kv,s0), a2=Pv(kv,s0+L); F3.arrow(ctx,a1[0],a1[1],a2[0],a2[1],c.S,3,8); } }
    var arg='k'+axk+(sg>0?' − ':' + ')+'ωt';
    F3.label(ctx,'E = E₀ cos('+arg+') ('+name(ev)+')',12,18,c.E,13);
    F3.label(ctx,'B = B₀ cos('+arg+') ('+name(bv)+')   [B = (1/c) k̂ × E]',12,37,c.B,13);
    F3.label(ctx,'S = E×B/μ₀ aponta para '+name(kv)+' (propagação)',12,56,c.S,13);
    if(note) F3.label(ctx,note,12,h-12,c.ok,11);
    else F3.label(ctx,'λ = '+(lam>=1?F3.fmt(lam,2)+' m':F3.fmt(lam*100,1)+' cm')+' (dois comprimentos de onda na tela)',w-10,h-12,c.muted,11,'right');

    /* S(t) num ponto fixo */
    var g=sp.ctx, gw=sp.w, gh=sp.h; g.clearRect(0,0,gw,gh);
    var x0=70,y0=gh-24,pw=gw-x0-14,phh=gh-44;
    g.strokeStyle=c.grid; g.lineWidth=1; g.strokeRect(x0,y0-phh,pw,phh);
    g.strokeStyle=c.S; g.lineWidth=2.2; g.beginPath();
    for(var i2=0;i2<=200;i2++){ var tt=i2/200*3*2*Math.PI, v2=Math.cos(-tt+ph); var X=x0+i2/200*pw, Y=y0-v2*v2*phh*0.9; i2?g.lineTo(X,Y):g.moveTo(X,Y); }
    g.stroke();
    g.setLineDash([5,5]); g.strokeStyle=c.ok; g.beginPath(); g.moveTo(x0,y0-0.45*phh); g.lineTo(x0+pw,y0-0.45*phh); g.stroke(); g.setLineDash([]);
    F3.label(g,'S_máx',x0-6,y0-0.9*phh,c.S,11,'right'); F3.label(g,'I = S_máx/2',x0-6,y0-0.45*phh,c.ok,11,'right'); F3.label(g,'0',x0-6,y0,c.muted,11,'right');
    F3.label(g,'|S(t)| na origem, três períodos: sempre ≥ 0, média = metade do pico',x0+6,y0-phh+11,c.muted,11);

    out.innerHTML='<span>E₀ = cB₀ = <b>'+(E0<1?F3.fmt(E0*1000,1)+' mV/m':F3.fmt(E0,2)+' V/m')+'</b></span><span>S_máx = E₀B₀/μ₀ = <b class="hl">'+(Smax<1?F3.fmt(Smax*1000,1)+' mW/m²':F3.fmt(Smax,2)+' W/m²')+'</b></span><span>I = S_máx/2 = <b class="hl">'+(I<1?F3.fmt(I*1000,1)+' mW/m²':F3.fmt(I,2)+' W/m²')+'</b></span><span>ω = 2πf = <b>'+F3.sci(w0,2)+' s⁻¹</b></span><span>k = 2π/λ = <b>'+(kk<100?F3.fmt(kk,2):F3.sci(kk,2))+' m⁻¹</b></span><span>λ = c/f = <b>'+(lam>=1?F3.fmt(lam,2)+' m':F3.fmt(lam*100,1)+' cm')+'</b></span>';
  });
})();

/* ====================== w-micro: micro-ondas e chocolate ====================== */
(function(){
  var root=document.getElementById('w-micro'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=$(root,'.w-readout');
  F3.bind(root,S,draw);
  if(window.ResizeObserver) new ResizeObserver(function(){ draw(); }).observe(st.c);
  var mo=new MutationObserver(function(){ draw(); }); mo.observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  function draw(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var x0=30, x1=w-30, cmPx=(x1-x0)/30, dx=S.dx, yb=h*0.6;
    ctx.strokeStyle=c.E; ctx.lineWidth=2; ctx.beginPath();
    for(var i=0;i<=300;i++){ var xc=i/300*30, v=Math.pow(Math.cos(Math.PI*xc/dx),2); var X=x0+xc*cmPx, Y=yb-26-v*70; i?ctx.lineTo(X,Y):ctx.moveTo(X,Y); }
    ctx.stroke();
    F3.label(ctx,'|E|² dentro do forno (onda estacionária)',x0,16,c.E,12);
    ctx.fillStyle='#5a3423'; ctx.fillRect(x0,yb,x1-x0,34);
    ctx.strokeStyle='#3b2015'; ctx.lineWidth=1; for(var xc2=0;xc2<=30;xc2+=2.5){ ctx.beginPath(); ctx.moveTo(x0+xc2*cmPx,yb); ctx.lineTo(x0+xc2*cmPx,yb+34); ctx.stroke(); }
    for(var n=0;n*dx<=30;n++){ var X2=x0+n*dx*cmPx, gr=ctx.createRadialGradient(X2,yb+17,2,X2,yb+17,22); gr.addColorStop(0,'rgba(196,132,86,.95)'); gr.addColorStop(1,'rgba(196,132,86,0)'); ctx.fillStyle=gr; ctx.beginPath(); ctx.arc(X2,yb+17,22,0,7); ctx.fill(); }
    var a=x0+dx*cmPx, b=x0+2*dx*cmPx;
    if(b<x1+1){ F3.arrow(ctx,(a+b)/2,yb+50,a,yb+50,c.ink,1.5,7); F3.arrow(ctx,(a+b)/2,yb+50,b,yb+50,c.ink,1.5,7); F3.label(ctx,'Δx = '+F3.fmt(dx,1)+' cm = λ/2',(a+b)/2,yb+64,c.ink,12,'center'); }
    F3.label(ctx,'barra de chocolate (30 cm); manchas claras = derretido',x0,yb-8,c.muted,11);
    var f=S.fm*1e9, cc=2*dx/100*f;
    F3.setOut(root,'dx',F3.fmt(dx,1)+' cm'); F3.setOut(root,'fm',F3.fmt(S.fm,2)+' GHz');
    out.innerHTML='<span>λ = 2Δx = <b>'+F3.fmt(2*dx,1)+' cm</b></span><span>c = λf = <b class="hl">'+F3.sci(cc,2)+' m/s</b></span><span>erro vs 3,00×10⁸: <b>'+F3.fmt(100*(cc-2.998e8)/2.998e8,1)+'%</b></span>';
  }
  draw();
})();

})();
