/* Vesícula esférica ideal: áreas dos folhetos; sem auto-organização ou transporte. */
window.VesicleLeafletModels=(()=>{
 function model(radius=20,thickness=4){
  if(!Number.isInteger(radius)||radius<10||radius>100||radius%10!==0||![2,4,6].includes(thickness))throw new RangeError('Raio 10–100 em passos de 10; separação 2, 4 ou 6');
  const outer=radius+thickness,ratio=outer*outer/(radius*radius);
  return{radius,thickness,outer,inner_area:4*Math.PI*radius**2,outer_area:4*Math.PI*outer**2,lumen_volume:4*Math.PI*radius**3/3,shell_volume:4*Math.PI*(outer**3-radius**3)/3,ratio,relative_excess:thickness*(2*radius+thickness)/(radius*radius),outer_fraction:outer*outer/(outer*outer+radius*radius)};
 }
 function createModels({fmt}){return{vesicleLeaflets:{label:'Compare as áreas das duas superfícies',controls:[['radius','Raio da superfície interna r (nm)',10,100,10,20],['thickness','Separação entre superfícies d (nm)',2,6,2,4]],render:({radius,thickness})=>{
  const s=model(radius,thickness),ro=155,ri=ro*radius/s.outer,gap=ro-ri;
  let svg='<svg class="vesicle-leaflet-scene" viewBox="0 0 600 520" role="img" aria-label="Corte de vesícula ideal, cabeças nas superfícies interna e externa e caudas na casca entre elas"><text x="300" y="28" text-anchor="middle">Corte esquemático · raios proporcionais</text><text x="300" y="62" text-anchor="middle">Água externa</text><circle cx="300" cy="245" r="'+ro+'" fill="var(--ink)" fill-opacity=".08" stroke="var(--blue)" stroke-width="2"/><circle cx="300" cy="245" r="'+ri+'" fill="var(--paper,#f2f1e6)" stroke="var(--blue)" stroke-width="2"/><circle cx="300" cy="245" r="'+ri+'" fill="var(--blue)" fill-opacity=".06"/>';
  for(const inner of [false,true])for(let i=0;i<16;i++){
   const a=2*Math.PI*(i+(inner?.25:0))/16,r=inner?ri:ro,direction=inner?1:-1,x=300+r*Math.cos(a),y=245+r*Math.sin(a),end=r+direction*gap*.43;
   for(const off of [-.014,.014])svg+='<line x1="'+x+'" y1="'+y+'" x2="'+(300+end*Math.cos(a+off))+'" y2="'+(245+end*Math.sin(a+off))+'" stroke="var(--ink)" stroke-width="2"/>';
   svg+='<circle cx="'+x+'" cy="'+y+'" r="3.5" fill="var(--blue)"/>';
  }
  svg+='<text x="300" y="239" text-anchor="middle">Cavidade</text><text x="300" y="268" text-anchor="middle">aquosa</text><text x="300" y="441" text-anchor="middle">Pontos: cabeças · traços: caudas</text><text x="300" y="480" text-anchor="middle">Símbolos indicam orientação, não quantidade</text></svg>';
  return{graph:svg+'<p>O desenho é um corte, mas as contas usam duas superfícies esféricas completas: interna de raio r e externa de raio r+d. Cabeças internas olham para a cavidade; caudas dos dois folhetos entram na casca. O tamanho do desenho se ajusta à tela; símbolos não contam moléculas.</p>',report:'r='+radius+' nm; d='+thickness+' nm; raio externo='+s.outer+' nm. A externa/A interna='+fmt(s.ratio)+'; excesso relativo de área externa='+fmt(100*s.relative_excess)+'%. Áreas interna/externa: '+fmt(s.inner_area)+' / '+fmt(s.outer_area)+' nm². Com mesma área média por molécula nos dois folhetos, a fração externa estimada seria '+fmt(s.outer_fraction)+'.',note:'Geometria ideal, não uma formação espontânea ou membrana medida. d é separação escolhida entre superfícies, sem valor experimental inferido. A desigualdade de áreas não determina composição, empacotamento, energia, estabilidade, permeabilidade ou fluxo. Proteínas, cargas e dinâmica foram omitidas. O núcleo da micela simples é hidrofóbico; a cavidade desta vesícula é aquosa.'};
 }}};}
 return{model,createModels};
})();
