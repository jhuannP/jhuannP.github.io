/* Uma linha hipotética de coexistência: balanços em mol, sem previsão de fases. */
window.PhaseLeverModels=(()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const fraction=(n,d)=>{if(n===0)return '0';const g=gcd(Math.abs(n),d);return d/g===1?`${n/g}`:`${n/g}/${d/g}`;};
 function model(z=50,total=1){
  if(!Number.isInteger(z)||z<0||z>100||!Number.isInteger(total)||total<1||total>5)throw new RangeError('Composição inteira 0..100%; quantidade inteira 1..5 mol.');
  const inside=z>=20&&z<=80,fa=inside?(80-z)/60:null,fb=inside?(z-20)/60:null;
  return{z,total,inside,two_present:z>20&&z<80,fa,fb,n_alpha:inside?total*fa:null,n_beta:inside?total*fb:null,b_alpha:inside?total*fa/5:null,b_beta:inside?total*fb*4/5:null,b_total:total*z/100};
 }
 function diagram(s){
  const X=z=>48+3.1*z;
  let body='<text x="20" y="27">Composições: x de B, em base molar</text><line x1="48" y1="80" x2="358" y2="80" class="phase-composition-axis"/><line x1="110" y1="80" x2="296" y2="80" class="phase-tie-line"/><text x="110" y="58" text-anchor="middle">α: 1/5</text><text x="296" y="58" text-anchor="middle">β: 4/5</text>';
  for(const z of [0,20,50,80,100])body+=`<line x1="${X(z)}" y1="76" x2="${X(z)}" y2="87" class="phase-composition-axis"/><text x="${X(z)}" y="108" text-anchor="middle">${fraction(z,100)}</text>`;
  body+=`<line x1="${X(s.z)}" y1="65" x2="${X(s.z)}" y2="121" class="phase-overall-marker"/><text x="${X(s.z)}" y="142" text-anchor="middle">z=${fraction(s.z,100)}</text>`;
  if(s.inside)body+=`<text x="20" y="177">Frações das fases no total, em base molar</text><rect x="48" y="196" width="${310*s.fa}" height="28" class="phase-alpha"/><rect x="${48+310*s.fa}" y="196" width="${310*s.fb}" height="28" class="phase-beta"/><text x="48" y="251">α: ${fraction(80-s.z,60)}</text><text x="358" y="251" text-anchor="end">β: ${fraction(s.z-20,60)}</text>`;
  else body+='<text x="20" y="197">Sem partição não negativa nesta linha.</text><text x="20" y="228">Não extrapole frações de fase negativas.</text>';
  return `<svg viewBox="0 0 420 275" role="img" aria-label="Linha de coexistência hipotética e composição global; frações de fase na tabela">${body}</svg>`;
 }
 function createModels(){return{phaseLever:{label:'Composição de fase não é quantidade de fase',controls:[['z','Composição global de B — em % molar',0,100,5,50],['total','Quantidade total — em mol',1,5,1,1]],render:({z,total})=>{
  const s=model(z,total),table=s.inside?`<table class="truth-table"><caption>Quantidades de matéria na linha fornecida</caption><thead><tr><th>Grandeza</th><th>α</th><th>β</th></tr></thead><tbody><tr><th>Composição limite de B</th><td>1/5</td><td>4/5</td></tr><tr><th>Fração da fase nᵢ/n</th><td>${fraction(80-z,60)}</td><td>${fraction(z-20,60)}</td></tr><tr><th>Quantidade da fase (mol)</th><td>${fraction(total*(80-z),60)}</td><td>${fraction(total*(z-20),60)}</td></tr><tr><th>B na fase (mol)</th><td>${fraction(total*(80-z),300)}</td><td>${fraction(total*(z-20)*4,300)}</td></tr></tbody></table>`:'<p>As composições fornecidas não permitem representar esse z por quantidades não negativas das duas fases. O painel não determina qual outro estado seria estável.</p>';
  return{graph:`<div class="phase-lever-panel">${diagram(s)}<p class="caption">Linha sintética a T e P fixos: x_Bα=1/5 e x_Bβ=4/5 são hipóteses. Azul: fração de α; preto: fração de β. A barra inferior usa quantidades de matéria, não volumes ou massas. Não é um diagrama temperatura–composição ou previsão de estabilidade.</p>${table}</div>`,report:`Quantidade global de B: ${fraction(total*z,100)} mol em ${total} mol totais. ${s.inside?(s.two_present?'Ambas as fases têm quantidade positiva.':'Limite da linha: uma quantidade de fase é zero; a composição da fase ausente é apenas a composição limite fornecida.'):'Fora da faixa desta linha: nenhuma partição α/β é apresentada.'}`,note:'Sistema binário fechado, sem reação, com dois extremos de coexistência fornecidos. Balanços: n=nα+nβ e nz=nαxα+nβxβ. Para prever extremos ou estabilidade, seriam necessários dados termodinâmicos adicionais. Pressão, temperatura, atividade, volumes e massas não são calculados.'};
 }}};}
 return{model,createModels};
})();
