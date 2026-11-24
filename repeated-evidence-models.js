/* Dois sinais sintéticos. Taxas individuais fixas; dependência escolhida. */
window.RepeatedEvidenceModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 function fraction(n,d=1){if(!d)return 'não definida';if(!n)return '0';const g=gcd(n,d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;}
 function model(prior=1,mode=0){
  if(!Number.isInteger(prior)||prior<0||prior>10||!Number.isInteger(mode)||mode<0||mode>2)throw new RangeError('Base em décimos de 0 a 10; modelo 0, 1 ou 2.');
  const [jh,jn]=[[16,1],[20,5],[15,0]][mode];
  const firstH=prior*20,firstN=(10-prior)*5,bothH=prior*jh,bothN=(10-prior)*jn;
  const first=firstH+firstN,both=bothH+bothN;
  return{prior,mode,jh,jn,firstH,firstN,bothH,bothN,first,both,
   afterFirst:firstH/first,afterBoth:both?bothH/both:null,
   secondH:prior?jh/20:null,secondN:prior<10?jn/5:null};
 }
 function createModels(){return{repeatedEvidence:{label:'O segundo sinal acrescenta informação?',controls:[['prior','P(H) inicial — em décimos',0,10,1,1],['mode','Modelo: 0 independente; 1 cópia; 2 interseções mínimas',0,2,1,0]],render:({prior,mode})=>{
  const r=model(prior,mode),names=['Independentes dado H e dado Hᶜ','S₂ é cópia de S₁','Interseções mínimas admissíveis'];
  const stages=[['Antes de observar',prior/10,fraction(prior,10)],['Depois de S₁',r.afterFirst,fraction(r.firstH,r.first)],['Depois de S₁ e S₂',r.afterBoth,fraction(r.bothH,r.both)]];
  const graph=`<p><strong>${names[mode]}</strong>. Mesmas taxas individuais nos três modelos: 4/5 dado H; 1/5 dado Hᶜ.</p><ol class="evidence-stages" aria-label="Probabilidade de H em três etapas">${stages.map(([label,value,text])=>`<li><span>${label}</span><strong>${text}</strong><span class="evidence-track" aria-hidden="true">${value===null?'':`<span style="width:${value*100}%"></span>`}</span></li>`).join('')}</ol><p class="caption">Barras de P(H), de 0 a 1. Ausência de barra no caso não definido não significa probabilidade zero.</p><table class="truth-table"><caption>Massas no espaço original — caminhos com sinais positivos</caption><thead><tr><th>Origem</th><th>Com S₁</th><th>Com S₁ e S₂</th></tr></thead><tbody><tr><th>H</th><td>${fraction(r.firstH,250)}</td><td>${fraction(r.bothH,250)}</td></tr><tr><th>Hᶜ</th><td>${fraction(r.firstN,250)}</td><td>${fraction(r.bothN,250)}</td></tr><tr><th>Total</th><td>${fraction(r.first,250)}</td><td>${fraction(r.both,250)}</td></tr></tbody></table>`;
  return{graph,report:`Segundo ramo: P(S₂|S₁∩H)=${prior?fraction(r.jh,20):'não definida (H ausente)'}; P(S₂|S₁∩Hᶜ)=${prior<10?fraction(r.jn,5):'não definida (Hᶜ ausente)'}. ${r.both?'Após os dois sinais, divida a massa da linha H pelo total da última coluna.':'O evento dos dois sinais tem massa zero: a razão posterior não está definida.'}`,note:'Todos os números são teóricos. O controle 1 significa base 1/10. Mudar o modelo altera a dependência; não acrescenta dados observados. Com base 0 ou 1, taxas declaradas para o grupo ausente são parâmetros da construção, não condicionais identificáveis. A razão de massa zero é exibida sem aplicar a convenção adicional dos livros.'};
 }}};}
 return{model,fraction,createModels};
})();
