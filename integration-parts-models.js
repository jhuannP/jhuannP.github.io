/* Integral orientada, termo de fronteira e integral restante. */
window.IntegrationPartsModels=(()=>{
 function model(tenths=10){
  if(!Number.isInteger(tenths)||tenths< -20||tenths>20)throw new RangeError('Limite inteiro em décimos de -20 a 20.');
  const b=tenths/10,boundary=b*Math.exp(b),remainder=Math.expm1(b),integral=tenths?(b-1)*Math.exp(b)+1:0;
  return{b,boundary,remainder,integral};
 }
 function createModels({plot,fmt}){return{integrationParts:{label:'Fronteira menos integral restante',controls:[['tenths','Limite superior b — em décimos',-20,20,1,10]],render:({tenths})=>{
  const z=model(tenths),lo=z.b===0?-1:Math.min(0,z.b),hi=z.b===0?1:Math.max(0,z.b);
  const points=Array.from({length:121},(_,i)=>{const x=lo+(hi-lo)*i/120;return[x,x*Math.exp(x)];});
  const ymin=-.5,ymax=z.b<=0&&z.b!==0?.1:Math.ceil(Math.max(...points.map(p=>p[1])))+.5;
  const X=x=>58+(x-lo)/(hi-lo)*564,Y=y=>260-(y-ymin)/(ymax-ymin)*242;
  const area=z.b===0?'':`<polygon points="${X(lo)},${Y(0)} ${points.map(([x,y])=>`${X(x)},${Y(y)}`).join(' ')} ${X(hi)},${Y(0)}" fill="#1957d6" fill-opacity="0.14"/>`;
  let svg=plot([{data:points}],{xmin:lo,xmax:hi,ymin,ymax});svg=svg.replace('>',`>${area}`);
  const graph=svg+`<p class="caption">Horizontal: x; vertical: f(x)=x exp(x). Variáveis adimensionais. Escalas adaptadas ao limite selecionado; não compare áreas pelo tamanho na tela. O preenchimento destaca a região entre a curva e zero, sem codificar a orientação. Integral calculada de 0 para ${fmt(z.b)}. Com b=0, não há região; a janela mostra apenas a função.</p><table class="truth-table"><caption>Identidade por partes, sem omitir a fronteira</caption><tbody><tr><th>Limite b</th><td>${fmt(z.b)}</td></tr><tr><th>[x exp(x)] de 0 a b</th><td>${fmt(z.boundary)}</td></tr><tr><th>∫ exp(x) de 0 a b</th><td>${fmt(z.remainder)}</td></tr><tr><th>Integral original: diferença</th><td>${fmt(z.integral)}</td></tr></tbody></table>`;
  return{graph:`<div class="integration-parts-panel">${graph}</div>`,report:`I(b)=${fmt(z.integral)}. ${z.b<0?'O integrando é negativo entre b e zero, mas os limites estão invertidos: a integral de 0 a b é positiva.':z.b===0?'Limites iguais: integral zero.':'Integrando não negativo de zero a b: integral positiva.'} Subtraia a integral restante do termo de fronteira.`,note:'u=x e dv=exp(x)dx; du=dx e v=exp(x). I(b)=b exp(b)−(exp(b)−1)=(b−1)exp(b)+1. Não é uma igualdade entre os integrandos originais. O exemplo envolve funções suaves e intervalos finitos; integrais impróprias exigem limites adicionais. O painel não é um integrador simbólico geral.'};
 }}};}
 return{model,createModels};
})();
