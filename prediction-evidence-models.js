/* Comparação com limite determinístico declarado, sem teste estatístico. */
window.PredictionEvidenceModels=(()=>{
 function model(accel=2,bias_cm=0,bound_cm=4){
  if(![accel,bias_cm,bound_cm].every(Number.isInteger)||accel<0||accel>4||bias_cm< -20||bias_cm>20||bound_cm<0||bound_cm>20)throw new RangeError('Controles inválidos');
  const noise=[0,4,-4,4,-4],rows=noise.map((e,i)=>{const observed=100+50*i+50*i*i+e+2*bias_cm,predicted=100+50*i+25*accel*i*i,residual=observed-predicted;return{time:i/2,observed:observed/200,predicted:predicted/200,residual:residual/200,within:Math.abs(residual)<=2*bound_cm};});
  return{accel,bias_cm,bound_cm,rows,inside:rows.filter(r=>r.within).length,max_abs:Math.max(...rows.map(r=>Math.abs(r.residual)))};
 }
 function createModels({fmt}){return{predictionEvidence:{label:'Previsão, resíduo e limite assumido',controls:[['accel','Aceleração candidata a (m/s²)',0,4,1,2],['bias_cm','Desvio comum no dado sintético (cm)',-20,20,5,0],['bound_cm','Limite de erro assumido B (cm)',0,20,2,4]],render:({accel,bias_cm,bound_cm})=>{
  const m=model(accel,bias_cm,bound_cm),B=bound_cm/100,R=Math.ceil(Math.max(.1,m.max_abs+.02,B+.02)*10)/10,X=t=>100+210*t,Y=r=>160-120*r/R;
  let svg='<svg viewBox="0 0 600 330" role="img" aria-label="Cinco resíduos versus tempo; faixa de limite assumido, valores completos na tabela"><rect x="100" y="'+Y(B)+'" width="420" height="'+(Y(-B)-Y(B))+'" fill="var(--blue)" opacity=".08"/>';
  for(let i=0;i<=4;i++){const t=i/2,r=-R+i*R/2;svg+='<line x1="100" y1="'+Y(r)+'" x2="520" y2="'+Y(r)+'" class="plot-grid"/><text x="85" y="'+(Y(r)+7)+'" text-anchor="end" style="font-size:22px">'+fmt(r)+'</text><text x="'+X(t)+'" y="308" text-anchor="middle" style="font-size:22px">'+fmt(t)+'</text>';}
  svg+='<line x1="100" y1="160" x2="520" y2="160" stroke="var(--ink)" stroke-width="1.5"/>';
  for(const b of [-B,B])svg+='<line x1="100" y1="'+Y(b)+'" x2="520" y2="'+Y(b)+'" stroke="var(--blue)" stroke-width="2" stroke-dasharray="7 4"/>';
  for(const r of m.rows)svg+='<circle cx="'+X(r.time)+'" cy="'+Y(r.residual)+'" r="6" fill="var(--ink)"/>';
  svg+='<text x="100" y="25" style="font-size:22px">r/m</text><text x="585" y="308" text-anchor="end" style="font-size:22px">t/s</text></svg>';
  const table='<table class="truth-table"><caption>Posições e resíduos, em metros; tempo em segundos</caption><thead><tr><th>t</th><th>Dado</th><th>Previsão</th><th>r</th><th>|r|≤B?</th></tr></thead><tbody>'+m.rows.map(r=>'<tr><td>'+fmt(r.time)+'</td><td>'+fmt(r.observed)+'</td><td>'+fmt(r.predicted)+'</td><td>'+fmt(r.residual)+'</td><td>'+(r.within?'Sim':'Não')+'</td></tr>').join('')+'</tbody></table>';
  return{graph:'<p>Pontos pretos: resíduos nos cinco instantes, sem interpolação. Linhas azuis: ±B, limite de erro assumido para o exercício. A escala vertical muda com os controles; compare os valores da tabela. Não é intervalo de confiança. x₀=0,5 m e v₀=0,5 m/s ficam fixos.</p>'+svg+table,report:m.inside+'/5 previsões dentro do limite declarado. Maior |r|='+fmt(m.max_abs)+' m; B='+fmt(B)+' m. '+(m.inside===5?'Compatibilidade com estas condições não prova o modelo.':'Há inconsistência entre estes dados, previsão e limite: investigue o conjunto de hipóteses.'),note:'Dados sintéticos fixos, gerados com a=2 m/s² e perturbações determinísticas de 0 ou ±0,02 m; o desvio comum é acrescentado a todos os pontos. Tempos e condições iniciais exatos por hipótese. Alterar B muda um limite assumido, não mede melhor nem gera dados novos; alterar o desvio cria outro cenário sintético. Não há sorteio, ajuste automático, teste de hipótese, p-valor ou probabilidade de o modelo ser verdadeiro. Aceleração constante só é explorada entre 0 e 2 s.'};
 }}};}
 return{model,createModels};
})();
