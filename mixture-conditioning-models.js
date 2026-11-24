/* Misturas produto sintéticas, calculadas em 64 átomos equiprováveis. */
window.MixtureConditioningModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 function fraction(n,d=1){if(!d)return 'não definida';if(n===0)return '0';const g=gcd(Math.abs(n),d);return d/g===1?String(n/g):`${n/g}/${d/g}`;}
 function model(k=2,p0=1,q0=1,p1=3,q1=3){
  if(![k,p0,q0,p1,q1].every(v=>Number.isInteger(v)&&v>=0&&v<=4))throw new RangeError('Use inteiros de 0 a 4, representando quartos.');
  const component=(p,q)=>[(4-p)*(4-q),(4-p)*q,p*(4-q),p*q];
  const components=[component(p0,q0),component(p1,q1)];
  const counts=components[0].map((n,i)=>(4-k)*n+k*components[1][i]);
  const a=counts[2]+counts[3],b=counts[1]+counts[3],joint=counts[3],gap=64*joint-a*b;
  return{counts,components,a,b,joint,gap,independent:gap===0,a_given_b:b?joint/b:null,weights:[4-k,k]};
 }
 function createModels(){return{conditionalMixture:{label:'O que muda quando reunimos os grupos?',controls:[['k','Peso do grupo 1 — em quartos',0,4,1,2],['p0','P(A | grupo 0) — em quartos',0,4,1,1],['q0','P(B | grupo 0) — em quartos',0,4,1,1],['p1','P(A | grupo 1) — em quartos',0,4,1,3],['q1','P(B | grupo 1) — em quartos',0,4,1,3]],render:({k,p0,q0,p1,q1})=>{
  const r=model(k,p0,q0,p1,q1),group=(i,p,q)=>({label:`Grupo ${i} · peso ${fraction(r.weights[i],4)}`,joint:p*q/16,product:p*q/16,jointText:fraction(p*q,16),productText:fraction(p*q,16),present:r.weights[i]>0});
  const rows=[group(0,p0,q0),group(1,p1,q1),{label:'Mistura · peso 1',joint:r.joint/64,product:r.a*r.b/4096,jointText:fraction(r.joint,64),productText:fraction(r.a*r.b,4096),present:true}];
  const bars=(v,cls,label,value)=>`<div class="mixture-bar"><span>${label}</span><span class="mixture-track"><span class="${cls}" style="width:${100*v}%"></span></span><strong>${value}</strong></div>`;
  const graph='<p>Escala comum de 0 a 1. Azul contínuo: conjunta J. Preto tracejado: produto das marginais.</p><div class="mixture-comparison">'+rows.map(row=>`<div class="mixture-row"><h4>${row.label}</h4>${row.present?bars(row.joint,'mixture-joint','J',row.jointText)+bars(row.product,'mixture-product','Produto',row.productText):'<p>Grupo ausente: condicionais não definidas pela razão.</p>'}</div>`).join('')+'</div><table class="truth-table"><caption>Células da mistura — massas exatas</caption><thead><tr><th>A</th><th>B</th><th>Probabilidade</th></tr></thead><tbody>'+r.counts.map((n,i)=>`<tr><th>${i>=2?1:0}</th><td>${i%2}</td><td>${fraction(n,64)}</td></tr>`).join('')+'</tbody></table>';
  return{graph,report:`P(A)=${fraction(r.a,64)}; P(B)=${fraction(r.b,64)}. Δ=J−P(A)P(B)=${fraction(r.gap,4096)}. Na mistura: ${r.independent?'independência (igualdade exata)':'dependência'}. P(A|B)=${fraction(r.joint,r.b)}.`,note:'Cada controle indica quartos: 1 significa 1/4, 2 significa 1/2. Independência dentro dos grupos é uma hipótese. Barras são probabilidades teóricas, sem erro amostral. Parâmetros de grupo ausente não são condicionais identificáveis. A diferença não demonstra causalidade.'};
 }}};}
 return{model,fraction,createModels};
})();
