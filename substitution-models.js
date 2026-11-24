/* Mudança afim: orientação e fator da cadeia, inclusive mapa constante. */
window.SubstitutionModels=(()=>{
 function experiment(alpha,b){return{upper:1+alpha*b,integral:((1+alpha*b)**3-1)/3,expanded:alpha*b+alpha**2*b*b+alpha**3*b**3/3};}
 function createModels({plot,sample,fmt}){return{linearSubstitution:{label:'Veja o fator da transformação e a orientação',controls:[['alpha','Taxa da mudança α',-3,3,.5,2],['b','Fronteira final em x',0,2,.1,1]],render:({alpha,b})=>{
  const r=experiment(alpha,b),end=Math.max(.1,b),curve=sample(x=>alpha*(1+alpha*x)**2,0,end),ys=curve.map(p=>p[1]),lo=Math.min(0,...ys),hi=Math.max(0,...ys),pad=Math.max(1,.1*(hi-lo));
  return{graph:plot([{data:curve}],{xmin:0,xmax:end,ymin:lo-pad,ymax:hi+pad},[[b,alpha*(1+alpha*b)**2]]),report:`u=1+αx; du/dx=${fmt(alpha)}. Fronteiras em x: 0 → ${fmt(b)}; em u: 1 → ${fmt(r.upper)}. Integral em x e em u=${fmt(r.integral)}. ${alpha<0?'Orientação invertida: a integral em u vai do valor maior ao menor.':alpha===0?'Mapa constante: intervalo em u colapsa e o integrando em x é zero.':'Orientação preservada.'}`,note:'Eixo horizontal x; vertical integrando α(1+αx)², não a função acumulada. Modelo f(u)=u², u=1+αx; em x precisamos do fator α. A curva e o ponto mostram o integrando, não uma estimativa da integral. Resultado usa a referência exata F(u)=u³/3. α=0 satisfaz a identidade da cadeia, mas não define uma mudança inversível para integrais gerais. Nenhum algoritmo simbólico geral é executado.'};
 }}};}return{experiment,createModels};
})();
