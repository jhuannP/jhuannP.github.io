/* Duas cadeiras tetraédricas ideais; face de R preservada, sem trajetória ou energia. */
window.ChairFlipModels=(()=>{
 function model(chair=0,site=1,up=1){
  if(!Number.isInteger(chair)||![0,1].includes(chair)||!Number.isInteger(site)||site<1||site>6||!Number.isInteger(up)||![0,1].includes(up))throw new RangeError('Cadeira/face 0 ou 1; carbono inteiro 1 a 6');
  const rho=Math.sqrt(8/9),carbons=[],axial=[],equatorial=[];
  for(let i=0;i<6;i++){const a=i*Math.PI/3,s=(-1)**(i+chair);carbons.push([rho*Math.cos(a),rho*Math.sin(a),s/6]);axial.push([0,0,s]);equatorial.push([rho*Math.cos(a),rho*Math.sin(a),-s/3]);}
  const index=site-1,wanted=up?1:-1,kind=axial[index][2]===wanted?'axial':'equatorial';
  return{chair,site,up,carbons,axial,equatorial,kind,direction:(kind==='axial'?axial:equatorial)[index],other_kind:kind==='axial'?'equatorial':'axial',axial_up:axial.map((v,i)=>v[2]>0?i+1:0).filter(Boolean)};
 }
 function createModels(){return{chairFlip:{label:'Inverta a cadeira e acompanhe o mesmo grupo R',controls:[['chair','Cadeira (0: A · 1: B)',0,1,1,0],['site','Carbono de R',1,6,1,1],['up','Face de R (0: abaixo · 1: acima)',0,1,1,1]],render:({chair,site,up})=>{
  const s=model(chair,site,up),proj=p=>[300+140*(p[0]+.4*p[1]),260+75*p[1]-125*p[2]],add=(p,v)=>p.map((x,i)=>x+.65*v[i]),line=(a,b,style)=>'<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+b[0]+'" y2="'+b[1]+'" '+style+'/>';
  let svg='<svg class="chair-flip-scene" viewBox="0 0 600 520" role="img" aria-label="Cadeira ideal '+(chair?'B':'A')+', carbonos numerados, grupo R em C'+site+' '+(up?'acima':'abaixo')+' '+s.kind+'"><text x="300" y="28" text-anchor="middle">Cadeira '+(chair?'B':'A')+' · R em C'+site+'</text><text x="300" y="57" text-anchor="middle">Acima: +z · abaixo: −z · vista inclinada</text>';
  for(let i=0;i<6;i++)for(const name of ['axial','equatorial'])if(!(i===site-1&&name===s.kind))svg+=line(proj(s.carbons[i]),proj(add(s.carbons[i],s[name][i])),'stroke="var(--ink)" stroke-opacity=".35" stroke-width="2" '+(name==='axial'?'stroke-dasharray="5 3"':''));
  for(let i=0;i<6;i++)svg+=line(proj(s.carbons[i]),proj(s.carbons[(i+1)%6]),'stroke="var(--ink)" stroke-width="4"');
  const p=proj(s.carbons[site-1]),end=proj(add(s.carbons[site-1],s.direction));svg+=line(p,end,'stroke="var(--blue)" stroke-width="6" '+(s.kind==='axial'?'stroke-dasharray="7 4"':''))+'<text x="'+end[0]+'" y="'+(end[1]+(up?-12:23))+'" text-anchor="middle" fill="var(--blue)">R</text>';
  for(let i=0;i<6;i++){const c=proj(s.carbons[i]);svg+='<circle cx="'+c[0]+'" cy="'+c[1]+'" r="5" fill="var(--ink)"/><text x="'+(c[0]+12)+'" y="'+(c[1]-8)+'">C'+(i+1)+'</text>';}
  svg+='<text x="300" y="470" text-anchor="middle">R: '+(up?'acima':'abaixo')+' · '+s.kind+'</text><text x="300" y="504" text-anchor="middle">Tracejado: axial · contínuo fino: equatorial</text></svg>';
  return{graph:svg+'<p>Ligações do anel em traço espesso; onze ligações externas restantes em cinza. R está destacado e nomeado. O desenho é uma projeção inclinada de coordenadas ideais, sem escala de comprimento real; a face é definida por z, não pela posição final do rótulo na tela.</p>',report:'Cadeira '+(chair?'B':'A')+': R em C'+site+' '+(up?'acima':'abaixo')+', '+s.kind+'. Na outra cadeira, permanece em C'+site+' '+(up?'acima':'abaixo')+', mas fica '+s.other_kind+'. Axiais acima: C'+s.axial_up.join(', C')+'.',note:'Duas conformações finais, sem animação do caminho. Trocar cadeira preserva carbono e face de R, e troca axial/equatorial. Não é rotação da molécula inteira, cálculo energético, atribuição CIP ou previsão de população. Modelo com apenas um R; relações cis/trans entre dois grupos ainda não são simuladas.'};
 }}};}
 return{model,createModels};
})();
