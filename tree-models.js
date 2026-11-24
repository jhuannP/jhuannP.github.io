/* Mesmas chaves, ordens distintas: nenhuma rotação automática. */
window.TreeModels=(()=>{
 const orders=[[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[4,2,6,1,3,5,7]];
 function build(mode,count,target){
  let root=null;const nodes=[];
  for(const key of orders[mode].slice(0,count)){const node={key,left:null,right:null};nodes.push(node);if(!root){root=node;continue;}let current=root;while(true){const side=key<current.key?'left':'right';if(!current[side]){current[side]=node;break;}current=current[side];}}
  const sorted=nodes.map(n=>n.key).sort((a,b)=>a-b);let height=0;
  const locate=(n,depth)=>{if(!n)return;n.x=80*n.key;n.y=40+depth*48;height=Math.max(height,depth+1);locate(n.left,depth+1);locate(n.right,depth+1)};locate(root,0);
  let current=root;const visited=[];let found=false;
  while(current){visited.push(current.key);if(current.key===target){found=true;break;}current=target<current.key?current.left:current.right;}
  return{root,nodes,report:{altura:height,em_ordem:sorted,encontrada:found,visitados:visited}};
 }
 function createModels(){return{binaryTreeShape:{label:'Compare a forma da árvore e o caminho de busca',controls:[['mode','Ordem: 0 crescente · 1 decrescente · 2 medianas',0,2,1,2],['count','Chaves inseridas',0,7,1,7],['target','Chave procurada',0,8,1,7]],render:({mode,count,target})=>{
  const result=build(mode,count,target),r=result.report;
  let drawing='';for(const node of result.nodes)for(const child of [node.left,node.right])if(child)drawing+=`<line x1="${node.x}" y1="${node.y}" x2="${child.x}" y2="${child.y}" stroke="currentColor" opacity="0.35"/>`;
  for(const node of result.nodes){const active=r.visitados.includes(node.key);drawing+=`<circle cx="${node.x}" cy="${node.y}" r="19" fill="${active?'var(--blue, #3949f5)':'var(--paper, #f6f5ed)'}" stroke="currentColor"/><text x="${node.x}" y="${node.y+5}" text-anchor="middle" style="fill:${active?'white':'currentColor'}">${node.key}</text>`;}
  if(!count)drawing='<text x="320" y="180" text-anchor="middle">Árvore vazia</text>';
  return{graph:`<svg viewBox="0 0 640 370" role="img" aria-label="Árvore binária de busca com nós visitados destacados">${drawing}</svg>`,report:`Altura em nós=${r.altura}; tamanho=${count}. Busca por ${target}: ${r.encontrada?'encontrada':'ausente'}; nós visitados=${r.visitados.length}; caminho=${r.visitados.join(' → ')||'nenhum'}. Em ordem: ${r.em_ordem.join(', ')||'vazio'}.`,note:'Círculos azuis são nós visitados; linhas ligam pai e filhos. Posições horizontais seguem as chaves e a vertical segue a profundidade, sem unidades físicas. Altura da árvore vazia=0; raiz sozinha=1. As três ordens contêm o mesmo conjunto completo de sete chaves. “Medianas” produz uma forma equilibrada para este exemplo; a estrutura não se balanceia automaticamente. A busca ausente termina num ramo vazio, sem contar esse vazio como nó.'};
 }}};}return{build,createModels};
})();
