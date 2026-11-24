/* Distribuição estável após contar/prefixar; rótulos tornam empates visíveis. */
window.StableCountingModels=(()=>{
 const sets=[[2,0,2,1,0,2],[0,0,1,2,2,2],[2,2,2,1,0,0],[],[1,1,1,1]];
 function model(dataset=0,K=3,step=3){
  if(!Number.isInteger(dataset)||dataset<0||dataset>4||!Number.isInteger(K)||K<3||K>8||!Number.isInteger(step)||step<0||step>6)throw new RangeError('Dados0..4,K3..8,passo0..6.');
  const records=sets[dataset].map((k,i)=>[k,String.fromCharCode(65+i)]),n=records.length,effective=Math.min(step,n),freq=Array(K).fill(0),starts=Array(K).fill(0);
  for(const [k]of records)freq[k]++;
  let total=0;for(let k=0;k<K;k++){starts[k]=total;total+=freq[k];}
  const cursor=starts.slice(),out=Array(n).fill(null);
  for(let i=0;i<effective;i++){const rec=records[i],k=rec[0];out[cursor[k]]=rec;cursor[k]++;}
  return{records,n,effective,freq,starts,cursor,out,next:effective<n?{record:records[effective],destination:cursor[records[effective][0]]}:null};
 }
 function createModels(){return{stableCounting:{label:'Distribuir por chave preserva os empates?',controls:[['dataset','Entrada: 0 mista; 1 ordenada; 2 inversa; 3 vazia; 4 empates',0,4,1,0],['K','Tamanho K do domínio [0,K)',3,8,1,3],['step','Registros já distribuídos',0,6,1,3]],render:({dataset,K,step})=>{
  const z=model(dataset,K,step),label=rec=>rec?`${rec[1]}:${rec[0]}`:'vazio';
  const graph=`<div class="stable-counting-panel"><p><strong>Entrada original:</strong> ${z.records.length?z.records.map(label).join(' · '):'sequência vazia'}.</p><p class="caption">Rótulo:chave. Os rótulos identificam registros; somente a chave decide a ordenação. Contagem e prefixos já estão calculados antes do passo0.</p><table class="truth-table"><caption>Frequências, inícios fixos e próxima posição por chave</caption><thead><tr><th>Chave</th><th>Frequência</th><th>Início</th><th>Cursor</th></tr></thead><tbody>${z.freq.map((f,k)=>`<tr><th>${k}</th><td>${f}</td><td>${z.starts[k]}</td><td>${z.cursor[k]}</td></tr>`).join('')}</tbody></table><p><strong>Saída auxiliar no passo ${z.effective}:</strong></p><ol class="counting-slots" aria-label="Posições da saída auxiliar">${z.out.map((rec,i)=>`<li><span>posição ${i}</span><strong>${label(rec)}</strong></li>`).join('')}</ol>${!z.n?'<p>Não há posições de saída nesta entrada.</p>':''}</div>`;
  return{graph,controlRanges:{step:{max:z.n,value:z.effective}},report:z.next?`Próximo registro: ${label(z.next.record)}; será escrito na posição ${z.next.destination}. O cursor dessa chave avançará uma unidade. ${z.effective} de ${z.n} registros distribuídos.`:`Distribuição concluída: ${z.n} registros. ${z.n?'Os empates mantêm a ordem dos rótulos da entrada.':'O resultado é vazio, mas inicializar K contadores ainda tem custo.'}`,note:`Chaves inteiras em [0,${K}); modelo unitário de acesso/indexação. Núcleo: Θ(n+K) tempo e Θ(n+K) espaço auxiliar, incluindo saída. Não compara valores dos registros, não ordena chaves arbitrárias e não é in-place. O traçado com cópias exige mais memória que o núcleo.`};
 }}};}
 return{model,createModels};
})();
