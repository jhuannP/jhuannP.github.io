/* Relações adimensionais, separadas dos exemplos aplicados. */
window.ProportionModels=(()=>{
 function model(x=2){
  if(!Number.isFinite(x)||x<1||x>6||!Number.isInteger(2*x))throw new RangeError('x de 1 a 6 em passos de 1/2.');
  const rows={direta:[4*x,8*x],inversa:[24/x,12/x],taxa_fixa:[6+4*x,6+8*x]};
  return Object.fromEntries(Object.entries(rows).map(([name,[y,doubled]])=>[name,{y,doubled,ratio:y/x,product:x*y,doubling:doubled/y}]));
 }
 function createModels({plot,fmt}){return{proportionCompare:{label:'Razão constante, produto constante ou nenhum dos dois?',controls:[['x','Entrada x',1,6,.5,2]],render:({x})=>{
  const s=model(x),line=fn=>Array.from({length:121},(_,i)=>{const t=i/20;return[t,fn(t)];}),inverse=Array.from({length:106},(_,i)=>{const t=.75+i/20;return[t,24/t];});
  const graph=plot([{data:line(t=>4*t)},{data:inverse,style:'reference'},{data:line(t=>6+4*t),style:'secondary'}],{xmin:0,xmax:6,ymin:0,ymax:32},Object.values(s).map(v=>[x,v.y]))+
   '<p class="caption">Eixos x e y adimensionais. Azul contínuo: y=4x; preto tracejado: y=24/x; pontilhado: y=6+4x. Os pontos marcam a entrada selecionada. No modelo inverso, x=0 é indefinido e o trecho 0&lt;x&lt;0,75 fica acima da janela. A tabela avalia também 2x, que pode estar fora da janela horizontal.</p>'+
   `<table class="truth-table"><caption>O que muda ao dobrar x=${fmt(x)} para ${fmt(2*x)}?</caption><thead><tr><th>Modelo</th><th>y(x)</th><th>y(2x)</th><th>Fator</th></tr></thead><tbody><tr><th>Direto: 4x</th><td>${fmt(s.direta.y)}</td><td>${fmt(s.direta.doubled)}</td><td>2</td></tr><tr><th>Inverso: 24/x</th><td>${fmt(s.inversa.y)}</td><td>${fmt(s.inversa.doubled)}</td><td>1/2</td></tr><tr><th>Taxa fixa: 6+4x</th><td>${fmt(s.taxa_fixa.y)}</td><td>${fmt(s.taxa_fixa.doubled)}</td><td>${fmt(s.taxa_fixa.doubling)}</td></tr></tbody></table>`;
  return{graph:`<div class="proportion-compare-panel">${graph}</div>`,report:`No direto, y/x=${fmt(s.direta.ratio)}. No inverso, xy=${fmt(s.inversa.product)}. Com taxa fixa, y/x=${fmt(s.taxa_fixa.ratio)} nesta entrada: mudar x altera essa razão, apesar de a taxa de variação ser 4.`,note:'Três relações sintéticas para comparação; não ajuste de dados nem oferta de preço. A entrada do controle fica de 1 a 6 em meios; isso não é o domínio completo das fórmulas. Domínios físicos e unidades devem ser definidos em cada aplicação. Python é exploração opcional.'};
 }}};}
 return{model,createModels};
})();
