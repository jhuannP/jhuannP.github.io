# Cholesky: estrutura, reutilização e precisão dos dados

27/10/2026. Ampliação da aula existente:15 seções/12 exercícios, em rascunho com apoio de IA; revisão pessoal de Jhuann pendente. Três seções, dois exercícios, exemplo2×2, código e desafio anteriores preservados. Novos textos, exemplo3×3, figura, provas e testes próprios; não certificam domínio pessoal ou resultado de pesquisa.

## Hipóteses e recorrências

Matriz real simétrica positiva definida em aritmética exata admite A=LLᵀ, L triangular inferior de diagonal positiva. Reciprocamente, esse fator invertível dá zᵀAz=‖Lᵀz‖²>0 para z≠0. Igualar as entradas fornece

Lii=√(aii−Σk<i Lik²),

Lij=(aij−Σk<j LikLjk)/Ljj para i>j.

A escolha da raiz positiva fixa o fator. Pelo primeiro elemento e pela primeira coluna, seguidos da matriz restante, uma indução prova unicidade. Se sinais de colunas fossem livres, a mesma reconstrução poderia ter outros fatores.

Positividade da matriz restante: A=[[a,rᵀ],[r,B]], com a>0; S=B−rrᵀ/a. Para w≠0, z=(−rᵀw/a,w) satisfaz zᵀAz=wᵀSw>0. Logo S é positiva definida e o passo pode repetir no cálculo exato. Essa prova não assegura os mesmos sinais após conversão e arredondamento em float.

## Exemplos e solução

Exemplo anterior A=[[4,2],[2,3]], L=[[2,0],[1,√2]]. Último quadrado3−1=2, det A=8=(det L)². Índices matemáticos começam em1; Python em0.

Novo exemplo original:

L=[[2,0,0],[1,2,0],[−1,1,1]],

A=LLᵀ=[[4,2,−2],[2,5,1],[−2,1,3]].

Para b=(−2,−1,3), Ly=b dá y=(−1,0,2); depois Lᵀx=y dá x=(1,−1,2). Conferir Ax=b. Se b muda e A permanece, reutilizar L, refazendo as duas substituições. Não é necessário formar A⁻¹. Custo assintótico denso da fatoração O(n³), par de substituições O(n²); armazenar apenas o triângulo requer implementação apropriada. O código didático ainda aloca listas quadradas.

## Limites numéricos

Aε=[[1,1],[1,1+ε]], ε>0: det=ε e q=(x+y)²+εy², provando positividade exata. Em binário64 com arredondamento usual, ε=2⁻⁵⁴ desaparece ao formar1+ε. Os dados recebidos ficam [[1,1],[1,1]], com pivô zero. A falha então se refere aos dados armazenados; não refuta a matriz racional original. O teste de conversão foi observado no runtime local.

Diag(1,−1) é realmente indefinida; [[1,1],[1,1]] é singular semidefinida e não admite o fator de diagonal positiva requerido, embora exista fator com diagonal zero. Rejeição em aritmética finita também pede atenção a escala e precisão. A rotina não decide automaticamente a causa de toda falha. Alterar a diagonal muda o problema matemático.

Reconstrução δ=‖A−LLᵀ‖∞/‖A‖∞ usa a maior soma absoluta de linha. Resíduo de solução é b−Ax. Pequenos defeitos não garantem erro pequeno sem controlar condicionamento; tampouco validam a origem dos dados. Não se demonstra aqui estabilidade geral do algoritmo ou cotas completas de erro.

LDLᵀ: se A=MDMᵀ, M triangular inferior de diagonal1 e D positiva diagonal, então L=M√D. São fatores diferentes. Não há implementação nova de LDLᵀ, casos complexos, pivotamento indefinido ou matrizes esparsas. Em caso complexo, transposta deve ser substituída por adjunta.

## Código preservado e funções novas

`factor.py` mantém a função `cholesky` e auxiliares da aula, extraídos sem alteração. Converte entradas para float real finito; rejeita bool e aceita objetos convertíveis, inclusive Fraction e strings numéricas. Exige matriz quadrada não vazia e simetria exata após conversão. Pivô não positivo gera ArithmeticError. Não há tolerância que transforme números negativos em zero, nem aceitação silenciosa de simetria aproximada.

`solve_factor` resolve Ly=b e Lᵀx=y usando fsum, exige fator inferior com diagonal positiva e dimensões compatíveis; entradas são copiadas. `relative_factor_residual` mede reconstrução relativa na norma infinita, exigindo norma de A positiva. Cálculos intermediários não finitos ou escalas extremas podem falhar: não há promessa de robustez para todo float finito de entrada. A função de resíduo mede uma reconstrução, sem certificar que o fator veio de uma matriz positiva.

Da raiz do protótipo:

```sh
python3 -m unittest discover -s labs/cholesky-estrutura -t .
```

Cinco testes:216 fatores triangulares positivos geram matrizes SPD e648 sistemas comparados à eliminação racional independente; exemplos anterior/novo e caso1×1; escalas e imutabilidade/reuso; matrizes não positivas e perda de positividade na conversão; contratos. Matrizes foram construídas por L conhecido, permitindo conferir o fator, sem alegar que amostrar216 casos prova o teorema. O comparador racional não usa raízes quadradas.

## Fontes consultadas

Burden, Faires e Burden, Análise Numérica, tradução da10ª edição norte-americana,3ª brasileira, Cengage2016. §6.6 pp.462–465/PDF476–479 inspecionadas visualmente em27/10/2026: menores principais, conexão LDLᵀ/LLᵀ e algoritmo6.6. Consulta parcial; não lemos a seção integral. Páginas do PDF contadas desde1. Exemplar privado não distribuído, sem copiar imagens, matrizes de exemplos ou exercícios do livro. A recorrência é apresentada por dedução das entradas, com código anterior e casos próprios.

CCM0218: mapa existente registra ativação2011, aprovação2024/2 pelo panorama acadêmico e reabertura da fonte em27/10/2026; versão ministrada não comprovada. Bibliografia oficial indica7ª edição, distinta da10ª escolhida por Jhuann. Não transferir paginação ou exercícios entre edições. Onze grupos continuam parciais.

## Exercícios e revisão pessoal

Respostas dos12 itens:1; não;2;8;1;2;1; fator L reutilizável; pivô zero na semidefinida;1/16; dados armazenados mudaram; condicionamento importa. Dicas e resoluções completas na aula.

Duas sessões propostas de20min: recorrências e exemplo2×2; depois as substituições3×3 e a comparação racional/float. Dúvidas e avaliação pessoal permanecem em branco. Pendentes: estabilidade geral, métodos para indefinidas, entradas aproximadamente simétricas, matrizes grandes/esparsas e revisão conceitual de Jhuann.

Conferência da entrega: cinco testes locais e14 de catálogo aprovados;723 estruturas MathML conferidas. No navegador390px, exercício12 rejeitou a garantia universal por resíduo e aceitou condicionamento pelo Enter. Figura legível, sem transbordamento horizontal e sem erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
