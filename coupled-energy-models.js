/* Termodinâmica de duas reações sintéticas, sem previsão cinética. */
window.CoupledEnergyModels=(()=>{
 function model(log_q=0){if(!Number.isInteger(log_q)||log_q< -3||log_q>3)throw new RangeError('log10 Q inteiro−3…3');const q=10**log_q,target=12+2.4942*Math.log(q);return{log_q,q,target,donor:-20,net:target-20,equilibrium_q:Math.exp(8/2.4942)};}
 function createModels({plot,fmt}){return{coupledEnergy:{label:'Acoplamento e composição: o sinal pode mudar',controls:[['log_q','log₁₀ Q da reação global',-3,3,1,0]],render:({log_q})=>{
  const r=model(log_q),xs=Array.from({length:121},(_,i)=>-3+i/20),net=xs.map(x=>[x,-8+2.4942*Math.LN10*x]),target=xs.map(x=>[x,12+2.4942*Math.LN10*x]);
  return{graph:'<div class="coupled-energy-plot">'+plot([{data:net},{data:target,style:'reference'},{data:[[-3,0],[3,0]],style:'secondary'}],{xmin:-3,xmax:3,ymin:-30,ymax:30},[[log_q,r.net]])+'</div>'+`<p class="caption">Horizontal: log₁₀ Q, adimensional. Vertical: ΔG em kJ/mol de reação como escrita. Azul: global A+D→B+E; tracejado preto: alvo A→B. Linha pontilhada: zero. Ponto azul: escolha atual. O gráfico compara composições, não mostra evolução temporal.</p>`,report:`Q=${fmt(r.q)}; alvo ΔG=${fmt(r.target)} kJ/mol; doadora ΔG=−20 kJ/mol; global ΔG=${fmt(r.net)} kJ/mol. Sentido direto global ${r.net<0?'termodinamicamente favorecido':'termodinamicamente desfavorecido'} nesta composição. Q de equilíbrio global≈${fmt(r.equilibrium_q)}.`,note:'Exemplo sintético, não valores do ATP. ΔG°alvo=+12, ΔG°doadora=−20 kJ/mol; T=300 K, R=0,008314 kJ/(mol K). Atividades aA=aD=aE=1, aB=Q; Qdoadora=1. Somar reações não demonstra mecanismo de acoplamento nem velocidade. Atividades variam entre casos; o painel não integra uma célula, via ou mistura fechada.'};
 }}};}
 return{model,createModels};
})();
