# Intervalo de confiança: cobertura de um procedimento

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Derivar um intervalo normal bilateral com σ conhecido.
- Interpretar cobertura em repetições sem atribuir posterior automaticamente.
- Separar erro padrão, margem e largura total.
- Avaliar efeitos de tamanho amostral, nível e hipóteses.

## Um intervalo é uma regra que recebe dados

O procedimento produz limites L(X) e U(X) a partir de uma amostra aleatória. Antes da coleta, os limites variam; depois, temos um intervalo observado. Na interpretação frequentista, μ é fixo no modelo e a aleatoriedade está na amostra e nos limites. O nível nominal descreve o procedimento sob hipóteses, não uma declaração universal sobre qualquer intervalo.

IC(X)=[L(X);U(X)]

## O pivô normal fornece a probabilidade conhecida

Sob observações normais iid, com σ conhecido, Z=(X̄−μ)/(σ/√n) é normal padrão. Para nível 1−α, escolha c=Φ⁻¹(1−α/2). Então P(−c≤Z≤c)=1−α. Normalidade e independência dão aqui um resultado exato para todo n≥1; em outros contextos pode haver apenas uma aproximação.

P(−c≤Z≤c)=1−α

## Reorganize o evento para obter os limites

Multiplicar pelo erro padrão positivo e isolar μ transforma o evento em X̄−cσ/√n≤μ≤X̄+cσ/√n. A mesma probabilidade é preservada, produzindo o intervalo bilateral. A demonstração é sobre o procedimento aleatório, não sobre escolher μ depois de observar um resultado.

IC=X̄±cσ/√n

## Erro padrão, margem e largura são grandezas distintas

O erro padrão é σ/√n; a margem é cσ/√n; a largura total é duas vezes a margem. Com σ=2, n=4 e nível 95%, c≈1,959964, erro padrão 1, margem≈1,959964 e largura≈3,919928. Usar c=2 é uma ilustração próxima, não o quantil de 95% exato.

largura=2cσ/√n

## Cobertura é uma frequência do procedimento no modelo

Repetir idealmente a coleta e o cálculo faz o intervalo incluir μ com probabilidade 1−α. Em vinte simulações, a contagem coberta não precisa ser exatamente 19 para um nível de 95%. Cada intervalo observado cobre ou não o parâmetro fixo; a contagem varia. O nível é nominal sob as hipóteses, não promessa de uma fração exata em um conjunto pequeno.

## Posterior exige outra construção

Depois de observar um intervalo frequentista, sua definição de cobertura não fornece automaticamente probabilidade posterior de 95% para μ estar ali. Uma posterior bayesiana exige um modelo de probabilidade para o parâmetro e atualização com os dados. Os dois procedimentos podem responder a perguntas diferentes. Esta aula não constrói uma posterior.

## Tamanho amostral e nível mudam a largura

Mantendo σ e o nível, quadruplicar n divide a margem e a largura por 2. Aumentar o nível aumenta c e amplia o intervalo. Na demonstração, a mesma semente mantém os desvios padronizados para comparar procedimentos: as médias simuladas variam com n, mas a cobertura de cada repetição depende de |Z|≤c.

margem proporcional a 1/√n

## Planeje n para uma margem desejada, com as hipóteses

Se σ e c forem especificados e a margem desejada for m>0, exija cσ/√n≤m; então n≥(cσ/m)² e arredonde para cima. Com σ=2, c=2 ilustrativo e m=0,5, n≥64. A conta não inclui erro sistemático, custo, dependência ou incerteza sobre σ.

n≥(cσ/m)²

## Sigma desconhecido muda o pivô

Substituir σ por s e usar o mesmo quantil normal não produz automaticamente o procedimento exato para n pequeno. Sob normalidade iid e n>1, (X̄−μ)/(s/√n) segue t de Student com n−1 graus de liberdade; seus quantis geram outro intervalo. A demonstração desta aula mantém σ=2 conhecido e não implementa o intervalo t.

## Nem toda incerteza está na margem

Seleção enviesada, erros de instrumento, dependência e um modelo inadequado podem invalidar a cobertura ou mudar o alvo. Um intervalo estreito não comprova precisão em relação à população pretendida. Também não é intervalo de previsão para uma nova observação: a dispersão de um dado individual envolve outra conta.

## Conheça o que a demonstração faz

Geramos diretamente vinte médias normais de μ=5 e σ=2 conhecido, sem ler dados de pesquisa. Os segmentos são intervalos e a linha horizontal marca μ. O nível vai de 90% a 99%; o quantil é obtido numericamente por inversão da CDF conferida. A interface permite comparar tamanho, nível e semente, sem inferir a validade de um experimento real.

## Exemplo resolvido

Média observada 5, σ conhecido 2, n=4: qual IC normal de 95%?

1. Erro padrão = 2 / √4 = 1.
2. c = Φ⁻¹(0,975) ≈ 1,959964.
3. Margem = c × 1 ≈ 1,959964.
4. Limites ≈ [3,040036; 6,959964].
5. Largura ≈ 3,919928.
6. A cobertura de 95% caracteriza o procedimento sob o modelo, não uma posterior construída para este intervalo.

## Exercícios e resoluções

### Com σ=2, n=4 e quantil ilustrativo c=2, qual a margem?

2×1=2.

### z=2 é o quantil exato de 95% normal bilateral?

Sim
Não

O quantil exato é próximo de 1,96, não exatamente 2.

### No mesmo exemplo ilustrativo, qual a largura total?

A margem é 2; largura 2×2=4.

### Com σ=2, c=2 ilustrativo e margem desejada 0,5, qual o menor n pela fórmula?

(2×2/0,5)²=8²=64.

### Uma margem é 2 em n=4. Mantendo σ e c, qual a margem em n=16?

Quadruplicar n divide a margem por 2.

### Média 5 e margem ilustrativa 2: qual o limite inferior?

5−2=3.

### Aumentar o nível, mantendo n e σ, geralmente torna o intervalo:

Mais estreito
Mais largo

Aumenta o quantil bilateral c e a margem.

### Um procedimento de 95% precisa cobrir exatamente 19 dos 20 intervalos simulados?

Sim
Não

A contagem observada varia; o nível não determina uma fração exata em vinte repetições.

### Com σ desconhecido e dados normais iid, o pivô exato com s usa:

Normal padrão em qualquer n
t de Student com n−1 graus de liberdade

A estimação de σ altera a distribuição do pivô.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Usa biblioteca padrão: contas racionais de riscos Bernoulli e quantil normal de NormalDist. Não lê dados privados nem escreve resultados externos.

## Proposta didática

Comece separando regra e valor observado; peça uma previsão antes de variar tamanho/nível; confira a conta manual; termine identificando uma hipótese sem a qual o procedimento não se justifica. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Normal iid e σ conhecido para o intervalo normal exato desta aula.
- Nível bilateral declarado e quantil apropriado.
- Simulação de médias sintéticas, sem dados reais ou decisão científica.
- Procedimento t e intervalos de previsão não estão implementados nesta demonstração.
