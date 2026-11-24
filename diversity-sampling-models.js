/* Coleções de 12 indivíduos; riqueza de prefixo fixo e esperança uniforme distintas. */
window.DiversitySamplingModels=(()=>{
 const populations=[[6,3,2,1],[3,3,3,3],[9,1,1,1]];
 function choose(n,k){if(k<0||k>n)return 0;let v=1;for(let i=1;i<=Math.min(k,n-k);i++)v=v*(n-i+1)/i;return Math.round(v);}
 function expectation(counts,n){const total=counts.reduce((a,b)=>a+b,0),den=choose(total,n),detection=counts.map(k=>1-choose(total-k,n)/den);return{detection,expected:detection.reduce((a,b)=>a+b,0),total_subsets:den};}
 function model(population=0,n=4,order=0){
  if(!Number.isInteger(population)||population<0||population>2||!Number.isInteger(order)||order<0||order>2||!Number.isInteger(n)||n<0||n>12)throw new RangeError('Coleção/ordem 0..2 e amostra 0..12 inteiros');
  const counts=populations[population],labels=counts.flatMap((v,i)=>Array(v).fill(i));let indices=[];
  if(order===0)indices=Array.from({length:12},(_,i)=>i);
  else if(order===1){const offsets=counts.map((_,i)=>counts.slice(0,i).reduce((a,b)=>a+b,0));for(let j=0;j<Math.max(...counts);j++)for(let i=0;i<4;i++)if(j<counts[i])indices.push(offsets[i]+j);}
  else indices=[0,6,1,9,7,2,11,3,8,10,4,5];
  const selected=indices.slice(0,n).map(i=>labels[i]),observed=counts.map((_,i)=>selected.filter(v=>v===i).length),r=expectation(counts,n);
  return{counts:[...counts],indices,selected,observed,richness:observed.filter(k=>k>0).length,rare_in_sample:observed[3]>0,rare_probability:r.detection[3],expected:r.expected,total_subsets:r.total_subsets};
 }
 function createModels({plot,fmt}){return{diversitySampling:{label:'Não apareceu: ausência ou amostragem?',controls:[['population','Coleção: 0 desigual · 1 equilibrada · 2 concentrada',0,2,1,0],['n','Indivíduos examinados — n',0,12,1,4],['order','Ordem ilustrativa: 0 agrupada · 1 alternada · 2 fixa',0,2,1,0]],render:({population,n,order})=>{
  const s=model(population,n,order),expected=[],example=[];
  for(let k=0;k<=12;k++){expected.push([k,model(population,k,order).expected]);example.push([k,model(population,k,order).richness]);}
  let graph=plot([{data:example,style:'reference'},{data:expected}],{xmin:0,xmax:12,ymin:0,ymax:4},[[n,s.expected]]);
  graph=graph.replace('<svg ','<svg class="diversity-sampling-scene" ').replace('viewBox="0 0 640 300"','viewBox="-20 0 680 310"');
  const table='<table class="truth-table"><caption>Contagens conhecidas somente neste gerador</caption><thead><tr><th>Categoria</th><th>Coleção</th><th>Amostra</th></tr></thead><tbody>'+s.counts.map((count,i)=>`<tr><th>${'ABCD'[i]}</th><td>${count}</td><td>${s.observed[i]}</td></tr>`).join('')+'</tbody></table>';
  return{graph:'<p>Horizontal: n inteiro, de 0 a 12 indivíduos. Vertical: número de categorias, de 0 a 4. Azul: riqueza esperada sob sorteio uniforme sem reposição. Preto tracejado: prefixos da ordem ilustrativa escolhida. Linhas só guiam a leitura entre tamanhos inteiros.</p>'+graph+table,report:`n=${n}; riqueza do exemplo=${s.richness}; riqueza esperada=${fmt(s.expected)}. ${s.total_subsets===1?'Existe 1 subconjunto':'Existem '+s.total_subsets+' subconjuntos'} de tamanho n. Sob sorteio uniforme: P(D aparecer)=${fmt(s.rare_probability)}. No exemplo escolhido, D ${s.rare_in_sample?'aparece':'não aparece'}.`,note:'N=12, categorias A–D inventadas e identificadas sem erro; todas as coleções têm quatro categorias. Ordens fixas são exemplos deliberados, não sorteios nem réplicas independentes. A curva azul conhece a composição inteira e não estima categorias desconhecidas. Indivíduos não são leituras de sequenciamento. Sem detecção imperfeita, viés de extração/PCR, estrutura espacial ou inferência de ausência absoluta.'};
 }}};}
 return{model,createModels};
})();
