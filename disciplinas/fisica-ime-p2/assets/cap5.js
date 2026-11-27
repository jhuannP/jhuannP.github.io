/* Capítulo V · Meios magnéticos — widgets (usa window.F3 de core.js) */
(function(){
"use strict";
var F3 = window.F3; if(!F3) return;
var MU0 = F3.MU0, PI = Math.PI;
function $(id){ return document.getElementById(id); }
function bindN(root,S,cb){ F3.bind(root,S,cb); for(var k in S) if(typeof S[k]==="string"&&S[k]!==""&&!isNaN(+S[k])) S[k]=+S[k]; } /* core.js guarda "0" como texto */
function clamp(x,a,b){ return x<a?a:(x>b?b:x); }
function group(root,acts,cb){
  acts.forEach(function(a){ var b=root.querySelector('[data-act="'+a+'"]'); if(!b) return;
    b.addEventListener('click',function(){ acts.forEach(function(o){ var x=root.querySelector('[data-act="'+o+'"]'); if(x) x.classList.toggle('on',o===a); }); cb(a); }); });
}
function rgb(hex,fb){ var m=/^#?([0-9a-f]{6})$/i.exec((hex||'').trim()); if(!m) return fb; var n=parseInt(m[1],16); return [(n>>16)&255,(n>>8)&255,n&255]; }
/* pseudo-aleatório reprodutível para o desenho das setas */
var seed=7; function rnd(){ seed=(seed*16807)%2147483647; return seed/2147483647; }

/* ================= 1. Arruela: campo no eixo ================= */
(function(){
  var root=$('w-arruela'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S,function(k){ if(k==='R'&&S.r>S.R-0.2) F3.setRange(root,'r',Math.max(0,S.R-0.2),S); if(k==='r'&&S.r>S.R-0.2) F3.setRange(root,'r',Math.max(0,S.R-0.2),S); });
  function loop(I,a,z){ if(a<=0) return 0; return MU0*I*a*a/(2*Math.pow(a*a+z*z,1.5)); } /* SI */
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    if(S.r>S.R-0.2) F3.setRange(root,'r',Math.max(0,S.R-0.2),S);
    var R=S.R/100, r=S.r/100, Ib=S.M*1e3*S.t*1e-3;
    F3.setOut(root,'R',F3.fmt(S.R,1)+' cm'); F3.setOut(root,'r',F3.fmt(S.r,1)+' cm'); F3.setOut(root,'M',F3.fmt(S.M,0)+' kA/m'); F3.setOut(root,'t',F3.fmt(S.t,1)+' mm');
    var tot=function(z){ return loop(Ib,R,z/100)-loop(Ib,r,z/100); };
    var mdip=S.M*1e3*PI*(R*R-r*r)*S.t*1e-3, dip=function(z){ var zz=Math.abs(z/100); return zz<1e-4?NaN:MU0*mdip/(2*PI*zz*zz*zz); };
    var Zm=Math.max(3*S.R,6), lo=0, hi=0;
    for(var q=0;q<=300;q++){ var v=tot(-Zm+2*Zm*q/300); lo=Math.min(lo,v); hi=Math.max(hi,v); }
    var span=Math.max(hi,-lo,1e-9)*1.25, y0=lo<-1e-12?-span:-span*0.15;
    var wide=w>560, insetW=wide?Math.min(230,w*0.3):0;
    /* desenho em corte (vista lateral) */
    if(wide){ var cx=insetW/2+8, cy=h/2, sc=(insetW/2-14)/5, th=Math.max(6,S.t*3);
      F3.label(ctx,'corte pelo eixo',cx,18,c.muted,12,'center');
      ctx.strokeStyle=c.muted; ctx.setLineDash([4,4]); ctx.beginPath(); ctx.moveTo(cx,30); ctx.lineTo(cx,h-20); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle=c.E; ctx.globalAlpha=0.3; ctx.fillRect(cx+S.r*sc,cy-th/2,(S.R-S.r)*sc,th); ctx.fillRect(cx-S.R*sc,cy-th/2,(S.R-S.r)*sc,th); ctx.globalAlpha=1;
      for(var k=0;k<4;k++){ var xx=cx-S.R*sc+(S.R-S.r)*sc*(k+0.5)/4; F3.arrow(ctx,xx,cy+th/2-1,xx,cy-th/2-10,c.ok,1.6,5); F3.arrow(ctx,2*cx-xx,cy+th/2-1,2*cx-xx,cy-th/2-10,c.ok,1.6,5); }
      F3.crossIn(ctx,cx+S.R*sc,cy+th/2+12,6,c.E); F3.dotOut(ctx,cx-S.R*sc,cy+th/2+12,6,c.E);
      if(S.r>0.05){ F3.dotOut(ctx,cx+S.r*sc,cy+th/2+12,6,c.neg); F3.crossIn(ctx,cx-S.r*sc,cy+th/2+12,6,c.neg); }
      F3.label(ctx,'M',cx+S.R*sc*0.6,cy-th/2-20,c.ok,13,'center','600');
      F3.label(ctx,'+Ib (externa)',cx,cy+60,c.E,12,'center'); if(S.r>0.05) F3.label(ctx,'−Ib (interna)',cx,cy+78,c.neg,12,'center');
      /* seta do campo no centro */
      var B0=tot(0), Ls=clamp(Math.abs(B0)/span*80,8,70); F3.arrow(ctx,cx,cy-30,cx,cy-30-(B0>=0?Ls:-Ls),c.B,2.5,8); F3.label(ctx,'B(0)',cx+8,cy-38,c.B,12,'left');
    }
    var box={x:insetW+50,y:22,w:w-insetW-66,h:h-56};
    var P=F3.plot(ctx,box,[-Zm,Zm],[y0,span],c,{xl:'z (cm)',yl:'B no eixo (mT)'});
    ctx.save(); ctx.beginPath(); ctx.rect(box.x,box.y,box.w,box.h); ctx.clip();
    F3.curve(ctx,function(z){return loop(Ib,R,z/100);},-Zm,Zm,P,c.E,1.5,[6,4]);
    if(S.r>0.05) F3.curve(ctx,function(z){return -loop(Ib,r,z/100);},-Zm,Zm,P,c.neg,1.5,[6,4]);
    F3.curve(ctx,dip,-Zm,Zm,P,c.muted,1.3,[2,4]);
    F3.curve(ctx,tot,-Zm,Zm,P,c.B,2.6,null,400);
    ctx.restore();
    F3.label(ctx,F3.fmt(span*1e3,1),box.x-4,box.y+4,c.muted,10,'right'); if(y0<0) F3.label(ctx,F3.fmt(y0*1e3,1),box.x-4,box.y+box.h-4,c.muted,10,'right');
    F3.label(ctx,'−'+F3.fmt(Zm,0),box.x,box.y+box.h+12,c.muted,10,'left'); F3.label(ctx,F3.fmt(Zm,0),box.x+box.w,box.y+box.h+12,c.muted,10,'right');
    /* zero */
    var zc=NaN; for(q=0;q<600;q++){ var z1=Zm*q/600, z2=Zm*(q+1)/600; if(tot(z1)*tot(z2)<0){ zc=(z1+z2)/2; break; } }
    out.innerHTML='<span>I<sub>b</sub> = M·t = <b class="hl">'+F3.fmt(Ib,0)+' A</b></span><span>B(0) = <b>'+F3.fmt(tot(0)*1e3,2)+' mT</b>'+(tot(0)<0?' (contra M)':'')+'</span>'+(isFinite(zc)?'<span>B muda de sinal em |z| ≈ <b>'+F3.fmt(zc,2)+' cm</b></span>':'')+'<span>m = M·volume = <b>'+F3.fmt(mdip,2)+' A·m²</b></span>';
  });
})();

/* ================= 2. As cinco respostas (campo médio) ================= */
(function(){
  var root=$('w-ordens'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout'), mode='ferro';
  var key='', curve=[], prevF=1;
  bindN(root,S);
  group(root,['dia','para','ferro','anti','ferri'],function(a){ mode=a; key=''; prevF=1; });
  var muA=1, muB=1;
  function solve(md,T,h,start){
    var mA, mB, i, nA, nB;
    if(md==='dia') return {A:-0.5*h,B:-0.5*h,M:-0.5*h,ord:false};
    if(md==='para'){ mA=Math.tanh(h/T); return {A:mA,B:mA,M:mA,ord:false}; }
    if(md==='ferro'){ mA=start===undefined?(h<0?-1:1):start; if(Math.abs(mA)<0.05) mA=h<0?-0.5:0.5;
      for(i=0;i<400;i++) mA=0.5*mA+0.5*Math.tanh((mA+h)/T); return {A:mA,B:mA,M:mA,ord:T<1}; }
    var a=1, b=(md==='ferri')?0.6:1, J=1/(a*b); mA=1; mB=-1;
    for(i=0;i<600;i++){ nA=Math.tanh(a*(h-J*b*mB)/T); nB=Math.tanh(b*(h-J*a*mA)/T); mA=0.5*mA+0.5*nA; mB=0.5*mB+0.5*nB; }
    return {A:mA,B:mB,M:(a*mA+b*mB)/(a+b),ord:T<1,stag:(mA-mB)/2};
  }
  /* sítios: posição, sub-rede, fase aleatória */
  var sites=[]; for(var j=0;j<7;j++) for(var i=0;i<12;i++) sites.push({i:i,j:j,sub:(i+j)%2,ph:rnd()*6.28,om:0.6+rnd()*1.4,amp:0.4+0.6*rnd(),off:rnd()*2-1});
  F3.loop(root,function(dt,t){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var T=S.T, hh=S.h;
    F3.setOut(root,'T',F3.fmt(T,2)); F3.setOut(root,'h',F3.fmt(hh,2));
    var s=solve(mode,T,hh,prevF); if(mode==='ferro') prevF=s.M;
    muB=mode==='ferri'?0.6:1;
    var k=mode+'|'+hh; if(k!==key){ key=k; curve=[]; var pf=hh<0?-1:1; for(var q=0;q<=120;q++){ var TT=0.02+1.98*q/120, r=solve(mode,TT,hh,pf); if(mode==='ferro') pf=r.M; curve.push([TT,r.M,r.stag]); } }
    var wide=w>560, Lw=wide?w*0.5:w, cols=12, rows=7, cell=Math.min((Lw-30)/cols,(h-30)/rows), x0=(Lw-cell*cols)/2+(wide?10:0), y0=(h-cell*rows)/2;
    /* campo aplicado */
    if(hh!==0){ var Lh=40*Math.abs(hh)+10; F3.arrow(ctx,x0-14,h/2+(hh>0?Lh/2:-Lh/2),x0-14,h/2-(hh>0?Lh/2:-Lh/2),c.S,3,9); F3.label(ctx,'H',x0-14,hh>0?h/2-Lh/2-10:h/2+Lh/2+10,c.S,12,'center','600'); }
    sites.forEach(function(o){
      var cx=x0+(o.i+0.5)*cell, cy=y0+(o.j+0.5)*cell, m, col, len;
      if(mode==='dia'){ ctx.fillStyle=c.muted; ctx.beginPath(); ctx.arc(cx,cy,1.8,0,7); ctx.fill(); if(Math.abs(hh)<0.02) return;
        len=cell*0.38*Math.abs(hh); var dir=hh>0?1:-1; F3.arrow(ctx,cx,cy-dir*len/2,cx,cy+dir*len/2,c.neg,1.6,5); return; }
      var sub=(mode==='anti'||mode==='ferri')?o.sub:0;
      m=sub?s.B:s.A; col=sub?c.B:c.E; len=cell*0.42*(sub?muB:1);
      var dev=Math.pow(1-Math.min(1,Math.abs(m)),0.7)*PI*(o.amp*Math.sin(o.om*t*2+o.ph)*0.5+o.off*0.5);
      var base=m>=0?0:PI, an=base+dev, ux=Math.sin(an), uy=-Math.cos(an);
      F3.arrow(ctx,cx-ux*len,cy-uy*len,cx+ux*len,cy+uy*len,col,2,6);
    });
    /* gráfico M(T) */
    if(wide){ var box={x:Lw+40,y:24,w:w-Lw-56,h:h-62}, P=F3.plot(ctx,box,[0,2],[-1.05,1.05],c,{xl:'T / T(ordem)',yl:mode==='dia'?'M (×10⁴ exagerado)':'M / Mmáx'});
      ctx.strokeStyle=c.muted; ctx.setLineDash([3,4]); ctx.beginPath(); ctx.moveTo(P.X(1),box.y); ctx.lineTo(P.X(1),box.y+box.h); ctx.stroke(); ctx.setLineDash([]);
      if(mode!=='dia'&&mode!=='para') F3.label(ctx,mode==='anti'?'TN':'TC',P.X(1)+4,box.y+10,c.muted,11,'left');
      ctx.strokeStyle=c.B; ctx.lineWidth=2.4; ctx.beginPath(); curve.forEach(function(p,ii){ var X=P.X(p[0]),Y=P.Y(p[1]); ii?ctx.lineTo(X,Y):ctx.moveTo(X,Y); }); ctx.stroke();
      if(mode==='anti'||mode==='ferri'){ ctx.strokeStyle=c.E; ctx.lineWidth=1.5; ctx.setLineDash([5,4]); ctx.beginPath(); curve.forEach(function(p,ii){ var X=P.X(p[0]),Y=P.Y(p[2]); ii?ctx.lineTo(X,Y):ctx.moveTo(X,Y); }); ctx.stroke(); ctx.setLineDash([]); F3.label(ctx,'ordem das sub-redes',box.x+box.w-4,box.y+12,c.E,11,'right'); }
      F3.label(ctx,'M total',box.x+box.w-4,box.y+box.h-12,c.B,11,'right');
      ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(T),P.Y(s.M),5.5,0,7); ctx.fill();
      F3.label(ctx,'0',P.X(0),box.y+box.h+12,c.muted,10,'center'); F3.label(ctx,'1',P.X(1),box.y+box.h+12,c.muted,10,'center'); F3.label(ctx,'2',P.X(2),box.y+box.h+12,c.muted,10,'center');
    }
    var nomes={dia:'Diamagnético: M oposto a H, χ &lt; 0, sem momentos permanentes',para:'Paramagnético: momentos ao acaso; H alinha um pouco; χ ∝ 1/T',ferro:'Ferromagnético: M espontâneo abaixo de T<sub>C</sub>',anti:'Antiferromagnético: sub-redes iguais e opostas abaixo de T<sub>N</sub>; M ≈ 0',ferri:'Ferrimagnético: sub-redes opostas e desiguais; M espontâneo'};
    out.innerHTML='<span><b>'+nomes[mode]+'</b></span><span>M = <b class="hl">'+F3.fmt(s.M,3)+'</b></span>'+((mode==='anti'||mode==='ferri')?'<span>sub-rede A: <b>'+F3.fmt(s.A,2)+'</b> · sub-rede B: <b>'+F3.fmt(s.B,2)+'</b></span>':'')+'<span>ordem espontânea: <b>'+(s.ord?'sim':'não')+'</b></span>';
  });
})();

/* ================= 3. Ising: domínios e Curie ================= */
(function(){
  var root=$('w-dominios'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var LX=100, LY=60, N=LX*LY, s=new Int8Array(N), i;
  function shuffle(){ for(i=0;i<N;i++) s[i]=Math.random()<0.5?1:-1; }
  shuffle();
  var off=document.createElement('canvas'); off.width=LX; off.height=LY; var octx=off.getContext('2d'), img=octx.createImageData(LX,LY);
  var pts=[], cooling=false, last=performance.now(), stepT=0, acc=0, accN=0;
  root.querySelector('[data-act=quente]').addEventListener('click',function(){ shuffle(); });
  var bCool=root.querySelector('[data-act=cool]');
  bCool.addEventListener('click',function(){ cooling=!cooling; bCool.classList.toggle('on',cooling); if(cooling){ F3.setRange(root,'T',4,S); F3.setRange(root,'h',0,S); shuffle(); stepT=0; acc=0; accN=0; } });
  root.querySelector('[data-act=limpa]').addEventListener('click',function(){ pts=[]; });
  var Tc=2/Math.log(1+Math.SQRT2);
  function onsager(T){ if(T>=Tc) return 0; var x=Math.pow(Math.sinh(2/T),-4); return Math.pow(1-x,0.125); }
  function sweep(T,h){
    for(var n=0;n<N;n++){ var p=(Math.random()*N)|0, x=p%LX, y=(p/LX)|0;
      var sum=s[y*LX+(x+1)%LX]+s[y*LX+(x+LX-1)%LX]+s[((y+1)%LY)*LX+x]+s[((y+LY-1)%LY)*LX+x];
      var si=s[p];
      var dE=2*si*(sum+h); if(dE<=0||Math.random()<Math.exp(-dE/T)) s[p]=-si; }
  }
  F3.loop(root,function(){
    var now=performance.now(), rdt=Math.min(0.1,(now-last)/1000); last=now;
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var T=S.T, hh=S.h;
    sweep(T,hh); sweep(T,hh);
    var M=0; for(i=0;i<N;i++) M+=s[i]; M/=N;
    if(cooling){ stepT+=rdt; if(stepT>0.35){ acc+=Math.abs(M); accN++; } if(stepT>0.7){ pts.push([T,acc/Math.max(1,accN)]); acc=0; accN=0; stepT=0; var Tn=Math.round((T-0.05)*100)/100; if(Tn<0.8){ cooling=false; bCool.classList.remove('on'); } else F3.setRange(root,'T',Tn,S); } }
    F3.setOut(root,'T',F3.fmt(S.T,2)); F3.setOut(root,'h',F3.fmt(S.h,2));
    var up=rgb(c.E,[255,154,77]), dn=rgb(c.B,[95,212,255]), d=img.data;
    for(i=0;i<N;i++){ var col=s[i]>0?up:dn, q=i*4; d[q]=col[0]; d[q+1]=col[1]; d[q+2]=col[2]; d[q+3]=255; }
    octx.putImageData(img,0,0);
    var wide=w>560, gw=wide?Math.min((w*0.58)-16,(h-16)*LX/LY):w-16, gh=gw*LY/LX;
    if(gh>h-16){ gh=h-16; gw=gh*LX/LY; }
    ctx.imageSmoothingEnabled=false; ctx.drawImage(off,8,(h-gh)/2,gw,gh); ctx.imageSmoothingEnabled=true;
    if(wide){ var box={x:gw+56,y:24,w:w-gw-72,h:h-62}, P=F3.plot(ctx,box,[0.5,4.5],[0,1.05],c,{xl:'T',yl:'|M|'});
      F3.curve(ctx,onsager,0.5,4.5,P,c.muted,1.6,[5,4],400);
      ctx.strokeStyle=c.ok; ctx.setLineDash([3,4]); ctx.beginPath(); ctx.moveTo(P.X(Tc),box.y); ctx.lineTo(P.X(Tc),box.y+box.h); ctx.stroke(); ctx.setLineDash([]);
      F3.label(ctx,'TC ≈ 2,27',P.X(Tc)+4,box.y+10,c.ok,11,'left');
      pts.forEach(function(p){ ctx.fillStyle=c.B; ctx.beginPath(); ctx.arc(P.X(p[0]),P.Y(p[1]),3.2,0,7); ctx.fill(); });
      ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(T),P.Y(Math.abs(M)),5.5,0,7); ctx.fill();
      for(var tk=1;tk<=4;tk++) F3.label(ctx,String(tk),P.X(tk),box.y+box.h+12,c.muted,10,'center');
      F3.label(ctx,'Onsager (exato)',box.x+box.w-4,box.y+box.h-12,c.muted,11,'right');
    }
    out.innerHTML='<span>M = <b class="hl">'+F3.fmt(M,3)+'</b></span><span>T/T<sub>C</sub> = <b>'+F3.fmt(T/Tc,2)+'</b></span><span>'+(T<Tc?'abaixo de T<sub>C</sub>: domínios crescem e ordenam':'acima de T<sub>C</sub>: desordem (paramagnético)')+'</span>'+(cooling?'<span><b>resfriando…</b></span>':'');
  });
})();

/* ================= 4. Histerese ================= */
(function(){
  var root=$('w-histerese'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  var wd=0.35, M=0, Hprev=0, virgin=true, trail=[[0,0]], auto=false, tA=0;
  bindN(root,S,function(k){ if(k==='Hc'){ reset(); } });
  function asc(H){ return Math.tanh((H-S.Hc)/wd); }
  function desc(H){ return Math.tanh((H+S.Hc)/wd); }
  function an(H){ return Math.tanh(H/(wd+S.Hc)); }
  function reset(){ M=0; Hprev=0; virgin=true; trail=[[0,0]]; F3.setRange(root,'H',0,S); }
  var bAuto=root.querySelector('[data-act=auto]');
  bAuto.addEventListener('click',function(){ auto=!auto; bAuto.classList.toggle('on',auto); tA=Math.asin(clamp(S.H/2.6,-1,1))/1.3; });
  root.querySelector('[data-act=mole]').addEventListener('click',function(){ F3.setRange(root,'Hc',0.15,S); reset(); });
  root.querySelector('[data-act=duro]').addEventListener('click',function(){ F3.setRange(root,'Hc',1.5,S); reset(); });
  root.querySelector('[data-act=virgem]').addEventListener('click',reset);
  function update(H){
    var dH=H-Hprev; if(dH===0) return;
    if(virgin && H*dH<0) virgin=false;
    if(virgin){ M = H>=0 ? Math.max(an(H),asc(H)) : Math.min(an(H),desc(H)); }
    else if(dH>0) M=Math.max(M,asc(H)); else M=Math.min(M,desc(H));
    Hprev=H; trail.push([H,M]); if(trail.length>2500) trail.shift();
  }
  F3.loop(root,function(dt){
    if(auto){ tA+=dt; F3.setRange(root,'H',(2.6*Math.sin(1.3*tA)).toFixed(3),S); }
    /* sub-passos para não pular trechos quando o slider anda rápido */
    var Ht=S.H, steps=Math.max(1,Math.ceil(Math.abs(Ht-Hprev)/0.01)), H0=Hprev; for(var k=1;k<=steps;k++) update(H0+(Ht-H0)*k/steps);
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    F3.setOut(root,'H',F3.fmt(S.H,2)); F3.setOut(root,'Hc',F3.fmt(S.Hc,2));
    var wide=w>560, dW=wide?120:0, box={x:46,y:20,w:w-dW-66,h:h-52};
    var P=F3.plot(ctx,box,[-3,3],[-1.15,1.15],c,{xl:'H (unid. arb.)',yl:'M / Ms'});
    ctx.strokeStyle=c.grid; ctx.beginPath(); ctx.moveTo(P.X(0),box.y); ctx.lineTo(P.X(0),box.y+box.h); ctx.stroke();
    F3.curve(ctx,asc,-3,3,P,c.muted,1.2,[4,4]); F3.curve(ctx,desc,-3,3,P,c.muted,1.2,[4,4]);
    F3.curve(ctx,function(H){ return H>=0?Math.max(an(H),asc(H)):NaN; },0,3,P,c.ok,1.2,[2,4]);
    [1,-1].forEach(function(v){ ctx.strokeStyle=c.grid; ctx.setLineDash([2,5]); ctx.beginPath(); ctx.moveTo(box.x,P.Y(v)); ctx.lineTo(box.x+box.w,P.Y(v)); ctx.stroke(); ctx.setLineDash([]); });
    F3.label(ctx,'+Ms',box.x+4,P.Y(1)-9,c.muted,11); F3.label(ctx,'−Ms',box.x+4,P.Y(-1)+9,c.muted,11);
    ctx.strokeStyle=c.B; ctx.lineWidth=2.4; ctx.beginPath(); trail.forEach(function(p,i){ var X=P.X(p[0]),Y=P.Y(p[1]); i?ctx.lineTo(X,Y):ctx.moveTo(X,Y); }); ctx.stroke();
    var Mr=Math.tanh(S.Hc/wd);
    [[0,Mr,'Mr'],[0,-Mr,'−Mr']].forEach(function(p){ ctx.fillStyle=c.ok; ctx.beginPath(); ctx.arc(P.X(p[0]),P.Y(p[1]),4,0,7); ctx.fill(); F3.label(ctx,p[2],P.X(p[0])+7,P.Y(p[1])+(p[1]>0?-9:9),c.ok,12,'left','600'); });
    [[-S.Hc,'−Hc'],[S.Hc,'Hc']].forEach(function(p){ ctx.fillStyle=c.neg; ctx.beginPath(); ctx.arc(P.X(p[0]),P.Y(0),4,0,7); ctx.fill(); F3.label(ctx,p[1],P.X(p[0]),P.Y(0)+(p[0]<0?-12:13),c.neg,12,'center','600'); });
    F3.label(ctx,'curva inicial',P.X(0.9),P.Y(an(0.9))+16,c.ok,11,'left');
    ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(S.H),P.Y(M),6,0,7); ctx.fill();
    for(var tk=-3;tk<=3;tk++) F3.label(ctx,String(tk),P.X(tk),box.y+box.h+12,c.muted,10,'center');
    /* domínios */
    if(wide){ var dx=w-dW+10, cols=3, rows=4, cw=(dW-24)/cols, ch=(h-80)/rows, nUp=Math.round((M+1)/2*cols*rows);
      F3.label(ctx,'domínios',dx+(dW-24)/2,16,c.muted,12,'center');
      for(var q=0;q<cols*rows;q++){ var cx=dx+(q%cols+0.5)*cw, cy=34+(Math.floor(q/cols)+0.5)*ch, upq=((q*7)%12)<nUp;
        ctx.strokeStyle=c.grid; ctx.strokeRect(cx-cw/2+1,cy-ch/2+1,cw-2,ch-2);
        F3.arrow(ctx,cx,cy+(upq?ch*0.3:-ch*0.3),cx,cy-(upq?ch*0.3:-ch*0.3),upq?c.E:c.B,2.2,7); } }
    var slope=NaN; if(trail.length>3){ var a=trail[trail.length-1], b=trail[trail.length-4]; if(Math.abs(a[0]-b[0])>1e-4) slope=(a[1]-b[1])/(a[0]-b[0]); }
    out.innerHTML='<span>M/M<sub>s</sub> = <b class="hl">'+F3.fmt(M,3)+'</b></span><span>M<sub>r</sub>/M<sub>s</sub> = <b>'+F3.fmt(Mr,3)+'</b></span><span>H<sub>c</sub> = <b>'+F3.fmt(S.Hc,2)+'</b></span><span>dM/dH local = <b>'+(isFinite(slope)?F3.fmt(slope,2):'—')+'</b></span><span>'+(virgin?'na curva inicial':(Math.abs(M)>0.98?'saturação: dM/dH ≈ 0':'no laço'))+'</span>';
  });
  reset();
})();

})();
