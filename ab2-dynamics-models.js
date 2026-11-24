/* Modelo harmônico AB2 escolhido, não campo de força de espécie real. */
window.AB2DynamicsModels=(()=>{
 const positions=[[0,0,0],[1,0,1],[-1,0,1]],J=[[-1,0,-1,1,0,1,0,0,0],[1,0,-1,0,0,0,-1,0,1],[0,0,-1,-.5,0,.5,.5,0,.5]];
 function modes(mass=2,bend=4){
  if(!Number.isInteger(mass)||mass<1||mass>8||!Number.isInteger(bend)||bend<0||bend>8)throw new RangeError('Massa 1..8 e rigidez em quartos 0..8 inteiros');
  const k=bend/4,a=2+2/mass,b=1/mass,c=1+1/mass,weights=[mass,mass,mass,1,1,1,1,1,1];
  const H=Array.from({length:9},(_,i)=>Array.from({length:9},(_,j)=>J.reduce((s,row,r)=>s+[1,1,k][r]*row[i]*row[j],0)));
  function lift(g,scale){let v=weights.map((w,i)=>J.reduce((s,row,r)=>s+row[i]*g[r],0)/w/scale);return v;}
  const asymmetric=lift([1/Math.sqrt(2),-1/Math.sqrt(2),0],Math.sqrt(a));let lower,upper,lambdas;
  if(k===0){const det=a*c-2*b*b;lower=lift([-b/det,-b/det,a/det],Math.sqrt(a/det)).map(v=>-v);upper=lift([1/Math.sqrt(2),1/Math.sqrt(2),0],Math.sqrt(a));lambdas=[0,a,a];}
  else{const coupling=Math.sqrt(2*k)*b,delta=Math.sqrt((a-k*c)**2+4*coupling**2);lambdas=[(a+k*c-delta)/2,a,(a+k*c+delta)/2];const ev=lam=>{const n=Math.hypot(coupling,lam-a),s=coupling/n,t=(lam-a)/n;return lift([s/Math.sqrt(2),s/Math.sqrt(2),Math.sqrt(k)*t],Math.sqrt(lam));};lower=ev(lambdas[0]);upper=ev(lambdas[2]);}
  return lambdas.map((eigenvalue,i)=>{const vector=[lower,asymmetric,upper][i],residual=Math.max(...H.map((row,r)=>Math.abs(row.reduce((s,v,c)=>s+v*vector[c],0)-eigenvalue*weights[r]*vector[r])));return{index:i,eigenvalue,omega:Math.sqrt(Math.max(0,eigenvalue)),vector,irrep:['A1','B1','A1'][i],mass_norm:vector.reduce((s,v,j)=>s+weights[j]*v*v,0),residual,floppy:k===0&&i===0};});
 }
 function model(mass=2,bend=4,mode=0,amplitude=1){
  if(!Number.isInteger(mode)||mode<0||mode>2||typeof amplitude!=='number'||!Number.isFinite(amplitude)||amplitude< -1||amplitude>1)throw new RangeError('Modo 0..2 e fator visual -1..1');
  const rows=modes(mass,bend),selected=rows[mode],max=Math.max(...selected.vector.map(Math.abs)),displacement=selected.vector.map(v=>amplitude*.25*v/max);
  return{mass,kappa:bend/4,mode,amplitude,rows,selected,displacement,positions:positions.map((p,i)=>p.map((v,j)=>v+displacement[3*i+j])),rigid_zeros:6,internal_zeros:Number(bend===0)};
 }
 function createModels({fmt}){return{ab2Dynamics:{label:'Da energia escolhida ao modo normal',controls:[['mass','Massa de A / massa de B',1,8,1,2],['bend','Rigidez angular κ — em quartos',0,8,1,4],['mode','Modo: 0 A₁ inferior · 1 B₁ · 2 A₁ superior',0,2,1,0],['amplitude','Fator do deslocamento visual — não é tempo',-1,1,.25,1]],render:({mass,bend,mode,amplitude})=>{
  const s=model(mass,bend,mode,amplitude),X=x=>300+140*x,Z=z=>330-140*z;
  let graph='<svg class="ab2-dynamics-scene" viewBox="0 115 600 315" role="img" aria-label="Projeção xz do modo; cinza é referência, azul é deformação visual normalizada"><defs><marker id="ab2-dynamics-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="var(--blue)"/></marker></defs>';
  for(const i of [1,2])graph+=`<line x1="${X(0)}" y1="${Z(0)}" x2="${X(positions[i][0])}" y2="${Z(positions[i][2])}" class="plot-grid"/><line x1="${X(s.positions[0][0])}" y1="${Z(s.positions[0][2])}" x2="${X(s.positions[i][0])}" y2="${Z(s.positions[i][2])}" stroke="var(--blue)" stroke-width="2"/>`;
  positions.forEach((p,i)=>{const v=s.positions[i],radius=i===0?20:14;graph+=`<circle cx="${X(p[0])}" cy="${Z(p[2])}" r="${radius}" fill="none" stroke="var(--muted)" stroke-dasharray="4 4"/><circle cx="${X(v[0])}" cy="${Z(v[2])}" r="${radius}" fill="var(--paper)" stroke="var(--blue)" stroke-width="2"/>`;if(Math.abs(v[0]-p[0])+Math.abs(v[2]-p[2])>1e-12)graph+=`<line x1="${X(p[0])}" y1="${Z(p[2])}" x2="${X(v[0])}" y2="${Z(v[2])}" stroke="var(--blue)" stroke-width="2" marker-end="url(#ab2-dynamics-arrow)"/>`;graph+=`<text x="${X(v[0])}" y="${Z(v[2])+radius+30}" text-anchor="middle">${['A','Bₐ','Bᵦ'][i]}</text>`;});
  graph+='<line x1="50" y1="375" x2="110" y2="375" class="plot-axis"/><line x1="50" y1="375" x2="50" y2="315" class="plot-axis"/><text x="119" y="382">x</text><text x="43" y="306">z</text></svg>';
  const table='<table class="truth-table"><caption>Três coordenadas internas: autovalor λ e frequência angular ω, unidades do modelo</caption><thead><tr><th>Modo/classe</th><th>λ</th><th>ω</th></tr></thead><tbody>'+s.rows.map(r=>`<tr><th>${r.index===mode?'→ ':''}${r.index} · ${r.irrep==='A1'?'A₁':'B₁'}</th><td>${fmt(r.eigenvalue)}</td><td>${fmt(r.omega)}</td></tr>`).join('')+'</tbody></table>';
  return{graph:'<p>Coordenadas cartesianas 3D; esta figura é a projeção xz. Cinza tracejado: referência. Azul: deslocamento estático no modo, ampliado para máximo 0,25×|fator visual|. Não é amplitude física ou animação temporal.</p>'+graph+table,report:`κ=${fmt(s.kappa)}; massas (A,Bₐ,Bᵦ)=(${mass},1,1). Seis zeros rígidos; ${s.internal_zeros?'um zero interno adicional':'nenhum zero interno adicional'}. `+(s.selected.floppy?'Modo selecionado sem restauração angular: zero interno, não movimento rígido.':'Modo selecionado: ω='+fmt(s.selected.omega)+' em unidades abstratas de tempo inverso.')+` Norma de massa do vetor=${fmt(s.selected.mass_norm)}.`,note:'Energia escolhida V=(q₁²+q₂²+κq₃²)/2, em deformações lineares adimensionais; não é campo de força de espécie real. Rigidez zero deixa uma direção interna livre. Os dois A₁ podem misturar estiramento e flexão; v e −v representam o mesmo modo. Frequências não estão em cm⁻¹; nenhuma intensidade IR/Raman ou derivada de dipolo/polarizabilidade foi calculada.'};
 }}};}
 return{modes,model,createModels};
})();
