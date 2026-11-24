/* Atributos reservados não ajustam a imputação neste protocolo indutivo. */
window.LeakageImputationModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const fraction=(n,d)=>{if(!n)return '0';const g=gcd(n,d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;};
 function model(q=8,missing_y=1){
  if(!Number.isInteger(q)||q<0||q>10||!Number.isInteger(missing_y)||![0,1].includes(missing_y))throw new RangeError('q inteiro 0..10 e rótulo 0/1.');
  const mean_train=1,mean_all=(2+q)/3,proper_prediction=0,leaked_prediction=q>=4?1:0;
  return{mean_train,mean_all,proper_prediction,leaked_prediction,proper_accuracy:(1+Number(missing_y===0))/2,leaked_accuracy:(1+Number(missing_y===leaked_prediction))/2};
 }
 function createModels({plot,fmt}){return{leakageImputation:{label:'Quem pode influenciar o valor preenchido?',controls:[['q','Atributo observado no teste',0,10,1,8],['missing_y','Rótulo do teste sem atributo: 0 ou 1',0,1,1,1]],render:({q,missing_y})=>{
  const s=model(q,missing_y),graph=plot([{data:[[0,1],[10,1]]},{data:[[0,2/3],[10,4]],style:'reference'},{data:[[0,2],[10,2]],style:'secondary'}],{xmin:0,xmax:10,ymin:0,ymax:4},[[q,1],[q,s.mean_all]])+
  '<p class="caption">Horizontal: atributo observado q do teste. Vertical: valor usado para preencher outro registro do teste. Azul: média aprendida só no treino; tracejado preto: média que incluiu teste; pontilhado: limiar fixo 2. As curvas não usam o rótulo do segundo controle.</p>'+
  `<p><strong>Dados inventados:</strong> treino x=[0,2]; teste x=[${q},ausente]. Regra fixada antes: classe 1 se x≥2. No teste, o primeiro rótulo é ${q>=2?1:0}; o segundo é ${missing_y}. Rótulos entram só na contagem de acertos.</p><table class="truth-table"><caption>Mesmo teste, duas origens para o estado de imputação</caption><thead><tr><th>Etapa</th><th>Só treino</th><th>Incluiu teste</th></tr></thead><tbody><tr><th>Média / preenchimento</th><td>1</td><td>${fraction(2+q,3)}</td></tr><tr><th>Classe do registro ausente</th><td>0</td><td>${s.leaked_prediction}</td></tr><tr><th>Acertos no teste de 2 registros</th><td>${s.proper_accuracy*2}/2</td><td>${s.leaked_accuracy*2}/2</td></tr><tr><th>Acurácia observada</th><td>${fmt(100*s.proper_accuracy)}%</td><td>${fmt(100*s.leaked_accuracy)}%</td></tr></tbody></table>`;
  const comparison=s.leaked_accuracy>s.proper_accuracy?'melhorou':s.leaked_accuracy<s.proper_accuracy?'piorou':'ficou igual';
  return{graph:`<div class="leakage-imputation-panel">${graph}</div>`,report:`Acurácia com informação do teste ${comparison} neste cenário. Isso não altera a regra do protocolo: o estado de imputação destinado a avaliação indutiva reservada deve ser aprendido no treino. Mudar q não muda a média correta 1; mudar o rótulo muda a pontuação, não o preenchimento.`,note:'Experimento didático de pré-processamento com dois registros de teste. A regra de decisão foi fornecida, não treinada; não há escolha de modelo, CV ou estimativa de generalização. Ausência é preenchida, não descartada. Mesmo se valores coincidirem, o fluxo de informação continua diferente. Nenhum dado privado ou pacote externo usado.'};
 }}};}
 return{model,createModels};
})();
