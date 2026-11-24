/* Enumeração e reamostragem sintéticas: mesmas posições e gerador no Python. */
window.BootstrapModels=(()=>{
 const presets=[[0,2],[0,0,2],[0,1,1,4],[2,2,2]];
 function statistic(data,kind){if(kind===0)return data.reduce((s,x)=>s+x,0)/data.length;const v=[...data].sort((a,b)=>a-b),n=v.length;return n%2?v[Math.floor(n/2)]:(v[n/2-1]+v[n/2])/2;}
 function percentile(values,numerator){const v=[...values].sort((a,b)=>a-b),index=Math.max(0,Math.ceil(numerator*v.length/40)-1);return v[index];}
 function summarize(values,observed){const n=values.length,mean=values.reduce((s,x)=>s+x,0)/n,variance=values.reduce((s,x)=>s+(x-mean)**2,0)/n,masses=new Map();for(const x of values)masses.set(x,(masses.get(x)||0)+1/n);return{mean,bias:mean-observed,variance,sampleVariance:n===1?null:variance*n/(n-1),lower:percentile(values,1),upper:percentile(values,39),masses};}
 function exact(data,kind){const values=[],current=[];function visit(){if(current.length===data.length){values.push(statistic(current,kind));return;}for(const x of data){current.push(x);visit();current.pop();}}visit();const result=summarize(values,statistic(data,kind));delete result.sampleVariance;return result;}
 function monteCarlo(data,kind,count,seed){let state=seed>>>0;const n=data.length,bucket=Math.floor(4294967296/n),limit=bucket*n;function index(){do{state=(Math.imul(1664525,state)+1013904223)>>>0;}while(state>=limit);return Math.floor(state/bucket);}const values=Array.from({length:count},()=>statistic(Array.from({length:n},()=>data[index()]),kind));return summarize(values,statistic(data,kind));}
 function createModels({plot,fmt}){return{
  bootstrapCompare:{label:'Compare enumeração exata e réplicas bootstrap',controls:[['scenario','Conjunto de dados (0 a 3)',0,3,1,0],['kind','Estatística: 0 média, 1 mediana',0,1,1,0],['count','Número de réplicas B',20,1000,20,200],['seed','Semente da reamostragem',1,100,1,42]],render:({scenario,kind,count,seed})=>{
   const data=presets[scenario],e=exact(data,kind),m=monteCarlo(data,kind,count,seed),support=[...e.masses.keys()].sort((a,b)=>a-b),xmin=support[0]-.25,xmax=support.at(-1)+.25,ymax=Math.max(...e.masses.values(),...m.masses.values())*1.2;
   const series=[...support.map(x=>({data:[[x,0],[x,e.masses.get(x)]]})),...support.map(x=>({data:[[x,0],[x,m.masses.get(x)||0]],style:'reference'}))];
   return{graph:`<p class="caption">Dados observados sintéticos: [${data.join('; ')}]. Estatística: ${kind===0?'média':'mediana'}.</p>`+plot(series,{xmin,xmax,ymin:0,ymax}),
    report:`Enumeração: ${data.length**data.length} sequências; E*[T*]=${fmt(e.mean)}; viés bootstrap=${fmt(e.bias)}; SE exato=${fmt(Math.sqrt(e.variance))}. Monte Carlo: média=${fmt(m.mean)}; SE estimado=${fmt(Math.sqrt(m.sampleVariance))}. Percentis 2,5%/97,5%: exato [${fmt(e.lower)}; ${fmt(e.upper)}], réplicas [${fmt(m.lower)}; ${fmt(m.upper)}].`,
    note:'Hastes azuis: massas bootstrap exatas; pontilhadas: frequências das réplicas. São massas discretas, não densidade contínua. Enumeração preserva posições repetidas; reamostragem tem reposição e tamanho n. SE exato usa a distribuição completa; SE Monte Carlo usa divisor B−1. Percentis usam a inversa da CDF empírica, sem interpolação; não garantem cobertura de 95% na população. Gerador congruencial didático com escolha por faixas e rejeição, compartilhado com Python; reprodutibilidade não comprova qualidade estatística. Mais réplicas reduzem erro Monte Carlo, sem criar novos dados. Dados constantes podem gerar SE zero sem provar variância populacional nula.'};
  }}
 };}
 return{presets,statistic,exact,monteCarlo,createModels};
})();
