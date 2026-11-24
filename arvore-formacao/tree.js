'use strict';
(function(){
const data=window.FORMATION_DATA, nodes=new Map(data.nodes.map(n=>[n.id,n])), branches=new Map(data.branches.map(b=>[b.id,b]));
const states={done:'Concluído',current:'Em curso',practice:'Experiência registrada',suggested:'Sugerido',history:'Histórico sem conclusão'};
const positions={math:[290,315],physics:[700,220],numerics:[310,570],software:[1040,565],ai:[1110,320],teaching:[1090,790],natural:[290,790]};
const featured={math:['CCM0213','EXP-FOURIER'],physics:['CCM0222','AGA0299'],numerics:['MAP2220','EXP-EM'],software:['EXP-PY','RES-AWS'],ai:['EXP-EVAL','MAC0460'],teaching:['4300356','EXP-EXT'],natural:['CCM0121','CCM0224']};
const $=id=>document.getElementById(id);
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const normalize=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
let branch=null, selected=null, view='tree', query='', filter='all', zoomed=false;
function matches(n){return (filter==='all'||n.state===filter)&&(!query||normalize([n.label,n.summary,n.code,n.kind,n.issuer,n.source].join(' ')).includes(normalize(query)));}
function filtered(){return data.nodes.filter(n=>(!branch||n.branch===branch)&&matches(n));}
function path(d,cl,width){return '<path d="'+d+'" class="'+cl+'"'+(width?' stroke-width="'+width+'"':'')+'/>';}
function mark(n,x,y,size){
const r=size||6;
if(n.state==='practice')return '<rect x="'+(x-r*.75)+'" y="'+(y-r*.75)+'" width="'+r*1.5+'" height="'+r*1.5+'" fill="var(--ink)" transform="rotate(45 '+x+' '+y+')"/>';
let shape='<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="'+(n.state==='done'?'var(--blue)':'var(--paper)')+'" stroke="'+(n.state==='history'?'var(--muted)':'var(--blue)')+'" stroke-width="1.5"'+(n.state==='suggested'?' stroke-dasharray="2 3"':'')+'/>';
if(n.state==='current')shape+='<path d="M '+x+' '+(y-r)+' A '+r+' '+r+' 0 0 0 '+x+' '+(y+r)+' Z" fill="var(--blue)"/>';
if(n.state==='history')shape+='<path d="M '+(x-r*.6)+' '+(y+r*.6)+' L '+(x+r*.6)+' '+(y-r*.6)+'" stroke="var(--muted)"/>';
return shape;
}
function wrap(text,limit){const words=String(text).split(' '),lines=[''];words.forEach(w=>{let i=lines.length-1;if(lines[i]&&lines[i].length+w.length+1>limit)lines.push(w);else lines[i]+=(lines[i]?' ':'')+w;});return lines;}
function nodeSVG(n,x,y,focus){
const brief={'4300356':'Ensino de Física','AGA0299':'Astrofísica galáctica','MAP2220':'Análise Numérica','EXP-PY':'Desenvolvimento com IA'};
const lines=wrap(focus?n.label:(brief[n.id]||n.label),focus?20:22),width=focus?235:205,sel=n.id===selected,lineHeight=focus?26:21;
let result='<g class="node '+(focus?'node-focus ':'')+(sel?'selected':'')+'" role="button" tabindex="0" data-node="'+escape(n.id)+'" aria-label="'+escape(n.label+', '+states[n.state])+'">';
result+='<title>'+escape(n.label+' · '+states[n.state])+'</title><rect class="node-hit" x="'+(x-width/2)+'" y="'+(y-18)+'" width="'+width+'" height="'+(45+lines.length*lineHeight)+'" rx="4"/>';
result+=mark(n,x,y,focus?8:6);
lines.forEach((line,i)=>{result+='<text x="'+x+'" y="'+(y+26+i*lineHeight)+'" text-anchor="middle">'+escape(line)+'</text>';});
result+='<text class="minor-label" x="'+x+'" y="'+(y+30+lines.length*lineHeight)+'" text-anchor="middle">'+escape(n.code||n.kind)+'</text></g>';
return result;
}
const relationLabels={foundation:'Base cursada',practice:'Experiência relacionada',growth:'Aprofundamento',requirement:'Requisito condicionado',alternative:'Alternativa / complemento'};
function curveTwig(x,y,angle,length,width,depth,seed){
 if(depth<0||length<8)return '';
 const bend=Math.sin(seed*3.17)*.28,ex=x+Math.cos(angle)*length,ey=y+Math.sin(angle)*length;
 let out=path('M'+x.toFixed(1)+' '+y.toFixed(1)+' Q'+(x+Math.cos(angle+bend)*length*.55).toFixed(1)+' '+(y+Math.sin(angle+bend)*length*.55).toFixed(1)+' '+ex.toFixed(1)+' '+ey.toFixed(1),'organic-twig',width.toFixed(2));
 if(depth===0){
  out+='<ellipse class="organic-leaf" cx="'+ex.toFixed(1)+'" cy="'+ey.toFixed(1)+'" rx="3.6" ry="10" transform="rotate('+(angle*180/Math.PI+90).toFixed(1)+' '+ex.toFixed(1)+' '+ey.toFixed(1)+')"/>';
 }else{
  out+=curveTwig(ex,ey,angle-.38-Math.sin(seed)*.12,length*.69,width*.62,depth-1,seed+1.71);
  out+=curveTwig(ex,ey,angle+.45+Math.cos(seed)*.13,length*.65,width*.58,depth-1,seed+3.13);
 }
 return out;
}
function treeDefs(){
 return '<defs><marker id="relation-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L6 3.5 L0 7" fill="none" stroke="var(--blue)" stroke-width="1.2"/></marker></defs>';
}
function organicTrunk(){
 let out='<path class="organic-trunk" d="M645 912 C676 812 619 760 668 632 C699 545 650 479 681 390 C709 306 668 260 700 187 C692 301 751 345 716 457 C694 535 752 596 707 677 C676 745 735 832 752 921 C718 889 679 893 645 912Z"/>';
 ['M666 885 C707 790 653 745 683 655 C718 566 682 516 701 430',
  'M695 891 C674 805 709 770 696 714 C682 659 724 628 710 568',
  'M713 880 C711 833 684 801 690 765',
  'M681 594 C692 540 676 494 693 454',
  'M700 398 C715 358 688 305 698 260'].forEach(d=>{out+=path(d,'bark-grain',1.8);});
 return out;
}
function roots(){
 let out='<g class="organic-roots">';
 const main=[
 ['M675 865 C654 920 569 944 511 978 C456 1013 395 988 337 1044 C302 1078 245 1084 190 1135',14],
 ['M714 876 C757 922 815 923 869 971 C922 1016 1004 1006 1040 1056 C1073 1102 1153 1077 1204 1135',13],
 ['M692 890 C683 951 726 979 700 1038 C675 1095 729 1133 687 1190',13],
 ['M676 917 C650 956 588 976 593 1039 C595 1085 538 1115 550 1166',8],
 ['M737 935 C768 978 799 1004 775 1055 C748 1114 817 1142 825 1180',7],
 ['M574 946 C552 1000 472 1044 467 1115',6],
 ['M853 958 C883 1000 916 1073 887 1135',6]];
 main.forEach(([d,w])=>{out+=path(d,'root-bark',w);});
 for(let i=0;i<10;i++){
  const side=i%2?-1:1,x=700+side*(95+Math.floor(i/2)*77),y=985+(i%3)*40;
  out+=curveTwig(x,y,side<0?2.1:1.03,62+(i%3)*14,2.4,3,21+i);
 }
 out+='</g><text class="tree-foot" x="700" y="1218" text-anchor="middle">Ciências Moleculares / USP</text><text class="branch-caption" x="700" y="1242" text-anchor="middle">A base interdisciplinar da trajetória</text>';
 return out;
}
function treeAtmosphere(){
 return '<circle class="tree-orbit" cx="700" cy="530" r="520"/><path class="tree-orbit" d="M145 903 Q700 989 1255 903"/>';
}
function drawOverview(){
 let out='<svg viewBox="0 0 1400 1270" role="group" aria-label="Yggdrasil da formação com sete áreas">'+treeDefs()+'<g class="tree-shape">';
 out+=treeAtmosphere()+roots()+organicTrunk();
 const routes={
 math:'M692 620 C621 577 612 495 493 465 C398 440 383 371 290 315',
 physics:'M698 520 C764 433 655 360 700 220',
 numerics:'M682 710 C585 673 483 701 424 635 C386 591 355 600 310 570',
 software:'M705 700 C769 644 851 668 914 630 C969 597 1007 604 1040 565',
 ai:'M714 608 C815 541 799 470 937 426 C1032 397 1063 351 1110 320',
 teaching:'M704 839 C810 809 891 878 978 825 C1020 800 1060 820 1090 790',
 natural:'M682 832 C589 779 497 859 405 816 C353 792 326 811 290 790'};
 const allPoints=new Map(),body=[],groups=[];
 data.branches.forEach((b,i)=>{
  const [x,y]=positions[b.id],group=data.nodes.filter(n=>n.branch===b.id&&matches(n));
  const opacity=group.length?1:.16;
  out+='<g opacity="'+opacity+'">'+path(routes[b.id],'organic-branch',b.id==='physics'?10:12);
  for(let k=0;k<5;k++){
   const angle=-Math.PI/2+(k-2)*.45;
   out+=curveTwig(x+(k-2)*25,y+25,angle,72+(i%3)*9,3.2,3,i*13+k+2);
  }
  out+='</g>';
  const picks=(!query&&filter==='all'?featured[b.id].map(id=>nodes.get(id)).filter(Boolean):group.slice(0,2));
  picks.forEach((n,j)=>{
   const nx=x+(j===0?-95:110),ny=y-113-(j===1?34:0);allPoints.set(n.id,[nx,ny]);
   body.push('<g opacity="'+opacity+'">'+nodeSVG(n,nx,ny,false)+'</g>');
  });
  let control='<g class="branch-control" role="button" tabindex="0" data-branch="'+b.id+'" aria-label="Explorar '+escape(b.label)+'"><circle class="branch-ring" cx="'+x+'" cy="'+y+'" r="16"/><path d="M'+(x-4)+' '+y+' h8 M'+x+' '+(y-4)+' v8" stroke="var(--blue)" stroke-width="1.3"/>';
  const lines=wrap(b.label,23),labelY=y+44;
  control+='<rect class="label-paper" x="'+(x-160)+'" y="'+(labelY-23)+'" width="320" height="'+(46+lines.length*27)+'" rx="20"/><text class="branch-label" x="'+x+'" y="'+labelY+'" text-anchor="middle">';
  lines.forEach((line,j)=>{control+='<tspan x="'+x+'" dy="'+(j?27:0)+'">'+escape(line)+'</tspan>';});
  control+='</text><text class="branch-caption" x="'+x+'" y="'+(labelY+22+(lines.length-1)*27)+'" text-anchor="middle">'+group.length+' registros · explorar ↗</text></g>';
  groups.push('<g opacity="'+opacity+'">'+control+'</g>');
 });
 data.edges.filter(e=>allPoints.has(e.source)&&allPoints.has(e.target)).forEach(e=>{
  const [ax,ay]=allPoints.get(e.source),[bx,by]=allPoints.get(e.target);
  out+=path('M'+ax+' '+ay+' Q'+((ax+bx)/2)+' '+(Math.min(ay,by)-60)+' '+bx+' '+by,'overview-relation',1.6);
 });
 out+=body.join('')+groups.join('')+'</g></svg>';
 if(!data.nodes.some(matches))out='<div class="empty">Nenhum registro encontrado.<br>Tente outra busca ou limpe os filtros.</div>';
 $('graph').innerHTML=out;
}
function connectedTo(id){return data.edges.filter(e=>e.source===id||e.target===id);}
function drawConnections(){
 const n=nodes.get(selected);
 if(!n){drawOverview();return;}
 const edges=connectedTo(n.id),related=[...new Set(edges.map(e=>e.source===n.id?e.target:e.source))].map(id=>nodes.get(id));
 const categories=[
  {key:'done',label:'FORMAÇÃO CONCLUÍDA',items:related.filter(x=>x.state==='done'),y:1020},
  {key:'suggested',label:'APROFUNDAMENTOS POSSÍVEIS',items:related.filter(x=>x.state==='suggested'),y:220},
  {key:'practice',label:'PRÁTICA E PERCURSO',items:related.filter(x=>!['done','suggested'].includes(x.state)),y:560}];
 const points=new Map([[n.id,[700,665]]]);
 let out='<svg viewBox="0 0 1400 1320" role="group" aria-label="Conexões de '+escape(n.label)+'">'+treeDefs()+'<g class="tree-shape">'+treeAtmosphere();
 out+='<g class="connection-tree">'+roots()+organicTrunk()+'</g>';
 categories.forEach(c=>{
  if(!c.items.length)return;
  const cols=Math.min(4,c.items.length);
  c.items.forEach((item,i)=>{
   let x,y;
   if(c.key==='practice'){x=i%2?1125:275;y=c.y+Math.floor(i/2)*175;}
   else{const row=Math.floor(i/cols),itemsRow=Math.min(cols,c.items.length-row*cols);x=700+(i%cols-(itemsRow-1)/2)*290;y=c.y+row*180;}
   points.set(item.id,[x,y]);
  });
  const labelY=c.key==='done'?980:c.key==='suggested'?115:465;
  out+='<text class="connection-heading" x="700" y="'+labelY+'" text-anchor="middle">'+c.label+'</text>';
 });
 edges.forEach(e=>{
  const a=points.get(e.source),b=points.get(e.target);
  if(!a||!b)return;
  const d='M'+a[0]+' '+a[1]+' C'+(a[0]*.72+700*.28)+' '+(a[1]+(b[1]>a[1]?100:-100))+' '+(b[0]*.72+700*.28)+' '+(b[1]+(b[1]>a[1]?-100:100))+' '+b[0]+' '+b[1];
  out+='<g class="connection-line '+escape(e.type||'growth')+'"><title>'+escape(nodes.get(e.source).label+' ↔ '+nodes.get(e.target).label+': '+e.relation)+'</title><path d="'+d+'"'+(e.type==='requirement'?' marker-end="url(#relation-arrow)"':'')+'/></g>';
 });
 related.forEach(item=>{const p=points.get(item.id);out+=nodeSVG(item,p[0],p[1],true);});
 out+='<g class="knowledge-center"><rect x="485" y="635" width="430" height="'+(75+wrap(n.label,20).length*26)+'" rx="42"/>'+nodeSVG(n,700,670,true)+'</g>';
 if(!edges.length)out+='<text class="branch-caption" x="700" y="460" text-anchor="middle">Nenhuma conexão formativa registrada para este nó.</text>';
 out+='</g></svg>';$('graph').innerHTML=out;
}
function drawBranch(){
let group=filtered();if(!group.length){$('graph').innerHTML='<div class="empty">Nenhum registro neste ramo com os filtros atuais.</div>';return;}
const nsel=selected?nodes.get(selected):null;
let chosen=group.slice(0,10);
if(nsel&&group.includes(nsel)&&!chosen.includes(nsel))chosen[chosen.length-1]=nsel;
const points=new Map(),count=chosen.length,cols=Math.min(5,count),rows=Math.ceil(count/cols);
let out='<svg viewBox="0 0 1400 1270" role="group" aria-label="Registros do ramo '+escape(branches.get(branch).label)+'"><g class="tree-shape">';
out+='<text class="canopy-caption" x="700" y="95" text-anchor="middle">FORMAÇÃO · EXPERIÊNCIA · POSSIBILIDADES</text>';
chosen.forEach((n,i)=>{
const row=Math.floor(i/cols),col=i%cols,numInRow=Math.min(cols,count-row*cols),x=700+(col-(numInRow-1)/2)*248,y=rows===1?320:215+row*255;points.set(n.id,[x,y]);
out+=path('M700 850 C'+(665+i*4)+' 745 '+(x+65)+' '+(y+260)+' '+(x-24)+' '+(y+160)+' C'+(x-48)+' '+(y+85)+' '+(x+28)+' '+(y+65)+' '+x+' '+y,'organic-branch',row===0?3:5);out+=curveTwig(x,y+85,-Math.PI/2,48,1.8,2,30+i);
for(let j=0;j<4;j++){const side=j%2?1:-1;out+=path('M'+x+' '+(y+100+j*35)+' q'+side*25+' -35 '+side*45+' -48','twig');}
});
out+=roots();
out+='<text class="draw-title" x="700" y="765" text-anchor="middle">'+escape(branches.get(branch).label)+'</text>';
if(group.length>10)out+='<text class="branch-caption" x="700" y="798" text-anchor="middle">10 de '+group.length+' registros · todos disponíveis no inventário</text>';
data.edges.filter(e=>(e.source===selected||e.target===selected)&&points.has(e.source)&&points.has(e.target)).forEach(e=>{
const [ax,ay]=points.get(e.source),[bx,by]=points.get(e.target);
out+=path('M'+ax+' '+(ay-15)+' Q'+((ax+bx)/2)+' '+(Math.min(ay,by)-95)+' '+bx+' '+(by-15),'node-link');
});
chosen.forEach(n=>{const p=points.get(n.id);out+=nodeSVG(n,p[0],p[1],true);});
out+='</g></svg>';$('graph').innerHTML=out;
}
function makeButton(text,cl,action){const el=document.createElement('button');el.type='button';el.className=cl;el.textContent=text;el.addEventListener('click',action);return el;}
function selectNode(id){const n=nodes.get(id);if(!n)return;selected=id;branch=n.branch;if(view!=='list'){view='links';query='';filter='all';$('search').value='';$('state').value='all';}render();if(window.innerWidth<760)$('inspector').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth',block:'start'});}
function selectBranch(id){branch=id;selected=null;view='tree';render();}
function inspector(){
const box=$('inspector');box.replaceChildren();
if(selected){
const n=nodes.get(selected);box.append(makeButton('← Explorar o ramo','back',()=>{selected=null;view='tree';render();}));
const kicker=document.createElement('p');kicker.className='kicker';kicker.textContent=branches.get(n.branch).label+' / '+n.kind;
const title=document.createElement('h2');title.textContent=n.label;
const status=document.createElement('p');status.className='status-label';status.innerHTML='<i class="mark '+n.state+'"></i>'+escape(states[n.state]);
const summary=document.createElement('p');summary.className='description';summary.textContent=n.summary;
box.append(kicker,title,status,summary);
const dl=document.createElement('dl');
[['Código',n.code],['Vínculo',n.bond==='CM'?'Ciências Moleculares':n.bond==='IF'?'Instituto de Física':n.bond],['Instituição',n.issuer],['Data de conclusão',n.date],['Carga indicada',n.hours],['Acesso',n.cost],['Prioridade de avaliação',n.priority],['Registro',n.state==='history'?n.statusDetail:null],['Fonte',n.source]].filter(pair=>pair[1]).forEach(([a,b])=>{const dt=document.createElement('dt');dt.textContent=a;const dd=document.createElement('dd');dd.textContent=b;dl.append(dt,dd);});box.append(dl);
if(n.url&&n.url.startsWith('https://')){const link=document.createElement('a');link.className='external';link.href=n.url;link.target='_blank';link.rel='noopener noreferrer';link.textContent=n.kind.includes('Disciplina')||n.code?'Consultar ementa oficial ↗':'Consultar o recurso ↗';box.append(link);}
const note=document.createElement('p');note.className='caveat';note.textContent=n.sourceNote||'Domínio atual ainda não avaliado.';box.append(note);
box.append(makeButton('Ver conexões no mapa ↗','connection-action',()=>{view='links';query='';filter='all';$('search').value='';$('state').value='all';render();}));const connections=connectedTo(n.id);
if(connections.length){const h=document.createElement('h3');h.className='connection-title';h.textContent='Conexões deste conhecimento';box.append(h);
connections.forEach(e=>{const other=nodes.get(e.source===n.id?e.target:e.source),btn=makeButton(other.label,'relation-button',()=>{query='';filter='all';$('search').value='';$('state').value='all';selectNode(other.id);});const dot=document.createElement('i');dot.className='mark '+other.state;btn.prepend(dot);const hint=document.createElement('small');hint.textContent=states[other.state]+' · '+e.relation;btn.append(hint);box.append(btn);});}
return;
}
const k=document.createElement('p');k.className='kicker';k.textContent=branch?'UM RAMO DA TRAJETÓRIA':'RAÍZES → FORMAÇÃO → CAMINHOS';
const title=document.createElement('h2');title.textContent=branch?branches.get(branch).label:'Conhecimento que se conecta.';
const description=document.createElement('p');description.className='description';description.textContent=branch?'Explore os registros deste ramo. Cada nó distingue formação, prática e possibilidades futuras.':'A base interdisciplinar sustenta a pesquisa e o desenvolvimento. Escolha um ramo para ver de onde vem a formação e onde ela pode crescer.';
box.append(k,title,description);
if(!branch){
const nav=document.createElement('div');nav.className='branch-navigation';
data.branches.forEach(b=>{const num=data.nodes.filter(n=>n.branch===b.id&&matches(n)).length,btn=makeButton(b.label,'',()=>selectBranch(b.id)),count=document.createElement('small');count.textContent=String(num);btn.append(count);nav.append(btn);});box.append(nav);
}else{
const h=document.createElement('h3');h.className='branch-items-title';h.textContent='Registros neste ramo';box.append(h);
filtered().slice(0,12).forEach(n=>{const btn=makeButton('','item-button',()=>selectNode(n.id)),dot=document.createElement('i');dot.className='mark '+n.state;const text=document.createElement('span');text.textContent=n.label;btn.append(dot,text);box.append(btn);});
if(filtered().length>12)box.append(makeButton('Ver todos no inventário ↗','more',()=>{view='list';render();}));
}
const note=document.createElement('p');note.className='caveat';note.textContent='Base conferida em '+data.updated+'. Formação concluída não mede domínio. Sugestões dependem de escolha, oferta e requisitos.';box.append(note);
}
function inventory(){
const root=$('inventory');root.replaceChildren();const head=document.createElement('div');head.className='inventory-head';head.innerHTML='<span>FORMAÇÃO / CONHECIMENTO</span><span>ESTADO</span><span>TIPO</span>';root.append(head);
const found=filtered();
if(!found.length){const empty=document.createElement('p');empty.className='empty';empty.textContent='Nenhum registro com esses filtros.';root.append(empty);}
found.forEach(n=>{
const btn=makeButton('','inventory-row'+(selected===n.id?' active':''),()=>selectNode(n.id));
const name=document.createElement('span');name.textContent=n.label;const sub=document.createElement('small');sub.textContent=(n.code?n.code+' · ':'')+branches.get(n.branch).label;name.append(sub);
const state=document.createElement('span');state.className='row-status';state.innerHTML='<i class="mark '+n.state+'"></i>'+escape(states[n.state]);
const kind=document.createElement('span');kind.className='row-kind';kind.textContent=n.kind;btn.append(name,state,kind);root.append(btn);
});
}
function bindGraph(){
$('graph').querySelectorAll('[data-node],[data-branch]').forEach(g=>{
const activate=()=>g.dataset.node?selectNode(g.dataset.node):selectBranch(g.dataset.branch);
g.addEventListener('click',activate);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();activate();}});
});
}
function render(){
$('tree-view').setAttribute('aria-pressed',String(view==='tree'));$('list-view').setAttribute('aria-pressed',String(view==='list'));$('links-view').setAttribute('aria-pressed',String(view==='links'));
$('graph').hidden=view==='list';$('graph').classList.toggle('zoomed',zoomed);$('zoom').hidden=view==='list';$('zoom').setAttribute('aria-pressed',String(zoomed));$('zoom').textContent=zoomed?'Enquadrar desenho −':'Ampliar desenho +';$('inventory').hidden=view!=='list';$('overview').hidden=!branch;
$('map-title').textContent=view==='links'&&selected?'Conexões de '+nodes.get(selected).label:branch?branches.get(branch).label:'A árvore inteira';
$('result-count').textContent=filtered().length+' registro'+(filtered().length===1?'':'s')+(query||filter!=='all'?' encontrados':'');
if(view!=='list'){view==='links'?drawConnections():branch?drawBranch():drawOverview();bindGraph();}else inventory();$('relation-legend').hidden=view!=='links';if(view==='links'&&selected)$('result-count').textContent=connectedTo(selected).length+' conexões';
inspector();
if(window.innerWidth<760&&view!=='list')requestAnimationFrame(()=>{$('graph').scrollLeft=($('graph').scrollWidth-$('graph').clientWidth)/2;});
}
$('zoom').addEventListener('click',()=>{zoomed=!zoomed;render();});
$('tree-view').addEventListener('click',()=>{view='tree';render();});$('list-view').addEventListener('click',()=>{view='list';render();});
$('overview').addEventListener('click',()=>{branch=null;selected=null;view='tree';render();});
$('search').addEventListener('input',e=>{query=e.target.value;branch=null;selected=null;if(view==='links')view='tree';render();});
$('state').addEventListener('change',e=>{filter=e.target.value;selected=null;if(view==='links')view='tree';render();});
$('reset').addEventListener('click',()=>{branch=null;selected=null;query='';filter='all';if(view==='links')view='tree';$('search').value='';$('state').value='all';render();});
$('links-view').addEventListener('click',()=>{if(!selected){const first=nodes.get('EXP-EM');selected=first.id;branch=first.branch;}query='';filter='all';$('search').value='';$('state').value='all';view='links';render();});
$('export').addEventListener('click',()=>{const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download='jhuann-arvore-formacao.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);$('export-status').textContent='Arquivo preparado com registros e conexões.';});
render();
})();
