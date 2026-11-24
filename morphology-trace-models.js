/* Traçado 2D sintético e calibração isotrópica; nenhuma fisiologia inferida. */
window.MorphologyTraceModels=(()=>{
 function model(height=160,scale=.1,coarse=0){
  if(![height,scale].every(Number.isFinite)||height<0||height>160||scale<.1||scale>1||!Number.isInteger(coarse)||coarse<0||coarse>1)throw new RangeError('Controles inválidos');
  const full_length=2*Math.hypot(120,height)*scale,distance=240*scale,length=coarse?distance:full_length;
  return{height,scale,coarse,length,distance,full_length,ratio:length/distance};
 }
 function createModels({fmt}){return{morphologyTrace:{label:'O que o traçado permite medir?',controls:[['height','Altura do ponto intermediário (px)',0,160,20,160],['scale','Calibração (µm/px)',.1,1,.1,.1],['coarse','Amostragem: 0 três pontos · 1 só pontas',0,1,1,0]],render:({height,scale,coarse})=>{
  const m=model(height,scale,coarse),X=x=>70+x*1.9,Y=y=>350-y*1.9;
  let svg='<svg class="neurite-trace-scene" viewBox="0 0 600 440" role="img" aria-label="Traçado sintético de três pontos, com a mesma escala em x e y; distâncias na tabela">';
  for(const x of [0,120,240])svg+='<line x1="'+X(x)+'" y1="30" x2="'+X(x)+'" y2="350" class="plot-grid"/><text x="'+X(x)+'" y="390" text-anchor="middle" style="font-size:22px">'+x+'</text>';
  for(const y of [0,80,160])svg+='<line x1="70" y1="'+Y(y)+'" x2="526" y2="'+Y(y)+'" class="plot-grid"/><text x="55" y="'+(Y(y)+7)+'" text-anchor="end" style="font-size:22px">'+y+'</text>';
  svg+='<polyline points="'+[[0,0],[120,height],[240,0]].map(([x,y])=>X(x)+','+Y(y)).join(' ')+'" fill="none" stroke="var(--ink)" stroke-width="4"/>';
  svg+='<polyline points="'+(coarse?[[0,0],[240,0]]:[[0,0],[120,height],[240,0]]).map(([x,y])=>X(x)+','+Y(y)).join(' ')+'" fill="none" stroke="var(--blue)" stroke-width="3" stroke-dasharray="8 5"/>';
  for(const [i,[x,y]] of [[0,[0,0]],[1,[120,height]],[2,[240,0]]])svg+='<circle cx="'+X(x)+'" cy="'+Y(y)+'" r="6" fill="'+(coarse&&i===1?'var(--ink)':'var(--blue)')+'"/>';
  svg+='<text x="300" y="430" text-anchor="middle" style="font-size:22px">x/px</text><text x="25" y="25" style="font-size:22px">y/px</text></svg>';
  const table='<table class="truth-table"><caption>Medidas do caminho e das pontas</caption><thead><tr><th>Grandeza</th><th>Valor</th></tr></thead><tbody><tr><th>Traçado completo sintético</th><td>'+fmt(m.full_length)+' µm</td></tr><tr><th>Comprimento com pontos usados</th><td>'+fmt(m.length)+' µm</td></tr><tr><th>Distância entre pontas</th><td>'+fmt(m.distance)+' µm</td></tr><tr><th>Razão comprimento/distância</th><td>'+fmt(m.ratio)+'</td></tr></tbody></table>';
  return{graph:'<p>Exemplo geométrico, sem imagem microscópica: preto é o caminho completo de três pontos; azul tracejado é o caminho medido com a amostragem escolhida. Eixos em pixels, com a mesma escala. Os números em µm usam a calibração indicada.</p>'+svg+table,report:'Comprimento medido='+fmt(m.length)+' µm; distância entre pontas='+fmt(m.distance)+' µm; razão='+fmt(m.ratio)+'. '+(coarse?'O ponto intermediário foi omitido: mede-se a corda.':'Os três pontos descrevem exatamente esta linha quebrada sintética.'),note:'A calibração muda as medidas físicas, não a geometria desenhada em pixels. Em um neurito real, esse traçado pode perder curvatura, dimensão z e ramos. Não mede área, volume, velocidade, transmissão sináptica ou função celular. Nenhum dado de Jhuann ou de pesquisa. A palavra comprimento refere-se ao traçado selecionado, não à extensão 3D verdadeira de uma célula.'};
 }}};}
 return{model,createModels};
})();
