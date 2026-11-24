/* Encadeamento separado, hashes didáticos determinísticos e rehash. */
window.HashModels=(()=>{
 const operations=[['put','ab',1],['put','ba',2],['put','ad',3],['put','x',4],['put','ab',9],['delete','ba'],['put','y',5],['put','z',6]];
 function rawHash(key,mode){if(mode==='constant')return 0;let value=0;for(const c of key)value=mode==='sum'?value+c.codePointAt(0):(31*value+c.codePointAt(0))>>>0;return value;}
 function trace(limit=.75,mode='sum'){
  let buckets=Array.from({length:4},()=>[]),size=0,migrated=0;const states=[];
  const index=key=>rawHash(key,mode)%buckets.length;
  const record=action=>states.push({action,capacity:buckets.length,size,load:size/buckets.length,buckets:buckets.map(b=>b.map(pair=>pair.slice())),migrated,longest:Math.max(...buckets.map(b=>b.length))});record('Inicial');
  for(const [op,key,value]of operations){let bucket=buckets[index(key)],i=bucket.findIndex(pair=>pair[0]===key);
   if(op==='delete'){if(i<0)throw Error('Chave ausente');bucket.splice(i,1);size--;record('Apagar '+key);continue;}
   if(i>=0){bucket[i]=[key,value];record('Guardar '+key+'='+value);continue;}
   if(size+1>limit*buckets.length){const old=buckets;buckets=Array.from({length:old.length*2},()=>[]);for(const b of old)for(const pair of b){buckets[index(pair[0])].push(pair.slice());migrated++;}}
   buckets[index(key)].push([key,value]);size++;record('Guardar '+key+'='+value);
  }return states;
 }
 function createModels({fmt}){return{hashGrowth:{label:'Compare colisões, carga e redimensionamento',controls:[['hash','Hash: 0 soma · 1 polinomial · 2 constante',0,2,1,0],['threshold','Limite: 0 → 0,75 · 1 → 2',0,1,1,0],['step','Operações executadas',0,8,1,4]],render:({hash,threshold,step})=>{
  const mode=['sum','poly','constant'][hash],r=trace(threshold?2:.75,mode)[step];
  return{graph:`<table class="truth-table"><caption>Baldes após ${r.action}</caption><thead><tr><th>Índice</th><th>Pares chave:valor</th></tr></thead><tbody>${r.buckets.map((b,i)=>`<tr class="${b.length>1?'selected':''}"><td>${i}</td><td>${b.length?b.map(([k,v])=>`${k}:${v}`).join(' → '):'—'}</td></tr>`).join('')}</tbody></table>`,report:`Passo ${step}: ${r.action}. n=${r.size}; baldes=${r.capacity}; fator de carga=${fmt(r.load)}; maior balde=${r.longest}; pares migrados=${r.migrated}.`,note:'Hash didático para strings: soma de códigos Unicode, polinomial base 31 (32 bits) ou constante zero. Destaque indica balde com colisões. Crescimento dobra o número de baldes e recalcula os índices; atualizar uma chave não aumenta n. Não há encolhimento. Carga controlada não garante dispersão: hash constante deixa todos os pares no mesmo balde. O traçado usa oito operações fixas e não representa o dict interno do Python.'};
 }}};}return{rawHash,trace,createModels};
})();
