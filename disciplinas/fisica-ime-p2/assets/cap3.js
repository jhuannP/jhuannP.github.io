/* Capítulo III · Lei de Biot–Savart — widgets (usa window.F3 de core.js) */
(function(){
"use strict";
var F3 = window.F3; if(!F3) return;
var MU0 = F3.MU0, PI = Math.PI;
function $(id){ return document.getElementById(id); }
function bindN(root,S,cb){ F3.bind(root,S,cb); for(var k in S) if(typeof S[k]==="string"&&S[k]!==""&&!isNaN(+S[k])) S[k]=+S[k]; } /* core.js guarda "0" como texto */
function clamp(x,a,b){ return x<a?a:(x>b?b:x); }
/* arrastar com ponteiro (mouse/toque). down(p) devolve false para ignorar. */
function drag(cv,down,move){
  cv.style.touchAction='none'; var on=false;
  function pos(e){ var r=cv.getBoundingClientRect(); return {x:e.clientX-r.left,y:e.clientY-r.top}; }
  cv.addEventListener('pointerdown',function(e){ var p=pos(e); if(down(p)===false) return; on=true; try{cv.setPointerCapture(e.pointerId);}catch(_){} e.preventDefault(); });
  cv.addEventListener('pointermove',function(e){ if(on) move(pos(e)); });
  function stop(){ on=false; }
  cv.addEventListener('pointerup',stop); cv.addEventListener('pointercancel',stop);
}
/* grupo de botões exclusivos */
function group(root,acts,cb){
  acts.forEach(function(a){ var b=root.querySelector('[data-act="'+a+'"]'); if(!b) return;
    b.addEventListener('click',function(){ acts.forEach(function(o){ var x=root.querySelector('[data-act="'+o+'"]'); if(x) x.classList.toggle('on',o===a); }); cb(a); }); });
}
function uT(B){ return F3.fmt(B*1e6, Math.abs(B*1e6)<10?2:1)+' μT'; }

/* ================= 1. Bússola de Oersted ================= */
(function(){
  var root=$('w-oersted'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var on=false, timer=null, sgn=1, th=0, om=0, BT=18e-6;
  var bOn=root.querySelector('[data-act=on]');
  bOn.addEventListener('click',function(){ on=true; bOn.classList.add('on'); clearTimeout(timer); timer=setTimeout(function(){ on=false; bOn.classList.remove('on'); },2000); });
  root.querySelector('[data-act=flip]').addEventListener('click',function(){ sgn=-sgn; });
  F3.loop(root,function(dt){
    var Bw = on ? sgn*MU0*S.I/(2*PI*S.h/100) : 0;          /* + = oeste (corrente p/ norte, fio acima) */
    var target=Math.atan2(Bw,BT), Bt=Math.hypot(Bw,BT);
    if(F3.reduce){ th=target; om=0; }
    else for(var k=0;k<4;k++){ var a=60*(Bt/BT)*Math.sin(target-th)-4.5*om; om+=a*dt/4; th+=om*dt/4; }
    F3.setOut(root,'I',F3.fmt(S.I,1)+' A'); F3.setOut(root,'h',F3.fmt(S.h,1)+' cm');
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var cx=w*0.34, cy=h/2, R=Math.min(115,w*0.27);
    /* bússola */
    ctx.strokeStyle=c.grid; ctx.lineWidth=2; ctx.beginPath(); ctx.arc(cx,cy,R,0,7); ctx.stroke();
    for(var i=0;i<36;i++){ var an=i*PI/18, r1=R-(i%9===0?12:6); ctx.strokeStyle=c.muted; ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(cx+R*Math.sin(an),cy-R*Math.cos(an)); ctx.lineTo(cx+r1*Math.sin(an),cy-r1*Math.cos(an)); ctx.stroke(); }
    F3.label(ctx,'N',cx,cy-R-12,c.ink,14,'center','600'); F3.label(ctx,'S',cx,cy+R+12,c.muted,13,'center');
    F3.label(ctx,'L',cx+R+12,cy,c.muted,13,'center'); F3.label(ctx,'O',cx-R-12,cy,c.muted,13,'center');
    /* agulha: ângulo th a partir do norte, positivo para oeste (esquerda) */
    var nx=-Math.sin(th), ny=-Math.cos(th), L=R*0.78, wd=9;
    ctx.fillStyle=c.neg; ctx.beginPath(); ctx.moveTo(cx+nx*L,cy+ny*L); ctx.lineTo(cx-ny*wd,cy+nx*wd); ctx.lineTo(cx+ny*wd,cy-nx*wd); ctx.closePath(); ctx.fill();
    ctx.fillStyle=c.muted; ctx.beginPath(); ctx.moveTo(cx-nx*L,cy-ny*L); ctx.lineTo(cx-ny*wd,cy+nx*wd); ctx.lineTo(cx+ny*wd,cy-nx*wd); ctx.closePath(); ctx.fill();
    ctx.fillStyle=c.ink; ctx.beginPath(); ctx.arc(cx,cy,4,0,7); ctx.fill();
    /* fio por cima */
    ctx.globalAlpha=0.8; ctx.fillStyle=on?c.E:c.grid; ctx.fillRect(cx-5,6,10,h-12); ctx.globalAlpha=1;
    if(on){ var y0=sgn>0?h*0.85:h*0.15, y1=sgn>0?h*0.62:h*0.38; F3.arrow(ctx,cx+22,y0,cx+22,y1,c.E,2.5,10); F3.label(ctx,'I',cx+32,(y0+y1)/2,c.E,14,'left','600'); }
    F3.label(ctx,on?'circuito fechado':'circuito aberto',cx,14,on?c.E:c.muted,12,'center');
    /* diagrama de vetores */
    var vx=w*0.78, vy=cy+50, sc=Math.min(70,w*0.14)/20e-6;
    F3.label(ctx,'campos (vista de cima)',vx,24,c.muted,12,'center');
    F3.arrow(ctx,vx,vy,vx,vy-BT*sc,c.ok,2.5); F3.label(ctx,'B Terra',vx+6,vy-BT*sc-8,c.ok,12,'left');
    if(Bw){ var bx=-Bw*sc; var Lw=Math.abs(bx); var bxc=clamp(bx,-w*0.2,w*0.2);
      F3.arrow(ctx,vx,vy,vx+bxc,vy,c.B,2.5); F3.label(ctx,'B fio',vx+bxc/2,vy+14,c.B,12,'center');
      var ang=Math.atan2(Bw,BT), Lr=Math.min(Math.hypot(Bw,BT)*sc, w*0.2);
      F3.arrow(ctx,vx,vy,vx-Math.sin(ang)*Lr,vy-Math.cos(ang)*Lr,c.S,3); F3.label(ctx,'soma',vx-Math.sin(ang)*Lr,vy-Math.cos(ang)*Lr-12,c.S,12,'center');
      if(Lw>w*0.2) F3.label(ctx,'(fora de escala)',vx,vy+32,c.muted,11,'center'); }
    var dev=th*180/PI;
    out.innerHTML='<span>B do fio: <b>'+(on?uT(Math.abs(Bw))+(Bw>0?' (oeste)':' (leste)'):'0 (desligado)')+'</b></span><span>B Terra (horizontal, SP): <b>≈18 μT</b></span><span>desvio da agulha: <b class="hl">'+F3.fmt(Math.abs(dev),0)+'°'+(Math.abs(dev)>0.5?(dev>0?' p/ oeste':' p/ leste'):'')+'</b></span>';
  });
})();

/* ================= 2. Construtor de Biot–Savart ================= */
(function(){
  var root=$('w-construtor'); if(!root) return;
  var cv=root.querySelector('canvas'), st=new F3.Stage(cv), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var shape='fio', scan=true, P={x:3,y:1}, geo={};
  group(root,['fio','espira','quadrado'],function(a){ shape=a; P = a==='fio'?{x:3,y:1}:{x:0.8,y:0.5}; });
  var bScan=root.querySelector('[data-act=scan]');
  bScan.addEventListener('click',function(){ scan=!scan; bScan.classList.toggle('on',scan); });
  function segs(n){
    var L=S.L, s=[], i;
    if(shape==='fio'){ for(i=0;i<n;i++) s.push([0,-L/2+L*i/n,0,-L/2+L*(i+1)/n]); }
    else if(shape==='espira'){ var R=L/2; for(i=0;i<n;i++){ var a0=2*PI*i/n,a1=2*PI*(i+1)/n; s.push([R*Math.cos(a0),R*Math.sin(a0),R*Math.cos(a1),R*Math.sin(a1)]); } }
    else { var h=L/2, C=[[h,-h],[h,h],[-h,h],[-h,-h],[h,-h]], m=Math.max(1,Math.round(n/4));
      for(var k=0;k<4;k++) for(i=0;i<m;i++){ var t0=i/m,t1=(i+1)/m; s.push([C[k][0]+(C[k+1][0]-C[k][0])*t0,C[k][1]+(C[k+1][1]-C[k][1])*t0,C[k][0]+(C[k+1][0]-C[k][0])*t1,C[k][1]+(C[k+1][1]-C[k][1])*t1]); } }
    return s;
  }
  /* dBz (T) de um segmento (cm) no ponto P (cm), corrente I (A): 1e-7·I·100·(dl×r)z/r³ */
  function dBz(sg,I){ var mx=(sg[0]+sg[2])/2,my=(sg[1]+sg[3])/2, dx=sg[2]-sg[0],dy=sg[3]-sg[1], rx=P.x-mx,ry=P.y-my, r=Math.hypot(rx,ry); if(r<0.12) r=0.12; return 1e-5*I*(dx*ry-dy*rx)/(r*r*r); }
  function exact(){
    if(shape==='fio'){ var rho=Math.abs(P.x); if(rho<0.05) return NaN; var x2=S.L/2-P.y, x1=-S.L/2-P.y;
      var b=1e-7*S.I/(rho/100)*(x2/Math.hypot(x2,rho)-x1/Math.hypot(x1,rho)); return P.x>0? -b : b; }
    var s=segs(2400), t=0; for(var i=0;i<s.length;i++) t+=dBz(s[i],S.I); return t;
  }
  var ox,oy,sc;
  function toPx(x,y){ return [ox+x*sc, oy-y*sc]; }
  drag(cv,function(p){ if(p.x>st.w*0.7) return false; P.x=(p.x-ox)/sc; P.y=(oy-p.y)/sc; },function(p){ P.x=clamp((p.x-ox)/sc,-8,8); P.y=clamp((oy-p.y)/sc,-8,8); });
  F3.loop(root,function(dt,t){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var panel=Math.max(110,w*0.24); ox=(w-panel)/2; oy=h/2; sc=Math.min((w-panel)/17,h/16);
    var n=Math.round(S.N), s=segs(n), I=S.I, d=s.map(function(sg){return dBz(sg,I);}), tot=0, mx=1e-12;
    d.forEach(function(v){ tot+=v; mx=Math.max(mx,Math.abs(v)); });
    var ex=exact();
    F3.setOut(root,'N',String(shape==='quadrado'?4*Math.max(1,Math.round(n/4)):n)); F3.setOut(root,'I',F3.fmt(I,1)+' A');
    F3.setOut(root,'L',(shape==='espira'?'R = '+F3.fmt(S.L/2,2):F3.fmt(S.L,1))+' cm');
    /* grade em cm */
    ctx.strokeStyle=c.grid; ctx.lineWidth=1; ctx.globalAlpha=0.5;
    for(var g=-8;g<=8;g+=2){ var a=toPx(g,-8),b=toPx(g,8); ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(b[0],b[1]); ctx.stroke(); a=toPx(-8,g); b=toPx(8,g); ctx.beginPath(); ctx.moveTo(a[0],a[1]); ctx.lineTo(b[0],b[1]); ctx.stroke(); }
    ctx.globalAlpha=1;
    /* segmentos coloridos */
    var k=scan&&!F3.reduce? Math.floor((t*Math.max(2,n)/3.5)%s.length) : -1, part=0;
    for(var i=0;i<s.length;i++){
      var p0=toPx(s[i][0],s[i][1]), p1=toPx(s[i][2],s[i][3]), f=Math.abs(d[i])/mx;
      var gx=(p1[0]-p0[0])*0.06, gy=(p1[1]-p0[1])*0.06;
      ctx.strokeStyle=d[i]>=0?c.B:c.neg; ctx.globalAlpha=0.25+0.75*f; ctx.lineWidth=3+6*f; ctx.lineCap='butt';
      ctx.beginPath(); ctx.moveTo(p0[0]+gx,p0[1]+gy); ctx.lineTo(p1[0]-gx,p1[1]-gy); ctx.stroke(); ctx.globalAlpha=1;
      if(i<=k) part+=d[i];
    }
    /* sentido da corrente */
    var s0=s[Math.floor(s.length*0.3)], q0=toPx(s0[0],s0[1]), q1=toPx(s0[2],s0[3]);
    var ux=q1[0]-q0[0], uy=q1[1]-q0[1], ul=Math.hypot(ux,uy)||1;
    F3.arrow(ctx,q0[0]+ux/2-ux/ul*14-uy/ul*16,q0[1]+uy/2-uy/ul*14+ux/ul*16,q0[0]+ux/2+ux/ul*14-uy/ul*16,q0[1]+uy/2+uy/ul*14+ux/ul*16,c.E,2,8);
    F3.label(ctx,'i',q0[0]+ux/2-uy/ul*30,q0[1]+uy/2+ux/ul*30,c.E,14,'center','600');
    var pp=toPx(P.x,P.y);
    if(k>=0){ var sk=s[k], m=toPx((sk[0]+sk[2])/2,(sk[1]+sk[3])/2), e0=toPx(sk[0],sk[1]), e1=toPx(sk[2],sk[3]);
      ctx.setLineDash([5,4]); ctx.strokeStyle=c.S; ctx.lineWidth=1.5; ctx.beginPath(); ctx.moveTo(m[0],m[1]); ctx.lineTo(pp[0],pp[1]); ctx.stroke(); ctx.setLineDash([]);
      F3.arrow(ctx,e0[0],e0[1],e1[0],e1[1],c.S,3,8); F3.label(ctx,'r',(m[0]+pp[0])/2+8,(m[1]+pp[1])/2-8,c.S,13,'left','600'); }
    /* ponto P */
    var big=Math.abs(tot), rr=7+Math.min(9,big/(Math.abs(ex)||big||1)*7);
    if(tot>=0) F3.dotOut(ctx,pp[0],pp[1],rr,c.ink); else F3.crossIn(ctx,pp[0],pp[1],rr,c.ink);
    F3.label(ctx,'P',pp[0]+rr+4,pp[1]-rr,c.ink,14,'left','600');
    /* painel da soma */
    var px=w-panel+16, pw=panel-32, top=34, bot=h-40, mid=(top+bot)/2, ref=Math.max(Math.abs(ex)||0,Math.abs(tot),1e-9)*1.15;
    F3.label(ctx,'Bz em P',px+pw/2,16,c.muted,12,'center');
    ctx.strokeStyle=c.grid; ctx.beginPath(); ctx.moveTo(px,mid); ctx.lineTo(px+pw,mid); ctx.stroke();
    function bar(v,x,wd,col){ var y=mid-v/ref*(mid-top); ctx.fillStyle=col; ctx.fillRect(x,Math.min(y,mid),wd,Math.abs(y-mid)); }
    var shown=k>=0?part:tot;
    bar(shown,px+4,pw*0.4,shown>=0?c.B:c.neg);
    if(isFinite(ex)){ var ye=mid-ex/ref*(mid-top); ctx.strokeStyle=c.S; ctx.lineWidth=2; ctx.setLineDash([4,3]); ctx.beginPath(); ctx.moveTo(px,ye); ctx.lineTo(px+pw,ye); ctx.stroke(); ctx.setLineDash([]); F3.label(ctx,'exato',px+pw,ye-9,c.S,11,'right'); }
    F3.label(ctx,k>=0?'soma parcial':'soma N',px+4+pw*0.2,bot+14,c.ink,11,'center');
    F3.label(ctx,'⊙ +',px+pw,top-6,c.muted,11,'right'); F3.label(ctx,'⊗ −',px+pw,bot+2,c.muted,11,'right');
    var err=isFinite(ex)&&ex!==0?Math.abs((tot-ex)/ex)*100:NaN;
    out.innerHTML='<span>Soma com N pedaços: <b>'+uT(Math.abs(tot))+(tot>=0?' ⊙':' ⊗')+'</b></span><span>Exato: <b>'+(isFinite(ex)?uT(Math.abs(ex))+(ex>=0?' ⊙':' ⊗'):'P em cima do fio')+'</b></span><span>erro: <b class="hl">'+(isFinite(err)?F3.fmt(err,err<1?2:1)+' %':'—')+'</b></span>';
  });
})();

/* ================= 3. Fio reto: bússolas e B(ρ) ================= */
(function(){
  var root=$('w-fio'); if(!root) return;
  var cv=root.querySelector('canvas'), st=new F3.Stage(cv), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  var sgn=1, probe={x:4,y:2}, cx,cy,sc,half;
  root.querySelector('[data-act=flip]').addEventListener('click',function(){ sgn=-sgn; });
  drag(cv,function(p){ if(p.x>cx+half) return false; probe.x=(p.x-cx)/sc; probe.y=(cy-p.y)/sc; },function(p){ probe.x=clamp((p.x-cx)/sc,-10,10); probe.y=clamp((cy-p.y)/sc,-10,10); });
  function Bat(x,y){ var r2=x*x+y*y; var k=sgn*MU0*S.I/(2*PI*Math.sqrt(r2)/100); var r=Math.sqrt(r2); return {bx:-y/r*k, by:x/r*k, B:Math.abs(k)}; }
  F3.loop(root,function(dt,t){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var wide=w>560; half=wide?Math.min(h/2-10,w*0.27):Math.min(h/2-10,w/2-10); cx=half+12; cy=h/2; sc=half/10;
    F3.setOut(root,'I',F3.fmt(S.I,0)+' A');
    /* círculos de campo com pontos andando */
    [1.5,3,5,7.5].forEach(function(rc,j){ var R=rc*sc; ctx.strokeStyle=c.B; ctx.globalAlpha=0.35; ctx.lineWidth=1.2; ctx.beginPath(); ctx.arc(cx,cy,R,0,7); ctx.stroke(); ctx.globalAlpha=1;
      var om=sgn*1.6/(rc*rc)*S.I/10*4; for(var q=0;q<6;q++){ var an=q*PI/3+om*t; ctx.fillStyle=c.B; ctx.beginPath(); ctx.arc(cx+R*Math.cos(an),cy-R*Math.sin(an),2.6,0,7); ctx.fill(); } });
    /* bússolas */
    var step=Math.max(30,half/4);
    for(var gx=cx-half+step/2; gx<cx+half; gx+=step) for(var gy=cy-half+step/2; gy<cy+half; gy+=step){
      var x=(gx-cx)/sc, y=(cy-gy)/sc; if(Math.hypot(gx-cx,gy-cy)<22) continue;
      var b=Bat(x,y), ux=b.bx/b.B, uy=-b.by/b.B, Ln=step*0.34, wd=3.2;
      ctx.fillStyle=c.neg; ctx.beginPath(); ctx.moveTo(gx+ux*Ln,gy+uy*Ln); ctx.lineTo(gx-uy*wd,gy+ux*wd); ctx.lineTo(gx+uy*wd,gy-ux*wd); ctx.closePath(); ctx.fill();
      ctx.fillStyle=c.muted; ctx.beginPath(); ctx.moveTo(gx-ux*Ln,gy-uy*Ln); ctx.lineTo(gx-uy*wd,gy+ux*wd); ctx.lineTo(gx+uy*wd,gy-ux*wd); ctx.closePath(); ctx.fill();
    }
    /* fio */
    ctx.fillStyle=c.bg; ctx.beginPath(); ctx.arc(cx,cy,13,0,7); ctx.fill();
    if(sgn>0) F3.dotOut(ctx,cx,cy,12,c.E); else F3.crossIn(ctx,cx,cy,12,c.E);
    /* sonda */
    var rho=Math.max(0.3,Math.hypot(probe.x,probe.y)); if(Math.hypot(probe.x,probe.y)<0.3){ probe.x=0.3; probe.y=0; }
    var b=Bat(probe.x,probe.y), px=cx+probe.x*sc, py=cy-probe.y*sc, La=clamp(18+12*Math.log10(b.B/1e-6),14,70);
    ctx.strokeStyle=c.muted; ctx.setLineDash([4,4]); ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(px,py); ctx.stroke(); ctx.setLineDash([]);
    F3.label(ctx,'ρ',(cx+px)/2+6,(cy+py)/2-8,c.muted,13);
    F3.arrow(ctx,px,py,px+b.bx/b.B*La,py-b.by/b.B*La,c.S,3,10);
    ctx.fillStyle=c.ink; ctx.beginPath(); ctx.arc(px,py,5,0,7); ctx.fill(); F3.label(ctx,'sonda',px+8,py+12,c.ink,12);
    /* gráfico */
    if(wide){ var bx0=cx+half+50, box={x:bx0,y:24,w:w-bx0-20,h:h-64}, Bmax=MU0*S.I/(2*PI*0.01);
      var P=F3.plot(ctx,box,[0,10],[0,Bmax],c,{xl:'ρ (cm)',yl:'B (μT)'});
      F3.curve(ctx,function(r){ return MU0*S.I/(2*PI*r/100); },0.5,10,P,c.B,2.2);
      var yE=P.Y(20e-6); if(yE>box.y){ ctx.strokeStyle=c.ok; ctx.setLineDash([5,4]); ctx.beginPath(); ctx.moveTo(box.x,yE); ctx.lineTo(box.x+box.w,yE); ctx.stroke(); ctx.setLineDash([]); F3.label(ctx,'Terra ~20 μT',box.x+box.w-4,yE-9,c.ok,11,'right'); }
      for(var tk=0;tk<=10;tk+=2) F3.label(ctx,String(tk),P.X(tk),box.y+box.h+12,c.muted,10,'center');
      F3.label(ctx,F3.fmt(Bmax*1e6,0),box.x-4,box.y+6,c.muted,10,'right');
      if(rho<=10){ var yy=P.Y(Math.min(b.B,Bmax)); ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(rho),yy,5,0,7); ctx.fill(); }
      F3.label(ctx,'B = μ0 i / (2π ρ)',box.x+box.w-6,box.y+14,c.B,13,'right');
    }
    out.innerHTML='<span>ρ = <b>'+F3.fmt(rho,1)+' cm</b></span><span>B = <b class="hl">'+uT(b.B)+'</b></span><span>B·ρ = <b>'+F3.fmt(b.B*1e6*rho,0)+' μT·cm</b> (constante!)</span><span>corrente: <b>'+(sgn>0?'saindo ⊙ → B anti-horário':'entrando ⊗ → B horário')+'</b></span>';
  });
})();

/* ================= 4. Solenoide: B(z) no eixo ================= */
(function(){
  var root=$('w-solenoide'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout'), shape='sq';
  bindN(root,S);
  group(root,['sq','ci'],function(a){ shape=a; });
  /* B/(μ0 n I) no eixo; a = 1 (lado do quadrado ou raio do círculo) */
  function f(z,L){ var p=z+L/2, m=z-L/2;
    if(shape==='sq') return 2/PI*(Math.atan(p/Math.sqrt(p*p+0.5))-Math.atan(m/Math.sqrt(m*m+0.5)));
    return 0.5*(p/Math.sqrt(p*p+1)-m/Math.sqrt(m*m+1)); }
  F3.loop(root,function(){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var L=S.L, Zm=Math.max(L/2+3,L*0.7), z=S.z*Zm;
    F3.setOut(root,'L',F3.fmt(L,1)); F3.setOut(root,'z','z = '+F3.fmt(z,2)+' a');
    var box={x:46,y:132,w:w-66,h:h-162}, P=F3.plot(ctx,box,[-Zm,Zm],[0,1.12],c,{xl:'z (em unidades de a)',yl:'B / (μ0 n I)'});
    /* bobina desenhada com a mesma escala horizontal */
    var x0=P.X(-L/2), x1=P.X(L/2), ac=Math.min(38,(P.X(1)-P.X(0))), yc=66;
    ctx.strokeStyle=c.muted; ctx.setLineDash([3,4]); ctx.beginPath(); ctx.moveTo(box.x,yc); ctx.lineTo(box.x+box.w,yc); ctx.stroke(); ctx.setLineDash([]);
    var nT=clamp(Math.round(L*3),1,70);
    for(var i=0;i<nT;i++){ var xx=nT===1?(x0+x1)/2:x0+(x1-x0)*i/(nT-1); ctx.strokeStyle=c.E; ctx.lineWidth=2;
      if(shape==='sq'){ ctx.beginPath(); ctx.moveTo(xx-4,yc-ac); ctx.lineTo(xx+4,yc-ac); ctx.lineTo(xx+4,yc+ac); ctx.lineTo(xx-4,yc+ac); ctx.closePath(); ctx.stroke(); }
      else { ctx.beginPath(); ctx.ellipse(xx,yc,5,ac,0,0,7); ctx.stroke(); } }
    F3.label(ctx,shape==='sq'?'seção quadrada, lado a':'seção circular, raio a',box.x,14,c.muted,12);
    /* campo médio dentro: seta */
    F3.arrow(ctx,(x0+x1)/2-20,yc,(x0+x1)/2+20,yc,c.B,3,9);
    /* curvas */
    ctx.strokeStyle=c.grid; ctx.setLineDash([5,4]); [1,0.5].forEach(function(v){ ctx.beginPath(); ctx.moveTo(box.x,P.Y(v)); ctx.lineTo(box.x+box.w,P.Y(v)); ctx.stroke(); }); ctx.setLineDash([]);
    F3.label(ctx,'1',box.x-6,P.Y(1),c.muted,11,'right'); F3.label(ctx,'1/2',box.x-6,P.Y(0.5),c.muted,11,'right');
    [x0,x1].forEach(function(xx){ ctx.strokeStyle=c.E; ctx.globalAlpha=0.35; ctx.beginPath(); ctx.moveTo(xx,box.y); ctx.lineTo(xx,box.y+box.h); ctx.stroke(); ctx.globalAlpha=1; });
    F3.curve(ctx,function(zz){return f(zz,L);},-Zm,Zm,P,c.B,2.5);
    var fz=f(z,L); ctx.fillStyle=c.S; ctx.beginPath(); ctx.arc(P.X(z),P.Y(fz),5.5,0,7); ctx.fill();
    ctx.strokeStyle=c.S; ctx.setLineDash([3,3]); ctx.beginPath(); ctx.moveTo(P.X(z),yc); ctx.lineTo(P.X(z),P.Y(fz)); ctx.stroke(); ctx.setLineDash([]);
    /* fração do comprimento com B > 95% */
    var cnt=0, tot=0; for(var q=0;q<=200;q++){ var zz=-L/2+L*q/200; tot++; if(f(zz,L)>0.95) cnt++; }
    out.innerHTML='<span>B(z) = <b class="hl">'+F3.fmt(fz,3)+'</b> μ0nI</span><span>centro: <b>'+F3.fmt(f(0,L),3)+'</b></span><span>boca (z = L/2): <b>'+F3.fmt(f(L/2,L),3)+'</b></span><span>trecho com B &gt; 0,95 μ0nI: <b>'+F3.fmt(100*cnt/tot,0)+' %</b> do comprimento</span>';
  });
})();

/* ================= 5. Dois fios paralelos ================= */
(function(){
  var root=$('w-fios'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), S={}, out=root.querySelector('.w-readout');
  bindN(root,S);
  root.querySelector('[data-act=flip2]').addEventListener('click',function(){ F3.setRange(root,'I2',-S.I2,S); });
  F3.loop(root,function(dt,t){
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var sc=Math.min(w*0.72/12,30), cx=w/2, cy=h/2, d=S.d, I1=S.I1, I2=S.I2;
    var wx=[cx-d/2*sc, cx+d/2*sc], Is=[I1,I2];
    F3.setOut(root,'I1',(I1>0?'+':'')+I1+' A'); F3.setOut(root,'I2',(I2>0?'+':'')+I2+' A'); F3.setOut(root,'d',F3.fmt(d,1)+' cm');
    var Bref=MU0*6/(2*PI*0.03), step=26;
    for(var gx=step/2; gx<w; gx+=step) for(var gy=step/2; gy<h; gy+=step){
      var bx=0, by=0, near=false;
      for(var k=0;k<2;k++){ var rx=(gx-wx[k])/sc/100, ry=-(gy-cy)/sc/100, r2=rx*rx+ry*ry; if(r2<(14/sc/100)*(14/sc/100)) near=true; var kk=MU0*Is[k]/(2*PI*r2); bx+=-ry*kk; by+=rx*kk; }
      if(near) continue; var B=Math.hypot(bx,by); if(B<1e-12) continue;
      var ux=bx/B, uy=-by/B, a=clamp(0.15+0.85*Math.sqrt(B/Bref),0.15,1), Ln=9;
      ctx.globalAlpha=a; F3.arrow(ctx,gx-ux*Ln,gy-uy*Ln,gx+ux*Ln,gy+uy*Ln,c.B,1.4,5); ctx.globalAlpha=1;
    }
    for(var j=0;j<2;j++){ ctx.fillStyle=c.bg; ctx.beginPath(); ctx.arc(wx[j],cy,14,0,7); ctx.fill();
      if(Is[j]>0) F3.dotOut(ctx,wx[j],cy,12,c.E); else if(Is[j]<0) F3.crossIn(ctx,wx[j],cy,12,c.E); else { ctx.strokeStyle=c.muted; ctx.beginPath(); ctx.arc(wx[j],cy,12,0,7); ctx.stroke(); }
      F3.label(ctx,j?'I₂':'I₁',wx[j],cy+30,c.E,13,'center','600'); }
    var FL=MU0*I1*I2/(2*PI*d/100), Fmax=MU0*100/(2*PI*0.02);
    if(FL!==0){ var Ln2=18+70*Math.sqrt(Math.abs(FL)/Fmax), dir=FL>0?1:-1; /* + = atração */
      F3.arrow(ctx,wx[0]-dir*0+(dir>0?16:-16),cy-40,wx[0]+(dir>0?16+Ln2:-16-Ln2),cy-40,c.S,3.5,11);
      F3.arrow(ctx,wx[1]+(dir>0?-16:16),cy-40,wx[1]+(dir>0?-16-Ln2:16+Ln2),cy-40,c.S,3.5,11);
      F3.label(ctx,'F',wx[0],cy-58,c.S,14,'center','600'); F3.label(ctx,'F',wx[1],cy-58,c.S,14,'center','600'); }
    var mid=(I2-I1)*MU0/(2*PI*d/200); /* campo no ponto médio (componente y) */
    var tipo=FL>0?'ATRAÇÃO (mesmo sentido)':(FL<0?'REPULSÃO (sentidos opostos)':'sem força');
    out.innerHTML='<span>F/L = μ0 I₁I₂/(2πd) = <b>'+F3.sci(Math.abs(FL),2)+' N/m</b></span><span><b class="hl">'+tipo+'</b></span><span>|B| no meio dos fios: <b>'+uT(Math.abs(mid))+'</b></span>';
  });
})();

})();
