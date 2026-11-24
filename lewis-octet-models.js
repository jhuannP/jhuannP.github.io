/* Ordens candidatas para NO3- e CO3(2-); contagem formal, não simulação eletrônica. */
window.LewisOctetModels=(()=>{
 function model(species=0,b1=2,b2=1,b3=1){
  if(!Number.isInteger(species)||species<0||species>1||[b1,b2,b3].some(x=>!Number.isInteger(x)||x<1||x>3))throw new RangeError('Espécie0/1; ordens inteiras1..3.');
  const orders=[b1,b2,b3],sum=b1+b2+b3,lone=orders.map(b=>8-2*b),valence=species===0?5:4;
  return{symbol:species===0?'N':'C',charge:species===0?-1:-2,total_electrons:2*sum+lone.reduce((a,b)=>a+b,0),lone,shells:[2*sum,8,8,8],formal:[valence-sum,...orders.map((b,j)=>6-lone[j]-b)],octets:sum===4};
 }
 const signed=x=>x>0?'+'+x:x<0?'−'+(-x):'0';
 function diagram(z,orders){
  const cx=230,cy=174,sites=[[230,58],[82,270],[378,270]],labels=['O₁','O₂','O₃'];let bonds='',atoms='';
  for(let i=0;i<3;i++){
   const [x,y]=sites[i],dx=x-cx,dy=y-cy,d=Math.hypot(dx,dy),ux=dx/d,uy=dy/d,nx=-uy,ny=ux;
   const offsets=orders[i]===1?[0]:orders[i]===2?[-4,4]:[-7,0,7];
   for(const off of offsets)bonds+=`<line x1="${cx+ux*32+nx*off}" y1="${cy+uy*32+ny*off}" x2="${x-ux*33+nx*off}" y2="${y-uy*33+ny*off}" stroke="currentColor" stroke-width="2"/>`;
   const pairs=z.lone[i]/2,angles=pairs===3?[-Math.PI/3,0,Math.PI/3]:pairs===2?[-Math.PI/4,Math.PI/4]:[0];
   for(const t of angles){const vx=ux*Math.cos(t)-uy*Math.sin(t),vy=ux*Math.sin(t)+uy*Math.cos(t),px=x+vx*29,py=y+vy*29;for(const off of [-3.5,3.5])atoms+=`<circle cx="${px-vy*off}" cy="${py+vx*off}" r="2.3" fill="currentColor"/>`;}
   atoms+=`<text x="${x}" y="${y+6}" text-anchor="middle">${labels[i]}</text><text x="${i===0?x+75:x}" y="${i===0?y+6:y+53}" text-anchor="middle" class="lewis-charge">CF ${signed(z.formal[i+1])}</text>`;
  }
  return`<svg class="lewis-diagram" viewBox="0 0 460 350" role="img" aria-label="Candidato de Lewis com três oxigênios fixos; ordens e cargas detalhadas na tabela">${bonds}${atoms}<text x="230" y="180" text-anchor="middle">${z.symbol}</text><text x="230" y="206" text-anchor="middle" class="lewis-charge">CF ${signed(z.formal[0])}</text></svg>`;
 }
 function createModels(){return{lewisOctet:{label:'Contagem, octeto e carga conferem ao mesmo tempo?',controls:[['species','Espécie: 0 nitrato; 1 carbonato',0,1,1,0],['b1','Ordem da ligação com O₁',1,3,1,2],['b2','Ordem da ligação com O₂',1,3,1,1],['b3','Ordem da ligação com O₃',1,3,1,1]],render:({species,b1,b2,b3})=>{
  const z=model(species,b1,b2,b3),orders=[b1,b2,b3],symbol=species===0?'NO₃⁻':'CO₃²⁻';
  const graph=`<div class="lewis-octet-panel"><p><strong>${symbol}: ${z.octets?'octetos completos neste contribuinte':'candidato fora do recorte de octeto'}</strong>.</p>${diagram(z,orders)}<p class="caption">Traços: pares compartilhados; pontos: elétrons não ligantes. CF é carga formal, em unidades de carga elementar. O₁–O₃ identificam sítios fixos. Desenho esquemático: posições, ângulos e distâncias não são uma previsão geométrica.</p><table class="truth-table"><caption>Contagem por átomo no candidato exibido</caption><thead><tr><th>Átomo</th><th>Elétrons não ligantes</th><th>Elétrons no entorno</th><th>CF</th></tr></thead><tbody>${[z.symbol,'O₁','O₂','O₃'].map((a,i)=>`<tr><th>${a}</th><td>${i?z.lone[i-1]:0}</td><td>${z.shells[i]}</td><td>${signed(z.formal[i])}</td></tr>`).join('')}</tbody></table></div>`;
  return{graph,report:`Total de elétrons de valência: ${z.total_electrons}; soma das CF: ${signed(z.formal.reduce((a,b)=>a+b,0))}, igual à carga ${signed(z.charge)} do íon. Centro: ${z.shells[0]} elétrons no entorno. ${z.octets?'Uma ligação dupla e duas simples: há três contribuintes equivalentes ao escolher qual O recebe a dupla.':z.shells[0]<8?'O centro está com octeto incompleto. A soma correta das cargas não resolve essa deficiência.':'O centro de segundo período excede oito elétrons. A contagem total correta não autoriza expandir seu octeto.'}`,note:'As ordens são candidatos escolhidos manualmente. Não há evolução temporal, energia, carga parcial ou densidade eletrônica calculada. Os pares não ligantes de cada O são ajustados para completar seu octeto; o centro não tem par isolado neste recorte. Mover a dupla entre sítios não move os núcleos nem representa alternância real entre moléculas.'};
 }}};}
 return{model,createModels};
})();
