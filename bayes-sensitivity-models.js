/* Sensibilidade de Bayes: parâmetros inteiros em porcentagem; sem amostragem. */
window.BayesSensitivityModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const fraction=(n,d)=>{if(!d)return 'não definida';if(!n)return '0';const g=gcd(n,d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;};
 function model(p=10,a=80,b=20){
  if([p,a,b].some(x=>!Number.isInteger(x)||x<0||x>100))throw new RangeError('Parâmetros inteiros de 0 a 100.');
  const h=p*a,n=(100-p)*b,m=h+n;
  return{p,a,b,h,n,m,mass:m/10000,posterior:m?h/m:null};
 }
 function createModels({plot,fmt}){return{bayesSensitivity:{label:'Quanto o resultado depende das hipóteses?',controls:[['p','Prior P(H) — em %',0,100,5,10],['a','Taxa P(S|H) — em %',0,100,5,80],['b','Taxa P(S|Hᶜ) — em %',0,100,5,20]],render:({p,a,b})=>{
  const z=model(p,a,b),curve=Array.from({length:101},(_,i)=>model(i,a,b)).filter(x=>x.posterior!==null).map(x=>[x.p/100,x.posterior]);
  const graph=(curve.length?plot([{data:[[0,0],[1,1]],style:'reference'},{data:curve}],{xmin:0,xmax:1,ymin:0,ymax:1},z.posterior===null?[]:[[p/100,z.posterior]]):'<p><strong>Sinal impossível para qualquer prior.</strong> As duas taxas são zero; não há curva posterior.</p>')+
   '<p class="caption">Horizontal: prior P(H), de 0 a 1. Vertical: posterior P(H|S), de 0 a 1. Azul: taxas fixadas nos controles; tracejado preto: posterior igual ao prior. O ponto marca o prior selecionado. Pontos de massa zero são omitidos, sem preencher por limite.</p>'+
   `<table class="truth-table"><caption>Massas no prior selecionado</caption><thead><tr><th>Origem</th><th>Com o sinal S</th></tr></thead><tbody><tr><th>H</th><td>${fraction(z.h,10000)}</td></tr><tr><th>Hᶜ</th><td>${fraction(z.n,10000)}</td></tr><tr><th>Total P(S)</th><td>${fraction(z.m,10000)}</td></tr></tbody></table>`;
  return{graph:`<div class="bayes-sensitivity-panel">${graph}</div>`,report:z.m?`Posterior: ${fraction(z.h,z.m)} (≈ ${fmt(z.posterior)}). Prior: ${fraction(p,100)}. Divida a massa da linha H pelo total. ${a===b?'Taxas iguais: o sinal mantém o prior.':a>b?'O sinal favorece H quando o prior é interior.':'O sinal favorece Hᶜ quando o prior é interior.'}`:'P(S)=0 no prior selecionado. Posterior não definido; isto não significa probabilidade zero.',note:'Parâmetros sintéticos escolhidos, sem dados ou estimação. O controle 10 significa 10%=1/10. A curva compara cenários; não é uma trajetória temporal nem um intervalo de confiança. Taxas do grupo ausente são parâmetros fornecidos, não condicionais identificadas nesse grupo.'};
 }}};}
 return{model,createModels};
})();
