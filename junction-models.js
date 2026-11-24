/* Ramos conhecidos simbolicamente; classificação não depende de tabela finita. */
window.JunctionModels=(()=>{
 function analyze(left,right,value){const bilateral=left===right?left:null;return{bilateral,category:bilateral===null?'salto':value===bilateral?'contínua':'descontinuidade removível'};}
 function createModels({plot,sample,fmt}){return{
  oneSidedJunction:{label:'Compare os dois limites com o valor no ponto',controls:[['left','Limite à esquerda',-2,2,.5,-1],['right','Limite à direita',-2,2,.5,1],['value','Valor definido f(0)',-2,2,.5,0],['power','Aproximação h=10^(−k): k',1,5,1,2]],render:({left,right,value,power})=>{
   const r=analyze(left,right,value),h=10**(-power),ymin=Math.min(left-1,right-1,value)-.5,ymax=Math.max(left,right,value)+.5,Y=y=>18+(ymax-y)/(ymax-ymin)*242;
   let graph=plot([{data:sample(x=>left+x,-1,-.0001)},{data:sample(x=>right-x,.0001,1)}],{xmin:-1,xmax:1,ymin,ymax},[[-h,left-h],[h,right-h]]);
   const holes=[...new Set([left,right])].map(y=>`<circle cx="340" cy="${Y(y)}" r="6" fill="var(--paper)" stroke="var(--blue)" stroke-width="2"/>`).join('');
   graph=graph.replace('</svg>',holes+`<circle cx="340" cy="${Y(value)}" r="4" fill="var(--blue)"/></svg>`);
   return{graph,report:`f(−h)=${fmt(left-h)}; f(h)=${fmt(right-h)}; h=${h.toExponential(0)}. Limites: ${fmt(left)} à esquerda e ${fmt(right)} à direita; f(0)=${fmt(value)}. ${r.bilateral===null?'Não existe limite real bilateral neste ponto.':`Limite bilateral=${fmt(r.bilateral)}.`} Classificação: ${r.category}.`,
    note:'Modelo em ℝ: f(x)=L₋+x para x<0; f(x)=L₊−x para x>0; valor escolhido em zero. Círculos abertos: valores de aproximação dos ramos; ponto cheio em zero: f(0). Pontos laterais mostram uma amostra. Os limites e a classificação vêm dos ramos afins conhecidos, não de testar poucos valores. Quando ambos os limites e o valor coincidem, a função é contínua, mas tem canto: derivadas laterais +1 e −1.'};
  }}
 };}
 return{createModels,analyze};
})();
