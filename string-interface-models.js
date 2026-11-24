/* Duas cordas ideais sob tensão comum. Solução analítica, não integração animada. */
window.StringInterfaceModels=(()=>{
 const A=.02,W=.5;
 const pulse=s=>Math.abs(s)<W?A*(1-(s/W)**2)**3:0;
 const prime=s=>Math.abs(s)<W?-6*A*(s/W)*(1-(s/W)**2)**2/W:0;
 function coefficients(q=2){if(!Number.isFinite(q)||q<.5||q>2||!Number.isInteger(4*q))throw new RangeError('Razão Z2/Z1 de0,5 a2, em quartos.');const r=(1-q)/(1+q),tau=2/(1+q);return{q,c1:1,c2:1/q,mu1:1,mu2:q*q,Z1:1,Z2:q,r,tau,R:r*r,transmission:q*tau*tau};}
 function cumulative(t){const z=(t-2)/W;if(z<=-1)return 0;if(z>=1)return 1;const h=u=>u**3/3-4*u**5/5+6*u**7/7-4*u**9/9+u**11/11;return(h(z)+128/3465)/(256/3465);}
 function field(side,x,t,q=2){const c=coefficients(q);if(!['left','right'].includes(side)||!Number.isFinite(x)||!Number.isFinite(t)||t<0||side==='left'&&x>0||side==='right'&&x<0)throw new RangeError('Lado, posição e tempo válidos.');let y,incident=0,reflected=0,velocity,slope,mu;
  if(side==='left'){const a=t-x-2,b=t+x-2;incident=pulse(a);reflected=c.r*pulse(b);y=incident+reflected;velocity=prime(a)+c.r*prime(b);slope=-prime(a)+c.r*prime(b);mu=1;}else{const s=t-x/c.c2-2;y=c.tau*pulse(s);velocity=c.tau*prime(s);slope=-velocity/c.c2;mu=c.mu2;}
  return{y,incident,reflected,velocity,slope,density:.5*mu*velocity**2+.5*slope**2,power:-velocity*slope};
 }
 function model(q=2,time=3.5){const c=coefficients(q);if(!Number.isFinite(time)||time<0||time>5)throw new RangeError('Tempo de0 a5s.');const passed=cumulative(time),energy0=1024*A*A/(385*W);return{...c,time,passed,energy0,energy_left:energy0*(1-passed+c.R*passed),energy_right:energy0*c.transmission*passed,left:field('left',0,time,q),right:field('right',0,time,q)};}
 function createModels({plot,sample,fmt}){return{stringInterface:{label:'Quanto se reflete e quanto passa para a outra corda?',controls:[['q','Razão de impedâncias Z₂/Z₁',.5,2,.25,2],['time','Tempo (s)',0,5,.25,3.5]],render:({q,time})=>{
  const r=model(q,time),physical=sample(x=>field(x<=0?'left':'right',x,time,q).y/A,-4,7,440),inc=sample(x=>field('left',x,time,q).incident/A,-4,0),ref=sample(x=>field('left',x,time,q).reflected/A,-4,0);
  let graph=plot([{data:inc,style:'secondary'},{data:physical},{data:ref,style:'reference'}],{xmin:-4,xmax:7,ymin:-1.5,ymax:1.5});
  const join=58+4/11*(640-58-18);graph=graph.replace('<svg ', '<svg class="string-interface-plot" ');graph=graph.replace('</svg>',`<line x1="${join}" y1="18" x2="${join}" y2="260" stroke="#717268" stroke-dasharray="3 5"/><text x="${join+7}" y="33">junção</text></svg>`);
  graph='<p>Eixo horizontal: x (m); vertical: deslocamento y/A, com A=0,02 m. Azul: campo físico; azul claro: incidente; preto tracejado: refletido, ambos só à esquerda.</p>'+graph;
  const rows=[['Deslocamento refletido r',r.r],['Deslocamento transmitido τ',r.tau],['Energia refletida final R',r.R],['Energia transmitida final T_E',r.transmission],['Energia à esquerda agora / E₀',r.energy_left/r.energy0],['Energia à direita agora / E₀',r.energy_right/r.energy0]];
  graph+='<table class="truth-table"><caption>Coeficientes e energia — junção sem perdas</caption><thead><tr><th>Grandeza</th><th>Valor</th></tr></thead><tbody>'+rows.map(([label,value])=>`<tr><th>${label}</th><td>${fmt(value)}</td></tr>`).join('')+'</tbody></table>';
  return{graph,report:`c₁=1 m/s; c₂=${fmt(r.c2)} m/s. μ₂=${fmt(r.mu2)} kg/m. Na junção: y esquerdo=${fmt(r.left.y)} m; y direito=${fmt(r.right.y)} m. Potências líquidas esquerda/direita=${fmt(r.left.power||0)}/${fmt(r.right.power||0)} W. R+T_E=${fmt(r.R+r.transmission)}.`,note:'Tensão 1 N, μ₁=1 kg/m; q muda μ₂ e redefine o cenário, não varia o meio durante a passagem. Pulso de duração 1 s, centro chega à junção em 2 s. Tempo seleciona fotografias analíticas. R e T_E são frações finais; durante o encontro, parte da energia incidente ainda está à esquerda. Não há atrito, absorção, massa na junção ou dados medidos.'};
 }}};}
 return{model,field,createModels};
})();
