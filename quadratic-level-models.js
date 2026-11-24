/* Coeficientes limitados e reais: níveis, vértice e casos degenerados. */
window.QuadraticLevelModels=(()=>{
 const clean=x=>x===0?0:x;
 function solve(a,b,c){
  if(a===0){if(b!==0)return{kind:'one',roots:[clean(-c/b)],discriminant:null};return{kind:c===0?'all':'none',roots:[],discriminant:null};}
  const d=b*b-4*a*c;if(d<0)return{kind:'none',roots:[],discriminant:d};if(d===0)return{kind:'one',roots:[clean(-b/(2*a))],discriminant:d};
  return{kind:'two',roots:[(-b-Math.sqrt(d))/(2*a),(-b+Math.sqrt(d))/(2*a)].map(clean).sort((x,y)=>x-y),discriminant:d};
 }
 function model(a=1,b=-4,c=3,level=0){
  if(![a,b,c,level].every(Number.isInteger)||a< -2||a>2||b< -4||b>4||c< -3||c>3||level< -4||level>4)throw new RangeError('Coeficientes/nível inteiros nas faixas do painel.');
  const vertex=a===0?null:[clean(-b/(2*a)),clean((4*a*c-b*b)/(4*a))],image=a===0?(b?'all':'constant'):(a>0?'lower':'upper');
  return{vertex,image,bound:vertex?vertex[1]:b===0?c:null,zeros:solve(a,b,c),level:solve(a,b,c-level),window:a?[vertex[0]-3,vertex[0]+3]:[-4,4]};
 }
 function createModels({plot,sample,fmt}){return{quadraticShape:{label:'Que entradas levam à altura escolhida?',controls:[['a','Coeficiente a',-2,2,1,1],['b','Coeficiente b',-4,4,1,-4],['c','Coeficiente c',-3,3,1,3],['level','Altura da reta y=L',-4,4,1,0]],render:({a,b,c,level=0})=>{
  const r=model(a,b,c,level),[xmin,xmax]=r.window,f=x=>a*x*x+b*x+c,data=sample(f,xmin,xmax),special=[0,level,f(xmin),f(xmax),...(r.vertex?[r.vertex[1]]:[])],low=Math.min(...special),high=Math.max(...special),ymin=Math.floor(low-1),ymax=ymin+4*Math.ceil((high-low+2)/4);
  if(r.vertex)data.push(r.vertex);data.sort((p,q)=>p[0]-q[0]);
  const visible=r.level.roots.filter(x=>x>=xmin&&x<=xmax),points=visible.map(x=>[x,level]);
  let graph=plot([{data:[[xmin,level],[xmax,level]],style:'reference'},{data}],{xmin,xmax,ymin,ymax},points).replace('<svg ','<svg class="quadratic-level-plot" ');
  if(r.vertex){const[x,y]=r.vertex,xx=58+(x-xmin)/(xmax-xmin)*564,yy=260-(y-ymin)/(ymax-ymin)*242,tangent=r.level.kind==='one'&&Math.abs(x-r.level.roots[0])<1e-12;
   graph=graph.replace('</svg>',`<path d="M${xx},${yy-6} l6,6 -6,6 -6,-6 Z" fill="#f4f4e9" stroke="#171814" stroke-width="2"/><text x="${xx+10}" y="${yy+(a>0?-14:24)}">${tangent?(level===0?'V=raiz':'V na reta'):'V'}</text></svg>`);
  }
  const describe=t=>t.kind==='all'?'todos os reais (ℝ)':t.kind==='none'?'nenhuma entrada real':`${t.kind==='one'?'uma entrada real':'duas entradas reais'}: ${t.roots.map(fmt).join('; ')}`;
  const image=r.image==='all'?'ℝ':r.image==='constant'?`{${fmt(r.bound)}}`:r.image==='lower'?`[${fmt(r.bound)}, +∞)`:`(−∞, ${fmt(r.bound)}]`;
  graph=`<p>Azul: f(x)=ax²+bx+c. Tracejado: y=${fmt(level)}. Círculos azuis: interseções visíveis; losango preto: vértice, quando existe. Eixos x e f(x).</p>`+graph+`<table class="truth-table"><caption>Resumo algébrico — domínio ℝ</caption><thead><tr><th>Pergunta</th><th>Resposta</th></tr></thead><tbody><tr><th>Vértice da parábola</th><td>${r.vertex?`(${r.vertex.map(fmt).join('; ')}) — ${a>0?'mínimo':'máximo'}`:'não se aplica: a=0'}</td></tr><tr><th>Imagem de f</th><td>${image}</td></tr><tr><th>Zeros de f (altura 0)</th><td>${describe(r.zeros)}</td></tr><tr><th>Entradas na altura ${fmt(level)}</th><td>${describe(r.level)}</td></tr><tr><th>Δ para a altura L</th><td>${a?r.level.discriminant:'não aplicado: a=0'}</td></tr></tbody></table>`;
  return{graph,report:`${a?'Função quadrática.':'a=0: a expressão não é quadrática.'} ${r.level.kind==='all'?'A função coincide com a reta escolhida.':`${visible.length} de ${r.level.roots.length} interseções isoladas dentro da janela.`} Alterar L muda a pergunta f(x)=L; não muda a função.`,note:`Janela x∈[${fmt(xmin)}; ${fmt(xmax)}], escolhida para visualização; o domínio continua ℝ. Raízes podem estar fora dela. Vértice também é raiz somente quando sua altura é zero; se V está na reta L≠0, é interseção com esse nível, não zero de f. Valores e exemplos são próprios; programação é opcional.`};
 }}};}
 return{model,solve,createModels};
})();
