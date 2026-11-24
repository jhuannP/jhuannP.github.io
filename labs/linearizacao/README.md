# Linearização e erro local

Material original em rascunho — 13/10/2026. Revisão pessoal pendente.

## Valor e taxa definem um modelo local

A linearização em a é L(a+h)=f(a)+f′(a)h. Ela usa o valor no centro e a taxa instantânea para prever a variação. Se f é diferenciável em a, escreva f(a+h)=L(a+h)+r(h), com r(h)/h→0. Isso justifica a aproximação local, mas não fornece por si só um número para o erro em um passo específico.

L(a+h)=f(a)+f′(a)h

## O diferencial é uma previsão de variação

A variação exata é Δf=f(a+h)−f(a). A previsão linear é df=f′(a)h, ao tomar dx=h. Portanto Δf=df+r(h). O diferencial não é uma segunda observação da função e não é automaticamente igual à variação exata. As duas expressões têm a mesma unidade da saída.



## No quadrado podemos calcular o resto inteiro

Para f(x)=x², (a+h)²=a²+2ah+h². A linearização é a²+2ah e o resto é h², não apenas uma cota. Para h positivo ou negativo, a tangente fica abaixo ou igual à curva. Reduzir |h| à metade reduz o erro a um quarto neste modelo.

r(h)=h²

## Escolher uma tolerância requer uma garantia

No quadrado, exigir erro absoluto ≤ε equivale a h²≤ε, ou |h|≤√ε. Para ε=0,01, basta |h|≤0,1. Essa garantia independe de a neste polinômio. Não se deve transportar o mesmo intervalo para outra função sem analisar seu resto.



## Diferenciabilidade não implica resto quadrático

Em a=0, f(x)=|x|^(3/2) é diferenciável e tem derivada zero: |h|^(3/2)/h tende a zero pelos dois lados. A linearização é zero, com resto |h|^(3/2). Dividir esse resto por h² dá 1/√|h|, que cresce sem limite. Logo não existe uma cota C h² para todo h suficientemente pequeno. O resto ainda é o(h), mas não O(h²).



## Uma cota da segunda derivada controla o erro

Se f é duas vezes continuamente diferenciável no segmento entre a e a+h e |f″(x)|≤M nele, o resto tem módulo ≤M h²/2. Uma justificativa usa r(h)=∫₀ʰ[f′(a+t)−f′(a)]dt. O Valor Médio dá |f′(a+t)−f′(a)|≤M|t|; integrar a cota, respeitando a orientação quando h<0, fornece M h²/2. A hipótese vale no segmento inteiro, não somente no centro.

|r(h)|≤M h²/2

## O inverso mostra o efeito da proximidade ao domínio excluído

Para f(x)=1/x em a≠0, L=1/a−h/a². Se a+h≠0, o resto exato é h²/[a²(a+h)]. Em a=1 e h=0,1, a previsão é 0,9 e o valor é 10/11; o resto é 1/110. Perto de zero, a curvatura e esse fator crescem: o mesmo tamanho de passo pode produzir erros muito distintos. Uma cota via segunda derivada requer que o segmento evite zero.



## Erro relativo pode ser grande perto de zero

Erro absoluto é |f−L|; erro relativo em relação ao valor exato é |f−L|/|f|, quando f≠0. Para x² em a=0 e h≠0, a previsão é zero e o erro absoluto é h², mas o relativo é 1: 100%. Se o valor exato for zero, o erro relativo nesta convenção é indefinido. Declare sempre a referência e não divida por zero.



## Uma derivada pequena também pode esconder variações

Uma taxa f′(a)=0 anula a previsão de primeira ordem, mas não todas as variações. Para x² em a=0, Δf=h². Em um experimento, concluir efeito nulo a partir apenas da sensibilidade linear pode ocultar termos de ordem maior. Esse exemplo é determinístico; propagação estatística de incerteza exige um modelo probabilístico adicional.



## Unidades e hipóteses acompanham a aproximação

Para s(t)=3t²−2t+5 metros, linearize em t=2 segundos: s(2+h)≈13+10h metros, com h em segundos e taxa 10 m/s. O resto exato é 3h² metros, onde o coeficiente é 3 m/s². Não confunda erro dessa aproximação com incerteza de medição ou arredondamento computacional.



## Um roteiro para prever e conferir

Declare o centro e o domínio; calcule valor e derivada; registre a aproximação com símbolo ≈; escolha o passo; determine se há resto exato, uma cota ou apenas comportamento assintótico; indique o erro usado e suas unidades. Confira com o valor exato quando disponível. A simulação cobre x² e não demonstra uma lei universal para toda função.



## Exemplo resolvido

Aproxime 2,1² pela tangente em a=2 e verifique erro absoluto, relativo e uma tolerância de 0,01.

h=0,1. f(2)=4 e f′(2)=4.

L(2,1)=4+4×0,1=4,4; a variação prevista é 0,4.

O valor exato é 4,41 e a variação exata é 0,41.

Resto assinado e erro absoluto valem h²=0,01.

O erro relativo é 0,01/4,41=1/441≈0,002268, ou cerca de 0,227%.

A condição |h|≤√0,01=0,1 garante o erro absoluto desejado neste modelo.

## Exercícios e resoluções

### No exemplo 2,1² linearizado em a=2, qual é o erro absoluto?

O resto é h².

### A reta tangente coincide com x² para todo x?

Há resto h² fora do ponto de expansão.

### Qual a previsão linear para 1/1,1 ao redor de a=1?

1−0,1=0,9.

### No quadrado, qual é a razão entre erros para passos h/2 e h, com h≠0?

(h/2)²/h²=1/4.

### No quadrado, qual é o maior |h| que garante erro absoluto ≤0,04?

√0,04=0,2.

### Se |f″|≤6 no segmento e |h|=0,1, qual cota M h²/2?

6×0,01/2=0,03.

### Diferenciabilidade sozinha garante um resto O(h²)?

|x|^(3/2) em zero tem resto o(h), mas não O(h²).

### Erro absoluto pequeno implica necessariamente erro relativo pequeno?

No quadrado linearizado em zero, o erro relativo é 1 para todo h≠0.

### O erro relativo |f−L|/|f| está definido quando f=0?

Essa convenção divide pelo valor exato; zero no denominador torna o erro relativo indefinido.

## Preparação manuscrita

Construa o quadrado por expansão, desenhe a tangente e marque o resto; compare erro absoluto e relativo; use |x|^(3/2) para mostrar o limite da garantia; deduza a cota M h²/2; feche com o inverso e o cuidado com zero no domínio. Peça ao aluno que classifique cada afirmação como identidade, aproximação ou cota com hipóteses.
