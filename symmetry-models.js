/* C2v esquemático: AB2 angular no plano xz; não calcula orbitais ou espectros. */
window.SymmetryModels=(()=>{
 const names=['E','C₂(z)','σ(xz)','σ(yz)'],signs=[[1,1,1],[-1,-1,1],[1,-1,1],[-1,1,1]];
 function valid(k){if(!Number.isInteger(k)||k<0||k>3)throw new RangeError('Operação de 0 a 3');}
 function compose(a,b){valid(a);valid(b);const s=signs[a].map((x,j)=>x*signs[b][j]);return signs.findIndex(t=>t.every((x,j)=>x===s[j]));}
 function apply(k,v){valid(k);if(v.length!==3)throw new RangeError('Três componentes');return signs[k].map((x,j)=>x*v[j]);}
 function snapshot(a,b){const k=compose(a,b),s=signs[k];return{op:k,permutation:s[0]===1?[0,1,2]:[0,2,1],probe:apply(k,[1,2,3]),determinant:s[0]*s[1]*s[2]};}
 function scene(op,center,title){
  const pts=[[0,0,0],[1,0,1],[-1,0,1]].map(v=>apply(op,v)),xy=v=>[center+74*v[0],174-74*v[2]];
  return `<text x="${center}" y="28" text-anchor="middle" font-size="21">${title}</text><line x1="${center-125}" y1="206" x2="${center+125}" y2="206" stroke="#aaa"/><text x="${center+125}" y="229" font-size="18">x</text><line x1="${center}" y1="211" x2="${center}" y2="54" stroke="#aaa" stroke-dasharray="4 4"/><text x="${center+10}" y="63" font-size="18">z</text>`+pts.slice(1).map(p=>{const [x,y]=xy(p);return `<line x1="${center}" y1="174" x2="${x}" y2="${y}" stroke="#888" stroke-width="3"/>`;}).join('')+pts.map((p,j)=>{const[x,y]=xy(p);return `<circle cx="${x}" cy="${y}" r="${j?14:18}" fill="${j?'#314cda':'#23241f'}"/><text x="${x}" y="${y-23}" text-anchor="middle" font-size="20">${['A','B₁','B₂'][j]}</text>`;}).join('');
 }
 function createModels(){return {c2vComposition:{label:'Compor operações sem confundir núcleos e espaço',controls:[['a','A depois: 0 E · 1 C₂ · 2 σxz · 3 σyz',0,3,1,1],['b','B primeiro: 0 E · 1 C₂ · 2 σxz · 3 σyz',0,3,1,2]],render:({a,b})=>{
  const q=snapshot(a,b),before=[1,2,3],mid=apply(b,before),rows=[['Inicial',before],[`Após ${names[b]}`,mid],[`Após ${names[a]}`,q.probe]];
  return{graph:`<svg class="symmetry-scene" viewBox="0 0 640 250" role="img" aria-label="Projeções xz do triátomo angular antes e depois da composição; y é zero para os núcleos"><title>AB₂ ideal antes e depois de ${names[q.op]}</title>${scene(0,155,'Inicial')}${scene(q.op,480,'Após A∘B')}<text x="320" y="143" text-anchor="middle" font-size="30">→</text></svg><table class="truth-table"><caption>Vetor-teste fora do plano: transformação em três dimensões</caption><thead><tr><th>Etapa</th><th>x</th><th>y</th><th>z</th></tr></thead><tbody>${rows.map(([label,v])=>`<tr><th>${label}</th>${v.map(x=>`<td>${x}</td>`).join('')}</tr>`).join('')}</tbody></table>`,report:`${names[a]} após ${names[b]} = ${names[q.op]}. ${q.permutation[1]===1?'B₁ e B₂ mantêm seus lugares.':'B₁ e B₂ trocam de lugar.'} Determinante espacial: ${q.determinant}. Vetor-teste final: (${q.probe.join(', ')}).`,note:'Triátomo AB₂ angular ideal, coordenadas adimensionais A=(0,0,0), B₁=(1,0,1), B₂=(−1,0,1). Esquema de simetria inspirado em moléculas como água; não representa seu ângulo medido. Plano molecular xz, eixo principal z; y sai do plano. Rótulos B₁/B₂ só acompanham núcleos equivalentes. Mesmos lugares nucleares não implicam mesma operação espacial: compare E com σxz usando o vetor-teste. Aplica B primeiro e A depois; sem movimento dinâmico, orbitais, caracteres irredutíveis ou espectros.'};
 }}};}
 return{compose,apply,snapshot,createModels};
})();
