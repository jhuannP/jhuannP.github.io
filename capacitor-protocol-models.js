/* Capacitor linear: estados sintéticos e balanços quase estáticos. */
window.CapacitorProtocolModels=(()=>{
 function compare(C0,V0,kappa){
  if(![C0,V0,kappa].every(Number.isFinite)||C0<=0||kappa<1)throw new RangeError('C0 positivo, tensão finita e kappa>=1');
  const Q0=C0*V0,U0=C0*V0*V0/2,C=C0*kappa;
  function state(mode){
   const V=mode==='charge'?V0/kappa:V0,Q=mode==='charge'?Q0:C*V,U=Q*V/2;
   const rawBattery=mode==='charge'?0:-V0*(Q-Q0),batteryEnergy=rawBattery===0?0:rawBattery,deltaU=U-U0;
   const r={C,Q,V,U,Q0,U0,deltaU,batteryEnergy,externalWork:deltaU+batteryEnergy};
   if(!Object.values(r).every(Number.isFinite))throw new RangeError('Escala numérica fora do intervalo finito');
   return r;
  }
  return{charge:state('charge'),voltage:state('voltage')};
 }
 function createModels({fmt}){return{
  capacitorProtocols:{label:'Compare carga fixa e tensão mantida por bateria',controls:[['C0','Capacitância inicial C₀ (μF)',1,4,1,2],['V0','Tensão inicial V₀ (V)',-4,4,1,3],['kappa','Fator dielétrico κ',1,4,0.5,3]],render:({C0,V0,kappa})=>{
   const r=compare(C0,V0,kappa);
   const row=(label,s)=>'<tr><td>'+label+'</td><td>'+fmt(s.Q)+'</td><td>'+fmt(s.V)+'</td><td>'+fmt(s.U)+'</td></tr>';
   const energy=(label,s)=>'<tr><td>'+label+'</td><td>'+fmt(s.deltaU)+'</td><td>'+fmt(s.batteryEnergy)+'</td><td>'+fmt(s.externalWork)+'</td></tr>';
   const graph='<div class="capacitor-protocol-panel"><table class="truth-table"><caption>Estados finais: C = '+fmt(r.charge.C)+' μF nos dois casos</caption><thead><tr><th>Controle</th><th>Q (μC)</th><th>V (V)</th><th>Ucap (μJ)</th></tr></thead><tbody>'+row('Q fixo',r.charge)+row('V fixo',r.voltage)+'</tbody></table><table class="truth-table"><caption>Balanços em μJ: ΔUcap + ΔEbat = Wext</caption><thead><tr><th>Controle</th><th>ΔUcap</th><th>ΔEbat</th><th>Wext</th></tr></thead><tbody>'+energy('Q fixo',r.charge)+energy('V fixo',r.voltage)+'</tbody></table></div>';
   return{graph,report:'Estado inicial comum: Q₀='+fmt(r.charge.Q0)+' μC e U₀='+fmt(r.charge.U0)+' μJ. '+(V0===0?'Sem carga inicial: as energias e os trabalhos são zero.':kappa===1?'κ=1: nenhuma alteração de capacitância ou energia.':'Aumento de κ: o agente pode retirar trabalho mecânico nos dois protocolos; a bateria participa apenas no controle de V.'),note:'Dielétrico ideal linear, preenchimento final completo, geometria fixa e processo quase estático sem perdas ou deformação. Wext positivo fornece trabalho ao conjunto; negativo corresponde a trabalho retirado. ΔEbat é a variação da energia da bateria ideal, não energia armazenada no capacitor. Não calcula força, corrente transitória, trajetória de inserção ou aquecimento.'};
  }}
 }}return{compare,createModels};
})();
