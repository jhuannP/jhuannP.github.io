/* Inequações lineares: conjunto real global, reta em janela e prova por casos na aula. */
window.LinearInequalityModels=(()=>{
 const ops=['<','<=','>','>='],symbols=['<','≤','>','≥'],flip={'<':'>','<=':'>=','>':'<','>=':'<='};
 const compare=(u,v,op)=>op==='<'?u<v:op==='<='?u<=v:op==='>'?u>v:u>=v;
 function model(a=-2,b=0,c=6,mode=0,probe=0){
  if(![a,b,c,mode].every(Number.isInteger)||a< -3||a>3||b< -4||b>4||c< -6||c>6||mode<0||mode>3||!Number.isFinite(probe)||probe< -8||probe>8||!Number.isInteger(2*probe))throw new RangeError('Coeficientes inteiros nos controles; ponto em meios inteiros de −8 a 8');
  const op=ops[mode],hit=compare(a*(2*probe)+2*b,2*c,op);
  if(a===0)return{a,b,c,mode,probe,kind:compare(b,c,op)?'all':'none',boundary:null,boundary_exact:null,operator:null,closed:false,hit};
  let n=(c-b)*(a<0?-1:1),d=Math.abs(a),x=Math.abs(n),y=d;while(y){const t=x%y;x=y;y=t;}n=n===0?0:n/x;d/=x;
  return{a,b,c,mode,probe,kind:'ray',boundary:n/d,boundary_exact:d===1?String(n):n+'/'+d,operator:a>0?op:flip[op],closed:mode===1||mode===3,hit};
 }
 function createModels(){return{linearInequality:{label:'Mude a condição e teste um ponto da reta',controls:[['a','Coeficiente de x: a',-3,3,1,-2],['b','Termo do lado esquerdo: b',-4,4,1,0],['c','Lado direito: c',-6,6,1,6],['mode','Comparação (0: < · 1: ≤ · 2: > · 3: ≥)',0,3,1,0],['probe','Ponto de teste x',-8,8,.5,0]],render:({a,b,c,mode,probe})=>{
  const s=model(a,b,c,mode,probe),esc=t=>String(t).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;'),nice=t=>String(t).replaceAll('-', '−'),op=s.operator?symbols[ops.indexOf(s.operator)]:'',q=nice(s.boundary_exact),solution=s.kind==='all'?'ℝ (todos os reais)':s.kind==='none'?'∅ (nenhum real)':'x '+op+' '+q;
  const interval=s.kind==='all'?'ℝ':s.kind==='none'?'∅':s.operator.startsWith('<')?'(−∞, '+q+(s.closed?']':')'):(s.closed?'[':'(')+q+', +∞)';
  const X=x=>52+(x+12)*496/24,blue='var(--blue)',expr=nice(a)+'x '+(b<0?'−':'+')+' '+Math.abs(b)+' '+symbols[mode]+' '+nice(c);
  let svg='<svg class="linear-inequality-scene" viewBox="0 0 600 400" role="img" aria-label="Inequação '+esc(expr)+'; solução '+esc(solution)+'; janela de menos 12 a 12"><text x="300" y="28" text-anchor="middle">'+esc(expr)+'</text><text x="300" y="65" text-anchor="middle">Solução: '+esc(solution)+'</text><line x1="45" y1="200" x2="555" y2="200" stroke="var(--ink)" stroke-width="2"/>';
  for(const tick of [-12,-8,-4,0,4,8,12])svg+='<line x1="'+X(tick)+'" y1="193" x2="'+X(tick)+'" y2="207" stroke="var(--ink)"/><text x="'+X(tick)+'" y="235" text-anchor="middle">'+nice(tick)+'</text>';
  const arrow=(x,left)=>'<polyline points="'+(x+(left?12:-12))+',190 '+x+',200 '+(x+(left?12:-12))+',210" fill="none" stroke="'+blue+'" stroke-width="4"/>';
  if(s.kind==='all')svg+='<line x1="45" y1="200" x2="555" y2="200" stroke="'+blue+'" stroke-width="6"/>'+arrow(45,true)+arrow(555,false);
  if(s.kind==='ray'){const left=s.operator.startsWith('<'),p=X(s.boundary);svg+='<line x1="'+(left?45:p)+'" y1="200" x2="'+(left?p:555)+'" y2="200" stroke="'+blue+'" stroke-width="6"/>'+arrow(left?45:555,left)+'<circle cx="'+p+'" cy="200" r="7" fill="'+(s.closed?blue:'var(--paper,#f2f1e6)')+'" stroke="'+blue+'" stroke-width="3"/><text x="'+p+'" y="277" text-anchor="middle">q='+esc(q)+'</text>';}
  const p=X(probe);svg+='<line x1="'+p+'" y1="140" x2="'+p+'" y2="187" stroke="var(--ink)" stroke-dasharray="4 4"/><circle cx="'+p+'" cy="133" r="5" fill="var(--ink)"/><text x="'+p+'" y="116" text-anchor="middle">x='+nice(probe)+'</text><text x="300" y="322" text-anchor="middle">'+esc(interval)+'</text><text x="300" y="365" text-anchor="middle">Janela: −12 a 12 · setas continuam além dela</text></svg>';
  return{graph:svg+'<p>Azul: parte visível do conjunto solução. Fronteira aberta exclui q; fechada inclui q. O ponto de teste preto é separado da reta para não cobrir a fronteira. A janela não limita o conjunto real; setas indicam continuação. ℝ e ∅ não têm fronteira finita.</p>',report:expr+'. Solução global: '+solution+'; intervalo '+interval+'. Ponto x='+nice(probe)+': '+(s.hit?'satisfaz':'não satisfaz')+' a condição original. '+(a===0?'a=0: avaliamos a condição constante, sem dividir.':a<0?'a<0: ao dividir, invertemos a comparação.':'a>0: ao dividir, preservamos a comparação.'),note:'Coeficientes constantes e domínio real. A condição do ponto é conferida na expressão original por aritmética inteira em unidades de meio; uma grade finita não prova o conjunto real. A solução global decorre da análise algébrica dos casos. O painel não resolve produtos, quocientes, módulo ou restrições de contexto automaticamente. Programação é opcional.'};
 }}};}
 return{model,createModels};
})();
