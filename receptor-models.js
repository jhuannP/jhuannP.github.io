/* Equilíbrio de ligação 1:1 fechado, sem resposta celular ou dinâmica implementada. */
window.ReceptorModels=(()=>{
 function binding(total=2,receptors=2,kd=1){
  if(![total,receptors,kd].every(Number.isFinite)||total<0||receptors<=0||kd<=0)throw new RangeError('Concentrações inválidas');
  const S=total+receptors+kd,disc=(receptors-total)**2+2*kd*(receptors+total)+kd*kd,C=2*receptors*total/(S+Math.sqrt(disc)),free_ligand=total-C,free_receptor=receptors-C;
  return{total,receptors,kd,complex:C,free_ligand,free_receptor,fraction:C/receptors,approximation:total/(kd+total),depletion:total?C/total:null,half_total:kd+receptors/2};
 }
 function model(total=2,receptors=2,kd=1){
  if(![total,receptors,kd].every(Number.isFinite)||total<0||total>10||receptors<.5||receptors>5||kd<.5||kd>4)throw new RangeError('Parâmetros fora do painel');
  return binding(total,receptors,kd);
 }
 function createModels({plot,sample,fmt}){return{receptorBinding:{label:'Compare ligante livre e total na ocupação',controls:[['total','Ligante total Ltotal em nM',0,10,.5,2],['receptors','Sítios totais Rtotal em nM',.5,5,.5,2],['kd','Kd sintético em nM',.5,4,.5,1]],render:({total,receptors,kd})=>{
  const s=model(total,receptors,kd),half=s.half_total;
  const graph=plot([{data:sample(L=>binding(L,receptors,kd).fraction,0,10)},{data:sample(L=>L/(kd+L),0,10),style:'reference'},{data:[[0,.5],[half,.5],[half,0]],style:'receptor-half'}],{xmin:0,xmax:10,ymin:0,ymax:1.2},[[total,s.fraction]]).replace('<svg ','<svg class="receptor-scene" ');
  const table='<table class="truth-table"><caption>Inventários no equilíbrio, em nM</caption><thead><tr><th>Complexo RL</th><th>L livre</th><th>R livre</th></tr></thead><tbody><tr><td>'+fmt(s.complex)+'</td><td>'+fmt(s.free_ligand)+'</td><td>'+fmt(s.free_receptor)+'</td></tr></tbody></table>';
  return{graph:'<p><strong>Horizontal: ligante total (nM); vertical: fração de sítios ocupados.</strong> Azul: equilíbrio fechado exato. Preto tracejado: aproximação que usa total no lugar de livre. Cinza pontilhado: meia ocupação e seu ligante total. Ponto azul: valor escolhido.</p>'+graph+table,report:'Ocupação exata='+fmt(s.fraction)+'; usando total como livre='+fmt(s.approximation)+'. '+(s.depletion===null?'Sem ligante: fração do ligante ligado não definida (0/0).':'Fração do ligante total que está ligada='+fmt(s.depletion)+'.')+' Meia ocupação requer Llivre=Kd='+fmt(kd)+' nM e Ltotal=Kd+Rtotal/2='+fmt(half)+' nM. A curva é ligação, não resposta celular.',
  note:'Modelo homogêneo, volume fixo, equilíbrio reversível 1:1, sítios independentes, sem internalização, cooperatividade, competição ou ligação inespecífica. Rtotal é concentração efetiva de sítios no volume, não densidade por área de membrana. Todos os números são sintéticos; não há ajuste experimental. A aproximação tracejada só é adequada quando a retirada de ligante livre pela ligação é desprezível. Não calcula tempo, ativação, amplificação ou efeito biológico. Material original em rascunho.'};
 }}}}
 return{binding,model,createModels};
})();
