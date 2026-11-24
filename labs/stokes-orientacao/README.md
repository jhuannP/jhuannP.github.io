# Stokes: conferir campo, superfície e borda

27/10/2026. Notas de aula originais, assistidas por IA, para revisão de Jhuann. Python opcional; não demonstra domínio pessoal ou conclusão de Cálculo 3.

Na aula `c3-stokes`, o campo original F=(−y/2,x/2,0) foi preservado. Disco unitário e calota z=1−x²−y², com normal para cima, dão circulação e fluxo do rotacional π. A calota usa vetor de área (2u,2v,1), não a área escalar curva. O campo G=(z,0,0) tem rotacional não nulo e circulação zero na borda dessa calota. Uma integral zero não implica integrando nulo.

Para H=(−y/(x²+y²),x/(x²+y²),0), o eixo z é excluído do domínio. Rotacional zero fora do eixo coexiste com circulação 2π ao redor dele: o disco não satisfaz a regularidade necessária. Na coroa, a borda interna é horária para normal +z: contribuições 2π e −2π. Para o F original, a soma é π(R²−a²), não zero.

## Fontes consultadas parcialmente

Apostol, Cálculo volume II, exemplar português do acervo: §12.11, pp.491–492/PDF504–505 e §12.12, p.493/PDF506 (PDF contado a partir de1). Reconferência textual parcial em 27/10/2026; OCR imperfeito, sem leitura integral ou nova inspeção visual. Enunciado, redução ao plano de parâmetros e definição de rotacional. O texto da aula deriva a identidade local pela regra da cadeia e cancelamento das derivadas mistas, sem alegar prova global por múltiplos recortes.

[OpenStax, Calculus Volume 3, §6.7](https://openstax.org/books/calculus-volume-3/pages/6-7-stokes-theorem), enunciado, orientação e prova para gráfico, consulta parcial em 27/10/2026. Exemplos, figura, código e exercícios próprios; sem copiar exercícios ou distribuir o livro privado. Júpiter não reaberto neste bloco; permanece a limitação de versão curricular já registrada em MATEMATICA_4.md.

## Laboratório e seus limites

Execute `python3 labs/stokes-orientacao/stokes.py`. Quatro testes: regra racional de Boole em graus0..5; 90 comparações de linha e fluxo (30 campos monomiais vetoriais de grau total≤2 em três gráficos quadráticos sobre o quadrado unitário); exemplos conhecidos no gráfico z=u²+v²; círculos e coroas por quadratura numérica.

Linha: os quatro lados do domínio são percorridos anti-horariamente; a componente z da tangente vem da derivada do gráfico. Fluxo: derivadas analíticas do monômio definem o rotacional; vetor de área (−z_u,−z_v,1). As duas rotinas não usam uma para obter a outra. Composição quadrática do campo tem grau univariado≤4 e tangente≤1, portanto integrandos de linha têm grau≤5. O fluxo tem grau univariado≤3. A regra é exata nesses recortes, com frações racionais. Por linearidade a comparação se estende a combinações da base testada, sem provar Stokes para campos gerais. Círculos usam ponto médio e tolerância, nunca avaliação no eixo singular.

O quadrado curvo do laboratório difere da calota circular da aula: G tem fluxo −1 no quadrado z=u²+v², enquanto dá zero na calota simétrica z=1−u²−v². O domínio e o vetor de área explicam a diferença. Normal invertida requer linha invertida. Unidades e hipóteses devem ser reconstruídas na revisão pessoal.

Próxima ação de20min: obter π pelas duas integrais, explicar por que a área curva não entra sozinha e reconstruir as duas orientações da coroa. Demonstração global, superfícies não orientáveis e uso com aluno permanecem pendentes.
