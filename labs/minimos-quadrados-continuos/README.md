# Mínimos quadrados contínuos

16/10/2026. Rascunho para revisão de Jhuann.

## Escolha o que significa melhor aproximação

Fixe f(x)=x² em [0,1], com x e f adimensionais. Procuramos p(x)=a+bx que minimize J(a,b)=∫₀¹[f(x)−p(x)]²dx, usando peso 1. Este é um critério contínuo de erro quadrático; uma soma sobre pontos escolhidos define outro problema.

## A integral funciona como produto interno

Defina ⟨g,h⟩=∫₀¹g(x)h(x)dx. Para funções contínuas reais, ⟨g,g⟩≥0, com igualdade somente para a função nula. A norma L² é √⟨g,g⟩. Queremos projetar f no espaço das retas gerado por 1 e x; essa base é linearmente independente, mas não ortogonal.

## As equações normais vêm das variações dos coeficientes

Escreva r=f−a−bx. Derivar J em relação a dá −2∫r dx; em relação a b dá −2∫xr dx. No candidato mínimo, ambos são zero. Logo o resíduo deve ser ortogonal às duas funções da base, e não necessariamente zero em cada ponto.

## Cada entrada do sistema é uma integral

As equações são a+b/2=1/3 e a/2+b/3=1/4. A matriz de Gram tem entradas ⟨1,1⟩=1, ⟨1,x⟩=1/2 e ⟨x,x⟩=1/3. O lado direito contém ⟨1,x²⟩=1/3 e ⟨x,x²⟩=1/4. Usar pontos nas extremidades no lugar dessas integrais mudaria o critério.

## Resolver o sistema dá uma reta que não interpola as extremidades

Subtraia metade da primeira equação da segunda: b/12=1/12, portanto b=1. Da primeira, a=−1/6. A aproximação é p*(x)=x−1/6. Em x=0 ela vale −1/6, enquanto f(0)=0; o critério quadrático integrado permite esse desvio.

## Confira o resíduo sem confiar apenas na resolução do sistema

O resíduo é r*(x)=x²−x+1/6. Sua integral vale 1/3−1/2+1/6=0. A integral de xr* vale 1/4−1/3+1/12=0. Expandindo e integrando (r*)², obtemos J*=1/180. O erro L² é 1/√180, não 1/180.

## Ortogonalidade demonstra que o candidato é o mínimo único

Para qualquer outra reta, escreva p=p*+q, com q=δa+δb x. Ao expandir ||r*−q||², o termo cruzado é zero porque r* é ortogonal a 1 e x. Assim J(p)=1/180+∫₀¹q²dx=1/180+δa²+δaδb+δb²/3. A parcela extra só zera quando q é a reta nula, provando mínimo e unicidade.

## Interpolar dois pontos pode produzir outro resultado

Usando apenas (0,0) e (1,1), a reta interpoladora é p=x e o erro nos dois pontos é zero. Mas seu erro contínuo é ∫₀¹(x²−x)²dx=1/30, seis vezes J*. A reta ótima contínua não minimiza aquela soma finita: os dois objetivos usam medidas diferentes.

## Amostragem pode aproximar a integral sob condições declaradas

No laboratório, use n+1 pontos uniformes i/n, com pesos iguais. A média de x é 1/2 e a de x² é (2n+1)/(6n); a simetria dá b=1. Assim, para este alvo e desenho, a=−(n−1)/(6n); seu erro contínuo excede J* em 1/(36n²). Ele converge ao ajuste contínuo quando n cresce. Distribuições de pontos ou pesos diferentes podem levar a outro limite; isso não justifica substituir qualquer integral por qualquer amostra.

## O critério não é a norma uniforme

A norma uniforme mede sup|f−p|, enquanto a norma L² usa a raiz da integral do quadrado. Uma função pode ter desvio concentrado numa região pequena; controlar um critério não é automaticamente minimizar o outro. A teoria da melhor aproximação uniforme e suas garantias continua sendo um tópico separado.

## A matriz de Gram pede cuidado em problemas maiores

Neste exemplo de dimensão dois, usamos aritmética racional e integrais exatas. Bases maiores ou quase dependentes podem tornar a representação mal condicionada. Não extrapole a inversão explícita de uma matriz pequena para uma recomendação de algoritmo geral; bases ortogonais, fatorações e erro de quadratura precisam de estudo específico.

## Uma comparação computacional deve preservar o problema

O Python integra produtos de polinômios exatamente com Fraction e resolve a projeção na base fixa {1,x}. A demonstração varia a reta e mostra J e os dois momentos do resíduo. O gráfico é sintético, sem dados de pesquisa ou ajuste experimental. Não é um resolvedor geral para funções arbitrárias, pesos ou intervalos diferentes.

## Resoluções

Qual o intercepto a da melhor reta contínua para x² em [0,1]? Aceita fração.

a=−1/6 e b=1 resolvem as equações normais.

Qual o coeficiente b da reta ótima contínua?

Subtrair metade da primeira equação da segunda dá b/12=1/12.

Qual ∫₀¹r*(x) dx no ajuste ótimo?

r*=x²−x+1/6: 1/3−1/2+1/6=0.

Qual J* mínimo? Aceita fração.

A integral do quadrado do resíduo ótimo vale 1/180.

Qual a razão entre o erro contínuo de p=x e o erro ótimo?

(1/30)/(1/180)=6.

No ótimo, o resíduo deve zerar em todos os pontos?

Ele é ortogonal à base; não é necessariamente a função nula.

A norma L² do resíduo ótimo é qual?

J é o quadrado da norma L².

Uma soma sobre pontos arbitrários sempre tem o mesmo minimizador que a integral com peso 1?

O desenho e os pesos alteram a medida e o problema.

A base {1,x} é ortogonal neste produto interno?

⟨1,x⟩=1/2, que não é zero.

## Fontes, roteiro e pendências

Escopo: CCM0218, programa indexado conferido em 16/10. Apoio sobre produtos internos de funções e norma L²: [W. C. Carter, MIT 3.016, aula 27](https://ocw.mit.edu/courses/3-016-mathematics-for-materials-scientists-and-engineers-fall-2005/4c57c6d107a9c5fd6fc670a096643a7d_lecture_27.pdf), consultado diretamente em 16/10/2026. A projeção de x², derivação, amostragem e exercícios deste material são próprios; não reproduzem o exemplo da fonte.

Pré-requisitos: integração de polinômios, álgebra linear, produto interno e derivadas parciais. Roteiro: definir critério; calcular Gram/momentos; resolver; conferir ortogonalidade; provar mínimo; comparar dois pontos e n+1 pontos. Produto: solução comentada que diferencia norma, erro ao quadrado e soma amostral. Sem uso de dados privados ou resultado de pesquisa.

Pendentes: bases/intervalos/pesos gerais, aproximação uniforme, bases ortogonais e estabilidade, quadratura para funções não polinomiais e interpretações estatísticas com hipóteses próprias.
