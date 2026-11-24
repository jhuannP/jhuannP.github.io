/* Tetraedro regular com grupos abstratos; nenhum R/S ou mecanismo de reação. */
window.ChiralityModels=(()=>{
 const BASE=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]];
 function det(a){return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])}
 function oriented(p){return det([0,1,2].map(i=>p[i].map((x,j)=>x-p[3][j])))}
 function perms(a){if(!a.length)return[[]];return a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(p=>[x,...p]))}
 const PERMS=perms([0,1,2,3]);
 function matching(points,labels){return PERMS.filter(p=>p.every((j,i)=>labels[i]===labels[j])).map(p=>{
  const Q=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>BASE.reduce((sum,r,t)=>sum+points[p[t]][i]*r[j],0)/4));
  const orth=Math.max(...Q.flatMap((r,i)=>Q.map((s,j)=>Math.abs(r.reduce((a,x,k)=>a+x*s[k],0)-(i===j?1:0)))));
  const error=Math.max(...BASE.flatMap((r,t)=>Q.map((row,i)=>Math.abs(row.reduce((s,x,j)=>s+x*r[j],0)-points[p[t]][i]))));
  return{matrix:Q,assignment:p,error,orth};
 }).filter(m=>det(m.matrix)>0&&m.error<1e-10&&m.orth<1e-10)}
 function model(kind=0,mirror=1,swap=0,angle=0){
  if(![0,1].includes(kind)||![0,1].includes(mirror)||![0,1].includes(swap)||!Number.isFinite(angle)||angle<0||angle>360)throw new RangeError('Parâmetros fora do domínio');
  const labels=kind===0?['A','B','C','D']:['A','A','C','D'];let points=BASE.map(([x,y,z])=>[mirror?-x:x,y,z]);
  if(swap)[points[0],points[1]]=[points[1],points[0]];
  const c=Math.cos(angle*Math.PI/180),s=Math.sin(angle*Math.PI/180);points=points.map(([x,y,z])=>[c*x-s*y,s*x+c*y,z]);
  const matches=matching(points,labels);
  return{kind,mirror,swap,angle,labels,points,orientation:oriented(points),reference:oriented(BASE),proper_count:matches.length,superposable:matches.length>0,match:matches[0]||null};
 }
 function aligned(s){return s.match?s.points.map(r=>[0,1,2].map(i=>s.match.matrix.reduce((a,row,j)=>a+row[i]*r[j],0))):s.points}
 function scene(points,labels,name){
  const a=35*Math.PI/180,b=17*Math.PI/180,e1=[Math.cos(a),-Math.sin(a),0],e2=[Math.sin(a)*Math.sin(b),Math.cos(a)*Math.sin(b),-Math.cos(b)],n=[Math.sin(a)*Math.cos(b),Math.cos(a)*Math.cos(b),Math.sin(b)],dot=(u,v)=>u.reduce((s,x,i)=>s+x*v[i],0);
  const projected=points.map(p=>({x:180+64*dot(e1,p),y:160-64*dot(e2,p),depth:dot(n,p)}));
  const bonds=projected.map(q=>'<line x1="180" y1="160" x2="'+q.x+'" y2="'+q.y+'" stroke="'+(q.depth>=0?'var(--blue)':'var(--ink)')+'" stroke-width="3" '+(q.depth<0?'stroke-dasharray="5 5"':'')+'/>').join('');
  const nodes=projected.map((q,i)=>'<circle cx="'+q.x+'" cy="'+q.y+'" r="14" fill="var(--paper)" stroke="var(--blue)" stroke-width="2"/><text x="'+q.x+'" y="'+(q.y+7)+'" text-anchor="middle">'+labels[i]+'</text>').join('');
  return '<svg class="chirality-scene" viewBox="0 0 360 320" role="img" aria-label="'+name+'">'+bonds+'<circle cx="180" cy="160" r="6" fill="var(--ink)"/>'+nodes+'</svg>';
 }
 function createModels({fmt}){return{chirality:{label:'Compare reflexão, rotação e identidade dos grupos',controls:[['kind','Grupos: 0 A,B,C,D · 1 A,A,C,D',0,1,1,0],['mirror','Reflexão espacial no plano yz: 0 não · 1 sim',0,1,1,1],['swap','Troca formal dos dois primeiros grupos: 0 não · 1 sim',0,1,1,0],['angle','Rotação própria ao redor de z, em graus',0,360,30,0],['align','Mostrar encaixe por rotação: 0 não · 1 sim',0,1,1,0]],render:({kind,mirror,swap,angle,align=0})=>{
  const s=model(kind,mirror,swap,angle),shown=align&&s.superposable?aligned(s):s.points;
  const classification=kind===1?'Neste modelo com dois grupos A idênticos, a imagem é sobreponível por rotação própria: modelo aquiral.':s.superposable?'Mesma configuração da referência; existe uma rotação própria de encaixe.':'Configuração oposta à referência; neste tetraedro com quatro grupos distintos, o par é enantiomérico.';
  const display=align?(s.superposable?'A rotação de encaixe foi aplicada só ao desenho da direita.':'Encaixe solicitado, mas nenhuma rotação própria respeita os grupos; o desenho não foi alinhado.'):'As duas figuras mostram orientações atuais; sobreponibilidade não exige que já pareçam alinhadas.';
  const graph='<p><strong>Grupos abstratos, não símbolos de elementos.</strong> Traço azul contínuo: ramo voltado ao observador; preto tracejado: ramo para trás. São projeções de coordenadas 3D, não espelhos planos da imagem nem desenhos CIP.</p><div class="chirality-pair"><figure><figcaption>Referência</figcaption>'+scene(BASE,s.labels,'Referência tetraédrica')+'</figure><figure><figcaption>'+(align&&s.superposable?'Após encaixe por rotação':'Após operações')+'</figcaption>'+scene(shown,s.labels,'Modelo tetraédrico após operações')+'</figure></div>';
  return{graph:graph+'<table class="truth-table"><caption>Determinantes auxiliares dos marcadores ordenados</caption><thead><tr><th>χ referência</th><th>χ após operações</th><th>Rotação de encaixe</th></tr></thead><tbody><tr><td>16</td><td>'+fmt(s.orientation)+'</td><td>'+(s.match?'det Q=+1':'não existe')+'</td></tr></tbody></table>',report:classification+' '+display+' '+(kind===1?'O sinal de χ não classifica quiralidade quando marcadores distintos representam grupos idênticos.':'Reflexão ou uma troca inverte χ; rotação própria preserva χ. Nenhum sinal foi chamado R ou S.'),note:'Tetraedro regular ideal, um centro e braços sem estrutura interna. O teste enumera correspondências de grupos idênticos, constrói Q, confere QᵀQ=I e det Q=+1 e mapeia todos os vértices; não se baseia em testar alguns ângulos. A troca é formal, sem mecanismo químico. χ depende da ordem dos marcadores e não atribui R/S, sinal óptico ou quiralidade de uma molécula geral. Sem conformações, múltiplos centros, meso ou atividade biológica prevista. Material original em rascunho.'};
 }}}}
 return{BASE,det,oriented,matching,model,aligned,createModels};
})();
