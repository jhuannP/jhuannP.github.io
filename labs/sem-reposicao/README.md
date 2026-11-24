# Sem reposição: condicionais, contagem e distribuição hipergeométrica

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: condicionamento, contagem por combinações, indicadoras e binomial. Percurso complementar; não é nova disciplina do histórico.

## O protocolo de retirada faz parte do modelo

Uma urna contém N objetos identificáveis, K vermelhos e N−K azuis. Em cada etapa escolhemos uniformemente um dos objetos restantes e não o devolvemos. O número n de retiradas é fixado antes do sorteio, com 0≤n≤N. Uniformidade é sobre objetos, não sobre cores. V significa vermelha e A significa azul nesta aula. A população é fechada: nenhuma entrada, saída adicional ou mudança de tipo ocorre durante o experimento.



## A primeira cor muda a urna disponível

No exemplo original, N=5, K=3 e n=2. A primeira retirada é vermelha com probabilidade 3/5. Se saiu V, restam duas vermelhas entre quatro objetos, logo P(V₂|V₁)=1/2. Se saiu A, restam três vermelhas entre quatro, logo P(V₂|A₁)=3/4. Os índices indicam a posição da retirada, e não a identidade de um objeto. A informação da primeira cor muda a probabilidade da segunda.

P(V₂|V₁)=2/4; P(V₂|A₁)=3/4

## Multiplique condicionais ao longo dos caminhos

O caminho VV tem probabilidade (3/5)(2/4)=3/10. VA tem (3/5)(2/4)=3/10; AV tem (2/5)(3/4)=3/10; AA tem (2/5)(1/4)=1/10. São caminhos disjuntos que cobrem as possibilidades de duas cores, e suas massas somam 1. As probabilidades ao lado dos segundos ramos já incorporam o resultado do primeiro. Não multiplique marginais como se os sorteios fossem independentes.



## A marginal da segunda retirada não mudou

Use probabilidade total na partição formada pelas duas primeiras cores possíveis: P(V₂)=P(V₂|V₁)P(V₁)+P(V₂|A₁)P(A₁). No exemplo, (1/2)(3/5)+(3/4)(2/5)=3/5. Assim as duas posições têm a mesma marginal, mas não são independentes: a conjunta VV é 3/10, diferente de (3/5)²=9/25. Mesmas marginais não implicam independência.

P(V₂)=3/5, mas P(V₁∩V₂)=3/10 ≠ 9/25

## Contar vermelhas é esquecer a ordem

Defina X como o número de vermelhas entre as duas retiradas. X=1 reúne VA e AV, portanto sua massa é 3/10+3/10=3/5. As massas de X=0,1,2 são respectivamente 1/10, 3/5 e 3/10. Um caminho específico e um evento sobre a contagem são objetos diferentes. Escolher as cores não é escolher um par de objetos identificáveis: vários pares de objetos dão a mesma sequência de cores.

P(X=1)=P(VA)+P(AV)=3/5

## Derive a massa por subconjuntos de objetos

Uma sequência ordenada de n objetos distintos tem chance 1/[N(N−1)…(N−n+1)]. Cada subconjunto de tamanho n corresponde a n! ordens, logo os C(N,n) subconjuntos são equiprováveis. Para obter k vermelhas, escolha k entre as K vermelhas e n−k entre as N−K azuis. O produto de combinações conta subconjuntos favoráveis. Dividindo pelo total obtemos a distribuição hipergeométrica. Para n=0 há apenas o subconjunto vazio e X=0.

P(X=k)=C(K,k)C(N−K,n−k)/C(N,n)

## O suporte impede retiradas impossíveis

O número k não pode ser negativo, maior que n ou maior que K. Também precisamos n−k≤N−K, pois não podemos retirar mais azuis do que existem. Reunindo as restrições, max(0,n−(N−K))≤k≤min(n,K). Fora desse intervalo a massa é zero. A soma das contagens favoráveis é C(N,n), já que os subconjuntos se particionam pelo número de vermelhas: isso verifica a normalização.

max(0,n−(N−K)) ≤ k ≤ min(n,K)

## A média depende das marginais; a variância depende também da relação entre posições

Escreva X=I₁+…+Iₙ, com Iᵢ=1 se a posição i é vermelha e 0 caso contrário. Por simetria cada posição tem probabilidade p=K/N, então E[X]=np, sem precisar de independência. Para N>1 e posições distintas, E[IᵢIⱼ]=K(K−1)/[N(N−1)]. Subtraindo p² obtemos Cov(Iᵢ,Iⱼ)=−p(1−p)/(N−1). Quando 0<K<N essa covariância é negativa. Se só há uma cor, ela é zero: os indicadores são constantes.

Cov(Iᵢ,Iⱼ)=−p(1−p)/(N−1), para N>1

## A correção de população finita vem da soma das covariâncias

Na variância da soma há n variâncias p(1−p) e n(n−1) covariâncias entre posições distintas. Substituindo a expressão anterior: Var(X)=np(1−p)−n(n−1)p(1−p)/(N−1)=np(1−p)(N−n)/(N−1). Quando n=N, conhecemos a contagem X=K e a variância é zero. Para N=1, X é determinístico para n=0 ou 1; não usamos a expressão com denominador N−1.

Var(X)=np(1−p)(N−n)/(N−1)

## Com reposição o experimento é outro

Se devolvemos cada objeto e cada nova escolha é uniforme e independente das anteriores, a probabilidade de V fica p=K/N em todas as etapas, mesmo após conhecer os resultados passados. Então X tem distribuição binomial. Só devolver o objeto não prova independência: ela também é hipótese do mecanismo. Para a urna de cinco objetos, a binomial de n=2,p=3/5 dá massas 4/25,12/25,9/25; sem reposição elas são 1/10,3/5,3/10. A média é 6/5 em ambos; as variâncias são 12/25 com reposição e 9/25 sem reposição.

Sem reposição: P(X=2)=3/10; com reposição independente: 9/25

## Uma aproximação precisa de regime e de critério de erro

Para n fixo, numa sequência de populações N→∞ com K/N→p, a massa hipergeométrica para cada k tende à binomial de parâmetros n,p. Em cada uma das finitíssimas retiradas o efeito de remover um objeto fica pequeno nesse limite. Isso não torna a distribuição finita exatamente binomial. A fração amostral ajuda a avaliar a diferença de variâncias, mas sozinha não define uma tolerância universal para probabilidades de cauda. Antes de aproximar, declare qual evento e erro importam; o laboratório permite comparar as massas exatas de modelos finitos.



## O que o laboratório verifica e o que continua pendente

O Python calcula massas por combinações e caminhos por atualização da urna, usando Fraction. Testes separados enumeram subconjuntos e sequências de objetos identificáveis para populações pequenas. Esses modelos são hipotéticos, sem estimativa de composição, coleta real ou resultado da IC. Aulas de condicionamento e binomial fornecem os pré-requisitos; inferência sobre populações desconhecidas, amostragem enviesada e limites quantitativos de aproximação ficam para depois. Conteúdo original em rascunho, aguardando revisão de Jhuann.



## Exemplo resolvido

Uma urna tem três vermelhas e duas azuis. Em duas retiradas uniformes sem reposição, qual a probabilidade de exatamente uma vermelha?

1. Dados: N=5, K=3, n=2. X conta vermelhas; queremos P(X=1).
2. O modelo é sem reposição: a composição muda após a primeira retirada.
3. Caminho VA: (3/5)(2/4)=3/10. Caminho AV: (2/5)(3/4)=3/10.
4. Os caminhos são disjuntos: P(X=1)=3/5.
5. Por subconjuntos: C(3,1)C(2,1)/C(5,2)=6/10=3/5.
6. Conferência: P(X=0)=1/10 e P(X=2)=3/10; somam 1 com P(X=1). Binomial com reposição daria 12/25, outra resposta para outro protocolo.

## Exercícios e resoluções

1. Na urna de 3 vermelhas e 2 azuis, quanto é P(V₁)?

   Resolução: Três objetos vermelhos entre cinco: 3/5.

2. Sem reposição, quanto é P(V₂|V₁)?

   Resolução: Após sair V restam 2 vermelhas entre 4 objetos: 1/2.

3. Sem reposição, quanto é P(V₂|A₁)?

   Resolução: Após sair A restam 3 vermelhas entre 4 objetos: 3/4.

4. Qual é P(V₁∩V₂) sem reposição?

   Resolução: Regra do produto: (3/5)(2/4)=3/10.

5. Qual a probabilidade de exatamente uma vermelha nas duas retiradas sem reposição?

   Resolução: Some VA e AV: 3/10+3/10=3/5.

6. Sem saber a primeira cor, quanto é P(V₂)?

   Resolução: Probabilidade total: (1/2)(3/5)+(3/4)(2/5)=3/5.

7. As duas posições terem a mesma chance marginal de vermelha prova independência?

   Resolução: Não. A conjunta é 3/10, diferente de 9/25, o produto das marginais.

8. Com N=7, K=5 e n=4, qual o MENOR valor possível de X?

   Resolução: Há só duas azuis, então pelo menos duas das quatro retiradas são vermelhas: max(0,4−2)=2.

9. Na urna inicial de N=5, K=3, n=2, quanto é E[X]?

   Resolução: Linearidade das indicadoras: 2×3/5=6/5.

10. Na mesma urna sem reposição, quanto é Var(X)?

   Resolução: 2(3/5)(2/5)(3/4)=9/25. O fator 3/4 vem de (N−n)/(N−1).

11. Retirando todos os cinco objetos, qual é Var(X)?

   Resolução: X=3 em todo resultado possível; uma constante tem variância zero.

12. Devolver os objetos basta, por si só, para provar que as retiradas são independentes?

   Resolução: Não. A reposição preserva a composição, mas independência também depende do mecanismo de escolha assumido.

## Fontes e convenções

Consulta parcial: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §3.3, pp.94–95 (PDF109–110), definição 3.8. Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §2.3, pp.87–88 e 90–91 (PDF48–50; duas páginas impressas por página do PDF), definição 2.11 e relação entre hipergeométrica e binomial. A p.87/PDF48 também foi conferida visualmente. Os textos usam n,m,r para população, objetos do tipo I e amostra; aqui usamos N,K,n. Os exemplares permanecem privados; nenhuma página, figura, questão ou solução dos autores foi distribuída.

A árvore, os parâmetros do exemplo, exercícios, derivação por indicadoras e código destas notas são originais. As páginas consultadas fundamentam o modelo e a comparação; não se afirma ter lido capítulos completos. Nestas notas os extremos n=0 e n=N são explicitamente incluídos e verificados. A variância para N=1 é tratada como caso determinístico, sem divisão por zero.

## Reprodução

Na raiz do site, sem instalar pacotes:

```sh
python3 -m labs.sem-reposicao.example
python3 -m unittest discover -s labs/sem-reposicao -t .
```

A enumeração dos testes verifica populações pequenas: não é um método eficiente para populações grandes. A função de massas usa combinações e aritmética racional exata, mas o custo de inteiros e frações cresce com os parâmetros. Não há simulação de coleta real, estimação, desenho de pesquisa ou garantia de erro para aproximação binomial nesta aula.

## Verificação de 22/10/2026

Cinco testes novos aprovados por enumeração de objetos; suíte global de 824 testes Python e 482 estruturas MathML aprovadas. No navegador, respostas 3/5 e 9/25 aceitas. Árvore conferida em 390 px, sem transbordamento horizontal e sem erros de console observados. Revisão conceitual e pessoal de Jhuann pendente.
