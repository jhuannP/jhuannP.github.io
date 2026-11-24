/* Duas entradas na mesma função, com domínio explícito; não ajusta dados reais. */
window.AffineModels=(()=>{
 function model(a=2,b=1,x1=0,x2=2,domain=0){
  if(![a,b,x1,x2].every(Number.isFinite)||a< -3||a>3||b< -3||b>6||x1< -3||x1>3||x2< -3||x2>3||![0,1].includes(domain))throw new RangeError('Parâmetros fora do domínio');
  const valid=x=>domain===0||x>=0,y1=valid(x1)?a*x1+b:null,y2=valid(x2)?a*x2+b:null,dx=x2-x1,dy=y1!==null&&y2!==null?y2-y1:null,slope=dy!==null&&dx!==0?dy/dx:null;
  let root=null,zero_kind;if(a!==0){root=-b/a;if(root===0)root=0;zero_kind=valid(root)?'unico':'fora'}else zero_kind=b===0?'todos':'nenhum';
  const image=domain===0&&a!==0?'R':a===0?'{b}':a>0?'[b,+infinito)':'(-infinito,b]';
  return{a,b,x1,x2,domain,y1,y2,dx,dy,slope,root,zero_kind,image,monotonic:a>0?'crescente':a<0?'decrescente':'constante'};
 }
 function createModels({plot,sample,fmt}){return{linear:{label:'Compare taxa, intercepto e dois pontos',controls:[['a','Coeficiente a',-3,3,.5,2],['b','Valor inicial b',-3,6,.5,1],['x1','Entrada do ponto P',-3,3,.5,0],['x2','Entrada do ponto Q',-3,3,.5,2],['domain','Domínio: 0 reais · 1 x≥0',0,1,1,0]],render:({a,b,x1=0,x2=2,domain=0})=>{
  const s=model(a,b,x1,x2,domain),series=[{data:sample(x=>a*x+b,domain===0?-3:0,3)}],points=[];
  if(s.y1!==null)points.push([x1,s.y1]);if(s.y2!==null)points.push([x2,s.y2]);
  if(s.slope!==null){series.push({data:[[x1,s.y1],[x2,s.y1]],style:'reference'},{data:[[x2,s.y1],[x2,s.y2]],style:'reference'})}
  let graph=plot(series,{xmin:-3,xmax:3,ymin:-12,ymax:16},points).replace('<svg ','<svg class="affine-scene" ');
  graph=graph.replace('</svg>','<circle cx="340" cy="'+(18+(16-b)*242/28)+'" r="7" fill="none" stroke="currentColor" stroke-width="2"/></svg>');
  const zero=s.zero_kind==='unico'?'Zero no domínio: x='+fmt(s.root)+'.':s.zero_kind==='fora'?'O zero algébrico x='+fmt(s.root)+' está fora do domínio; não há zero na função restrita.':s.zero_kind==='todos'?'Todos os pontos do domínio são zeros.':'Função constante não nula: nenhum zero.';
  const rate=s.y1===null||s.y2===null?'Um ponto escolhido está fora do domínio; a taxa entre eles não é definida nesta função.':s.dx===0?'P e Q coincidem: Δx=0, então Δy/Δx é indefinido. Isso não transforma o gráfico em reta vertical.':'Δx='+fmt(s.dx)+'; Δy='+fmt(s.dy)+'; Δy/Δx='+fmt(s.slope)+'.';
  const rows=[['P',x1,s.y1],['Q',x2,s.y2]].map(([name,x,y])=>'<tr><td>'+name+'</td><td>'+fmt(x)+'</td><td>'+(y===null?'fora do domínio':fmt(y))+'</td></tr>').join('');
  return{graph:'<p><strong>Horizontal: x; vertical: f(x).</strong> Azul: gráfico no domínio e pontos P/Q válidos. Círculo preto: (0,b). Tracejado: variações horizontal e vertical entre os pontos, quando a taxa está definida. Eixos têm escalas diferentes.</p>'+graph+'<table class="truth-table"><caption>Entradas e saídas; pontos fora do domínio não recebem valor</caption><thead><tr><th>Ponto</th><th>x</th><th>f(x)</th></tr></thead><tbody>'+rows+'</tbody></table>',
  report:'f(x)='+fmt(a)+'x'+(b>=0?'+':'')+fmt(b)+'. f(0)='+fmt(b)+'. '+s.monotonic[0].toUpperCase()+s.monotonic.slice(1)+'. '+rate+' '+zero+' Imagem: '+s.image.replaceAll('b',fmt(b)).replaceAll('infinito','∞')+'.',
  note:'Adotamos função afim com a real, incluindo a=0; função polinomial de primeiro grau exige a≠0. Contradomínio R; domínio selecionado R ou [0,+∞). A janela mostra apenas −3≤x≤3; a reta não termina no limite do desenho. Ângulo visual depende da escala dos eixos, mas Δy/Δx é calculado nas coordenadas. Fora do domínio há extensão algébrica possível, sem atribuir valor à função restrita. Não são preços, medições ou ajuste estatístico. Python é opcional; material original em rascunho.'};
 }}}}
 return{model,createModels};
})();
