# Limites laterais: concordar dos dois lados

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Definir aproximação à esquerda e à direita.
- Justificar o critério bilateral quando há aproximação dos dois lados.
- Separar limites laterais de valor no ponto.
- Reconhecer fronteiras de domínio e tipos de falha do limite finito.

## O lado restringe as entradas da aproximação

O limite à esquerda usa x<a; o direito usa x>a. Em ambos, x pertence ao domínio e se aproxima de a sem ser a. Para definir cada limite, o domínio precisa ter pontos arbitrariamente próximos daquele lado. Isso não se resolve olhando apenas o valor f(a).

esquerda: a−δ<x<a; direita: a<x<a+δ

## A definição lateral ainda é universal

Para limite esquerdo L₋, toda ε>0 deve admitir δ>0 tal que os x do domínio em a−δ<x<a satisfaçam |f(x)−L₋|<ε. À direita, troque o intervalo por a<x<a+δ. Uma tabela de entradas positivas não examina a definição à esquerda.

limites laterais usam todos os x admissíveis daquele lado

## O bilateral implica os dois laterais

Se a garantia do limite bilateral vale em 0<|x−a|<δ, também vale ao restringir para x<a ou x>a. Portanto os limites laterais, quando ambos os lados permitem aproximação, são iguais ao limite bilateral. Não é possível um limite bilateral real finito com laterais finitos distintos.

## O acordo dos dois lados também é suficiente

Se ambos os limites laterais são L, escolha os raios δ₋ e δ₊ correspondentes à mesma ε. Use δ=min(δ₋,δ₊). Todo x com distância positiva menor que δ está à esquerda ou à direita e satisfaz a respectiva garantia. Assim existe limite bilateral L.

L₋=L₊=L ⇒ limite bilateral L

## Ramos afins permitem uma justificativa direta

No modelo da demonstração, f(x)=L₋+x para x<0 e f(x)=L₊−x para x>0, com valor b em zero. Os erros em relação aos limites dos ramos têm módulo |x|. Portanto δ=ε garante cada limite lateral. O limite esquerdo é L₋, o direito L₊, e b não participa dessa conta.

## Um salto não é resolvido mudando um ponto

Escolha L₋=−1 e L₊=1. Os limites existem separadamente, mas não concordam; não há limite bilateral real em zero. Nenhuma escolha de f(0) corrige esse desacordo entre os ramos. O valor isolado pode mudar sem alterar os limites laterais.

L₋=−1; L₊=1: não há limite bilateral real

## Um furo é um caso diferente do salto

Se L₋=L₊=2, o limite bilateral é 2. Escolher b=9 mantém o limite, mas a função fica descontínua no ponto; escolher b=2 torna a junção contínua. Nesse caso, uma alteração no ponto basta para remover a descontinuidade. A demonstração permite comparar esses casos sem mudar as inclinações dos ramos.

## Na fronteira, declare o domínio

Para f(x)=√x com domínio [0;∞), aproximar de zero pelo domínio significa aproximar pela direita. Não existe aproximação admissível pela esquerda nesse domínio. O limite relativo ao domínio é 0 e a função é contínua em zero quando f(0)=0. Não exigir artificialmente um ramo em números negativos reais.

## Infinito e oscilação não são o mesmo tipo de falha

Em 1/x perto de zero, o comportamento à esquerda é −∞ e à direita +∞, em sentidos que precisam de definições próprias. Não são limites reais finitos. Uma oscilação também pode impedir um limite sem crescer indefinidamente. O modelo atual apresenta apenas laterais finitos afins; não cobre todos esses comportamentos.

## A ferramenta mostra casos, mas os ramos justificam os limites

Pontos em ±h ilustram aproximações. A classificação vem das fórmulas afins e do critério dos dois lados, não da quantidade de pontos testados. O laboratório racional confere identidades, valor isolado e classificações. Antes de usar um resultado, indique o domínio, o lado e se está falando de limite finito ou infinito.

## Exemplo resolvido

Ramos f(x)=−1+x à esquerda e f(x)=1−x à direita, com f(0)=0: quais limites?

1. À esquerda, f(x)−(−1)=x, que tende a zero.
2. À direita, f(x)−1=−x, que tende a zero.
3. Limites laterais: −1 e 1.
4. Como são distintos, não existe limite bilateral real em zero.
5. O valor f(0)=0 não altera essa conclusão.

## Exercícios e resoluções

### Para o ramo f(x)=1−x em x>0, qual o limite à direita em zero?

O ramo positivo vale 1.

### Existe limite bilateral em 0?

Sim
Não

−1 e 1 são distintos.

### Para o ramo f(x)=−1+x em x<0, qual o limite à esquerda em zero?

O ramo tende a −1.

### Se ambos os limites laterais em a são 2, qual o limite bilateral?

O acordo dos dois lados fornece o limite 2, independentemente de f(a).

### Para a mesma ε, δ₋=0,2 e δ₊=0,05. Qual δ=min(δ₋,δ₊)?

Escolha o menor raio para controlar os dois lados.

### No domínio [0;∞), qual o limite de √x quando x→0 pelo domínio?

A aproximação admissível é à direita; √x tende a 0.

### Escolher f(0)=1 resolve o salto com laterais −1 e 1?

Sim
Não

O valor isolado não muda o desacordo dos limites laterais.

### Uma tabela só com x positivos verifica também o limite esquerdo em zero?

Sim
Não

O lado esquerdo exige aproximações negativas no domínio.

### +∞ é um limite real finito?

Sim
Não

É uma noção distinta de crescimento ilimitado; não é um número real finito.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão e frações; classificação calculada das fórmulas dos ramos. Não lê dados privados nem escreve resultados externos.

## Preparação manuscrita

Defina domínio e aproximações admissíveis; calcule cada lateral por identidade; compare com o valor; desenhe salto/furo/canto; encerre distinguindo continuidade e derivada. As notas pessoais de Cálculo 1 ainda precisam de preparação e revisão de Jhuann.

## Hipóteses e limites

- Critério bilateral usado quando o domínio permite aproximação dos dois lados.
- Modelo da demonstração tem domínio ℝ e ramos afins.
- Limites e valor isolado são grandezas distintas.
- Gráficos e tabelas finitas não substituem a justificativa matemática.
