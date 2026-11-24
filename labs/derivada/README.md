# Derivada como taxa de variação


Material original em rascunho — 13/10/2026. Revisão de Jhuann pendente.


## A taxa média compara duas observações

Entre a e a+h, a variação é f(a+h)−f(a). A taxa média divide essa variação pelo incremento h, que precisa ser não nulo. Quando h é negativo, numerador e denominador seguem a mesma orientação: estamos comparando com um ponto à esquerda. A unidade é a unidade de f dividida pela da variável.

m(h)=[f(a+h)−f(a)]/h, h≠0


## A derivada é um limite, não uma divisão por zero

Em um ponto interior do domínio, f é diferenciável em a quando o quociente incremental tem um mesmo limite real finito ao aproximar h de zero por ambos os sinais. O valor no ponto f(a) precisa estar definido, assim como os pontos próximos envolvidos. Em extremos de um intervalo pode-se definir uma derivada lateral; deve-se indicar que essa é a convenção usada.

f′(a)=limₕ→₀ [f(a+h)−f(a)]/h


## Calcule primeiro para h diferente de zero

Para f(x)=x², expanda (a+h)²−a²=2ah+h². Dividindo por h≠0, o quociente é 2a+h. Só então passe ao limite: 2a. Não se substitui h=0 no quociente original. O mesmo resultado vale pelas aproximações à esquerda e à direita.

[(a+h)²−a²]/h=2a+h → 2a


## Uma tangente fornece o modelo linear local

A reta y=f(a)+f′(a)(x−a) passa pelo ponto e tem inclinação igual à derivada. Diferenciabilidade equivale a escrever f(a+h)=f(a)+f′(a)h+r(h), com r(h)/h→0. Para o quadrado, r(h)=h² exatamente. A tangente aproxima valores próximos, mas não coincide com toda a curva.

f(a+h)=f(a)+f′(a)h+r(h), r(h)/h→0


## Diferenciabilidade implica continuidade

Se o quociente tende a um número finito, ele fica limitado perto de h=0. Multiplicá-lo por h mostra f(a+h)−f(a)→0. Logo f(a+h)→f(a). A recíproca é falsa: a continuidade sozinha não garante a existência de uma taxa instantânea bilateral.




## Um canto tem duas inclinações incompatíveis

Para f(x)=|x| em zero, o quociente é |h|/h. Pela direita vale 1; pela esquerda vale −1. A função é contínua, mas a derivada em zero não existe. Uma reta tangente com inclinação única, no sentido da definição anterior, não pode representar ambos os lados.

h>0: |h|/h=1; h<0: |h|/h=−1


## A diferença central pode esconder o canto

A fórmula [f(a+h)−f(a−h)]/(2h) usa pontos simétricos. Para |x| em zero, ela é zero para todo h≠0, apesar de não existir derivada. Se uma derivada existe, a diferença central converge para ela; a convergência central isolada não prova diferenciabilidade. Compare também os quocientes laterais.




## Velocidade leva unidades e sinal

Considere s(t)=3t²−2t+5, com t em segundos e s em metros; os coeficientes têm unidades 3 m/s², −2 m/s e 5 m. A taxa média em t é 6t−2+3h m/s, e a velocidade é v(t)=6t−2 m/s. Em t=2, v=10 m/s. Velocidade negativa indica movimento no sentido negativo do eixo. Em uma dimensão, rapidez é |v|.




## Derivada zero em um ponto não força função constante

Para x², f′(0)=0, mas f(1)=1. A informação é local. Constância em todo um intervalo exige derivada zero em todo esse intervalo, junto das hipóteses do Teorema do Valor Médio. Também não basta uma derivada zero para concluir máximo ou mínimo: x³ tem derivada zero em zero e muda de sinal através dele.




## Duas fontes diferentes de erro numérico

No quadrado, usar a secante como aproximação da derivada tem erro algébrico h. Em computadores, avaliar f(a+h)−f(a) pode ainda cancelar algarismos próximos e amplificar arredondamento ao dividir por h. Diminuir h indefinidamente não garante melhorar o resultado em ponto flutuante. A simulação usa a expressão simplificada exata do modelo para destacar o primeiro erro, sem reproduzir o cancelamento.




## Um salto impede até a continuidade necessária

Defina f(0)=0 e f(x)=1 para x≠0. No centro, o quociente é 1/h, sem limite real finito. Uma inclinação que explode não é uma derivada real no sentido desta aula. O laboratório usa esse caso, o canto e o quadrado para contrastar falhas diferentes.




## Exemplo resolvido

Para s(t)=3t²−2t+5 metros, calcule a taxa média entre 2 e 2,5 segundos e a velocidade em t=2.

s(2)=13 m e s(2,5)=18,75 m.

A variação 5,75 m dividida por 0,5 s dá 11,5 m/s.

Em um passo geral h≠0, a taxa média é 10+3h m/s.

No limite h→0, v(2)=10 m/s. A taxa média de um intervalo não é automaticamente a velocidade no início.

O modelo linear s(2+h)≈13+10h tem resto exato 3h² metros, com h em segundos.


## Exercícios e resoluções


### Para f(x)=x², qual é f′(3)?

f′(x)=2x. Em x=3, f′(3)=6.


### A taxa média em a=2 com h=0,5 é:

A taxa média é 2a+h=4+0,5=4,5.


### Para x² em a=2, qual a taxa média com h=−0,5?

2a+h=4−0,5=3,5.


### Qual é a taxa média do movimento s(t)=3t²−2t+5 entre t=2 e t=2,5?

(18,75−13)/0,5=11,5 m/s.


### Qual é a velocidade desse movimento em t=2?

v(t)=6t−2, portanto v(2)=10 m/s.


### Para x² em a=2 e h=0,1, quanto vale o resto em relação à tangente?

O resto exato é h²=0,01.


### A função |x| é diferenciável em zero?

Os limites laterais do quociente são −1 e 1.


### Diferença central igual a zero em todos os passos prova derivada zero?

|x| em zero é um contraexemplo: diferença central zero, sem derivada.


### f′(0)=0 basta para concluir que f é constante?

x² tem derivada zero em zero e não é constante.


## Preparação manuscrita

1. Derivar o quadrado a partir da definição, mantendo h≠0 até o limite.

2. Desenhar secante e tangente e identificar a unidade de cada eixo.

3. Explicar o canto e o contraexemplo à diferença central.

4. Resolver o movimento com metros e segundos, distinguindo média e instantânea.

5. Conferir os testes localmente e explicar por que não são provas de limite.
