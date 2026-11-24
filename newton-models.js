/* Resposta inicial, chão horizontal sem atrito; não integra trajetória. */
window.NewtonModels=(()=>{
 function direction(angle){const r=Math.sqrt(3)/2,special={'-180':[-1,0],'-150':[-r,-.5],'-120':[-.5,-r],'-90':[0,-1],'-60':[.5,-r],'-30':[r,-.5],0:[1,0],30:[r,.5],60:[.5,r],90:[0,1],120:[-.5,r],150:[-r,.5],180:[-1,0]};return special[angle]||[Math.cos(angle*Math.PI/180),Math.sin(angle*Math.PI/180)]}
 function response(mass,fx,fy,vx=0){
  if(![mass,fx,fy,vx].every(Number.isFinite)||mass<=0)throw new RangeError('Massa positiva e entradas finitas');
  const weight=10*mass,trial=weight-fy,normal=Math.max(trial,0),net_y=trial>=0?0:fy-weight,state=trial>0?'contato':trial===0?'limite':'separacao';
  return{mass,fx,fy,vx,weight,normal,ax:fx/mass,ay:net_y/mass,net_y,state,power:fx===0||vx===0?0:fx*vx,kinetic:mass*vx*vx/2};
 }
 function model(mass=2,force=6,angle=0,vx=2){
  if(![mass,force,angle,vx].every(Number.isFinite)||mass<1||mass>4||force<0||force>40||angle< -180||angle>180||vx< -4||vx>4)throw new RangeError('Parâmetros fora do domínio');
  const[c,s]=direction(angle),clean=x=>x===0?0:x;
  return{...response(mass,clean(force*c),clean(force*s),vx),force,angle};
 }
 function createModels({fmt}){return{newtonContact:{label:'Isole o corpo e calcule a normal',controls:[['mass','Massa em kg',1,4,.5,2],['force','Força aplicada F em N',0,40,2,6],['angle','Ângulo desde +x em graus',-180,180,15,0],['vx','Velocidade inicial vx em m/s; vy=0',-4,4,1,2]],render:({mass,force,angle,vx})=>{
  const s=model(mass,force,angle,vx),scale=130/Math.max(force,s.weight,s.normal,1);
  function arrow(x,y,dx,dy,label,blue=false){if(Math.hypot(dx,dy)<1e-12)return '';const ex=x+scale*dx,ey=y-scale*dy;return '<path d="M '+x+' '+y+' L '+ex+' '+ey+'" fill="none" stroke="'+(blue?'var(--blue)':'currentColor')+'" stroke-width="3" marker-end="url(#newton-'+(blue?'blue':'black')+')"/><text x="'+(ex+(blue?18:-22))+'" y="'+(ey+5)+'" fill="'+(blue?'var(--blue)':'currentColor')+'">'+label+'</text>'}
  const defs='<defs><marker id="newton-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--blue)"/></marker><marker id="newton-black" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs>';
  const svg='<svg class="newton-scene" viewBox="0 0 640 400" role="img" aria-label="Diagrama de corpo livre: força aplicada F azul, peso P e normal N pretos; sem vetor velocidade">'+defs+'<path d="M 70 315 H 125 M 70 315 V 260" fill="none" stroke="var(--muted)" stroke-width="2"/><text x="130" y="323">+x</text><text x="55" y="250">+y</text>'+arrow(312,200,0,s.normal,'N')+arrow(320,200,0,-s.weight,'P')+arrow(328,200,s.fx,s.fy,'F',true)+'<circle cx="320" cy="200" r="10" fill="currentColor"/><text x="320" y="378" text-anchor="middle">Corpo isolado · forças em N</text></svg>';
  const rows=[['Aplicada F',s.fx,s.fy],['Peso P',0,-s.weight],['Normal N',0,s.normal],['Resultante',s.fx,s.net_y]].map(([name,x,y])=>'<tr><td>'+name+'</td><td>'+fmt(x)+'</td><td>'+fmt(y)+'</td></tr>').join('');
  const regime=s.state==='contato'?'Contato carregado: ay=0 e N>0.':s.state==='limite'?'Limite N=0 e ay=0: não há compressão. Isso não implica aceleração vertical positiva.':'Separação inicial: o contato exigiria normal negativa. Usamos N=0 e ay>0.';
  const motion=vx===0?'O corpo está instantaneamente em repouso; aceleração não nula pode iniciar movimento.':s.power>0?'A energia cinética aumenta neste instante.':s.power<0?'A energia cinética diminui neste instante.':'dK/dt=0 neste instante; isso sozinho não prova rapidez constante depois.';
  return{graph:'<p><strong>Somente forças que atuam no corpo.</strong> F azul; peso e normal pretos. Setas verticais partem de pontos ligeiramente separados para leitura; não representam um cálculo de torque. Escala relativa comum às forças, reajustada entre configurações.</p>'+svg+'<table class="truth-table"><caption>Componentes no referencial inercial</caption><thead><tr><th>Força</th><th>Fx (N)</th><th>Fy (N)</th></tr></thead><tbody>'+rows+'</tbody></table>',report:regime+' a=('+fmt(s.ax)+', '+fmt(s.ay)+') m/s². v inicial=('+fmt(vx)+', 0) m/s. K inicial='+fmt(s.kinetic)+' J; dK/dt='+fmt(s.power)+' W. '+motion,note:'g=10 m/s² didático, massa constante, chão horizontal liso e sem adesão. Instante inicial y=0 e vy=0. A normal só empurra, N≥0; não substituímos força por velocidade. Sem trajetória, colisão, atrito, rotação ou força de resistência. Na separação o desenho continua sendo o diagrama no instante inicial, não um corpo já elevado. Potência usa a velocidade neste referencial e instante. Material original em rascunho.'};
 }}}}
 return{direction,response,model,createModels};
})();
