# Convergência de funções: pontual ou uniforme?

Material original em rascunho — 16/10/2026. Escopo de CCM0123, consultado em 16/10, ativação 01/01/2025; versão da turma de 2024/1 não recuperada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

## Uma sequência pode ter funções como termos

Considere fₙ:D→ℝ, todas no mesmo domínio D. Para cada x fixado, n↦fₙ(x) é uma sequência numérica. Procuramos uma função f que descreva seus limites, quando existirem. O domínio deve acompanhar a afirmação: a mesma sequência pode convergir uniformemente em uma região e não em outra.



## Convergência pontual permite que o índice dependa do ponto

fₙ→f pontualmente significa: para todo x∈D e todo ε>0, existe N=N(x,ε) tal que n≥N implica |fₙ(x)−f(x)|<ε. Primeiro fixa-se x; depois se escolhe um índice adequado àquele ponto. Isso não fornece automaticamente um único N para todos os pontos.



## Convergência uniforme muda a ordem dos quantificadores

A convergência é uniforme quando, para todo ε>0, existe um único N=N(ε) que serve para todo n≥N e todo x∈D. O índice pode depender do domínio e de ε, mas não de x. Uniforme implica pontual; a recíproca não é geral.

∀ε>0 ∃N ∀n≥N ∀x∈D: |fₙ(x)−f(x)|<ε

## O supremo do erro dá uma ferramenta global

Se Eₙ=supₓ∈D |fₙ(x)−f(x)| é finito, convergência uniforme equivale a Eₙ→0. O supremo não precisa ser atingido. Para fₙ(x)=x/n em [0;1], f=0 e Eₙ=1/n. Escolher N>1/ε garante erro <ε simultaneamente em todo o intervalo.

Eₙ=supₓ∈D |fₙ(x)−f(x)|

## Potências em [0;1] têm limite descontínuo

Para fₙ(x)=xⁿ, cada x com 0≤x<1 tem limite zero, enquanto fₙ(1)=1 para todo n. A função limite é f=0 em [0;1) e f(1)=1. O erro é xⁿ quando x<1 e zero em 1. Seu supremo é 1 para todo n, apesar de não ser atingido. Logo a convergência não é uniforme.



## Uma testemunha móvel explicita a falha

Escolha xₙ=1−1/(2n). Cada xₙ<1, portanto f(xₙ)=0. Pela desigualdade de Bernoulli, (1−a)ⁿ≥1−na para 0≤a≤1, obtemos xₙⁿ≥1/2. A desigualdade vem por indução: multiplicar a hipótese por 1−a≥0 acrescenta o termo positivo na². Assim, mesmo com n grande, há um ponto cujo erro não fica abaixo de 1/2. O ponto ruim se move; isso não contradiz convergência em cada x fixo.



## Restringir o domínio pode restaurar uniformidade

Em [0;b] com 0≤b<1, o mesmo xⁿ satisfaz 0≤xⁿ≤bⁿ e o supremo é bⁿ→0. Portanto converge uniformemente para zero nesse domínio. Em [0;1), sem incluir a extremidade, ainda não é uniforme, pois o supremo continua 1. Retirar apenas o ponto 1 não é a mesma coisa que manter uma distância positiva dele.



## O limite uniforme de contínuas é contínuo

Se cada fₙ é contínua em D e fₙ→f uniformemente, f é contínua no domínio relativo. Para um ponto a, escolha uma função f_N cujo erro uniforme seja <ε/3. Pela continuidade dessa função, tome δ que controle |f_N(x)−f_N(a)|<ε/3. A desigualdade triangular soma dois erros uniformes e esse erro local, dando |f(x)−f(a)|<ε. A prova usa apenas uma função escolhida após fixar ε.



## Uniformidade permite uma troca de integral com hipóteses

Se fₙ são Riemann-integráveis em [a;b] e convergem uniformemente para f, então f é integrável e as integrais convergem para a de f. A cota |∫fₙ−∫f|≤(b−a)Eₙ controla o erro. A existência da integral do limite é parte do teorema e não é demonstrada integralmente aqui. Uniformidade é condição suficiente, não necessária: para xⁿ em [0;1], as integrais 1/(n+1) tendem a zero, igual à integral do limite pontual.



## Convergência pontual sozinha não permite trocar integrais

Para n≥2, defina gₙ(x)=n·max(1−n|x−1/n|,0) em [0;1]. É um triângulo contínuo com base [0;2/n], altura n e área 1. Para x>0 fixo, eventualmente x>2/n e gₙ(x)=0; em zero também vale zero. O limite pontual é zero, mas as integrais permanecem 1. O laboratório confere as áreas exatas; a afirmação de limite usa o argumento para cada x fixado.



## Derivar o limite exige mais que uniformidade das funções

A sequência sin(nx)/n converge uniformemente para zero, pois o módulo é ≤1/n. Suas derivadas são cos(nx), que em x=π alternam entre −1 e 1. Assim não convergem nesse ponto para a derivada zero do limite. Trocar limite e derivada exige outras hipóteses; não aplique o teorema de integração como se valesse também para derivação. A demonstração visual é uma amostra finita, e as provas estão nos argumentos anteriores.



## Exemplo resolvido

Para fₙ(x)=x/n em [0;1], encontre um índice que garanta erro estritamente menor que 0,1 em todo o domínio.

O limite é f=0 e o erro |x/n| é limitado por 1/n.

Para ter 1/n<0,1, precisamos n>10.

Escolha N=11; para todo n≥11 e todo x∈[0;1], o erro é ≤1/11<0,1.

N=10 não serve para desigualdade estrita: em x=1, o erro seria exatamente 0,1.

O mesmo N serve para todos os pontos, caracterizando a garantia uniforme.

## Exercícios e resoluções

### Para x/n em [0;1], qual o menor N que garante erro <0,1 para todo n≥N?

N>10; o menor inteiro é 11.

### Qual o supremo do erro de xⁿ para seu limite pontual em [0;1], para cada n≥1?

Valores arbitrariamente próximos de 1 pela esquerda aproximam esse erro.

### Para n=4, qual o supremo de x⁴ em [0;1/2]?

(1/2)⁴=1/16.

### Qual a área do pico triangular de base 2/n e altura n?

(2/n)×n/2=1.

### Qual o limite pontual dos picos triangulares em cada x fixado de [0;1]?

O suporte se aproxima de zero e o valor em zero é sempre zero.

### Na convergência uniforme, o índice N pode depender de x?

Deve servir simultaneamente a todos os pontos do domínio.

### Retirar só o ponto 1 torna xⁿ uniforme em [0;1)?

O supremo do erro continua 1.

### O limite uniforme de funções contínuas é contínuo?

A prova com ε/3 usa a cota uniforme e uma função contínua escolhida.

### Convergência uniforme das funções basta para trocar limite e derivada?

sin(nx)/n é uniforme, mas cos(nx) não converge em x=π.

## Preparação de aula

Troque a ordem dos quantificadores no quadro; compare xⁿ em três domínios; construa uma testemunha móvel; prove a preservação da continuidade por ε/3; mostre o pico de área constante; termine distinguindo integração de derivação.

## Pendências

Atualização29/10/2026: a prova do teorema de integração em intervalo compacto foi desenvolvida por partições em integracao.md,assumindo o critério de Darboux. Critérios de séries uniformes e outras demonstrações continuam pendentes. O conteúdo não certifica domínio pessoal.


Complemento: [prova e limites do domínio](integracao.md). A figura faixa.svg é original;painéis/scripts anteriores preservados.
