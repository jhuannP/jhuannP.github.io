# Newton para sistemas não lineares

16/10/2026. Rascunho para revisão de Jhuann.

## Um sistema procura um vetor que zera todas as componentes

Queremos resolver F(z)=0, com z=(x,y). Neste exemplo adimensional, F₁=x²+y²−1 e F₂=x−y. A primeira equação descreve o círculo unitário; a segunda, a reta x=y. As soluções são (1/√2,1/√2) e (−1/√2,−1/√2).

## O Jacobiano é o mapa linear da aproximação local

As derivadas parciais formam J_F=[[2x,2y],[1,−1]]. Para uma pequena correção Δ, F(z+Δ)=F(z)+J_F(z)Δ+termos de ordem superior. O passo de Newton impõe que essa aproximação linear seja zero; não afirma que a função original zera após o passo.

## Cada iteração resolve um sistema linear

Calcule F e J no ponto atual, resolva J_F(z_k)Δ_k=−F(z_k) e atualize z_(k+1)=z_k+Δ_k. O laboratório usa eliminação 2×2 com pivotamento parcial. A escrita com inversa ajuda a teoria, mas formar explicitamente a inversa não é necessário para obter a correção.

## A geometria do exemplo permite uma verificação independente

det J_F=−2(x+y). Se x+y≠0, resolver as duas linhas mostra que o próximo ponto satisfaz x_novo=y_novo=(x²+y²+1)/[2(x+y)]. Essa fórmula serve como referência independente para testar o passo linear. Ela é particular deste sistema, não uma fórmula geral de Newton.

## Um primeiro passo pode não reduzir o resíduo

Começando em (1,0), temos F=(0,1) e J=[[2,0],[1,−1]]. O sistema dá Δ=(0,1), logo o próximo ponto é (1,1). A norma infinito do resíduo é 1 antes e depois desse passo. Não se deve prometer diminuição estrita do resíduo em toda iteração de Newton completo.

## Depois da primeira correção, a conta se reduz neste exemplo

Quando x=y=t≠0, a recorrência vira t_novo=(t+1/(2t))/2. Por exemplo, de (1,1) segue-se (3/4,3/4). O sistema continua tendo duas raízes. Para iniciar com soma negativa, o primeiro ponto na reta também tem sinal negativo; o gráfico permite comparar as duas sequências.

## Um Jacobiano singular impede esta correção

Na linha x+y=0, o determinante é zero. Na origem, o resíduo F=(−1,0) não é nulo e a primeira linha do Jacobiano também é nula: a equação linear pede 0=1. A existência de soluções do problema original não torna esse passo linear resolúvel.

## Pivô pequeno é um diagnóstico numérico, não uma prova simbólica

O código interrompe se o pivô da eliminação não supera 10⁻¹² vezes a maior entre 1 e as magnitudes das entradas de J. Esse limiar depende da escala. Um Jacobiano não singular, mas perto da linha problemática, também pode ser recusado. A rotina não estima número de condição nem trata escala física geral.

## Critérios de parada precisam de nomes e significados

Resíduo: ||F||∞≤10⁻¹⁰ nesta demonstração. Passo pequeno: ||Δ||∞≤10⁻¹⁴(1+||z_novo||∞), sem declarar sucesso caso o resíduo ainda seja grande. Há limite de iterações e guarda de coordenadas finitas até 10⁶. Parar por limite, pivô ou guarda não demonstra raiz, inexistência ou divergência matemática.

## A tolerância não é uma prova de erro na posição

Um resíduo pequeno informa quanto as equações são satisfeitas na escala escolhida. Converter isso em erro na posição exige hipóteses sobre o problema e o Jacobiano. As raízes conhecidas permitem conferir este exemplo; em problemas reais, não se deve substituir análise por um status de parada.

## A convergência local exige hipóteses

A convergência quadrática local de Newton requer regularidade suficiente do Jacobiano, invertibilidade na raiz e início suficientemente próximo, além de uma resolução adequada do passo. Este laboratório não implementa amortecimento ou busca linear. A experiência com círculo/reta não prova comportamento global de sistemas gerais.

## O experimento registra a sequência, não apenas a última coordenada

O Python guarda ponto, norma do resíduo e motivo da parada. A figura mostra círculo, reta e pontos iterados; o segmento que liga iterações não é uma trajetória física nem uma curva solução. Se uma iteração se afasta, os eixos se expandem para mantê-la visível, preservando a mesma escala em x e y. Dados, equações e cálculos são sintéticos.

## Resoluções

Quantas raízes reais tem o sistema do exemplo?

Há uma raiz positiva e uma negativa.

É obrigatório calcular a inversa do Jacobiano para cada passo?

Resolva o sistema linear da correção diretamente.

Qual det J_F em (1,0)?

−2(x+y)=−2.

Do ponto (1,0), qual a componente Δx do primeiro passo?

A primeira linha é 2Δx=0.

Do ponto (1,0), qual o novo valor de y?

Δy=1, então y_novo=1.

De (1,1), qual o próximo x? Aceita fração.

(1²+1²+1)/(2(1+1))=3/4.

Qual ||F(0,0)||∞?

F(0,0)=(−1,0); máximo dos módulos é 1.

A parada por pivô pequeno prova que o sistema original não tem solução?

O sistema tem duas soluções; o diagnóstico refere-se à correção local e ao limiar.

Newton completo deve reduzir estritamente o resíduo em todo passo?

De (1,0) para (1,1), o resíduo infinito permanece 1.

Um passo pequeno com resíduo grande deve ser declarado raiz encontrada?

Pode indicar estagnação; o critério de resíduo ainda não foi satisfeito.

## Fontes, roteiro e pendências

Escopo: CCM0218, programa indexado conferido em 16/10. Apoio para separar critérios de resíduo, passo e limite: [SUNDIALS, documentação oficial de KINSOL 7.8](https://sundials.readthedocs.io/en/v7.8.0/kinsol/Usage/index.html), consultada em 16/10/2026. O laboratório é uma implementação didática própria, não utiliza KINSOL nem replica seus critérios completos. O exemplo círculo/reta e suas contas são próprios.

Pré-requisitos: derivadas parciais, Jacobiano, norma infinito e sistemas lineares. Roteiro: resolver as equações geometricamente; derivar J; calcular primeira correção; comparar fórmula fechada e eliminação; iniciar na origem e perto da linha singular; registrar motivo de parada e resíduo. Produto: tabela de iterações e explicação dos limites de cada diagnóstico.

Pendentes: escalas e unidades gerais, busca linear/amortecimento, prova do teorema local, sistemas maiores/esparsos, Jacobiano aproximado e análise de condicionamento. Tolerâncias e limite de coordenadas são opções didáticas; sem certificação matemática por um status de software.
