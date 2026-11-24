const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const context={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/model.js','utf8'),context);
const {angleState,createModels}=context.window.UnitCircleModels;
for(const [d,x,y] of [[0,1,0],[90,0,1],[180,-1,0],[270,0,-1],[360,1,0],[-90,0,-1]]){
 const s=angleState(d);assert.equal(s.x,x);assert.equal(s.y,y);
 assert.equal(s.tangent,x===0?null:y/x);
}
assert.equal(angleState(30).radianLabel,'π/6 rad');
assert.equal(angleState(-120).radianLabel,'−2π/3 rad');
assert.equal(angleState(360).radianLabel,'2π rad');
for(let d=-360;d<=360;d++){
 const s=angleState(d);assert.ok(Math.abs(s.x*s.x+s.y*s.y-1)<1e-14);
 const reflected=angleState(-d);assert.ok(Math.abs(s.x-reflected.x)<1e-14);assert.ok(Math.abs(s.y+reflected.y)<1e-14);
 if(d<=0){const t=angleState(d+360);assert.ok(Math.abs(t.x-s.x)<1e-14);assert.ok(Math.abs(t.y-s.y)<1e-14);}
}
assert.equal(angleState(120).location,'quadrante II');
assert.equal(angleState(-30).location,'quadrante IV');
assert.ok(Math.abs(angleState(30).y-.5)<1e-14);
for(const bad of [true,'30',null,NaN,Infinity,30.5,-361,361])assert.throws(()=>angleState(bad));
const model=createModels({fmt:n=>String(Math.round(n*1e5)/1e5)}).schoolUnitCircle;
for(let d=-360;d<=360;d+=15){const r=model.render({degrees:d});assert.match(r.graph,/viewBox="0 0 360 360"/);assert.match(r.graph,/aria-label=/);assert.doesNotMatch(r.graph,/NaN|Infinity/);assert.ok(r.report.includes('cos θ'));}
assert.match(model.render({degrees:90}).report,/tangente não definida/);
console.log('Círculo: 721 ângulos, eixos, simetrias, unidades e 49 estados visuais conferidos.');
