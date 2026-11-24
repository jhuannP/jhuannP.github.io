/* Energia de uma mola ideal; ponto candidato, não uma integração temporal. */
window.SpringPotentialModels=(()=>{
 function model(q=0,c=0){
  if(!Number.isInteger(q)||q< -150||q>150||!Number.isInteger(c)||c< -10||c>10)throw new RangeError('Posição em centésimos e constante em joules fora do contrato.');
  const x=q/100,u=4*x*x+c,e=4+c,difference=(40000-4*q*q)/10000,allowed=difference>=0;
  return{x,u,e,difference,allowed,kinetic:allowed?difference:null,speed:allowed?Math.sqrt(difference):null,force:q===0?0:-8*x};
 }
 function createModels({plot,fmt}){return{springPotential:{label:'Mudar o zero não muda o movimento',controls:[['q','Posição x — centésimos de metro',-150,150,25,0],['c','Constante C — em joules',-10,10,1,0]],render:({q,c})=>{
  const z=model(q,c),curve=Array.from({length:121},(_,i)=>{const x=-1.5+i/40;return[x,4*x*x+c];});
  const graph=plot([{data:curve},{data:[[-1.5,z.e],[1.5,z.e]],style:'reference'}],{xmin:-1.5,xmax:1.5,ymin:-10,ymax:20},[[z.x,z.u]])+
   '<p class="caption">Horizontal: posição x (m). Vertical: energia (J), escala fixa de −10 a 20 J. Azul: U(x); tracejado preto: E. O ponto marca o potencial na posição candidata, inclusive quando ela é proibida para esta energia. Não representa uma trajetória. Os cruzamentos ocorrem em x=−1 m e x=1 m.</p>'+
   `<table class="truth-table"><caption>Mola ideal: m=2 kg, k=8 N/m, amplitude 1 m</caption><tbody><tr><th>Posição candidata</th><td>${fmt(z.x)} m</td></tr><tr><th>Potencial U</th><td>${fmt(z.u)} J</td></tr><tr><th>Energia E</th><td>${fmt(z.e)} J</td></tr><tr><th>Diferença E−U</th><td>${fmt(z.difference)} J</td></tr><tr><th>Rapidez permitida</th><td>${z.allowed?fmt(z.speed)+' m/s':'nenhuma neste modelo'}</td></tr><tr><th>Força F(x)</th><td>${fmt(z.force)} N</td></tr></tbody></table>`;
  return{graph:`<div class="spring-potential-panel">${graph}</div>`,report:z.allowed?`Posição permitida. K=${fmt(z.kinetic)} J; rapidez ${fmt(z.speed)} m/s. ${z.kinetic===0?'Ponto de retorno: velocidade zero, força diferente de zero.':'O sinal da velocidade não é determinado pela energia.'} ${z.e<0?'E é negativa por escolha do zero; isso não impede o movimento.':''}`:`Posição proibida para E=${fmt(z.e)} J: E−U=${fmt(z.difference)} J é negativo e não pode ser energia cinética. Não há rapidez real a apresentar.`,note:'Mola e massa ideais em movimento horizontal 1D, referencial inercial, sem dissipação ou trabalho externo adicional. C desloca U e E pela mesma constante; preserva K, força e rapidez. O gráfico compara posições e não calcula tempos ou sentido do movimento. A mola parabólica não cobre potenciais com vários poços ou barreiras.'};
 }}};}
 return{model,createModels};
})();
