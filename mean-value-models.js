/* Secante e tangente, com contraexemplo em que falta diferenciabilidade. */
window.MeanValueModels=(()=>{
 function analyze(kind,a,b){const f=x=>kind===0?x*x:Math.abs(x),slope=(f(b)-f(a))/(b-a);return{f,slope,c:kind===0?(a+b)/2:null};}
 function createModels({plot,sample,fmt}){return{meanValueHypotheses:{label:'Compare a secante e verifique as hipóteses',controls:[['kind','Função: 0 → x² · 1 → |x|',0,1,1,0],['a','Fronteira esquerda a',-2,-.5,.1,-1],['b','Fronteira direita b',.5,2,.1,1]],render:({kind,a,b})=>{
  const r=analyze(kind,a,b),curve=sample(r.f,a,b);if(kind===1){curve.push([0,0]);curve.sort((p,q)=>p[0]-q[0]);}
  const series=[{data:curve},{data:[[a,r.f(a)],[b,r.f(b)]],style:'reference'}],points=[[a,r.f(a)],[b,r.f(b)]];
  if(kind===0){series.push({data:sample(x=>r.f(r.c)+r.slope*(x-r.c),a,b),style:'secondary'});points.push([r.c,r.f(r.c)]);}
  const ys=series.flatMap(s=>s.data.map(p=>p[1])),lo=Math.min(...ys),hi=Math.max(...ys),pad=Math.max(.5,.1*(hi-lo));
  return{graph:plot(series,{xmin:a,xmax:b,ymin:lo-pad,ymax:hi+pad},points),report:`Intervalo [${fmt(a)}, ${fmt(b)}]; secante m=${fmt(r.slope)}. ${kind===0?`Hipóteses satisfeitas. c=${fmt(r.c)}; f′(c)=2c=${fmt(2*r.c)}. Tangente e secante são paralelas.`:'|x| é contínua, mas não diferenciável em zero. Não há c com derivada igual a m: fora de zero, a derivada é −1 ou 1; m está entre esses valores.'}`,note:'Eixo horizontal x; vertical f(x). Azul: função; pontilhado: secante dos extremos. Na parábola, azul claro: tangente no c encontrado. No módulo, o intervalo sempre atravessa zero e o teorema não se aplica. Os controles evitam intervalo degenerado; c é ponto médio apenas nesta parábola, não uma regra geral do Teorema do Valor Médio. Desenho finito ilustra exemplos, não substitui a demonstração.'};
 }}};}return{analyze,createModels};
})();
