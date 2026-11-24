/* Modelos sintéticos: normal e distribuição exata da média de Bernoullis. */
window.LimitModels=(()=>{
 const phi=z=>Math.exp(-z*z/2)/Math.sqrt(2*Math.PI);
 function normalCDF(z){
  if(!Number.isFinite(z)||Math.abs(z)>6)throw Error('z fora da faixa numérica deste modelo');
  const b=Math.abs(z),n=512,h=b/n;let sum=phi(0)+phi(b);
  for(let i=1;i<n;i++)sum+=(i%2?4:2)*phi(i*h);
  return .5+(z<0?-1:1)*h*sum/3;
 }
 function normalQuantile(prob){
  if(!Number.isFinite(prob)||prob<.5||prob>.999)throw Error('Probabilidade fora da faixa de inversão');
  let lo=0,hi=6;for(let i=0;i<48;i++){const mid=(lo+hi)/2;if(normalCDF(mid)<prob)lo=mid;else hi=mid;}return(lo+hi)/2;
 }
 function bernoulliMean(n,p){
  const masses=window.ProbabilityModels.binomial(n,p),sdCount=Math.sqrt(n*p*(1-p)),step=1/sdCount;
  const bars=masses.map((mass,k)=>({z:(k-n*p)/sdCount,mass,height:mass/step}));
  // Margens evitam excluir uma fronteira devido a representação binária dos controles.
  const tail=masses.reduce((sum,mass,k)=>sum+(Math.abs(k-n*p)>=n*.2-1e-12?mass:0),0);
  return{bars,step,se:Math.sqrt(p*(1-p)/n),variance:p*(1-p)/n,tail,bound:Math.min(1,p*(1-p)/(n*.2**2))};
 }
 function createModels({plot,sample,fmt}){return{
 normalCurve:{label:'Mude localização, escala e valor padronizado',controls:[['mu','Média μ',-3,3,.5,0],['sd','Desvio padrão σ',.25,3,.25,1],['z','Valor padronizado z',-3,3,.1,1]],render:({mu,sd,z})=>{
  const xmin=mu-4*sd,xmax=mu+4*sd,ymax=phi(0)/sd*1.2,cut=mu+z*sd;
  let graph=plot([{data:sample(x=>phi((x-mu)/sd)/sd,xmin,xmax)}],{xmin,xmax,ymin:0,ymax});
  const X=x=>58+(x-xmin)/(xmax-xmin)*564,Y=y=>18+(ymax-y)/ymax*242;
  const polygon=[[xmin,0],...sample(x=>phi((x-mu)/sd)/sd,xmin,cut,80),[cut,0]].map(([x,y])=>`${X(x)},${Y(y)}`).join(' ');
  graph=graph.replace(/(<svg[^>]*>)/,`$1<polygon points="${polygon}" fill="var(--blue)" opacity=".14"/>`);
  return{graph,report:`x=μ+σz=${fmt(cut)}; P(X≤x)=Φ(z)≈${fmt(normalCDF(z))}. Var(X)=σ²=${fmt(sd*sd)}.`,
   note:'Modelo normal declarado, não transformação de dados em gaussianos. Eixo x: valores de X; y: densidade. Janela de μ−4σ a μ+4σ; a área preenchida não inclui a cauda esquerda fora da janela, de cerca de 0,00003167. A acumulada exibida integra desde −∞ e usa Simpson composto com 512 subintervalos. Alterar σ muda largura e altura, mantendo a área total teórica 1.'};
 }},
 bernoulliLimit:{label:'Compare a média exata com a referência normal',controls:[['n','Número de observações iid',1,40,1,4],['p','Probabilidade de sucesso',.1,.9,.1,.5]],render:({n,p})=>{
  const r=bernoulliMean(n,p),xmin=Math.min(-4,r.bars[0].z-r.step/2),xmax=Math.max(4,r.bars.at(-1).z+r.step/2),ymax=Math.max(.45,...r.bars.map(b=>b.height))*1.2;
  const X=x=>58+(x-xmin)/(xmax-xmin)*564,Y=y=>18+(ymax-y)/ymax*242;
  const rectangles=r.bars.map(b=>`<rect x="${X(b.z-r.step/2)}" y="${Y(b.height)}" width="${r.step/(xmax-xmin)*564}" height="${Y(0)-Y(b.height)}" fill="var(--blue)" opacity=".24"/>`).join('');
  const graph=plot([{data:sample(phi,xmin,xmax,360)}],{xmin,xmax,ymin:0,ymax}).replace(/(<svg[^>]*>)/,`$1${rectangles}`);
  return{graph,report:`E[média]=${fmt(p)}; Var(média)=${fmt(r.variance)}; erro padrão=${fmt(r.se)}. P(|média−p|≥0,2)=${fmt(r.tail)}; limite de Chebyshev=${fmt(r.bound)}.`,
   note:'Binomial exata de n Bernoullis iid com p fixo. Eixo x: Z=√n(média−p)/√(p(1−p)). Barras: cada massa é espalhada em uma classe de largura 1/√(np(1−p)); área da barra é a massa. Curva: densidade normal padrão, referência aproximada em n finito. Z continua discreto. Não são trajetórias sorteadas nem prova do TCL. A cota pode ser pouco informativa; mais dados correlacionados exigem outra conta. A comparação da fronteira da cauda usa margem numérica 10⁻¹².'};
 }}}; }
 return{createModels,phi,normalCDF,normalQuantile,bernoulliMean};
})();
