/* Esquema próprio de polaridades; uma forquilha, sem sequência, velocidade ou escala. */
window.ReplicationOrientationModels=(()=>{
 function model(direction=1){
  if(!Number.isInteger(direction)||![-1,1].includes(direction))throw new RangeError('Sentido -1 ou +1.');
  return{direction,leading:direction===1?'inferior':'superior',lagging:direction===1?'superior':'inferior',leadingGrowth:direction,laggingGrowth:-direction};
 }
 function diagram(z){
  const right=z.direction===1,forkX=right?280:140;
  let body=`<text x="210" y="26" text-anchor="middle">Forquilha ${right?'→ direita':'← esquerda'}</text><line x1="${forkX}" y1="52" x2="${forkX}" y2="299" class="replication-front"/>`;
  [['superior',80,'5′','3′'],['inferior',280,'3′','5′']].forEach(([name,y,left,rightEnd])=>{
   body+=`<text x="35" y="${y-19}">Molde ${name} · parental</text><line x1="45" y1="${y}" x2="375" y2="${y}" class="replication-template"/><text x="15" y="${y+5}">${left}</text><text x="382" y="${y+5}">${rightEnd}</text>`;
   const leading=z.leading===name,ny=name==='superior'?120:230,growth=leading?z.leadingGrowth:z.laggingGrowth;
   const spans=leading?[[right?60:160,right?260:370]]:right?[[60,110],[135,185],[210,260]]:[[160,210],[235,285],[310,360]];
   spans.forEach(([a,b])=>{const start=growth===1?a:b,end=growth===1?b:a;body+=`<line x1="${start}" y1="${ny}" x2="${end}" y2="${ny}" class="replication-new" marker-end="url(#replication-poly-arrow)"/><text x="${start}" y="${ny-10}" text-anchor="middle" class="replication-end">5′</text><text x="${end}" y="${ny-10}" text-anchor="middle" class="replication-end">3′</text>`;});
   body+=`<text x="35" y="${name==='superior'?155:197}">${leading?'Contínua (líder)':'Descontínua (fragmentos)'}: ${growth===1?'síntese →':'síntese ←'}</text>`;
  });
  body+='<text x="210" y="330" text-anchor="middle">Azul: fitas novas · cada seta indica síntese 5′→3′</text>';
  return `<svg viewBox="0 0 420 350" role="img" aria-label="Orientação das fitas parentais e síntese das fitas novas, também descritas na tabela"><defs><marker id="replication-poly-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1957d6"/></marker></defs>${body}</svg>`;
 }
 function createModels(){return{replicationOrientation:{label:'A fita líder depende do sentido da forquilha',controls:[['direction','Forquilha: −1 esquerda; +1 direita',-1,1,2,1]],render:({direction})=>{
  const z=model(direction),arrow=d=>d===1?'direita →':'esquerda ←';
  return{graph:`<div class="replication-orientation-panel">${diagram(z)}<p class="caption">Esquema de uma única forquilha, sem escala ou geometria helicoidal. Moldes fixos: superior 5′ à esquerda e 3′ à direita; inferior antiparalelo. Tracejado marca uma frente esquemática. As três setas descontínuas são ilustração de fragmentos, não contagem prevista ou cronologia real.</p><table class="truth-table"><caption>Síntese sempre 5′→3′; direção espacial depende do molde</caption><tbody><tr><th>Avanço da forquilha</th><td>${arrow(direction)}</td></tr><tr><th>Molde da fita contínua</th><td>${z.leading}</td></tr><tr><th>Alongamento contínuo</th><td>${arrow(z.leadingGrowth)}</td></tr><tr><th>Molde dos fragmentos</th><td>${z.lagging}</td></tr><tr><th>Alongamento dos fragmentos</th><td>${arrow(z.laggingGrowth)}</td></tr></tbody></table></div>`,report:`Forquilha para a ${direction===1?'direita':'esquerda'}: o molde ${z.leading} sustenta a filha contínua; o ${z.lagging} sustenta os fragmentos. Cada segmento novo cresce pela extremidade 3′. Inverter a direção da forquilha troca os papéis, mantendo a orientação dos moldes.`,note:'Não é animação molecular nem modelo de taxas. Iniciadores, remoção/substituição, ligação entre fragmentos, proteínas acessórias, topologia, origens e terminação não são representados. “Contínua” e “descontínua” descrevem a síntese relativa a esta forquilha, não propriedades permanentes de toda a fita.'};
 }}};}
 return{model,createModels};
})();
