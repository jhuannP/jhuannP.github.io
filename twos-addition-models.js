/* Soma em largura fixa, com diagnósticos distintos para carry e overflow. */
window.TwosAdditionModels=(()=>{
 function model(a=7,b=1){
  if([a,b].some(x=>!Number.isInteger(x)||x<0||x>15))throw new RangeError('Padrões inteiros0–15');
  const signed=u=>u<8?u:u-16,carries=[0],bits=[];
  for(let i=0;i<4;i++){const total=((a>>i)&1)+((b>>i)&1)+carries[i];bits.push(total&1);carries.push(total>>1);}
  const result=bits.reduce((s,x,i)=>s+(x<<i),0),exact=signed(a)+signed(b);
  return{a,b,a_signed:signed(a),b_signed:signed(b),result,result_signed:signed(result),exact,carry:carries[4],overflow:exact< -8||exact>7,carries};
 }
 function createModels(){return{twosAddition:{label:'Mesmos bits, duas interpretações da soma',controls:[['a','Padrão A (valor sem sinal)',0,15,1,7],['b','Padrão B (valor sem sinal)',0,15,1,1]],render:({a,b})=>{
  const r=model(a,b),word=u=>u.toString(2).padStart(4,'0'),row=(label,cells)=>`<tr><th scope="row">${label}</th>${cells.map(x=>`<td>${x}</td>`).join('')}</tr>`,bitrow=(label,u)=>row(label,word(u).split(''));
  const graph=`<table class="truth-table twos-word-table"><caption>Quatro bits: colunas do mais significativo para o menos significativo</caption><thead><tr><th>Bit i</th><th>3</th><th>2</th><th>1</th><th>0</th></tr></thead><tbody>${row('Peso com sinal',[-8,4,2,1])}${row('Carry entra',[3,2,1,0].map(i=>r.carries[i]))}${bitrow('A',a)}${bitrow('B',b)}${bitrow('Resultado',r.result)}${row('Carry sai',[3,2,1,0].map(i=>r.carries[i+1]))}</tbody></table><p class="caption">Cada coluna soma os dois bits e o carry que entra. O último carry para fora é c₄; o que entra no bit de sinal é c₃. Resultado guardado: ${word(r.result)}. Carry e overflow são diagnósticos distintos.</p>`;
  return{graph,report:`Sem sinal: ${a}+${b}=${a+b}; palavra baixa=${r.result}; carry=${r.carry}. Com sinal: ${r.a_signed}+(${r.b_signed})=${r.exact}; palavra lida=${r.result_signed}; overflow=${r.overflow?'sim':'não'}. c₃=${r.carries[3]}, c₄=${r.carries[4]}; XOR=${r.carries[3]^r.carries[4]}.`,note:'Modelo didático de quatro bits, soma módulo16. Entradas são padrões sem sinal0–15; suas leituras com sinal pertencem a−8…7. Carry detecta saída do quinto bit na soma sem sinal; overflow detecta soma com sinal fora da faixa. Python int não vira inteiro de quatro bits e não possui essas flags: o modelo as calcula explicitamente. Não é circuito elétrico nem política geral de overflow de qualquer linguagem.'};
 }}};}
 return{model,createModels};
})();
