/* Geometrias MA2B2 ideais: permutações induzidas por rotações próprias. */
window.CoordinationIsomerModels=(()=>{
 const points=[[[1,0,0],[0,1,0],[-1,0,0],[0,-1,0]],[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]];
 const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
 const det=m=>m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]);
 const apply=(m,v)=>m.map(row=>row.reduce((s,x,i)=>s+x*v[i],0));
 const key=v=>v.join(',');
 function rotations(g){
  const out=[];
  for(const a of [0,1,2])for(const b of [0,1,2])for(const c of [0,1,2]){
   if(new Set([a,b,c]).size!==3)continue;
   for(const x of [-1,1])for(const y of [-1,1])for(const z of [-1,1]){
    const axes=[a,b,c],signs=[x,y,z],matrix=axes.map((k,i)=>[0,1,2].map(j=>j===k?signs[i]:0));
    if(det(matrix)!==1)continue;
    const permutation=points[g].map(v=>points[g].findIndex(w=>key(w)===key(apply(matrix,v))));
    if(permutation.every(i=>i>=0))out.push({permutation,matrix});
   }
  }
  return out.sort((a,b)=>key(a.permutation).localeCompare(key(b.permutation)));
 }
 const groups=[rotations(0),rotations(1)];
 function model(geometry=0,pair=0,rotation=0){
  if(![geometry,pair,rotation].every(Number.isInteger)||geometry<0||geometry>1||pair<0||pair>5||rotation<0||rotation>11)throw new RangeError('Geometria 0/1, par 0..5 e rotação 0..11.');
  const group=groups[geometry];rotation=Math.min(rotation,group.length-1);
  const {permutation,matrix}=group[rotation],[a,b]=pairs[pair];
  const orbit=[...new Set(group.map(r=>key([r.permutation[a],r.permutation[b]].sort())))].sort().map(v=>v.split(',').map(Number));
  const dot=points[geometry][a].reduce((s,x,i)=>s+x*points[geometry][b][i],0),normSquared=geometry?3:1,cosine=dot/normSquared;
  return{geometry,pair,rotation,permutation,moved_pair:[permutation[a],permutation[b]].sort(),orbit,group_size:group.length,orbit_size:orbit.length,stabilizer:group.length/orbit.length,dot,norm_squared:normSquared,cosine,angle:Math.acos(cosine)*180/Math.PI,label:geometry?'uma classe tetraédrica':dot===0?'cis':'trans',positions:points[geometry].map(v=>apply(matrix,v))};
 }
 function createModels(){return{coordinationIsomers:{label:'Girar o desenho cria outro arranjo?',controls:[['geometry','Geometria: 0 quadrado-planar; 1 tetraédrica',0,1,1,0],['pair','Par de sítios para A — 0 a 5',0,5,1,0],['rotation','Rotação própria da estrutura inteira',0,7,1,0]],render:({geometry,pair,rotation})=>{
  const r=model(geometry,pair,rotation),fmt=n=>n.toLocaleString('pt-BR',{maximumFractionDigits:3});
  const project=v=>geometry?[300+95*v[0],185-95*(2*v[1]-v[2])/Math.sqrt(5)]:[300+130*v[0],185-130*v[1]];
  const xy=r.positions.map(project),isA=i=>pairs[pair].includes(i);
  const svg=`<svg class="coordination-scene" viewBox="110 -10 380 405" role="img" aria-label="${geometry?'Projeção esquemática tetraédrica':'Vista frontal quadrado-planar'} de MA₂B₂. Classe ${r.label}. A ocupa os sítios ${r.moved_pair.map(i=>i+1).join(' e ')} após a rotação.">${xy.map(([x,y],i)=>`<line x1="300" y1="185" x2="${x}" y2="${y}" class="coordination-bond ${geometry&&r.positions[i][1]+2*r.positions[i][2]<0?'coordination-back':''}"/>`).join('')}<circle cx="300" cy="185" r="22" class="coordination-metal"/><text x="300" y="192" text-anchor="middle">M</text>${xy.map(([x,y],i)=>`<circle cx="${x}" cy="${y}" r="22" class="coordination-${isA(i)?'a':'b'}"/><text x="${x}" y="${y+7}" text-anchor="middle" class="coordination-label-${isA(i)?'a':'b'}">${isA(i)?'A':'B'}</text><text x="${x}" y="${y<185?y-34:y+43}" text-anchor="middle" class="coordination-site">sítio ${r.permutation[i]+1}</text>`).join('')}</svg>`;
  const graph=`<p><strong>${geometry?'Tetraédrica ideal':'Quadrado-planar ideal'} · ${r.label}</strong></p>${svg}<p class="caption">A azul e B claro são tipos de ligantes monodentados pontuais. Sítios são posições, não identidades distintas de ligantes. ${geometry?'Projeção ortográfica: os ângulos na tela não são os espaciais. Ligações tracejadas apontam para trás da tela; contínuas, para frente. O traço não indica força de ligação.':'Vista frontal do plano de coordenação.'}</p><table class="truth-table"><caption>Classificação por rotações próprias — todos os seis pares</caption><thead><tr><th>Par inicial de sítios A</th><th>Classe</th><th>Desenhos equivalentes</th></tr></thead><tbody>${pairs.map((p,i)=>{const t=model(geometry,i,0);return`<tr class="${i===pair?'selected':''}"><th>${p.map(x=>x+1).join(' e ')}</th><td>${geometry?'única':t.label}</td><td>${t.orbit_size}</td></tr>`}).join('')}</tbody></table>`;
  return{graph,controlRanges:{rotation:{max:r.group_size-1,value:r.rotation}},report:`Par inicial A: ${pairs[pair].map(i=>i+1).join(' e ')}. Após a rotação: ${r.moved_pair.map(i=>i+1).join(' e ')}. Ângulo A–M–A=${fmt(r.angle)}°. ${r.group_size} rotações do esqueleto: órbita com ${r.orbit_size} pares e estabilizador com ${r.stabilizer} operações. ${r.orbit_size} × ${r.stabilizer} = ${r.group_size}.`,note:'São seis escolhas de dois sítios, não seis isômeros. O controle muda uma orientação por rotação rígida, sem trocar ligações individualmente. O grupo é do esqueleto sem cores; operações que preservam as cores formam o estabilizador. Não há previsão de energia, mecanismo, abundância, quiralidade de ligantes reais ou existência experimental.'};
 }}};}
 return{model,rotations,createModels};
})();
