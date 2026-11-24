/* MathML declarativo: sem interpretação de HTML, TeX ou código do conteúdo. */
window.LessonMath=(()=>{
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function node(value,depth=0){
  if(depth>20)throw Error('Fórmula muito profunda');
  if(typeof value==='number'){if(!Number.isFinite(value))throw Error('Número inválido');return`<mn>${value}</mn>`;}
  if(typeof value==='string'){
   const tag=/^[A-Za-zΑ-ω](?:′|″)?$/.test(value)||['sin','cos','ln','exp'].includes(value)?'mi':/^[=+−×·<>≤≥→∘(),|]$/.test(value)?'mo':'mtext';
   return`<${tag}${['sin','cos','ln','exp'].includes(value)?' mathvariant="normal"':''}>${esc(value)}</${tag}>`;
  }
  if(!Array.isArray(value)||!value.length)throw Error('Estrutura inválida');
  const [type,...args]=value;
  if(type==='matrix'){
   if(!args.length||args.length>20||!Array.isArray(args[0])||!args[0].length||args[0].length>20||args.some(row=>!Array.isArray(row)||row.length!==args[0].length))throw Error('Matriz inválida');
   return`<mrow><mo>[</mo><mtable>${args.map(row=>`<mtr>${row.map(x=>`<mtd>${node(x,depth+1)}</mtd>`).join('')}</mtr>`).join('')}</mtable><mo>]</mo></mrow>`;
  }

  const tags={row:'mrow',frac:'mfrac',sup:'msup',sub:'msub',sqrt:'msqrt',int:'msubsup'};
  if(!Object.hasOwn(tags,type)||args.length>100)throw Error('Operação inválida');
  if(['frac','sup','sub','int'].includes(type)&&args.length!==2)throw Error('Aridade inválida');
  if(type==='sqrt'&&args.length!==1)throw Error('Aridade inválida');
  const tag=tags[type],prefix=type==='int'?'<mo>∫</mo>':'';
  return`<${tag}>${prefix}${args.map(x=>node(x,depth+1)).join('')}</${tag}>`;
 }
 let equationId=0;
 function equation(section){
  if(!section.formula)return'';
  let body;
  if(section.formulaMath){try{body=`<div class="equation math-equation" tabindex="0"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block" aria-label="${esc(section.formula)}">${node(section.formulaMath)}</math></div>`;}catch{/* Texto escapado preservado se a estrutura não for válida. */}}
  if(!body)body=`<div class="equation" role="math" tabindex="0" aria-label="${esc(section.formula)}">${esc(section.formula)}</div>`;
  const helpId=`equation-scroll-help-${++equationId}`;
  return`<div class="equation-frame">${body}<p class="equation-scroll-help" id="${helpId}" hidden>Fórmula extensa: deslize na horizontal ou, com o foco, use ← e →.</p></div>`;
 }
 function enhance(root){
  const frames=Array.from(root.querySelectorAll('.equation-frame'));
  let active=true;
  const update=()=>{
   if(!active)return;
   for(const frame of frames){
    const equation=frame.querySelector('.equation'),help=frame.querySelector('.equation-scroll-help');
    const wide=equation.clientWidth>0&&equation.scrollWidth>equation.clientWidth+1;
    equation.tabIndex=wide?0:-1;
    equation.classList.toggle('is-scrollable',wide);
    help.hidden=!wide;
    if(wide)equation.setAttribute('aria-describedby',help.id);
    else equation.removeAttribute('aria-describedby');
   }
  };
  update();
  const observer=window.ResizeObserver?new window.ResizeObserver(update):null;
  if(observer)frames.forEach(frame=>observer.observe(frame.querySelector('.equation')));
  else window.addEventListener?.('resize',update);
  root.ownerDocument?.fonts?.ready?.then(update);
  return()=>{active=false;observer?.disconnect();if(!observer)window.removeEventListener?.('resize',update)};
 }
 return{node,equation,enhance};
})();
