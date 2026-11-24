/* Cortes analíticos de seis polinômios; classificação provada na aula. */
window.DegenerateHessianModels=(()=>{
 const coefficients=[[1,-1,0],[1,1,0],[-1,-1,0],[1,0,1],[1,0,-1],[1,0,0]];
 const truths=['saddle','strict-min','strict-max','strict-min','saddle','nonstrict-min'];
 const names=['x²−y²','x²+y²','−x²−y²','x²+y⁴','x²−y⁴','x²'];
 function model(mode=3,direction=2,radius_step=10){
  if(!Number.isInteger(mode)||mode<0||mode>5||!Number.isInteger(direction)||direction<0||direction>2||!Number.isInteger(radius_step)||radius_step<1||radius_step>10)throw new RangeError('Modo0..5,direção0..2,raio1..10.');
  const [a,b,c]=coefficients[mode],[u2,v2]=[[1,0],[.5,.5],[0,1]][direction],q=a*u2+b*v2,radius=radius_step/10;
  const times=[-radius,-radius/2,0,radius/2,radius],quadratic=times.map(t=>q*t*t),values=times.map((t,i)=>quadratic[i]+c*v2*v2*t**4),determinant=4*a*b;
  return{hessian:[[2*a,0],[0,2*b]],determinant,test:determinant<0?'saddle':determinant>0?(a>0?'min':'max'):'inconclusive',truth:truths[mode],radius,times,values,quadratic,q,c,v2};
 }
 function createModels({plot,fmt}){return{degenerateHessian:{label:'Mesma Hessiana: o teste decide o extremo?',controls:[['mode','Função: 0 sela; 1 mínimo; 2 máximo; 3–5 degeneradas',0,5,1,3],['direction','Corte: 0 eixo x; 1 diagonal unitária; 2 eixo y',0,2,1,2],['radius_step','Raio do corte — em décimos',1,10,1,10]],render:({mode,direction,radius_step})=>{
  const z=model(mode,direction,radius_step),r=z.radius,actual=t=>z.q*t*t+z.c*z.v2*z.v2*t**4,quad=t=>z.q*t*t;
  const xs=Array.from({length:121},(_,i)=>-r+2*r*i/120),ys=xs.flatMap(t=>[actual(t),quad(t)]),peak=Math.max(...ys.map(Math.abs)),span=peak?peak*1.2:r*r;
  const graph=`<div class="hessian-degenerate-panel"><p><strong>f(x,y)=${names[mode]}</strong>; origem estacionária. Corte ${['(t,0)','(t/√2,t/√2)','(0,t)'][direction]}.</p>`+plot([{data:xs.map(t=>[t,actual(t)])},{data:xs.map(t=>[t,quad(t)]),style:'reference'}],{xmin:-r,xmax:r,ymin:-span,ymax:span},[[0,0]]).replace('viewBox="0 0 640 300"','viewBox="-45 0 685 300"')+`<p class="caption">Horizontal: parâmetro t do corte, em [−${fmt(r)};${fmt(r)}]. Vertical: valor da função. Azul: f no corte; tracejado: aproximação quadrática (1/2)hᵀHh no mesmo corte. A escala vertical se ajusta ao cenário; compare números, não só alturas entre telas.</p><table class="truth-table"><caption>Hessiana e diagnóstico na origem</caption><tbody><tr><th>H</th><td>diag(${z.hessian[0][0]},${z.hessian[1][1]})</td></tr><tr><th>det H</th><td>${z.determinant}</td></tr><tr><th>Teste de segunda ordem</th><td>${{saddle:'sela',min:'mínimo estrito',max:'máximo estrito',inconclusive:'inconclusivo'}[z.test]}</td></tr><tr><th>Conclusão pela expressão completa</th><td>${{saddle:'sela', 'strict-min':'mínimo estrito','strict-max':'máximo estrito','nonstrict-min':'mínimo não estrito'}[z.truth]}</td></tr></tbody></table></div>`;
  return{graph,report:mode>=3?'Nos modos3–5, H=diag(2,0) e det H=0. As conclusões diferentes vêm dos termos completos: não são deduzidas de uma Hessiana semidefinida nem da amostragem do gráfico.':'Neste polinômio quadrático, a aproximação de segunda ordem coincide com f. O teste na origem é conclusivo.',note:'Todos os exemplos são polinômios C² em ℝ² e têm gradiente zero na origem. Cortes ilustram, mas não provam um mínimo em todas as direções. A classificação da tabela foi demonstrada algebricamente na aula; não há busca numérica de extremos ou garantia geral por varredura.'};
 }}};}
 return{model,createModels};
})();
