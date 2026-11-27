/* Capítulo VI · Indução magnética — widgets: w-ima, w-haste, w-ac, w-rail, w-tube */
(function(){
"use strict";
var F3 = window.F3;
if(!F3) return;
function $(id){ return document.getElementById(id); }
function clamp(x,a,b){ return Math.max(a,Math.min(b,x)); }

/* ---------------------------------------------------------------
   W1 · ímã e bobina (quick quiz)
   Bobina com eixo em x, sentido positivo de circulação ligado a n = +x.
   Fluxo de um dipolo pontual no eixo através de uma espira de raio a:
   Φ = μ0 m a² / (2 (a² + d²)^{3/2})  (mesmo sinal dos dois lados).
---------------------------------------------------------------- */
(function(){
  var root=$('w-ima'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), out=root.querySelector('.w-readout');
  var X0=-0.24, X1=0.26, xc=0.02, Lc=0.07, a=0.015, Nturns=200, K=24, m0=1.0, Rtot=10, lm=0.05;
  var xm=-0.15, s=1, mode='idle', target=0, speed=0.22, drag=false, last=performance.now();
  var hist=[], tt=0, eps=0, I=0;
  function flux(x){ var sum=0; for(var k=0;k<K;k++){ var xk=xc-Lc/2+Lc*(k+0.5)/K, d=xk-x; sum+=F3.MU0*m0*a*a/(2*Math.pow(a*a+d*d,1.5)); } return s*sum*Nturns/K; }
  var PhiMax=Math.abs(flux(xc)); s=1;
  // escala típica de fem: |dΦ/dx|max × 0,25 m/s
  var gmax=0; for(var i=0;i<200;i++){ var x=X0+(X1-X0)*i/200; gmax=Math.max(gmax,Math.abs(flux(x+1e-4)-flux(x-1e-4))/2e-4); }
  var epsScale=gmax*0.25, Iscale=epsScale/Rtot;
  var Phi=flux(xm);
  function geo(){ var w=st.w; var L=40, Rr=w-20; return {X:function(x){return L+(x-X0)/(X1-X0)*(Rr-L);}, inv:function(px){return X0+(px-L)/(Rr-L)*(X1-X0);}, y:105}; }
  function setMode(m,from,to){ mode=m; if(from!==undefined) xm=from; target=to; Phi=flux(xm); }
  root.querySelector('[data-act=in]').onclick=function(){ setMode('auto',-0.17,xc); };
  root.querySelector('[data-act=out]').onclick=function(){ setMode('auto',xc,-0.17); };
  root.querySelector('[data-act=through]').onclick=function(){ setMode('auto',-0.19,0.22); };
  var fb=root.querySelector('[data-act=flip]');
  fb.onclick=function(){ s=-s; Phi=flux(xm); fb.textContent=s>0?'Virar o ímã (S para a bobina)':'Virar o ímã (N para a bobina)'; };
  var cv=cvs[0];
  function px(e){ var r=cv.getBoundingClientRect(); return e.clientX-r.left; }
  cv.addEventListener('pointerdown',function(e){ var g=geo(); if(Math.abs(px(e)-g.X(xm))<60){ drag=true; mode='idle'; try{cv.setPointerCapture(e.pointerId);}catch(_){} } });
  cv.addEventListener('pointermove',function(e){ if(!drag) return; var g=geo(); xm=clamp(g.inv(px(e)),X0+lm/2,X1-lm/2); });
  function up(){ drag=false; }
  cv.addEventListener('pointerup',up); cv.addEventListener('pointercancel',up);

  F3.loop(root,function(){
    var now=performance.now(), dt=Math.min(0.05,(now-last)/1000); last=now;
    if(mode==='auto'){ var dir=target>xm?1:-1; xm+=dir*speed*dt; if((target-xm)*dir<=0){ xm=target; mode='idle'; } }
    var Pn=flux(xm), raw=dt>0?-(Pn-Phi)/dt:0; Phi=Pn;
    eps+=(raw-eps)*Math.min(1,dt*20); if(Math.abs(eps)<epsScale*1e-3) eps=0;
    I=eps/Rtot; tt+=dt; hist.push([tt,Phi,eps]); while(hist.length&&hist[0][0]<tt-6) hist.shift();
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h, g=geo(), ya=g.y; ctx.clearRect(0,0,w,h);
    // eixo
    ctx.strokeStyle=c.grid; ctx.lineWidth=1; ctx.setLineDash([4,4]); ctx.beginPath(); ctx.moveTo(10,ya); ctx.lineTo(w-10,ya); ctx.stroke(); ctx.setLineDash([]);
    var xl=g.X(xc-Lc/2), xr=g.X(xc+Lc/2), ry=46, nd=12, q;
    var copper='#e08a4f';
    // metades de trás das espiras
    ctx.strokeStyle='rgba(224,138,79,.35)'; ctx.lineWidth=2;
    for(q=0;q<nd;q++){ var xq=xl+(xr-xl)*(q+0.5)/nd; ctx.beginPath(); ctx.ellipse(xq,ya,6,ry,0,Math.PI/2,3*Math.PI/2); ctx.stroke(); }
    // ímã
    var mx=g.X(xm), mw=g.X(xm+lm/2)-g.X(xm-lm/2);
    var leftCol=s>0?'#4a7bd9':'#d94a4a', rightCol=s>0?'#d94a4a':'#4a7bd9';
    ctx.fillStyle=leftCol; ctx.fillRect(mx-mw/2,ya-13,mw/2,26); ctx.fillStyle=rightCol; ctx.fillRect(mx,ya-13,mw/2,26);
    F3.label(ctx,s>0?'S':'N',mx-mw/4,ya,'#fff',13,'center','600'); F3.label(ctx,s>0?'N':'S',mx+mw/4,ya,'#fff',13,'center','600');
    if(drag||Math.abs(mx-g.X(-0.15))<4) F3.label(ctx,'arraste',mx,ya-24,c.muted,11,'center');
    // metades da frente e setas de corrente
    var Ir=clamp(I/Iscale,-1.5,1.5);
    for(q=0;q<nd;q++){ var xf=xl+(xr-xl)*(q+0.5)/nd; ctx.strokeStyle=copper; ctx.lineWidth=2.6; ctx.beginPath(); ctx.ellipse(xf,ya,6,ry,0,-Math.PI/2,Math.PI/2); ctx.stroke(); }
    if(Math.abs(Ir)>0.04){ for(q=1;q<nd;q+=3){ var xa=xl+(xr-xl)*(q+0.5)/nd+6; var L2=8+10*Math.min(1,Math.abs(Ir)); if(Ir>0) F3.arrow(ctx,xa,ya+ry*0.55-L2/2,xa,ya+ry*0.55+L2/2,c.S,2,6); else F3.arrow(ctx,xa,ya+ry*0.55+L2/2,xa,ya+ry*0.55-L2/2,c.S,2,6); } }
    // setas de campo no centro da bobina
    var xcp=g.X(xc), Bl=clamp(Phi/PhiMax,-1,1)*48;
    if(Math.abs(Bl)>2) F3.arrow(ctx,xcp-Bl/2,ya-ry-16,xcp+Bl/2,ya-ry-16,c.B,3,9);
    F3.label(ctx,'B do ímã',xcp,ya-ry-32,c.B,11,'center');
    var Bi=clamp(Ir,-1,1)*48;
    if(Math.abs(Bi)>2) F3.arrow(ctx,xcp-Bi/2,ya+ry+16,xcp+Bi/2,ya+ry+16,c.E,3,9);
    F3.label(ctx,'B induzido',xcp,ya+ry+32,c.E,11,'center');
    // polos induzidos nas faces
    if(Math.abs(Ir)>0.06){ var leftN=I<0; F3.label(ctx,leftN?'N':'S',xl-16,ya-ry+6,leftN?'#ff7b7b':'#8fb3ff',16,'center','600'); F3.label(ctx,leftN?'S':'N',xr+16,ya-ry+6,leftN?'#8fb3ff':'#ff7b7b',16,'center','600'); }
    // fios até o galvanômetro
    var gx=w-90, gy=h-48;
    ctx.strokeStyle=c.muted; ctx.lineWidth=1.5; ctx.beginPath(); ctx.moveTo(xl+3,ya+ry); ctx.lineTo(xl+3,h-12); ctx.lineTo(gx-30,h-12); ctx.moveTo(xr,ya+ry); ctx.lineTo(xr,h-24); ctx.lineTo(gx-60,h-24); ctx.stroke();
    // LEDs em antiparalelo
    var ledG=I>0?Math.min(1,I/Iscale*2):0, ledR=I<0?Math.min(1,-I/Iscale*2):0;
    [[gx-60,h-24,'rgba(110,231,183,','verde (+)',ledG],[gx-30,h-12,'rgba(255,107,138,','vermelho (−)',ledR]].forEach(function(L){
      ctx.fillStyle=L[2]+(0.18+0.82*L[4])+')'; ctx.beginPath(); ctx.arc(L[0],L[1]-14,7,0,7); ctx.fill();
      if(L[4]>0.05){ ctx.fillStyle=L[2]+(0.25*L[4])+')'; ctx.beginPath(); ctx.arc(L[0],L[1]-14,16,0,7); ctx.fill(); }
    });
    F3.label(ctx,'LEDs',gx-45,h-48,c.muted,10,'center');
    // galvanômetro
    ctx.strokeStyle=c.ink; ctx.lineWidth=1.6; ctx.beginPath(); ctx.arc(gx+20,gy+20,40,Math.PI,2*Math.PI); ctx.closePath(); ctx.stroke();
    for(var tk=-4;tk<=4;tk++){ var an=-Math.PI/2+tk*0.22; ctx.beginPath(); ctx.moveTo(gx+20+34*Math.cos(an),gy+20+34*Math.sin(an)); ctx.lineTo(gx+20+40*Math.cos(an),gy+20+40*Math.sin(an)); ctx.stroke(); }
    var na=-Math.PI/2+clamp(Ir,-1.2,1.2)*0.85;
    ctx.strokeStyle=c.neg; ctx.lineWidth=2.4; ctx.beginPath(); ctx.moveTo(gx+20,gy+20); ctx.lineTo(gx+20+34*Math.cos(na),gy+20+34*Math.sin(na)); ctx.stroke();
    F3.label(ctx,'G',gx+20,gy+10,c.muted,11,'center'); F3.label(ctx,'−',gx-14,gy+14,c.muted,12,'center'); F3.label(ctx,'+',gx+54,gy+14,c.muted,12,'center');
    F3.label(ctx,'n = +x (sentido positivo)',12,16,c.muted,11);
    // gráfico
    var gc=gp.ctx, gw=gp.w, gh=gp.h; gc.clearRect(0,0,gw,gh);
    var em=epsScale*1.6; hist.forEach(function(p){ em=Math.max(em,Math.abs(p[2])*1.1); });
    var P1=F3.plot(gc,{x:44,y:14,w:gw-58,h:(gh-44)/2},[tt-6,tt],[-PhiMax*1.1,PhiMax*1.1],c,{yl:'Φ (fluxo total)'});
    var P2=F3.plot(gc,{x:44,y:30+(gh-44)/2,w:gw-58,h:(gh-44)/2},[tt-6,tt],[-em,em],c,{yl:'ε = −dΦ/dt',xl:'últimos 6 s'});
    [[P1,1,c.B],[P2,2,c.E]].forEach(function(T){ gc.strokeStyle=T[2]; gc.lineWidth=2; gc.beginPath(); hist.forEach(function(p,k){ var X=T[0].X(p[0]),Y=T[0].Y(p[T[1]]); k?gc.lineTo(X,Y):gc.moveTo(X,Y); }); gc.stroke(); });
    // leitura
    var facePole, magPole, side;
    if(xm<xc){ facePole=I<0?'N':'S'; magPole=s>0?'N':'S'; side='esquerda'; } else { facePole=I<0?'S':'N'; magPole=s>0?'S':'N'; side='direita'; }
    var still=Math.abs(I)<Iscale*0.04;
    var rel=still?'nenhuma força (fluxo constante)':(facePole===magPole?'<b class="hl">repele</b> o ímã':'<b class="hl">atrai</b> o ímã');
    var sense=still?'—':(I>0?'horário':'anti-horário');
    out.innerHTML='<span>Φ = <b>'+F3.fmt(Phi*1e3,2)+' mWb</b></span><span>ε = <b>'+F3.fmt(eps*1e3,0)+' mV</b></span><span>I = <b>'+F3.fmt(I*1e3,1)+' mA</b></span>'+
      '<span>corrente vista da esquerda: <b>'+sense+'</b></span><span>face '+side+' da bobina: '+(still?'<b>sem polo</b>':'<b>'+facePole+'</b> ⇒ '+rel)+'</span>';
  });
})();

/* ---------------------------------------------------------------
   W2 · gerador de haste deslizante (Exercício 29), B = −B k (entrando)
---------------------------------------------------------------- */
(function(){
  var root=$('w-haste'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  var x=0.6, vcur=0, mode='push', qph=0, Pref=1e-9;
  F3.bind(root,S,function(k){ Pref=1e-9; if(k==='v'&&mode==='free'){ vcur=S.v; } });
  vcur=S.v;
  var bp=root.querySelector('[data-act=push]'), bf=root.querySelector('[data-act=free]');
  bp.onclick=function(){ mode='push'; bp.classList.add('on'); bf.classList.remove('on'); Pref=1e-9; };
  bf.onclick=function(){ mode='free'; vcur=S.v; if(x>2.4) x=0.5; bf.classList.add('on'); bp.classList.remove('on'); Pref=1e-9; };
  F3.loop(root,function(dt){
    var B=S.B,h=S.h,R=S.R,m=S.m, slow=0.5, sdt=dt*slow, tau=m*R/(B*B*h*h);
    if(mode==='push'){ vcur=S.v; x+=vcur*sdt; if(x>3.0) x=0.45; }
    else { vcur*=Math.exp(-sdt/tau); x+=vcur*sdt; if(x>3.0){ x=3.0; } if(vcur<1e-3) vcur=0; }
    var eps=B*h*vcur, i=eps/R, F=B*B*h*h*vcur/R, PJ=i*i*R, Pm=mode==='push'?F*vcur:0;
    Pref=Math.max(Pref,PJ,Pm);
    F3.setOut(root,'B',F3.fmt(B,1)+' T'); F3.setOut(root,'h',F3.fmt(h,2)+' m'); F3.setOut(root,'v',F3.fmt(S.v,1)+' m/s'); F3.setOut(root,'R',F3.fmt(R,1)+' Ω'); F3.setOut(root,'m',F3.fmt(m,2)+' kg');
    var c=F3.W(), ctx=st.ctx, w=st.w, H=st.h; ctx.clearRect(0,0,w,H);
    var barW=w<520?0:130, ppm=Math.min((w-barW-80)/3.2,190), left=46, yc=H/2+6, hp=h*ppm, top=yc-hp/2, bot=yc+hp/2;
    // campo entrando
    ctx.globalAlpha=0.45; for(var yy=22;yy<H-8;yy+=30){ for(var xx=left+14;xx<w-barW-10;xx+=30){ F3.crossIn(ctx,xx,yy,4,c.B); } } ctx.globalAlpha=1;
    var rx=left+x*ppm;
    ctx.fillStyle='rgba(95,212,255,.10)'; ctx.fillRect(left,top,rx-left,hp);
    // trilhos e resistor
    ctx.strokeStyle=c.muted; ctx.lineWidth=5; ctx.beginPath(); ctx.moveTo(w-barW-10,top); ctx.lineTo(left,top); ctx.lineTo(left,top+hp*0.25); ctx.moveTo(left,bot-hp*0.25); ctx.lineTo(left,bot); ctx.lineTo(w-barW-10,bot); ctx.stroke();
    ctx.strokeStyle=c.ink; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(left,top+hp*0.25); var zz=6, zy=hp*0.5/zz; for(var z=0;z<=zz;z++){ ctx.lineTo(left+(z%2?9:-9),top+hp*0.25+z*zy); } ctx.lineTo(left,bot-hp*0.25); ctx.stroke();
    F3.label(ctx,'R',left-22,yc,c.ink,14,'center','600');
    // haste
    ctx.fillStyle=c.E; ctx.fillRect(rx-5,top-12,10,hp+24);
    F3.label(ctx,'A',rx+10,top-14,c.ink,13,'left','600'); F3.label(ctx,"A'",rx+10,bot+14,c.ink,13,'left','600');
    // corrente anti-horária: sobe na haste, esquerda no trilho de cima, desce no resistor, direita no de baixo
    qph+=dt*i*4; var per=2*(rx-left)+2*hp, n=Math.max(6,Math.round(per/34));
    if(i>1e-6){ ctx.fillStyle=c.S; for(var k=0;k<n;k++){ var sPos=((k/n+qph)%1)*per, px, py;
      if(sPos<hp){ px=rx; py=bot-sPos; } else if(sPos<hp+(rx-left)){ px=rx-(sPos-hp); py=top; } else if(sPos<2*hp+(rx-left)){ px=left; py=top+(sPos-hp-(rx-left)); } else { px=left+(sPos-2*hp-(rx-left)); py=bot; }
      ctx.beginPath(); ctx.arc(px,py,3,0,7); ctx.fill(); }
      F3.arrow(ctx,rx-16,yc+22,rx-16,yc-22,c.S,2.2,8); F3.label(ctx,'i',rx-28,yc,c.S,14,'center','600'); }
    // forças e velocidade
    var Fs=F/Math.max(1e-9,B*B*h*h*Math.max(S.v,0.5)/R)*60;
    if(F>1e-6) F3.arrow(ctx,rx-8,yc-hp*0.25,rx-8-Math.min(90,Fs),yc-hp*0.25,c.neg,3.2,10);
    F3.label(ctx,'Fm',rx-14-Math.min(90,Fs),yc-hp*0.25-14,c.neg,12,'center','600');
    if(mode==='push'&&F>1e-6){ F3.arrow(ctx,rx+8,yc+hp*0.25,rx+8+Math.min(90,Fs),yc+hp*0.25,c.ok,3.2,10); F3.label(ctx,'F ext',rx+14+Math.min(90,Fs),yc+hp*0.25-14,c.ok,12,'center','600'); }
    if(vcur>1e-3) F3.arrow(ctx,rx+8,yc,rx+8+Math.min(70,vcur*16),yc,c.ink,2.4,9);
    F3.label(ctx,'B = −B k (entrando)',w-barW-14,12,c.B,11,'right');
    // barras de potência
    if(barW){ var bx=w-barW+10, bw=barW-24, bh=H-80;
      var p1=mode==='push'?Pm:PJ, lab1=mode==='push'?'P mec = F·v':'−dK/dt';
      [[bx,p1,lab1,c.ok],[bx+bw/2+6,PJ,'P Joule = i²R',c.E]].forEach(function(T){
        var hh=bh*T[1]/Pref; ctx.fillStyle=T[3]; ctx.fillRect(T[0],H-34-hh,bw/2-6,hh);
        ctx.strokeStyle=c.grid; ctx.strokeRect(T[0],H-34-bh,bw/2-6,bh);
        F3.label(ctx,T[2],T[0]+(bw/2-6)/2,H-20,c.muted,9.5,'center'); });
      F3.label(ctx,'potências',bx+bw/2,24,c.ink,12,'center','600'); }
    out.innerHTML='<span>ε = Bhv = <b>'+F3.fmt(eps,3)+' V</b></span><span>i = <b>'+F3.fmt(i,3)+' A</b> (anti-horário, sobe A′→A)</span><span>Fm = <b class="hl">−'+F3.fmt(F,3)+' î N</b></span>'+
      (mode==='push'?'<span>P mec = <b>'+F3.fmt(Pm,3)+' W</b></span>':'<span>v = <b>'+F3.fmt(vcur,2)+' m/s</b>, τ = mR/(Bh)² = <b>'+F3.fmt(tau,2)+' s</b></span>')+'<span>P Joule = <b>'+F3.fmt(PJ,3)+' W</b></span>';
  });
})();

/* ---------------------------------------------------------------
   W3 · gerador de corrente alternada (Exercício 31)
---------------------------------------------------------------- */
(function(){
  var root=$('w-ac'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), S={}, out=root.querySelector('.w-readout');
  var th=0.3, paused=false;
  F3.bind(root,S);
  root.querySelector('[data-act=br]').onclick=function(){ F3.setRange(root,'f',60,S); };
  var pb=root.querySelector('[data-act=pause]'); pb.onclick=function(){ paused=!paused; pb.classList.toggle('on',paused); pb.textContent=paused?'Continuar':'Pausar'; };
  F3.loop(root,function(dt){
    var N=S.N,B=S.B,A=S.A*1e-4,f=S.f,R=S.R, w0=2*Math.PI*f;
    var fa=f<=1.5?f:0.75, slow=f/fa;
    if(!paused) th=(th+2*Math.PI*fa*dt)%(4*Math.PI);
    var Phi=B*A*Math.cos(th), eps=N*B*A*w0*Math.sin(th), em=N*B*A*w0;
    F3.setOut(root,'N',String(N)); F3.setOut(root,'B',F3.fmt(B,2)+' T'); F3.setOut(root,'A',S.A+' cm²'); F3.setOut(root,'f',F3.fmt(f,1)+' Hz'); F3.setOut(root,'R',S.R+' Ω');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var cx=w/2, cy=h/2+8, p=0.35, sc=Math.min(1,w/640);
    // polos
    ctx.fillStyle='#d94a4a'; ctx.fillRect(cx-250*sc-30,cy-70,40,140); F3.label(ctx,'N',cx-250*sc-10,cy,'#fff',18,'center','600');
    ctx.fillStyle='#4a7bd9'; ctx.fillRect(cx+250*sc-10,cy-70,40,140); F3.label(ctx,'S',cx+250*sc+10,cy,'#fff',18,'center','600');
    ctx.globalAlpha=0.55; for(var yy=-50;yy<=50;yy+=25){ F3.arrow(ctx,cx-250*sc+16,cy+yy,cx+250*sc-16,cy+yy,c.B,1.4,7); } ctx.globalAlpha=1;
    F3.label(ctx,'B',cx-250*sc+22,cy-62,c.B,14,'left','600');
    // espira
    var W=Math.min(110,w*0.17), Hh=72, s1=Math.sin(th), c1=Math.cos(th);
    function P(X,Y,Z){ return [cx+X, cy-Y*Math.cos(p)+Z*Math.sin(p)]; }
    var ux=s1*W, uz=-c1*W; // u' = (sin, 0, -cos): u' x y = n
    var C=[P(ux,-Hh,uz),P(ux,Hh,uz),P(-ux,Hh,-uz),P(-ux,-Hh,-uz)];
    ctx.strokeStyle=c.muted; ctx.setLineDash([4,4]); ctx.lineWidth=1; ctx.beginPath(); var a1=P(0,Hh+30,0),a2=P(0,-Hh-34,0); ctx.moveTo(a1[0],a1[1]); ctx.lineTo(a2[0],a2[1]); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle='rgba(224,138,79,.10)'; ctx.beginPath(); ctx.moveTo(C[0][0],C[0][1]); for(var k=1;k<4;k++) ctx.lineTo(C[k][0],C[k][1]); ctx.closePath(); ctx.fill();
    ctx.strokeStyle='#e08a4f'; ctx.lineWidth=4; ctx.stroke();
    // corrente: lado +u' sobe se ε>0
    if(Math.abs(Math.sin(th))>0.12){ var sg=eps>0?1:-1, mA=P(ux,0,uz), mB=P(-ux,0,-uz);
      F3.arrow(ctx,mA[0],mA[1]+sg*16,mA[0],mA[1]-sg*16,c.S,2.6,9); F3.arrow(ctx,mB[0],mB[1]-sg*16,mB[0],mB[1]+sg*16,c.S,2.6,9); }
    // normal
    var n0=P(0,0,0), n1=P(70*c1,0,70*s1); F3.arrow(ctx,n0[0],n0[1],n1[0],n1[1],c.E,3,10); F3.label(ctx,'n',n1[0]+8,n1[1]-8,c.E,14,'left','600');
    // anéis
    var r0=P(0,-Hh-34,0); ctx.strokeStyle=c.ink; ctx.lineWidth=1.5; ctx.beginPath(); ctx.ellipse(r0[0],r0[1]+6,14,4,0,0,7); ctx.stroke(); ctx.beginPath(); ctx.ellipse(r0[0],r0[1]+16,14,4,0,0,7); ctx.stroke();
    F3.label(ctx,'anéis deslizantes',r0[0]+22,r0[1]+12,c.muted,11);
    if(slow>1.01) F3.label(ctx,'câmera lenta ×'+F3.fmt(slow,0),12,16,c.S,12);
    F3.label(ctx,'φ = ωt = '+F3.fmt((th*180/Math.PI)%360,0)+'°',w-12,16,c.ink,12,'right');
    // gráficos
    var g=gp.ctx, gw=gp.w, gh=gp.h; g.clearRect(0,0,gw,gh);
    var hb=(gh-46)/2, x2=th/(2*Math.PI);
    var Q1=F3.plot(g,{x:44,y:14,w:gw-58,h:hb},[0,2],[-1.15,1.15],c,{yl:'Φ / BA = cos ωt'});
    var Q2=F3.plot(g,{x:44,y:30+hb,w:gw-58,h:hb},[0,2],[-1.15,1.15],c,{yl:'ε / NBAω = sen ωt',xl:'t / T'});
    F3.curve(g,function(u){return Math.cos(2*Math.PI*u);},0,2,Q1,c.B,2);
    F3.curve(g,function(u){return Math.sin(2*Math.PI*u);},0,2,Q2,c.E,2);
    g.fillStyle=c.B; g.beginPath(); g.arc(Q1.X(x2),Q1.Y(Math.cos(th)),5,0,7); g.fill();
    g.fillStyle=c.E; g.beginPath(); g.arc(Q2.X(x2),Q2.Y(Math.sin(th)),5,0,7); g.fill();
    g.strokeStyle=c.muted; g.setLineDash([3,3]); g.beginPath(); g.moveTo(Q1.X(x2),14); g.lineTo(Q1.X(x2),gh-16); g.stroke(); g.setLineDash([]);
    var Pm=em*em/(2*R);
    out.innerHTML='<span>ω = <b>'+F3.fmt(w0,1)+' rad/s</b></span><span>Φ máx por espira = BA = <b>'+F3.sci(B*A,2)+' Wb</b></span><span>ε máx = NBAω = <b class="hl">'+F3.fmt(em,em<10?2:0)+' V</b></span><span>ε eficaz = <b>'+F3.fmt(em/Math.SQRT2,em<10?2:0)+' V</b></span><span>ε agora = <b>'+F3.fmt(eps,em<10?2:0)+' V</b></span><span>P média na carga = <b>'+F3.fmt(Pm,Pm<10?3:0)+' W</b></span><span>torque médio da turbina = P/ω = <b>'+F3.fmt(Pm/w0,3)+' N·m</b></span>';
  });
})();

/* ---------------------------------------------------------------
   W4 · barra com bateria (simulado P2, Ex. 2) — B saindo da tela
---------------------------------------------------------------- */
(function(){
  var root=$('w-rail'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), S={}, out=root.querySelector('.w-readout');
  var v=0,t=0,hist=[],noLenz=false,scroll=0,qphase=0;
  function restart(){ v=0; t=0; hist=[]; scroll=0; }
  F3.bind(root,S,function(){ restart(); });
  root.querySelector('[data-act=restart]').onclick=restart;
  root.querySelector('[data-act=sears]').onclick=function(){ F3.setRange(root,'E',12,S); F3.setRange(root,'B',2.4,S); F3.setRange(root,'d',0.36,S); F3.setRange(root,'R',5,S); F3.setRange(root,'m',0.9,S); restart(); };
  var nl=root.querySelector('[data-act=nolenz]'); nl.onclick=function(){ noLenz=!noLenz; nl.classList.toggle('on',noLenz); nl.textContent=noLenz?'Religar Lenz':'Desligar Lenz (física errada)'; restart(); };
  function step(dt,E,B,d,R,m){ var n=20; for(var k=0;k<n;k++){ var Inet=noLenz?E/R:(E-B*d*v)/R; v+=(Inet*d*B/m)*dt/n; t+=dt/n; } hist.push([t,v]); }
  F3.loop(root,function(dtr){
    var E=S.E,B=S.B,d=S.d,R=S.R,m=S.m, tau=m*R/(B*d*B*d), vT=E/(B*d), Tmax=5*tau, rate=Tmax/9;
    if(F3.reduce){ if(!hist.length){ while(t<Tmax) step(Tmax/200,E,B,d,R,m); } }
    else if(t<Tmax) step(dtr*rate,E,B,d,R,m);
    var I=noLenz?E/R:(E-B*d*v)/R, F=I*d*B;
    F3.setOut(root,'E',E+' V'); F3.setOut(root,'B',F3.fmt(B,1)+' T'); F3.setOut(root,'d',F3.fmt(d,2)+' m'); F3.setOut(root,'R',F3.fmt(R,1)+' Ω'); F3.setOut(root,'m',F3.fmt(m,1)+' kg');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var top=48, bot=h-48, left=60, barX=w*0.62, mid=(top+bot)/2;
    scroll+=dtr*Math.min(v/vT,1.6)*140;
    ctx.globalAlpha=0.5; var sp=34; for(var y=top-24;y<=bot+24;y+=sp/1.2){ for(var x=-sp+((-scroll)%sp+sp)%sp; x<w; x+=sp){ ctx.fillStyle=c.B; ctx.beginPath(); ctx.arc(x,y,2.4,0,7); ctx.fill(); } } ctx.globalAlpha=1;
    var batX=left-scroll;
    ctx.strokeStyle=c.muted; ctx.lineWidth=6; ctx.lineCap='butt';
    ctx.beginPath(); ctx.moveTo(Math.max(batX,0),top); ctx.lineTo(w,top); ctx.moveTo(Math.max(batX,0),bot); ctx.lineTo(w,bot); ctx.stroke();
    if(batX>-30){ ctx.strokeStyle=c.ink; ctx.lineWidth=2.5; ctx.beginPath(); ctx.moveTo(batX,top); ctx.lineTo(batX,mid-12); ctx.moveTo(batX,mid+12); ctx.lineTo(batX,bot); ctx.stroke();
      ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(batX-16,mid-8); ctx.lineTo(batX+16,mid-8); ctx.stroke(); ctx.lineWidth=6; ctx.beginPath(); ctx.moveTo(batX-8,mid+8); ctx.lineTo(batX+8,mid+8); ctx.stroke();
      F3.label(ctx,'ε',batX+22,mid,c.ink,16); }
    ctx.fillStyle=c.E; ctx.fillRect(barX-6,top-14,12,bot-top+28);
    F3.label(ctx,'d',barX-22,mid,c.muted,14,'center');
    qphase+=dtr*Math.max(0,I)*14;
    ctx.fillStyle=c.S;
    var nq=8,q,f; for(q=0;q<nq;q++){ f=((q/nq)+qphase*0.05)%1; ctx.beginPath(); ctx.arc(barX,bot-f*(bot-top),3,0,7); ctx.fill(); }
    var railLen=barX-Math.max(batX,0); for(q=0;q<10;q++){ f=((q/10)+qphase*0.05)%1; ctx.beginPath(); ctx.arc(barX-f*railLen,top,3,0,7); ctx.fill(); ctx.beginPath(); ctx.arc(Math.max(batX,0)+f*railLen,bot,3,0,7); ctx.fill(); }
    var Fmax=E*d*B/R, fl=noLenz?70:70*F/Fmax;
    if(fl>3) F3.arrow(ctx,barX+10,mid,barX+10+fl,mid,c.E,4,12);
    F3.label(ctx,'F = I d B î',barX+16,mid-22,c.E,13);
    F3.label(ctx,'I sobe na barra (anti-horário)',barX+16,bot-12,c.S,12);
    F3.label(ctx,'B saindo da tela (⊙)',w-10,16,c.B,12,'right');
    var g=gp.ctx, gw=gp.w, gh=gp.h; g.clearRect(0,0,gw,gh);
    var x0=52,y0=gh-28,pw=gw-x0-14,ph=gh-44, vmax=vT*1.25;
    g.strokeStyle=c.grid; g.lineWidth=1; g.strokeRect(x0,y0-ph,pw,ph);
    g.setLineDash([5,5]); g.strokeStyle=c.ok; g.beginPath(); var yT=y0-vT/vmax*ph; g.moveTo(x0,yT); g.lineTo(x0+pw,yT); g.stroke(); g.setLineDash([]);
    F3.label(g,'v_T = ε/(Bd) = '+F3.fmt(vT,1)+' m/s',x0+pw-4,yT-9,c.ok,11,'right');
    g.strokeStyle=c.muted; g.setLineDash([2,4]); g.lineWidth=1.5; g.beginPath(); for(var i=0;i<=100;i++){ var tt=i/100*Tmax, vv=vT*(1-Math.exp(-tt/tau)); var X=x0+tt/Tmax*pw, Y=y0-vv/vmax*ph; i?g.lineTo(X,Y):g.moveTo(X,Y);} g.stroke(); g.setLineDash([]);
    g.strokeStyle=c.E; g.lineWidth=2.6; g.beginPath(); hist.forEach(function(p,k){ var X=x0+p[0]/Tmax*pw, Y=Math.max(y0-ph,y0-p[1]/vmax*ph); k?g.lineTo(X,Y):g.moveTo(X,Y); }); g.stroke();
    F3.label(g,'v(t)',x0+6,y0-ph+10,c.E,12); F3.label(g,'t →',x0+pw,y0+14,c.muted,11,'right'); F3.label(g,'0',x0,y0+14,c.muted,11,'center');
    var X5=x0+tau/Tmax*pw; g.strokeStyle=c.muted; g.beginPath(); g.moveTo(X5,y0); g.lineTo(X5,y0+5); g.stroke(); F3.label(g,'τ',X5,y0+14,c.muted,11,'center');
    F3.label(g,(noLenz?'sem Lenz: v cresce sem parar':'tracejado: fórmula do gabarito'),x0+60,y0-ph+10,c.muted,11);
    out.innerHTML='<span>t = <b>'+F3.fmt(t,2)+' s</b></span><span>v = <b class="hl">'+F3.fmt(v,2)+' m/s</b></span><span>fem induzida = −Bdv = <b>'+F3.fmt(noLenz?0:-B*d*v,2)+' V</b></span><span>I = <b>'+F3.fmt(I,2)+' A</b></span><span>F = <b>'+F3.fmt(F,2)+' N</b></span><span>τ = mR/(Bd)² = <b>'+F3.fmt(tau,2)+' s</b></span>';
  });
})();

/* ---------------------------------------------------------------
   W5 · ímã caindo em tubo de cobre vs PVC
---------------------------------------------------------------- */
(function(){
  var root=$('w-tube'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  var t=0,yP=0,yC=0,vC=0,run=false,tP=null,tC=null,Ltube=1.5,g=9.8;
  F3.bind(root,S);
  function arrivalCopper(k){ var y=0,v=0,tt=0,dt=1e-3; while(y<Ltube&&tt<60){ v+=(g-k*v)*dt; y+=v*dt; tt+=dt; } return tt; }
  root.querySelector('[data-act=drop]').onclick=function(){ t=0;yP=0;yC=0;vC=0;tP=null;tC=null;run=true;
    if(F3.reduce){ tP=Math.sqrt(2*Ltube/g); tC=arrivalCopper(S.k); yP=yC=Ltube; run=false; } };
  F3.loop(root,function(dt){
    F3.setOut(root,'k',S.k+' s⁻¹');
    if(run){ var sdt=dt*0.6; t+=sdt; if(tP===null){ yP=0.5*g*t*t; if(yP>=Ltube){ yP=Ltube; tP=t; } } if(tC===null){ for(var k=0;k<10;k++){ vC+=(g-S.k*vC)*sdt/10; yC+=vC*sdt/10; } if(yC>=Ltube){ yC=Ltube; tC=t; } } if(tP!==null&&tC!==null) run=false; }
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var top=30, bot=h-30, tw=46;
    [[w*0.3,'PVC (isolante)','#9a8fb3',yP,false],[w*0.7,'Cobre','#e08a4f',yC,true]].forEach(function(T){
      var x=T[0]; ctx.fillStyle=T[4]?'rgba(224,138,79,.18)':'rgba(154,143,179,.14)'; ctx.fillRect(x-tw/2,top,tw,bot-top);
      ctx.strokeStyle=T[2]; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(x-tw/2,top); ctx.lineTo(x-tw/2,bot); ctx.moveTo(x+tw/2,top); ctx.lineTo(x+tw/2,bot); ctx.stroke();
      F3.label(ctx,T[1],x,top-14,c.ink,13,'center');
      var my=top+(T[3]/Ltube)*(bot-top-30);
      if(T[4]&&run){ for(var r=-1;r<=1;r+=2){ var yy=my+15+r*22; ctx.strokeStyle='rgba(255,224,102,.8)'; ctx.lineWidth=2; ctx.beginPath(); ctx.ellipse(x,yy,tw/2+6,6,0,0,7); ctx.stroke(); } }
      ctx.fillStyle='#d94a4a'; ctx.fillRect(x-13,my,26,15); ctx.fillStyle='#4a7bd9'; ctx.fillRect(x-13,my+15,26,15);
      F3.label(ctx,'N',x,my+8,'#fff',10,'center'); F3.label(ctx,'S',x,my+23,'#fff',10,'center');
    });
    var vT=g/S.k;
    out.innerHTML='<span>PVC: queda livre, chega em <b>'+(tP!==null?F3.fmt(tP,2)+' s':'…')+'</b></span><span>Cobre: velocidade terminal g/k = <b class="hl">'+F3.fmt(vT,2)+' m/s</b>, chega em <b>'+(tC!==null?F3.fmt(tC,2)+' s':'…')+'</b></span><span>(tubo de 1,5 m)</span>';
  });
})();
})();
