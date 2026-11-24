/* Duas hipóteses sintéticas com o mesmo nível estacionário; sem ajuste a dados. */
window.RNATurnoverModels=(()=>{
 function solution(production,loss,initial,time){
  if(![production,loss,initial,time].every(v=>typeof v==='number'&&Number.isFinite(v))||production<0||loss<=0||initial<0||time<0)throw new RangeError('Parâmetros finitos e não negativos; perda positiva');
  const star=production/loss;if(!Number.isFinite(star))throw new RangeError('Escala fora do intervalo numérico');
  const value=initial+(star-initial)*(-Math.expm1(-loss*time));if(!Number.isFinite(value))throw new RangeError('Resultado fora do intervalo numérico');return value;
 }
 function model(fold=2,initial=10,time=10){
  if(!Number.isInteger(fold)||fold<1||fold>4||(!Number.isInteger(initial)||initial<0||initial>50||initial%5!==0)||!Number.isInteger(time)||time<0||time>30)throw new RangeError('Fator 1..4, início 0..50 em passos de 5 e tempo 0..30 inteiros');
  const row=(production,loss)=>{const level=solution(production,loss,initial,time);return{production,loss,stationary:production/loss,level,derivative:production-loss*level,half_life:Math.log(2)/loss};};
  return{a:row(2*fold,.2),b:row(2,.2/fold)};
 }
 function createModels({plot,sample,fmt}){return{rnaTurnover:{label:'Mesmo nível final, explicações diferentes',controls:[['fold','Fator r: produção A ou estabilidade B',1,4,1,2],['initial','Abundância inicial M₀ — u',0,50,5,10],['time','Instante observado — h',0,30,1,10]],render:({fold,initial,time})=>{
  const r=model(fold,initial,time),ymax=Math.ceil(Math.max(initial,r.a.stationary)*1.1/10)*10;
  let graph=plot([{data:sample(t=>solution(r.b.production,r.b.loss,initial,t),0,30),style:'reference'},{data:sample(t=>solution(r.a.production,r.a.loss,initial,t),0,30)}],{xmin:0,xmax:30,ymin:0,ymax},[[time,r.a.level]]);
  const x=58+time/30*564,y=18+(ymax-r.b.level)/ymax*242,ys=18+(ymax-r.a.stationary)/ymax*242;
  graph=graph.replace('</svg>',`<line x1="58" y1="${ys}" x2="622" y2="${ys}" class="plot-grid" stroke-dasharray="5 5"/><text x="72" y="${ys-8}" style="font-size:23px">M*=${fmt(r.a.stationary)}</text><circle cx="${x}" cy="${y}" r="6" style="fill:none;stroke:var(--ink);stroke-width:2"/></svg>`).replace('<svg ','<svg class="rna-turnover-scene" ').replace('viewBox="0 0 640 300"','viewBox="-20 0 680 310"');
  const table='<table class="truth-table"><caption>Parâmetros hipotéticos após t=0: α em u/h, δ em h⁻¹</caption><thead><tr><th>Hipótese</th><th>α</th><th>δ</th></tr></thead><tbody><tr><th>A · maior produção</th><td>'+fmt(r.a.production)+'</td><td>'+fmt(r.a.loss)+'</td></tr><tr><th>B · menor perda</th><td>'+fmt(r.b.production)+'</td><td>'+fmt(r.b.loss)+'</td></tr></tbody></table>';
  return{graph:'<p>Horizontal: tempo, de 0 a 30 h. Vertical: abundância M em unidades arbitrárias u. A: azul contínuo/ponto cheio; B: preto tracejado/círculo aberto. A linha pontilhada marca M*. Curvas teóricas, sem medições.</p>'+graph+table,report:`Em t=${time} h: M(A)=${fmt(r.a.level)} u; M(B)=${fmt(r.b.level)} u. Ambas tendem a M*=${fmt(r.a.stationary)} u. Meia-vida de perda do modelo: A=${fmt(r.a.half_life)} h; B=${fmt(r.b.half_life)} h.`,note:'dM/dt=α−δM, taxas constantes após t=0; sem processamento, diluição, proteína ou ruído. Referência α₀=2 u/h e δ₀=0,2 h⁻¹. A usa α=rα₀, δ=δ₀; B usa α=α₀, δ=δ₀/r. M₀ é uma condição inicial livre; somente o padrão M₀=10 coincide com o estacionário de referência. Não estimamos taxas a partir de RNA-seq, PCR ou dados pessoais.'};
 }}};}
 return{solution,model,createModels};
})();
