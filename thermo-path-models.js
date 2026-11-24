/* Mesmo estado inicial e final, três caminhos; trabalho realizado pelo gás positivo. */
window.ThermoPathModels=(()=>{
 function model(ratio=2){
  if(!Number.isFinite(ratio)||ratio<.5||ratio>3||!Number.isInteger(2*ratio))throw new RangeError('Razão de 0,5 a 3 em meios.');
  return{ratio,v2:3*ratio,p2:100/ratio,isothermal:300*Math.log(ratio),pressure_first:300*(1-1/ratio),volume_first:300*(ratio-1),intermediate_pressure_first:300/ratio,intermediate_volume_first:300*ratio};
 }
 function createModels({plot,fmt}){return{thermoPaths:{label:'Mesmos estados, calor e trabalho diferentes',controls:[['ratio','Razão de volumes V₂/V₁',.5,3,.5,2]],render:({ratio})=>{
  const s=model(ratio),lo=Math.min(3,s.v2),hi=Math.max(3,s.v2),iso=ratio===1?[[3,100]]:Array.from({length:121},(_,i)=>{const v=lo+(hi-lo)*i/120;return[v,300/v];});
  const graph=plot([{data:iso},{data:[[3,100],[3,s.p2],[s.v2,s.p2]],style:'reference'},{data:[[3,100],[s.v2,100],[s.v2,s.p2]],style:'secondary'}],{xmin:0,xmax:9,ymin:0,ymax:200},[[3,100],[s.v2,s.p2]])+
  `<p class="caption">Horizontal: V em litros; vertical: p em kPa. Inicial I=(3 L,100 kPa); final F=(${fmt(s.v2)} L,${fmt(s.p2)} kPa). Azul: isotérmico; tracejado preto: mudar p a V fixo e depois V a p final; pontilhado: mudar V a p inicial e depois p a V final. Cada caminho vai de I para F. Os pontos são estados, não medidas.</p><table class="truth-table"><caption>Balanço entre os mesmos extremos: ΔU=0 J</caption><thead><tr><th>Caminho</th><th>W pelo gás (J)</th><th>Q ao gás (J)</th></tr></thead><tbody><tr><th>Isotérmico</th><td>${fmt(s.isothermal)}</td><td>${fmt(s.isothermal)}</td></tr><tr><th>Isocórico → isobárico</th><td>${fmt(s.pressure_first)}</td><td>${fmt(s.pressure_first)}</td></tr><tr><th>Isobárico → isocórico</th><td>${fmt(s.volume_first)}</td><td>${fmt(s.volume_first)}</td></tr></tbody></table>`;
  return{graph:`<div class="thermo-path-panel">${graph}</div>`,report:`T inicial e final:300 K; ΔU=0 J no gás ideal. ${ratio===1?'Os caminhos colapsam no mesmo estado; W=Q=0.':ratio>1?'Expansão: os três trabalhos e calores líquidos são positivos.':'Compressão: os três trabalhos e calores líquidos são negativos.'} Nos caminhos quebrados, T varia no meio: ${fmt(s.intermediate_pressure_first)} K na primeira sequência e ${fmt(s.intermediate_volume_first)} K na segunda.`,note:'Sistema fechado, quantidade fixa com nR=1 J/K. Processos quase estáticos sem atrito; só trabalho p dV, sem variação macroscópica de energia cinética/potencial. Q entra positivo e W pelo gás sai positivo:ΔU=Q−W. Os extremos têm mesmo T, mas não o mesmo V/p quando a razão difere de1; isso não é um ciclo. Não representa expansão livre, reservatórios reais ou duração.'};
 }}};}
 return{model,createModels};
})();
