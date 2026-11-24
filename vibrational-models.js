/* Três massas livres em uma dimensão; não calcula um espectro molecular. */
window.VibrationalModels=(()=>{
 function modes(mass=1,spring=1){
  if(![mass,spring].every(x=>Number.isFinite(x)&&x>0))throw new RangeError('Parâmetros positivos');
  const raw=[[1,1,1],[-1,0,1],[1,-2/mass,1]],weights=[1,mass,1],eig=[0,spring,spring*(1+2/mass)];
  return raw.map((u,i)=>{const norm=Math.sqrt(u.reduce((a,x,j)=>a+weights[j]*x*x,0)),scale=Math.max(...u.map(Math.abs));return{eigenvalue:eig[i],omega:Math.sqrt(eig[i]),mass_vector:u.map(x=>x/norm),shape:u.map(x=>x/scale)}});
 }
 function model(mode=1,mass=1,spring=1,phase=45){
  if(![0,1,2].includes(mode)||![mass,spring,phase].every(Number.isFinite)||mass<.5||mass>4||spring<.5||spring>2||phase<0||phase>360)throw new RangeError('Parâmetros fora do domínio');
  const s=modes(mass,spring)[mode],omega=s.omega,shape=s.shape,A=.15;
  let[c,si]=({0:[1,0],90:[0,1],180:[-1,0],270:[0,-1],360:[1,0]})[phase]||[Math.cos(phase*Math.PI/180),Math.sin(phase*Math.PI/180)];
  if(mode===0){c=1;si=0}
  const clean=x=>x===0?0:x,q=shape.map(x=>clean(A*x*c)),v=shape.map(x=>clean(-A*omega*x*si)),bonds=[q[1]-q[0],q[2]-q[1]],potential=.5*spring*bonds.reduce((a,x)=>a+x*x,0),kinetic=.5*v.reduce((a,x,i)=>a+[1,mass,1][i]*x*x,0);
  return{mode,mass,spring,phase,omega,cyclic:omega/(2*Math.PI),shape,q,v,bonds,potential,kinetic,energy:potential+kinetic,com:(q[0]+mass*q[1]+q[2])/(2+mass)};
 }
 function createModels({fmt}){return{vibrationalModes:{label:'Explore dois estiramentos e a translação',controls:[['mode','Modo: 0 translação · 1 iguais · 2 opostos',0,2,1,1],['mass','Massa central M; massas externas = 1',.5,4,.5,1],['spring','Rigidez comum k',.5,2,.5,1],['phase','Fase vibratória em graus',0,360,15,45]],render:({mode,mass,spring,phase})=>{
  const s=model(mode,mass,spring,phase),base=[140,320,500],pos=base.map((x,i)=>x+180*s.q[i]);
  function coil(a,b){let d='M '+a+' 150 L '+(a+15)+' 150';for(let i=1;i<=10;i++)d+=' L '+(a+15+(b-a-30)*i/11)+' '+(150+(i%2?7:-7));return '<path d="'+d+' L '+(b-15)+' 150 L '+b+' 150" fill="none" stroke="currentColor" stroke-width="2"/>'}
  const arrows=base.map((x,i)=>Math.abs(pos[i]-x)>1e-8?'<path d="M '+x+' 95 H '+pos[i]+'" fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#vibration-arrow)"/>':'').join('');
  const nodes=base.map((x,i)=>'<circle cx="'+x+'" cy="150" r="18" fill="none" stroke="var(--muted)" stroke-width="2"/><circle cx="'+pos[i]+'" cy="150" r="12" fill="var(--blue)"/><text x="'+x+'" y="208" text-anchor="middle">x'+(i+1)+'</text>').join('');
  const svg='<svg class="vibrational-scene" viewBox="0 0 640 270" role="img" aria-label="Cadeia de três massas: posições de equilíbrio cinzas, deslocamentos azuis e setas pretas"><defs><marker id="vibration-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><text x="320" y="40" text-anchor="middle">m=1 · M='+fmt(mass)+' · m=1</text>'+arrows+coil(pos[0],pos[1])+coil(pos[1],pos[2])+nodes+'<text x="320" y="252" text-anchor="middle">Equilíbrio: (−1, 0, 1); amplitude A=0,15</text></svg>';
  const rows=s.q.map((q,i)=>'<tr><td>x'+(i+1)+'</td><td>'+fmt(q)+'</td><td>'+fmt(s.v[i])+'</td></tr>').join('');
  return{graph:'<p><strong>Modelo longitudinal de massas e molas.</strong> Cinza: equilíbrio; azul: posição atual; setas pretas: deslocamento. O tamanho do ponto não representa raio atômico. Só os deslocamentos ao longo da cadeia são permitidos.</p>'+svg+'<table class="truth-table"><caption>Coordenadas reduzidas: deslocamento q e velocidade v</caption><thead><tr><th>Massa</th><th>q</th><th>v</th></tr></thead><tbody>'+rows+'</tbody></table>',
   report:'Ω='+fmt(s.omega)+'; frequência cíclica reduzida Ω/(2π)='+fmt(s.cyclic)+'. Extensões das ligações: ('+s.bonds.map(x=>fmt(x)).join(', ')+'). Energia potencial='+fmt(s.potential)+'; cinética='+fmt(s.kinetic)+'; total='+fmt(s.energy)+'. Deslocamento do centro de massa='+fmt(s.com)+'. '+(mode===0?'Frequência zero: desenhamos apenas uma translação estática. A fase não altera este caso; ele não é vibração.':mode===1?'As duas ligações alongam/encurtam juntas. Ω²=k independe da massa central neste modo selecionado.':'Uma ligação alonga enquanto a outra encurta. Ω²=k(1+2/M).'),
   note:'Massas em m₀, rigidez em k₀, comprimento em ℓ₀ e tempo em √(m₀/k₀). Ω é frequência angular reduzida, não Hz ou cm⁻¹. Mudar fase seleciona uma configuração do modo, não mede tempo entre sistemas. Em q=0 a velocidade pode ser máxima. Modelo harmônico livre, sem força externa, amortecimento, flexão ou rotação; duas molas iguais e duas massas externas iguais. Não é uma simulação de molécula específica. Frequência e vetor mecânico não determinam atividade IV/Raman: faltam resposta eletrônica e regras de seleção. Material original em rascunho.'};
 }}}}
 return{modes,model,createModels};
})();
