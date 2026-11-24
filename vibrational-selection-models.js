/* Produtos de representações 1D reais em C2v; números de projeção não são intensidades. */
window.VibrationalSelectionModels=(()=>{
 const ops=[[1,1,1],[-1,-1,1],[1,-1,1],[-1,1,1]],names=['A1','A2','B1','B2'];
 const chars=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
 const channels=[['x',[1,0,0]],['y',[0,1,0]],['z',[0,0,1]],['xx',[2,0,0]],['yy',[0,2,0]],['zz',[0,0,2]],['xy',[1,1,0]],['xz',[1,0,1]],['yz',[0,1,1]]];
 const character=e=>ops.map(s=>s[0]**e[0]*s[1]**e[1]*s[2]**e[2]);
 function model(irrep=0,channel=2){
  if(!Number.isInteger(irrep)||irrep<0||irrep>3||!Number.isInteger(channel)||channel<0||channel>8)throw new RangeError('Classe 0..3 e canal 0..8 inteiros');
  const mode=chars[irrep],operator=character(channels[channel][1]),product=mode.map((v,i)=>v*operator[i]),projection=product.reduce((a,b)=>a+b,0)/4;
  const compatible=channels.filter(([_,e])=>character(e).every((v,i)=>v===mode[i])).map(c=>c[0]);
  return{irrep:names[irrep],operator:channels[channel][0],kind:channel<3?'IR':'Raman',mode_character:[...mode],operator_character:operator,product_character:product,product_irrep:names[chars.findIndex(row=>row.every((v,i)=>v===product[i]))],a1_multiplicity:projection,allowed:projection===1,ir_components:compatible.filter(c=>c.length===1),raman_components:compatible.filter(c=>c.length===2),ab2_multiplicity:[2,0,1,0][irrep]};
 }
 const pretty={A1:'A₁',A2:'A₂',B1:'B₁',B2:'B₂'},sign=n=>n===1?'+1':'−1';
 function createModels(){return{vibrationalSelection:{label:'Que canal é permitido pela simetria?',controls:[['irrep','Classe: 0 A₁ · 1 A₂ · 2 B₁ · 3 B₂',0,3,1,0],['channel','Canal: 0 x · 1 y · 2 z · 3 xx · 4 yy · 5 zz · 6 xy · 7 xz · 8 yz',0,8,1,2]],render:({irrep,channel})=>{
  const s=model(irrep,channel),op=channel<3?'μ'+s.operator:'α'+s.operator;
  const table='<table class="truth-table selection-character-table"><caption>Ordem E, C₂z, σxz, σyz; estado inicial totalmente simétrico</caption><thead><tr><th>Operação</th><th>χQ</th><th>χO</th><th>Produto</th></tr></thead><tbody>'+['E','C₂z','σxz','σyz'].map((g,i)=>`<tr><th>${g}</th><td>${sign(s.mode_character[i])}</td><td>${sign(s.operator_character[i])}</td><td class="${s.product_character[i]===1?'selection-plus':'selection-minus'}">${sign(s.product_character[i])}</td></tr>`).join('')+'</tbody></table>';
  return{graph:`<p>Classe ${pretty[s.irrep]}; canal ${op} (${s.kind}). χQ é o caractere do modo; χO é o do canal. O produto mostra o que sobrevive à média sobre o grupo.</p>`+table+`<p class="selection-projection">ΓQ × ΓO = ${pretty[s.product_irrep]}. Média dos quatro produtos = ${s.product_character.reduce((a,b)=>a+b,0)}/4 = ${s.a1_multiplicity}.</p>`,report:(s.allowed?'Permitido por simetria neste canal; intensidade ainda não calculada.':'Acoplamento anulado por simetria neste canal, nas hipóteses da aula.')+` Para ${pretty[s.irrep]}: IR em ${s.ir_components.join(', ')||'nenhum componente cartesiano'}; Raman em ${s.raman_components.join(', ')}. `+(s.ab2_multiplicity?`A classe aparece ${s.ab2_multiplicity} ${s.ab2_multiplicity===1?'vez':'vezes'} em Γvib=2A₁+B₁ do AB₂ angular.`:`A classe não ocorre em Γvib=2A₁+B₁; este teste de classe é genérico para C₂v.`),note:'Média 0/1 é multiplicidade de A₁, não probabilidade ou intensidade. Convenção: plano molecular xz e eixo C₂ em z; x→B₁, y→B₂. Fundamentais harmônicas a partir do estado vibracional totalmente simétrico; resposta dipolar/polarizabilidade simétrica. xx, xy etc. indicam transformação de componentes do tensor, não valores da polarizabilidade. Sem frequências, derivadas físicas ou espectro; não aplicar a classificação incompleta da geometria linear como regra completa.'};
 }}};}
 return{model,createModels};
})();
