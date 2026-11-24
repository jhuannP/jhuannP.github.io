/* Superposição linear em três situações distintas; m, s e Hz. */
window.WaveSuperpositionModels=(()=>{
 const A=.01,F=8,K=2*Math.PI,W=2*Math.PI*F;
 function evaluate(mode,x,t,phasePi=0,df=1){if(![0,1,2].includes(mode)||![x,t,phasePi,df].every(Number.isFinite)||df<0)throw new RangeError('Modo e valores finitos');let u,v,envelope;
 if(mode===0){u=K*x-W*t;v=u+Math.PI*phasePi;envelope=2*A*Math.abs(Math.cos(Math.PI*phasePi/2))}
 else if(mode===1){u=K*x-W*t;v=K*x+W*t;envelope=2*A*Math.abs(Math.cos(K*x))}
 else{u=2*Math.PI*F*t;v=2*Math.PI*(F+df)*t;envelope=2*A*Math.abs(Math.cos(Math.PI*df*t))}
 const y1=A*Math.cos(u),y2=A*Math.cos(v);return{y1,y2,total:y1+y2,envelope}}
 function beatMetrics(df){if(!Number.isFinite(df)||df<0)throw new RangeError('df não negativo');return{mean_frequency:F+df/2,beat_frequency:df,beat_period:df?1/df:null}}
 function createModels({plot,sample,fmt}){const f=x=>fmt(Math.abs(x)<1e-12?0:x);return{
 waveSuperposition:{label:'Distinga fase, nós espaciais e batimentos no tempo',controls:[['mode','Situação: 0 fase · 1 estacionária · 2 batimentos',0,2,1,0],['time','Instante de leitura (s)',0,1,.025,0],['phasePi','Fase relativa φ/π (só situação 0)',0,2,.25,0],['df','Diferença Δf (Hz, só situação 2)',0,2,.25,1]],render:({mode,time,phasePi,df})=>{
 const end=mode===2?(df?2/df:2):1;
 const read=z=>mode===2?evaluate(mode,0,z,phasePi,df):evaluate(mode,z,time,phasePi,df);
 const series=[{data:sample(z=>read(z).total/A,0,end,800)},{data:sample(z=>read(z).envelope/A,0,end,800),style:'reference'},{data:sample(z=>-read(z).envelope/A,0,end,800),style:'reference'}];
 const marker=mode===2?[[time,read(time).total/A]]:mode===1?[[.25,0],[.75,0]]:[];
 const points=Array.from({length:5},(_,i)=>end*i/4),caption=mode===2?'Leitura temporal num ponto: tempo em s e deslocamentos em m':'Corte espacial: posição x em m e deslocamentos em m';
 const rows=points.map(z=>{const r=read(z);return`<tr><td>${f(z)}</td><td>${f(r.total)}</td><td>${f(r.envelope)}</td></tr>`}).join('');
 const metrics=beatMetrics(df);let report;
 if(mode===0){const amp=2*A*Math.abs(Math.cos(Math.PI*phasePi/2)),ratio=4*Math.cos(Math.PI*phasePi/2)**2;report=`Ondas no mesmo sentido, f=8 Hz e λ=1 m. Fase=${f(phasePi)}π rad; amplitude da soma=${f(amp)} m. Razão entre potência média total e a de uma componente=${f(ratio)}, no mesmo meio e frequência. A amplitude é igual em todo x; zeros momentâneos da curva não são nós permanentes.`}
 else if(mode===1)report='Ondas iguais em sentidos opostos: f=8 Hz, λ=1 m. Nós em x=0,25 m e 0,75 m nesta janela; separação=0,5 m. Antinós em 0; 0,5; 1 m. Fluxo médio líquido de energia zero; energia armazenada não é zero. A janela de 0 a 1 m não representa uma corda com as duas pontas fixas.';
 else report=`Leitura num ponto fixo: f₁=8 Hz, f₂=${f(8+df)} Hz; frequência média=${f(metrics.mean_frequency)} Hz. ${df?`Batimentos=${f(df)} Hz; intervalo entre máximos do envelope=${f(metrics.beat_period)} s. Janela com dois períodos de batimento.`:'Sem batimentos periódicos: frequências iguais e envelope constante de 0,02 m.'} Em t=${f(time)} s: y=${f(read(time).total)} m; envelope=${f(read(time).envelope)} m. O cosseno modulador tem sinal; o envelope é seu módulo.`;
 return{graph:`<p>Horizontal: ${mode===2?'tempo t (s)':'posição x (m)'} · vertical: y/A · azul: soma; tracejados: ±envelope/A</p>`+plot(series,{xmin:0,xmax:end,ymin:-2.2,ymax:2.2},marker).replace('<svg ','<svg class="wave-superposition-scene" ')+`<table class="truth-table wave-superposition-table"><caption>${caption}</caption><thead><tr><th>${mode===2?'t (s)':'x (m)'}</th><th>Soma y (m)</th><th>Envelope (m)</th></tr></thead><tbody>${rows}</tbody></table>`,report,note:`Amplitude de cada componente A=0,01 m. Nas situações 0/1: λ=1 m, f=8 Hz e c=8 m/s; o instante seleciona um corte espacial. Na situação 2, o instante seleciona o círculo na série temporal; x não varia. φ só altera 0, Δf só altera 2. Em 1 os círculos marcam nós; em 0 não há marcadores. O gráfico usa y/A adimensional e a tabela usa metros. Superposição linear ideal, sem dissipação, dados experimentais ou condições de contorno impostas nas bordas da janela. Valores exibidos arredondados.`}
 }}
 }}return{createModels,evaluate,beatMetrics};
})();
