# Comparação de séries e cotas da cauda

Material original em rascunho; revisão pessoal pendente. Para p=2, a monotonicidade de 1/x² fornece 1/(M+1) ≤ R_M ≤ 1/M. Como R_N=T_NM+R_M, acrescente as cotas ao bloco finito calculado. Sua largura é 1/[M(M+1)]. Um bloco sozinho não satisfaz necessariamente a cota inferior da cauda infinita.

Execute `python3 labs/comparacao-caudas/tails.py`. Frações exatas verificam largura, encaixe de intervalos e o contraexemplo de um único termo. Os testes finitos não provam o teorema geral.

Fontes da preparação anterior: Apostol I, 2ª ed., pp.395–398/PDF415–418 (comparação e teste da integral); OpenStax Calculus 2, §§5.3–5.4. Consulta parcial registrada na preparação; não reaberta neste bloco de probabilidade. Recursos que estavam referenciados mas ausentes foram reparados durante a validação global em 27/10/2026. Revisão de interface desta aula ainda pendente.


## 27/10/2026 — revisão de comparação e cotas do resto

Conferida a preparação de `c2-comparacao`: 12 seções/12 exercícios, com desigualdades de majorante/minorante, razão positiva finita, séries p e cotas da cauda. A revisão abriu o passo dos retângulos em cada intervalo e o exemplo resolvido, distinguiu explicitamente T_(N,M) de R_N, esclareceu dois enunciados e corrigiu espaçamento. Acrescentou a dedução alternativa 1/[n(n+1)]≤1/n²≤1/[n(n−1)], válida para n≥2, com telescopagem das séries dos lados. Prova própria, sem nova consulta externa. Fontes parcialmente consultadas na preparação anterior: Apostol I 2ª ed. pp.395–398/PDF415–418 e OpenStax Calculus 2 §§5.3–5.4; limitações de OCR/leitura parcial preservadas. Júpiter e livros não reabertos neste bloco.

Quatro testes em `labs/comparacao-caudas/tails.py` aprovados: largura/encaixe, bloco finito, contratos e identidades telescópicas independentes com comparação racional dos blocos. A grade finita confere implementação; a passagem ao infinito é justificada nas notas. 14 testes do catálogo e 862 estruturas MathML aprovados. Navegador390px rejeitou1/2 e aceitou1/4 para o bloco de N=1 até M=2; documento390/390px, console sem erros observados. Figura inspecionada em `comparacao-caudas-mobile.jpg`; viewport restaurada. Windows real, leitor de tela e revisão de Jhuann pendentes.

Atualizados o cabeçalho de Cálculo2 (antes desatualizado) e a etapa de comparação do percurso, que ainda dizia introdutória. Cálculo2 mantém21 aulas/217 exercícios, duas introduções curtas e seis grupos oficiais parciais. Global51 trilhas/573 aulas/5214 exercícios,145 introduções curtas; contagens não certificam cobertura ou domínio. Próxima ação20min: reconstruir as cotas e explicar por que um bloco de1/4 não representa a cauda R_1. Próxima elaboração global: conferir uma lacuna de química orgânica nas conexões bioquímicas, após localizar programa e referências, mantendo alternância e todo o escopo. Saldo semanal antes/depois68%; parada operacional65% preservada.
