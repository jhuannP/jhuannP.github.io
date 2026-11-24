/* Diferenciais compostos, com resto polinomial explícito. */
window.VectorChainModels=(()=>{
 const H=(u,v)=>[u*u+u*v*v,u*u*v*v-v];
 const mul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((sum,x,k)=>sum+x*B[k][j],0)));
 function model(u=1,v=2,direction=2,k=4){
  if(![u,v].every(Number.isFinite)||Math.abs(u)>2||Math.abs(v)>2||!Number.isInteger(direction)||direction<0||direction>2||!Number.isInteger(k)||k<1||k>8)throw new RangeError('Controles inválidos');
  const w=[[1,0],[0,1],[1,1]][direction],eps=2**(-k),a=eps*w[0],b=eps*w[1],A=[[2*u,0],[0,1],[v,u]],B=[[1,u*v,v],[0,-1,2*u*v]],C=mul(B,A),jv=C.map(r=>r[0]*w[0]+r[1]*w[1]),linear=jv.map(x=>eps*x),base=H(u,v),actual=H(u+a,v+b).map((x,i)=>x-base[i]),remainder=[a*a+u*b*b+2*v*a*b+a*b*b,u*u*b*b+4*u*v*a*b+2*u*a*b*b+a*a*v*v+2*v*a*a*b+a*a*b*b];
  return{u,v,direction,k,eps,h:[a,b],w,A,B,C,jv,linear,actual,remainder,secant:actual.map(x=>x/eps),relative_remainder:Math.hypot(...remainder)/Math.hypot(a,b),bound:34*Math.hypot(a,b)};
 }
 function createModels({fmt}){const num=x=>x!==0&&Math.abs(x)<1e-4?x.toExponential(3).replace(".",","):fmt(x);return{vectorChain:{label:'Compor derivadas e observar o resto',controls:[['u','Ponto-base u',-2,2,1,1],['v','Ponto-base v',-2,2,1,2],['direction','Direção: 0 (1,0) · 1 (0,1) · 2 (1,1)',0,2,1,2],['k','Refinamento k: ε = 2⁻ᵏ',1,8,1,4]],render:({u,v,direction,k})=>{
  const m=model(u,v,direction,k),R=Math.max(1,Math.ceil(Math.max(...m.jv.map(Math.abs),...m.secant.map(Math.abs))*1.2)),X=x=>300+200*x/R,Y=y=>245-200*y/R;
  let svg='<svg class="vector-chain-scene" viewBox="0 0 600 500" role="img" aria-label="Coordenadas da derivada direcional e da secante escalada; eixos com mesma escala, valores na tabela"><line x1="100" y1="245" x2="500" y2="245" class="plot-axis"/><line x1="300" y1="45" x2="300" y2="445" class="plot-axis"/>';
  for(const t of [-R,0,R])svg+='<text x="'+X(t)+'" y="477" text-anchor="middle" style="font-size:22px">'+num(t)+'</text><text x="85" y="'+(Y(t)+7)+'" text-anchor="end" style="font-size:22px">'+num(t)+'</text>';
  svg+='<text x="580" y="477" text-anchor="end" style="font-size:22px">q₁</text><text x="310" y="28" style="font-size:22px">q₂</text>';
  svg+='<line x1="300" y1="245" x2="'+X(m.jv[0])+'" y2="'+Y(m.jv[1])+'" stroke="var(--blue)" stroke-width="2.5"/><rect x="'+(X(m.jv[0])-5)+'" y="'+(Y(m.jv[1])-5)+'" width="10" height="10" fill="var(--blue)"/>';
  svg+='<line x1="300" y1="245" x2="'+X(m.secant[0])+'" y2="'+Y(m.secant[1])+'" stroke="var(--ink)" stroke-width="2" stroke-dasharray="7 4"/><circle cx="'+X(m.secant[0])+'" cy="'+Y(m.secant[1])+'" r="5" fill="var(--ink)"/></svg>';
  const matrix=(name,A)=>'<table class="truth-table"><caption>'+name+'</caption><tbody>'+A.map(row=>'<tr>'+row.map(x=>'<td>'+num(x)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
  const table='<table class="truth-table"><caption>Incremento h=εw; vetores em coordenadas adimensionais</caption><thead><tr><th>Grandeza</th><th>Componente 1</th><th>Componente 2</th></tr></thead><tbody>'+[['DH(p)w',m.jv],['ΔH/ε',m.secant],['ΔH exato',m.actual],['DH(p)h',m.linear],['Resto',m.remainder]].map(([name,v])=>'<tr><th>'+name+'</th>'+v.map(x=>'<td>'+num(x)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
  return{graph:'<p>F(u,v)=(u²,v,uv), G(x,y,z)=(x+yz,z²−y), H=G∘F. Quadrado azul: DH(p)w. Círculo preto: [H(p+εw)−H(p)]/ε. Eixos q₁/q₂ com a mesma escala, adaptada aos controles. Posição no gráfico representa vetor de variação por ε; não é o gráfico de H. Para w=(1,1), a direção não é unitária. Marcadores podem quase coincidir; consulte os valores.</p>'+svg+matrix('DF(p): 3×2',m.A)+matrix('DG(F(p)): 2×3',m.B)+matrix('Produto DH(p): 2×2',m.C)+table,report:'ε='+num(m.eps)+'; ||resto||/||h||='+num(m.relative_remainder)+'. Limite uniforme demonstrado para esta família: 34||h||='+num(m.bound)+'. DH(p)w=('+m.jv.map(num).join('; ')+').',note:'Funções polinomiais diferenciáveis em todos os pontos. Base no quadrado [-2,2]² e ||h||≤1: limite 34||h|| vale para o quociente do resto e tende a zero. O painel mostra só três direções; a prova algébrica cobre as demais. Resto calculado pela expansão polinomial, evitando subtração numérica como justificativa do limite. Não há dados físicos, calibração, inferência ou domínio pessoal certificado.'};
 }}};}
 return{model,createModels};
})();
