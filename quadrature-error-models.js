/* Referência analítica, erro com sinal e contraste de regularidade. */
window.QuadratureErrorModels=(()=>{
 const fun=(family,x)=>family===0?x**4:Math.abs(x-.3);
 function model(family=0,level=2){
  if(!Number.isInteger(family)||![0,1].includes(family)||!Number.isInteger(level)||level<1||level>6)throw new RangeError('family0/1;level1..6');
  const n=2**level,h=1/n,values=Array.from({length:n+1},(_,i)=>fun(family,i*h));let t=(values[0]+values[n])/2,s=values[0]+values[n];
  for(let i=1;i<n;i++){t+=values[i];s+=(i%2?4:2)*values[i];}
  const trapezoid=h*t,simpson=h*s/3,integral=family===0?.2:.29;
  return{family,level,n,h,values,trapezoid,simpson,integral,et:trapezoid-integral,es:simpson-integral,bound_t:family===0?1/n**2:null,bound_s:family===0?2/(15*n**4):null};
 }
 function createModels({plot}){return{quadratureError:{label:'Refinar a malha não substitui a hipótese',controls:[['family','Função (0=x⁴;1=|x−0,3|)',0,1,1,0],['level','Refinamento k (n=2ᵏ)',1,6,1,2]],render:({family,level})=>{
  const r=model(family,level),xs=Array.from({length:161},(_,j)=>j/160),curve=xs.map(x=>[x,fun(family,x)]),trap=r.values.map((v,i)=>[i*r.h,v]),quad=xs.map(x=>{const i=Math.min(r.n-2,2*Math.floor(x/(2*r.h))),u=(x-i*r.h)/(2*r.h),value=r.values[i]*2*(u-.5)*(u-1)-r.values[i+1]*4*u*(u-1)+r.values[i+2]*2*u*(u-.5);return[x,value];}),prec=x=>x.toFixed(9).replace('.',','),sci=x=>x.toExponential(3).replace('.',',');
  const graph='<div class="quadrature-error-plot">'+plot([{data:curve},{data:trap,style:'reference'},{data:quad,style:'secondary'}],{xmin:0,xmax:1,ymin:-.05,ymax:1.05})+'</div>'+`<p class="caption">Horizontal: x; vertical: f(x), grandezas adimensionais. Azul: função. Tracejado preto: interpolação linear dos trapézios. Roxo pontilhado: interpolação quadrática usada em blocos de Simpson. São gráficos dos integrandos/interpolantes, não dos erros. Curvas podem ficar sobrepostas; a tabela explicita os resultados.</p><table class="truth-table quadrature-error-table"><caption>I=${r.integral.toFixed(2).replace('.',',')}; erro assinado e=regra−I</caption><thead><tr><th>Regra</th><th>Valor</th><th>e</th></tr></thead><tbody><tr><th>Trapézio</th><td>${prec(r.trapezoid)}</td><td>${sci(r.et)}</td></tr><tr><th>Simpson</th><td>${prec(r.simpson)}</td><td>${sci(r.es)}</td></tr></tbody></table>`;
  return{graph,report:`n=${r.n} subintervalos; ${r.n+1} nós; h=1/${r.n}. ${family===0?'f=x⁴: limites clássicos |eT|≤'+sci(r.bound_t)+' e |eS|≤'+sci(r.bound_s)+'.':'f=|x−0,3|: quina no intervalo; não aplicamos os limites que exigem C²/C⁴. Simpson pode ficar abaixo da integral.'}`,note:'Integração em [0,1], malha uniforme, n par. I analítica: 1/5 para x⁴; 29/100 para |x−0,3|. Constantes e curvas são construções didáticas. Erros pequenos usam notação científica; diferença entre malhas não é automaticamente erro verdadeiro. O laboratório racional separa truncamento de arredondamento; navegador usa ponto flutuante.'};
 }}};}
 return{model,createModels};
})();
