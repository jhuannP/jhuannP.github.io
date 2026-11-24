/* Modelo passivo efetivo, sem potencial de ação ou cálculo de Goldman. */
window.PassiveMembraneModels=(()=>{
 function model(gk,gna,I,t){
  if(![gk,gna,I,t].every(Number.isFinite)||gk<0||gna<0||gk+gna<=0||t<0)throw new RangeError('Condutâncias não negativas com soma positiva; t>=0');
  const C=100,V0=-80,EK=-90,ENa=60,G=gk+gna,Vinf=(gk*EK+gna*ENa+I)/G,tau=C/G;
  const factor=Math.exp(-t/tau),V=Vinf+(V0-Vinf)*factor,dV=-(V0-Vinf)*factor/tau;
  const r={Vinf,tau,G,V,dV,IK:gk*(V-EK),INa:gna*(V-ENa)};
  for(const key of Object.keys(r))if(r[key]===0)r[key]=0;
  if(!Object.values(r).every(Number.isFinite))throw new RangeError('Escala fora do intervalo numérico');
  return r;
 }
 function createModels({plot,sample,fmt}){return{
  passiveMembrane:{label:'Compare voltagem, corrente total e correntes iônicas',controls:[['gk','Condutância de K⁺ (nS)',1,8,1,4],['gna','Condutância de Na⁺ (nS)',0,3,0.5,1],['I','Corrente aplicada para dentro (pA)',-100,100,25,0],['t','Tempo de leitura (ms)',0,100,5,20]],render:({gk,gna,I,t})=>{
   const r=model(gk,gna,I,t),zero=n=>n===0?0:n,ssK=zero(gk*(r.Vinf+90)),ssNa=zero(gna*(r.Vinf-60)),Icap=100*r.dV;
   const ymin=Math.floor(Math.min(-80,r.Vinf)/20)*20-10,ymax=Math.ceil(Math.max(-80,r.Vinf)/20)*20+10;
   const chart=plot([{data:sample(s=>model(gk,gna,I,s).V,0,100)},{data:[[0,r.Vinf],[100,r.Vinf]],style:'reference'}],{xmin:0,xmax:100,ymin,ymax},[[t,r.V]]).replace('<svg ','<svg class="passive-membrane-scene" ').replace('viewBox="0 0 640 300"','viewBox="-30 0 690 310"');
   const graph='<div class="passive-membrane-panel"><p>Horizontal: t (ms). Vertical: V (mV), escala adaptativa. Azul: V(t); tracejado: valor estacionário. Ponto no tempo escolhido.</p>'+chart+'<table class="truth-table"><caption>Correntes iônicas positivas para fora; em pA</caption><thead><tr><th>Instante</th><th>I_K</th><th>I_Na</th><th>Soma</th></tr></thead><tbody><tr><td>t='+fmt(t)+' ms</td><td>'+fmt(r.IK)+'</td><td>'+fmt(r.INa)+'</td><td>'+fmt(r.IK+r.INa)+'</td></tr><tr><td>Estacionário</td><td>'+fmt(ssK)+'</td><td>'+fmt(ssNa)+'</td><td>'+fmt(I)+'</td></tr></tbody></table></div>';
   return{graph,report:'Em t='+fmt(t)+' ms, V='+fmt(r.V)+' mV; Icap='+fmt(Math.abs(Icap)<1e-12?0:Icap)+' pA. V∞='+fmt(r.Vinf)+' mV e τ='+fmt(r.tau)+' ms. Balanço: Iaplicada = I_K + I_Na + Icap. '+(I===0?'No estado estacionário, soma iônica zero não exige cada corrente zero.':'No estado estacionário, a soma iônica iguala a corrente aplicada.'),note:'C=100 pF, V(0)=−80 mV, E_K=−90 mV e E_Na=+60 mV, todos parâmetros didáticos. Condutâncias constantes, reservatórios iônicos mantidos. Não é Goldman, não inclui limiar, disparo, bombas dinâmicas ou previsão de neurônio real.'};
  }}
 }}return{model,createModels};
})();
