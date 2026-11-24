# Binomial: contar sucessos em ensaios iguais e independentes

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Identificar ensaios de Bernoulli, independência, p constante e n fixo.
- Derivar a massa binomial pela contagem de sequências.
- Obter esperança e variância por variáveis indicadoras.
- Calcular caudas e distinguir contagens binomiais de experimentos com outras dependências.

## Sucesso é uma definição do experimento

Um ensaio de Bernoulli tem dois resultados, codificados como I=1 para o evento que chamamos sucesso e I=0 para o complemento. Sucesso não significa algo desejável: pode ser encontrar uma peça defeituosa. Com probabilidade p, E[I]=p e Var(I)=p−p²=p(1−p).

I∈{0,1}; P(I=1)=p

## O modelo declara n, p e independência

X=I₁+…+Iₙ conta sucessos em n ensaios independentes com a mesma probabilidade p. O número n é fixado antes da contagem, e cada resultado é sucesso ou fracasso. Neste contexto, independência é mútua, não apenas aos pares. n inteiro não negativo e p∈[0,1] definem a família binomial.

X=Σᵢ Iᵢ

## A probabilidade de uma sequência vem do produto

Uma sequência específica com k sucessos e n−k fracassos tem probabilidade pᵏ(1−p)ⁿ⁻ᵏ, por independência. A ordem importa ao enumerar as sequências, mas X retém apenas a contagem k. Sequências com o mesmo k têm o mesmo peso porque o p de cada ensaio é igual.

P(sequência)=pᵏ(1−p)ⁿ⁻ᵏ

## Conte quais posições recebem os sucessos

Escolha k das n posições para conter sucesso: há C(n,k)=n!/[k!(n−k)!] possibilidades. As sequências são disjuntas, portanto somamos seus pesos. Assim P(X=k)=C(n,k)pᵏ(1−p)ⁿ⁻ᵏ, para k=0,…,n. Fora desse intervalo, a massa é zero.

P(X=k)=C(n,k)pᵏ(1−p)ⁿ⁻ᵏ

## A soma 1 também confere a construção

O teorema binomial dá Σₖ C(n,k)pᵏ(1−p)ⁿ⁻ᵏ=(p+1−p)ⁿ=1. Outra justificativa é que todas as sequências possíveis particionam o espaço dos n ensaios. No laboratório, enumerar sequências para n pequeno fornece uma verificação independente da fórmula fechada.

Σₖ P(X=k)=1

## Derive a média pelas indicadoras

Pela linearidade, E[X]=Σᵢ E[Iᵢ]=np. Esse passo não precisa de independência: se todos os ensaios têm marginal p, a média da contagem ainda é np mesmo com dependência. A distribuição completa e a fórmula da variância precisam de hipóteses adicionais.

E[X]=np

## Derive a variância e reconheça a hipótese usada

Independência implica covariâncias zero entre as indicadoras, então Var(X)=Σᵢ Var(Iᵢ)=np(1−p). Se todos os ensaios repetem a mesma variável de Bernoulli, X=nI: a média continua np, mas Var(X)=n²p(1−p). Para n>1 e 0<p<1, esse modelo não é a binomial.

Var(X)=np(1−p)

## Exatamente, no máximo e pelo menos são perguntas distintas

Exatamente k usa uma massa. No máximo k soma massas de 0 até k. Pelo menos k soma de k até n, ou usa 1−P(X≤k−1). Para pelo menos um sucesso, o complemento é nenhum: P(X≥1)=1−(1−p)ⁿ. O limite k−1 evita incluir indevidamente a massa em k duas vezes.

P(X≥1)=1−(1−p)ⁿ

## Casos degenerados não são erros

Se n=0, a soma vazia vale X=0 com probabilidade 1, independentemente de p. Se p=0, X=0; se p=1, X=n. Todos têm variância zero. A expressão combinatória é interpretada de modo consistente nos expoentes zero, incluindo 0⁰ como termo vazio da construção. No gráfico, as hastes são massas em k inteiro, não uma densidade contínua.

## Quando a contagem deixa de ser binomial

Amostragem sem reposição de uma população finita geralmente torna os ensaios dependentes. Ensaios independentes com probabilidades diferentes também não seguem em geral esta binomial; a distribuição da soma precisa considerar cada taxa. Parar no primeiro sucesso não mantém n fixo. Isso exige escolher outro modelo, em vez de inserir uma média de taxas na fórmula sem justificativa.

## Modelar não é estimar p nem comprovar independência

As demonstrações usam p escolhido e ensaios hipotéticos. Em uma aplicação real, justificar a coleta e estimar p são etapas adicionais, com incerteza. Uma contagem próxima de np não comprova a distribuição binomial; uma contagem distante também não refuta sozinha o modelo. No Python deste laboratório n vai até 100; a interface limita n a 20 para leitura, sem alegar que esses limites fazem parte da teoria.

## Exemplo resolvido

Em três ensaios independentes com p=1/2, qual P(X=2) e P(X≥2)?

1. As oito sequências têm peso 1/8.
2. Exatamente dois sucessos: 110,101,011; P(X=2)=3/8.
3. Três sucessos: 111, com probabilidade 1/8.
4. P(X≥2)=3/8+1/8=1/2.
5. E[X]=3/2 e Var(X)=3/4.
6. Uma realização pode ser 0,1,2 ou 3; a média 1,5 não é uma contagem observável.

## Exercícios e resoluções

### Com n=3, p=1/2 e ensaios independentes, qual P(X=2)?

3/8.

### O modelo binomial permite p variar livremente entre os ensaios sem mudar distribuição?

Sim
Não

p constante faz parte do modelo.

### No mesmo modelo, qual P(X≥2)?

P(X=2)+P(X=3)=3/8+1/8=1/2.

### Com n=3 e p=1/2, qual P(X≥1)?

1−P(X=0)=1−1/8=7/8.

### Com n=10 e p=0,2, qual E[X]?

np=10×0,2=2.

### No mesmo modelo binomial, qual Var(X)?

np(1−p)=10×0,2×0,8=1,6.

### Se os três ensaios repetem a mesma Bernoulli de p=1/2, qual Var(3I)?

3²×(1/2)×(1/2)=9/4=2,25; não é a variância binomial.

### Se n=0, a distribuição de X é:

X=0 com probabilidade 1
Indefinida

A soma vazia vale zero, com massa total 1.

### Amostrar sem reposição permite assumir automaticamente ensaios independentes?

Sim
Não

Retirar um elemento geralmente altera as probabilidades condicionais das retiradas seguintes.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`, usando apenas biblioteca padrão. Modelos racionais finitos e comparação de cancelamento em ponto flutuante. Sem leitura de arquivos privados ou escrita de resultados externos.

## Proposta didática

Peça uma previsão antes de alterar os controles; calcule um caso manualmente; compare média, dispersão e uma realização possível; encerre verificando uma hipótese do modelo. A condução e a duração precisam de revisão de Jhuann.

## Hipóteses e limites

- Número de ensaios fixo, p constante e independência mútua para a massa binomial.
- n inteiro não negativo e p entre 0 e 1, incluindo casos degenerados.
- Laboratório racional limitado a n≤100; interface a n≤20.
- Probabilidades sintéticas, não ajuste ou validação de dados reais.
