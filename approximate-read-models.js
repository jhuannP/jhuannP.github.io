/* Busca exaustiva sem gaps; modelo de substituição hipotético, sem MAPQ. */
window.ApproximateReadModels=(()=>{
 const reference='ACGTTACGAT',reads=['CGTT','GGTT','CGCT','CCCC','ACGT'];
 function dna(s){if(typeof s!=='string'||s.length<1||s.length>256||/[^ACGT]/.test(s))throw new RangeError('DNA ACGT maiúsculo, 1..256 bases');return s;}
 const revcomp=s=>dna(s).split('').reverse().map(c=>({A:'T',C:'G',G:'C',T:'A'}[c])).join('');
 function search(ref,read,limit=1,q=20){
  dna(ref);dna(read);if(!Number.isInteger(limit)||limit<0||limit>read.length||![10,20,30,40].includes(q))throw new RangeError('Limite inteiro válido e Q10/20/30/40');
  const p=10**(-q/10),rows=[];
  for(let start=0;start<=ref.length-read.length;start++)for(const [strand,query] of [['+',read],['-',revcomp(read)]]){
   const fragment=ref.slice(start,start+read.length),differences=[];
   for(let j=0;j<query.length;j++)if(query[j]!==fragment[j])differences.push(j);
   const cost=differences.length;rows.push({start,end:start+query.length,strand,query,fragment,differences,cost,likelihood:(1-p)**(query.length-cost)*(p/3)**cost,accepted:cost<=limit});
  }
  const minimum=rows.length?Math.min(...rows.map(r=>r.cost)):null,accepted=rows.filter(r=>r.accepted),best=accepted.filter(r=>r.cost===minimum);
  return{rows,accepted,best,minimum,oriented_count:best.length,interval_count:new Set(best.map(r=>r.start+':'+r.end)).size,p,expected_errors:read.length*p};
 }
 function model(kind=1,limit=1,q=20){if(!Number.isInteger(kind)||kind<0||kind>4)throw new RangeError('Leitura 0..4');return{reference,read:reads[kind],...search(reference,reads[kind],limit,q)};}
 const precise=v=>v<.001?v.toExponential(3).replace('.',','):v.toLocaleString('pt-BR',{maximumSignificantDigits:6});
 function createModels({fmt}){return{approximateRead:{label:'Uma discrepância não decide a origem',controls:[['kind','Leitura: 0 exata · 1 troca · 2 empate · 3 ausente · 4 palíndromo',0,4,1,1],['limit','Máximo de discrepâncias aceitas',0,2,1,1],['q','Q hipotético igual em todas as bases',10,40,10,20]],render:({kind,limit,q})=>{
  const s=model(kind,limit,q),shown=s.best.slice(0,3),height=shown.length?130+shown.length*65:105;
  let scene=`<svg class="approximate-read-scene" viewBox="0 0 600 ${height}" role="img" aria-label="Referência nas posições 1 a 10 e melhores comparações aceitas; X marca discrepância. Todos os candidatos na tabela abaixo.">`;
  for(let j=0;j<10;j++)scene+=`<text x="${55+50*j}" y="25" text-anchor="middle">${j+1}</text><text x="${55+50*j}" y="67" text-anchor="middle">${reference[j]}</text>`;
  scene+='<line x1="30" y1="83" x2="545" y2="83" class="plot-grid"/>';
  shown.forEach((r,i)=>{const y=125+i*65;scene+=`<text x="12" y="${y}">${r.strand}</text><text x="565" y="${y}" text-anchor="middle">d=${r.cost}</text>`;for(let j=0;j<4;j++){const x=55+50*(r.start+j),bad=r.differences.includes(j);scene+=`<text x="${x}" y="${y}" text-anchor="middle"${bad?' fill="var(--blue)"':''}>${r.query[j]}</text>`;if(bad)scene+=`<text x="${x}" y="${y+24}" text-anchor="middle" fill="var(--blue)">×</text>`;}});
  scene+='</svg>';
  const rows=s.rows.map(r=>`<tr><th>[${r.start+1},${r.end}] ${r.strand}</th><td>${r.cost}</td><td>${r.accepted?(r.cost===s.minimum?'Melhor':'Aceita'):'Fora'}</td><td>${precise(r.likelihood)}</td></tr>`).join('');
  const table='<details><summary>Comparar todas as 14 candidatas orientadas</summary><div class="approximate-read-table" role="region" aria-label="Candidatas sem gaps" tabindex="0"><table class="truth-table"><caption>Posições inclusivas; verossimilhança P(letras | janela, modelo), sem posterior</caption><thead><tr><th>Posição/fita</th><th>d</th><th>Corte</th><th>Verossim.</th></tr></thead><tbody>'+rows+'</tbody></table></div></details>';
  return{graph:`<p>Leitura observada: ${s.read}. Referência escrita 5′→3′; posições 1 a 10. As linhas abaixo mostram ${shown.length} de ${s.oriented_count} melhores candidatas aceitas; “−” usa o complemento reverso da leitura. × marca uma letra diferente.</p>`+scene+table,report:`Menor custo entre todas as janelas=${s.minimum}; corte=${limit}. Aceitas=${s.accepted.length}; melhores orientadas=${s.oriented_count}; intervalos distintos entre as melhores=${s.interval_count}. ${s.oriented_count===0?'Nenhuma candidata passa pelo corte.':s.interval_count===1?(s.oriented_count===1?'Intervalo e orientação únicos neste modelo.':'Intervalo único; orientação ambígua.'):'Empate de posições: não escolher uma origem.'} p de erro por base=${fmt(s.p)}; erros esperados na leitura=${fmt(s.expected_errors)}.`,note:'Busca sem gaps e sem recorte, com ACGT, referência de dez bases e leitura de quatro. Qualidades homogêneas hipotéticas. Verossimilhança assume erros independentes e cada substituição errada com chance p/3; não é P(origem | leitura), MAPQ ou evidência de variante. Q altera a verossimilhança, mas não o custo nem os empates neste modelo. Sem dados reais ou inferência de expressão.'};
 }}};}
 return{search,model,revcomp,createModels};
})();
