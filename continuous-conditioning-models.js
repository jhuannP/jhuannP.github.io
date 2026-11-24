/* Suporte triangular sintético; faixas positivas e uma versão condicional interior. */
window.ContinuousConditioningModels=(()=>{
 function model(iy=5,ih=20,ia=5){
  if(!Number.isInteger(iy)||iy<1||iy>9||!Number.isInteger(ih)||ih<1||ih>20||!Number.isInteger(ia)||ia<0||ia>10)throw new RangeError('Centro 1–9, meia largura 1–20 e limiar 0–10 inteiros.');
  // Todas as massas são razões de inteiros em unidades de 1/100.
  const y=10*iy,h=ih,a=10*ia,lo=Math.max(0,y-h),hi=Math.min(100,y+h),mass=hi*hi-lo*lo;
  function bandCDF(x){const t=Math.max(0,Math.min(100,x*100));return(t<=lo?2*t*(hi-lo):t>=hi?mass:2*t*hi-t*t-lo*lo)/mass;}
  function pointCDF(x){return Math.max(0,Math.min(1,x*100/y));}
  const joint=a<=lo?2*a*(hi-lo):a>=hi?mass:2*a*hi-a*a-lo*lo;
  return{y:y/100,h:h/100,a:a/100,lower:lo/100,upper:hi/100,band_mass:mass/10000,joint:joint/10000,point:pointCDF(a/100),band:joint/mass,difference:joint/mass-pointCDF(a/100),marginal:2*a/100-(a/100)**2,bandCDF,pointCDF};
 }
 function createModels({plot,sample,fmt}){return{continuousConditioning:{label:'Uma faixa tem massa; um ponto, não',controls:[['iy','Centro y — em décimos',1,9,1,5],['ih','Meia largura h — em centésimos',1,20,1,20],['ia','Limiar a — em décimos',0,10,1,5]],render:({iy,ih,ia})=>{
  const s=model(iy,ih,ia);
  let graph=plot([{data:sample(s.bandCDF,0,1,200),style:'reference'},{data:[[0,0],[s.y,1],[1,1]]}],{xmin:0,xmax:1,ymin:0,ymax:1,xlabel:'x',ylabel:'F(x)'},[[s.a,s.point]]);
  graph=graph.replace('<svg ', '<svg class="continuous-conditioning-plot" ').replace('viewBox="0 0 640 300"','viewBox="-20 0 680 310"');
  return{graph:'<p>Horizontal: limiar x, de 0 a 1. Acumuladas de X: azul contínuo, versão dado Y=y; preto tracejado, dado Y na faixa. Altura é P(X≤x | informação), entre 0 e 1.</p>'+graph,report:`y=${fmt(s.y)}; h=${fmt(s.h)}; faixa [${fmt(s.lower)}; ${fmt(s.upper)}]; a=${fmt(s.a)}. Massa da faixa=${fmt(s.band_mass)}. P(X≤a | faixa)=${fmt(s.band)}; versão P(X≤a | Y=y)=${fmt(s.point)}; diferença=${fmt(s.difference)}. Sem informar Y: P(X≤a)=${fmt(s.marginal)}.`,note:'Modelo f(x,y)=2 em 0<x<y<1, sem unidades físicas. Centro e limiar em décimos; h em centésimos. Faixa recortada a [0,1]. Diminua h para comparar com a versão escolhida, válida para y interior. P(Y=y)=0: a curva azul vem da densidade condicional, não de uma divisão de probabilidades de eventos nulos. Não há amostragem nem dados de pesquisa.'};
 }}};}
 return{model,createModels};
})();
