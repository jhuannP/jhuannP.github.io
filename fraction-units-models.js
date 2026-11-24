/* Unidade comum, barras racionais não negativas; sem sorteio ou dados pessoais. */
window.FractionUnitsModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 function model(p=1,q=3,r=1,s=4){
  if(![p,q,r,s].every(Number.isInteger)||p<0||p>6||r<0||r>6||q<1||q>6||s<1||s>6)throw new RangeError('Numeradores 0–6 e denominadores 1–6');
  const common=q*s/gcd(q,s),a=p*(common/q),b=r*(common/s),n=a+b,g=gcd(n,common);return{p,q,r,s,common,a,b,n,numerator:n/g,denominator:common/g,extent:Math.max(1,Math.ceil(n/common))};
 }
 function createModels(){return{schoolFractionUnits:{label:'As partes mudam de nome; a quantidade permanece',controls:[['p','Primeiro numerador',0,6,1,1],['q','Primeiro denominador',1,6,1,3],['r','Segundo numerador',0,6,1,1],['s','Segundo denominador',1,6,1,4]],render:({p,q,r,s})=>{
  const a=model(p,q,r,s),X=v=>48+v/a.extent*504,scale=504/a.extent,rows=[[p+'/'+q+' = '+a.a+'/'+a.common,p/q,0],[r+'/'+s+' = '+a.b+'/'+a.common,r/s,1],['Soma = '+a.n+'/'+a.common,(p/q+r/s),2]];
  let svg='<svg class="fraction-units-scene" viewBox="0 0 600 350" role="img" aria-label="Três barras na mesma escala: primeira fração, segunda fração e soma"><text x="300" y="26" text-anchor="middle">Mesma unidade · partes de tamanho 1/'+a.common+'</text>';
  rows.forEach(([name,value,i])=>{const y=76+90*i;svg+='<text x="48" y="'+(y-12)+'">'+name+'</text><rect x="48" y="'+y+'" width="504" height="30" fill="none" stroke="var(--line)"/>';
   if(i===2)svg+='<rect x="48" y="'+y+'" width="'+p/q*scale+'" height="30" fill="var(--blue)"/><rect x="'+X(p/q)+'" y="'+y+'" width="'+r/s*scale+'" height="30" fill="var(--ink)"/>';
   else svg+='<rect x="48" y="'+y+'" width="'+value*scale+'" height="30" fill="'+(i?'var(--ink)':'var(--blue)')+'"/>';
   for(let k=0;k<=a.extent*a.common;k++)svg+='<line x1="'+X(k/a.common)+'" y1="'+y+'" x2="'+X(k/a.common)+'" y2="'+(y+30)+'" stroke="'+(k%a.common===0?'var(--ink)':'var(--paper)')+'" stroke-width="'+(k%a.common===0?1.5:.7)+'"/><line x1="'+X(k/a.common)+'" y1="'+(y+30)+'" x2="'+X(k/a.common)+'" y2="'+(y+36)+'" stroke="var(--ink)" stroke-width=".8"/>';
  });
  for(let k=0;k<=a.extent;k++)svg+='<text x="'+X(k)+'" y="318" text-anchor="middle">'+k+'</text>';
  svg+='<text x="300" y="346" text-anchor="middle">Eixo em unidades inteiras; escala ajustada ao total</text></svg>';
  return{graph:svg+'<p>Azul: primeira quantidade. Preto: segunda. Na terceira barra, elas aparecem em sequência. As três linhas usam o mesmo inteiro; marcas grossas separam inteiros e as finas, partes de 1/'+a.common+'. Valores e conversões estão escritos acima das barras.</p>',report:p+'/'+q+' + '+r+'/'+s+' = '+a.a+'/'+a.common+' + '+a.b+'/'+a.common+' = '+a.n+'/'+a.common+' = '+a.numerator+'/'+a.denominator+'. Denominador comum mínimo: '+a.common+'.',note:'Frações não negativas, denominadores positivos e mesmo inteiro de referência. Numeradores até 6 podem produzir quantidades maiores que um; o eixo amplia até '+a.extent+' unidade(s). Comparar comprimento entre configurações exige ler a escala. O painel mostra soma e equivalência; não representa números negativos, subtração, multiplicação ou divisão. Conteúdo próprio para revisão, sem certificação de domínio.'};
 }}};}
 return{model,createModels};
})();
