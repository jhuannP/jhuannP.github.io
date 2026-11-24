# RK4: refinamento, estabilidade e energia

Rascunho original, 21/10/2026. Execute experiment.py em Python 3.
Teste: python3 -m unittest labs.rk4-oscilador.test_experiment.

Sistema adimensional q′=v, v′=−q, estado inicial (1,0), solução (cos t,−sen t).
N=2^nível, nível 1..7; T=4..12; duas integrações completas, N e 2N.
Os estágios usam derivadas, não incrementos hf. A aula conserva a função
step anterior e o exemplo escalar R(−1)=3/8; o módulo novo não os substitui.
A demonstração odeComparison compartilhada também foi preservada.

Erro exibido é norma do estado no instante final, não máximo sobre o tempo.
Δ/15 estima o erro fino só no regime assintótico de ordem quatro. Não é cota
ou controlador adaptativo. O cálculo independente das malhas custa 12N
chamadas de f; não se afirma custo mínimo com reutilização.

J²=−I; um passo é aI+bJ, a=1−h²/2+h⁴/24, b=h−h³/6.
O fator de energia a²+b²=1−h⁶/72+h⁸/576 dá faixa estável h²≤8 neste sistema.
Passos interiores amortecem artificialmente; na borda de módulo um ainda
há erro de fase. Não se extrapola esta faixa para EDOs gerais. RK4 não é
simplético nem conservador de energia em geral. Defeito de um passo O(h⁵)
e erro local normalizado por h O(h⁴) são convenções distintas.

Quatro testes: quatro estágios auditados e 18 avanços contra matriz racional;
21 traços completos contra potências complexas e fator de energia elevado
à quantidade de passos; nove refinamentos com ordem observada/estimativa;
estabilidade sem conservação, borda e erro de fase, contratos. Vinte e uma
malhas também cruzadas em Python/JavaScript. Não é validação de todo solver.

Fontes parciais, consulta em 21/10/2026:
- Burden/Faires/Burden, Análise Numérica, décima edição do acervo,
  5.4, p. impressa 316 (PDF 330), inspecionada visualmente: RK4, convenção
  de incrementos e regularidade. Livro não foi transcrito. Sumário em PDF 12
  e páginas 313, 292, 294 e 297 também inspecionadas na busca do trecho;
  nenhuma fórmula de seus exemplos foi reproduzida.
- [Cleve Moler, Numerical Computing with MATLAB, capítulo 7](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/odes.pdf),
  versão 17/09/2013, 7.2/7.4, pp. 2 e 6–8 do PDF, leitura parcial: sistema
  vetorial, quatro estágios, passo fixo e necessidade de estimar erro.
  Não se copia código ou figura do livro; os dados do experimento são próprios.

Visual: uma figura com vista de tempo ou fase, tabela de erros e estágios
expansíveis; azul N, cinza 2N, preto exato, escalas iguais no plano de fase.
N muda passo/custo, T muda horizonte, vista não muda o experimento. Retas
entre amostras não são uma extensão contínua de ordem quatro.
Pendente: outras EDOs, rigidez, adaptação, eventos, escalas/normas físicas,
validação em pesquisa e revisão pessoal.
