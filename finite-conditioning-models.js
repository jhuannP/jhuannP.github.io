/* Contagens inventadas, uma seleção uniforme dos átomos representados. */
window.FiniteConditioningModels=(()=>{
 function inspect(a=2,b=1,c=1,d=2){
  if(![a,b,c,d].every(x=>Number.isSafeInteger(x)&&x>=0&&x<=1000000))throw new RangeError('Contagens inteiras de 0 a 1000000');
  const n=a+b+c+d;return{counts:[a,b,c,d],n,pA:n?(a+b)/n:null,pB:n?(a+c)/n:null,joint:n?a/n:null,a_given_b:a+c?a/(a+c):null,b_given_a:a+b?a/(a+b):null,independent:n?a*n===(a+b)*(a+c):null};
 }
 function createModels({fmt}){return{conditionalFinite:{label:'Qual é o universo da pergunta?',controls:[['a','A e B',0,10,1,2],['b','A e não B',0,10,1,1],['c','Não A e B',0,10,1,1],['d','Nem A nem B',0,10,1,2]],render:({a,b,c,d})=>{
  const s=inspect(a,b,c,d),f=x=>x===null?'não definida':fmt(x),items=[['A ∩ B',a,true],['A ∩ Bᶜ',b,false],['Aᶜ ∩ B',c,true],['Aᶜ ∩ Bᶜ',d,false]];
  const rows=items.map(([name,count,inB])=>'<tr><th>'+name+'</th><td>'+count+'</td><td>'+(s.n?fmt(count/s.n):'não definida')+'</td><td>'+(a+c?(inB?fmt(count/(a+c)):'0'):'não definida')+'</td></tr>').join('');
  const bars=items.map(([name,count,inB])=>'<div class="conditional-bar"><span>'+name+'</span><span class="conditional-track"><span style="width:'+count*10+'%;background:'+(inB?'var(--blue)':'var(--ink)')+'"></span></span><strong>'+count+'</strong></div>').join('');
  return{graph:'<p>As quatro regiões são disjuntas. Cada unidade representa um resultado de mesma massa. Azul marca B; preto marca seu complemento. Comprimento é contagem, na mesma escala de 0 a 10.</p>'+bars+'<table class="truth-table"><caption>Massa original e após informar B</caption><thead><tr><th>Região</th><th>Contagem</th><th>P original</th><th>P dado B</th></tr></thead><tbody>'+rows+'</tbody></table>',report:s.n?'Total='+s.n+'; resultados em B='+(a+c)+'. P(A)='+f(s.pA)+'; P(B)='+f(s.pB)+'; P(A∩B)='+f(s.joint)+'. P(A|B)='+f(s.a_given_b)+'; P(B|A)='+f(s.b_given_a)+'. Independência: '+(s.independent?'sim':'não')+' (igualdade exata das contagens).':'Total zero: não há distribuição para normalizar. Probabilidades e independência não são definidas neste painel.',note:'Modelo finito sintético, sem amostragem aleatória ou dados pessoais. Condicionar conserva as proporções dentro de B e atribui massa zero fora dele. Se B tem massa zero, a razão não é definida; não aplicamos automaticamente a convenção dos livros. P(A|B) e P(B|A) podem ser diferentes. Contagens não são inferências sobre uma população.'};
 }}};}
 return{inspect,createModels};
})();
