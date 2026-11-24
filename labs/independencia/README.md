# Independência: uma hipótese de fatoração

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Comparar probabilidade conjunta com o produto das marginais.
- Distinguir independência de disjunção e de covariância zero.
- Verificar condicionais e complementos quando os denominadores existem.
- Construir um contraexemplo à passagem de independência aos pares para mútua.

## A definição compara conjunta e marginais

A e B são independentes quando P(A∩B)=P(A)P(B). O modelo precisa fornecer ambas as marginais e a conjunta. Saber apenas P(A)=P(B)=1/2 não determina a interseção: ela pode variar de 0 a 1/2. Independência seleciona o valor 1/4 entre essas possibilidades.

P(A∩B)=P(A)P(B)

## Duas moedas: declare a distribuição

Considere Ω={(0,0),(0,1),(1,0),(1,1)} com peso 1/4 em cada par. A indica primeiro componente 1 e B segundo componente 1. Temos P(A)=P(B)=1/2 e P(A∩B)=1/4. Aqui a distribuição conjunta especificada prova a igualdade. Dizer apenas “duas moedas justas” não basta para justificar independência sem uma hipótese sobre como os resultados se relacionam.

P(A∩B)=1/4=(1/2)(1/2)

## Mesmo peso individual, três relações distintas

Com p=q=1/2, a conjunta r=0 dá eventos disjuntos: as únicas células com massa são “apenas A” e “apenas B”. Com r=1/4, as quatro massas são iguais e há independência. Com r=1/2, A e B coincidem com probabilidade 1. O controle da conjunta muda essa relação mantendo as marginais fixas.

r=0: disjunção; r=1/4: independência; r=1/2: coincidência

## Por que disjunção positiva impede independência

Se A e B são disjuntos, P(A∩B)=0. Se ambas as probabilidades são positivas, o produto é positivo e a igualdade falha. Já um evento de probabilidade zero é independente de qualquer B: a interseção tem probabilidade zero por inclusão e o produto também. A condicional em um evento de probabilidade zero continua indefinida pela divisão elementar.

P(A)>0, P(B)>0, A∩B=∅ ⇒ dependência

## A interpretação condicional tem uma condição

Se P(B)>0, divida a igualdade de independência por P(B): P(A|B)=P(A). Reciprocamente, multiplicar essa condicional por P(B) recupera a igualdade. Se P(A)>0, a pergunta inversa também preserva a marginal de B. Não interprete essas frases via divisão quando o denominador é zero.

P(B)>0: independência ⇔ P(A|B)=P(A)

## Complementos também são independentes

Se A e B são independentes, P(A∩Bᶜ)=P(A)−P(A∩B)=P(A)(1−P(B)). Portanto A e Bᶜ são independentes. Repetir o argumento para Aᶜ e B ou para os dois complementos mostra que todas as quatro células fatoram. Isso explica a tabela conjunta de duas variáveis indicadoras independentes.

P(A∩Bᶜ)=P(A)P(Bᶜ)

## Aos pares não é o mesmo que mútua

No mesmo espaço das moedas, acrescente C: os dois componentes são iguais. C={(0,0),(1,1)} tem probabilidade 1/2. Cada par entre A,B,C tem interseção de probabilidade 1/4 e é independente. Mas A∩B∩C={(1,1)} tem probabilidade 1/4, diferente do produto 1/8. Para independência mútua, a fatoração deve valer para toda subfamília com pelo menos dois eventos.

P(A∩B∩C)=1/4≠1/8=P(A)P(B)P(C)

## Covariância zero pode esconder dependência

Escolha X uniforme em {−1,0,1} e Y=X². Então E[X]=0, E[Y]=2/3 e E[XY]=E[X³]=0, logo Cov(X,Y)=0. Porém Y é determinado por X. Mais concretamente, P(X=0,Y=0)=1/3, enquanto P(X=0)P(Y=0)=1/9. A fatoração falha. Para usar covariância precisamos de momentos finitos pertinentes; aqui todos existem.

Cov(X,Y)=E[XY]−E[X]E[Y]=0

## Como conferir a tabela interativa

Os controles escolhem p e q e uma posição entre limites válidos de r. Independência exige r=pq; o ponto médio do intervalo só coincide com isso em alguns casos. O relatório usa tolerância numérica 10⁻¹² para comparar valores calculados. Essa comparação do modelo não é um teste estatístico de independência em dados.

r=pq; diferença r−pq

## Independência não resolve causalidade ou desenho da coleta

A definição expressa uma propriedade probabilística. Ela não prova ausência de qualquer mecanismo causal; uma associação também não prova causa. Em simulações, amostras repetidas e ensaios binomiais, declare por que a hipótese de independência é apropriada. Dados temporais ou de um mesmo grupo podem violá-la, mesmo quando os valores individuais parecem plausíveis.

## Exemplo resolvido

Três eventos de duas moedas: independentes aos pares, mas não mutuamente?

1. Use os quatro pares equiprováveis 00,01,10,11.
2. A={10,11}; B={01,11}; C={00,11}. Todas as marginais valem 1/2.
3. A∩B=A∩C=B∩C={11}; cada conjunta vale 1/4 e cada produto de duas marginais vale 1/4.
4. A∩B∩C={11}, também com probabilidade 1/4.
5. O produto de três marginais é 1/8. A igualdade mútua falha.
6. Conferir apenas pares não autoriza multiplicar todas as marginais.

## Exercícios e resoluções

### No modelo dos quatro pares equiprováveis das duas moedas, qual P(A∩B)?

1/4.

### Eventos disjuntos de probabilidades positivas são independentes?

Sim
Não

A interseção zero difere do produto positivo.

### Se A e B são independentes com probabilidades 0,3 e 0,4, quanto vale P(A∩B)?

O produto é 0,3×0,4=0,12.

### Nos mesmos eventos independentes, quanto vale P(A∪B)?

0,3+0,4−0,12=0,58; independência não elimina a interseção.

### Nos mesmos eventos, quanto vale P(A∩Bᶜ)?

0,3×(1−0,4)=0,18.

### No exemplo de A, B e C das duas moedas, quanto vale P(A∩B∩C)?

A interseção contém apenas 11; probabilidade 1/4, não 1/8.

### Independência de todos os pares garante independência mútua?

Sim
Não

O exemplo das duas moedas e do evento “componentes iguais” viola a igualdade tripla.

### Covariância zero implica independência em qualquer distribuição?

Sim
Não

X uniforme em {−1,0,1}, Y=X² tem covariância zero e eventos que não fatoram.

### Saber somente P(A)=P(B)=1/2 prova independência?

Sim
Não

A conjunta pode ser 0, 1/4 ou 1/2, entre outros valores válidos.

## Experimento e código

Baixe finite.py e execute `python3 finite.py`. Usa apenas a biblioteca padrão, probabilidades racionais e modelos finitos sintéticos. A tabela do navegador usa ponto flutuante. Não há leitura de dados privados ou escrita em arquivos.

## Proposta de condução da aula

Comece enumerando os resultados com o aluno; peça previsão antes de alterar a tabela; resolva um exercício por definição e outro por identidade; encerre com um contraexemplo. A sequência e a duração precisam de revisão didática de Jhuann.

## Hipóteses e limites

- Independência é propriedade de uma distribuição conjunta especificada.
- Equivalências condicionais exigem denominadores positivos.
- Momento/covariância requer existência dos momentos usados.
- Igualdade numérica da demonstração não é teste estatístico nem análise causal.
