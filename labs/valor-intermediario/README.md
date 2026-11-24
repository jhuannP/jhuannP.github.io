# Valor intermediário: existência sem localizar a raiz

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Enunciar o TVI com continuidade e intervalo.
- Justificar existência pelo argumento do supremo.
- Separar existência, unicidade e localização numérica.
- Identificar falha da garantia quando há salto.

## A continuidade impede pular um valor intermediário

Se f é contínua em [a;b], a<b, ela assume todo valor y entre f(a) e f(b). Se y está estritamente entre esses valores, existe c no intervalo aberto (a;b) com f(c)=y. Se y coincide com uma extremidade, essa própria extremidade já fornece uma solução. O domínio precisa conter o intervalo usado.

## Reformule o problema como busca de zero

Defina h(x)=f(x)−y, que continua contínua. Se f(a)<y<f(b), então h(a)<0<h(b). Assim basta provar a versão de mudança de sinal. Se a ordem dos sinais estiver invertida, trocar h por −h resolve a orientação sem mudar seus zeros.

h(a)<0<h(b) ⇒ ∃c∈(a;b): h(c)=0

## O supremo constrói um candidato sem assumir monotonia

Para h(a)<0<h(b), considere S={x∈[a;b]:h(x)<0}. Ele é não vazio porque contém a e é limitado por b; pela completude dos reais, c=sup S existe. Continuidade em a mantém valores negativos em um pequeno trecho à direita e continuidade em b mantém valores positivos perto de b. Portanto a<c<b. Não exigimos que h seja crescente.

## A continuidade força o candidato a ter valor zero

Se h(c)<0, continuidade manteria h negativo um pouco à direita de c, produzindo um ponto de S maior que seu supremo. Se h(c)>0, haveria um pequeno intervalo à esquerda de c sem pontos de S, contradizendo pontos de S arbitrariamente próximos do supremo. Restaria apenas h(c)=0. Esse argumento usa o domínio contínuo e a completude dos reais.

## O teorema prova existência, não conta todas as soluções

Para f(x)=x³−x em [−2;2], os sinais nas extremidades são opostos e há zeros em −1,0,1, pela fatoração x(x−1)(x+1). O TVI não garante exatamente uma raiz. Uma bissecção que encontra zero não exclui as demais.

x³−x=x(x−1)(x+1)

## Unicidade precisa de um argumento adicional

Para x³−2 em [1;2], continuidade e sinais opostos garantem uma raiz. O crescimento estrito da cúbica nesse intervalo garante no máximo uma. Para u>v≥1, u³−v³=(u−v)(u²+uv+v²)>0. Assim existência e unicidade vêm de dois argumentos distintos, sem precisar de uma fórmula fechada para a raiz.

## Um salto fornece mudança de sinal sem raiz

Defina f(x)=−1 para x<0 e f(x)=1 para x≥0. Em [−1;1], as extremidades têm sinais opostos, mas os únicos valores são −1 e 1: zero nunca ocorre. Há descontinuidade em zero e o TVI não se aplica. Ausência de uma hipótese não prova ausência de raiz em toda função; este exemplo mostra que a garantia pode falhar.

## Bissecção mantém um intervalo sob as hipóteses

Quando a função é contínua e os sinais são opostos, avaliar o ponto médio permite manter uma das metades com sinais opostos, ou encontrar um zero. Após N reduções sem parada por zero, a largura é (b₀−a₀)/2ᴺ. A existência dentro do intervalo torna útil a aproximação pelo ponto médio. O teorema não fornece sozinho avaliação exata ou estabilidade de um algoritmo.

largura após N reduções=(b₀−a₀)/2ᴺ

## Estreitar um intervalo não substitui a hipótese

No salto da demonstração, a regra dos sinais também estreita o intervalo perto de zero. Porém, nenhum candidato zera a função e o módulo do resíduo permanece 1. Um critério apenas de largura poderia devolver um número sem ser raiz. A demonstração compara esse caso com duas funções contínuas.

## Como usar o resultado em uma solução escrita

Declare o intervalo, justifique continuidade, calcule valores das extremidades e diga qual valor intermediário é buscado. Conclua ao menos uma solução. Se precisar de unicidade, apresente uma hipótese adicional; se precisar de uma aproximação, especifique método e critério. Não substituir essas etapas por um gráfico com poucos pontos.

## Exemplo resolvido

Para x³−2 em [1;2], o que o TVI garante e qual a primeira redução?

1. O polinômio é contínuo em todo o intervalo.
2. f(1)=−1 e f(2)=6, então existe uma raiz em (1;2).
3. Crescimento estrito fornece unicidade por argumento adicional.
4. O meio é 1,5 e f(1,5)=1,375>0.
5. O novo intervalo com sinais opostos é [1;1,5].
6. Isso localiza melhor uma solução cuja existência já foi justificada.

## Exercícios e resoluções

### Após a primeira redução para x³−2 em [1;2], qual o novo extremo superior?

O sinal positivo do meio permite substituir b.

### O teorema garante exatamente uma raiz em todo caso?

Sim
Não

Ele garante ao menos uma; unicidade exige outra hipótese.

### Quanto vale f(1) para f(x)=x³−2?

1³−2=−1.

### Partindo de um intervalo de largura 1, qual a largura após quatro reduções sem parada?

1/2⁴=1/16.

### Quantas raízes reais distintas tem x³−x?

A fatoração x(x−1)(x+1) dá −1,0,1.

### No salto com valores −1 e 1, qual o módulo do resíduo em qualquer candidato?

Os únicos valores são ±1; o módulo nunca é zero.

### Mudança de sinal sozinha garante raiz sem nenhuma hipótese estrutural?

Sim
Não

O salto da aula tem sinais opostos e nenhuma raiz.

### A prova do TVI exige que a função seja monótona?

Sim
Não

O argumento do supremo usa continuidade; a função pode assumir um valor várias vezes.

### O TVI fornece automaticamente uma aproximação com erro numérico controlado?

Sim
Não

O teorema garante existência; método, avaliação e critério de erro são etapas adicionais.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão, intervalos racionais e avaliação trigonométrica em ponto flutuante. Casos computacionais não substituem as provas. Não lê dados privados nem escreve resultados externos.

## Preparação manuscrita

Escreva enunciado e hipóteses; justifique o exemplo; separe existência de cálculo, ou cota de valor exato; desenhe o contraexemplo; resolva exercícios antes da ferramenta. Revisão e notas pessoais de Jhuann continuam pendentes.

## Hipóteses e limites

- Continuidade no intervalo fechado e domínio contendo todo esse intervalo.
- Valor buscado entre os valores das extremidades.
- Unicidade e aproximação requerem argumentos adicionais.
- Laboratório sintético; avaliação racional não resolve toda equação real.
