# Diferenciação implícita

Material original em rascunho — 13/10/2026. Revisão pessoal pendente.

## Uma relação pode conter mais de um ramo

O círculo x²+y²=25 não é o gráfico de uma única função y de x: para −5<x<5 há um ramo superior e um inferior. Perto de (3,4), pode-se usar y=√(25−x²); perto de (3,−4), y=−√(25−x²). O ponto dado e a vizinhança selecionam o ramo, não a equação isoladamente.



## Derive y como uma função, não como uma constante

Quando y=y(x), a cadeia dá d(y²)/dx=2yy′. Assim, derivar x²+y²=25 ao longo de um ramo diferenciável produz 2x+2yy′=0. Essa conta pressupõe a existência do ramo; ela fornece uma condição necessária para sua derivada.

2x+2yy′=0

## A divisão exige uma condição local

Se y≠0, podemos isolar y′=−x/y. No círculo, a forma explícita do ramo justifica que ele é diferenciável para |x|<5. Em uma relação geral F(x,y)=0, se F tem derivadas parciais contínuas numa vizinhança e Fᵧ(a,b)≠0, o Teorema da Função Implícita garante um ramo local diferenciável. O teorema geral será estudado em cálculo de várias variáveis; não o estamos provando aqui.

y′=−x/y, y≠0

## Verifique o ponto antes de calcular a inclinação

(3,4) satisfaz 9+16=25; a inclinação é −3/4. Em (3,−4), ela é +3/4. Aplicar a fórmula a (1,1) gera um número, mas não uma inclinação do círculo nesse ponto, pois ele não pertence à curva. O laboratório rejeita entradas fora da relação.



## A equação da tangente preserva o ponto

Em (a,b) no círculo, a tangente satisfaz a(x−a)+b(y−b)=0, equivalentemente ax+by=25. O vetor (a,b) é normal à tangente e (−b,a) é tangente: seu produto escalar é zero. Como o raio é 5, esses vetores nunca são ambos nulos. Em (3,4), a reta é 3x+4y=25.



## Uma tangente vertical pede outra representação

Em (5,0), a tangente é x=5. A identidade 2x+2yy′=0 não poderia valer com y′ finito ali: daria 10=0. O círculo continua regular, mas y não é um ramo diferenciável de x naquele ponto. Usar x=√(25−y²) resolve a representação: dx/dy=−y/x=0 em (5,0). Não é adequado escrever uma derivada real infinita; aqui não há dy/dx finito.



## Horizontal e vertical são situações diferentes

Em (0,5), y′=0 e a tangente é horizontal y=5; em (0,−5), é y=−5. Em (±5,0), é vertical. A demonstração usa uma parametrização por ângulo apenas para percorrer o círculo e construir o vetor tangente; ela não presume que y seja função de x em todo o percurso.



## Produtos com y também precisam de duas contribuições

Na relação xy+y²=6, derivar xy exige y+xy′. Logo y+(x+2y)y′=0, e y′=−y/(x+2y) quando x+2y≠0. O ponto (1,2) está na curva e dá y′=−2/5. Derivar xy como apenas xy′ perderia a contribuição da variação de x.



## A segunda derivada usa a cadeia novamente

No ramo do círculo com y≠0, derive x+yy′=0: 1+(y′)²+yy″=0. Substituindo y′=−x/y e x²+y²=25, obtemos y″=−25/y³. Em (3,4), vale −25/64; no ramo inferior em (3,−4), vale +25/64. A concavidade muda com o ramo.

y″=−[1+(y′)²]/y=−25/y³

## Uma fórmula indefinida não classifica toda curva

Para y²−x²=0, a origem leva formalmente à razão x/y=0/0. A relação é a união de duas retas y=x e y=−x, com inclinações diferentes no cruzamento. Nesse caso há singularidade, e não uma única tangente vertical. Quando o coeficiente de y′ é zero, volte à geometria e aos ramos; não conclua sempre a mesma situação.



## Roteiro de uma solução com hipóteses visíveis

Confira se o ponto pertence à curva, declare o ramo local, derive com cadeia e produto, agrupe os termos em y′ e verifique o divisor. Escreva a reta tangente com o ponto e a inclinação, ou como equação normal se for vertical. Confira por um ramo explícito quando disponível. Um cálculo numérico isolado não estabelece existência nem unicidade do ramo.



## Exemplo resolvido

Encontre a tangente e a segunda derivada do ramo do círculo x²+y²=25 no ponto (3,4).

9+16=25: o ponto pertence ao círculo e seleciona o ramo superior.

Como y=4≠0, a derivação implícita fornece y′=−3/4.

A tangente é y−4=−(3/4)(x−3), ou 3x+4y=25.

Derive x+yy′=0: 1+(y′)²+yy″=0.

y″=−(1+9/16)/4=−25/64.

Confira no ramo y=√(25−x²); a inclinação e a concavidade são as mesmas.

## Exercícios e resoluções

### Qual inclinação em (3,4)?

−3/4.

### A fórmula −x/y fornece uma derivada finita em (5,0)?

Divisão por zero corresponde à tangente vertical neste caso.

### Qual a inclinação do círculo em (3,−4)?

−3/(−4)=3/4.

### Qual a inclinação do círculo em (0,5)?

−0/5=0: tangente horizontal.

### Quanto vale y″ em (3,4)?

−25/4³=−25/64.

### Para xy+y²=6, qual y′ em (1,2)?

−2/(1+4)=−2/5.

### A fórmula −x/y dá uma inclinação do círculo no ponto (1,1)?

O ponto não satisfaz x²+y²=25.

### Toda falha de uma razão para y′ significa tangente vertical única?

Na origem de y²−x²=0 há duas retas que se cruzam.

### O círculo inteiro pode ser representado por uma única função y(x)?

Para |x|<5 há dois valores de y; é necessário escolher um ramo.

## Preparação manuscrita

Desenhe os dois ramos do círculo; derive y² pela cadeia; construa a tangente em (3,4) e em (5,0); troque para x(y) no ponto vertical; derive a segunda vez; compare o círculo com o cruzamento y²−x²=0. Peça ao aluno que explique por que uma fórmula avaliada fora da curva não tem interpretação como sua inclinação.
