/* Fontes esféricas prescritas. R=epsilon0=1 normalizados; shift = 4*pi*C. */
window.PotentialModels=(()=>{
 function model(profile=0,charge=1,radius=.5,test_charge=-1,shift=0){
  if(![0,1].includes(profile)||![charge,radius,test_charge,shift].every(Number.isFinite)||radius<0)throw new RangeError('Perfil 0/1, parâmetros finitos e raio não negativo');
  const scaled=radius<=1?charge*(profile===0?(3-radius*radius)/2:1):charge/radius;
  const base=scaled/(4*Math.PI),value=(scaled+shift)/(4*Math.PI),delta=(scaled-charge/2)/(4*Math.PI),boundary=profile===1&&radius===1&&charge!==0;
  const field=boundary?null:profile===0&&radius<=1?charge*radius/(4*Math.PI):radius<1?0:charge/(4*Math.PI*radius*radius);
  const energy=test_charge*delta;
  return{profile,charge,radius,test_charge,shift,base,value,start:(charge/2+shift)/(4*Math.PI),delta,field,energy,work:-energy,boundary,inner_field:profile===0?charge/(4*Math.PI):0,outer_field:charge/(4*Math.PI)};
 }
 function createModels({plot,sample,fmt}){return{electricPotential:{label:'Mude a referência e confira o trabalho',controls:[['profile','Fonte: 0 esfera volumétrica · 1 casca fina',0,1,1,0],['Q','Carga da fonte Q (normalizada)',-2,2,.5,1],['r','Destino B: raio r/R',0,4,.1,.5],['q','Carga de teste q: −1, 0 ou +1',-1,1,1,-1],['C','Referência: deslocamento 4πC',-1,1,.5,0]],render:({profile,Q,r,q,C})=>{
  const s=model(profile,Q,r,q,C), f=x=>4*Math.PI*model(profile,Q,x,q,0).base;
  const graph=plot([{data:sample(f,0,4),style:'reference'},{data:sample(x=>f(x)+C,0,4)}],{xmin:0,xmax:4,ymin:-4,ymax:4},[[r,4*Math.PI*s.value]]).replace('<svg ','<svg class="potential-scene" ');
  const value=x=>x===null?'não único':fmt(x);
  return{graph:'<p>Horizontal: r/R. Vertical: 4πV. Azul: referência escolhida; preto tracejado: V₀ com zero no infinito. Ponto: destino B. Fonte termina em r/R=1; origem A fixa em r/R=2.</p>'+graph+`<table class="truth-table potential-table"><caption>Valores em B, sem o fator gráfico 4π</caption><thead><tr><th>V(B)</th><th>Eᵣ(B)</th><th>ΔU de A a B</th></tr></thead><tbody><tr><td>${fmt(s.value)}</td><td>${value(s.field)}</td><td>${fmt(s.energy)}</td></tr></tbody></table>`,
  report:`V(A)=${fmt(s.start)}; ΔV=${fmt(s.delta)}; ΔU=qΔV=${fmt(s.energy)}; trabalho elétrico Wₑₗ=${fmt(s.work)}. ${s.boundary?`Na casca ideal: V é contínuo, mas Eᵣ tem limites ${fmt(s.inner_field)} e ${fmt(s.outer_field)}; não há derivada radial única na camada.`:s.field===0&&Q!==0?'Campo nulo neste ponto não exige potencial nulo.':'O campo acompanha a inclinação negativa de V; a força também depende do sinal de q.'} ${q===0?'q=0: energia transferida e força são nulas; o potencial da fonte permanece.':''}`,
  note:'R=ε₀=1 em unidades normalizadas, como no painel de Gauss; kₑ=1/(4π). O controle mostra 4πC: C real do modelo é esse número dividido por 4π. Mudar a referência desloca os valores de V e de U nos dois pontos, sem mudar E, ΔV ou ΔU. Fonte prescrita sem resposta à carga de teste; q=±1 representa o sinal de uma sonda sem retroação. Não integra trajetória: ΔK=Wₑₗ exige que apenas a força elétrica realize trabalho. Nenhum dado experimental ou da IC.'};
 }}}}
 return{model,createModels};
})();
