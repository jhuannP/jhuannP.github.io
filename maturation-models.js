/* Filtro finito de hipóteses estipuladas, sem previsão imune ou afinidade. */
window.MaturationModels=(()=>{
 const HEAVY=[false,true,true,true,true,false],SELF=[[[0,0,0],[0,1,1],[1,0,1],[1,1,0],[1,1,1],[0,0,0]],[[0,0,0],[1,0,0],[1,1,0],[0,1,1],[0,1,1],[0,0,0]]];
 function choose(reactivity,edits){
  if(reactivity.length!==3||reactivity.some(x=>!Number.isInteger(x)||![0,1].includes(x))||!Number.isInteger(edits)||edits<0||edits>2)throw new RangeError('Indicadores e limite fora do domínio');
  const visited=[];
  for(let j=0;j<=edits;j++){visited.push(j);if(!reactivity[j])return{visited,last:j,passed:true,edits_used:j};}
  return{visited,last:edits,passed:false,edits_used:edits};
 }
 function model(edits=1,panel=0,cell=3){
  if(!Number.isInteger(panel)||![0,1].includes(panel)||!Number.isInteger(cell)||cell<1||cell>6)throw new RangeError('Painel ou precursor inválido');
  choose([0,0,0],edits);
  const rows=HEAVY.map((heavy,i)=>({cell:i+1,heavy,reactivity:SELF[panel][i].slice(),...(heavy?choose(SELF[panel][i],edits):{visited:[],last:null,passed:false,edits_used:0})}));
  const eligible=HEAVY.filter(Boolean).length,passed=rows.filter(r=>r.passed).length;
  return{edits,panel,cell,rows,selected:rows[cell-1],eligible,passed,unresolved:eligible-passed,excluded:6-eligible,edited_pass:rows.filter(r=>r.passed&&r.edits_used>0).length,fraction:passed/eligible,all_fraction:passed/6};
 }
 function createModels({fmt}){return{bMaturation:{label:'Edite, teste novamente e acompanhe o filtro',controls:[['edits','Alternativas de cadeia leve permitidas após L0',0,2,1,1],['panel','Painel de autoantígenos fictícios: 0 A · 1 B',0,1,1,0],['cell','Precursor em destaque',1,6,1,3]],render:({edits,panel,cell})=>{
  const s=model(edits,panel,cell),r=s.selected;
  const steps=[0,1,2].map(j=>{const seen=r.visited.includes(j);return'<div class="maturation-step '+(seen?'is-visited':'')+'"><strong>L'+j+'</strong><span>'+(seen?'s='+r.reactivity[j]:'não visitada')+'</span><small>'+(seen?(r.reactivity[j]?'reatividade estipulada':'passa o filtro'):'—')+'</small></div>';}).join('');
  const trace='<p><strong>Precursor '+cell+':</strong> '+(r.heavy?'cadeia pesada funcional estipulada. Cada L é uma cadeia leve funcional hipotética.':'não passa o checkpoint pesado estipulado; nenhuma cadeia leve é testada neste recorte.')+'</p><div class="maturation-path" role="group" aria-label="Cadeias leves testadas do precursor '+cell+'">'+steps+'</div>';
  const table='<table class="truth-table maturation-table"><caption>Coorte fictícia, sem proliferação ou tempo físico</caption><thead><tr><th>Precursor</th><th>H funcional</th><th>Última L testada</th><th>Resultado do recorte</th></tr></thead><tbody>'+s.rows.map(x=>'<tr'+(x.cell===cell?' class="is-selected"':'')+'><th>C'+x.cell+'</th><td>'+(x.heavy?'sim':'não')+'</td><td>'+(x.last===null?'nenhuma':'L'+x.last)+'</td><td>'+(x.passed?'passa filtro':x.heavy?'não resolvido':'fora do checkpoint')+'</td></tr>').join('')+'</tbody></table>';
  return{graph:trace+table,report:'Passam o filtro: '+s.passed+' de '+s.eligible+' elegíveis ('+fmt(100*s.fraction)+'%); '+s.unresolved+' com filtro não resolvido; '+s.excluded+' fora do checkpoint pesado. Em relação aos seis iniciais: '+fmt(Math.round(10000*s.all_fraction)/100)+'%. Total que passa após edição: '+s.edited_pass+'. Nenhum resultado significa célula madura ou ativada.',note:'s=0/1 é uma tabela de reatividade imposta para cada par H/L em cada painel, sem afinidade calculada. L0 é inicial; L1/L2 são alternativas em ordem fixa, sem otimização pelo antígeno. Testa-se novamente após cada troca e para-se no primeiro s=0. Os dois painéis são conjuntos fictícios de autoantígenos, não sinais de coestimulação. Todos os L candidatos são supostos funcionais; falhas iniciais de rearranjo leve não estão no algoritmo. Não resolvido não atribui automaticamente apoptose ou anergia. Sem expansão, mutação somática, troca de classe, maturação periférica ou resposta real. Material original em rascunho.'};
 }}};}
 return{HEAVY,SELF,choose,model,createModels};
})();
