/* Páginas profissionais do portfólio: Desenvolvimento, Pesquisa e Formação.
   Carregado antes de app.js; usa os auxiliares globais de app.js (intro, sectionLabel, contactCTA) só no momento da renderização.
   Fatos vêm dos repositórios e do registro acadêmico; nada aqui afirma resultado, domínio ou publicação sem evidência. */
const GITHUB = 'https://github.com/jhuannP';

const projects = [
  { id: 'biblioteca', kind: 'Produto próprio · em revisão', title: 'Portfólio e biblioteca didática',
    lead: 'Este site: uma biblioteca de estudo navegável, com correção de exercícios no servidor e simulações no navegador.',
    built: ['Servidor em Python (biblioteca padrão) com API de catálogo e de correção', 'Interface em JavaScript sem etapa de build', 'Mais de 100 modelos de simulação e laboratórios', 'Testes automatizados em Python e Node'],
    stack: ['Python', 'JavaScript', 'HTML/CSS', 'MathML', 'testes'],
    stat: [['51', 'trilhas'], ['664', 'aulas em rascunho']],
    links: [['Abrir a biblioteca', '#biblioteca'], ['Ver três exemplos', '#exemplos']],
    note: 'Repositório privado. Conteúdo didático gerado com apoio de IA e ainda em revisão.' },
  { id: 'aga', kind: 'Ferramenta de estudo · 2026/2', title: 'Notas interativas de Astrofísica Galáctica',
    lead: 'Um gerador que transforma o caderno em LaTeX de AGA0299 em um site de capítulos, com figuras que se mexem.',
    built: ['Script Python de LaTeX para HTML', '8 capítulos com notas no formato Cornell', '12 simulações em canvas (rotação, Hubble, Sérsic…)', 'Tema claro e escuro, fórmulas com KaTeX'],
    stack: ['Python', 'LaTeX', 'JavaScript', 'Canvas', 'KaTeX'],
    stat: [['8', 'capítulos'], ['12', 'simulações']],
    links: [['Abrir as notas', 'disciplinas/aga0299/']],
    note: 'Notas de estudo, não material oficial da disciplina.' },
  { id: 'som', kind: 'Projeto em grupo · público', title: 'Desenhe o som',
    lead: 'Protótipo para um seminário sobre tecnologias no ensino de Física: ondas, harmônicos e sonificação de desenhos e pinturas.',
    built: ['Três modos: onda periódica com espectro, desenho livre, quadros em domínio público', 'A regra de tradução imagem → som fica sempre visível', 'Testado em desktop e celular (375 px)'],
    stack: ['HTML', 'JavaScript', 'áudio no navegador', 'GitHub Pages'],
    stat: [['3', 'modos'], ['27', 'quadros sonificados']],
    links: [['Abrir o site', 'https://jhuannp.github.io/desenhe-o-som/'], ['Código', `${GITHUB}/desenhe-o-som`]],
    note: 'Trabalho coletivo do Grupo 6; as contribuições de cada integrante estão documentadas no repositório.' },
  { id: 'wf', kind: 'Modelagem · disciplina', title: 'Seleção flutuante sazonal',
    lead: 'Simulações de frequência alélica em populações finitas, comparando deriva pura, seleção constante e seleção que oscila com as estações.',
    built: ['Wright–Fisher discreto com amostragem binomial', 'Versão contínua por aproximação de difusão', 'EDE integrada por Euler–Maruyama'],
    stack: ['Python', 'EDEs', 'Monte Carlo'],
    stat: [['3', 'cenários']],
    links: [['Código', `${GITHUB}/Modelagem-de-Selecao-Flutuante-Sazonal`]],
    note: 'Projeto da disciplina de Biologia Evolutiva.' },
  { id: 'escape', kind: 'Pesquisa · em andamento', title: 'Escape estocástico em Julia',
    lead: 'Código da iniciação científica: potenciais biestáveis e equações de Langevin aplicados às reversões do campo magnético terrestre.',
    built: ['Integração de EDEs e ensembles', 'Tempos de residência e sua variabilidade', 'Diário de pesquisa reprodutível em construção'],
    stack: ['Julia', 'EDEs', 'Langevin', 'Monte Carlo'],
    stat: [],
    links: [['Sobre a pesquisa', '#pesquisa']],
    note: 'Repositório privado enquanto a pesquisa está em andamento.' },
  { id: 'laravel', kind: 'Estudos full stack · 2025', title: 'Aplicações web em Laravel',
    lead: 'Projetos de estudo de desenvolvimento web completo: loja virtual, gestão de eventos e gestão de usuários.',
    built: ['Estrutura MVC: rotas, controladores e views em Blade', 'Projetos de curso e um exame prático', 'Interfaces com CSS e JavaScript'],
    stack: ['PHP', 'Laravel', 'Blade', 'JavaScript'],
    stat: [['3', 'aplicações']],
    links: [],
    note: 'Repositórios privados de estudo, disponíveis sob pedido.' },
];

const skills = [
  ['Linguagens', ['Python', 'JavaScript', 'Julia', 'PHP', 'LaTeX']],
  ['Web', ['HTML e CSS', 'Canvas e SVG', 'Laravel', 'APIs simples em Python']],
  ['Computação científica', ['EDOs e EDEs', 'Monte Carlo', 'Métodos numéricos', 'Visualização interativa']],
  ['Prática', ['Git e GitHub', 'Testes automatizados', 'Documentação', 'Trabalho com IA, com revisão']],
];

const chips = xs => `<span class="chips">${xs.map(x => `<i>${x}</i>`).join('')}</span>`;
const ext = h => /^https?:/.test(h) ? ' target="_blank" rel="noopener"' : '';
const projectCard = (p, compact = false) => `<article class="proj" id="proj-${p.id}"><header><span class="proj-kind">${p.kind}</span><h3>${p.title}</h3></header><p class="proj-lead">${p.lead}</p>${compact ? '' : `<ul class="proj-built">${p.built.map(b => `<li>${b}</li>`).join('')}</ul>`}${p.stat.length ? `<div class="proj-stat">${p.stat.map(([v, l]) => `<span><b>${v}</b>${l}</span>`).join('')}</div>` : ''}${chips(p.stack)}<footer>${p.links.map(([t, h]) => `<a href="${h}"${ext(h)}>${t} <span>↗</span></a>`).join('')}${compact ? '' : `<small>${p.note}</small>`}</footer></article>`;
const featuredProjects = () => `<div class="proj-grid compact">${['biblioteca', 'aga', 'som'].map(id => projectCard(projects.find(p => p.id === id), true)).join('')}</div>`;

const profilePages = {
  trabalho: () => `${intro('Desenvolvimento / projetos', 'Software para pesquisa,<br>ensino e produto.', 'Construo ferramentas que ajudam alguém a entender ou fazer algo: bibliotecas de estudo, simulações interativas, modelos científicos e aplicações web. Cada projeto abaixo tem código ou página que você pode abrir.')}
  <section class="section scroll-reveal">${sectionLabel('01 / Projetos selecionados')}<div class="proj-grid">${projects.map(p => projectCard(p)).join('')}</div><p class="caption">Parte do código está em repositórios privados; o que é público tem link direto. <a class="text-link" href="${GITHUB}" target="_blank" rel="noopener">Perfil no GitHub ↗</a></p></section>
  <section class="section soft-section split scroll-reveal"><div>${sectionLabel('02 / Ferramentas')}<h2>O que uso<br>no dia a dia.</h2><p>Lista baseada nos projetos desta página, não em autoavaliação de nível.</p></div><div class="skill-grid">${skills.map(([h, xs]) => `<div><h3>${h}</h3>${chips(xs)}</div>`).join('')}</div></section>
  <section class="section split scroll-reveal"><div>${sectionLabel('03 / Como trabalho')}<h2>Do problema<br>à entrega verificável.</h2><p>Uso IA como ferramenta de programação e mantenho a revisão humana, os testes e os limites de cada entrega à vista.</p></div><div class="steps"><div class="step"><div><h3>Entender a necessidade</h3><p>Quem vai usar, para quê e o que conta como funcionando.</p></div></div><div class="step"><div><h3>Prototipar e testar</h3><p>Uma versão pequena que roda, com testes desde o início.</p></div></div><div class="step"><div><h3>Documentar os limites</h3><p>O que foi verificado, o que falta e como continuar.</p></div></div></div></section>
  ${contactCTA('Tem um problema<br>para resolver?', 'Conte a necessidade e o resultado esperado. Começamos por uma versão pequena que funcione.', 'Conversar sobre um projeto')}`,

  pesquisa: () => `${intro('Pesquisa / iniciação científica', 'Escape estocástico<br>e reversões geomagnéticas.', 'Na iniciação científica em processos estocásticos, estudo como sistemas com dois estados estáveis alternam entre eles sob ruído, com o campo magnético da Terra como caso de estudo.')}
  <section class="section split scroll-reveal"><div>${sectionLabel('01 / A pergunta')}<h2>Por que um sistema<br>salta de um estado<br>para outro?</h2></div><div><p>O campo magnético terrestre já inverteu sua polaridade muitas vezes, em intervalos irregulares. Um modelo mínimo trata a polaridade como uma partícula num poço duplo de potencial, empurrada por ruído. A pergunta é que mecanismos tornam esses saltos mais ou menos regulares.</p><p>As grandezas centrais são os tempos de residência em cada estado e a sua variabilidade, comparados aos registros geológicos.</p></div></section>
  <section class="section soft-section scroll-reveal">${sectionLabel('02 / O modelo, para mexer')}<div class="well"><div class="well-text"><h2>Uma partícula<br>num poço duplo.</h2><p>A equação é <span class="eq">dx = (x − x³) dt + √(2D) dW</span>. Com pouco ruído, a partícula fica presa num poço. Com mais ruído, salta entre os dois.</p><label for="well-noise">Intensidade do ruído D <output id="well-out">0,25</output></label><input id="well-noise" type="range" min="0.05" max="0.6" step="0.01" value="0.25"><p class="caption">Simulação ilustrativa por Euler–Maruyama, no navegador. Não reproduz resultados da pesquisa.</p></div><canvas id="well" aria-label="Trajetória simulada de uma partícula num poço duplo"></canvas></div></section>
  <section class="section split scroll-reveal"><div>${sectionLabel('03 / Métodos')}<h2>Ferramentas<br>da pesquisa.</h2></div><div>${chips(['Equações diferenciais estocásticas', 'Equação de Langevin', 'Euler–Maruyama', 'Fokker–Planck', 'Lei de Kramers', 'Ressonância estocástica', 'Ensembles de Monte Carlo', 'Julia'])}<div class="fact-row"><h3>Estado</h3><p>Em andamento. O próximo passo é um ambiente reprodutível que recupere resultados de artigos de referência antes de avançar nos modelos próprios.</p></div><div class="fact-row"><h3>Resultados</h3><p>Ainda não são apresentados aqui. Entram nesta página depois de revisados e publicados.</p></div><div class="fact-row"><h3>Antes</h3><p>Experiências em Biofísica no início da graduação.</p></div></div></section>
  <section class="section scroll-reveal">${sectionLabel('04 / Para onde estou olhando')}<div class="section-head"><h2>Dos processos<br>estocásticos à <em>astrofísica</em>.</h2><p>Séries temporais, inferência e simulação aparecem também na astronomia. Estou estudando essa ponte.</p></div>${disciplinePanes()}<p class="caption"><a class="text-link" href="#curso/processos-estocasticos">Trilha de processos estocásticos na biblioteca ↗</a></p></section>
  ${contactCTA('Interesse em<br>conversar sobre pesquisa?', 'Métodos estocásticos, simulação ou pontes com a astronomia: escreva com o contexto.', 'Conversar sobre pesquisa')}`,

  trajetoria: () => `${intro('Formação / USP', 'Ciências Moleculares<br>e Licenciatura em Física.', 'Uma formação interdisciplinar em Matemática, Física, Computação, Química e Biologia, que hoje se aproxima da astronomia e do ensino de Física.')}
  <section class="section scroll-reveal">${sectionLabel('01 / Cursos')}<div class="degree-grid"><article class="degree"><span class="proj-kind">USP · desde 2023</span><h3>Ciências Moleculares</h3><p>Ciclo básico concluído, com disciplinas de cinco áreas. A próxima etapa é o ciclo avançado, ainda em planejamento.</p></article><article class="degree rosa"><span class="proj-kind">IF-USP · em andamento</span><h3>Licenciatura em Física</h3><p>Disciplinas de educação e ensino de Física, cursadas em paralelo com o objetivo de concluir a licenciatura.</p></article><article class="degree past"><span class="proj-kind">IF-USP · 2021–2023</span><h3>Bacharelado em Física</h3><p>Primeiro curso na USP, encerrado pela transferência para Ciências Moleculares.</p></article></div></section>
  <section class="section soft-section scroll-reveal">${sectionLabel('02 / Base do ciclo básico')}<div class="section-head"><h2>Cinco áreas,<br>um percurso.</h2><p>Cada área tem trilhas de estudo na biblioteca, preparadas a partir das disciplinas.</p></div><div class="area-grid">${[['Matemática', 'calculo-1', 'Cálculo, álgebra linear, análise numérica'], ['Física', 'fisica-1', 'Mecânica a física moderna, física matemática'], ['Computação', 'computacao-1', 'Algoritmos, arquitetura, computação científica'], ['Química', 'quimica-1', 'Estrutura, termodinâmica, espectroscopia'], ['Biologia', 'biologia-1', 'Biomoléculas, células, sistemas']].map(([t, id, d]) => `<a class="area" href="#curso/${id}"><b>${t}</b><span>${d}</span><i>trilhas ↗</i></a>`).join('')}</div></section>
  <section class="section scroll-reveal">${sectionLabel('03 / Em curso · 2026/2')}<div class="section-head"><h2>O que estou<br><em>estudando</em> agora.</h2><p>Astronomia em azul, ensino em rosa.</p></div>${disciplinePanes()}</section>
  <section class="section split scroll-reveal"><div>${sectionLabel('04 / Percurso')}<h2>Aprender entre áreas.<br>Construir conexões.</h2><a class="text-link" href="arvore-formacao/">Explorar a árvore da formação <span>↗</span></a></div><div class="timeline"><article class="timeline-item"><span>2021</span><h3>Entrada na USP, em Física.</h3><p>Início da formação universitária e das experiências em Biofísica.</p></article><article class="timeline-item"><span>2022</span><h3>Ensino no IMEnsina.</h3><p>Aulas e plantões voluntários de preparação para vestibulares.</p></article><article class="timeline-item"><span>2023</span><h3>Ciências Moleculares.</h3><p>Transferência e aprofundamento interdisciplinar.</p></article><article class="timeline-item"><span>2023 — 2025</span><h3>Extensão na Matemateca.</h3><p>Modelagem, realidade virtual e aumentada e comunicação da Matemática; ensino de OpenSCAD em 2024.</p></article><article class="timeline-item"><span>2025 — atual</span><h3>Iniciação científica.</h3><p>Escape estocástico e reversões geomagnéticas.</p></article><article class="timeline-item"><span>2026/2</span><h3>Astronomia e licenciatura.</h3><p>Astrofísica galáctica, ensino de Física e Didática.</p></article></div></section>
  <section class="section soft-section split scroll-reveal"><div>${sectionLabel('05 / Formação complementar')}<h2>Cursos e<br>certificados.</h2></div><div><div class="fact-row"><h3>Python</h3><p>Programming for Everybody e Python Data Structures — University of Michigan / Coursera, 2023 e 2024.</p></div><div class="fact-row"><h3>Web</h3><p>Programming Foundations with JavaScript, HTML and CSS — Duke University / Coursera, 2024.</p></div><div class="fact-row"><h3>Interesses</h3><p>Matemática, computação e IA aplicadas à Física, com interesse especial em astrofísica.</p></div></div></section>
  <section class="section scroll-reveal"><blockquote class="quote">“Quero usar Matemática e Computação para entender problemas físicos e transformar o que aprendo em ferramentas e explicações úteis.”</blockquote></section>
  ${contactCTA('Vamos conectar<br>uma boa ideia?', 'Desenvolvimento, aulas ou uma conversa sobre pesquisa: escolha o ponto de partida.')}`,
};

/* Poço duplo: x' = x − x³ + √(2D) ξ, integrado por Euler–Maruyama. */
function setupWell() {
  const cv = document.querySelector('#well'), inp = document.querySelector('#well-noise'), out = document.querySelector('#well-out');
  if (!cv || !inp) return () => {};
  const g = cv.getContext('2d'), reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const N = 600, xs = new Float32Array(N).fill(-1); let x = -1, frame = 0, w = 1, h = 1;
  const gauss = () => { let u = 0, v = 0; while (!u) u = Math.random(); while (!v) v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(6.283185 * v); };
  const step = n => { const D = +inp.value, dt = 0.02; for (let k = 0; k < n; k++) { x += (x - x * x * x) * dt + Math.sqrt(2 * D * dt) * gauss(); xs.copyWithin(0, 1); xs[N - 1] = x; } };
  const resize = () => { const r = cv.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 2); w = r.width; h = r.height; cv.width = w * d; cv.height = h * d; g.setTransform(d, 0, 0, d, 0, 0); draw(); };
  const yOf = v => h / 2 - v * h * 0.3;
  function draw() {
    g.clearRect(0, 0, w, h);
    g.strokeStyle = 'rgba(143,182,255,.18)'; g.setLineDash([4, 6]); [1, -1].forEach(v => { g.beginPath(); g.moveTo(0, yOf(v)); g.lineTo(w, yOf(v)); g.stroke(); }); g.setLineDash([]);
    g.fillStyle = '#9aa6c6'; g.font = '12px "IBM Plex Mono", monospace'; g.fillText('estado +1', 10, yOf(1) - 8); g.fillText('estado −1', 10, yOf(-1) + 18);
    g.strokeStyle = '#7aa8ff'; g.lineWidth = 1.6; g.beginPath(); for (let i = 0; i < N; i++) { const px = i / (N - 1) * w, py = yOf(xs[i]); i ? g.lineTo(px, py) : g.moveTo(px, py); } g.stroke();
    g.fillStyle = '#5fd4ff'; g.beginPath(); g.arc(w - 4, yOf(xs[N - 1]), 5, 0, 6.283); g.fill();
  }
  const loop = () => { step(3); draw(); frame = requestAnimationFrame(loop); };
  const onInput = () => { out.textContent = (+inp.value).toFixed(2).replace('.', ','); if (reduced) { step(N); draw(); } };
  inp.addEventListener('input', onInput);
  const ro = new ResizeObserver(resize); ro.observe(cv);
  if (reduced) { step(N); resize(); } else { resize(); loop(); }
  return () => { cancelAnimationFrame(frame); ro.disconnect(); };
}
