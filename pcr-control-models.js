/* Tabela lógica de sinais hipotéticos; não é simulador de reação PCR. */
window.PCRControlModels=(()=>{
 const keys=['target','inhibited','contamination','working','nonspecific'];
 function signals(target=1,inhibited=0,contamination=0,working=1,nonspecific=0){
  if(![target,inhibited,contamination,working,nonspecific].every(v=>Number.isInteger(v)&&(v===0||v===1)))throw new RangeError('Indicadores 0 ou 1');
  return[Number(Boolean(working&&!inhibited&&(target||contamination||nonspecific))),Number(Boolean(working&&contamination)),working,Number(Boolean(working&&!inhibited))];
 }
 function model(target=1,inhibited=0,contamination=0,working=1,nonspecific=0){
  const observed=signals(target,inhibited,contamination,working,nonspecific),compatible=[];
  for(let mask=0;mask<32;mask++){
   const values=keys.map((_,i)=>(mask>>(4-i))&1),obs=signals(...values);
   if(obs.every((v,i)=>v===observed[i]))compatible.push(Object.fromEntries(keys.map((k,i)=>[k,values[i]])));
  }
  return{observed,compatible,compatible_count:compatible.length,target_values:[...new Set(compatible.map(s=>s.target))].sort()};
 }
 function createModels(){return{pcrControls:{label:'O sinal sozinho identifica a explicação?',controls:[['target','Alvo na amostra: 0 não · 1 sim',0,1,1,1],['inhibited','Bloqueio na matriz: 0 não · 1 sim',0,1,1,0],['contamination','Contaminação compartilhada: 0 não · 1 sim',0,1,1,0],['working','Sistema funcional: 0 não · 1 sim',0,1,1,1],['nonspecific','Produto inespecífico na amostra: 0 não · 1 sim',0,1,1,0]],render:({target,inhibited,contamination,working,nonspecific})=>{
  const s=model(target,inhibited,contamination,working,nonspecific);
  const names=['Amostra','Sem molde · NTC','Positivo externo','Controle na matriz'];
  const roles=['Material cuja interpretação interessa.','Sinal de fundo no conjunto da reação.','Verifica funcionamento fora da matriz da amostra.','Canal distinguível de controle, sujeito ao bloqueio da matriz.'];
  const graph='<p>Quatro sinais binários inventados, sem intensidade, tamanho de banda ou Cq. “Detectado” não identifica a sequência.</p><div class="pcr-observations">'+names.map((name,i)=>`<div class="pcr-observation"><div><h4>${name}</h4><p>${roles[i]}</p></div><strong class="${s.observed[i]?'pcr-detected':'pcr-undetected'}">${s.observed[i]?'● Detectado':'○ Não detectado'}</strong></div>`).join('')+'</div><details><summary>Ver os estados compatíveis com os mesmos sinais</summary><p>Colunas: alvo, bloqueio, contaminação, sistema funcional, inespecífico; 0 não, 1 sim. Hipóteses enumeradas, sem pesos probabilísticos.</p><div class="pcr-state-table" role="region" aria-label="Estados lógicos compatíveis" tabindex="0"><table class="truth-table"><thead><tr><th>Alvo</th><th>Bloq.</th><th>Cont.</th><th>Func.</th><th>Inesp.</th></tr></thead><tbody>'+s.compatible.map(row=>'<tr>'+keys.map(k=>`<td>${row[k]}</td>`).join('')+'</tr>').join('')+'</tbody></table></div></details>';
  const alerts=[];if(s.observed[1])alerts.push('NTC com sinal: investigar fundo/contaminação; interpretação da amostra comprometida.');if(!s.observed[2])alerts.push('Positivo externo sem sinal: não validar resultado negativo da amostra.');if(s.observed[2]&&!s.observed[3])alerts.push('Controle na matriz sem sinal: bloqueio é uma hipótese, sem identificar a causa real.');if(s.observed[2]&&s.observed[3]&&!s.observed[1])alerts.push(s.observed[0]?'Sinal na amostra com esses controles: produto detectado, identidade ainda não demonstrada.':'Sem sinal na amostra com esses controles: não detectado nas condições representadas; não concluir ausência absoluta.');
  return{graph,report:alerts.join(' ')+` Os mesmos quatro sinais são compatíveis com ${s.compatible_count} de 32 estados lógicos. Valores de presença do alvo compatíveis: ${s.target_values.join(' e ')}. Contar hipóteses não dá probabilidades.`,note:'Modelo de portas lógicas, não de cinética PCR. O controle na matriz tem canal distinguível e responde ao bloqueio como a reação-alvo por hipótese; não há competição, extração, limiar ou ruído. Produto inespecífico é restrito à amostra no modelo. Nenhum padrão diagnostica uma amostra real ou demonstra prática pessoal.'};
 }}};}
 return{signals,model,createModels};
})();
