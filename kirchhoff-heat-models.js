/* Modelo inventado, não tabelas termoquímicas de uma substância real. */
window.KirchhoffHeatModels=(()=>{
 function model(t=500,cpb=30){
  if(![t,cpb].every(Number.isFinite)||t<250||t>650||cpb<20||cpb>60)throw new RangeError('T250..650 K; CpB20..60 J/(mol K)');
  const u=t-300,cpa=40+.02*u,dcp=cpb-cpa,ha=(40*u+.01*u*u)/1000,hb=2+cpb*u/1000,dh=hb-ha,constant=2+(cpb-40)*u/1000;
  return{t,cpb,cpa,dcp,ha,hb,dh,constant,error:dh-constant,heat_a:ha,heat_b:hb-2,cycle:-ha+2+(hb-2)};
 }
 function createModels({fmt}){return{kirchhoffHeat:{label:'Da capacidade calorífica à entalpia de reação',controls:[['t','Temperatura T (K)',250,650,25,500],['cpb','Cp molar de B, constante (J/mol/K)',20,60,5,30],['view','Vista: 0 capacidades · 1 entalpia',0,1,1,1]],render:({t,cpb,view})=>{
  if(!Number.isInteger(view)||view<0||view>1)throw new RangeError('Vista0/1');const s=model(t,cpb),lo=view?-10:0,hi=view?10:60,X=T=>65+(T-250)*1.22,Y=y=>252-(y-lo)/(hi-lo)*220;
  let g='<svg viewBox="0 0 600 300" role="img" aria-label="Curvas do modelo, com eixo de temperatura e valores descritos na tabela">';
  for(let i=0;i<=4;i++){const T=250+100*i,y=lo+(hi-lo)*i/4;g+='<line x1="65" y1="'+Y(y)+'" x2="553" y2="'+Y(y)+'" class="plot-grid"/><text x="52" y="'+(Y(y)+7)+'" text-anchor="end" style="font-size:22px">'+fmt(y)+'</text><text x="'+X(T)+'" y="285" text-anchor="middle" style="font-size:22px">'+T+'</text>';}
  const curve=which=>Array.from({length:81},(_,i)=>{const T=250+5*i,m=model(T,cpb);return X(T)+','+Y(view?(which?m.constant:m.dh):(which?m.cpb:m.cpa));}).join(' ');
  g+='<line x1="65" y1="'+Y(0)+'" x2="553" y2="'+Y(0)+'" class="plot-axis"/><polyline points="'+curve(0)+'" class="plot-line"/><polyline points="'+curve(1)+'" class="plot-line reference"/><circle cx="'+X(t)+'" cy="'+Y(view?s.dh:s.cpa)+'" r="6" class="plot-dot"/></svg>';
  const rows=[['Cp,A',s.cpa,'J/(mol K)'],['Cp,B',s.cpb,'J/(mol K)'],['ΔrCp',s.dcp,'J/(mol de reação K)'],['hA',s.ha,'kJ/mol'],['hB',s.hb,'kJ/mol'],['ΔrH',s.dh,'kJ/mol de reação'],['Aproximação Cp constante',s.constant,'kJ/mol de reação'],['Modelo − aproximação',s.error,'kJ/mol de reação']];
  return{graph:'<p>Modelo sintético A→B, isômeros hipotéticos, pressão padrão 1 bar e fase fixa. T₀=300 K; hA(T₀)=0 e hB(T₀)=2 kJ/mol.</p><p>Horizontal: T em K. Vertical: '+(view?'ΔrH em kJ/mol de reação. Azul: Cp variável; preto tracejado: aproximação constante em T₀.':'Cp molar em J/(mol K). Azul: A; preto tracejado: B. Não são calores transferidos.')+'</p>'+g+'<table class="truth-table"><caption>Estado selecionado em '+fmt(t)+' K</caption><thead><tr><th>Grandeza</th><th>Valor</th><th>Unidade</th></tr></thead><tbody>'+rows.map(([label,value,unit])=>'<tr><th>'+label+'</th><td>'+fmt(value)+'</td><td>'+unit+'</td></tr>').join('')+'</tbody></table>',report:'ΔrH='+fmt(s.dh)+' kJ/mol de reação. Correção desde 300 K: '+fmt(s.dh-2)+' kJ/mol. Integral por caminho de Hess: '+fmt(s.cycle)+' kJ/mol. Erro da aproximação (modelo−constante)='+fmt(s.error)+' kJ/mol.',note:'CpA=40+0,02(T−300), CpB escolhido constante, em J/(mol K). Dados inventados, somente 250–650 K, sem mudança de fase, cinética, equilíbrio previsto ou calorímetro. O ponto é um estado, não evolução temporal. ΔrCp pode ser negativo apesar de ambas as capacidades serem positivas. Uma mudança de sinal da entalpia não determina espontaneidade.'};
 }}};}
 return{model,createModels};
})();
