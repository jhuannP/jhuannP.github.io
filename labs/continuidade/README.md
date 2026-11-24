# Continuidade: encaixar valor e limite

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Verificar continuidade relativa ao domínio.
- Comparar valor, limite e possibilidade de extensão.
- Justificar continuidade de uma composição com domínio adequado.
- Distinguir continuidade de diferenciabilidade e de propriedades globais.

## Continuidade é proximidade no domínio

Uma função definida em a é contínua ali se, para toda ε>0, existe δ>0 tal que x no domínio e |x−a|<δ implica |f(x)−f(a)|<ε. Aqui o centro pode ser incluído, pois seu erro é zero. Em um ponto isolado do domínio, essa condição vale automaticamente escolhendo um raio que não inclua outros pontos.

|x−a|<δ ⇒ |f(x)−f(a)|<ε, x no domínio

## No ponto de acumulação, confira três condições

Quando a pertence ao domínio e é ponto de acumulação, continuidade equivale a: f(a) existe, o limite relativo ao domínio existe e coincide com f(a). Ter apenas um valor definido não basta. Nas junções com domínio ℝ, compare os dois laterais e depois o valor no centro.

limₓ→ₐ f(x)=f(a)

## A extensão de um furo precisa do valor correto

O quociente (x²−4)/(x−2) não é definido em 2, mas seu limite ali é 4. Definir o valor como 4 produz uma nova função contínua, concordante com a original fora de 2. Definir 9 produz uma extensão descontínua. Não dizer que a expressão original já foi calculada no ponto.

## O modelo por partes separa três classificações

Nos ramos L₋+x e L₊−x, há salto se L₋≠L₊. Se ambos os laterais são L e f(0)≠L, a descontinuidade é removível. Se f(0)=L, a junção é contínua. Essas classificações são específicas a ramos com limites finitos; outras funções podem ter comportamento infinito ou oscilatório.

## Um canto prova que continuidade não garante derivada

Quando L₋=L₊=f(0)=c, a função da demonstração é c−|x|. Ela é contínua, pois a desigualdade ||x|−|a||≤|x−a| controla o erro. Em zero, os quocientes de diferença valem +1 à esquerda e −1 à direita, então não há derivada. A existência de derivada é uma exigência mais forte.

derivadas laterais em zero: +1 e −1

## Soma, produto e quociente preservam continuidade com hipóteses

Se f e g são contínuas em a, soma e produto também são. Para o produto, podemos controlar um fator em um entorno e combinar os erros; continuidade fornece esse controle local. O quociente exige g(a)≠0, condição que permite manter o denominador afastado de zero em um entorno. Sempre respeite o domínio.

## A composição usa duas garantias encaixadas

Se g é contínua em a e f é contínua em g(a), para uma tolerância ε de saída escolha uma tolerância η na entrada de f. Pela continuidade de g, há δ fazendo g(x) ficar a menos de η de g(a). Assim f(g(x)) fica a menos de ε de f(g(a)). As saídas de g usadas precisam pertencer ao domínio de f.

continuidade de g em a e de f em g(a) ⇒ continuidade de f∘g

## Fronteiras e conjuntos precisam de contexto

Em [0;∞), √x é contínua em zero pelo limite relativo à direita e valor zero. Em uma função definida só em um conjunto discreto, os pontos isolados pedem a definição relativa ao domínio. A imagem de “desenhar sem levantar a caneta” não substitui a definição e pode falhar fora de intervalos usuais.

## Continuidade em todos os pontos não implica todas as propriedades globais

A função x é contínua em ℝ e não é limitada. Em (0;1), a mesma função é limitada, mas não atinge mínimo ou máximo. Teoremas de existência de extremos em intervalos fechados e limitados usam hipóteses adicionais; o Teorema do Valor Intermediário também exige um intervalo e continuidade. Não elimine essas hipóteses por aparência do gráfico.

## O que demonstrar ao aluno

Peça ao aluno comparar os dois laterais antes de olhar o ponto cheio, depois verificar continuidade. Mostre um salto, um furo preenchido incorretamente e uma junção contínua com canto. O laboratório classifica fórmulas conhecidas; os pontos selecionados só ilustram aproximações. O material permanece em rascunho para revisão didática.

## Exemplo resolvido

Qual valor em 2 torna o quociente (x²−4)/(x−2) uma extensão contínua?

1. Fora de 2, o quociente é x+2.
2. O limite em 2 é 4, com garantia δ=ε.
3. Escolha o novo valor f(2)=4.
4. O limite relativo e o valor passam a coincidir.
5. Isso justifica continuidade dessa extensão; não altera retroativamente o domínio da expressão original.

## Exercícios e resoluções

### Qual valor em 2 torna a extensão do quociente contínua?

Deve igualar o limite.

### Basta que f(a) exista para haver continuidade?

Sim
Não

O limite deve existir e coincidir com o valor.

### Laterais em zero iguais a 2 e f(0)=−3: qual o limite bilateral?

O limite depende dos ramos; ambos tendem a 2.

### Na mesma situação, qual valor deve substituir f(0) para continuidade?

Precisa coincidir com o limite 2.

### No modelo f(x)=−|x|, qual a derivada lateral esquerda em zero?

Para h<0, f(h)=h; quociente f(h)/h=1.

### No mesmo modelo, qual a derivada lateral direita em zero?

Para h>0, f(h)=−h; quociente f(h)/h=−1.

### Ser contínua em um ponto garante derivada nesse ponto?

Sim
Não

−|x| é contínua em zero e tem derivadas laterais distintas.

### A regra de continuidade do quociente permite ignorar g(a)=0?

Sim
Não

A regra exige denominador não nulo no ponto considerado.

### Toda função contínua em ℝ é limitada?

Sim
Não

A função x é contínua em ℝ e não é limitada.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão e frações; classificação calculada das fórmulas dos ramos. Não lê dados privados nem escreve resultados externos.

## Preparação manuscrita

Defina domínio e aproximações admissíveis; calcule cada lateral por identidade; compare com o valor; desenhe salto/furo/canto; encerre distinguindo continuidade e derivada. As notas pessoais de Cálculo 1 ainda precisam de preparação e revisão de Jhuann.

## Hipóteses e limites

- Continuidade relativa ao domínio e valor definido no ponto.
- Critério por limite em pontos de acumulação do domínio.
- Quociente/composição exigem restrições de domínio.
- Modelo da junção é específico, sem representar todas as descontinuidades.
