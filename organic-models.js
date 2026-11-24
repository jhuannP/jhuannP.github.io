/* Representações CHO selecionadas; não prevê estabilidade ou estereoquímica. */
window.OrganicModels=(()=>{
 const molecules=[{"name":"Etanol","group":"álcool","atoms":["C","C","O"],"bonds":[[0,1,1],[1,2,1]],"xy":[[90,150],[230,90],[370,150]]},{"name":"Éter dimetílico","group":"éter","atoms":["C","O","C"],"bonds":[[0,1,1],[1,2,1]],"xy":[[90,150],[230,90],[370,150]]},{"name":"Propanal","group":"aldeído","atoms":["C","C","C","O"],"bonds":[[0,1,1],[1,2,1],[2,3,2]],"xy":[[65,180],[175,120],[285,180],[395,120]]},{"name":"Propanona","group":"cetona","atoms":["C","C","C","O"],"bonds":[[0,1,1],[1,2,1],[1,3,2]],"xy":[[80,180],[230,120],[380,180],[230,32]]},{"name":"Ácido etanoico","group":"ácido carboxílico","atoms":["C","C","O","O"],"bonds":[[0,1,1],[1,2,2],[1,3,1]],"xy":[[75,170],[220,110],[220,25],[370,170]]},{"name":"Metanoato de metila","group":"éster","atoms":["C","O","O","C"],"bonds":[[0,1,2],[0,2,1],[2,3,1]],"xy":[[75,115],[75,25],[225,175],[375,115]]}];
 function analyze(atoms,bonds){
  const n=atoms.length;if(!n||atoms.some(a=>!['C','O'].includes(a)))throw new RangeError('Átomos C/O');
  const used=Array(n).fill(0),edges=new Set(),adj=Array.from({length:n},()=>[]);
  for(const[i,j,o]of bonds){if(![i,j,o].every(Number.isInteger)||i<0||j<0||i>=n||j>=n||i===j||![1,2,3].includes(o))throw new RangeError('Ligação');const key=[i,j].sort((a,b)=>a-b).join(',');if(edges.has(key))throw new RangeError('Duplicada');edges.add(key);used[i]+=o;used[j]+=o;adj[i].push(j);adj[j].push(i);}
  const seen=new Set([0]),stack=[0];while(stack.length){for(const j of adj[stack.pop()])if(!seen.has(j)){seen.add(j);stack.push(j);}}if(seen.size!==n)throw new RangeError('Desconectado');
  const hydrogens=atoms.map((a,i)=>(a==='C'?4:2)-used[i]);if(hydrogens.some(x=>x<0))throw new RangeError('Valência');const C=atoms.filter(x=>x==='C').length,O=atoms.filter(x=>x==='O').length,H=hydrogens.reduce((a,b)=>a+b,0),part=(s,n)=>n?s+(n===1?'':n):'';
  return{hydrogens,C,H,O,formula:part('C',C)+part('H',H)+part('O',O),dbe:(2*C+2-H)/2};
 }
 function isomorphic(a,b){
  if([...a.atoms].sort().join()!=[...b.atoms].sort().join())return false;
  const edgeString=(bonds,p)=>bonds.map(([i,j,o])=>[...([p[i],p[j]].sort((a,b)=>a-b)),o].join(',')).sort().join(';'),target=edgeString(b.bonds,b.atoms.map((_,i)=>i));let yes=false;
  function visit(p,left){if(yes)return;if(!left.length){if(edgeString(a.bonds,p)===target)yes=true;return;}const i=p.length;for(const j of left)if(a.atoms[i]===b.atoms[j])visit([...p,j],left.filter(k=>k!==j));}
  visit([],b.atoms.map((_,i)=>i));return yes;
 }
 function drawing(m,q,mode){
  const lines=m.bonds.map(([i,j,o])=>{const[x1,y1]=m.xy[i],[x2,y2]=m.xy[j],dx=x2-x1,dy=y2-y1,len=Math.hypot(dx,dy),nx=-dy/len,ny=dx/len;return Array.from({length:o},(_,k)=>{const shift=(k-(o-1)/2)*7;return `<line x1="${x1+nx*shift}" y1="${y1+ny*shift}" x2="${x2+nx*shift}" y2="${y2+ny*shift}" stroke="#23241f" stroke-width="3"/>`;}).join('');}).join('');
  const labels=m.atoms.map((a,i)=>{if(mode===1&&a==='C')return '';const h=q.hydrogens[i],label=a+(h?'H'+(h===1?'':h):''),[x,y]=m.xy[i];return `<rect x="${x-31}" y="${y-17}" width="62" height="34" fill="#f4f3eb"/><text x="${x}" y="${y+7}" text-anchor="middle">${label}</text>`;}).join('');
  return `<svg class="organic-scene" viewBox="0 0 460 240" role="img" aria-label="${m.name}, representação ${mode?'esquelética':'com grupos condensados'}"><title>${m.name}: mesma conectividade em outra notação</title>${lines}${labels}${m.xy.map(([x,y],i)=>`<text class="atom-index" x="${x+26}" y="${y+32}">${i+1}</text>`).join('')}</svg>`;
 }
 function createModels(){return{organicConnectivity:{label:'A fórmula conta átomos; o desenho informa conexões',controls:[['pair','Par: 0 álcool/éter · 1 aldeído/cetona · 2 ácido/éster',0,2,1,0],['which','Estrutura: 0 primeira · 1 segunda',0,1,1,0],['mode','Notação: 0 grupos · 1 esquelética',0,1,1,0]],render:({pair,which,mode})=>{const index=2*pair+which,m=molecules[index],other=molecules[2*pair+1-which],q=analyze(m.atoms,m.bonds),r=analyze(other.atoms,other.bonds),same=isomorphic(m,other);
  return{graph:drawing(m,q,mode)+`<table class="truth-table"><caption>Hidrogênios por átomo — números indicados no desenho</caption><thead><tr><th>Átomo</th>${m.atoms.map((a,i)=>`<th>${i+1}: ${a}</th>`).join('')}</tr></thead><tbody><tr><th>H</th>${q.hydrogens.map(h=>`<td>${h}</td>`).join('')}</tr></tbody></table>`,report:`${m.name}: ${q.formula}; grupo ${m.group}. Hidrogênios totais: ${q.H}; índice de insaturação CHO: ${q.dbe}. No par, ${other.name} tem ${r.formula}. Grafos com elementos e ordens de ligação: ${same?'iguais':'diferentes'}.`,note:'Seis exemplos selecionados, neutros e de camada fechada; só C/H/O. Notação 0 mostra grupos condensados, não todos os átomos de H; notação 1 omite C e H ligados a C, mas mostra O/OH. Carbonos estão nas pontas e vértices não rotulados. Coordenadas são disposição gráfica, não ângulos ou energia. Contagem por valência não prova estabilidade nem resolve estereoquímica; classificação funcional destes exemplos foi curada, não inferida para moléculas gerais.'};
 }}};}
 return{molecules,analyze,isomorphic,createModels};
})();
