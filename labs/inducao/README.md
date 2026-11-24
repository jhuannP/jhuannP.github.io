# Indução: provar somas e desigualdades

Material original em rascunho — 16/10/2026. Escopo: CCM0113, programa consultado em 16/10/2026 com ativação em 15/07/2024; versão da turma de 2023 não recuperada. https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0113

## Uma afirmação para todos os naturais

Nesta aula usamos ℕ₀={0,1,2,…}. Uma proposição P(n) tem um valor de verdade para cada n nesse domínio. Conferir alguns valores pode sugerir um padrão, mas a conclusão para todo n precisa de uma justificativa que alcance todos os casos. Fixe também o primeiro índice quando a fórmula só vale a partir de n₀.

## Base e passo formam a estrutura da indução

Para provar P(n) para todo n≥n₀, prove P(n₀) e prove que, para um k arbitrário com k≥n₀, P(k) implica P(k+1). A hipótese indutiva é usada temporariamente dentro dessa implicação. Não é permitido assumir P(k+1), que é justamente o que se quer demonstrar.

## Por que a estrutura alcança todos os índices

Pela boa ordenação dos naturais, se houvesse um contraexemplo, existiria o menor deles m. A base garante m>n₀. Pela minimalidade, P(m−1) seria verdadeira; pelo passo indutivo, P(m) também seria, contradição. Indução e boa ordenação são propriedades fundamentais equivalentes no desenvolvimento usual dos naturais; aqui usamos essa conexão, não uma simulação infinita.

## Somatórios precisam de limites e convenções

Σ de k=1 até n representa a soma dos termos com esses índices. Para n=0, adotamos soma vazia igual a zero. Ao passar de n para n+1, acrescente exatamente o novo termo. O índice de soma é variável ligada: trocar seu nome não muda o valor, mas mudar os limites pode mudar tudo.

## Demonstre a soma dos primeiros naturais

A identidade Σₖ₌₁ⁿ k=n(n+1)/2 vale para n≥0. Base: ambos os lados são zero em n=0. Suponha Σⱼ₌₁ᵏ j=k(k+1)/2, escrevendo j como índice da soma. Ao acrescentar k+1, obtenha k(k+1)/2+(k+1)=(k+1)(k+2)/2, que é a fórmula no próximo índice. A hipótese fornece a soma antiga; a álgebra fecha o passo.

## A soma de ímpares constrói um quadrado

Os n primeiros ímpares são 1,3,…,2n−1 e sua soma é n². Base n=0: zero. Se a soma dos k primeiros é k², acrescente 2(k+1)−1=2k+1. O total vira k²+2k+1=(k+1)². Uma figura de quadrados pode motivar, mas o argumento algébrico explicita base e passo.

## A soma de quadrados exige mais álgebra

A fórmula é Σₖ₌₁ⁿ k²=n(n+1)(2n+1)/6. Base n=0: zero. No passo, acrescente (k+1)² a k(k+1)(2k+1)/6. Fatorando (k+1)/6, sobra 2k²+7k+6=(k+2)(2k+3). O resultado é (k+1)(k+2)(2k+3)/6, a expressão desejada no próximo índice. Isso ajuda a justificar fórmulas das somas de Riemann.

## Uma desigualdade também pode ser induzida

Para n≥0, 2ⁿ≥n+1. A base é 1≥1. Se 2ᵏ≥k+1, multiplicar por 2 positivo preserva a ordem: 2ᵏ⁺¹≥2k+2≥k+2, pois k≥0. O último passo precisa de justificativa; a conclusão não vem apenas de dizer que uma função cresce mais rápido.

## A base sozinha e o passo sozinho são insuficientes

P(n): 2ⁿ>n+1 é falsa em n=0, embora valha em índices posteriores. Já Q(n): n=n+1 é sempre falsa, mas a implicação Q(k)⇒Q(k+1) é logicamente verdadeira quando o antecedente é falso. Sem uma base verdadeira, uma implicação não inicia a cadeia. Também não basta uma base sem demonstrar a transição.

## Quarenta casos verdadeiros podem esconder um contraexemplo

O polinômio n²+n+41 é primo para n=0,…,39, mas em n=40 vale 1681=41². Um teste finito pode refutar uma afirmação universal encontrando um contraexemplo, mas passar em muitos casos não a prova. A recorrência do valor do polinômio não assegura que a primalidade seja preservada no próximo índice.

## Indução forte e próximos usos

Na indução forte, para provar P(k+1), supomos todos os casos de n₀ até k, com base ou bases adequadas. Isso é útil quando uma recorrência depende de mais de um valor anterior. A justificativa geral usa a mesma ideia do menor contraexemplo. Esta aula concentra as demonstrações trabalhadas na indução simples; fatoração, recorrências e mais problemas de indução forte ficam para aprofundamento.

## Exemplo resolvido

Demonstre que a soma dos n primeiros ímpares vale n² e calcule o caso n=4.

Base n=0: a soma vazia vale 0=0².

Hipótese: a soma dos k primeiros ímpares é k².

O próximo ímpar é 2k+1, portanto a soma seguinte é k²+2k+1=(k+1)².

A base e o passo provam a identidade para todo inteiro n≥0.

Em n=4: 1+3+5+7=16=4². O cálculo é uma ilustração da identidade já provada.

## Exercícios e resoluções

### Qual a soma dos inteiros de 1 a 10?

10×11/2=55.

### Qual a soma dos cinco primeiros ímpares?

5²=25.

### Qual a soma de 1²+2²+3²?

1+4+9=14.

### Qual novo termo é acrescentado ao passar da soma dos quatro primeiros ímpares para a dos cinco primeiros?

2×4+1=9.

### Qual o valor de n²+n+41 em n=40?

40²+40+41=1681=41².

### Testar mil casos sem falha prova uma afirmação para todos os naturais?

A verificação é finita; ainda é necessário um argumento universal.

### No passo indutivo, pode-se assumir P(k+1) para provar P(k+1)?

Isso é circular; a hipótese permitida é P(k).

### Uma base verdadeira é necessária na indução?

Sem base, a implicação não inicia a cadeia.

### Ao multiplicar uma desigualdade por 2 positivo, o sentido é preservado?

A compatibilidade da ordem com produto positivo preserva o sentido.

## Preparação manuscrita

Separe base, hipótese e passo por escrito; derive as somas; peça ao aluno que explique o novo termo; analise uma prova circular; mostre o polinômio primo em muitos casos e seu contraexemplo; conclua distinguindo teorema de teste finito.

## Pendências

Mais exercícios de demonstração, indução forte e recorrências. A aula não comprova domínio pessoal nem cobertura integral do programa.
