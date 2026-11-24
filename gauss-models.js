/* Duas fontes prescritas esféricas, R=epsilon0=1 em unidades normalizadas. */
window.GaussModels=(()=>{
 function sphere(profile=0,charge=1,radius=.5){
  if(![0,1].includes(profile)||!Number.isFinite(charge)||!Number.isFinite(radius)||radius<0)throw new RangeError('Perfil 0/1, carga finita e raio não negativo');
  const boundary=profile===1&&radius===1&&charge!==0;
  let inside=null,field=null,flux=null;
  if(!boundary){inside=profile===0?charge*Math.min(radius**3,1):(radius<1?0:charge);field=radius===0?0:inside/(4*Math.PI*radius**2);flux=inside}
  return{profile,charge,radius,boundary,inside,field,flux,inner_limit:profile===0?charge/(4*Math.PI):0,outer_limit:charge/(4*Math.PI)};
 }
 function createModels({plot,sample,fmt}){return{chargedSphere:{label:'Compare esfera volumétrica e casca fina',controls:[['profile','Fonte: 0 esfera volumétrica uniforme · 1 casca fina uniforme',0,1,1,0],['Q','Carga total Q (normalizada)',-2,2,.5,1],['r','Raio gaussiano r/R',0,3,.1,.5],['view','Vista: 0 campo radial 4πEᵣ · 1 fluxo Φ',0,1,1,0]],render:({profile,Q,r,view})=>{const s=sphere(profile,Q,r),f=x=>{if(profile===1)return x<1?0:(view?Q:Q/(x*x));return view?Q*Math.min(x**3,1):(x<=1?Q*x:Q/(x*x))};
 const data=profile===0?[{data:sample(f,0,3)}]:[{data:sample(()=>0,0,1)},{data:sample(x=>view?Q:Q/(x*x),1,3)}];
 const graph=plot([...data,{data:[[1,-2.2],[1,2.2]],style:'reference'}],{xmin:0,xmax:3,ymin:-2.2,ymax:2.2},s.boundary?[]:[[r,f(r)]]).replace('<svg ','<svg class="gauss-scene" ');
 const value=x=>x===null?'—':fmt(x),table=`<table class="truth-table gauss-table"><caption>Grandezas distintas na superfície gaussiana escolhida</caption><thead><tr><th>Q interna</th><th>Eᵣ</th><th>Φ</th></tr></thead><tbody><tr><td>${value(s.inside)}</td><td>${value(s.field)}</td><td>${value(s.flux)}</td></tr></tbody></table>`;
 let report=s.boundary?`A superfície r=R coincide com a carga da casca ideal. Não se atribui valor único a Eᵣ ou fluxo nessa superfície: limites Eᵣ⁻=0 e Eᵣ⁺=${fmt(s.outer_limit)}; Φ⁻=0 e Φ⁺=${fmt(Q)}. Salto Eᵣ⁺−Eᵣ⁻=${fmt(s.outer_limit)}=σ_s/ε₀.`:`Q interna=${fmt(s.inside)}; Eᵣ=${fmt(s.field)}; fluxo Φ=${fmt(s.flux)}. Verificação 4πr²Eᵣ=${fmt(4*Math.PI*r*r*s.field)}. ${r===0?'r=0 é centro, não superfície fechada regular: campo por simetria e fluxo como limite.':profile===1&&r<1?'Campo nulo na cavidade pela simetria esférica, não apenas porque o fluxo é zero.':'Componente radial positiva aponta para fora; negativa para o centro.'}`;
 return{graph:`<p>Eixo horizontal: r/R. Vertical: ${view?'fluxo Φ=Q interna (ε₀=1)':'4πEᵣ, componente radial multiplicada por 4π para leitura'}. Linha vertical tracejada: r/R=1, fronteira da fonte. Os traços na casca mostram limites de cada lado, sem preencher o salto.</p>`+graph+table,report,note:'R=1, ε₀=1 e Q em unidades normalizadas; não são valores SI de um material. Esfera com densidade volumétrica prescrita ou casca com densidade superficial uniforme, no vácuo e sem fontes externas. Não se presume que a esfera volumétrica seja condutora. A superfície gaussiana é matemática; não altera a fonte. Em Q=0 não há salto. Nenhuma medição ou resultado da IC.'}}}}}
 return{sphere,createModels};
})();
