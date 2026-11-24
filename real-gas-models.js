/* EOS reduzida; painel acima de Tc, sem coexistência ou dados experimentais. */
window.RealGasModels=(()=>{
 function eos(theta,x){
  if(!Number.isFinite(theta)||theta<=0||!Number.isFinite(x)||x<0||x>=1)throw new RangeError('theta>0 e 0<=x<1');
  const pressure=theta*x/(1-x)-x*x,ideal=theta*x,repulsive=theta*x/(1-x),z=1/(1-x)-x/theta,slope=theta/(1-x)**2-2*x,second=2*theta/(1-x)**3-2,pkappa=x?(slope>0?pressure/(x*slope):null):1;
  return{theta,x,pressure,ideal,repulsive,z,slope,second,pkappa,volume_ratio:x?1/x:null,virial:1+(1-1/theta)*x,volume_correction:x/(1-x),attraction:x===0?0:-x/theta,b2_ratio:1-1/theta,temperature_ratio:27*theta/8};
 }
 function model(theta=.6,x=.2,view=0){
  if(!Number.isFinite(theta)||theta<.4||theta>2||!Number.isFinite(x)||x<0||x>.6||![0,1].includes(view))throw new RangeError('Parâmetros fora do painel');
  return{...eos(theta,x),view};
 }
 function createModels({plot,sample,fmt}){return{realGas:{label:'Compare pressão, Z e limite diluído',controls:[['theta','Temperatura reduzida Θ=RTb/a',.4,2,.1,.6],['x','Densidade reduzida x=b/Vm',0,.6,.05,.2],['view','Vista: 0 fator Z · 1 pressão reduzida',0,1,1,0]],render:({theta,x,view})=>{
  const s=model(theta,x,view),data=sample(u=>eos(theta,u)[view===0?'z':'pressure'],0,.6),ref=sample(u=>view===0?1:eos(theta,u).ideal,0,.6),third=sample(u=>eos(theta,u)[view===0?'virial':'repulsive'],0,.6);
  const graph=plot([{data},{data:ref,style:'reference'},{data:third,style:'gradient-level'}],{xmin:0,xmax:.6,ymin:0,ymax:view===0?2.4:3.2},[[x,view===0?s.z:s.pressure]]).replace('<svg ','<svg class="real-gas-scene" ');
  const caption=view===0?'Vertical: Z. Azul: van der Waals; preto tracejado: ideal Z=1; cinza pontilhado: virial truncado após o termo linear em x.':'Vertical: P*=pb²/a. Azul: van der Waals; preto tracejado: pressão ideal; cinza pontilhado: só o termo de volume, na mesma escala.';
  const rows='<table class="truth-table"><caption>'+(x===0?'Valores-limite em x→0; não há volume molar finito em x=0':'Valores na densidade escolhida')+'</caption><thead><tr><th>Z</th><th>P*</th><th>pκT</th></tr></thead><tbody><tr><td>'+fmt(s.z)+'</td><td>'+fmt(s.pressure)+'</td><td>'+fmt(s.pkappa)+'</td></tr></tbody></table>';
  return{graph:'<p><strong>Horizontal: x=b/Vm.</strong> '+caption+' Ponto azul: estado escolhido, ou seu limite diluído.</p>'+graph+rows,report:'Θ='+fmt(theta)+'; T/Tc='+fmt(s.temperature_ratio)+'. '+(x===0?'x=0 representa Vm/b→∞.':'Vm/b='+fmt(s.volume_ratio)+'.')+' Z=1 + '+fmt(s.volume_correction)+' '+(s.attraction<0?'− '+fmt(-s.attraction):'+ 0')+'. B₂/b='+fmt(s.b2_ratio)+'. Derivada dP*/dx='+fmt(s.slope)+' positiva no painel. '+(Math.abs(theta-1)<1e-12?'Temperatura de Boyle do modelo: o termo linear do virial é zero, mas o desvio finito não desaparece.':'O fator Z e a compressibilidade κT são grandezas diferentes.'),
  note:'a,b>0 são parâmetros do modelo, sem valores de substância real. Θ=RTb/a não é T/Tc; Tc corresponde a Θc=8/27. O painel usa Θ≥0,4, acima de Θc, e x≤0,6; não mostra laços subcríticos, coexistência ou construção de Maxwell. pκT é produto adimensional da pressão pela compressibilidade isotérmica; no ideal vale 1. A expansão virial truncada deve ser usada no regime diluído; ela não reproduz a equação completa em toda a janela. Em x=0 mostramos limites, sem avaliar 0/0. Sem trajetória, ajuste ou precisão experimental presumida. Material original em rascunho.'};
 }}}}
 return{eos,model,createModels};
})();
