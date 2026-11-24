/* Duas composições específicas e uma composição alvo; taxas internas fixadas. */
window.AggregationWeightModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const fraction=(n,d)=>{if(n===0)return '0';const g=gcd(Math.abs(n),d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;};
 function model(a=10,b=90,w=50){
  if([a,b,w].some(x=>!Number.isInteger(x)||x<0||x>100))throw new RangeError('Pesos inteiros entre 0 e 100.');
  const an=300+6*a,bn=200+6*b,ca=300+6*w,cb=200+6*w;
  return{a,b,w,an,bn,ca,cb,pooledA:an/1000,pooledB:bn/1000,commonA:ca/1000,commonB:cb/1000,difference:(an-bn)/1000,reversal:an<bn};
 }
 function bars(z){
  const rows=[['Grupo 0 · taxas fornecidas',900,800],['Grupo 1 · taxas fornecidas',300,200],['Mistura · pesos por opção',z.an,z.bn],['Padronização · peso comum',z.ca,z.cb]];
  let body='';
  rows.forEach(([title,a,b],i)=>{const y=28+i*90;body+=`<text x="12" y="${y}" class="aggregation-row-title">${title}</text>`;
   [[a,'A',y+12],[b,'B',y+35]].forEach(([v,name,by])=>{body+=`<text x="20" y="${by+13}">${name}</text><rect x="42" y="${by}" width="${220*v/1000}" height="17" class="aggregation-bar-${name.toLowerCase()}"/><text x="278" y="${by+13}">${fraction(v,1000)}</text>`;});
  });
  for(let i=0;i<=4;i++){const x=42+220*i/4;body+=`<line x1="${x}" y1="382" x2="${x}" y2="387" class="plot-axis"/><text x="${x}" y="405" text-anchor="middle">${String(i/4).replace('.',',')}</text>`;}
  return `<svg viewBox="0 0 360 420" role="img" aria-label="Taxas de sucesso nas opções A e B: dois grupos, mistura e composição comum; frações na tabela abaixo">${body}</svg>`;
 }
 function createModels(){return{aggregationWeights:{label:'A comparação depende dos pesos',controls:[['a','Grupo 0 em A — em %',0,100,5,10],['b','Grupo 0 em B — em %',0,100,5,90],['w','Grupo 0 no alvo comum — em %',0,100,5,50]],render:({a,b,w})=>{
  const z=model(a,b,w),absent=[a,b].some(x=>x===0||x===100);
  const graph=`<div class="aggregation-weight-panel">${bars(z)}<p class="caption">Comprimento horizontal: taxa de sucesso, de 0 a 1. A em azul; B em preto. Cada barra tem rótulo e fração. As duas primeiras linhas são taxas de componentes fixadas, inclusive se uma componente receber peso zero.</p><table class="truth-table"><caption>Mesmas taxas internas, composições diferentes</caption><thead><tr><th>Comparação</th><th>A</th><th>B</th></tr></thead><tbody><tr><th>Peso de G=0</th><td>${a}%</td><td>${b}%</td></tr><tr><th>Taxa na mistura</th><td>${fraction(z.an,1000)}</td><td>${fraction(z.bn,1000)}</td></tr><tr><th>Peso alvo comum</th><td>${w}%</td><td>${w}%</td></tr><tr><th>Taxa padronizada</th><td>${fraction(z.ca,1000)}</td><td>${fraction(z.cb,1000)}</td></tr></tbody></table></div>`;
  return{graph,report:`Na mistura, A ${z.reversal?'fica abaixo de':'supera'} B: diferença A−B = ${fraction(z.an-z.bn,1000)}. ${z.reversal?'Há inversão em relação às duas comparações internas.':'Não há inversão neste cenário.'} Com o peso comum, A−B = 1/10. ${absent?'Há componente de peso zero: sua taxa é fornecida como hipótese, não identificada como condicional nessa população.':''}`,note:'Populações sintéticas parametrizadas, sem amostra ou inferência causal. Mover o peso muda a composição; não muda as taxas internas. O alvo comum responde a outra pergunta e não é automaticamente a comparação correta. Não há igualdade das taxas agregadas nesta grade inteira de porcentagens; o limiar exato pode ficar entre posições do controle.'};
 }}};}
 return{model,createModels};
})();
