/* Modelos sintéticos: teste normal planejado e associação linear. */
window.InferenceModels=(()=>{
 function testNormal(z,side,alpha){
  const cdf=window.LimitModels.normalCDF(z),p=side===0?2*(1-window.LimitModels.normalCDF(Math.abs(z))):side===1?1-cdf:cdf;
  return{p,reject:p<=alpha};
 }
 function covarianceExample(a,b,c){
  const xs=[-2,-1,0,1,2],ys=xs.map(x=>a*x+b*x*x+c),mx=0,my=ys.reduce((s,y)=>s+y,0)/5;
  const vx=2,vy=ys.reduce((s,y)=>s+(y-my)**2,0)/5,cov=xs.reduce((s,x,i)=>s+(x-mx)*(ys[i]-my),0)/5;
  return{xs,ys,mx,my,vx,vy,cov,rho:vy===0?null:cov/Math.sqrt(vx*vy),slope:cov/vx};
 }
 function createModels({plot,sample,fmt}){
  return{
   normalTestTail:{label:'Compare a cauda do teste e o nível escolhido',controls:[['z','Estatística observada z',-4,4,.1,2],['side','Cauda: 0 bilateral, 1 direita, 2 esquerda',0,2,1,0],['alpha','Nível α',.01,.1,.01,.05]],render:({z,side,alpha})=>{
    const phi=window.LimitModels.phi,r=testNormal(z,side,alpha),xmin=-4,xmax=4,ymax=.48;
    const tails=side===0?[[-4,-Math.abs(z)],[Math.abs(z),4]]:side===1?[[z,4]]:[[-4,z]];
    const X=x=>58+(x+4)/8*564,Y=y=>18+(ymax-y)/ymax*242;
    const fill=tails.filter(([lo,hi])=>lo<hi).map(([lo,hi])=>{
     const points=[[lo,0],...sample(phi,lo,hi,100),[hi,0]].map(([x,y])=>`${X(x)},${Y(y)}`).join(' ');
     return`<polygon points="${points}" fill="var(--blue)" opacity=".18"/>`;
    }).join('');
    const graph=plot([{data:sample(phi,xmin,xmax)},{data:[[z,0],[z,phi(z)]],style:'reference'}],{xmin,xmax,ymin:0,ymax},[[z,phi(z)]]).replace(/(<svg[^>]*>)/,`$1${fill}`);
    const type=['bilateral','à direita','à esquerda'][side];
    return{graph,report:`Teste ${type}; p-valor≈${fmt(r.p)}; α=${fmt(alpha)}. Pelo critério p≤α, ${r.reject?'rejeitaria':'não rejeitaria'} H₀ neste modelo.`,note:'Sob H₀, Z tem distribuição normal padrão, com σ conhecido no teste de média correspondente. Preenchimento: parte da cauda escolhida dentro da janela [−4;4]; o p-valor inclui caudas fora dela e usa a CDF numérica conferida. Alterar α não altera o p-valor; altera o critério. Escolher cauda após ver o resultado não preserva automaticamente o erro planejado. Não é probabilidade posterior de H₀ nem decisão científica da IC.'};
   }},
   covarianceShape:{label:'Explore associação linear e dependência não linear',controls:[['a','Coeficiente linear a',-2,2,.5,0],['b','Coeficiente quadrático b',0,2,.5,1],['c','Deslocamento c',-3,3,.5,0]],render:({a,b,c})=>{
    const r=covarianceExample(a,b,c),ymin=Math.min(...r.ys)-1,ymax=Math.max(...r.ys)+1;
    return{graph:plot([{data:sample(x=>a*x+b*x*x+c,-2,2)},{data:[[-2,r.my-2*r.slope],[2,r.my+2*r.slope]],style:'reference'}],{xmin:-2.5,xmax:2.5,ymin,ymax},r.xs.map((x,i)=>[x,r.ys[i]])),
     report:`E[X]=0; E[Y]=${fmt(r.my)}; Var(X)=2; Var(Y)=${fmt(r.vy)}; Cov(X,Y)=${fmt(r.cov)}. ${r.rho===null?'Correlação não definida: Var(Y)=0.':`Correlação ρ=${fmt(r.rho)}.`} Inclinação da melhor reta=${fmt(r.slope)}.`,
     note:'Modelo finito: X equiprovável em {−2;−1;0;1;2} e Y=aX+bX²+c. Pontos: suporte conjunto; curva: função escolhida entre os pontos, sem massa contínua adicional. Reta pontilhada: melhor aproximação linear em erro quadrático no modelo. a=0,b>0 dá covariância zero com dependência determinística; a=b=0 dá Y constante e correlação indefinida. Deslocar c não muda covariância ou correlação. O desenho não prova causalidade.'};
   }}
  };
 }
 return{createModels,testNormal,covarianceExample};
})();
