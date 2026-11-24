/* Composição escalar com fator interno explícito; diferenças finitas não provam a regra. */
window.ChainModels=(()=>{
 const value=(x,b)=>(1+b*x)**3;
 const derivative=(x,b)=>3*b*(1+b*x)**2;
 function createModels({plot,sample,fmt}){return{chainSensitivity:{label:'Separe os fatores e compare com a reta tangente',controls:[['x','Ponto x',-1,2,.1,1],['b','Taxa interna b',-2,2,.5,2],['h','Passo de diferença central',.001,.301,.01,.101]],render:({x,b,h})=>{
  const u=1+b*x,outer=3*u*u,total=derivative(x,b),difference=(value(x+h,b)-value(x-h,b))/(2*h),curve=sample(t=>value(t,b),-1,2),tangent=sample(t=>value(x,b)+total*(t-x),-1,2),ys=[...curve,...tangent].map(p=>p[1]);let lo=Math.min(...ys),hi=Math.max(...ys),pad=Math.max(1,.1*(hi-lo));
  return{graph:plot([{data:curve},{data:tangent,style:'reference'}],{xmin:-1,xmax:2,ymin:lo-pad,ymax:hi+pad},[[x,value(x,b)]]),report:`u=1+bx=${fmt(u)}. Taxa externa 3u²=${fmt(outer)}; taxa interna b=${fmt(b)}; produto dy/dx=${fmt(total)}. Diferença central=${fmt(difference)}; erro absoluto=${Math.abs(difference-total).toExponential(3)}.`,note:'Eixo horizontal x; vertical y=(1+bx)³, sem unidades especificadas. Pontilhado: reta tangente no ponto selecionado. A escala vertical se adapta à função e à reta; compare números, não só inclinação na tela. Para este polinômio, diferença central = derivada + b³h² em aritmética exata. b=0 dá função constante. Diferença finita confere um exemplo, não prova a regra nem remove erro de arredondamento.'};
 }}};}return{value,derivative,createModels};
})();
