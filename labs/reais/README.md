# Números reais: ordem, distância e completude

Material original em rascunho — 16/10/2026. Referência de escopo: CCM0113, programa conferido em 16/10, ativação 15/07/2024. Versão da turma de 2023 não recuperada. https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0113

## As regras algébricas precisam de um sistema

Nos reais, soma e produto são associativos e comutativos; o produto distribui sobre a soma. Existem elementos neutros 0 e 1, com 0≠1; todo número tem oposto e todo número não nulo tem inverso multiplicativo. Essas propriedades de corpo permitem cancelar fatores somente quando são não nulos. Não se divide por zero.

## A ordem é compatível com as operações

Se a<b, somar c aos dois lados preserva a desigualdade. Multiplicar por c>0 também preserva; multiplicar por c<0 inverte. Por exemplo, −2x<6 equivale a x>−3. Multiplicar uma desigualdade por uma expressão de sinal desconhecido exige separar casos.

## Módulo mede distância na reta

|x| é x quando x≥0 e −x quando x<0. A distância entre x e a é |x−a|. Para ε>0, |x−a|<ε equivale a a−ε<x<a+ε. Isso permite traduzir a linguagem de limites em intervalos, sem tratar o módulo como um símbolo que pode ser retirado sem análise.

## A desigualdade triangular controla somas

Como −|x|≤x≤|x| e −|y|≤y≤|y|, somar fornece −(|x|+|y|)≤x+y≤|x|+|y|. Logo |x+y|≤|x|+|y|. Aplicando a desigualdade a x=(x−y)+y e trocando os papéis, obtemos ||x|−|y||≤|x−y|. Não há igualdade em geral: com x=3,y=−3, o lado esquerdo da primeira é zero e a soma dos módulos é 6.

## Ser cota superior não exige pertencer ao conjunto

M é cota superior de S se todo s∈S satisfaz s≤M. Um conjunto é limitado superiormente quando existe ao menos uma cota superior. Se uma cota superior pertence a S, ela é seu máximo. Para S=(0;1), 1 e 2 são cotas superiores, mas não há máximo: para qualquer s∈S, (s+1)/2 ainda pertence a S e é maior.

## O supremo é a menor cota superior

α=sup S significa duas condições: α é cota superior e nenhuma cota menor funciona. A segunda pode ser escrita: para todo ε>0 existe s∈S com α−ε<s≤α. O supremo pode pertencer ao conjunto ou não. Para (0;1) e [0;1], o supremo é 1 em ambos, mas só o segundo tem máximo 1.

## Completude diferencia os reais dos racionais

O axioma da completude afirma: todo subconjunto não vazio de ℝ limitado superiormente tem supremo em ℝ. As condições não vazio e limitado são essenciais. ℕ é não limitado superiormente nos reais, e ∅ não tem supremo real na convenção desta aula. Os racionais são um corpo ordenado, mas não satisfazem esse axioma.

## A raiz de dois mostra uma lacuna dos racionais

A existência da raiz positiva de 2 nos reais pode ser estabelecida pela completude ou pelo Valor Intermediário para x²−2. Ela não é racional: se √2=p/q em forma irredutível, com q>0, então p²=2q². Assim p é par, p=2k; substituir dá q²=2k², então q também é par, contradizendo a fração irredutível. Logo aproximações racionais não se tornam iguais à raiz por terem muitas casas.

## Um conjunto infinito não é a sua lista truncada

Para S={1−1/n:n≥1}, cada termo é menor que 1 e os termos crescem. Não há máximo porque o termo seguinte é maior. O número 1 é supremo: dado ε>0, escolha inteiro n>1/ε, então 1−1/n>1−ε. Essa escolha usa a propriedade arquimediana dos reais, consequência da completude. Uma lista dos primeiros N termos, por outro lado, tem máximo 1−1/N.

## A propriedade arquimediana não vem de um teste finito

Os naturais não são limitados superiormente em ℝ. Se fossem e α fosse seu supremo, α−1 não seria cota superior; haveria n>α−1, logo n+1>α, contradição. Assim podemos escolher naturais maiores que qualquer real dado. Essa propriedade justifica o passo n>1/ε do exemplo, não um limite de iterações do computador.

## Intervalos racionais são certificados de aproximação

Comece com 1<√2<2 e tome o ponto médio racional m. Se m²<2, substitua a ponta esquerda; se m²>2, a direita. A raiz permanece no intervalo, cuja largura após n etapas é 2^(−n). O laboratório usa frações exatas e compara quadrados, sem chamar uma raiz de ponto flutuante. A existência do real buscado vem da matemática anterior, não do número de etapas; a amostra não prova completude.

## Exemplo resolvido

Compare o conjunto S={1−1/n:n≥1} com a lista dos primeiros quatro termos.

Os quatro primeiros são 0, 1/2, 2/3 e 3/4; o máximo dessa lista é 3/4.

No conjunto infinito, todo termo é menor que 1, portanto 1 é cota superior.

Para qualquer n, 1−1/(n+1)>1−1/n; não há máximo.

Dado ε>0, escolha n>1/ε para obter um termo maior que 1−ε.

Logo nenhuma cota menor que 1 funciona: sup S=1, embora 1 não pertença a S.

## Exercícios e resoluções

### Qual é o supremo de (0;1)?

1 é cota superior e há pontos arbitrariamente próximos pela esquerda.

### Qual o máximo dos quatro primeiros termos de 1−1/n?

O último é 1−1/4=3/4.

### Qual a largura do intervalo após quatro reduções a partir de [1;2]?

2^(−4)=1/16.

### Qual a distância entre −2 e 3?

|−2−3|=5.

### Para x=3 e y=−3, quanto vale |x+y|?

|0|=0, embora |x|+|y|=6.

### Todo conjunto com supremo tem esse supremo como elemento?

(0;1) tem supremo 1 sem conter 1.

### O axioma da completude se aplica diretamente a todo conjunto, mesmo vazio ou não limitado?

O enunciado exige conjunto não vazio e limitado superiormente.

### Uma aproximação racional de √2 com muitas casas prova igualdade exata?

√2 é irracional; aproximação não é igualdade.

### Multiplicar a<b por um número negativo inverte a desigualdade?

Se c<0, então ac>bc.

## Preparação manuscrita

Enuncie as hipóteses da completude; contraste máximo e supremo com intervalos; prove a propriedade arquimediana por contradição; prove irracionalidade por paridade; compare conjunto infinito e lista truncada; explique por que a bisseção certifica um intervalo sem provar existência por computador.

## Lacunas restantes

Construções dos reais, densidade, mais exemplos de ínfimo e exercícios de demonstração precisam de aprofundamento. Não há certificação de domínio pessoal.
