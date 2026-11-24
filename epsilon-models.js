/* Uma escolha de delta justificada e outra sem garantia geral. */
window.EpsilonModels=(()=>{
 function experiment(epsilon,ratio,choice){const delta=choice===0?Math.min(1,epsilon/3):epsilon,x=1+ratio*delta,y=x*x;return{delta,x,y,error:Math.abs(y-1),inside:Math.abs(ratio)>0&&Math.abs(ratio)<1};}
 function createModels({plot,sample,fmt}){return{
  epsilonQuadratic:{label:'Compare uma garantia com uma escolha ingênua',controls:[['epsilon','Tolerância ε',.1,4,.1,.3],['ratio','Deslocamento como fração de δ',-1.5,1.5,.1,.5],['choice','Escolha de δ: 0 garantia, 1 ingênua',0,1,1,0]],render:({epsilon,ratio,choice})=>{
   const r=experiment(epsilon,ratio,choice),radius=Math.max(.5,1.6*r.delta),xmin=1-radius,xmax=1+radius,ymin=Math.min(0,1-epsilon)-.2,ymax=Math.max(xmin*xmin,xmax*xmax,1+epsilon)+.3;
   return{graph:plot([{data:sample(x=>x*x,xmin,xmax)},{data:[[xmin,1-epsilon],[xmax,1-epsilon]],style:'reference'},{data:[[xmin,1+epsilon],[xmax,1+epsilon]],style:'reference'},{data:[[1-r.delta,ymin],[1-r.delta,ymax]],style:'reference'},{data:[[1+r.delta,ymin],[1+r.delta,ymax]],style:'reference'}],{xmin,xmax,ymin,ymax},[[r.x,r.y]]),
    report:`δ=${fmt(r.delta)}; x=${fmt(r.x)}; |x−1|=${fmt(Math.abs(r.x-1))}; |x²−1|=${fmt(r.error)}; ε=${fmt(epsilon)}. ${!r.inside?'O ponto não satisfaz o entorno perfurado 0<|x−1|<δ.':r.error<epsilon?'O ponto selecionado satisfaz a tolerância de saída.':'Contraexemplo: o ponto está dentro do entorno, mas falha na tolerância de saída.'}`,
    note:'Azul: f(x)=x²; ponto: entrada selecionada. Horizontais: 1±ε; verticais: 1±δ. A escolha 0 usa δ=min(1,ε/3), cuja garantia vem de |x+1|<3 quando |x−1|<1. A escolha 1 usa δ=ε, sem garantia geral. Um ponto que passa não prova a condição universal. O gráfico muda de escala conforme δ.'};
  }}
 };}
 return{createModels,experiment};
})();
