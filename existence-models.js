/* Continuidade dá a garantia; estreitar um intervalo sozinho não a fornece. */
window.ExistenceModels=(()=>{
 const f=(mode,x)=>mode===0?x*x*x-2:mode===1?x*x*x-x:x<0?-1:1;
 function bracket(mode,n){let a=mode===0?1:mode===1?-2:-1,b=mode===0?2:mode===1?2:1,steps=0;for(let i=0;i<n;i++){const m=(a+b)/2,v=f(mode,m);steps++;if(v===0){a=b=m;break;}if((f(mode,a)<0)===(v<0))a=m;else b=m;}return{a,b,mid:(a+b)/2,residual:f(mode,(a+b)/2),steps};}
 function extrema(n,p){const plus=1/(Math.PI/2+2*Math.PI*n),minus=1/(3*Math.PI/2+2*Math.PI*n);return{plus,minus,positive:plus**p,negative:-(minus**p)};}
 function createModels({plot,sample,fmt}){return{
  intermediateGuarantee:{label:'Compare existência com uma aproximação numérica',controls:[['mode','Função: 0 cúbica, 1 três raízes, 2 salto',0,2,1,0],['n','Reduções solicitadas',0,8,1,2]],render:({mode,n})=>{
   const r=bracket(mode,n),xmin=mode===0?1:mode===1?-2:-1,xmax=mode===0?2:mode===1?2:1,ymin=mode===0?-1.5:mode===1?-6.5:-1.5,ymax=mode===0?6.5:mode===1?6.5:1.5;
   const curves=mode===2?[{data:[[-1,-1],[0,-1]]},{data:[[0,1],[1,1]]}]:[{data:sample(x=>f(mode,x),xmin,xmax)}];
   let graph=plot([...curves,{data:[[r.a,ymin],[r.a,ymax]],style:'reference'},{data:[[r.b,ymin],[r.b,ymax]],style:'reference'}],{xmin,xmax,ymin,ymax},[[r.mid,r.residual]]);
   if(mode===2){const Y=y=>18+(ymax-y)/(ymax-ymin)*242;graph=graph.replace('</svg>',`<circle cx="340" cy="${Y(-1)}" r="6" fill="var(--paper)" stroke="var(--blue)" stroke-width="2"/><circle cx="340" cy="${Y(1)}" r="4" fill="var(--blue)"/></svg>`);}
   return{graph,
    report:`Intervalo [${fmt(r.a)}; ${fmt(r.b)}]; largura=${fmt(r.b-r.a)}; candidato=${fmt(r.mid)}; f(candidato)=${fmt(r.residual)}. ${mode===2?'Há mudança de sinal, mas a função tem salto e não possui zero.':mode===1?'Função contínua com três raízes: −1, 0 e 1. Localizar uma não prova unicidade.':'Continuidade garante uma raiz; crescimento estrito nesta cúbica dá unicidade.'}`,
    note:'Modelos 0: x³−2 em [1;2]; 1: x³−x em [−2;2]; 2: −1 para x<0 e 1 para x≥0. Eixo x: entrada; y: função. Verticais: intervalo após as reduções; ponto: candidato ou zero encontrado. TVI garante existência sob continuidade, não erro numérico automaticamente. O salto não tem raiz: resíduo ±1 persiste quando a largura diminui.'};
  }},
  squeezeEnvelope:{label:'Controle a oscilação por uma envoltória',controls:[['p','Potência da envoltória p: 0, 1 ou 2',0,2,1,2],['n','Índice das sequências n',1,20,1,2]],render:({p,n})=>{
   const r=extrema(n,p),bound=x=>Math.abs(x)**p,curve=x=>bound(x)*Math.sin(1/x),height=p===0?1.2:1.2*.25**p;
   return{graph:plot([{data:sample(curve,-.25,-.002,900)},{data:sample(curve,.002,.25,900)},{data:sample(bound,-.25,.25),style:'reference'},{data:sample(x=>-bound(x),-.25,.25),style:'reference'}],{xmin:-.25,xmax:.25,ymin:-height,ymax:height},[[r.plus,r.positive],[r.minus,r.negative]]),
    report:`xₙ⁺≈${fmt(r.plus)}; f(xₙ⁺)≈${fmt(r.positive)}; xₙ⁻≈${fmt(r.minus)}; f(xₙ⁻)≈${fmt(r.negative)}. ${p===0?'As sequências tendem a zero, mas as saídas são +1 e −1: não existe limite.':'As cotas ±|x|ᵖ tendem a zero; o limite é 0 pelo Confronto.'}`,
    note:'f(x)=|x|ᵖ sin(1/x), x≠0, em radianos. Pontilhadas: cotas; azul: amostra finita da curva. Sequências: xₙ⁺=1/(π/2+2πn), xₙ⁻=1/(3π/2+2πn). Pontos têm seno +1/−1 na identidade analítica. O desenho omite |x|<0,002 e não mostra todas as oscilações. Para p=0, cotas constantes não concluem um limite; para p>0, a desigualdade universal fornece a garantia.'};
  }}
 };}
 return{createModels,bracket,extrema};
})();
