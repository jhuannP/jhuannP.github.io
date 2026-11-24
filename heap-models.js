/* Heap mínimo estável: exemplo sintético, sem agendamento externo. */
window.HeapModels=(()=>{
 const actions=[[3,'A'],[1,'B'],[1,'C'],[2,'D'],null,null,[0,'E'],null,null,null];
 const less=(a,b)=>a[0]<b[0]||(a[0]===b[0]&&a[1]<b[1]);
 function trace(){
  const heap=[],removed=[],out=[{heap:[],removed:[],action:'Estado vazio'}];let ticket=0;
  for(const action of actions){let label;
   if(action){const [p,value]=action;heap.push([p,ticket++,value]);let i=heap.length-1;while(i>0){const parent=Math.floor((i-1)/2);if(!less(heap[i],heap[parent]))break;[heap[i],heap[parent]]=[heap[parent],heap[i]];i=parent}label=`Inserir ${value} com prioridade ${p}`}
   else{const value=heap[0][2],last=heap.pop();if(heap.length){heap[0]=last;let i=0;while(2*i+1<heap.length){let child=2*i+1;if(child+1<heap.length&&less(heap[child+1],heap[child]))child++;if(!less(heap[child],heap[i]))break;[heap[i],heap[child]]=[heap[child],heap[i]];i=child}}removed.push(value);label=`Retirar ${value}`}
   out.push({heap:heap.map(e=>[...e]),removed:[...removed],action:label});
  }return out;
 }
 const models={stableHeapTrace:{label:'Acompanhe o heap e os desempates',controls:[['step','Operações concluídas',0,10,1,4]],render:({step})=>{const s=trace()[step];return{graph:`<table class="finite-set-table"><caption>Vetor do heap após a operação ${step}</caption><thead><tr><th>Índice</th><th>Pai</th><th>Prioridade</th><th>Bilhete</th><th>Valor</th></tr></thead><tbody>${s.heap.length?s.heap.map(([p,t,v],i)=>`<tr><td>${i}</td><td>${i===0?'raiz':Math.floor((i-1)/2)}</td><td>${p}</td><td>${t}</td><td>${v}</td></tr>`).join(''):'<tr><td colspan="5">Fila de prioridade vazia</td></tr>'}</tbody></table>`,report:`${s.action}. ${s.heap.length?`Próxima retirada: ${s.heap[0][2]}, prioridade ${s.heap[0][0]}.`:'Sem próximo elemento.'} Retirados: ${s.removed.length?s.removed.join(', '):'nenhum'}.`,note:'Menor prioridade sai primeiro; empate usa bilhete crescente. Sequência: inserir A:3, B:1, C:1, D:2; retirar duas vezes; inserir E:0; retirar até esvaziar. A ordem do vetor não é a ordem completa de retirada. Os bilhetes e valores não são novos índices da árvore. Traço discreto, sem custos temporais reais ou execução de tarefas.'}}}};
 return{models,trace};
})();
