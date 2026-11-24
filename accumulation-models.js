/* Integral de t: fronteiras lineares, composta e duas fronteiras móveis. */
window.AccumulationModels=(()=>{
 function boundaries(kind,x){return kind===0?[0,x,0,1]:kind===1?[0,x*x,0,2*x]:[x,2*x,1,2];}
 const value=(kind,x)=>{const [a,b]=boundaries(kind,x);return(b*b-a*a)/2;};
 const rate=(kind,x)=>{const [a,b,da,db]=boundaries(kind,x);return b*db-a*da;};
 function createModels({plot,sample,fmt}){return{movingIntegral:{label:'Compare acumulação e taxa com fronteiras móveis',controls:[['kind','Fronteiras: 0 → [0,x] · 1 → [0,x²] · 2 → [x,2x]',0,2,1,1],['x','Ponto x',-2,2,.1,1]],render:({kind,x})=>{
  const [a,b,da,db]=boundaries(kind,x),A=value(kind,x),d=rate(kind,x),curve=sample(t=>value(kind,t),-2,2),tangent=sample(t=>A+d*(t-x),-2,2),ys=[...curve,...tangent].map(p=>p[1]),lo=Math.min(...ys),hi=Math.max(...ys),pad=Math.max(1,.1*(hi-lo));
  return{graph:plot([{data:curve},{data:tangent,style:'reference'}],{xmin:-2,xmax:2,ymin:lo-pad,ymax:hi+pad},[[x,A]]),report:`Fronteiras: a=${fmt(a)}, b=${fmt(b)}. Acumulação A=${fmt(A)}. Taxa da fronteira superior=${fmt(db)}; inferior=${fmt(da)}. A′=f(b)b′−f(a)a′=${fmt(b*db)}−(${fmt(a*da)})=${fmt(d)}.`,note:'Eixo horizontal x; vertical acumulação ∫_a(x)^b(x) t dt. Azul: acumulação; pontilhado: tangente no x selecionado. O integrando é f(t)=t. Valores da acumulação e sua taxa são coisas diferentes; a taxa pode ser negativa mesmo com acumulação positiva. A integral é orientada: inverter fronteiras inverte o sinal. Escala vertical se adapta às curvas. Modelo polinomial contínuo, sem dados de pesquisa.'};
 }}};}return{boundaries,value,rate,createModels};
})();
