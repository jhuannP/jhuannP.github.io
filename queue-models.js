/* Traçado próprio: FIFO lógico versus vetor físico, com duplicação. */
window.QueueModels=(()=>{
 const operations=[['in','A'],['in','B'],['out'],['in','C'],['in','D'],['in','E'],['out'],['out'],['in','F'],['in','G'],['in','H'],['out'],['out'],['out']];
 function trace(capacity=2){
  if(![2,4].includes(capacity))throw Error('Capacidade de demonstração 2 ou 4');
  let slots=Array(capacity).fill(null),head=0,size=0,copied=0,inserted=0;const states=[];
  const record=(action,removed=null)=>states.push({action,removed,slots:slots.slice(),head,size,capacity:slots.length,copied,inserted,logical:Array.from({length:size},(_,i)=>slots[(head+i)%slots.length])});
  record('Inicial');
  for(const [op,value]of operations){if(op==='in'){
   if(size===slots.length){const next=Array(slots.length*2).fill(null);for(let i=0;i<size;i++)next[i]=slots[(head+i)%slots.length];slots=next;head=0;copied+=size;}
   slots[(head+size)%slots.length]=value;size++;inserted++;record('Entrar '+value);
  }else{const removed=slots[head];slots[head]=null;head=(head+1)%slots.length;size--;record('Retirar '+removed,removed)}}return states;
 }
 function createModels(){return{circularQueue:{label:'Veja a fila lógica e suas posições no vetor',controls:[['capacity','Capacidade inicial: 0 → 2 · 1 → 4',0,1,1,0],['step','Operações executadas',0,14,1,5]],render:({capacity,step})=>{
  const states=trace(capacity?4:2),r=states[step],old=states[Math.max(0,step-1)],occupied=new Set(Array.from({length:r.size},(_,i)=>(r.head+i)%r.capacity));
  const graph=`<p>Ordem de saída: <strong>${r.logical.length?r.logical.join(' → '):'fila vazia'}</strong></p><table class="truth-table"><caption>Vetor físico após ${r.action}</caption><thead><tr><th>Índice</th><th>Valor</th><th>Função</th></tr></thead><tbody>${r.slots.map((x,i)=>`<tr class="${i===r.head&&r.size?'selected':''}"><td>${i}</td><td>${x??'—'}</td><td>${i===r.head&&r.size?'Primeiro a sair':occupied.has(i)?'Ocupado':'Livre'}</td></tr>`).join('')}</tbody></table>`;
  return{graph,report:`Passo ${step}: ${r.action}. n=${r.size}; capacidade=${r.capacity}; cabeça=${r.head}. Inserções=${r.inserted}; cópias acumuladas=${r.copied}.${r.capacity>old.capacity?' Crescimento: capacidade duplicada e cabeça voltou a zero.':''}`,note:'O traçado usa 14 operações fixas. FIFO segue (cabeça+i) mod capacidade, não a ordem dos índices do vetor. A fila dobra ao ficar cheia e não encolhe; retirar libera a referência. Cópias contam somente itens transferidos no crescimento, sem alocação, limpeza ou operações internas do Python. Uma inserção pode custar O(n); uma sequência custa O(1) amortizado por inserção.'};
 }}};}return{trace,createModels};
})();
