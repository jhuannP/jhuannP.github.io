/* Três leis aparentes,mesma concentração e velocidade iniciais;sem dados experimentais. */
window.RateOrderModels=(()=>{
 function model(u=1){
  if(typeof u!=='number'||!Number.isFinite(u)||u<0||u>3)throw new RangeError('u em[0,3].');
  const concentrations=[Math.max(1-u,0),Math.exp(-u),1/(1+u)];
  return{concentrations,products:concentrations.map(a=>1-a),rates:[u<1?1:u===1?null:0,concentrations[1],concentrations[2]**2],half_times:[.5,Math.log(2),1]};
 }
 function createModels({plot,sample,fmt}){return{rateOrders:{label:'Mesma velocidade inicial: as concentrações evoluem iguais?',controls:[['u','Tempo normalizado u=v₀t/[A]₀',0,3,.25,1]],render:({u})=>{
  const z=model(u),graph=`<div class="rate-order-panel">`+plot([{data:sample(t=>Math.max(1-t,0),0,3,120),style:'reference'},{data:sample(t=>Math.exp(-t),0,3,120)},{data:sample(t=>1/(1+t),0,3,120),style:'secondary'}],{xmin:0,xmax:3,ymin:0,ymax:1},z.concentrations.map(a=>[u,a]))+`<p class="caption">Horizontal: u=v₀t/[A]₀. Vertical: a=[A]/[A]₀. Preto tracejado: ordem 0, com término de consumo em u=1. Azul contínuo: ordem 1. Azul pontilhado: ordem 2. Todos começam em a=1 com inclinação −1; as curvas são modelos diferentes, não ajustes aos mesmos dados.</p><table class="truth-table"><caption>Estado no tempo u=${fmt(u)} — valores normalizados</caption><thead><tr><th>Ordem</th><th>A/A₀</th><th>P/A₀</th><th>v/v₀</th></tr></thead><tbody>${z.concentrations.map((a,i)=>`<tr><th>${i}</th><td>${fmt(a)}</td><td>${fmt(z.products[i])}</td><td>${z.rates[i]===null?'não definida na junção':fmt(z.rates[i])}</td></tr>`).join('')}</tbody></table></div>`;
  return{graph,report:`Meias-vidas no eixo u: ordem 0 = 1/2; ordem 1 = ln2 ≈ ${fmt(Math.log(2))}; ordem 2 = 1. ${u===1?'Ordem 0: na quina, a derivada temporal não é única; os trechos têm taxas laterais 1 e 0.':u>1?'Ordem 0: estoque esgotado; consumo interrompido por hipótese adicional.':'As três taxas coincidem apenas inicialmente; depois dependem da lei escolhida.'}`,note:'Mistura fechada ideal A→P 1:1, volume e temperatura constantes, P inicial zero, sem reversão. v=−d[A]/dt; ordem não é deduzida da estequiometria. v₀ e [A]₀ são comuns, mas k₀,k₁,k₂ têm unidades distintas. Não é experimento ou inferência de mecanismo.'};
 }}};}
 return{model,createModels};
})();
