/* Exp em zero; cota analítica e estimativa numérica do resto são objetos distintos. */
window.TaylorRemainderModels=(()=>{
 function factorial(n){let a=1;for(let j=2;j<=n;j++)a*=j;return a;}
 function polynomial(x,n){let t=1,s=1;for(let k=1;k<=n;k++){t*=x/k;s+=t;}return s;}
 function tail(x,n){if(x===0)return 0;let t=x**(n+1)/factorial(n+1),s=t;for(let k=n+2;k<n+82;k++){t*=x/k;s+=t;}return s;}
 function uniformBound(n,rho){return Math.exp(rho)*rho**(n+1)/factorial(n+1);}
 function requiredDegree(rho,epsilon){for(let n=0;n<=40;n++)if(uniformBound(n,rho)<=epsilon)return n;throw new RangeError('Grau acima da busca');}
 function model(n=2,rho=1,u=.1,p=4){
  if(!Number.isInteger(n)||n<0||n>12||!Number.isInteger(p)||p<2||p>6||!Number.isFinite(rho)||rho<.25||rho>1||!Number.isFinite(u)||u<-1||u>1)throw new RangeError('Controles fora do domínio');
  const x=rho*u,P=polynomial(x,n),R=tail(x,n),local_bound=Math.exp(Math.max(0,x))*Math.abs(x)**(n+1)/factorial(n+1),uniform_bound=uniformBound(n,rho),epsilon=10**(-p);
  return{n,rho,u,p,x,polynomial:P,remainder:R,local_bound,uniform_bound,epsilon,required:requiredDegree(rho,epsilon),certified:uniform_bound<=epsilon,normalized:R/uniform_bound};
 }
 function createModels({plot,sample,fmt}){return{taylorRemainder:{label:'Escolha um grau e confira a cota no intervalo',controls:[['N','Grau N do polinômio',0,12,1,2],['rho','Raio ρ do intervalo [−ρ,ρ]',.25,1,.25,1],['u','Posição relativa u; x=ρu',-1,1,.1,.1],['p','Tolerância ε=10^(−p)',2,6,1,4]],render:({N,rho,u,p})=>{
  const s=model(N,rho,u,p),B=s.uniform_bound,point=x=>Math.exp(Math.max(0,x))*Math.abs(x)**(N+1)/factorial(N+1),num=x=>x===0?'0':Math.abs(x)<.001?x.toExponential(3).replace('.',','):fmt(x);
  const graph=plot([{data:[[-rho,1],[rho,1]],style:'taylor-uniform'},{data:[[-rho,-1],[rho,-1]],style:'taylor-uniform'},{data:sample(x=>point(x)/B,-rho,rho),style:'reference'},{data:sample(x=>-point(x)/B,-rho,rho),style:'reference'},{data:sample(x=>tail(x,N)/B,-rho,rho)}],{xmin:-rho,xmax:rho,ymin:-1.2,ymax:1.2},[[s.x,s.normalized]]).replace('<svg ','<svg class="taylor-remainder-scene" ');
  const table='<table class="truth-table"><caption>Valores em x='+fmt(s.x)+'; o resto é uma estimativa numérica</caption><thead><tr><th>P_N(x)</th><th>R com sinal</th><th>Cota no ponto</th><th>Cota uniforme</th></tr></thead><tbody><tr><td>'+num(s.polynomial)+'</td><td>'+num(s.remainder)+'</td><td>'+num(s.local_bound)+'</td><td>'+num(B)+'</td></tr></tbody></table>';
  return{graph:'<p><strong>Horizontal: x em [−ρ,ρ]; vertical: resto dividido pela cota uniforme B.</strong> Azul: R/B. Preto tracejado: ±cota do ponto/B. Cinza pontilhado: ±1, os limites uniformes. A escala é normalizada a cada mudança de grau ou raio.</p>'+graph+table,report:'Expansão de exp em zero. ε='+num(s.epsilon)+'. Menor grau que esta cota suficiente aceita no intervalo: '+s.required+'. Grau escolhido '+N+': '+(s.certified?'a cota uniforme atende ε.':'a cota uniforme ainda não atende ε; isso não prova que o erro real exceda ε.')+' A posição escolhida não muda o grau requerido para o intervalo.',note:'Exp é suave, |x|≤ρ≤1, ρ≥0,25. A cota no ponto usa e^max(0,x)|x|^(N+1)/(N+1)!; a uniforme usa e^ρρ^(N+1)/(N+1)!. O resto desenhado soma 81 termos da cauda para evitar cancelamento de exp(x)−P_N(x), mas continua numérico. A justificativa da cota vem do teorema, não do gráfico ou dessa soma. Não é aritmética intervalar certificada em máquina, nem garantia de erro total de um programa. Cinza/azul e tabela têm significados explícitos; não comparar alturas normalizadas como erros absolutos entre graus.'};
 }}};}
 return{factorial,polynomial,tail,uniformBound,requiredDegree,model,createModels};
})();
