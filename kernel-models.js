/* Uma família de entradas diferentes com imagem idêntica. */
window.KernelModels=(()=>{
 const apply=v=>[v[0]+v[1],2*(v[0]+v[1])];
 function createModels({plot,fmt}){return{kernelDirections:{label:'Mova a entrada numa direção do núcleo',controls:[['x','Primeira coordenada da entrada',-3,3,.5,3],['y','Segunda coordenada da entrada',-3,3,.5,2],['t','Parâmetro na direção (1,−1)',-2,2,.5,1]],render:({x,y,t})=>{
  const u=[x,y],shifted=[x+t,y-t],output=apply(u),second=apply(shifted);
  return{graph:`<p>Entradas em R²</p>${plot([{data:[[0,0],u]},{data:[[0,0],shifted],style:'secondary'},{data:[[-6,6],[6,-6]],style:'reference'}],{xmin:-6,xmax:6,ymin:-6,ymax:6,equalScale:true},[u,shifted])}<p>Saída em R²</p>${plot([{data:[[0,0],output]}],{xmin:-13,xmax:13,ymin:-13,ymax:13,equalScale:true},[output])}`,report:`u=(${fmt(x)}, ${fmt(y)}); u+t(1,−1)=(${fmt(shifted[0])}, ${fmt(shifted[1])}). Ambas as imagens: (${fmt(output[0])}, ${fmt(output[1])}); diferença=(${fmt(second[0]-output[0])}, ${fmt(second[1]-output[1])}).`,note:'Matriz fixa A=[[1,1],[2,2]], sem unidades físicas. Primeiro gráfico: entrada azul, entrada deslocada azul clara e núcleo x+y=0 pontilhado. Segundo: a única saída comum. Cada gráfico usa a mesma escala nos seus dois eixos; escalas entre gráficos são diferentes e declaradas pelos números. t=0 coincide as entradas; u no núcleo produz saída zero. A identidade A(u+tz)=Au vem de Az=0, não da aparência do desenho.'};
 }}};}return{apply,createModels};
})();
