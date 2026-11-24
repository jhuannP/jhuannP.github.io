/* Plano z=x+y, produto euclidiano; gráfico em seção afim ortonormal. */
window.PlaneProjectionModels=(()=>{
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),U=[1,0,1],V=[0,1,1],N=[-1,-1,1];
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 function fraction(n,d=1){if(!n)return '0';const g=gcd(Math.abs(n),d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;}
 function model(x=1,y=1,z=1,s=1){if(![x,y,z,s].every(v=>Number.isInteger(v)&&v>=-2&&v<=2))throw new RangeError('Quatro controles inteiros entre−2 e2.');
  const b=[x,y,z],pn=[2*x-y+z,-x+2*y+z,x+y+2*z],rn=b.map((v,i)=>3*v-pn[i]),qn=pn.map((v,i)=>v+3*s*U[i]),err=b.map((v,i)=>3*v-qn[i]);
  const p=pn.map(v=>v/3),residual=rn.map(v=>v/3),candidate=qn.map(v=>v/3),naive=U.map((v,i)=>dot(b,U)*v/2+dot(b,V)*V[i]/2),nr=b.map((v,i)=>v-naive[i]);
  const horizontal=dot(b,U)/Math.sqrt(2),vertical=dot(b,N)/Math.sqrt(3);
  return{b,p,residual,candidate,coefficients:[pn[0]/3,pn[1]/3],pn,rn,qn,
   residual_squared:dot(rn,rn)/9,candidate_error_squared:dot(err,err)/9,increment:2*s*s,p_squared:dot(pn,pn)/9,b_squared:dot(b,b),
   naive,naive_dot_u:dot(nr,U),naive_dot_v:dot(nr,V),omitted:(-x+2*y+z)/Math.sqrt(6),
   points:[[horizontal,vertical],[horizontal,0],[horizontal+s*Math.sqrt(2),0]],error_numerator:dot(err,err),residual_numerator:dot(rn,rn)};
 }
 function createModels({plot,fmt}){return{planeProjection:{label:'Qual ponto do plano fica mais perto de b?',controls:[['x','Componente b₁',-2,2,1,1],['y','Componente b₂',-2,2,1,1],['z','Componente b₃',-2,2,1,1],['s','Candidato q=p+s u — parâmetro s',-2,2,1,1]],render:({x,y,z,s})=>{
  const r=model(x,y,z,s),[b,p,q]=r.points,xs=r.points.map(t=>t[0]),ys=r.points.map(t=>t[1]),cx=Math.round((Math.min(...xs)+Math.max(...xs))/2),cy=Math.round((Math.min(...ys)+Math.max(...ys))/2),M=Math.max(1,Math.ceil(Math.max(...xs.map(t=>Math.abs(t-cx)),...ys.map(t=>Math.abs(t-cy)))+.5)),xmin=cx-M,xmax=cx+M,ymin=cy-M,ymax=cy+M;
  let graph=plot([{data:[[xmin,0],[xmax,0]],style:'secondary'},{data:[p,b]},{data:[b,q],style:'reference'}],{xmin,xmax,ymin,ymax,equalScale:true},r.points);
  const groups=[];for(const[point,name]of [[b,'b'],[p,'p'],[q,'q']]){const same=groups.find(v=>Math.hypot(v.point[0]-point[0],v.point[1]-point[1])<1e-10);if(same)same.name+='='+name;else groups.push({point,name});}
  const labels=groups.map(({point,name})=>{const xx=48+(point[0]-xmin)/(2*M)*292,yy=312-(point[1]-ymin)/(2*M)*292;return`<text x="${xx+8}" y="${yy+(point[1]<-1e-10?24:point[1]>1e-10?-13:b[1]<0?-13:24)}">${name}</text>`}).join('');
  graph=graph.replace('<svg ','<svg class="plane-projection-plot" ').replace('</svg>',labels+'</svg>');
  graph='<p><strong>Seção ortonormal que contém b, p e q.</strong> Horizontal: componente em u/√2; vertical: componente em n/√3. A interseção dessa seção com S é a linha horizontal.</p>'+graph+`<p class="caption">Azul: b−p. Tracejado preto: b−q. A terceira componente, em (−1,2,1)/√6, é a mesma nos três pontos: ${fmt(r.omitted)}. O gráfico é uma seção afim, não uma vista de todo ℝ³; sua origem pode representar um vetor não nulo. Escala igual nos dois eixos.</p>`;
  graph+='<table class="truth-table"><caption>Vetores nas coordenadas originais de ℝ³</caption><thead><tr><th>Componente</th><th>b</th><th>p</th><th>r=b−p</th></tr></thead><tbody>'+[0,1,2].map(i=>`<tr><th>${i+1}</th><td>${r.b[i]}</td><td>${fraction(r.pn[i],3)}</td><td>${fraction(r.rn[i],3)}</td></tr>`).join('')+'</tbody></table>';
  return{graph,report:`Erro mínimo²=${fraction(r.residual_numerator,9)}; erro do candidato²=${fraction(r.error_numerator,9)}. Acréscimo=2s²=${r.increment}. Resíduo verdadeiro: r·u=r·v=0. Na soma ingênua de projeções, os produtos residuais são ${fmt(r.naive_dot_u)} e ${fmt(r.naive_dot_v)}.`,note:'S=span(u,v), u=(1,0,1), v=(0,1,1); n=(−1,−1,1). Vetores adimensionais e produto interno euclidiano. q é somente um candidato escolhido na direção u; a prova de mínimo considera todo S. Alterar s não muda a projeção p. Sobreposição de pontos tem rótulo combinado. A figura não determina a ortogonalidade por aparência: coordenadas e produtos internos a verificam.'};
 }}};}
 return{model,fraction,createModels};
})();
