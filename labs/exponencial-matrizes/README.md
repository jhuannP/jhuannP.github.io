# Exponencial de matrizes e sistemas — notas originais

16/10/2026. Rascunho para revisão de Jhuann.

## O estado reúne várias incógnitas

Um sistema linear autônomo de coeficientes constantes tem forma z′=Az, z(0)=z₀, com A uma matriz quadrada fixa e z um vetor. Mesmo quando cada linha é simples, o acoplamento impede resolver componentes como se fossem independentes. Usaremos variáveis e tempo normalizados; não estamos ajustando um sistema físico real.

## A exponencial matricial não aplica exp a cada entrada

Define-se exp(tA)=I+tA+t²A²/2!+⋯. O termo inicial é a identidade, não uma matriz preenchida com uns. Potências e produtos são matriciais. Aplicar a exponencial escalar separadamente às entradas produz outra operação e não fornece, em geral, a evolução do sistema.

## A série converge para toda matriz finita e todo tempo finito

Na norma matricial induzida pela norma euclidiana, cada termo satisfaz ||tᵏ Aᵏ/k!||≤|t|^k||A||^k/k!. A série escalar majorante é exp(|t| ||A||), portanto a série converge absolutamente, uniformemente em intervalos compactos de t. As séries de derivadas também admitem majorantes compactas. Isso fundamenta a derivação termo a termo; a demonstração completa dos teoremas de séries de funções fica como aprofundamento.

## A solução conserva a condição inicial

Derivando a série, d(exp(tA))/dt=Aexp(tA)=exp(tA)A. Em t=0, e⁰=I, logo z=exp(tA)z₀ satisfaz a equação e z(0)=z₀. O teorema de existência e unicidade de sistemas lineares garante que essa é a solução do problema inicial; o teorema geral não é demonstrado integralmente aqui.

## Diagonalizar é útil, mas não é obrigatório

Se A=PDP⁻¹, então Aᵏ=PD^kP⁻¹ e exp(tA)=P e^{tD}P⁻¹. A exponencial da diagonal D tem entradas diagonais exp(tλ_i). Essa ferramenta exige uma base de autovetores. A exponencial, definida pela série, continua existindo mesmo quando essa base não existe.

## Um autovalor repetido pode não dar duas direções próprias

Considere A=[[a,b],[0,a]]. Seu único autovalor é a, com multiplicidade algébrica dois. Se b≠0, (A−aI)v=0 obriga a segunda coordenada a zero; o autoespaço é unidimensional e a matriz não é diagonalizável. Se b=0, A=aI e qualquer base funciona. Autovalor repetido sozinho não decide a questão.

## A parte nilpotente faz a série terminar

Escreva A=aI+N, com N=[[0,b],[0,0]] e N²=0. Como aI e N comutam, exp(tA)=exp(at)exp(tN)=exp(at)(I+tN). Assim exp(tA)=exp(at)[[1,bt],[0,1]]. O termo t acompanha o acoplamento que uma tentativa de diagonalizar sem base própria perderia. Para blocos nilpotentes maiores surgem outros termos polinomiais.

## Resolver por componentes fornece outra conferência

O sistema é y′=ay e x′=ax+by. Primeiro y=y₀exp(at). Multiplicando a equação de x por exp(−at), temos (exp(−at)x)′=by₀. Integrando: x=exp(at)(x₀+bty₀). Esta derivação confirma a exponencial sem usar diagonalização e também mostra o papel de cada condição inicial.

## Autovalores zero não bastam para concluir estabilidade

Para a<0, o fator exponencial domina o fator t e todas as soluções dessa família tendem a zero, apesar de possível crescimento transitório. Para a=0 e b≠0, y é constante e x pode crescer linearmente se y₀≠0; a origem não é estável. Para a=b=0, todos os estados são constantes: a origem é estável, mas não atrai os demais. Com a>0 existem soluções crescentes; o estado inicial nulo ainda permanece nulo.

## A regra de soma exige comutação

Para a mesma matriz, exp(sA)exp(tA)=exp((s+t)A) e a inversa é exp(−tA). Para matrizes diferentes, exp(A+B)=exp(A) exp(B) exige cuidado: comutação é uma condição suficiente. No produto de séries, o termo misto de segunda ordem no produto é AB; na exponencial da soma ele é (AB+BA)/2. Matrizes não comutantes em geral dão resultados diferentes. A solução por exponencial simples também não se transfere automaticamente para A(t).

## O laboratório verifica a família, não implementa expm geral

O Python e a demonstração usam a fórmula fechada da família triangular. Os testes a comparam com potências matriciais e série racional truncada, lei de composição, inversa e derivadas por diferenças centrais. A série truncada de teste é referência neste domínio pequeno, não um algoritmo de produção para qualquer matriz. Estimativas numéricas de expm geral, sistemas forçados, Jordan geral e modelos científicos concretos permanecem pendentes.

## Resoluções

No exemplo resolvido, qual x(2)?

x(2)=1+6×2=13.

No exemplo resolvido, qual y(2)?

y permanece igual a 3.

Para A=[[a,2],[0,a]], qual a dimensão do autoespaço?

b≠0 obriga a segunda coordenada a zero.

Se A²=0 e t=2, qual o coeficiente de A em exp(tA)=I+cA?

A série termina em I+tA, então c=2.

Para a=0, b=3 e estado inicial (0,1), qual x(4)?

x=bty₀=3×4×1=12.

A exponencial matricial aplica exp a cada entrada?

É definida por uma série de potências matriciais.

A exponencial deixa de existir quando A não é diagonalizável?

A série converge para toda matriz finita.

Pode-se aplicar exp(A+B)=exp(A)exp(B) a matrizes quaisquer sem verificar hipóteses?

Comutação é uma condição suficiente; sem ela a igualdade pode falhar.

Com a<0, um fator t multiplicando exp(at) impede o limite zero?

A exponencial decrescente domina o crescimento polinomial.

## Roteiro de ensino e evidência

Pré-requisitos: multiplicação de matrizes, autovetores, séries e EDO de primeira ordem. Começar por um sistema nilpotente, resolvê-lo por componentes e só então formular a série matricial. Pedir ao aluno que explique por que não pode diagonalizar o bloco com b≠0 e que confira condição inicial e equação. Produto: resolução própria de outra condição inicial e comparação comentada com uma aproximação numérica. Não há dado experimental nem domínio pessoal demonstrado por esta geração.

## Fontes e limites

Escopo curricular: [CCM0213 no Júpiter](https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0213), consultado em 16/10/2026. A bibliografia oficial e as limitações de localização estão no mapa da disciplina. Fórmulas e argumentos desenvolvidos aqui são originais, sem transcrição. Pendentes: teoremas completos de convergência/derivação, existência/unicidade, forçamento, Jordan geral e cálculo numérico de expm com controle de erro. A série racional de referência usa quarenta termos apenas no domínio pequeno testado.

## 28/10/2026 — estabilidade e amplificação transitória

Extensão original para A=[[-1,b],[0,-1]],norma euclidiana e tempo normalizado não negativo. A solução anterior,Python,simulação e nove exercícios preservados. Autovalores−1 dão limite zero,mas não monotonicidade. b4,z0(0,1),t1 produz(4/e,1/e),norma√17/e≈1,516806. Essa norma não é energia física presumida.

A derivada d||z||²/dt=−2(x²+y²)+2bxy é não positiva para todo estado se |b|≤2. Acima disso há estados com derivada positiva. Em b4,z0(1,1)/√2,derivada inicial2 da norma ao quadrado. A base/coordenadas e a norma precisam ser declaradas.

Exp(tA)=exp(−t)T,k=bt,T=[[1,k],[0,1]]. TᵀT tem traço2+k² e determinante1; seu maior autovalor leva a σmax=(√(k²+4)+|k|)/2. G(t)=exp(−t)σmax. Vetor proporcional a(1,sign(k)σmax) atinge o ganho para k≠0;normalizar. Para k0,qualquer unitário. Esse cálculo fundamenta o supremo,sem depender só de amostras angulares. A direção ótima pode mudar com t;G não é automaticamente uma trajetória única. A trajetória fixa(0,1) tem normaexp(−t)√(1+b²t²).

d logG/dt=−1+|b|/√(b²t²+4). |b|≤2: máximo1 emt0. |b|>2: t*=√(b²−4)/|b|. b4:t*≈0,866025404,Gmax≈1,569775308. Em t1,G≈1,558362320,distinto de1,516805793 da trajetória. A fórmula se estende analiticamente a todo t≥0;b4tem pico dentro da faixa do código. Algoritmo geral de expm,SVD,pseudoespectro,forçamento,não linearidade e norma física não implementados.

`transient.py` usa float,|b|≤4,t0–20,componentes iniciais−4 a4. Quatro testes novos:42combinações b/t com96direções cada e vetor que atinge ganho;9b×401tempos versus pico analítico;trajetória e compatibilidade com rotina antiga;contratos. Oito testes totais do laboratório passam. Amostragem não é prova do máximo global;derivações fornecem esse resultado para a família. `transiente.svg` gerado das duas fórmulas,sem dados medidos.

Fonte pública complementar: Nick Trefethen,Chebfun,Transient growth,2011,https://www.chebfun.org/examples/linalg/TransientGrowth.html ,introdução/definição de norma e distinção de seu quadrado consultadas parcialmente em28/10/2026. Não executamos Chebfun nem reproduzimos a matriz7×7,código ou figuras. A referência não substitui bibliografia oficial de CCM0213;exemplo2×2,cálculo e gráfico próprios. Fontes anteriores preservadas,sem nova leitura de livros ou programa oficial. Revisão pessoal pendente.
