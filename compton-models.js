/* Cinemática Compton: elétron livre inicialmente em repouso, E em me*c² e p em me*c. */
window.ComptonModels=(()=>{
 function model(alpha=1,angle=90){
  if(![alpha,angle].every(Number.isFinite)||alpha<.1||alpha>2||angle<0||angle>180)throw new RangeError('alpha .1..2 e ângulo 0..180 graus');
  const theta=angle*Math.PI/180,d=angle===90?1:2*Math.sin(theta/2)**2,cosine=1-d,sine=angle===0||angle===180?0:Math.sin(theta),denominator=1+alpha*d,scattered=alpha/denominator,kinetic=alpha*alpha*d/denominator,electron_x=alpha*(1+alpha)*d/denominator,electron_y=-scattered*sine,electron_energy=1+kinetic,momentum=Math.hypot(electron_x,electron_y),recoil_angle=momentum?Math.atan2(Math.abs(electron_y),electron_x)*180/Math.PI:null;
  return{alpha,angle,d,scattered,kinetic,photon_x:scattered*cosine,photon_y:scattered*sine,electron_x,electron_y,electron_energy,beta:momentum/electron_energy,recoil_angle,wavelength_in:1/alpha,wavelength_out:1/alpha+d,photon_fraction:1/denominator,electron_fraction:alpha*d/denominator,mass_squared:electron_energy**2-electron_x**2-electron_y**2};
 }
 function diagram(s){
  const line=(x1,y1,x2,y2,kind)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="compton-vector ${kind}" marker-end="url(#compton-${kind})"/>`;
  let drawing='';
  if(s.angle===0||s.angle===180){
   drawing=line(220,70,380,70,'incoming')+line(220,160,220+160*s.photon_x/s.alpha,160,'photon');
   drawing+=s.kinetic?line(60,250,60+160*s.electron_x/s.alpha,250,'electron'):'<circle cx="60" cy="250" r="4"/><text x="85" y="258">pₑ=0</text>';
   drawing+='<text x="24" y="40">Incidente</text><text x="24" y="130">Espalhado</text><text x="24" y="220">Recuo</text>';
  }else{
   const bx=220+160*s.photon_x/s.alpha,by=230-160*s.photon_y/s.alpha,theta=s.angle*Math.PI/180;
   drawing=line(bx,by,380,230,'electron')+line(220,230,380,230,'incoming')+line(220,230,bx,by,'photon');
   drawing+=`<path d="M252 230 A32 32 0 0 0 ${220+32*Math.cos(theta)} ${230-32*Math.sin(theta)}" class="compton-angle"/><text x="${220+48*Math.cos(theta/2)}" y="${230-48*Math.sin(theta/2)}">θ</text><text x="290" y="260">pγ</text><text x="${(220+bx)/2-15}" y="${(230+by)/2-15}" text-anchor="end" class="compton-photon-label">pγ′</text><text x="${(bx+380)/2+18}" y="${(by+230)/2-3}">pₑ</text><circle cx="220" cy="230" r="3"/><text x="200" y="258">0</text>`;
  }
  return `<svg class="compton-scene" viewBox="${s.angle===0||s.angle===180?'0 0 460 300':'30 50 420 230'}" role="img" aria-label="${s.angle===0||s.angle===180?'Momentos colineares em faixas transladadas':'Triângulo de soma vetorial de momentos'}, ângulo do fóton ${s.angle} graus; componentes na tabela"><defs>${[['incoming','#77786e'],['photon','#3049d1'],['electron','#23241f']].map(([id,color])=>`<marker id="compton-${id}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="${color}"/></marker>`).join('')}</defs>${drawing}</svg>`;
 }
 function createModels({plot,sample,fmt}){return{comptonRecoil:{label:'Conserve energia e as duas componentes do momento',controls:[['alpha','Energia incidente α=Eγ/(mₑc²)',.1,2,.1,1],['angle','Ângulo θ do fóton espalhado (graus)',0,180,15,90],['view','Vista: 0 frações de energia · 1 soma de momentos',0,1,1,0]],render:({alpha,angle,view})=>{
  const s=model(alpha,angle),show=x=>x!==0&&Math.abs(x)<1e-4?x.toExponential(3).replace('.',','):fmt(x);
  let graph;
  if(view===0)graph='<p>Horizontal: ângulo θ do fóton, em graus. Vertical: fração da energia incidente. Azul: Eγ′/Eγ; preto tracejado: Kₑ/Eγ. As duas frações somam 1. Ponto azul: ângulo escolhido. Não são intensidades ou probabilidades de espalhamento.</p>'+plot([{data:sample(t=>model(alpha,t).photon_fraction,0,180)},{data:sample(t=>model(alpha,t).electron_fraction,0,180),style:'reference'}],{xmin:0,xmax:180,ymin:0,ymax:1.2},[[angle,s.photon_fraction]]).replace('<svg ','<svg class="compton-energy-scene" ');
  else graph=`<p>Momentos divididos pelo momento incidente Eγ/c: tracejado cinza = fóton antes; azul = fóton depois; preto = elétron de recuo. ${angle===0||angle===180?'Caso colinear: vetores transladados para faixas separadas; as origens das faixas não são posições físicas.':'Triângulo de soma: o vetor do elétron foi transladado para unir a ponta do fóton final à ponta do inicial.'} São vetores, não trajetórias. O comprimento da seta incidente vale 1.</p>`+diagram(s);
  graph+=`<table class="truth-table compton-table"><caption>Energia em mₑc² e componentes do momento em mₑc; o elétron antes tinha E*=1 e p=0</caption><thead><tr><th>Objeto</th><th>E*</th><th>pₓ*</th><th>pᵧ*</th></tr></thead><tbody><tr><th>Fóton antes</th><td>${show(alpha)}</td><td>${show(alpha)}</td><td>0</td></tr><tr><th>Fóton depois</th><td>${show(s.scattered)}</td><td>${show(s.photon_x)}</td><td>${show(s.photon_y)}</td></tr><tr><th>Elétron depois</th><td>${show(s.electron_energy)}</td><td>${show(s.electron_x)}</td><td>${show(s.electron_y)}</td></tr></tbody></table>`;
  return{graph,report:`Eγ′*=${show(s.scattered)}; Kₑ*=${show(s.kinetic)}. λ/λC=${fmt(s.wavelength_in)} → λ′/λC=${fmt(s.wavelength_out)}; deslocamento Δλ/λC=${fmt(s.d)}. Elétron: v/c=${fmt(s.beta)}; ${s.recoil_angle===null?'sem recuo, portanto sem ângulo de recuo definido.':`ângulo abaixo de +x=${fmt(s.recoil_angle)}°.`} Norma do elétron Eₑ*²−pₓ*²−pᵧ*²=${fmt(s.mass_squared)} (esperado 1).`,note:'Cinemática de um fóton e um elétron livre inicialmente em repouso, sem ligação, campos, movimento térmico, múltiplos espalhamentos ou emissão adicional. λC=h/(mₑc), sem fator 2π. Parâmetros normalizados; não são medidas de um material. θ é escolhido, não sorteado: não há seção de choque, fluxo, intensidade ou probabilidade. Neste recorte o fóton não ganha energia; Compton inverso exige outro estado inicial. Transferência e componente longitudinal usam expressões estáveis para pequenos ângulos. Nenhum resultado experimental ou da IC.'};
 }}}}
 return{model,diagram,createModels};
})();
