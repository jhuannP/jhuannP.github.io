const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const context={window:{}};vm.runInNewContext(fs.readFileSync('schoolphysics-models.js','utf8'),context);
const model=context.window.SchoolPhysicsModels;
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-10,`${a} vs ${b}`);
let states=0;
for(let V=1;V<=12;V++)for(let R1=1;R1<=6;R1++)for(let R2=1;R2<=6;R2++){
  // Midpoint from the independent conductance node equation.
  const mid=(V/R1)/(1/R1+1/R2),left=(V-mid)/R1,right=mid/R2;
  const r=model.series(V,R1,R2);
  near(r.I,left);near(r.I,right);near(r.V1,V-mid);near(r.V2,mid);
  near(r.P1,r.I*(V-mid));near(r.P2,r.I*mid);near(r.total,r.P1+r.P2);
  states++;
}
const demo=model.createModels({fmt:x=>String(x)}).schoolSeriesCircuit;
assert.equal(demo.controls.length,3);
for(const values of [{V:12,R1:2,R2:4},{V:12,R1:2,R2:6}]){
 const r=demo.render(values);assert.ok(r.graph.includes('Dois resistores em série'));
 assert.ok(!/NaN|Infinity|undefined/.test(r.graph+r.report));
}
console.log(`${states} estados do circuito série conferidos por equação de nó; painel preservado.`);
