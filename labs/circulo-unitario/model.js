/* Círculo didático em posição padrão; sem ligação com observação real. */
window.UnitCircleModels=(()=>{
 function gcd(a,b){while(b)[a,b]=[b,a%b];return a}
 function angleState(degrees){
  if(!Number.isInteger(degrees)||degrees < -360||degrees > 360)throw new RangeError('Use graus inteiros entre −360 e 360');
  const radians=degrees*Math.PI/180,turn=((degrees%360)+360)%360;
  let x=Math.cos(radians),y=Math.sin(radians);
  if(turn%90===0)[x,y]=[[1,0],[0,1],[-1,0],[0,-1]][turn/90];
  const g=gcd(Math.abs(degrees),180),n=degrees/g,d=180/g;
  const radianLabel=degrees===0?'0 rad':`${n<0?'−':''}${Math.abs(n)===1?'':Math.abs(n)}π${d===1?'':`/${d}`} rad`;
  const location=turn===0?'eixo x positivo':turn===90?'eixo y positivo':turn===180?'eixo x negativo':turn===270?'eixo y negativo':`quadrante ${['I','II','III','IV'][Math.floor(turn/90)]}`;
  return{degrees,radians,radianLabel,x,y,tangent:x===0?null:y/x,location};
 }
 function createModels({fmt}){return{
  schoolUnitCircle:{label:'Explore o círculo: ângulo, coordenadas e sinais',controls:[['degrees','Ângulo em graus',-360,360,15,30]],render:({degrees})=>{
   const s=angleState(degrees),px=180+110*s.x,py=180-110*s.y;
   const description=`Ângulo ${degrees} graus. Ponto com cosseno ${fmt(s.x)} e seno ${fmt(s.y)}. ${s.location}.`;
   return{graph:`<svg viewBox="0 0 360 360" role="img" aria-label="${description}"><circle cx="180" cy="180" r="110" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M40 180H320 M180 40V320" stroke="currentColor" stroke-width="1"/><path d="M180 180H${px}V${py}" fill="none" stroke="currentColor" stroke-dasharray="4 4"/><path d="M180 180L${px} ${py}" fill="none" stroke="var(--blue)" stroke-width="3"/><circle cx="${px}" cy="${py}" r="6" fill="var(--blue)"/><g fill="currentColor" font-size="14"><text x="307" y="166">x</text><text x="192" y="48">y</text><text x="292" y="199">1</text><text x="52" y="199">−1</text><text x="188" y="71">1</text><text x="188" y="306">−1</text><text x="14" y="342">x=cos θ · y=sin θ · raio 1</text></g></svg>`,report:`θ=${degrees}°=${s.radianLabel}; ${s.location}. cos θ=${fmt(s.x)}; sin θ=${fmt(s.y)}; ${s.tangent===null?'tangente não definida: cos θ=0':`tan θ≈${fmt(s.tangent)}`}.`,note:'Posição padrão: início no eixo x positivo; sentido positivo anti-horário. Seno e cosseno nos eixos são exatos no código; outros valores são aproximações. As projeções pontilhadas mostram coordenadas com sinal. 0° e 360° chegam ao mesmo ponto, mas representam rotações diferentes.'};
  }}
 }}return{angleState,createModels};
})();
