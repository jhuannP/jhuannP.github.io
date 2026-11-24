# Regras de derivação

Material original em rascunho — 13/10/2026. Revisão de Jhuann pendente.

## Verifique as hipóteses antes de usar uma regra

As regras desta aula pressupõem funções diferenciáveis no ponto interior considerado. No quociente, também é necessário g(a)≠0. Diferenciabilidade implica continuidade: se g(a) não é zero, g permanece não nula em algum entorno pequeno, permitindo definir o quociente ali. Uma expressão com denominador zero no ponto não ganha derivada por aplicar uma fórmula.



## A linearidade vem das operações com limites

Para constantes α e β, o quociente incremental de αf+βg é α vezes o quociente de f mais β vezes o de g. Como ambos têm limites finitos, o limite da combinação é a mesma combinação dos limites. Constantes têm derivada zero; x tem derivada 1.

(αf+βg)′=αf′+βg′

## Abra o incremento do produto sem perder um termo

Escreva f(a+h)g(a+h)−f(a)g(a) como [f(a+h)−f(a)]g(a+h)+f(a)[g(a+h)−g(a)]. Divida por h≠0. O primeiro quociente tende a f′(a), g(a+h) tende a g(a) pela continuidade, e o segundo quociente tende a g′(a). Isso fornece as duas contribuições.

(fg)′=f′g+fg′

## Derivar cada fator e multiplicar não funciona

Para f(x)=g(x)=x, o produto é x², cuja derivada é 2x. Multiplicar f′g′ daria 1, que já está errado em x=0. Cada contribuição da regra preserva um fator sem derivá-lo. Para x²(x+1), obtenha 2x(x+1)+x² e confira expandindo x³+x².



## A regra do inverso sai de uma diferença de frações

Para g(a)≠0, [1/g(a+h)−1/g(a)]/h é −[g(a+h)−g(a)]/[h g(a+h)g(a)]. Por continuidade e derivabilidade, seu limite é −g′(a)/g(a)². O sinal negativo vem da ordem da subtração das frações, não de uma convenção arbitrária.

(1/g)′=−g′/g²

## O quociente é produto com o inverso

Escreva f/g=f·(1/g) e aplique o produto e o inverso. Colocando tudo sobre g², a contribuição do numerador é positiva e a do denominador é subtraída. A ordem importa: trocar os dois termos muda o sinal.

(f/g)′=(f′g−fg′)/g², g≠0

## Potências inteiras podem ser justificadas sem decorar

Para n inteiro positivo, o produto e indução dão (xⁿ)′=nxⁿ⁻¹: a base n=1 vale pela definição, e xⁿ⁺¹=xⁿ·x fornece o passo. Para n=0, x⁰=1 como função constante tem derivada zero. Para n negativo, aplique o inverso no domínio x≠0. Potências reais gerais exigem justificativas adicionais e domínio adequado.



## Confira o quociente por divisão algébrica

Para q(x)=(x²+1)/(x+1), x≠−1, a regra dá [2x(x+1)−(x²+1)]/(x+1)². Dividir polinômios fornece q=x−1+2/(x+1); derivar essa expressão dá 1−2/(x+1)². As duas formas são iguais. Em zero, q′=−1; em um, q′=1/2.



## Cancelar um fator conserva a restrição original

A expressão (x²−1)/(x−1) coincide com x+1 somente para x≠1. Sua derivada é 1 em seu domínio, mas não existe derivada da função original em 1 porque ela nem está definida ali. Definir o valor 2 no ponto cria uma extensão, que então é a função x+1 e tem derivada 1. São funções com domínios distintos.



## Uma regra suficiente não é uma condição necessária

Se um fator não é diferenciável, não use automaticamente a regra do produto naquele ponto. Isso não prova que o produto seja não diferenciável: |x|·|x|=x² é diferenciável em zero, embora cada fator não seja. É possível retornar à definição ou simplificar a função inteira para analisar o caso.



## Organize uma solução que possa ser conferida

Identifique a função e seu domínio; nomeie numerador e denominador ou os fatores; derive os blocos; aplique a regra sem mudar a ordem; simplifique por último; avalie apenas em pontos admissíveis. Uma conferência por expansão ou outra forma algébrica é mais informativa que repetir exatamente a mesma conta. Amostras numéricas não provam a identidade para todo x.



## Exemplo resolvido

Derive q(x)=(x²+1)/(x+1), indique o domínio e encontre q′(1).

O domínio é ℝ sem −1; numerador e denominador são polinômios diferenciáveis.

Use f′=2x e g′=1: q′=[2x(x+1)−(x²+1)]/(x+1)².

Simplifique para (x²+2x−1)/(x+1)².

Em x=1, o valor é (1+2−1)/4=1/2.

Confira por q=x−1+2/(x+1): q′=1−2/(x+1)², que também dá 1/2.

Em −1, a função original não está definida: não substitua esse ponto na fórmula.

## Exercícios e resoluções

### Para p(x)=x²(x+1), qual é p′(2)?

4×3+4=16.

### A derivada de fg é f′g′?

É f′g+fg′.

### Quanto vale a derivada de 3x²−2x+5 em x=2?

6x−2 em 2 vale 10.

### Quanto vale a derivada de (x²+1)/(x+1) em x=0?

1−2/(0+1)²=−1.

### Quanto vale a derivada do mesmo quociente em x=1?

1−2/4=1/2.

### Quanto vale a derivada de 1/x em x=2?

−1/x² em 2 dá −1/4.

### A função original (x²−1)/(x−1) tem derivada em x=1?

Não está definida em 1. Cancelar não altera automaticamente o domínio.

### Se os dois fatores não são diferenciáveis, o produto necessariamente também não é?

|x|·|x|=x² é um contraexemplo em zero.

### Na regra do quociente, podemos trocar a ordem de f′g e fg′ sem mudar o resultado?

Trocar a ordem da subtração muda o sinal.

## Preparação manuscrita

Derive o produto introduzindo um termo intermediário; derive o inverso por diferença de frações; monte o quociente; confira o exemplo por divisão; explique a diferença entre cancelar um fator e preencher um furo. Termine pedindo ao aluno que identifique um erro de sinal e um erro de domínio.
