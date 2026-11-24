/* Contabilidade de Lewis para dois pares curados; não simula alternância temporal. */
window.ResonanceModels=(()=>{
 const valence={C:4,N:5,O:6};
 function audit(atoms,hydrogens,bonds,pairs,charge){
  const n=atoms.length;if(!n||hydrogens.length!==n||pairs.length!==n||atoms.some(a=>!(a in valence))||!Number.isInteger(charge)||[...hydrogens,...pairs].some(x=>!Number.isInteger(x)||x<0))throw new RangeError('C/N/O e contagens inteiras');
  const orders=[...hydrogens],seen=new Set();
  for(const[i,j,b]of bonds){if(![i,j,b].every(Number.isInteger)||i<0||j<0||i>=n||j>=n||i===j||![1,2,3].includes(b))throw new RangeError('Ligação inválida');const key=[i,j].sort((a,b)=>a-b).join(',');if(seen.has(key))throw new RangeError('Ligação duplicada');seen.add(key);orders[i]+=b;orders[j]+=b}
  const formal=atoms.map((a,i)=>valence[a]-2*pairs[i]-orders[i]),local=pairs.map((v,i)=>2*(v+orders[i]));
  const electrons=2*(bonds.reduce((s,b)=>s+b[2],0)+hydrogens.reduce((s,v)=>s+v,0)+pairs.reduce((s,v)=>s+v,0)),target=atoms.reduce((s,a)=>s+valence[a],0)+hydrogens.reduce((s,v)=>s+v,0)-charge,total_charge=formal.reduce((s,v)=>s+v,0);
  return{orders,formal,local,electrons,target,total_charge,electron_ok:electrons===target,charge_ok:total_charge===charge,octet_ok:local.every(x=>x===8)};
 }
 function model(family=0,form=0){
  if(![0,1].includes(family)||![0,1,2].includes(form))throw new RangeError('Família 0/1 e forma 0/1/2');
  const atoms=['C','C','O',family===0?'O':'N'],hydrogens=[3,0,0,family===0?0:2],orders=form===0?[2,1]:form===1?[1,2]:[2,2],pairs=[0,0,form===1?3:2,family===0?(form===0?3:2):(form===0?1:0)],bonds=[[0,1,1],[1,2,orders[0]],[1,3,orders[1]]],charge=family===0?-1:0;
  return{family,form,atoms,hydrogens,bonds,pairs,charge,formula:family===0?'C2H3O2−':'C2H5NO',...audit(atoms,hydrogens,bonds,pairs,charge)};
 }
 function drawing(s,arrows){
  const xy=[[65,165],[220,165],[220,65],[365,225]],text=['CH₃','C','O',s.family===0?'O':'NH₂'];
  let body=s.bonds.map(([i,j,b])=>{const[x1,y1]=xy[i],[x2,y2]=xy[j],dx=x2-x1,dy=y2-y1,d=Math.hypot(dx,dy);return Array.from({length:b},(_,k)=>{const z=(k-(b-1)/2)*8;return `<line x1="${x1-dy/d*z}" y1="${y1+dx/d*z}" x2="${x2-dy/d*z}" y2="${y2+dx/d*z}" class="res-bond"/>`}).join('')}).join('');
  body+=xy.map(([x,y],i)=>`<rect x="${x-(i===0||i===3?38:18)}" y="${y-22}" width="${i===0||i===3?76:36}" height="44" fill="#f4f3eb"/><text x="${x}" y="${y+11}" text-anchor="middle" class="res-atom">${text[i]}</text><text x="${x-28}" y="${y+37}" class="res-index">${i+1}</text>${s.formal[i]?`<text x="${i===3?420:x+53}" y="${y-20}" class="res-charge">${s.formal[i]>0?'+':'−'}</text>`:''}`).join('');
  for(const i of [2,3]){const centers=i===2?[[256,65],[220,26],[184,65]]:[[410,225],[365,267],[365,184]];for(let k=0;k<s.pairs[i];k++){const[x,y]=centers[k],horizontal=(i===2&&k===1)||(i===3&&k>0);for(const off of [-4,4])body+=`<circle cx="${x+(horizontal?off:0)}" cy="${y+(horizontal?0:off)}" r="2.7" class="res-electron"/>`}}
  if(arrows&&s.form!==2){const paths=s.form===0?['M410 225 Q407 152 300 191','M212 115 Q155 111 184 68']:['M184 65 Q145 96 208 113',s.family===0?'M292 201 Q327 133 365 181':'M292 194 Q366 150 410 222'];body+=paths.map(d=>`<path d="${d}" class="res-arrow" marker-end="url(#res-pair-arrow)"/>`).join('')}
  return `<svg class="resonance-scene" viewBox="0 0 460 315" role="img" aria-label="${s.family===0?'Acetato':'Acetamida'}, ${s.form===2?'teste inválido de dez elétrons no carbono 2':'contribuinte '+(s.form===0?'A':'B')}; valores e pares livres na tabela"><title>Posições nucleares fixas; só representação eletrônica muda</title><defs><marker id="res-pair-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#3049d1"/></marker></defs>${body}</svg>`;
 }
 function createModels(){return{resonanceBookkeeping:{label:'Conte elétrons antes de aceitar o desenho',controls:[['family','Exemplo: 0 acetato · 1 acetamida',0,1,1,0],['form','Desenho: 0 contribuinte A · 1 contribuinte B · 2 teste inválido',0,2,1,0],['arrows','Setas de pares A↔B: 0 ocultar · 1 mostrar',0,1,1,1]],render:({family,form,arrows})=>{
  const s=model(family,form),name=family===0?'Acetato':'Acetamida';
  const table=`<table class="truth-table resonance-table"><caption>B = soma das ordens de ligação, incluindo H; L = pares livres; CF = carga formal</caption><thead><tr><th>Átomo</th><th>B</th><th>L</th><th>CF</th></tr></thead><tbody>${s.atoms.map((a,i)=>`<tr><th>${i+1}: ${a}</th><td>${s.orders[i]}</td><td>${s.pairs[i]}</td><td>${s.formal[i]>0?'+':''}${s.formal[i]}</td></tr>`).join('')}</tbody></table>`;
  return{graph:`<p><strong>${name} · ${form===2?'teste inválido':'contribuinte '+(form===0?'A':'B')}</strong>. H ligados aos mesmos átomos em todos os desenhos. Pontos: elétrons não ligantes; duas setas azuis: redistribuição formal simultânea de dois pares, sem eixo de tempo. ${form===2?'Setas ocultas: não se propõe esta figura como contribuinte aceitável.':''}</p>`+drawing(s,arrows)+table,
  report:`${s.formula}: ${s.electrons} elétrons de valência (esperados ${s.target}); soma CF=${s.total_charge}. Elétrons ao redor de 1/2/3/4: ${s.local.join(' / ')}. ${form===2?'Inválido neste recorte: carbono 2 com dez elétrons; conservar a carga e o inventário não basta.':family===0?'Os dois contribuintes selecionados são relacionados pela troca dos oxigênios equivalentes no modelo ideal. Nenhum deles é uma espécie separada.':'A e B não são equivalentes: B separa cargas O−/N+. Não se atribuem pesos iguais nem percentuais; o programa só confere contabilidade.'}`,
  note:'Átomos C/N/O de segunda linha, H condensados, camada fechada e dois exemplos curados. CF=valência−2L−B; carga formal não é carga parcial medida. Os pontos e índices são contabilidade, não órbitas ou geometria otimizada. A↔B relaciona desenhos do mesmo sistema; não é equilíbrio, reação ou movimento nuclear. O teste 2 viola o octeto máximo do carbono. Conservar elétrons e octetos não prova estabilidade, pesos de contribuintes, pKa ou energia. Nenhum dado experimental ou resultado da IC.'};
 }}}}
 return{audit,model,createModels};
})();
