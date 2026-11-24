/* Traço abstrato de execução sequencial; não observa a pilha real do navegador. */
window.RecursionModels=(()=>{
 function trace(kind=0,n=4){
  if(![0,1].includes(kind)||!Number.isInteger(n)||n<0||n>10)throw new RangeError('Modo 0/1, n inteiro de 0 a 10');
  const events=[],stack=[];let calls=0,mults=0,peak=0;
  function record(event,arg,value=null){events.push({event,arg,value,stack:stack.map(f=>({...f})),calls,mults,peak})}
  function visit(m){
   calls++;stack.push({n:m,state:'executando'});peak=Math.max(peak,stack.length);record('entrada',m);let value;
   if(m===0)value=1;
   else{stack.at(-1).state='aguardando';const q=visit(kind===0?m-1:Math.floor(m/2));
    if(kind===0){value=m*q;mults++}else{value=q*q;mults++;if(m%2){value*=2;mults++}}
   }
   stack.at(-1).state='devolvendo';record('retorno',m,value);stack.pop();return value;
  }
  const result=visit(n);record('fim',n,result);return{kind,n,result,events,calls,mults,peak};
 }
 function createModels(){return{recursionTrace:{label:'Acompanhe chamadas e retornos',controls:[['kind','Algoritmo: 0 fatorial · 1 potência 2ⁿ',0,1,1,0],['n','Entrada n',0,10,1,4],['step','Evento do traço',0,22,1,4]],render:({kind,n,step})=>{
  const t=trace(kind,n),k=Math.min(step,t.events.length-1),s=t.events[k],name=kind===0?'fat':'pot2';
  const pending=m=>m===0?'caso base: 1':kind===0?`${m} × fat(${m-1})`:`q=pot2(${Math.floor(m/2)}); q²${m%2?' × 2':''}`;
  const rows=s.stack.map((f,i)=>`<tr class="${i===s.stack.length-1?'selected':''}"><td>${name}(${f.n})</td><td>${f.state==='devolvendo'?`devolve ${s.value}`:f.state==='aguardando'?pending(f.n):'avalia caso base'}</td></tr>`).join('');
  const event=s.event==='entrada'?`Entrou em ${name}(${s.arg}).`:s.event==='retorno'?`${name}(${s.arg}) devolve ${s.value}. O quadro ainda aparece antes de ser retirado.`:`Fim: resultado ${s.value}; pilha vazia.`;
  return{controlRanges:{step:{max:t.events.length-1,value:k}},graph:`<p><strong>${event}</strong> Raiz no alto; chamada atual na última linha azul. Cada linha mantém seu próprio argumento.</p><table class="truth-table recursion-table"><caption>Pilha no evento ${k} de ${t.events.length-1}</caption><thead><tr><th>Chamada</th><th>Ação pendente</th></tr></thead><tbody>${rows||'<tr><td colspan="2">Nenhuma chamada ativa.</td></tr>'}</tbody></table>`,report:`Até este evento: ${s.calls} ${s.calls===1?'entrada':'entradas'}, pico de ${s.peak} ${s.peak===1?'quadro':'quadros'} e ${s.mults} multiplicações concluídas. ${s.event==='fim'?`Resultado final: ${t.result}.`:'Avance para acompanhar a execução.'} Total deste algoritmo e entrada: ${t.calls} ${t.calls===1?'chamada':'chamadas'}, pico ${t.peak}, ${t.mults} multiplicações.`,note:'Fatorial usa base n=0 e uma chamada n−1. Potência usa base n=0, uma única chamada n//2 e reaproveita q: q², seguido de ×2 se n for ímpar. O traço não inclui as funções de validação nem o programa chamador. Retornos mostram o quadro antes de desempilhar; fim mostra pilha vazia. Eventos são passos lógicos, não tempo medido; multiplicações contam inclusive fatores 1. Os valores n≤10 ficam exatos em Number. Memória do histórico de snapshots não é a memória auxiliar do algoritmo. Material original em rascunho.'};
 }}}}
 return{trace,createModels};
})();
