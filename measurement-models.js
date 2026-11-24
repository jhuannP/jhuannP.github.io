/* Ajuste manual da mesma tabela sintética do laboratório Python. */
window.MeasurementModels=(()=>{
 const points=[[0,1],[1,3.1],[2,4.9],[3,7.1],[4,8.9]];
 const SSE=(v,b)=>points.reduce((sum,[t,x])=>sum+(x-(b+v*t))**2,0);
 function createModels({plot,sample,fmt}){return{
 measurementFit:{label:'Ajuste a reta e confira os resíduos da tabela',controls:[['v','Inclinação proposta (m/s)',1.5,2.5,.02,2],['b','Intercepto proposto (m)',.5,1.5,.02,1]],render:({v,b})=>{const s=SSE(v,b);return{graph:plot([{data:sample(t=>b+v*t,0,4)}],{xmin:0,xmax:4,ymin:0,ymax:10},points),report:`SSE da proposta=${fmt(s)} m²; RMSE=${fmt(Math.sqrt(s/5))} m. Referência OLS: inclinação 1,98 m/s, intercepto 1,04 m, SSE 0,036 m².`,note:'Eixo horizontal tempo em s; vertical posição em m. Pontos são as cinco medições inventadas do CSV do laboratório; reta usa os controles. Ajuste manual não altera o arquivo nem estima incerteza experimental. OLS com pesos iguais e intercepto.'}}}
 }}return{createModels,SSE,points};
})();
