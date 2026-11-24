/* Mapeamento exato de duas fitas; origem sintética só entra na curva de referência. */
window.ReadMappingModels=(()=>{
 const REFERENCES=['ATGCCGTACGATTCAGGCTAACGT','ACGTTAGCTGCAACGTTAGCTGCA'],STARTS=[0,4,8,12,16],COMPLEMENT={A:'T',C:'G',G:'C',T:'A'};
 function dna(s){if(typeof s!=='string'||!s||/[^ACGT]/.test(s))throw new RangeError('DNA ACGT maiúsculo não vazio');return s;}
 function revcomp(s){return [...dna(s)].reverse().map(c=>COMPLEMENT[c]).join('');}
 function locate(reference,query){
  dna(reference);dna(query);const rc=revcomp(query),hits=[];
  for(let start=0;start<=reference.length-query.length;start++){
   const fragment=reference.slice(start,start+query.length),strands=[];
   if(fragment===query)strands.push('+');if(fragment===rc)strands.push('-');
   if(strands.length)hits.push({start,end:start+query.length,strands});
  }return hits;
 }
 function coverage(intervals,n){const a=Array(n).fill(0);for(const[start,end]of intervals){if(!Number.isInteger(start)||!Number.isInteger(end)||start<0||start>=end||end>n)throw new RangeError('Intervalo inválido');for(let i=start;i<end;i++)a[i]++;}return a;}
 function model(genome=1,length=6,read=3){
  if(!Number.isInteger(genome)||![0,1].includes(genome)||!Number.isInteger(length)||length<4||length>8||!Number.isInteger(read)||read<1||read>5)throw new RangeError('Controles fora do domínio');
  const reference=REFERENCES[genome],rows=STARTS.map((origin,i)=>{const origin_strand=i%2===0?'+':'-',fragment=reference.slice(origin,origin+length),query=origin_strand==='+'?fragment:revcomp(fragment),hits=locate(reference,query);return{read:i+1,query,origin,origin_strand,hits,unique:hits.length===1};});
  const truth=coverage(STARTS.map(s=>[s,s+length]),reference.length),unique=rows.filter(r=>r.unique),retained=coverage(unique.map(r=>[r.hits[0].start,r.hits[0].end]),reference.length);
  return{genome,length,read,reference,rows,selected:rows[read-1],truth,retained,unique_count:unique.length,ambiguous_count:5-unique.length,mean_truth:truth.reduce((a,b)=>a+b,0)/reference.length,mean_retained:retained.reduce((a,b)=>a+b,0)/reference.length};
 }
 function createModels({plot,fmt}){return{readMapping:{label:'Mapeie leituras e compare a cobertura recuperada',controls:[['genome','Referência: 0 A · 1 B com bloco repetido',0,1,1,1],['length','Comprimento de cada leitura, em bases',4,8,1,6],['read','Leitura em destaque',1,5,1,3]],render:({genome,length,read})=>{
  const s=model(genome,length,read),r=s.selected,step=a=>a.flatMap((v,i)=>[[i,v],[i+1,v]]);
  const graph=plot([{data:step(s.truth),style:'reference'},{data:step(s.retained)}],{xmin:0,xmax:24,ymin:0,ymax:3}).replace('<svg ','<svg class="read-mapping-scene" ');
  const seq='<div class="read-reference" role="group" aria-label="Referência de 24 bases com índices de zero a 23">'+[...s.reference].map((c,i)=>'<span><small>'+i+'</small><strong>'+c+'</strong></span>').join('')+'</div>';
  const hits='<table class="truth-table"><caption>Todos os intervalos exatos para R'+read+'; origem não fornecida ao buscador</caption><thead><tr><th>Intervalo [a,b)</th><th>Fita(s)</th><th>Trecho da referência</th></tr></thead><tbody>'+r.hits.map(h=>'<tr><td>['+h.start+','+h.end+')</td><td>'+h.strands.join(' / ')+'</td><td><code>'+s.reference.slice(h.start,h.end)+'</code></td></tr>').join('')+'</tbody></table>';
  const values='<details><summary>Valores da cobertura por base</summary><table class="truth-table"><caption>Contagens sintéticas; índice da base com início zero</caption><thead><tr><th>Base</th><th>Gerada</th><th>Retida</th></tr></thead><tbody>'+s.truth.map((v,i)=>'<tr><th>'+i+'</th><td>'+v+'</td><td>'+s.retained[i]+'</td></tr>').join('')+'</tbody></table></details>';
  return{graph:'<p><strong>Referência sintética '+('AB'[genome])+', escrita 5′→3′.</strong></p>'+seq+'<p><strong>R'+read+' lida 5′→3′: <code>'+r.query+'</code></strong>. Origem conhecida só pelo gerador: ['+r.origin+','+(r.origin+length)+'), fita '+r.origin_strand+'.</p>'+hits+'<p><strong>Horizontal: coordenada entre bases; vertical: número de leituras por base.</strong> Preto tracejado: cobertura das origens conhecidas. Azul: só leituras com intervalo único; se coincidem, o azul recobre o preto.</p>'+graph+values,report:'Cinco leituras: '+s.unique_count+' com intervalo único; '+s.ambiguous_count+' com múltiplos intervalos. R'+read+': '+r.hits.length+' intervalo(s) candidato(s). Cobertura média gerada='+fmt(s.mean_truth)+'; retida='+fmt(s.mean_retained)+'. Média gerada=5×'+length+'/24. Zero retido pode resultar de ambiguidade, sem ausência de DNA.',note:'Duas referências inventadas de 24 bases, cinco origens fixas 0/4/8/12/16, comprimentos 4..8 e fitas alternadas. Busca todas as correspondências exatas nas duas orientações, sem usar a origem. Palíndromo pode ter +/− no mesmo intervalo e conta uma vez na cobertura; unicidade aqui é de intervalo, não de orientação. Multimapeadas são descartadas nesta política didática, sem escolha arbitrária ou soma em todos os locais. Sem erros, N, gaps, qualidade, paired-end, variantes, genes ou dados de pessoas. Não executa FASTQ, SAM/BAM, montagem ou um alinhador real.'};
 }}};}
 return{REFERENCES,STARTS,revcomp,locate,coverage,model,createModels};
})();
