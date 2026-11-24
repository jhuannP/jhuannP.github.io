/* Duas funções selecionadas; não classifica diferenciabilidade de funções arbitrárias. */
window.GradientModels=(()=>{
 function value(kind,x,y){if(kind===0)return x*x+2*y*y;if(kind!==1)throw new RangeError('Função 0/1');const r2=x*x+y*y;return r2?x*x*x/r2:0}
 function partials(kind,x,y){if(kind===0)return[2*x,4*y];if(kind!==1)throw new RangeError('Função 0/1');if(x===0)return y?[0,0]:[1,0];const r2=x*x+y*y;return r2?[x*x*(x*x+3*y*y)/(r2*r2),-2*x*x*x*y/(r2*r2)]:[1,0]}
 function direction(angle){const special={0:[1,0],90:[0,1],180:[-1,0],270:[0,-1],360:[1,0]};return special[angle]||[Math.cos(angle*Math.PI/180),Math.sin(angle*Math.PI/180)]}
 function model(kind=0,x=1,y=2,angle=45,refinements=2){
  if(![0,1].includes(kind)||![x,y,angle].every(Number.isFinite)||Math.abs(x)>2||Math.abs(y)>2||angle<0||angle>360||!Number.isInteger(refinements)||refinements<0||refinements>6)throw new RangeError('Parâmetros fora do domínio didático');
  const h=2**(-refinements),u=direction(angle),g=partials(kind,x,y),norm=Math.hypot(...g),differentiable=!(kind===1&&x===0&&y===0),dot=g[0]*u[0]+g[1]*u[1],derivative=differentiable?dot:u[0]**3,end=[x+h*u[0],y+h*u[1]],base=value(kind,x,y),final=value(kind,...end),secant=(final-base)/h,remainder=final-base-h*dot;
  return{kind,x,y,angle,refinements,h,u,g,norm,base,end,final,dot,derivative,secant,remainder,scaled_remainder:Math.abs(remainder)/h,differentiable,normal_available:differentiable&&norm>0,max_growth:differentiable?norm:null};
 }
 function levelCurves(kind,level){
  if(kind===0){if(level<0)return[];if(level===0)return[[[0,0]]];return[Array.from({length:181},(_,i)=>{const t=2*Math.PI*i/180;return[Math.sqrt(level)*Math.cos(t),Math.sqrt(level/2)*Math.sin(t)]})]}
  if(level===0)return[[[0,-4],[0,4]]];
  const branch=sign=>Array.from({length:181},(_,i)=>{const x=level+(Math.sign(level)*4-level)*i/180;return[x,sign*Math.abs(x)*Math.sqrt(Math.max(0,x/level-1))]}).filter(([x,y])=>Math.abs(x)<=4&&Math.abs(y)<=4);
  return[branch(1),branch(-1)];
 }
 function createModels({plot,fmt}){return{gradient:{label:'Compare a taxa direcional e a aproximação linear',controls:[['kind','Função: 0 quadrática · 1 contraexemplo',0,1,1,0],['x','Ponto inicial: x',-2,2,.1,1],['y','Ponto inicial: y',-2,2,.1,2],['angle','Direção unitária: ângulo em graus desde +x',0,360,15,45],['refinements','Refinamentos n: passo h=2⁻ⁿ',0,6,1,2]],render:({kind,x,y,angle,refinements})=>{
  const s=model(kind,x,y,angle,refinements),levels=kind===0?[.5,1,2,4,8,12]:[-2,-1,-.5,0,.5,1,2];
  const curves=levels.flatMap(k=>levelCurves(kind,k).map(data=>({data,style:'gradient-level'})));
  curves.push(...levelCurves(kind,s.base).map(data=>({data,style:'continuum-reference'})));
  if(s.norm)curves.push({data:[[x,y],[x+s.g[0]/s.norm,y+s.g[1]/s.norm]],style:s.differentiable?'':'candidate-partials'});
  curves.push({data:[[x,y],s.end],style:'reference'});
  const graph=plot(curves,{xmin:-4,xmax:4,ymin:-4,ymax:4,equalScale:true},[[x,y],s.end]).replace('<svg ','<svg class="gradient-scene" ');
  const table=`<table class="truth-table gradient-table"><caption>Taxas no ponto inicial; secante usa o passo h=${fmt(s.h)}</caption><thead><tr><th>Dᵤf</th><th>g·u</th><th>Secante</th></tr></thead><tbody><tr><td>${fmt(s.derivative)}</td><td>${fmt(s.dot)}</td><td>${fmt(s.secant)}</td></tr></tbody></table>`;
  return{graph:`<p><strong>${kind===0?'f=x²+2y²':'f=x³/(x²+y²), f(0,0)=0'}</strong>. Horizontal x; vertical y, mesma escala. Cinza: níveis de referência; preto contínuo: nível do ponto. Azul: direção de g=(fₓ,fᵧ), normalizada para comprimento 1 ${s.differentiable?'quando g≠0':'e tracejada por ser apenas candidata ao diferencial na origem'}. Preto tracejado: deslocamento h·u. Pontos: início e fim do deslocamento. As curvas não mostram altura em 3D.</p>`+graph+table,
  report:`f(p)=${fmt(s.base)}; g=(${fmt(s.g[0])}, ${fmt(s.g[1])}); ||g||=${fmt(s.norm)}. u=(${fmt(s.u[0])}, ${fmt(s.u[1])}); h=${fmt(s.h)}. |f(p+hu)−f(p)−h(g·u)|/h=${fmt(s.scaled_remainder)}. ${!s.differentiable?'Na origem do contraexemplo, todas as derivadas direcionais existem, mas Dᵤf=uₓ³ e não g·u em geral. Reduzir h nesta direção não corrige a falha do candidato linear.':s.norm?`Neste ponto diferenciável, a taxa máxima unitária é ${fmt(s.norm)}; o gradiente é normal ao nível regular.`:(kind===0?'Gradiente zero: todas as taxas de primeira ordem são zero, mas a função não é constante. O nível f=0 da quadrática é só a origem, sem curva regular.':'Gradiente zero: todas as taxas de primeira ordem são zero. Aqui o nível zero é a reta x=0; não se pode aplicar o critério de nível regular baseado em g≠0.')}`,
  note:'Coordenadas adimensionais com métrica euclidiana. Para a quadrática, a identidade exata dá resto h²(uₓ²+2uᵧ²), logo resto/h→0. O contraexemplo é contínuo e não diferenciável apenas na origem, por demonstração analítica; fora dela é suave. O programa não infere diferenciabilidade por amostragem. Zero de uma derivada direcional ou um único teste com resto zero não prova constância ou diferenciabilidade. Gradiente nulo não define uma direção normalizada. Material original em rascunho, sem certificação de domínio pessoal.'};
 }}}}
 return{value,partials,direction,model,levelCurves,createModels};
})();
