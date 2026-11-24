# Teorema do Valor Médio — notas

Aprofundamento original de 13/10/2026, preparado com apoio de IA para revisão de Jhuann. Notas pessoais não foram importadas.

## O que o teorema garante

Pré-requisitos: continuidade, derivada, extremo local e taxa média. Se a<b, f é contínua em [a,b] e diferenciável em (a,b), então existe pelo menos um c interior com f′(c)=[f(b)−f(a)]/(b−a). A reta secante entre os extremos tem essa inclinação; alguma reta tangente é paralela a ela. O teorema não afirma que c seja o ponto médio nem que seja único. Não exige continuidade da derivada.

`∃c∈(a,b): f′(c)=[f(b)−f(a)]/(b−a)`

## Por que as hipóteses aparecem em intervalos distintos

Continuidade no fechado inclui as duas fronteiras e permite controlar os valores usados na secante. Diferenciabilidade no aberto permite falar em tangentes nos pontos onde c pode estar. Não é preciso ter derivadas bilaterais nas fronteiras; elas não são candidatas do teorema. Um canto interior pode impedir a conclusão, assim como uma descontinuidade numa fronteira pode alterar a taxa média sem alterar as derivadas interiores.

`contínua em [a,b]; diferenciável em (a,b)`

## Rolle: extremos iguais exigem uma taxa zero

Rolle usa as mesmas hipóteses e acrescenta f(a)=f(b). Pelo teorema dos extremos, continuidade no compacto garante máximo e mínimo. Se f é constante, qualquer ponto interior tem derivada zero. Se não é constante, algum valor difere do valor comum das fronteiras; então um máximo ou mínimo global é atingido no interior. Pelo critério de Fermat, diferenciabilidade nesse extremo interior implica derivada zero. A existência de extremos e a derivada no ponto têm papéis diferentes nesse argumento.

`f(a)=f(b) ⇒ ∃c∈(a,b): f′(c)=0`

## Deduzir o Valor Médio de Rolle

Defina m=[f(b)−f(a)]/(b−a) e subtraia a secante: h(x)=f(x)−f(a)−m(x−a). As hipóteses de continuidade/diferenciabilidade são preservadas; h(a)=h(b)=0. Rolle garante h′(c)=0. Como h′(x)=f′(x)−m, obtemos f′(c)=m. Esse argumento transforma uma conclusão de tangente horizontal em uma conclusão de tangente paralela à secante.

`h(x)=f(x)−f(a)−m(x−a); h′(c)=f′(c)−m=0`

## Parábola: aqui o ponto médio funciona

Para f(x)=x² em [1,3], m=(9−1)/(3−1)=4. Como f′(x)=2x, o ponto c=2 satisfaz 2c=4. Em qualquer intervalo a<b, m=a+b e c=(a+b)/2. A solução é única porque a derivada 2x é estritamente crescente. Essas duas características pertencem à parábola; não fazem parte da conclusão geral do teorema.

`m=a+b; c=(a+b)/2 para f(x)=x²`

## Existência sem unicidade ou ponto médio

Para f(x)=x³ em [−1,1], a taxa média é 1. Resolver 3c²=1 dá dois pontos interiores: c=−1/√3 e c=+1/√3. Já em [0,2], a taxa média é 4 e c=2/√3, diferente do ponto médio 1. O teorema garante existência; localizar todos os candidatos exige analisar a derivada e conferir se pertencem ao intervalo aberto.

`em [−1,1]: c=±1/√3; em [0,2]: c=2/√3`

## Contraexemplo: um canto no interior

Para |x| em [−1,1], a função é contínua e a secante tem inclinação zero. Nos pontos negativos, a derivada é −1; nos positivos, é 1; em zero, ela não existe. Não há ponto com derivada zero. Falta a hipótese de diferenciabilidade no interior. O contraexemplo mostra que continuidade sozinha não basta; não diz que todo caso com canto necessariamente teria a mesma falha.

`m=0; f′(x)=−1 ou 1 para x≠0`

## Contraexemplo: descontinuidade na fronteira

Em [0,1], defina f(0)=2 e f(x)=x para x>0. A taxa média entre as fronteiras é (1−2)/(1−0)=−1. Em todo ponto interior, f′(x)=1. Assim não há c com derivada −1. A função é diferenciável no aberto, mas não contínua no fechado. O valor da fronteira afeta a secante e precisa ser compatível com a continuidade.

`m=−1; f′(x)=1 para 0<x<1`

## Consequência: monotonia e constância

Se f satisfaz as hipóteses entre quaisquer dois pontos de um intervalo e f′≥0, então f(b)−f(a)=f′(c)(b−a)≥0: f é não decrescente. Se f′>0 em todo o interior, f é estritamente crescente. Essa condição estrita é suficiente, mas não necessária: x³ é estritamente crescente, apesar de f′(0)=0. Se f′=0 em todo um intervalo, f é constante nele. A palavra intervalo importa; uma função pode ter derivada zero em componentes separados e valores constantes diferentes em cada componente.

`f(b)−f(a)=f′(c)(b−a)`

## Consequência: uma cota para a variação

Se |f′(x)|≤M no interior do intervalo e as hipóteses se mantêm, então |f(b)−f(a)|≤M|b−a|. Isso limita variação sem localizar c. Como |cos(x)|≤1, obtemos |sin(b)−sin(a)|≤|b−a|. Em movimento, se a posição é contínua e diferenciável nas condições do teorema, alguma velocidade instantânea coincide com a velocidade média; essa média usa deslocamento, não distância total percorrida.

`|f(b)−f(a)|≤M|b−a|`

## Roteiro de solução e explicação

Confira domínio e intervalo não degenerado; verifique as duas hipóteses separadamente; calcule a taxa média; derive f no interior; resolva f′(c)=m e descarte candidatos fora do aberto. Para uma aplicação qualitativa, use a identidade para sinais ou cotas, sem inventar um ponto exato. Explique se está garantindo existência, mostrando candidatos ou provando unicidade. O gráfico ajuda a visualizar, mas a justificativa depende das hipóteses.

`hipóteses → secante → derivada → candidatos interiores → interpretação`

## Exercícios e resoluções

Resolva antes de consultar e declare as hipóteses.

### 1. Para f(x)=x² em [1,3], qual o ponto c do exemplo?

Resolução: 2c=4.

### 2. O teorema se aplica a |x| em [−1,1]?

- Sim

- Não

Resolução: Há um canto no interior.

### 3. Para x² em [−2,1], qual a inclinação da secante?

Resolução: −3/3=−1.

### 4. Para x² em [−2,1], qual c satisfaz f′(c)=−1?

Resolução: 2c=−1, logo c=−1/2, interior ao intervalo.

### 5. Para x³ em [−1,1], quantos pontos satisfazem a igualdade do Valor Médio?

- Nenhum

- Um

- Dois

Resolução: c=±1/√3; ambos são interiores.

### 6. O Teorema do Valor Médio exige que f′ seja contínua?

- Sim

- Não; exige existência de f′ no aberto e continuidade de f no fechado

Resolução: A continuidade de f′ não integra o enunciado usado aqui.

### 7. Se |f′|≤3 entre a e b, com as hipóteses do teorema, e |b−a|=0,2, qual a cota M|b−a| para a variação absoluta?

Resolução: 3×0,2=0,6.

### 8. Derivada zero em todo um intervalo implica:

- Função constante nesse intervalo

- Função sempre igual a zero

- Função sem domínio

Resolução: f(b)−f(a)=0. A constante não precisa ser zero.

### 9. No exemplo f(0)=2 e f(x)=x para x>0 em [0,1], qual hipótese falha?

- Diferenciabilidade em todo ponto interior

- Continuidade no intervalo fechado

- Intervalo não degenerado

Resolução: O limite pela direita é zero, diferente de f(0)=2. A derivada no aberto é 1.

## Revisão pessoal

Explique Rolle, a subtração da secante e os dois contraexemplos sem ler. Resolva um caso com mais de um candidato e um caso de cota de variação. O gráfico não substitui demonstração e a revisão do curso continua pendente.
