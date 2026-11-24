/* Modelos didáticos originais de Computação 2. Nenhum simula sinais elétricos. */
window.ComputerModels=(()=>{
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const bits=(n,w=8)=>n.toString(2).padStart(w,'0');
 const hex=n=>'0x'+n.toString(16).toUpperCase().padStart(2,'0');
 const names=['HALT','LDI','LDA','STA','ADD','SUB','JMP','JZ','OUT'];
 const programs=[[0x13,0x3E,0x15,0x4E,0x80,0],[0x13,0x3E,0x11,0x3F,0x2E,0x80,0x5F,0x3E,0x7A,0x64,0]];
 function alu4(a,b,op){let result,c=0,v=0;if(op===0){const sum=a+b;result=sum&15;c=Number(sum>=16);v=Number(((a^result)&(b^result)&8)!==0)}else if(op===1)result=a&b;else if(op===2)result=a|b;else if(op===3)result=a^b;else throw new Error('Operação inválida');return{result,z:Number(result===0),c,v}}
 function m8Trace(program,budget=128,data=Array(16).fill(0)){
  if(!Array.isArray(program)||program.length<1||program.length>16||program.some(x=>!Number.isInteger(x)||x<0||x>255))throw new Error('Programa inválido');
  if(!Array.isArray(data)||data.length!==16||data.some(x=>!Number.isInteger(x)||x<0||x>255)||!Number.isInteger(budget)||budget<0)throw new Error('Estado inválido');
  let pc=0,acc=0,ir=null,halted=false;const memory=[...data],output=[],events=[],frames=[{pc,acc,ir,halted,data:[...memory],output:[],write:null}];let error=null;
  for(let i=0;i<budget&&!halted;i++){
   if(pc>=program.length){error='PC aponta para posição sem instrução';break}
   ir=program[pc];const opcode=ir>>4,arg=ir&15,operation=names[opcode];if(!operation){error='Opcode não definido na M8';break}
   const oldPc=pc,oldAcc=acc;let next=(pc+1)%16,write=null;
   if(opcode===0)halted=true;
   else if(opcode===1)acc=arg;
   else if(opcode===2)acc=memory[arg];
   else if(opcode===3){memory[arg]=acc;write=[arg,acc]}
   else if(opcode===4)acc=(acc+memory[arg])&255;
   else if(opcode===5)acc=(acc-memory[arg])&255;
   else if(opcode===6)next=arg;
   else if(opcode===7&&acc===0)next=arg;
   else if(opcode===8)output.push(acc);
   pc=next;
   events.push({cycle:events.length+1,pc_before:oldPc,word:ir,operation,operand:arg,acc_before:oldAcc,acc_after:acc,pc_after:pc,write,halted,output:[...output]});
   frames.push({pc,acc,ir,halted,data:[...memory],output:[...output],write});
  }
  return{frames,events,error,limitReached:!halted&&!error};
 }
 const models={
 turingUnary:{label:'Acompanhe a cabeça na fita',controls:[['n','Quantidade inicial de símbolos 1',0,6,1,3],['step','Transições executadas',0,7,1,2]],render:({n,step})=>{const k=Math.min(step,n+1),halted=k===n+1,ones=halted?n+1:n;return{controlRanges:{step:{max:n+1,value:k}},graph:`<div class="tape-sequence" role="img" aria-label="Janela da fita; cabeça na posição ${k}">${Array.from({length:n+3},(_,i)=>`<span class="${i===k?'head':''}">${i<ones?'1':'_'}<small>${i}</small></span>`).join('')}</div>`,report:`Após ${k} transições: ${ones} símbolos 1; cabeça na posição ${k}; estado ${halted?'parada':'buscar'}.`,note:'A janela mostra só as posições próximas usadas neste exemplo. A regra lê 1 e move à direita; ao ler branco, escreve 1, move e para. Não é uma máquina universal.'}}},
 bitWord:{label:'Leia os oito bits',controls:[['value','Valor sem sinal',0,255,1,46]],render:({value})=>({graph:`<div class="bit-sequence eight-bits" role="img" aria-label="Padrão binário ${bits(value)}">${[...bits(value)].map((b,i)=>`<span class="${b==='1'?'processed':''}">${b}<small>${2**(7-i)}</small></span>`).join('')}</div>`,report:`${bits(value)}₂ = ${value} em decimal = ${hex(value)}. Leitura com sinal em 8 bits: ${value<128?value:value-256}.`,note:'O mesmo padrão recebe duas interpretações. Os valores sob os bits são pesos para a leitura sem sinal. A mudança de interpretação não altera os bits.'})},
 multiplexer:{label:'Escolha uma fonte de dados',controls:[['a','Entrada A',0,1,1,1],['b','Entrada B',0,1,1,0],['s','Seletor S',0,1,1,1]],render:({a,b,s})=>{const y=s?b:a;return{graph:`<div class="mux-flow"><span class="${s===0?'chosen':''}">A = ${a}</span><span class="${s===1?'chosen':''}">B = ${b}</span><strong>→ Y = ${y}</strong></div>`,report:`S=${s} seleciona ${s?'B':'A'}. Saída Y=${y}.`,note:'Modelo combinacional ideal de um bit. Mudar a entrada não selecionada não altera a saída; não há memória.'}}},
 aluFour:{label:'Compare operações e flags',controls:[['a','Palavra A (0 a 15)',0,15,1,7],['b','Palavra B (0 a 15)',0,15,1,1],['op','Operação: 0 ADD, 1 AND, 2 OR, 3 XOR',0,3,1,0]],render:({a,b,op})=>{const r=alu4(a,b,op),name=['ADD','AND','OR','XOR'][op];return{graph:`<table class="truth-table"><caption>Palavras e flags da ALU de quatro bits</caption><tbody><tr><th>A</th><td>${bits(a,4)}</td><td>${a}</td></tr><tr><th>B</th><td>${bits(b,4)}</td><td>${b}</td></tr><tr class="selected"><th>${name}</th><td>${bits(r.result,4)}</td><td>${r.result}</td></tr><tr><th>Z</th><td colspan="2">${r.z}</td></tr><tr><th>C</th><td colspan="2">${r.c}</td></tr><tr><th>V</th><td colspan="2">${r.v}</td></tr></tbody></table>`,report:`${name}: resultado baixo=${r.result}; leitura com sinal=${r.result<8?r.result:r.result-16}. Z=${r.z}, C=${r.c}, V=${r.v}.`,note:'Z: zero; C: transporte; V: overflow com sinal. Para AND, OR e XOR, C e V são definidos como zero nesta ALU didática.'}}},
 clockRegister:{label:'Separe a entrada do bit armazenado',controls:[['d','Entrada D',0,1,1,1],['en','Habilitação EN',0,1,1,1]],initialState:{q:0,pulses:0},actions:[['pulse','Aplicar pulso de clock'],['reset','Reiniciar registrador']],update:(state,values,action)=>action==='reset'?{q:0,pulses:0}:{q:values.en?values.d:state.q,pulses:state.pulses+1},render:({d,en,q=0,pulses=0})=>({graph:`<div class="register-state"><div><small>Entrada atual</small><strong>D = ${d}</strong></div><span>→</span><div><small>Estado armazenado</small><strong>Q = ${q}</strong></div></div>`,report:`Q=${q}; EN=${en}; pulsos aplicados=${pulses}. ${en?'O próximo pulso captura D.':'O próximo pulso mantém Q.'}`,note:'Mudar D ou EN não aplica um pulso. Reiniciar define Q=0 no simulador; não representa um reset elétrico específico. Entradas ideais e estáveis no evento.'})},
 micro8:{label:'Acompanhe a M8 por instrução',controls:[['program','Programa: 0 soma, 1 contagem',0,1,1,0],['cycle','Instruções executadas',0,22,1,4]],render:({program,cycle})=>{const source=programs[program],run=m8Trace(source),k=Math.min(cycle,run.frames.length-1),state=run.frames[k],last=run.events[k-1];return{controlRanges:{cycle:{max:run.frames.length-1,value:k}},graph:`<dl class="machine-state"><div><dt>PC: próxima posição</dt><dd>${state.pc}</dd></div><div><dt>IR: última instrução</dt><dd>${state.ir===null?'—':hex(state.ir)}</dd></div><div><dt>ACC: acumulador</dt><dd>${state.acc}</dd></div></dl><div class="machine-workspace"><table class="truth-table machine-program"><caption>Programa: linha azul indica a próxima instrução</caption><thead><tr><th>Pos.</th><th>Palavra</th><th>Operação</th></tr></thead><tbody>${source.map((w,i)=>`<tr class="${!state.halted&&i===state.pc?'selected':''}"><td>${i}</td><td>${hex(w)}</td><td>${names[w>>4]} ${[0,8].includes(w>>4)?'':w&15}</td></tr>`).join('')}</tbody></table><div><h4>Memória de dados</h4><div class="machine-memory">${state.data.map((x,i)=>`<div class="${state.write?.[0]===i?'written':''}"><small>M[${i}]</small><strong>${x}</strong></div>`).join('')}</div><p class="caption">Destaque: posição escrita na última instrução.</p></div></div>`,report:`${k} instruções executadas. ${last?'Última: '+last.operation+'. ':'Estado inicial. '}Saída: [${state.output.join(', ')}]. ${state.halted?'HALT observado.':'Ainda não executou HALT.'}`,note:'M8 original de oito bits, programa e dados separados. Um passo representa uma instrução inteira, sem temporização elétrica. Programa 0 calcula 3+5; programa 1 mostra 3,2,1.'}}}
 };
 return{models,m8Trace,alu4,programs};
})();
