/* Capítulo VII · Indutância e energia magnética — widgets: w-freio, w-sol, w-rl, w-coax */
(function(){
"use strict";
var F3 = window.F3;
if(!F3) return;
function $(id){ return document.getElementById(id); }
function clamp(x,a,b){ return Math.max(a,Math.min(b,x)); }

/* ---------------------------------------------------------------
   W1 · freio por correntes de Foucault (três pêndulos)
   θ'' = −(g/Lp) sen θ − k·c·f(θ)·θ',  f(θ) = exp(−(θ/0,18)²) (placa dentro do vão)
---------------------------------------------------------------- */
(function(){
  var root=$('w-freio'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), S={}, out=root.querySelector('.w-readout');
  var g=9.8, Lp=0.5, w02=g/Lp, types=[{n:'Cobre maciço',c:1},{n:'Cobre com fendas',c:0.08},{n:'Plástico',c:0}];
  var P=[], t=0, hist=[];
  function reset(){ var a=S.a0*Math.PI/180; P=types.map(function(){ return {th:a,om:0}; }); t=0; hist=[]; }
  F3.bind(root,S,function(k){ if(k==='a0') reset(); });
  reset();
  root.querySelector('[data-act=go]').onclick=reset;
  function f(th){ return Math.exp(-Math.pow(th/0.18,2)); }
  F3.loop(root,function(dt){
    var n=20, h=dt/n;
    for(var k=0;k<n;k++){ P.forEach(function(p,j){ var al=-w02*Math.sin(p.th)-S.k*types[j].c*f(p.th)*p.om; p.om+=al*h; p.th+=p.om*h; }); }
    t+=dt; if(dt>0){ hist.push([t,P[0].th,P[1].th,P[2].th]); while(hist.length&&hist[0][0]<t-10) hist.shift(); }
    F3.setOut(root,'k',S.k+' s⁻¹'); F3.setOut(root,'a0',S.a0+'°');
    var c=F3.W(), ctx=st.ctx, w=st.w, H=st.h; ctx.clearRect(0,0,w,H);
    var Lpx=Math.min(185,H-90), py0=22, cols=[c.E,c.S,c.B];
    P.forEach(function(p,j){
      var px0=w*(1+2*j)/6;
      // ímã (vão)
      ctx.fillStyle='rgba(217,74,74,.28)'; ctx.fillRect(px0-30,py0+Lpx-34,30,68); ctx.fillStyle='rgba(74,123,217,.28)'; ctx.fillRect(px0,py0+Lpx-34,30,68);
      F3.label(ctx,'ímã',px0,py0+Lpx+44,c.muted,11,'center');
      var x=px0+Lpx*Math.sin(p.th), y=py0+Lpx*Math.cos(p.th);
      ctx.strokeStyle=c.muted; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(px0,py0); ctx.lineTo(x,y); ctx.stroke();
      ctx.fillStyle=c.ink; ctx.beginPath(); ctx.arc(px0,py0,4,0,7); ctx.fill();
      ctx.save(); ctx.translate(x,y); ctx.rotate(-p.th);
      var pw=50, ph=40;
      ctx.fillStyle=j===2?'rgba(200,200,215,.55)':'rgba(224,138,79,.85)'; ctx.fillRect(-pw/2,-ph/2+6,pw,ph);
      if(j===1){ ctx.fillStyle=c.bg; for(var s=-2;s<=2;s++){ if(s===0) continue; ctx.fillRect(s*10-1.5,-ph/2+6,3,ph-8); } }
      var I=types[j].c*f(p.th)*Math.abs(p.om)*S.k;
      if(I>0.05){ ctx.strokeStyle='rgba(255,224,102,'+Math.min(0.95,0.25+I/6)+')'; ctx.lineWidth=2;
        if(j===0){ ctx.beginPath(); ctx.arc(0,6,14,0,7); ctx.stroke(); ctx.beginPath(); ctx.arc(0,6,7,0,7); ctx.stroke(); }
        else { for(var q=-2;q<=1;q++){ ctx.beginPath(); ctx.ellipse(q*10+5,6,3,14,0,0,7); ctx.stroke(); } } }
      ctx.restore();
      F3.label(ctx,types[j].n,px0,H-10,cols[j],12,'center','600');
    });
    // gráfico θ(t)
    var gc=gp.ctx, gw=gp.w, gh=gp.h; gc.clearRect(0,0,gw,gh);
    var A=S.a0*Math.PI/180*1.1, Q=F3.plot(gc,{x:40,y:14,w:gw-54,h:gh-40},[t-10,t],[-A,A],c,{yl:'θ(t)',xl:'últimos 10 s'});
    [1,2,3].forEach(function(j){ gc.strokeStyle=cols[j-1]; gc.lineWidth=2; gc.beginPath(); hist.forEach(function(p,k){ var X=Q.X(p[0]),Y=Q.Y(p[j]); k?gc.lineTo(X,Y):gc.moveTo(X,Y); }); gc.stroke(); });
    var E0=1-Math.cos(S.a0*Math.PI/180);
    out.innerHTML=P.map(function(p,j){ var E=(1-Math.cos(p.th))+p.om*p.om/(2*w02); return '<span>'+types[j].n+': energia restante <b'+(j===0?' class="hl"':'')+'>'+F3.fmt(100*E/E0,0)+'%</b></span>'; }).join('')+'<span>t = <b>'+F3.fmt(t,1)+' s</b></span>';
  });
})();

/* ---------------------------------------------------------------
   W2 · solenoide: ½LI² contra u·volume
---------------------------------------------------------------- */
(function(){
  var root=$('w-sol'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  F3.bind(root,S);
  F3.loop(root,function(){
    var N=S.N, l=S.l/100, r=S.r/100, I=S.I, n=N/l, Sx=Math.PI*r*r, B=F3.MU0*n*I, L=F3.MU0*n*n*Sx*l, U=0.5*L*I*I, u=B*B/(2*F3.MU0), V=Sx*l;
    F3.setOut(root,'N',String(N)); F3.setOut(root,'l',S.l+' cm'); F3.setOut(root,'r',F3.fmt(S.r,1)+' cm'); F3.setOut(root,'I',F3.fmt(I,1)+' A');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var k=Math.min((w-70)/60,150/12), Lx=S.l*k, Dy=2*S.r*k, cx=w/2, cy=h/2-6, x0=cx-Lx/2, y0=cy-Dy/2;
    // linhas de borda (campo de fuga)
    ctx.strokeStyle=c.B; ctx.globalAlpha=0.35; ctx.lineWidth=1.4;
    [1,-1].forEach(function(sg){ ctx.beginPath(); ctx.moveTo(x0+Lx,cy-sg*Dy*0.25); ctx.bezierCurveTo(x0+Lx+60,cy-sg*(Dy/2+50),x0-60,cy-sg*(Dy/2+50),x0,cy-sg*Dy*0.25); ctx.stroke(); });
    ctx.globalAlpha=1;
    // densidade de energia
    var al=0.08+0.8*clamp(Math.log(1+u)/Math.LN10/6,0,1);
    ctx.fillStyle='rgba(95,212,255,'+al.toFixed(3)+')'; ctx.fillRect(x0,y0,Lx,Dy);
    // espiras
    var nd=Math.min(N,Math.max(4,Math.floor(Lx/9))), rr=Math.min(4,Lx/nd/2.4);
    for(var q=0;q<nd;q++){ var xq=x0+Lx*(q+0.5)/nd; F3.dotOut(ctx,xq,y0,rr,c.E); F3.crossIn(ctx,xq,y0+Dy,rr,c.E); }
    if(I>0&&Dy>14){ F3.arrow(ctx,x0+Lx*0.2,cy,x0+Lx*0.8,cy,c.B,2.4,9); }
    F3.label(ctx,'B = μ0 n I = '+F3.sci(B,2)+' T',cx,y0+Dy+26,c.B,12,'center');
    F3.label(ctx,'l = '+S.l+' cm',cx,y0-22,c.muted,11,'center');
    F3.label(ctx,'u = B²/2μ0 = '+F3.sci(u,2)+' J/m³',10,h-12,c.ink,12);
    var ratio=l/r, wheel=l/(l+0.9*r);
    out.innerHTML='<span>n = <b>'+F3.fmt(n,0)+' m⁻¹</b></span><span>L = μ0n²Sl = <b>'+F3.sci(L,3)+' H</b></span><span>½LI² = <b class="hl">'+F3.sci(U,3)+' J</b></span><span>u·(Sl) = <b class="hl">'+F3.sci(u*V,3)+' J</b></span><span>volume = <b>'+F3.sci(V,2)+' m³</b></span>'+
      (ratio<10?'<span>Atenção: l/raio = '+F3.fmt(ratio,1)+': solenoide curto; com bordas, L real ≈ <b>'+F3.fmt(100*wheel,0)+'%</b> disso (fórmula de Wheeler)</span>':'<span>l/raio = '+F3.fmt(ratio,0)+': aproximação de solenoide longo boa</span>');
  });
})();

/* ---------------------------------------------------------------
   W3 · circuito R-L com chave
---------------------------------------------------------------- */
(function(){
  var root=$('w-rl'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), S={}, out=root.querySelector('.w-readout');
  var on=false, i0=0, s=6, hist=[], qph=0, iCur=0;
  function iNow(){ var f=on?S.E/S.R:0; return f+(i0-f)*Math.exp(-s); }
  function sw(state){ i0=iNow(); on=state; s=0; hist=[]; if(F3.reduce) s=6; }
  F3.bind(root,S,function(){ i0=iCur; s=F3.reduce?6:0; hist=[]; });
  root.querySelector('[data-act=on]').onclick=function(){ sw(true); };
  root.querySelector('[data-act=off]').onclick=function(){ sw(false); };
  F3.loop(root,function(dt){
    var E=S.E,R=S.R,L=S.L,tau=L/R, f=on?E/R:0;
    if(s<6) s=Math.min(6,s+1.25*dt);
    var i=iNow(), vL=(f-i)*R, U=0.5*L*i*i, imax=E/R, Umax=0.5*L*imax*imax; iCur=i;
    if(F3.reduce){ if(hist.length<2){ hist=[]; for(var z0=0;z0<=60;z0++){ var sz=z0/10, iz=f+(i0-f)*Math.exp(-sz); hist.push([sz,iz/imax,(f-iz)*R/E,0.5*L*iz*iz/Umax]); } } }
    else if(dt>0||!hist.length) hist.push([s,i/imax,vL/E,U/Umax]);
    F3.setOut(root,'E',E+' V'); F3.setOut(root,'R',R+' Ω'); F3.setOut(root,'L',F3.fmt(L,2)+' H');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var xl=50, xr=w-60, yt=40, yb=h-30, xs=130, mid=(yt+yb)/2;
    ctx.strokeStyle=c.muted; ctx.lineWidth=2.5; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(xl,yb); ctx.lineTo(xr,yb); ctx.lineTo(xr,mid+40); ctx.moveTo(xr,mid-40); ctx.lineTo(xr,yt); ctx.lineTo(xs+28,yt); ctx.stroke();
    // bateria (ramo esquerdo)
    ctx.beginPath(); ctx.moveTo(xl,yb); ctx.lineTo(xl,mid+8); ctx.moveTo(xl,mid-8); ctx.lineTo(xl,yt); ctx.lineTo(xs-50,yt); ctx.stroke();
    ctx.strokeStyle=c.ink; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(xl-14,mid-8); ctx.lineTo(xl+14,mid-8); ctx.stroke(); ctx.lineWidth=6; ctx.beginPath(); ctx.moveTo(xl-7,mid+8); ctx.lineTo(xl+7,mid+8); ctx.stroke();
    F3.label(ctx,'ε',xl-26,mid,c.ink,15,'center');
    // chave S1 (bateria) e ramo de curto
    ctx.strokeStyle=c.muted; ctx.lineWidth=2.5; ctx.beginPath(); ctx.moveTo(xs,yt); ctx.lineTo(xs+28,yt); ctx.moveTo(xs,yt); ctx.lineTo(xs,yb); ctx.stroke();
    ctx.strokeStyle=on?c.ok:c.neg; ctx.lineWidth=3;
    ctx.beginPath(); ctx.moveTo(xs,yt); if(on) ctx.lineTo(xs-50,yt); else ctx.lineTo(xs-44,yt-20); ctx.stroke();
    ctx.fillStyle=c.ink; [xs,xs-50].forEach(function(x){ ctx.beginPath(); ctx.arc(x,yt,3.5,0,7); ctx.fill(); });
    // ramo de curto: interrompido quando ligado
    ctx.fillStyle=c.bg; if(on){ ctx.fillRect(xs-4,mid-14,8,28); ctx.strokeStyle=c.neg; ctx.lineWidth=3; ctx.beginPath(); ctx.moveTo(xs,mid+14); ctx.lineTo(xs+16,mid-12); ctx.stroke(); }
    F3.label(ctx,on?'chave na bateria':'chave no curto',xs-20,yt-26,on?c.ok:c.neg,11,'center');
    // resistor
    var rx0=xr-200, rx1=xr-110; ctx.fillStyle=c.bg; ctx.fillRect(rx0,yt-8,rx1-rx0,16); ctx.strokeStyle=c.ink; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(rx0,yt); for(var z=1;z<=8;z++) ctx.lineTo(rx0+(rx1-rx0)*z/8,yt+(z%2?-7:7)); ctx.lineTo(rx1,yt); ctx.stroke();
    F3.label(ctx,'R',(rx0+rx1)/2,yt-18,c.ink,13,'center','600');
    // indutor
    ctx.strokeStyle=c.E; ctx.lineWidth=2.4; ctx.beginPath(); for(var b=0;b<5;b++){ ctx.arc(xr,mid-40+8+b*16,8,-Math.PI/2,Math.PI/2,false); } ctx.stroke();
    ctx.fillStyle='rgba(95,212,255,'+(0.06+0.5*U/Umax).toFixed(3)+')'; ctx.beginPath(); ctx.ellipse(xr+4,mid,30,52,0,0,7); ctx.fill();
    F3.label(ctx,'L',xr+24,mid,c.E,14,'left','600');
    F3.label(ctx,'v_L = '+F3.fmt(vL,2)+' V',xr-14,mid+60,c.E,11,'right');
    // corrente (horário: sobe na bateria, direita no topo)
    qph+=dt*(i/imax)*0.4;
    if(i/imax>0.01){ ctx.fillStyle=c.S; var path=on?[[xl,yb],[xl,yt],[xr,yt],[xr,yb],[xl,yb]]:[[xs,yb],[xs,yt],[xr,yt],[xr,yb],[xs,yb]];
      var segs=[],tot=0; for(var p=0;p<4;p++){ var d=Math.abs(path[p+1][0]-path[p][0])+Math.abs(path[p+1][1]-path[p][1]); segs.push(d); tot+=d; }
      var nq=Math.round(tot/30); for(var q=0;q<nq;q++){ var sp=((q/nq+qph)%1)*tot, m=0; while(m<3&&sp>segs[m]){ sp-=segs[m]; m++; } var A=path[m],B2=path[m+1],fr=segs[m]?sp/segs[m]:0; ctx.beginPath(); ctx.arc(A[0]+(B2[0]-A[0])*fr,A[1]+(B2[1]-A[1])*fr,3,0,7); ctx.fill(); } }
    // gráfico
    var g=gp.ctx, gw=gp.w, gh=gp.h; g.clearRect(0,0,gw,gh);
    var Q=F3.plot(g,{x:40,y:16,w:gw-54,h:gh-44},[0,6],[-1.1,1.1],c,{xl:'t / τ',yl:'relativo ao máximo'});
    for(var tk=1;tk<=5;tk++){ F3.label(g,String(tk),Q.X(tk),gh-18,c.muted,10,'center'); }
    var cs=[c.S,c.E,c.B];
    [1,2,3].forEach(function(j){ g.strokeStyle=cs[j-1]; g.lineWidth=2.2; g.beginPath(); hist.forEach(function(p,k){ var X=Q.X(p[0]),Y=Q.Y(p[j]); k?g.lineTo(X,Y):g.moveTo(X,Y); }); g.stroke(); });
    F3.label(g,'i / (ε/R)',gw-16,24,c.S,11,'right'); F3.label(g,'v_L / ε',gw-16,38,c.E,11,'right'); F3.label(g,'U / Umáx',gw-16,52,c.B,11,'right');
    if(on){ g.setLineDash([3,4]); g.strokeStyle=c.muted; g.beginPath(); g.moveTo(Q.X(1),Q.Y(-1.1)); g.lineTo(Q.X(1),Q.Y(1.1)); g.stroke(); g.setLineDash([]); F3.label(g,'63%',Q.X(1)+4,Q.Y(0.63),c.muted,10); }
    var di=(f-i)/tau;
    out.innerHTML='<span>τ = L/R = <b>'+(tau<1?F3.fmt(tau*1000,1)+' ms':F3.fmt(tau,2)+' s')+'</b></span><span>i = <b class="hl">'+F3.fmt(i,3)+' A</b></span><span>v_L = L di/dt = <b>'+F3.fmt(vL,2)+' V</b></span><span>U = ½Li² = <b>'+F3.fmt(U,3)+' J</b></span>'+
      '<span>bateria εi = <b>'+F3.fmt(on?E*i:0,2)+' W</b></span><span>Joule i²R = <b>'+F3.fmt(i*i*R,2)+' W</b></span><span>dU/dt = Li di/dt = <b>'+F3.fmt(L*i*di,2)+' W</b></span>';
  });
})();

/* ---------------------------------------------------------------
   W4 · cabo coaxial (Exercício 32)
---------------------------------------------------------------- */
(function(){
  var root=$('w-coax'); if(!root) return;
  var cvs=root.querySelectorAll('canvas'), st=new F3.Stage(cvs[0]), gp=new F3.Stage(cvs[1]), S={}, out=root.querySelector('.w-readout');
  var dir=-1, solid=false;
  F3.bind(root,S);
  var bd=root.querySelector('[data-act=dir]'), bs=root.querySelector('[data-act=solid]');
  bd.onclick=function(){ dir=-dir; };
  bs.onclick=function(){ solid=!solid; bs.classList.toggle('on',solid); };
  F3.loop(root,function(){
    var a=S.a, b=Math.max(S.b,S.a*1.02), i=S.i, am=a/1000, bm=b/1000, lnr=Math.log(b/a);
    F3.setOut(root,'a',F3.fmt(a,2)+' mm'); F3.setOut(root,'b',F3.fmt(S.b,1)+' mm'); F3.setOut(root,'i',F3.fmt(i,1)+' A');
    function Bof(rm){ if(rm>bm) return 0; if(rm<am) return solid?F3.MU0*i*rm/(2*Math.PI*am*am):0; return F3.MU0*i/(2*Math.PI*rm); }
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var half=w<560?w:w/2, Rp=Math.min(h/2-22,half/2-20), cx=half/2, cy=h/2;
    // corte
    ctx.fillStyle='rgba(154,143,179,.12)'; ctx.beginPath(); ctx.arc(cx,cy,Rp,0,7); ctx.fill();
    ctx.strokeStyle=c.ink; ctx.lineWidth=4; ctx.beginPath(); ctx.arc(cx,cy,Rp,0,7); ctx.stroke();
    var ap=Math.max(3,Rp*a/b);
    ctx.fillStyle='rgba(224,138,79,.55)'; ctx.beginPath(); ctx.arc(cx,cy,ap,0,7); ctx.fill();
    if(ap>9){ if(dir<0) F3.crossIn(ctx,cx,cy,Math.min(8,ap*0.6),c.ink); else F3.dotOut(ctx,cx,cy,Math.min(8,ap*0.6),c.ink); }
    for(var m=0;m<8;m++){ var ph=m*Math.PI/4+0.2, xx=cx+Rp*Math.cos(ph), yy=cy-Rp*Math.sin(ph); if(dir<0) F3.dotOut(ctx,xx,yy,4,c.ink); else F3.crossIn(ctx,xx,yy,4,c.ink); }
    // setas de B
    var rings=[], k;
    for(k=0;k<4;k++) rings.push(a+(b-a)*(k+0.5)/4);
    if(solid&&ap>14) rings.push(a*0.6);
    var Bref=Bof(rings[0]/1000);
    rings.forEach(function(rr){ var Bv=Bof(rr/1000), len=Math.min(30,28*Bv/Bref), rpx=Rp*rr/b; if(len<2||rpx<6) return;
      var nA=Math.max(4,Math.min(12,Math.round(rpx/9)));
      for(var q=0;q<nA;q++){ var phi=q*2*Math.PI/nA, px=cx+rpx*Math.cos(phi), py=cy-rpx*Math.sin(phi), tx=-Math.sin(phi)*dir, ty=-Math.cos(phi)*dir;
        F3.arrow(ctx,px-tx*len/2,py-ty*len/2,px+tx*len/2,py+ty*len/2,c.B,1.8,6); } });
    F3.label(ctx,dir<0?'fio: corrente −k (⊗) ⇒ B = −B θ̂':'fio: corrente +k (⊙) ⇒ B = +B θ̂',cx,12,c.B,11,'center');
    F3.label(ctx,'B = 0 fora',cx+Rp*0.72,cy+Rp+12,c.muted,11,'center');
    // gráfico B(ρ)
    if(w>=560){ var Ba=solid?F3.MU0*i/(2*Math.PI*am):F3.MU0*i/(2*Math.PI*am);
      var Q=F3.plot(ctx,{x:half+30,y:24,w:half-44,h:h-56},[0,1.25*b],[0,Ba*1.1*1000],c,{xl:'ρ (mm)',yl:'B (mT)'});
      ctx.strokeStyle=c.B; ctx.lineWidth=2.2; ctx.beginPath(); for(var p=0;p<=300;p++){ var rho=1.25*b*p/300, v=Bof(rho/1000)*1000; var X=Q.X(rho),Y=Q.Y(v); p?ctx.lineTo(X,Y):ctx.moveTo(X,Y); } ctx.stroke();
      ctx.setLineDash([3,4]); ctx.strokeStyle=c.muted; [a,b].forEach(function(x,j){ ctx.beginPath(); ctx.moveTo(Q.X(x),24); ctx.lineTo(Q.X(x),h-32); ctx.stroke(); F3.label(ctx,j?'b':'a',Q.X(x),h-22,c.muted,11,'center'); }); ctx.setLineDash([]);
      F3.label(ctx,'∝ 1/ρ',Q.X((a+b)/2)+8,Q.Y(Bof((a+b)/2000)*1000)-12,c.B,11); }
    // gráfico log
    var g=gp.ctx, gw=gp.w, gh=gp.h; g.clearRect(0,0,gw,gh);
    var P=F3.plot(g,{x:44,y:18,w:gw-60,h:gh-48},[0,4],[0,10],c,{xl:'b/a (escala log)',yl:'2πL/(μ0 l) = ln(b/a)'});
    for(k=0;k<=4;k++){ F3.label(g,String(Math.pow(10,k)),P.X(k),gh-20,c.muted,10,'center'); g.strokeStyle=c.grid; g.beginPath(); g.moveTo(P.X(k),18); g.lineTo(P.X(k),gh-30); g.stroke(); }
    for(k=0;k<=10;k+=2) F3.label(g,String(k),36,P.Y(k),c.muted,10,'right');
    F3.curve(g,function(x){ return x*Math.LN10; },0,4,P,c.E,2.4);
    if(solid) F3.curve(g,function(x){ return x*Math.LN10+0.25; },0,4,P,c.S,1.6,[5,4]);
    var lx=Math.log10(b/a), ly=lnr+(solid?0.25:0);
    if(lx<=4){ g.fillStyle=c.ok; g.beginPath(); g.arc(P.X(lx),P.Y(ly),6,0,7); g.fill(); F3.label(g,'seu cabo',P.X(lx)+10,P.Y(ly)-10,c.ok,11); }
    var Ll=F3.MU0/(2*Math.PI)*(lnr+(solid?0.25:0)), Ul=0.5*Ll*i*i, Phil=F3.MU0*i/(2*Math.PI)*lnr;
    out.innerHTML='<span>b/a = <b>'+F3.fmt(b/a,b/a<10?2:0)+'</b></span><span>B(ρ = a⁺) = <b>'+F3.fmt(F3.MU0*i/(2*Math.PI*am)*1000,2)+' mT</b></span><span>B(ρ = b⁻) = <b>'+F3.fmt(F3.MU0*i/(2*Math.PI*bm)*1000,2)+' mT</b></span>'+
      '<span>Φ/l (entre a e b) = <b>'+F3.sci(Phil,2)+' Wb/m</b></span><span>L/l = <b class="hl">'+F3.fmt(Ll*1e9,0)+' nH/m</b>'+(solid?' (inclui 50 nH/m internos)':'')+'</span><span>U/l = ½(L/l)i² = <b>'+F3.sci(Ul,2)+' J/m</b></span>'+(S.b<=S.a*1.02?'<span>Atenção: b precisa ser maior que a</span>':'');
  });
})();
})();
