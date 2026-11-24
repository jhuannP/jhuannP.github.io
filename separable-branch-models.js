/* Fórmula não prolonga o PVI através de um polo. */
window.SeparableBranchModels=(()=>{
 function model(kind=1,y0=1,t=.5){
  if(!Number.isInteger(kind)||kind<0||kind>1||![y0,t].every(x=>Number.isFinite(x)&&x>=-2&&x<=2))throw new RangeError('Caso0/1, controles[-2,2]');
  const pole=kind===0||y0===0?null:1/y0,lower=pole!==null&&y0<0?pole:null,upper=pole!==null&&y0>0?pole:null,d=1-y0*t;
  const reason=kind===1&&y0!==0&&d===0?'polo':kind===1&&d<0?'outro-intervalo':'valida',defined=reason==='valida';
  const value=defined?(kind===0?y0*Math.exp(2*t):y0/d):null,derivative=defined?(kind===0?2*value:value*value):null;
  return{case:kind,y0,t,pole,lower,upper,reason,defined,value,derivative};
 }
 function createModels({fmt}){return{separableBranches:{label:'Solução, equilíbrio e intervalo do PVI',controls:[['kind','Equação: 0 exponencial · 1 quadrática',0,1,1,1],['y0','Valor inicial y(0)',-2,2,.5,1],['t','Consultar parâmetro t',-2,2,.125,.5]],render:({kind,y0,t})=>{
  const s=model(kind,y0,t),X=x=>65+(x+2)*122,Y=y=>250-(y+6)/12*220;
  let g='<svg viewBox="0 0 600 300" role="img" aria-label="Trecho da solução no intervalo que contém zero; valores e limites descritos abaixo">';
  for(let i=0;i<=4;i++){const x=-2+i,y=-6+3*i;g+='<line x1="65" y1="'+Y(y)+'" x2="553" y2="'+Y(y)+'" class="plot-grid"/><text x="52" y="'+(Y(y)+7)+'" text-anchor="end" style="font-size:22px">'+y+'</text><text x="'+X(x)+'" y="285" text-anchor="middle" style="font-size:22px">'+x+'</text>';}
  g+='<line x1="65" y1="'+Y(0)+'" x2="553" y2="'+Y(0)+'" class="plot-axis"/>';
  let segment=[];const flush=()=>{if(segment.length>1)g+='<polyline points="'+segment.join(' ')+'" class="plot-line"/>';segment=[];};
  for(let i=0;i<=800;i++){const x=-2+i/200,a=model(kind,y0,x);if(a.defined&&Math.abs(a.value)<=6)segment.push(X(x)+','+Y(a.value));else flush();}flush();
  if(s.pole!==null&&s.pole>=-2&&s.pole<=2)g+='<line x1="'+X(s.pole)+'" y1="30" x2="'+X(s.pole)+'" y2="250" stroke="var(--ink)" stroke-dasharray="6 6"/>';
  g+='<circle cx="'+X(0)+'" cy="'+Y(y0)+'" r="5" fill="var(--ink)"/>';
  if(s.defined&&Math.abs(s.value)<=6)g+='<circle cx="'+X(t)+'" cy="'+Y(s.value)+'" r="6" class="plot-dot"/>';g+='</svg>';
  const interval=s.pole===null?'ℝ':s.lower===null?'(−∞; '+fmt(s.upper)+')':'('+fmt(s.lower)+'; +∞)';
  const state=s.reason==='polo'?'Polo: não existe valor finito da solução aqui.':s.reason==='outro-intervalo'?'Fora do intervalo do PVI: a expressão do outro lado do polo não é continuação desta solução.':'y(t)='+fmt(s.value)+'; y′(t)='+fmt(s.derivative)+'.';
  return{graph:'<p>'+(kind===0?'y′=2y; y(0)='+fmt(y0)+'. Fórmula y=y₀exp(2t).':'y′=y²; y(0)='+fmt(y0)+'. Para y₀≠0, y=y₀/(1−y₀t); para y₀=0, equilíbrio zero.')+'</p><p>Horizontal: t, adimensional. Vertical: y, adimensional. Azul: apenas o intervalo do PVI; preto: condição inicial. Linha vertical tracejada: polo, quando presente. Janela fixa t∈[−2;2], y∈[−6;6]; trechos fora dela são omitidos, sem conectar através de regiões inválidas.</p>'+g+'<table class="truth-table"><caption>Consulta ao problema de valor inicial</caption><tbody><tr><th>Intervalo maximal que contém t=0</th><td>'+interval+'</td></tr><tr><th>Polo finito</th><td>'+(s.pole===null?'Nenhum':fmt(s.pole))+'</td></tr><tr><th>Estado da consulta em t='+fmt(t)+'</th><td>'+state+'</td></tr></tbody></table>',report:'Intervalo: '+interval+'. '+state+(s.defined&&Math.abs(s.value)>6?' Valor válido fora da janela vertical do desenho.':''),note:'Expressões exatas de dois modelos didáticos, sem solver numérico ou dados físicos. A janela não limita o intervalo matemático. Uma solução de PVI vive em intervalo conectado; não se salta o polo nem se substitui divergência por zero. Não é uma prova geral de existência/unicidade. O caso zero é tratado antes de dividir.'};
 }}};}
 return{model,createModels};
})();
