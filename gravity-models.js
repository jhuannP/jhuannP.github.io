/* Órbita binária ideal; backend Python admite outros estados de N corpos. */
window.GravityModels=(()=>{
 const period=2*Math.PI/Math.sqrt(2);
 function binary(steps,method){
  if(!Number.isInteger(steps)||steps<1||steps>10000||![0,1].includes(method))throw Error('Passos e método inválidos');
  let r=[[-.5,0],[.5,0]],v=[[0,-1/Math.sqrt(2)],[0,1/Math.sqrt(2)]],h=period/steps;
  const accel=r=>{const d=[r[1][0]-r[0][0],r[1][1]-r[0][1]],radius=Math.hypot(...d);if(!radius)throw Error('Colisão não resolvida');const a=d.map(x=>x/radius**3);return[a,a.map(x=>-x)]};
  const record=()=>({r:r.map(row=>row.slice()),v:v.map(row=>row.slice()),energy:v.reduce((s,row)=>s+.5*row.reduce((t,x)=>t+x*x,0),0)-1/Math.hypot(r[1][0]-r[0][0],r[1][1]-r[0][1]),momentum:Math.hypot(v[0][0]+v[1][0],v[0][1]+v[1][1]),center:Math.hypot((r[0][0]+r[1][0])/2,(r[0][1]+r[1][1])/2)});
  const trace=[record()];let a=accel(r);
  for(let n=0;n<steps;n++){
   if(method===0){v=v.map((row,i)=>row.map((x,k)=>x+h*a[i][k]));r=r.map((row,i)=>row.map((x,k)=>x+h*v[i][k]));a=accel(r)}
   else{const next=r.map((row,i)=>row.map((x,k)=>x+h*v[i][k]+.5*h*h*a[i][k]));const b=accel(next);v=v.map((row,i)=>row.map((x,k)=>x+.5*h*(a[i][k]+b[i][k])));r=next;a=b}
   trace.push(record());
  }return trace;
 }
 function createModels({plot,sample,fmt}){return{
 gravityOrbit:{label:'Compare a órbita numérica com a solução conhecida',controls:[['method','Método: 0 Euler–Cromer · 1 Verlet',0,1,1,1],['steps','Passos por período',40,400,20,100],['phase','Fração do período exibida',0,1,.05,1]],render:({method,steps,phase})=>{
  const trace=binary(steps,method),n=Math.round(phase*steps),t=n*period/steps,p=trace[n],exact=[.5*Math.cos(Math.sqrt(2)*t),.5*Math.sin(Math.sqrt(2)*t)];
  const error=Math.hypot(p.r[1][0]-exact[0],p.r[1][1]-exact[1]),drift=Math.max(...trace.slice(0,n+1).map(row=>Math.abs(row.energy+.5))),scale=Math.max(.65,...trace.flatMap(row=>row.r.flat().map(Math.abs)))*1.05;
  const circle=sample(theta=>theta,0,2*Math.PI).map(([theta])=>[.5*Math.cos(theta),.5*Math.sin(theta)]);
  const series=[{data:circle,style:'reference'},...([0,1].map(i=>({data:trace.slice(0,n+1).map(row=>row.r[i]),style:i?'':'secondary'})))];
  return{graph:plot(series,{xmin:-scale,xmax:scale,ymin:-scale,ymax:scale,equalScale:true},p.r),report:`${method?'Verlet':'Euler–Cromer'}; Δt=${fmt(period/steps)}. t=${fmt(t)}; erro de posição=${error.toExponential(3)}. Máximo |ΔE| até t=${drift.toExponential(3)}; |P|=${p.momentum.toExponential(2)}; |centro de massa|=${p.center.toExponential(2)}.`,note:'Eixos x e y adimensionais, mesma escala. Duas massas unitárias, G=1, separação inicial 1; energia inicial −0,5 e período 2π/√2. Pontilhado: círculo exato; curvas: passos numéricos; pontos: instante selecionado. Energia é diagnosticada, não conservada exatamente. Modelo newtoniano sem colisões, relatividade ou dados astronômicos. O navegador mostra apenas este binário; Python admite 2–20 corpos.'}
 }}};
 }return{binary,period,createModels};
})();
