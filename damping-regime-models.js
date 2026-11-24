/* m=1 kg,k=4 N/m,x0=1 m,v0=0: três regimes do mesmo PVI. */
window.DampingRegimeModels=(()=>{
 function model(b=2,t=2){
  if([b,t].some(z=>typeof z!=='number'||!Number.isFinite(z))||b<0||b>8||t<0||t>10)throw new RangeError('b em [0,8],t em [0,10].');
  const gamma=b/2;let x,v,regime;
  if(b<4){const w=Math.sqrt(4-gamma*gamma),factor=Math.sin(w*t)/w,decay=Math.exp(-gamma*t);x=decay*(Math.cos(w*t)+gamma*factor);v=-4*decay*factor;regime=b===0?'sem amortecimento':'subamortecido';}
  else if(b===4){x=Math.exp(-2*t)*(1+2*t);v=-4*t*Math.exp(-2*t);regime='crítico';}
  else{const beta=Math.sqrt(gamma*gamma-4),slow=-4/(gamma+beta),decay=Math.exp(slow*t),factor=Math.expm1(-2*beta*t)/(2*beta);x=decay*(1+slow*factor);v=4*decay*factor;regime='superamortecido';}
  return{b,t,gamma,x,v,energy:v*v/2+2*x*x,power:-b*v*v,regime};
 }
 function createModels({plot,fmt}){return{dampingRegimes:{label:'Três regimes, mesmas condições iniciais',controls:[['b','Resistência b (kg/s)',0,8,.5,2],['t','Instante de leitura (s)',0,10,.25,2]],render:({b,t})=>{
  const r=model(b,t),curve=Array.from({length:401},(_,j)=>[j/40,model(b,j/40).x]),critical=Array.from({length:401},(_,j)=>[j/40,model(4,j/40).x]);
  return{graph:'<div class="damping-regime-plot">'+plot([{data:curve},{data:critical,style:'reference'}],{xmin:0,xmax:10,ymin:-1.2,ymax:1.2},[[t,r.x]])+'</div>'+`<p class="caption">Horizontal: tempo em segundos; vertical: deslocamento em metros. Azul: b escolhido; tracejado preto: crítico b=4 kg/s. O ponto azul marca a leitura, sem alterar as curvas. Escalas fixas para comparar. Em b=4 as curvas coincidem.</p>`,report:`Regime ${r.regime}; γ=${fmt(r.gamma)} s⁻¹. Em t=${fmt(t)} s: x=${fmt(r.x)} m; v=${fmt(r.v)} m/s; E=${fmt(r.energy)} J; dE/dt=${fmt(r.power)} W. Energia inicial:2 J.`,note:'PVI sintético: m=1 kg,k=4 N/m,x(0)=1 m,v(0)=0. Resistência linear −bv; sem força externa. γ=b/(2m), metade do parâmetro γ de Nussenzveig II. A energia mecânica diminui por transferência ao ambiente; energia total não é destruída. Para estas condições, crítico e superamortecido voltam sem cruzar zero. Comparação em janela finita, não tempo de parada nem prova de retorno mais rápido em qualquer critério.'};
 }}};}
 return{model,createModels};
})();
