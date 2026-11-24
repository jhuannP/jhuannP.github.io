/* Cortes exatos de duas superfícies quadráticas; não reconstitui a superfície inteira. */
window.TangentPlaneModels=(()=>{
 function plane(kind,a,b,h,k){
  if(![0,1].includes(kind)||![a,b,h,k].every(Number.isFinite))throw new RangeError('Função 0/1 e coordenadas finitas');
  const sign=kind===0?1:-1,base=a*a+2*sign*b*b,g=[2*a,4*sign*b],linear=base+g[0]*h+g[1]*k,exact=(a+h)**2+2*sign*(b+k)**2,remainder=h*h+2*sign*k*k,rho=Math.hypot(h,k);
  return{base,g,normal:[g[0]===0?0:-g[0],g[1]===0?0:-g[1],1],linear,exact,remainder,rho,scaled:rho?Math.abs(remainder)/rho:null,bound:2*rho*rho};
 }
 function model(kind=0,point=0,angle=45,refinements=2){
  if(![0,1].includes(kind)||![0,1,2].includes(point)||!Number.isFinite(angle)||angle<0||angle>360||!Number.isInteger(refinements)||refinements<0||refinements>6)throw new RangeError('Parâmetros fora do domínio');
  const[a,b]=[[1,1],[0,0],[-1,1]][point],u=({0:[1,0],90:[0,1],180:[-1,0],270:[0,-1],360:[1,0]})[angle]||[Math.cos(angle*Math.PI/180),Math.sin(angle*Math.PI/180)],rho=2**(-refinements);
  return{...plane(kind,a,b,rho*u[0],rho*u[1]),a,b,u};
 }
 function createModels({plot,fmt}){return{tangentPlane:{label:'Compare a superfície e o plano num corte',controls:[['kind','Superfície: 0 convexa · 1 sela',0,1,1,0],['point','Ponto: 0 (1,1) · 1 (0,0) · 2 (−1,1)',0,2,1,0],['angle','Direção do corte: graus desde +x',0,360,15,45],['refinements','Refinamentos n: distância ρ=2⁻ⁿ',0,6,1,2]],render:({kind,point,angle,refinements})=>{
  const s=model(kind,point,angle,refinements),curve=[],line=[];
  for(let i=0;i<=160;i++){const t=-1+i/80,v=plane(kind,s.a,s.b,t*s.u[0],t*s.u[1]);curve.push([t,v.exact]);line.push([t,v.linear])}
  const vals=[...curve,...line].map(p=>p[1]),lo=Math.floor(Math.min(...vals)-.5),hi=Math.ceil(Math.max(...vals)+.5);
  const graph=plot([{data:curve},{data:line,style:'reference'},{data:[[s.rho,s.linear],[s.rho,s.exact]],style:'continuum-reference'}],{xmin:-1,xmax:1,ymin:lo,ymax:hi},[[0,s.base],[s.rho,s.exact]]).replace('<svg ','<svg class="tangent-plane-scene" ');
  return{graph:`<p><strong>${kind===0?'f=x²+2y²':'f=x²−2y²'}</strong>. Corte (x,y)=p+t·u. Horizontal: t; vertical: altura z. Azul: superfície no corte. Preto tracejado: plano no mesmo corte. Segmento vertical: diferença no deslocamento escolhido.</p>`+graph+`<table class="truth-table"><caption>Valores no ponto p+ρu</caption><thead><tr><th>f exato</th><th>Plano L</th><th>R=f−L</th></tr></thead><tbody><tr><td>${fmt(s.exact)}</td><td>${fmt(s.linear)}</td><td>${fmt(s.remainder)}</td></tr></tbody></table>`,report:`p=(${s.a}, ${s.b}); f(p)=${fmt(s.base)}; ∇f=(${s.g.join(', ')}). Normal ao gráfico N=(${s.normal.map(v=>fmt(v)).join(', ')}). ρ=${fmt(s.rho)}; |R|/ρ=${fmt(s.scaled)}; limite 2ρ²=${fmt(s.bound)}. ${point===1?'Na origem, o plano é horizontal e sua normal é (0,0,1), mesmo com gradiente bidimensional zero.':''}`,note:'Coordenadas adimensionais; u unitário na métrica euclidiana. É um corte vertical, não uma vista de toda a superfície. Mudar a direção pode inverter o sinal do erro na sela. Reduzir ρ pela metade divide R por 4 e |R|/ρ por 2, salvo resto já zero. A prova usa R=h²±2k² e |R|≤2ρ²; alguns cortes ou amostras não provam diferenciabilidade em geral. Escala vertical automática: compare números ao trocar parâmetros. Diferenças menores que um pixel continuam na tabela. Material original em rascunho.'};
 }}}}
 return{plane,model,createModels};
})();
