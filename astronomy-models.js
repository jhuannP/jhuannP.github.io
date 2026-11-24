/* Geometria e inversão didática; não lê catálogos nem faz inferência astrométrica. */
window.AstronomyModels=(()=>{
 function parallaxBand(p,sigma){
  if(!Number.isFinite(p)||!Number.isFinite(sigma)||p<=0||sigma<0)throw new RangeError('p positivo e sigma não negativo, finitos');
  return {distance:1000/p,relative:sigma/p,linear:1000*sigma/p**2,lower:1000/(p+sigma),upper:p>sigma?1000/(p-sigma):null};
 }
 function photometry(m,M,A=0){
  if(![m,M,A].every(Number.isFinite)||A<0)throw new RangeError('Dados finitos e extinção não negativa');
  const modulus=m-M-A;return{modulus,distance:10**((modulus+5)/5),naive:10**((m-M+5)/5),bias:10**(A/5),transmission:10**(-.4*A)};
 }
 function diskFraction(x){
  if(!Number.isFinite(x)||x<0)throw new RangeError('x finito e não negativo');
  if(x<.01){let term=x*x/2,total=term;for(let k=1;k<=12;k++){term*=-x*(k+1)/(k*(k+2));total+=term;}return total;}
  return -Math.expm1(-x)-x*Math.exp(-x);
 }
 function diskHalfRatio(){let lo=0,hi=10;for(let i=0;i<70;i++){const mid=(lo+hi)/2;if(diskFraction(mid)<.5)lo=mid;else hi=mid;}return(lo+hi)/2;}
 function exponentialDisk(I0,h,R){
  if(![I0,h,R].every(Number.isFinite)||I0<=0||h<=0||R<0)throw new RangeError('I0,h positivos; R não negativo, finitos');
  const x=R/h,f=diskFraction(x),total=2*Math.PI*I0*h*h;return{x,local:I0*Math.exp(-x),fraction:f,total,enclosed:total*f,missed:1-f,half_radius:h*diskHalfRatio()};
 }
 function createModels({plot,sample,fmt}){return {exponentialDisk:{label:'Brilho local e luz acumulada são curvas diferentes',controls:[['I0','Brilho central I₀ (uL/kpc²)',.5,5,.5,2],['h','Escala h (kpc)',.5,4,.5,3],['R','Abertura R (kpc)',0,16,.5,6]],render:({I0,h,R})=>{
  const q=exponentialDisk(I0,h,R);return{graph:plot([{data:sample(r=>diskFraction(r/h),0,16)},{data:sample(r=>Math.exp(-r/h),0,16),style:'reference'}],{xmin:0,xmax:16,ymin:0,ymax:1.05},[[R,q.fraction],[R,q.local/I0]]),report:`R/h=${fmt(q.x)}. Brilho local/I₀=${fmt(q.local/I0)}. Luz dentro de R: ${fmt(100*q.fraction)}%; fora: ${fmt(100*q.missed)}%. L(<R)=${fmt(q.enclosed)} uL; L∞=${fmt(q.total)} uL. Raio de meia-luz=${fmt(q.half_radius)} kpc.`,note:'Horizontal: raio físico em kpc; vertical: razões adimensionais. Azul: L(<R)/L∞; pontilhado: I(R)/I₀. Pontos indicam a abertura escolhida nas duas curvas. Alterar I₀ muda luminosidades, mas não essas razões. Disco circular visto de frente, exponencial infinito e sem poeira; uL é unidade sintética de luminosidade na banda. Não é imagem observada, ajuste, perfil de massa ou prova de matéria escura.'};
 }},photometricDistance:{label:'O mesmo brilho, diferentes hipóteses de extinção',controls:[['m','Magnitude aparente m',8,20,.2,15],['M','Magnitude absoluta M',-5,10,.2,4],['A','Extinção A (mag)',0,3,.1,1]],render:({m,M,A})=>{
  const q=photometry(m,M,A);return{graph:plot([{data:sample(a=>photometry(m,M,a).distance,0,3)},{data:[[0,q.naive],[3,q.naive]],style:'reference'}],{xmin:0,xmax:3,ymin:0,ymax:Math.ceil(q.naive*1.1/10**Math.floor(Math.log10(q.naive)))*10**Math.floor(Math.log10(q.naive))},[[A,q.distance]]),report:`Módulo corrigido: ${fmt(q.modulus)} mag. Distância: ${fmt(q.distance)} pc. Ignorando A: ${fmt(q.naive)} pc, fator ${fmt(q.bias)} maior. Transmissão da tela: ${fmt(100*q.transmission)}%.`,note:'Horizontal: extinção assumida A, em magnitudes; vertical: distância em pc. Curva azul: m e M fixos, variando a hipótese de A; ponto: escolha atual. Pontilhado: inferência com A=0. Não é perfil de poeira em função da distância. Mesma banda/sistema, M conhecido e tela sintética; sem catálogo, ajuste de M/A ou cosmologia. Brilho observado sozinho não identifica uma distância.'};
 }},parallaxDistance:{label:'Paralaxe: inverter uma faixa muda sua forma',controls:[['p','Paralaxe p (mas)',.2,20,.2,10],['sigma','Escala σ (mas)',0,5,.1,2]],render:({p,sigma})=>{
  const q=parallaxBand(p,sigma),xmin=Math.min(p*.5,p>sigma?(p-sigma)*.8:p*.1),xmax=p+Math.max(2*sigma,p*.5),points=[[p,q.distance],[p+sigma,q.lower],...(q.upper===null?[]:[[p-sigma,q.upper]])];
  return {graph:plot([{data:sample(x=>1000/x,xmin,xmax)},{data:[[xmin,q.distance],[xmax,q.distance]],style:'reference'}],{xmin,xmax,ymin:0,ymax:1000/xmin*1.05},points),report:`Inversão central: ${fmt(q.distance)} pc. Escala linear local: ${fmt(q.linear)} pc; σ/p=${fmt(q.relative)}. Imagem da faixa positiva: de ${fmt(q.lower)} pc ${q.upper===null?'sem limite superior finito':`até ${fmt(q.upper)} pc`}. ${q.relative>=.2?'A não linearidade já merece atenção; não há limiar universal de validade.':'Aproximação linear é local; não substitui análise dos dados.'}`,note:'Horizontal: paralaxe positiva em mas; vertical: distância em pc. Curva azul: 1000/p; pontos: centro e extremos positivos de p±σ. Reta pontilhada: distância central. Faixa invertida não é intervalo de confiança ou posterior por si só. Quando cruza zero, apenas a parte positiva é representada e não há teto finito; o gráfico mostra somente um trecho. Valores sintéticos, sem ajuste de catálogo, ponto zero, movimento próprio ou seleção de amostra.'};
 }}};}
 return {parallaxBand,photometry,diskFraction,diskHalfRatio,exponentialDisk,createModels};
})();
