/* Newman: seis orientações do butano ideal; geometria sem potencial de energia. */
window.ButaneNewmanModels=(()=>{
 function model(phi=180){
  if(!Number.isInteger(phi)||phi<0||phi>360||phi%60!==0)throw new RangeError('Ângulo inteiro múltiplo de 60 entre 0 e 360');
  const angle=phi%360,rho=Math.sqrt(8/9),vectors=(turn,z)=>Array.from({length:3},(_,k)=>[rho*Math.cos(Math.PI/2+2*Math.PI*k/3+turn),rho*Math.sin(Math.PI/2+2*Math.PI*k/3+turn),z]);
  const eclipsed={HH:0,MH:0,MM:0};
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(((120*i-angle-120*j)%360+360)%360===0)eclipsed[i===0&&j===0?'MM':i!==0&&j!==0?'HH':'MH']++;
  return{phi,angle,kind:angle===180?'anti':[60,300].includes(angle)?'gauche':'eclipsada',front:vectors(0,-1/3),back:vectors(angle*Math.PI/180,1/3),eclipsed,methyl_separation:Math.min(angle,360-angle)};
 }
 function createModels(){return{butaneNewman:{label:'Compare seis orientações ao longo de C2 → C3',controls:[['phi','Diedro CH₃ frente → trás (graus)',0,360,60,180]],render:({phi})=>{
  const s=model(phi),rho=Math.sqrt(8/9);
  let svg='<svg class="newman-lesson-scene" viewBox="0 0 600 480" role="img" aria-label="Newman do butano: CH3 e dois H em cada carbono central, vista C2 para C3"><text x="300" y="28" text-anchor="middle">C2 na frente · C3 atrás</text><circle cx="300" cy="210" r="44" fill="none" stroke="var(--blue)" stroke-width="2"/>';
  const draw=(u,i,back)=>{const x=u[0]/rho,y=-u[1]/rho,start=back?44:0,end=back?125:90,label=back?157:110,name=(i===0?'CH₃':('H'+i))+(back?'t':'f');return'<line x1="'+(300+start*x)+'" y1="'+(210+start*y)+'" x2="'+(300+end*x)+'" y2="'+(210+end*y)+'" stroke="'+(back?'var(--blue)':'var(--ink)')+'" stroke-width="3" '+(back?'stroke-dasharray="6 3"':'')+'/><text x="'+(300+label*x+(back?0:-y*30))+'" y="'+(216+label*y+(back?0:x*30))+'" text-anchor="middle">'+name+'</text>';};
  svg+=s.back.map((u,i)=>draw(u,i,true)).join('')+s.front.map((u,i)=>draw(u,i,false)).join('')+'<circle cx="300" cy="210" r="5" fill="var(--ink)"/><text x="300" y="425" text-anchor="middle">φ='+phi+'° · '+s.kind+'</text><text x="300" y="460" text-anchor="middle">f: frente · t: trás · H1 e H2 equivalentes</text></svg>';
  return{graph:svg+'<p>Ponto: carbono C2 da frente; círculo: carbono C3 de trás. Frente em traço preto contínuo, trás em azul tracejado; os rótulos f/t também distinguem os grupos. Raios de tamanhos diferentes evitam ocultar rótulos: não medem ligações.</p>',report:'φ='+phi+'°: '+s.kind+'. Separação angular projetada dos CH₃: '+s.methyl_separation+'°. Pares eclipsados: H/H='+s.eclipsed.HH+'; CH₃/H='+s.eclipsed.MH+'; CH₃/CH₃='+s.eclipsed.MM+'.',note:'Carbonos centrais tetraédricos ideais, metilas como grupos. Seis orientações distintas; 360° repete 0°. Nos ângulos alternados não há pares eclipsados, mas anti e gauche não são o mesmo arranjo. O painel não calcula energia, população, distâncias reais ou taxa de rotação. CH₃ e H são diferentes: 120° não preserva sempre a relação entre grupos.'};
 }}};}
 return{model,createModels};
})();
