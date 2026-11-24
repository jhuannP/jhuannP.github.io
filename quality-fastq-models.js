/* Leituras inventadas; qualidade marginal não é garantia nem alinhamento. */
window.QualityFASTQModels=(()=>{
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const profiles=[[20,20,20,20,20,20],[40,40,40,40,10,10],[30,30,30,30,30,30]];
 function summarize(qs){
  if(!Array.isArray(qs)||!qs.length||!qs.every(q=>Number.isInteger(q)&&q>=0&&q<=40))throw new RangeError('Q inteiro 0..40, não vazio');
  const ps=qs.map(q=>10**(-q/10)),expected=ps.reduce((a,b)=>a+b,0),mean_p=expected/qs.length;
  return{qs:[...qs],ps,mean_q:qs.reduce((a,b)=>a+b,0)/qs.length,expected,mean_p,effective_q:-10*Math.log10(mean_p),lower:Math.max(...ps),upper:Math.min(1,expected),any_independent:1-ps.reduce((a,p)=>a*(1-p),1),encoded:qs.map(q=>String.fromCharCode(q+33)).join('')};
 }
 function model(kind=1,shift=0,cutoff=.1){
  if(!Number.isInteger(kind)||kind<0||kind>2||!Number.isInteger(shift)||shift< -10||shift>0||!Number.isFinite(cutoff)||cutoff<0||cutoff>3)throw new RangeError('Caso 0..2, deslocamento -10..0, limite 0..3');
  const rows=profiles.map((base,i)=>{const s={case:i,...summarize(base.map(q=>q+shift))};s.retained=s.expected<=cutoff;return s;});
  return{case:kind,shift,cutoff,rows,selected:rows[kind],retained_count:rows.filter(r=>r.retained).length};
 }
 const precise=x=>x.toLocaleString('pt-BR',{maximumSignificantDigits:5});
 function createModels({plot,fmt}){return{fastqQuality:{label:'Qualidade por base, decisão por leitura',controls:[['kind','Leitura: 0 uniforme · 1 heterogênea · 2 uniforme alta',0,2,1,1],['shift','Deslocamento de Q em todas as leituras',-10,0,1,0],['cutoff','Limite de erros esperados por leitura',0,3,.05,.1]],render:({kind,shift,cutoff})=>{
  const s=model(kind,shift,cutoff),r=s.selected;
  const table='<table class="truth-table"><caption>Três leituras sintéticas de seis bases; reter se E ≤ limite</caption><thead><tr><th>Leitura</th><th>Q médio</th><th>E</th><th>Decisão</th></tr></thead><tbody>'+s.rows.map(row=>'<tr class="'+(row.case===kind?'selected':'')+'"><th>'+row.case+'</th><td>'+fmt(row.mean_q)+'</td><td>'+precise(row.expected)+'</td><td>'+(row.retained?'Reter':'Descartar')+'</td></tr>').join('')+'</tbody></table>';
  const perbase='<details><summary>Valores e codificação das seis bases</summary><table class="truth-table"><caption>ACGTAC, escrito na ordem 5′→3′</caption><thead><tr><th>Posição</th><th>Base</th><th>Q</th><th>Caractere</th><th>p de erro</th></tr></thead><tbody>'+r.qs.map((q,i)=>'<tr><th>'+(i+1)+'</th><td>'+'ACGTAC'[i]+'</td><td>'+q+'</td><td>'+esc(String.fromCharCode(q+33))+'</td><td>'+precise(r.ps[i])+'</td></tr>').join('')+'</tbody></table></details>';
  const X=i=>58+i*102,Y=q=>252-q*5.5;
  let graph='<svg viewBox="0 0 600 300" role="img" aria-label="Qualidade por posição; valores exatos na tabela expansível">';
  for(let q=0;q<=40;q+=10)graph+='<line x1="58" y1="'+Y(q)+'" x2="568" y2="'+Y(q)+'" class="plot-grid"/><text x="46" y="'+(Y(q)+7)+'" text-anchor="end" style="font-size:22px">'+q+'</text>';
  for(let i=0;i<6;i++)graph+='<text x="'+X(i)+'" y="285" text-anchor="middle" style="font-size:22px">'+(i+1)+'</text>';
  graph+='<polyline points="'+r.qs.map((q,i)=>X(i)+','+Y(q)).join(' ')+'" class="plot-line"/>'+r.qs.map((q,i)=>'<circle cx="'+X(i)+'" cy="'+Y(q)+'" r="5" class="plot-dot"/>').join('')+'</svg>';
  return{graph:'<p>Horizontal: posição da base (1–6). Vertical: qualidade Q (0–40), em escala logarítmica da probabilidade de erro. A linha apenas liga posições discretas.</p>'+graph+table+perbase,
   report:'Leitura '+kind+': E='+precise(r.expected)+' erros esperados; p médio='+precise(r.mean_p)+', Q equivalente='+fmt(r.effective_q)+'. '+s.retained_count+' de 3 leituras retidas. Sem independência: P(≥1 erro) entre '+precise(r.lower)+' e '+precise(r.upper)+'. Sob independência adicional: '+precise(r.any_independent)+'.',
   note:'Dados sintéticos de qualidade, sem erros sorteados ou medidos. E é uma esperança, não uma contagem observada nem uma probabilidade. A soma não exige independência; o produto exige. Deslocar Q é uma alteração hipotética, não uma recalibração validada. O corte é ilustrativo, não uma recomendação para um protocolo. Qualidade de base não é confiança de alinhamento ou evidência de expressão.'};
 }}};}
 return{summarize,model,createModels};
})();
