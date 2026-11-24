# Um operador inclui suas condições de contorno

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: derivadas, integração, equações diferenciais lineares e álgebra linear básica. Trilha complementar, sem equivalência administrativa ou estudo concluído presumidos.


## O que é fixado nas pontas faz parte do problema

Considere −u″=g em [0,L], com L>0, g contínua e solução clássica u com duas derivadas contínuas. g é a fonte no interior. Em um modelo de difusão numa barra, fixar o valor de u nas pontas e impor fluxo nulo são escolhas físicas diferentes; fluxo é proporcional a −u′ quando o coeficiente é constante. O laboratório usa coordenada, fonte e solução adimensionais e coeficiente igual a 1. Não calcula temperaturas ou condutividades reais.



## A expressão não define tudo

Escrever A=−d²/dx² não determina sozinho o problema. Domínio, regularidade e condições de contorno fazem parte do operador. Em [0,L], Dirichlet homogêneo fixa u(0)=u(L)=0.

operador = ação + domínio

## Dirichlet admite uma fonte constante positiva

Para g=1 e L=1, integre −u″=1: u′=−x+C₁ e u=−x²/2+C₁x+C₀. As bordas u(0)=0 e u(1)=0 fornecem C₀=0 e C₁=1/2. Portanto u=x(1−x)/2. Substituir na equação e nas duas bordas confere a solução. É a mesma fonte do exemplo inicial incompatível de Neumann: o que mudou foram os dados de borda.

u(x)=x(1−x)/2

## A diferença entre duas soluções revela a unicidade

Se u e v resolvem a mesma equação e as mesmas bordas, w=u−v satisfaz −w″=0; portanto w=ax+b. Em Dirichlet homogêneo, w(0)=w(L)=0 impõe b=0 e a=0: a solução é única, quando existe. Em Neumann homogêneo, w′(0)=w′(L)=0 impõe a=0, mas deixa b livre. As soluções podem diferir por uma constante. Essa prova usa a equação da diferença e não depende de exemplos numéricos.



## Neumann pode manter um modo constante

Com u′(0)=u′(L)=0, a função constante está no núcleo de −d²/dx². Por isso um problema de Poisson exige compatibilidade do dado e pode não ter unicidade sem outra condição.

constante → autovalor zero em Neumann

## Integração mostra a compatibilidade

Em −u″=g com Neumann homogêneo, integrar dá ∫g dx=−[u′]_0^L=0. Um g constante positivo não satisfaz esse requisito. Alterar a borda altera existência, unicidade e espectro.

∫_0^L g dx=0 para Neumann homogêneo

## Construa uma solução compatível de Neumann

Agora g=2x−1 em [0,1]. Sua integral é [x²−x]₀¹=0. Integre a equação: u′=−x²+x+C₁. A borda u′(0)=0 dá C₁=0, e a outra fica u′(1)=−1+1=0. Integrando novamente, u=−x³/3+x²/2+C₀. Todo C₀ produz uma solução clássica com as duas bordas satisfeitas. A compatibilidade é também suficiente neste problema regular 1D; aqui sua suficiência foi exibida pela construção.

u_N(x)=−x³/3+x²/2+C₀

## Escolher a média remove a constante livre

A média em [0,L] é (1/L)∫u dx. No exemplo unitário, a média de −x³/3+x²/2+C₀ é −1/12+1/6+C₀=1/12+C₀. Exigir média zero seleciona C₀=−1/12. Assim u_N(0)=−1/12 e u_N(1)=1/12, embora as derivadas nas pontas sejam zero. Esta é uma normalização adicional, não outra condição local de borda; uma média escolhida não conserta uma fonte incompatível. Ao mencionar o núcleo de Neumann, usamos o domínio completo sem fixar a média; a normalização seleciona um representante da família de soluções de Poisson.

u_N(x)=x²/2−x³/3−1/12

## A mesma fonte também permite comparar os perfis

Para g=2x−1 com Dirichlet homogêneo, u_D=−x³/3+x²/2−x/6. Seus valores nas duas pontas são zero, mas u_D′(0)=u_D′(1)=−1/6. Já a solução normalizada de Neumann tem derivadas nulas e valores de ponta diferentes de zero. As funções resolvem a mesma expressão no interior; satisfazem problemas distintos. Derivada no eixo x e derivada normal à borda precisam de atenção aos sinais em condições não homogêneas.



## Integração por partes mostra onde a borda entra

Para funções reais u e v suficientemente regulares, adote ⟨u,v⟩=∫₀ᴸuv dx e A=−d²/dx². Integrando os dois termos por partes, obtemos ⟨u,Av⟩−⟨Au,v⟩=[u′v−uv′]₀ᴸ. Se ambas as funções obedecem Dirichlet homogêneo, seus valores de borda zeram o termo. Se ambas obedecem Neumann homogêneo, são as derivadas que o zeram. Não basta integrar a expressão e esquecer quais funções foram admitidas.

⟨u,Av⟩−⟨Au,v⟩=[u′v−uv′]₀ᴸ

## A forma de energia identifica o núcleo

Outra integração por partes dá ⟨u,Au⟩=∫₀ᴸ(u′)²dx−[uu′]₀ᴸ. Em cada uma das bordas homogêneas acima o último termo desaparece. A integral é não negativa e zera apenas se u for constante no intervalo. Dirichlet admite entre essas constantes apenas u=0; Neumann admite todas. Este argumento explica a diferença entre positividade estrita da forma no primeiro domínio e semipositividade no segundo.

⟨u,Au⟩=∫₀ᴸ(u′)²dx ≥ 0, nas bordas indicadas

## As funções próprias também mudam com a borda

No problema Aφ=λφ, uma função própria precisa ser não nula e satisfazer o domínio. Dirichlet homogêneo admite sen(nπx/L), n=1,2,…, com λ=(nπ/L)². Neumann homogêneo admite cos(nπx/L), n=0,1,…; n=0 fornece a constante e λ=0. Sen(0x) é a função zero, portanto não cria um modo de autovalor zero para Dirichlet. Essas famílias podem ser conferidas por derivação e bordas; a prova de completude não foi feita aqui.



## Simetria não é toda a prova de auto-adjunticidade

O cancelamento do termo de borda prova a identidade de simetria nas funções regulares escolhidas. Para afirmar auto-adjunticidade como operador em L², precisamos definir um domínio apropriado e provar que ele coincide com o domínio do adjunto. Essa etapa de análise funcional não foi executada nesta aula. Nas funções complexas, o produto interno também exige conjugação. Mantivemos as contas explícitas no caso real.



## O laboratório exato não discretiza a equação

O Python integra fontes polinomiais com coeficientes racionais. Dirichlet devolve coeficientes da solução homogênea; Neumann devolve uma solução de média zero quando a fonte é compatível, e None quando não é. Não subtrai silenciosamente a média da fonte para mudar o problema. Os testes usam curvatura por um stencil exato para polinômios de grau até cinco, além de bordas, integrais e identidades. Fontes gerais, condições mistas/Robin, solução fraca, malhas e erros de discretização permanecem pendentes.



## Exercícios e resoluções

1. Qual integral de g=1 em [0,1]?

   Resolução: A área é 1.

2. Mudar Dirichlet para Neumann mantém automaticamente o mesmo núcleo?

   Resolução: A constante passa a satisfazer a condição de Neumann.

3. Para −u″=1 em [0,1] com Dirichlet homogêneo, quanto vale u(1/2)?

   Resolução: u=x(1−x)/2; em x=1/2 resulta 1/8.

4. A constante u=2 satisfaz qual destas bordas homogêneas?

   Resolução: Seu valor não é zero nas pontas, mas sua derivada é zero.

5. Qual é a integral de g=2x−1 em [0,1]?

   Resolução: [x²−x]₀¹=0, satisfazendo a compatibilidade de Neumann.

6. Na solução de Neumann de média zero para g=2x−1, quanto vale u(0)?

   Resolução: A constante é −1/12; os termos em x se anulam em zero.

7. Somar uma constante à solução de Neumann muda −u″ ou as derivadas nas pontas?

   Resolução: As derivadas de uma constante são zero; apenas o valor médio muda.

8. Se uma solução tem média zero e somamos a constante 5, qual é sua nova média?

   Resolução: A média de u+5 é a média de u mais 5.

9. Impor média zero cria solução de Neumann homogêneo para g=1?

   Resolução: A integral da fonte continua 1; a compatibilidade falha independentemente da constante.

10. Qual é o autovalor do modo constante de Neumann?

   Resolução: A segunda derivada da constante é zero.

11. u(x)=x em [0,1] satisfaz qual borda homogênea?

   Resolução: u(1)=1 e u′(0)=u′(1)=1: falham ambos os domínios.

12. Zerar o termo de borda, sozinho, prova que o domínio do operador é igual ao do adjunto?

   Resolução: A simetria é uma etapa; auto-adjunticidade requer também conferir o domínio do adjunto.

## Fontes e limites da consulta

Steven G. Johnson, MIT OpenCourseWare 18.303 (Fall 2014), consulta parcial em 22/10/2026:
- [Aula 2](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/resources/mit18_303f14_lecture2/), PDF p.1: Dirichlet, núcleo e modos.
- [Aula 4](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/resources/mit18_303f14_lecture4/), PDF pp.1–2: produto interno, integração por partes e distinção de domínio na auto-adjunticidade.
- [Aula 10](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/resources/mit18_303f14_lecture10/), PDF pp.1–2: valores/derivadas normais, fluxo e núcleo de Neumann.

As notas da fonte usam +d²/dx² em parte de sua formulação; adotamos −d²/dx², portanto invertemos o sinal de autovalores e da forma quadrática. g aqui é a fonte no interior, não a função de borda de outras notações. Texto, exemplos polinomiais, figura, provas elementares, exercícios e código próprios, sem copiar notas, figuras ou soluções da fonte. Consulta parcial, sem afirmar curso integral, vídeo assistido ou crédito acadêmico.

O exemplo inicial incompatível de Neumann, os dois IDs e o código/desafio anteriores foram mantidos. Para g=2x−1, a solução normalizada foi construída explicitamente. A afirmação de simetria não foi usada como prova completa de auto-adjunticidade. O esquema mostra dados de borda, sem ser gráfico de uma solução.

## Reprodução

Na raiz do site, execute python3 -m labs.poisson-bordas.experiment e python3 -m unittest discover -s labs/poisson-bordas -t .

Coeficientes são dados em ordem crescente: [-1,2] significa −1+2x. O contrato exato usa int/Fraction, excluindo bool; L deve ser racional positivo. Neumann devolve None se a integral não é zero, preservando a fonte fornecida. Não há malha, solver de fontes gerais, erro de discretização ou validação experimental. O stencil de cinco pontos é apenas referência independente nos testes de polinômios de grau até cinco, não solucionador numérico oferecido ao aluno.

## Verificação de 22/10/2026

Cinco testes novos aprovados, incluindo 1875 pares fonte/intervalo; suíte global com 844 testes Python e 492 estruturas MathML. No navegador, respostas 1/8 e −1/12 aceitas, etapa aberta por teclado e esquema conferido em 390 px sem rolagem horizontal ou erros de console observados. Revisão conceitual e pessoal de Jhuann pendente.
