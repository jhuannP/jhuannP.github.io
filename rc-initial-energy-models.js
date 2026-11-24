/* RC ideal generalizado; guarda a API visual rcCharging e os controles antigos. */
window.RCInitialEnergyModels=(()=>{
 function model(R=2,C=3,V=4,u=1,V0=0){
  if([R,C,V,u,V0].some(x=>typeof x!=='number'||!Number.isFinite(x))||R<=0||C<=0||V<0||V0<0||u<0)throw new RangeError('R,C positivos;V,V0,u não negativos e finitos.');
  const e=Math.exp(-u),fraction=-Math.expm1(-u),delta=V-V0,VC=V0+delta*fraction,I=delta/R*e;
  const result={tau:R*C,time:u*R*C,VC,I,q:C*VC,VR:R*I,initial:C*V0*V0/2,stored:C*VC*VC/2,change:C*delta*fraction*(VC+V0)/2,source:C*V*delta*fraction,dissipated:C*delta*delta*(-Math.expm1(-2*u))/2,power_source:V*I,power_R:R*I*I,power_C:VC*I};
  for(const key of Object.keys(result))if(result[key]===0)result[key]=0;
  return result;
 }
 function createModels({plot,sample,fmt}){return{rcCharging:{label:'RC: para onde vai a energia?',controls:[['R','Resistência R (Ω)',.5,3,.5,2],['C','Capacitância C (F)',1,4,1,3],['V','Tensão da fonte V (V)',0,5,1,4],['u','Tempo em constantes u=t/(RC)',0,5,.5,1],['V0','Tensão inicial V₀ (V)',0,6,1,0],['view','Vista: 0 tensões; 1 energias',0,1,1,0]],render:({R,C,V,u,V0=0,view=0})=>{
  const z=model(R,C,V,u,V0),at=s=>model(R,C,V,s,V0),energy=view===1;
  let series,M,negative;
  if(energy){series=[{data:sample(s=>at(s).stored,0,5)},{data:sample(s=>at(s).dissipated,0,5),style:'reference'},{data:sample(s=>at(s).source,0,5),style:'secondary'}];M=Math.max(z.initial,C*V*V/2,C*(V-V0)**2/2,Math.abs(C*V*(V-V0)),1);negative=V<V0&&V>0;}
  else{series=[{data:sample(s=>at(s).VC,0,5)},{data:sample(s=>at(s).VR,0,5),style:'reference'}];M=Math.max(V,V0,Math.abs(V-V0),1);negative=V<V0;}
  const graph=`<div class="rc-initial-energy-panel">`+plot(series,{xmin:0,xmax:5,ymin:negative?-M:0,ymax:M},[[u,energy?z.stored:z.VC]]).replace('viewBox="0 0 640 300"','viewBox="-20 0 660 300"')+`<p class="caption">Horizontal: u=t/(RC), sem unidade. ${energy?'Vertical: energia em joules. Azul: U_C atual; tracejado preto: Q_R acumulado; pontilhado azul: E_fonte fornecida (negativa se absorvida).':'Vertical: tensão em volts. Azul: V_C; tracejado preto: V_R=RI,com sinal. Corrente não está sobreposta a um eixo de tensão.'} O ponto marca ${energy?'U_C':'V_C'} no instante escolhido.</p><table class="truth-table"><caption>Balanço desde t=0 até ${fmt(z.time)} s — τ=${fmt(z.tau)} s</caption><tbody><tr><th>V_C / I</th><td>${fmt(z.VC)} V / ${fmt(z.I)} A</td></tr><tr><th>U_C inicial / atual</th><td>${fmt(z.initial)} / ${fmt(z.stored)} J</td></tr><tr><th>ΔU_C</th><td>${fmt(z.change)} J</td></tr><tr><th>E_fonte fornecida</th><td>${fmt(z.source)} J</td></tr><tr><th>Q_R dissipado</th><td>${fmt(z.dissipated)} J</td></tr></tbody></table></div>`;
  return{graph,report:`E_fonte=ΔU_C+Q_R. Valores arredondados em J: fonte ${fmt(z.source)}; variação ${fmt(z.change)}; dissipação ${fmt(z.dissipated)}. ${V<V0?(V>0?'Corrente negativa: a fonte ideal absorve energia do capacitor.':'Descarga resistiva: fonte0V equivale ao fechamento por fio ideal,sem energia fornecida.'):V===V0?'Sem transiente: tensão inicial igual à fonte.':'Carga: a fonte fornece energia ao circuito.'}`,note:'Fonte ideal constante capaz de fornecer ou absorver energia,R e C positivos e constantes,regime de circuito concentrado sem indutância ou radiação. I=dq/dt é positiva ao aumentar a carga da placa definida por q=C V_C. V₀ é condição inicial;não se aplica R=0. Números são cenários didáticos,não componentes ou medidas de laboratório.'};
 }}};}
 return{model,createModels};
})();
