/* Deslizamento à direita até a primeira parada; nenhuma lei de atrito estático. */
window.SlidingWorkModels=(()=>{
 function model(m=2,v0=3,force=2,friction=5,distance=2){
  const vals=[m,v0,force,friction,distance],limits=[[1,4],[1,6],[0,8],[0,8],[0,12]];
  if(vals.some((v,i)=>!Number.isInteger(v)||v<limits[i][0]||v>limits[i][1]))throw new RangeError('Parâmetros inteiros nos limites dos controles.');
  const k0=m*v0*v0/2,net=force-friction,stop=net<0?k0/-net:null;
  const reachable=k0+net*distance>=0,end=stop===null?distance:Math.min(distance,stop),k=Math.max(0,k0+net*end);
  return{m,v0,force,friction,distance,k0,net,stop,reachable,query_k:reachable?k0+net*distance:null,end,k,speed:Math.sqrt(2*k/m),applied:force*end,friction_work:friction*end===0?0:-friction*end,net_work:net*end,internal:friction*end};
 }
 function createModels({plot,fmt}){return{slidingWork:{label:'O trabalho da força aplicada é o trabalho total?',controls:[['m','Massa — kg',1,4,1,2],['v0','Rapidez inicial à direita — m/s',1,6,1,3],['force','Força aplicada à direita — N',0,8,1,2],['friction','Atrito cinético contrário — N',0,8,1,5],['distance','Distância consultada — m',0,12,1,2]],render:({m,v0,force,friction,distance})=>{
  const r=model(m,v0,force,friction,distance),end=r.stop===null?12:Math.min(12,r.stop),data=Array.from({length:101},(_,i)=>{const x=end*i/100;return[x,Math.max(0,r.k0+r.net*x)]}),maxK=Math.max(r.k0,data.at(-1)[1]);
  const graph=plot([{data},{data:[[0,r.k0],[12,r.k0]],style:'reference'}],{xmin:0,xmax:12,ymin:0,ymax:Math.max(2,Math.ceil(maxK*1.1))},[[r.end,r.k]])+
   '<p class="caption">Horizontal: distância percorrida à direita, em metros. Vertical: energia cinética K, em joules. Azul: trecho admissível até a primeira parada. Tracejado: K inicial como referência; não é outra trajetória. O ponto indica a consulta ou o limite de parada, se a consulta não for alcançável.</p>'+
   `<table class="truth-table"><caption>${r.reachable?'Balanço na distância consultada':'Consulta fora do trecho: balanço somente até a parada'} — ${fmt(r.end)} m</caption><tbody><tr><th>K inicial / final</th><td>${fmt(r.k0)} / ${fmt(r.k)} J</td></tr><tr><th>Trabalho aplicado</th><td>${fmt(r.applied)} J</td></tr><tr><th>Trabalho do atrito</th><td>${fmt(r.friction_work)} J</td></tr><tr><th>Trabalho total = ΔK</th><td>${fmt(r.net_work)} J</td></tr></tbody></table>`;
  return{graph:`<div class="sliding-work-panel">${graph}</div>`,report:r.reachable?`Consulta alcançável: K=${fmt(r.k)} J; rapidez=${fmt(r.speed)} m/s. ${r.stop===null?'Não há parada neste modelo de forças constantes.':`Primeira parada em ${fmt(r.stop)} m. O que ocorre depois exige outro modelo.`}`:`${distance} m não é alcançado antes da primeira parada (${fmt(r.stop)} m). Não atribuímos energia negativa nem velocidade imaginária à consulta. A tabela termina na parada.`,note:'Bloco pontual já em movimento, apoio horizontal fixo; força aplicada e módulo do atrito constantes até a parada. Peso/normal têm trabalho zero. Não se calcula μ nem atrito estático, reinício ou inversão. Dados sintéticos, sem montagem real. Se bloco+superfície formarem o sistema, sem outras trocas, o aumento de energia interna até a distância da tabela é '+fmt(r.internal)+' J.'};
 }}};}
 return{model,createModels};
})();
