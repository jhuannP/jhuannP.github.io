const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const context={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../../schoolmath-models.js','utf8'),context);
const {axisState,createModels}=context.window.SchoolMathModels;
for(const cut of [0,1]){
 const s=axisState(cut);
 assert.equal(s.percent,10);assert.equal(s.absolute,10);assert.equal(s.valueRatio,1.1);
 assert.equal(s.drawnRatio,cut?2:1.1);
 const model=createModels({fmt:n=>String(n)}).truncatedAxis;
 assert.equal(model.controls[0][0],'cut');
 const r=model.render({cut});
 assert.match(r.graph,/viewBox="0 0 440 330"/);assert.match(r.graph,/aria-label=/);assert.match(r.graph,/<desc>/);
 assert.doesNotMatch(r.graph,/NaN|Infinity|undefined/);
 assert.ok(r.report.includes('aumento relativo=10%'));assert.ok(r.report.includes('razão das alturas desenhadas='));
 const heights=[...r.graph.matchAll(/<rect[^>]*height="([\d.]+)"/g)].map(m=>Number(m[1]));
 assert.equal(heights.length,2);assert.ok(Math.abs(heights[1]/heights[0]-s.drawnRatio)<1e-12);
}
for(const bad of [true,'1',null,NaN,Infinity,-1,2,.5])assert.throws(()=>axisState(bad));
console.log('Eixo: dois estados, razões geométricas, descrição e contratos conferidos.');
