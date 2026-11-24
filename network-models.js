/* Adiciona arestas a um anel; mantém convenções e LCG compartilhados com Python. */
window.NetworkModels=(()=>{
 function ring(n){return Array.from({length:n},(_,u)=>new Set([-2,-1,1,2].map(d=>(u+d+n)%n)));}
 function network(n,extra,seed){
  if(!Number.isInteger(n)||n<8||n>40||!Number.isInteger(seed)||seed<0||seed>4294967295)throw Error('Tamanho/semente inválidos');
  const g=ring(n),c=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)if(!g[u].has(v))c.push([u,v]);
  if(!Number.isInteger(extra)||extra<0||extra>c.length)throw Error('Atalhos inválidos');
  let state=seed>>>0;for(let i=c.length-1;i>0;i--){state=(Math.imul(1664525,state)+1013904223)>>>0;const j=Math.floor(state/4294967296*(i+1));[c[i],c[j]]=[c[j],c[i]];}
  const added=c.slice(0,extra);for(const [u,v]of added){g[u].add(v);g[v].add(u);}return{g,added};
 }
 function metrics(g){
  const n=g.length;let sum=0,connected=true;const local=[];
  for(let source=0;source<n;source++){
   const d=Array(n).fill(-1),queue=[source];d[source]=0;for(let i=0;i<queue.length;i++)for(const v of g[queue[i]])if(d[v]<0){d[v]=d[queue[i]]+1;queue.push(v);}
   if(queue.length<n)connected=false;else sum+=d.reduce((a,b)=>a+b,0);
   const neighbors=[...g[source]],k=neighbors.length;let edges=0;for(let i=0;i<k;i++)for(let j=i+1;j<k;j++)if(g[neighbors[i]].has(neighbors[j]))edges++;
   local.push(k<2?0:2*edges/(k*(k-1)));
  }return{connected,mean_distance:connected?sum/(n*(n-1)):null,mean_clustering:local.reduce((a,b)=>a+b,0)/n,local_clustering:local,edges:g.reduce((s,row)=>s+row.size,0)/2};
 }
 function createModels({fmt}){return{networkShortcuts:{label:'Meça distâncias e agrupamento ao acrescentar atalhos',controls:[['n','Número de vértices',8,20,2,12],['extra','Arestas acrescentadas',0,12,1,4],['seed','Semente dos atalhos',1,100,1,42]],render:({n,extra,seed})=>{
  const base=ring(n),{g,added}=network(n,extra,seed),m=metrics(g),b=metrics(base),pos=Array.from({length:n},(_,u)=>[200+150*Math.cos(2*Math.PI*u/n-Math.PI/2),200+150*Math.sin(2*Math.PI*u/n-Math.PI/2)]);
  let drawing='';const line=(u,v,shortcut)=>`<line x1="${pos[u][0]}" y1="${pos[u][1]}" x2="${pos[v][0]}" y2="${pos[v][1]}" stroke="${shortcut?'var(--blue, #3949f5)':'currentColor'}" opacity="${shortcut?'.8':'.2'}" ${shortcut?'stroke-width="2"':''}/>`;
  for(let u=0;u<n;u++)for(const v of base[u])if(u<v)drawing+=line(u,v,false);for(const [u,v]of added)drawing+=line(u,v,true);
  for(let u=0;u<n;u++)drawing+=`<circle cx="${pos[u][0]}" cy="${pos[u][1]}" r="13" fill="var(--paper, #f6f5ed)" stroke="currentColor"/><text x="${pos[u][0]}" y="${pos[u][1]+4}" text-anchor="middle" style="font-size:11px;fill:currentColor">${u}</text>`;
  return{graph:`<svg viewBox="0 0 400 400" role="img" aria-label="Anel de quatro vizinhos com atalhos azuis">${drawing}</svg>`,report:`Arestas: ${b.edges} → ${m.edges}. Distância média L: ${fmt(b.mean_distance)} → ${fmt(m.mean_distance)}. Média do agrupamento local C: ${fmt(b.mean_clustering)} → ${fmt(m.mean_clustering)}.`,note:'Cinza: quatro vizinhos originais por vértice; azul: arestas novas. O desenho circular só organiza os nós: distância é número de arestas. L usa todos os pares distintos; C é média dos coeficientes locais. Acrescentar arestas não aumenta L, mas C pode subir ou cair. Amostra sintética finita com embaralhamento Fisher–Yates e LCG de 32 bits compartilhado com Python. Adição aumenta graus/arestas; não é religação de Watts–Strogatz nem evidência de pequeno mundo em uma rede real.'};
 }}};}return{ring,network,metrics,createModels};
})();
