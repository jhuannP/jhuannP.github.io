/* Física III para IME · Resolução da prova
   w-crono: cronômetro de 90 min com fases sugeridas; placar do treino (quizzes de #treino). */
(function(){
"use strict";
var F3=window.F3; if(!F3) return;

function mmss(s){ s=Math.max(0,Math.round(s)); var m=Math.floor(s/60), r=s%60; return (m<10?'0':'')+m+':'+(r<10?'0':'')+r; }

/* ====================== cronômetro ====================== */
(function(){
  var root=document.getElementById('w-crono'); if(!root) return;
  var st=new F3.Stage(root.querySelector('canvas')), out=root.querySelector('.w-readout');
  var FASES=[{n:'Questão 1 · torque',m:25},{n:'Questão 2 · indução',m:35},{n:'Questão 3 · ondas',m:25},{n:'Revisão (checklist)',m:5}];
  var TOTAL=0, i; for(i=0;i<FASES.length;i++){ FASES[i].ini=TOTAL; TOTAL+=FASES[i].m*60; FASES[i].fim=TOTAL; }
  var running=false, acc=0, t0=0, lastFase=-1;
  var bGo=root.querySelector('[data-act=go]');
  function elapsed(){ return Math.min(TOTAL, acc+(running?(Date.now()-t0)/1000:0)); }
  bGo.onclick=function(){
    if(running){ acc=elapsed(); running=false; bGo.textContent='Continuar'; bGo.classList.remove('on'); }
    else { if(elapsed()>=TOTAL) acc=0; t0=Date.now(); running=true; bGo.textContent='Pausar'; bGo.classList.add('on'); }
  };
  root.querySelector('[data-act=reset]').onclick=function(){ running=false; acc=0; lastFase=-1; bGo.textContent='Iniciar'; bGo.classList.remove('on'); };
  root.querySelector('[data-act=skip]').onclick=function(){
    var e=elapsed(); for(var k=0;k<FASES.length;k++){ if(e<FASES[k].fim){ acc=FASES[k].fim; if(running) t0=Date.now(); break; } }
  };
  function faseDe(e){ for(var k=0;k<FASES.length;k++) if(e<FASES[k].fim) return k; return FASES.length-1; }

  /* desenha mesmo com reduced-motion (F3.loop chama draw com dt=0) */
  F3.loop(root,function(){
    var e=elapsed(); if(running && e>=TOTAL){ acc=TOTAL; running=false; bGo.textContent='Recomeçar'; bGo.classList.remove('on'); }
    var c=F3.W(), ctx=st.ctx, w=st.w, h=st.h; ctx.clearRect(0,0,w,h);
    var x0=16, x1=w-16, bw=x1-x0, yb=w>420?58:66, bh=24, X=function(s){ return x0+bw*s/TOTAL; };
    var cols=[c.E,c.B,c.S,c.ok], fz=faseDe(e);
    for(var k=0;k<FASES.length;k++){
      var a=X(FASES[k].ini), b=X(FASES[k].fim);
      ctx.globalAlpha=k===fz?0.95:0.35; ctx.fillStyle=cols[k]; ctx.fillRect(a+1,yb,b-a-2,bh); ctx.globalAlpha=1;
      if(b-a>70) F3.label(ctx,FASES[k].m+' min',(a+b)/2,yb+bh/2,c.bg,12,'center','600');
      if(b-a>90) F3.label(ctx,FASES[k].n,(a+b)/2,yb+bh+14,k===fz?c.ink:c.muted,11,'center');
    }
    /* marca de 60 min */
    var x60=X(3600); ctx.setLineDash([4,4]); ctx.strokeStyle=c.ink; ctx.lineWidth=1.2; ctx.beginPath(); ctx.moveTo(x60,yb-8); ctx.lineTo(x60,yb+bh+4); ctx.stroke(); ctx.setLineDash([]);
    F3.label(ctx,'60 min',x60,yb-14,c.muted,10,'center');
    /* cursor */
    var xc=X(e); ctx.fillStyle=c.ink; ctx.beginPath(); ctx.moveTo(xc,yb-2); ctx.lineTo(xc-6,yb-12); ctx.lineTo(xc+6,yb-12); ctx.closePath(); ctx.fill();
    ctx.fillRect(xc-1,yb,2,bh);
    F3.label(ctx,'restam '+mmss(TOTAL-e),x0,18,c.ink,20,'left','600');
    F3.label(ctx,'decorrido '+mmss(e),w>420?x1:x0,w>420?18:38,c.muted,12,w>420?'right':'left');

    var faseResta=FASES[fz].fim-e;
    if(fz!==lastFase || !running){
      lastFase=fz;
      out.innerHTML='<span>Fase: <b class="hl">'+FASES[fz].n+'</b></span><span>Restam nesta fase: <b>'+mmss(faseResta)+'</b></span><span>'+(e>=3600?'<b>Já pode sair (60 min).</b>':'Saída liberada em '+mmss(3600-e))+'</span>';
    } else {
      var spans=out.querySelectorAll('b'); if(spans[1]) spans[1].textContent=mmss(faseResta);
      var s3=out.querySelectorAll('span')[2]; if(s3) s3.innerHTML=e>=3600?'<b>Já pode sair (60 min).</b>':'Saída liberada em '+mmss(3600-e);
    }
  });
})();

/* ====================== placar do treino ====================== */
(function(){
  var sec=document.getElementById('treino'), box=document.getElementById('placar'); if(!sec||!box) return;
  var msg=box.querySelector('[data-placar]'), quizzes=[].slice.call(sec.querySelectorAll('.quiz')), N=quizzes.length;
  var resp=new Map(), tIni=0, timer=null;
  function upd(){
    var n=resp.size, ok=0; resp.forEach(function(v){ if(v) ok++; });
    var t=tIni?(Date.now()-tIni)/1000:0;
    if(!n){ msg.textContent='Responda às '+N+' perguntas abaixo. O relógio do treino começa na primeira resposta.'; return; }
    msg.textContent=n+' de '+N+' respondidas · '+ok+' acerto'+(ok===1?'':'s')+' · tempo '+mmss(t)+(n===N?' · fim! '+(ok>=N*0.8?'Ótimo, você está pronto.':'Releia os comentários das que errou.'):'');
    if(n===N && timer){ clearInterval(timer); timer=null; }
  }
  quizzes.forEach(function(q){
    q.querySelectorAll('.quiz-opts button').forEach(function(b){
      b.addEventListener('click',function(){
        if(resp.has(q)) return; /* conta só a primeira tentativa */
        if(!tIni){ tIni=Date.now(); timer=setInterval(upd,1000); }
        resp.set(q,b.hasAttribute('data-ok')); upd();
      });
    });
  });
  var z=box.querySelector('[data-act=zerar-treino]');
  if(z) z.addEventListener('click',function(){
    resp.clear(); tIni=0; if(timer){ clearInterval(timer); timer=null; }
    quizzes.forEach(function(q){ q.querySelectorAll('.quiz-opts button').forEach(function(o){ o.classList.remove('right','wrong'); }); var fb=q.querySelector('.quiz-fb'); if(fb) fb.classList.remove('show'); });
    upd();
  });
  upd();
})();

})();
