/* Riscos de estimadores calculados na distribuição binomial sintética. */
window.EstimationModels=(()=>{
 function varianceRisk(n,p){
  const masses=window.ProbabilityModels.binomial(n,p),target=p*(1-p);
  function risk(divisor){const values=masses.map((_,k)=>k*(n-k)/(n*divisor)),mean=values.reduce((s,x,k)=>s+x*masses[k],0),bias=mean-target;
   return{mean,bias,variance:values.reduce((s,x,k)=>s+(x-mean)**2*masses[k],0),mse:values.reduce((s,x,k)=>s+(x-target)**2*masses[k],0)};}
  return{target,biased:risk(n),unbiased:risk(n-1)};
 }
 function createModels({fmt}){return{
 varianceEstimators:{label:'Compare duas regras para estimar a variância',controls:[['n','Tamanho da amostra iid',2,12,1,4],['p','Parâmetro Bernoulli p',.1,.9,.1,.5]],render:({n,p})=>{
  const r=varianceRisk(n,p),rows=[['Esperança','mean'],['Viés','bias'],['Variância do estimador','variance'],['Erro quadrático médio','mse']];
  return{graph:`<table class="truth-table"><caption>Riscos calculados sobre todas as amostras possíveis</caption><thead><tr><th>Grandeza</th><th>Divisor n</th><th>Divisor n−1</th></tr></thead><tbody>${rows.map(([label,key])=>`<tr><th scope="row">${label}</th><td>${fmt(r.biased[key])}</td><td>${fmt(r.unbiased[key])}</td></tr>`).join('')}</tbody></table>`,
   report:`Variância populacional do modelo: p(1−p)=${fmt(r.target)}. ${r.biased.mse<r.unbiased.mse?'Neste caso, o divisor n tem menor erro quadrático médio, apesar do viés.':'Compare erro quadrático médio, viés e variância: nenhum rótulo resolve sozinho a escolha.'}`,
   note:'Modelo Bernoulli iid com p conhecido para avaliar as regras, não para estimar a partir de dados reais. A tabela soma as massas binomiais de todas as contagens de sucesso. Viés e MSE são propriedades do procedimento em repetições; não são o erro conhecido de uma única amostra. Números na tela são arredondados.'};
 }}}; }
 return{createModels,varianceRisk};
})();
