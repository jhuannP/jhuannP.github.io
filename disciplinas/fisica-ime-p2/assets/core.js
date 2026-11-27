/* Física III para IME · utilitários compartilhados (window.F3)
   Carregue este arquivo ANTES dos scripts de cada capítulo (sem defer/async em ordem diferente). */
(function(){
"use strict";
var F3 = window.F3 = {};
F3.reduce = !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
F3.MU0 = 4*Math.PI*1e-7; F3.EPS0 = 8.854e-12; F3.C = 3e8;

/* leitura de cores do tema (sempre ler a cada quadro: o tema pode mudar) */
F3.css = function(n){ return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); };
F3.W = function(){ var c=F3.css; return {bg:c('--w-bg'),ink:c('--w-ink'),muted:c('--w-muted'),grid:c('--w-grid'),E:c('--w-E'),B:c('--w-B'),S:c('--w-S'),ok:c('--w-ok'),neg:c('--w-neg')}; };

/* números em pt-BR */
F3.fmt = function(x,d){ if(d===undefined)d=2; if(!isFinite(x)) return '∞'; return x.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d}); };
F3.sup = function(n){ var m={'-':'⁻','0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}; return String(n).split('').map(function(c){return m[c]||c;}).join(''); };
F3.sci = function(x,d){ if(x===0) return '0'; var e=Math.floor(Math.log10(Math.abs(x))); var m=x/Math.pow(10,e); if(Math.abs(m)>=9.995){m/=10;e++;} return F3.fmt(m,d===undefined?2:d)+'×10'+F3.sup(e); };

/* Canvas com DPR e redimensionamento. Use st.w / st.h (px CSS) e st.ctx. */
F3.Stage = function(canvas){
  var self=this; this.c=canvas; this.ctx=canvas.getContext('2d'); this.h0=+canvas.getAttribute('height')||300;
  this.fit=function(){ var dpr=Math.min(window.devicePixelRatio||1,2), w=canvas.clientWidth||600;
    self.w=w; self.h=self.h0; canvas.width=Math.round(w*dpr); canvas.height=Math.round(self.h*dpr); canvas.style.height=self.h+'px'; self.ctx.setTransform(dpr,0,0,dpr,0,0); };
  this.fit(); if(window.ResizeObserver) new ResizeObserver(function(){ self.fit(); }).observe(canvas);
};

/* primitivas de desenho */
F3.arrow = function(ctx,x1,y1,x2,y2,col,w,head){
  head=head||9; var dx=x2-x1,dy=y2-y1,L=Math.hypot(dx,dy); if(L<1) return; if(head>L*0.8) head=L*0.8;
  ctx.strokeStyle=col; ctx.fillStyle=col; ctx.lineWidth=w||2.5; ctx.lineCap='round';
  var ux=dx/L,uy=dy/L,hx=x2-ux*head*0.9,hy=y2-uy*head*0.9;
  ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(hx,hy); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x2,y2); ctx.lineTo(x2-ux*head-uy*head*0.55,y2-uy*head+ux*head*0.55); ctx.lineTo(x2-ux*head+uy*head*0.55,y2-uy*head-ux*head*0.55); ctx.closePath(); ctx.fill();
};
F3.dotOut = function(ctx,x,y,r,col){ ctx.strokeStyle=col; ctx.lineWidth=1.6; ctx.beginPath(); ctx.arc(x,y,r,0,7); ctx.stroke(); ctx.fillStyle=col; ctx.beginPath(); ctx.arc(x,y,r*0.32,0,7); ctx.fill(); };
F3.crossIn = function(ctx,x,y,r,col){ ctx.strokeStyle=col; ctx.lineWidth=1.6; ctx.beginPath(); ctx.arc(x,y,r,0,7); ctx.stroke(); var a=r*0.6; ctx.beginPath(); ctx.moveTo(x-a,y-a); ctx.lineTo(x+a,y+a); ctx.moveTo(x+a,y-a); ctx.lineTo(x-a,y+a); ctx.stroke(); };
F3.label = function(ctx,t,x,y,col,size,align,weight){ ctx.fillStyle=col; ctx.font=(weight||'')+' '+(size||13)+'px "IBM Plex Sans",sans-serif'; ctx.textAlign=align||'left'; ctx.textBaseline='middle'; ctx.fillText(t,x,y); };
/* eixos de gráfico simples: devolve funções X(v), Y(v) */
F3.plot = function(ctx,box,xr,yr,c,opts){
  opts=opts||{}; var X=function(v){return box.x+(v-xr[0])/(xr[1]-xr[0])*box.w;}, Y=function(v){return box.y+box.h-(v-yr[0])/(yr[1]-yr[0])*box.h;};
  ctx.strokeStyle=c.grid; ctx.lineWidth=1; ctx.strokeRect(box.x,box.y,box.w,box.h);
  if(yr[0]<0&&yr[1]>0){ ctx.beginPath(); ctx.moveTo(box.x,Y(0)); ctx.lineTo(box.x+box.w,Y(0)); ctx.stroke(); }
  if(opts.xl) F3.label(ctx,opts.xl,box.x+box.w,box.y+box.h+13,c.muted,11,'right');
  if(opts.yl) F3.label(ctx,opts.yl,box.x+4,box.y-10,c.muted,11,'left');
  return {X:X,Y:Y};
};
F3.curve = function(ctx,f,x0,x1,P,col,w,dash,n){ n=n||200; ctx.strokeStyle=col; ctx.lineWidth=w||2; ctx.setLineDash(dash||[]); ctx.beginPath(); for(var i=0;i<=n;i++){ var x=x0+(x1-x0)*i/n, y=f(x); if(!isFinite(y)) continue; var px=P.X(x),py=P.Y(y); i?ctx.lineTo(px,py):ctx.moveTo(px,py);} ctx.stroke(); ctx.setLineDash([]); };

F3.visible = function(el){ var r=el.getBoundingClientRect(); return r.bottom>-60 && r.top<innerHeight+60; };

/* Liga <input type=range data-k="..."> ao objeto state; onchange(k) opcional */
F3.bind = function(root,state,onchange){
  root.querySelectorAll('input[type=range][data-k],select[data-k]').forEach(function(inp){ var k=inp.dataset.k; state[k]=isNaN(+inp.value)?inp.value:+inp.value;
    inp.addEventListener('input',function(){ state[k]=isNaN(+inp.value)?inp.value:+inp.value; if(onchange) onchange(k); }); });
};
F3.setOut = function(root,k,txt){ var o=root.querySelector('output[data-o="'+k+'"]'); if(o) o.textContent=txt; };
F3.setRange = function(root,k,v,state){ var i=root.querySelector('input[data-k="'+k+'"]'); if(i){ i.value=v; if(state) state[k]=+v; } };

/* Laço de animação que só roda quando o widget está visível. draw(dt, t) */
F3.loop = function(root,draw){
  var last=performance.now(), t=0;
  function frame(now){ var dt=Math.min(0.05,(now-last)/1000); last=now;
    if(F3.visible(root)){ t+=F3.reduce?0:dt; draw(F3.reduce?0:dt,t); }
    requestAnimationFrame(frame); }
  requestAnimationFrame(frame);
};

/* tema claro/escuro */
document.addEventListener('DOMContentLoaded',function(){
  var tg=document.querySelector('.theme-toggle');
  if(tg) tg.addEventListener('click',function(){ var root=document.documentElement, cur=root.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'), nx=cur==='dark'?'light':'dark'; root.dataset.theme=nx; try{localStorage.setItem('fis3-tema',nx);}catch(e){} });

  /* quizzes: <div class="quiz"><p class="quiz-q">..</p><div class="quiz-opts"><button data-ok>..</button><button>..</button></div><p class="quiz-fb">explicação</p></div> */
  document.querySelectorAll('.quiz').forEach(function(q){
    var fb=q.querySelector('.quiz-fb');
    q.querySelectorAll('.quiz-opts button').forEach(function(b){ b.addEventListener('click',function(){
      q.querySelectorAll('.quiz-opts button').forEach(function(o){ o.classList.remove('right','wrong'); if(o.hasAttribute('data-ok')) o.classList.add('right'); });
      if(!b.hasAttribute('data-ok')) b.classList.add('wrong');
      if(fb) fb.classList.add('show'); }); });
  });

  /* sumário lateral: destaca a seção visível */
  var links=[].slice.call(document.querySelectorAll('.toc a[href^="#"]'));
  if(links.length){ var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'));});
    var upd=function(){ var y=scrollY+140,on=-1; secs.forEach(function(s,i){ if(s&&s.getBoundingClientRect().top+scrollY<=y) on=i; }); links.forEach(function(a,i){ a.classList.toggle('on',i===on); }); };
    addEventListener('scroll',upd,{passive:true}); upd(); }
});

/* KaTeX: \( \) inline e $$ $$ display */
window.addEventListener('load',function(){ if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false}); });
})();
