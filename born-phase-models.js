/* Superposição contínua de dois modos; parâmetros sintéticos, sem tempo. */
window.BornPhaseModels=(()=>{
 function model(k=0){if(!Number.isInteger(k)||k<0||k>8)throw new RangeError('k inteiro0..8');const c=Math.cos(k*Math.PI/4);return{k,left:.5+4*c/(3*Math.PI),right:.5-4*c/(3*Math.PI),mean_u:.5-16*c/(9*Math.PI*Math.PI),norm:1};}
 function density(u,k=0){model(k);if(!Number.isFinite(u)||u<0||u>1)throw new RangeError('u em[0,1]');const a=Math.sin(Math.PI*u),b=Math.sin(2*Math.PI*u),phi=k*Math.PI/4;return(a+Math.cos(phi)*b)**2+(Math.sin(phi)*b)**2;}
 function createModels({plot,fmt}){return{bornPhase:{label:'Fase relativa: redistribuir probabilidade',controls:[['k','Fase relativa φ = kπ/4 (k de 0 a 8)',0,8,1,0]],render:({k})=>{
 const r=model(k),xs=Array.from({length:201},(_,i)=>i/200);
 return{graph:'<div class="born-phase-plot">'+plot([{data:xs.map(u=>[u,density(u,k)])},{data:xs.map(u=>[u,Math.sin(Math.PI*u)**2+Math.sin(2*Math.PI*u)**2]),style:'reference'}],{xmin:0,xmax:1,ymin:0,ymax:3.2})+'</div><p class="caption">Horizontal: u=x/L, de 0 a 1. Vertical: Lρ(x), adimensional. Azul: superposição com fase escolhida. Tracejado preto: mistura com 50% em cada modo. Probabilidades abaixo são integrais, não alturas. Curvas coincidentes não demonstram estados iguais.</p>',report:`φ=${k}π/4; P(x<L/2)=${fmt(r.left)}; P(x>L/2)=${fmt(r.right)}; média ⟨x⟩/L=${fmt(r.mean_u)}. Integral total=1 em todos os casos. Na mistura: metade esquerda=0,5 e média=0,5.`,note:'Um instante e dois modos ortonormais em [0,L], pesos iguais. O controle compara preparações; não é um relógio ou simulação da evolução livre. Em φ=π/2 e 3π/2, as densidades de posição coincidem com a mistura; a superposição continua sendo um estado puro. Sem amostragem de detecções, instrumento ou dados reais.'};
 }}};}
 return{model,density,createModels};
})();
