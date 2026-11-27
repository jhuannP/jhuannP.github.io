/* Capítulo IV · Lei de Ampère — widgets (usa window.F3 de core.js) */
(function(){
"use strict";
var F3 = window.F3; if(!F3) return;
var MU0 = F3.MU0, PI = Math.PI;
function $(id){ return document.getElementById(id); }
function bindN(root,S,cb){ F3.bind(root,S,cb); for(var k in S) if(typeof S[k]==="string"&&S[k]!==""&&!isNaN(+S[k])) S[k]=+S[k]; } /* core.js guarda "0" como texto */
function clamp(x,a,b){ return x<a?a:(x>b?b:x); }
function drag(cv,down,move){
  cv.style.touchAction='none'; var on=false;
  function pos(e){ var r=cv.getBoundingClientRect(); return {x:e.clientX-r.left,y:e.clientY-r.top}; }
  cv.addEventListener('pointerdown',function(e){ var p=pos(e); if(down(p)===false) return; on=true; try{cv.setPointerCapture(e.pointerId);}catch(_){} e.preventDefault(); });
  cv.addEventListener('pointermove',function(e){ if(on) move(pos(e)); });
  function stop(){ on=false; }
  cv.addEventListener('pointerup',stop); cv.addEventListener('pointercancel',stop);
}
function group(root,acts,cb){
  acts.forEach(function(a){ var b=root.querySelector('[data-act="'+a+'"]'); if(!b) return;
    b.addEventListener('click',function(){ acts.forEach(function(o){ var x=root.querySelector('[data-act="'+o+'"]'); if(x) x.classList.toggle('on',o===a); }); cb(a); }); });
}
/* campo (T) de fios retilíneos perpendiculares à tela. Posições em cm, eixo y para cima.
   I > 0 = corrente saindo da tela (+z): B = μ0 I/(2π r) φ̂ (anti-horário). */
function Bwires(ws,x,y){
  var bx=0,by=0;
  for(var i=0;i<ws.length;i++){ var w=ws[i]; if(!w.I) continue; var rx=(x-w.x)/100, ry=(y-w.y)/100, r2=rx*rx+ry*ry; if(r2<1e-10) r2=1e-10; var k=MU0*w.I/(2*PI*r2); bx-=ry*k; by+=rx*k; }
  return [bx,by];
}
function inPoly(pts,x,y){ var c=false; for(var i=0,j=pts.length-1;i<pts.length;j=i++){ var a=pts[i],b=pts[j]; if(((a[1]>y)!==(b[1]>y)) && (x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])) c=!c; } return c; }
function symbol(ctx,x,y,I,r,c){ ctx.fillStyle=c.bg; ctx.beginPath(); ctx.arc(x,y,r+1.5,0,7); ctx.fill(); if(I>0) F3.dotOut(ctx,x,y,r,c.E); else if(I<0) F3.crossIn(ctx,x,y,r,c.E); else { ctx.strokeStyle=c.muted; ctx.lineWidth=1.4; ctx.beginPath(); ctx.arc(x,y,r,0,7); ctx.stroke(); } }
/* malha de setinhas do campo; ref = campo "típico" para a opacidade */
function fieldArrows(ctx,c,x0,y0,x1,y1,step,toW,ws,ref,skip){
  for(var gx=x0+step/2; gx<x1; gx+=step) for(var gy=y0+step/2; gy<y1; gy+=step){
    var p=toW(gx,gy); if(skip&&skip(p[0],p[1])) continue; var b=Bwires(ws,p[0],p[1]), B=Math.hypot(b[0],b[1]); if(B<ref*0.01) continue;
    var ux=b[0]/B, uy=-b[1]/B, L=step*0.34; ctx.globalAlpha=clamp(0.12+0.88*Math.sqrt(B/ref),0.12,1);
    F3.arrow(ctx,gx-ux*L,gy-uy*L,gx+ux*L,gy+uy*L,c.B,1.3,5); }
  ctx.globalAlpha=1;
}

/* ================= 1. Laço amperiano ================= */
(function(){
  var root=$('w-ampere'); if(!root) return;
  var cv=root.querySelector('canvas'), st=new F3.Stage(cv), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var shape='circ', loopC={x:0,y:0}, wires=[{x:-1.2,y:0.8,k:'I1'},{x:1.6,y:-1.3,k:'I2'},{x:5.6,y:2.4,k:'I3'}];
  group(root,['circ','quad','bat'],function(a){ shape=a; });
  var sc=20, ox=0, oy=0, dragW=-1, off={x:0,y:0};
  function toW(px,py){ return [(px-ox)/sc,(oy-py)/sc]; }
  function toP(x,y){ return [ox+x*sc,oy-y*sc]; }
  drag(cv,function(p){ dragW=-1; for(var i=0;i<3;i++){ var q=toP(wires[i].x,wires[i].y); if(Math.hypot(p.x-q[0],p.y-q[1])<18){ dragW=i; break; } }
      var m=toW(p.x,p.y); if(dragW<0){ off.x=loopC.x-m[0]; off.y=loopC.y-m[1]; } },
    function(p){ var m=toW(p.x,p.y), lim=Math.max(4,(st.w/2-10)/sc);
      if(dragW>=0){ wires[dragW].x=clamp(m[0],-lim,lim); wires[dragW].y=clamp(m[1],-7.6,7.6); }
      else { loopC.x=clamp(m[0]+off.x,-lim,lim); loopC.y=clamp(m[1]+off.y,-7,7); } });
  function loopPts(n){
    var R=S.R, pts=[], i, t;
    for(i=0;i<n;i++){ t=i/n;
      if(shape==='circ'){ var a=2*PI*t; pts.push([loopC.x+R*Math.cos(a),loopC.y+R*Math.sin(a)]); }
      else if(shape==='bat'){ var b=2*PI*t, rr=R*(1+0.22*Math.sin(3*b)+0.12*Math.cos(2*b)); pts.push([loopC.x+rr*Math.cos(b),loopC.y+rr*Math.sin(b)]); }
      else { var s=R*0.9, u=t*4, k=Math.floor(u), f=u-k, C=[[s,-s],[s,s],[-s,s],[-s,-s],[s,-s]];
        pts.push([loopC.x+C[k][0]+(C[k+1][0]-C[k][0])*f, loopC.y+C[k][1]+(C[k+1][1]-C[k][1])*f]); } }
    return pts;
  }
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    sc=h/16; ox=w/2; oy=h/2;
    var ws=wires.map(function(o){ return {x:o.x,y:o.y,I:S[o.k]}; });
    ['I1','I2','I3'].forEach(function(k){ F3.setOut(root,k,(S[k]>0?'+':'')+F3.fmt(S[k],1)+' A'); });
    F3.setOut(root,'R',F3.fmt(S.R,1)+' cm');
    var ref=MU0*3/(2*PI*0.03);
    fieldArrows(ctx,c,0,0,w,h,30,toW,ws,ref,null);
    /* laço: circulação numérica */
    var n=720, pts=loopPts(n), circ=0, Bpar=new Array(n), mx=1e-12, dmin=1e9;
    for(var i=0;i<n;i++){ var a=pts[i], b=pts[(i+1)%n], mxp=(a[0]+b[0])/2, myp=(a[1]+b[1])/2, dx=(b[0]-a[0])/100, dy=(b[1]-a[1])/100;
      var B=Bwires(ws,mxp,myp), dl=Math.hypot(dx,dy); var v=B[0]*dx+B[1]*dy; circ+=v; Bpar[i]=v/dl; mx=Math.max(mx,Math.abs(Bpar[i]));
      for(var q=0;q<3;q++) dmin=Math.min(dmin,Math.hypot(mxp-ws[q].x,myp-ws[q].y)); }
    ctx.lineCap='round';
    for(i=0;i<n;i+=3){ var p0=toP(pts[i][0],pts[i][1]), p1=toP(pts[(i+3)%n][0],pts[(i+3)%n][1]), f=Math.abs(Bpar[i])/mx;
      ctx.strokeStyle=Bpar[i]>=0?c.ok:c.neg; ctx.lineWidth=2+4*f; ctx.beginPath(); ctx.moveTo(p0[0],p0[1]); ctx.lineTo(p1[0],p1[1]); ctx.stroke(); }
    /* sentido de percurso e B em alguns pontos */
    for(i=0;i<n;i+=60){ var pa=toP(pts[i][0],pts[i][1]), pb=toP(pts[(i+6)%n][0],pts[(i+6)%n][1]); F3.arrow(ctx,pa[0],pa[1],pb[0],pb[1],c.ink,1.5,8);
      var Bq=Bwires(ws,pts[i][0],pts[i][1]), Bm=Math.hypot(Bq[0],Bq[1]), Lq=clamp(10+14*Math.log10(1+Bm/ref*10),6,34);
      if(Bm>0) F3.arrow(ctx,pa[0],pa[1],pa[0]+Bq[0]/Bm*Lq,pa[1]-Bq[1]/Bm*Lq,c.S,1.8,7); }
    /* fios */
    var Ienc=0, list=[];
    for(i=0;i<3;i++){ var pw=toP(ws[i].x,ws[i].y), ins=inPoly(pts,ws[i].x,ws[i].y); symbol(ctx,pw[0],pw[1],ws[i].I,11,c);
      F3.label(ctx,String(i+1),pw[0]+14,pw[1]-12,c.ink,12,'left','600');
      if(ins){ Ienc+=ws[i].I; } list.push('fio '+(i+1)+': '+(ins?'<b>dentro</b>':'fora')); }
    var ratio=circ/MU0;
    out.innerHTML='<span>∮B·dl = <b>'+F3.sci(circ,3)+' T·m</b></span><span>μ0 I<sub>enc</sub> = <b>'+F3.sci(MU0*Ienc,3)+' T·m</b></span><span>∮B·dl / μ0 = <b class="hl">'+F3.fmt(ratio,3)+' A</b></span><span>I<sub>enc</sub> = <b class="hl">'+F3.fmt(Ienc,2)+' A</b></span><span>'+list.join(' · ')+'</span>'+(dmin<0.2?'<span>⚠ fio quase em cima da curva: a soma numérica perde precisão</span>':'');
  });
})();

/* ================= 2. Fio grosso ================= */
(function(){
  var root=$('w-fiogrosso'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  function Bof(r,i,a){ r/=1000; a/=1000; return r<a? MU0*i*r/(2*PI*a*a) : MU0*i/(2*PI*r); }
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var i=S.i, a=S.a, r=S.r;
    F3.setOut(root,'i',F3.fmt(i,0)+' A'); F3.setOut(root,'a',F3.fmt(a,1)+' mm'); F3.setOut(root,'r',F3.fmt(r,2)+' mm');
    var Ls=Math.min(h-24,w*0.42), cx=12+Ls/2, cy=h/2, range=Math.max(3*a,r*1.15,4), sc=(Ls/2-6)/range;
    /* fio */
    ctx.fillStyle=c.E; ctx.globalAlpha=0.18; ctx.beginPath(); ctx.arc(cx,cy,a*sc,0,7); ctx.fill();
    ctx.globalAlpha=0.5; ctx.beginPath(); ctx.arc(cx,cy,Math.min(r,a)*sc,0,7); ctx.fill(); ctx.globalAlpha=1;
    ctx.strokeStyle=c.E; ctx.lineWidth=1.5; ctx.beginPath(); ctx.arc(cx,cy,a*sc,0,7); ctx.stroke();
    var stp=Math.max(9,a*sc/4);
    for(var x=-a*sc; x<=a*sc; x+=stp) for(var y=-a*sc; y<=a*sc; y+=stp){ if(x*x+y*y>(a*sc-3)*(a*sc-3)) continue; ctx.fillStyle=c.E; ctx.beginPath(); ctx.arc(cx+x,cy+y,1.6,0,7); ctx.fill(); }
    /* laço amperiano */
    ctx.strokeStyle=c.ok; ctx.lineWidth=2; ctx.setLineDash([6,4]); ctx.beginPath(); ctx.arc(cx,cy,Math.max(1,r*sc),0,7); ctx.stroke(); ctx.setLineDash([]);
    var B=Bof(r,i,a), Bmax=MU0*i/(2*PI*a/1000);
    for(var k=0;k<8;k++){ var an=k*PI/4, px=cx+r*sc*Math.cos(an), py=cy-r*sc*Math.sin(an), L=34*B/Bmax; if(L>3) F3.arrow(ctx,px,py,px-L*Math.sin(an),py-L*Math.cos(an),c.B,2.2,7); }
    F3.label(ctx,'escala: '+F3.fmt(range,0)+' mm',cx,h-10,c.muted,11,'center');
    F3.label(ctx,'ρ',cx+r*sc*0.7+6,cy+r*sc*0.7+6,c.ok,13,'left','600');
    /* gráfico */
    var bx=cx+Ls/2+40, box={x:bx,y:24,w:w-bx-16,h:h-60};
    if(box.w>80){
      var P=F3.plot(ctx,box,[0,30],[0,Bmax*1.2],c,{xl:'ρ (mm)',yl:'B (mT)'});
      F3.curve(ctx,function(q){return Bof(q,i,a);},0,30,P,c.B,2.4);
      ctx.strokeStyle=c.E; ctx.setLineDash([4,4]); ctx.beginPath(); ctx.moveTo(P.X(a),box.y); ctx.lineTo(P.X(a),box.y+box.h); ctx.stroke(); ctx.setLineDash([]);
      F3.label(ctx,'a',P.X(a)+4,box.y+10,c.E,12,'left','600');
      F3.label(ctx,F3.fmt(Bmax*1e3,2),box.x-4,P.Y(Bmax),c.muted,10,'right');
      for(var t=0;t<=30;t+=10) F3.label(ctx,String(t),P.X(t),box.y+box.h+12,c.muted,10,'center');
      ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(r),P.Y(B),5.5,0,7); ctx.fill();
      F3.label(ctx,r<a?'dentro: B ∝ ρ':'fora: B ∝ 1/ρ',box.x+box.w-6,box.y+14,c.ink,12,'right');
    }
    var ienc=r<a?i*r*r/(a*a):i;
    out.innerHTML='<span>i<sub>enc</sub> = <b>'+F3.fmt(ienc,2)+' A</b>'+(r<a?' (= i·ρ²/a²)':' (tudo)')+'</span><span>B(ρ) = <b class="hl">'+F3.fmt(B*1e3,3)+' mT</b></span><span>máximo na superfície: <b>'+F3.fmt(Bmax*1e3,3)+' mT</b></span>';
  });
})();

/* ================= 3. Solenoide em corte + retângulo ================= */
(function(){
  var root=$('w-solamp'); if(!root) return;
  var cv=root.querySelector('canvas'), st=new F3.Stage(cv), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var Rs=2, p=0.5, Iw=2, wires=[], k;
  for(k=-120;k<120;k++){ var x=(k+0.5)*p; wires.push({x:x,y:Rs,I:Iw}); wires.push({x:x,y:-Rs,I:-Iw}); }
  var B0=MU0*Iw/(p/100); /* μ0 n I */
  var rect={x:0.1,y:Rs}, sc=34, ox=0, oy=0, off={x:0,y:0}, cacheKey='', arrows=[];
  function toW(px,py){ return [(px-ox)/sc,(oy-py)/sc]; }
  function toP(x,y){ return [ox+x*sc,oy-y*sc]; }
  drag(cv,function(q){ var m=toW(q.x,q.y); off.x=rect.x-m[0]; off.y=rect.y-m[1]; },function(q){ var m=toW(q.x,q.y), lim=(st.w/2)/sc; rect.x=clamp(m[0]+off.x,-lim,lim); rect.y=clamp(m[1]+off.y,-4.8,4.8); });
  root.querySelector('[data-act=cruza]').addEventListener('click',function(){ rect.x=0.1; rect.y=Rs; F3.setRange(root,'H',3,S); });
  root.querySelector('[data-act=dentro]').addEventListener('click',function(){ rect.x=0.1; rect.y=0; F3.setRange(root,'H',2.5,S); });
  root.querySelector('[data-act=fora]').addEventListener('click',function(){ rect.x=0.1; rect.y=3.6; F3.setRange(root,'H',1.5,S); });
  /* circulação exata de cada fio num segmento reto: (μ0 I/2π)·Δθ */
  function dtheta(wx,wy,a,b){ var t1=Math.atan2(a[1]-wy,a[0]-wx), t2=Math.atan2(b[1]-wy,b[0]-wx), d=t2-t1; while(d>PI) d-=2*PI; while(d<-PI) d+=2*PI; return d; }
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    sc=h/10; ox=w/2; oy=h/2;
    F3.setOut(root,'W',F3.fmt(S.W,2)+' cm'); F3.setOut(root,'H',F3.fmt(S.H,2)+' cm');
    /* corpo do solenoide */
    ctx.fillStyle=c.B; ctx.globalAlpha=0.07; var t0=toP(0,Rs); ctx.fillRect(0,t0[1],w,2*Rs*sc); ctx.globalAlpha=1;
    var key=w+'x'+h;
    if(key!==cacheKey){ cacheKey=key; arrows=[]; var step=24;
      for(var gx=step/2; gx<w; gx+=step) for(var gy=step/2; gy<h; gy+=step){ var m=toW(gx,gy); if(Math.abs(Math.abs(m[1])-Rs)<0.35) continue; var b=Bwires(wires,m[0],m[1]); arrows.push([gx,gy,b[0],b[1]]); } }
    arrows.forEach(function(A){ var B=Math.hypot(A[2],A[3]); if(B<B0*0.02) return; var ux=A[2]/B, uy=-A[3]/B, L=8; ctx.globalAlpha=clamp(B/B0,0.15,1); F3.arrow(ctx,A[0]-ux*L,A[1]-uy*L,A[0]+ux*L,A[1]+uy*L,c.B,1.3,5); });
    ctx.globalAlpha=1;
    var xl=w/2/sc+1;
    wires.forEach(function(o){ if(Math.abs(o.x)>xl) return; var q=toP(o.x,o.y); if(o.I>0) F3.dotOut(ctx,q[0],q[1],5,c.E); else F3.crossIn(ctx,q[0],q[1],5,c.E); });
    /* retângulo anti-horário */
    var W=S.W, H=S.H, C=[[rect.x-W/2,rect.y-H/2],[rect.x+W/2,rect.y-H/2],[rect.x+W/2,rect.y+H/2],[rect.x-W/2,rect.y+H/2]];
    var tot=0, Nenc=0;
    wires.forEach(function(o){ var s=0; for(var e=0;e<4;e++) s+=dtheta(o.x,o.y,C[e],C[(e+1)%4]); tot+=o.I*s/(2*PI);
      if(o.x>C[0][0]&&o.x<C[1][0]&&o.y>C[0][1]&&o.y<C[2][1]) Nenc+=o.I>0?1:-1; });
    ctx.strokeStyle=c.S; ctx.lineWidth=2.2; ctx.beginPath(); var q0=toP(C[0][0],C[0][1]); ctx.moveTo(q0[0],q0[1]);
    for(var e=1;e<=4;e++){ var q1=toP(C[e%4][0],C[e%4][1]); ctx.lineTo(q1[0],q1[1]); } ctx.stroke();
    for(e=0;e<4;e++){ var A1=toP(C[e][0],C[e][1]), A2=toP(C[(e+1)%4][0],C[(e+1)%4][1]), mx=(A1[0]+A2[0])/2, my=(A1[1]+A2[1])/2, dx=(A2[0]-A1[0]), dy=(A2[1]-A1[1]), L=Math.hypot(dx,dy)||1; F3.arrow(ctx,mx-dx/L*8,my-dy/L*8,mx+dx/L*8,my+dy/L*8,c.S,2.2,9); }
    F3.label(ctx,'a',toP(C[0][0],C[0][1])[0]-10,toP(C[0][0],C[0][1])[1]+10,c.S,12,'center','600');
    F3.label(ctx,'b',toP(C[1][0],C[1][1])[0]+10,toP(C[1][0],C[1][1])[1]+10,c.S,12,'center','600');
    F3.label(ctx,'c',toP(C[2][0],C[2][1])[0]+10,toP(C[2][0],C[2][1])[1]-10,c.S,12,'center','600');
    F3.label(ctx,'d',toP(C[3][0],C[3][1])[0]-10,toP(C[3][0],C[3][1])[1]-10,c.S,12,'center','600');
    F3.label(ctx,'campo dentro ≈ μ0 n I →',8,oy,c.B,12,'left');
    var Bc=Bwires(wires,0,0);
    out.innerHTML='<span>∮B·dl / μ0 = <b class="hl">'+F3.fmt(tot,2)+' A</b></span><span>espiras abraçadas: <b>'+Nenc+'</b> × '+Iw+' A = <b class="hl">'+F3.fmt(Nenc*Iw,2)+' A</b></span><span>B no centro (soma dos fios): <b>'+F3.fmt(Math.hypot(Bc[0],Bc[1])*1e3,3)+' mT</b></span><span>μ0 n I = <b>'+F3.fmt(B0*1e3,3)+' mT</b> (n = 200 espiras/m)</span>';
  });
})();

/* ================= 4. Toroide ================= */
(function(){
  var root=$('w-toroide'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var r1=2, r2=5, wires=[], keyW='', keyF='', arrows=[], keyC='', circ=0;
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var N=Math.round(S.N), I=S.I, r=S.r;
    F3.setOut(root,'N',String(N)); F3.setOut(root,'I',F3.fmt(I,1)+' A'); F3.setOut(root,'r',F3.fmt(r,2)+' cm');
    var kw=N+'|'+I; if(kw!==keyW){ keyW=kw; wires=[]; for(var k=0;k<N;k++){ var an=2*PI*(k+0.5)/N; wires.push({x:r1*Math.cos(an),y:r1*Math.sin(an),I:I}); wires.push({x:r2*Math.cos(an),y:r2*Math.sin(an),I:-I}); } keyF=''; keyC=''; }
    var Ls=Math.min(h-16,w*0.55), cx=8+Ls/2, cy=h/2, sc=(Ls/2-8)/7;
    function toW(px,py){ return [(px-cx)/sc,(cy-py)/sc]; }
    /* núcleo */
    ctx.fillStyle=c.E; ctx.globalAlpha=0.08; ctx.beginPath(); ctx.arc(cx,cy,r2*sc,0,7); ctx.arc(cx,cy,r1*sc,0,7,true); ctx.fill(); ctx.globalAlpha=1;
    var Bref=MU0*N*I/(2*PI*0.035);
    var kf=keyW+'|'+w+'|'+h; if(kf!==keyF){ keyF=kf; arrows=[]; var step=Math.max(20,Ls/16);
      for(var gx=cx-Ls/2+step/2; gx<cx+Ls/2; gx+=step) for(var gy=cy-Ls/2+step/2; gy<cy+Ls/2; gy+=step){ var m=toW(gx,gy), rr=Math.hypot(m[0],m[1]); if(rr>7||Math.abs(rr-r1)<0.3||Math.abs(rr-r2)<0.3) continue; var b=Bwires(wires,m[0],m[1]); arrows.push([gx,gy,b[0],b[1]]); } }
    arrows.forEach(function(A){ var B=Math.hypot(A[2],A[3]); if(B<Bref*0.03) return; var ux=A[2]/B, uy=-A[3]/B, L=7; ctx.globalAlpha=clamp(B/Bref,0.15,1); F3.arrow(ctx,A[0]-ux*L,A[1]-uy*L,A[0]+ux*L,A[1]+uy*L,c.B,1.3,5); });
    ctx.globalAlpha=1;
    var rad=N>40?3.5:5;
    wires.forEach(function(o){ var px=cx+o.x*sc, py=cy-o.y*sc; if(o.I>0) F3.dotOut(ctx,px,py,rad,c.E); else F3.crossIn(ctx,px,py,rad,c.E); });
    /* laço */
    var kc=keyW+'|'+r; if(kc!==keyC){ keyC=kc; circ=0; var n=720;
      for(var j=0;j<n;j++){ var a0=2*PI*j/n, a1=2*PI*(j+1)/n, am=(a0+a1)/2, b=Bwires(wires,r*Math.cos(am),r*Math.sin(am)); circ+=(b[0]*(-Math.sin(am))+b[1]*Math.cos(am))*r/100*(a1-a0); } }
    ctx.strokeStyle=c.S; ctx.lineWidth=2.2; ctx.setLineDash([6,4]); ctx.beginPath(); ctx.arc(cx,cy,r*sc,0,7); ctx.stroke(); ctx.setLineDash([]);
    F3.arrow(ctx,cx+r*sc,cy+6,cx+r*sc,cy-8,c.S,2.2,9);
    /* gráfico */
    var bx=cx+Ls/2+34, box={x:bx,y:24,w:w-bx-14,h:h-60}, Bth=function(q){ return (q>r1&&q<r2)? MU0*N*I/(2*PI*q/100) : 0; };
    var Bmx=MU0*N*I/(2*PI*r1/100)*1.15;
    if(box.w>80){
      var P=F3.plot(ctx,box,[0,7],[0,Bmx],c,{xl:'r (cm)',yl:'B (mT)'});
      F3.curve(ctx,Bth,0,7,P,c.B,2.3,null,700);
      [r1,r2].forEach(function(q){ ctx.strokeStyle=c.E; ctx.setLineDash([3,4]); ctx.beginPath(); ctx.moveTo(P.X(q),box.y); ctx.lineTo(P.X(q),box.y+box.h); ctx.stroke(); ctx.setLineDash([]); });
      for(var t=0;t<=7;t++) F3.label(ctx,String(t),P.X(t),box.y+box.h+12,c.muted,10,'center');
      F3.label(ctx,F3.fmt(Bmx*1e3,2),box.x-4,box.y+6,c.muted,10,'right');
      var Bavg=circ/(2*PI*r/100); ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(r),P.Y(clamp(Bavg,0,Bmx)),5.5,0,7); ctx.fill();
      F3.label(ctx,'buraco',P.X(r1/2),box.y+box.h-10,c.muted,11,'center'); F3.label(ctx,'núcleo',P.X((r1+r2)/2),box.y+12,c.muted,11,'center'); F3.label(ctx,'fora',P.X(6),box.y+box.h-10,c.muted,11,'center');
    }
    var Nenc=r<r1?0:(r<r2?N:0);
    out.innerHTML='<span>∮B·dl / μ0 (numérico) = <b class="hl">'+F3.fmt(circ/MU0,2)+' A</b></span><span>I<sub>enc</sub> = <b class="hl">'+F3.fmt(Nenc*I,2)+' A</b> ('+(r<r1?'buraco: nada':(r<r2?'N espiras atravessam':'N sobem e N descem'))+')</span><span>B = μ0NI/(2πr) = <b>'+F3.fmt(Bth(r)*1e3,3)+' mT</b></span>'+((Math.abs(r-r1)<0.08||Math.abs(r-r2)<0.08)?'<span>⚠ o laço passa em cima das espiras: escolha r dentro ou fora do núcleo</span>':'');
  });
})();

})();
