# Planos no espaço: normal e incidência

Material original em rascunho — 16/10/2026. Escopo de CCM0123: programa consultado em 16/10, ativação 01/01/2025; versão da turma de 2024/1 não recuperada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

## Um vetor normal fixa a orientação do plano

Um plano em ℝ³ pode ser escrito como n·(R−P₀)=0, com vetor normal n≠0 e ponto P₀ no plano. O produto escalar zero exige que cada deslocamento R−P₀ dentro do plano seja perpendicular à normal. A normal aponta transversalmente ao plano; não é uma direção de deslocamento ao longo dele.

n·(R−P₀)=0, n≠0

## A equação cartesiana vem de abrir o produto

Para n=(a,b,c), temos ax+by+cz=d, onde d=n·P₀. Pelo menos um coeficiente entre a,b,c deve ser não nulo. No plano x+2y−z=3, uma normal é (1,2,−1) e o ponto (3,0,0) pertence. O ponto (0,0,0) não pertence: o lado esquerdo vale zero, diferente de 3.

ax+by+cz=d

## Multiplicar a equação não muda o plano

Se λ≠0, multiplicar normal e d pelo mesmo λ preserva o conjunto de soluções. A orientação da normal pode inverter quando λ<0, mas o plano geométrico não muda. Alterar somente a normal, sem ajustar d, em geral muda o plano. O resíduo n·R−d também escala, por isso não é uma distância geométrica sem normalização.



## Três pontos precisam ser não colineares

Dados A,B,C, forme u=B−A e v=C−A. Se esses vetores forem independentes, n=u×v é não nulo e define uma normal ao plano que contém os três pontos. Se forem dependentes, o produto vetorial é zero: três pontos colineares não selecionam um plano único. Pontos repetidos também podem tornar os dados degenerados.



## A forma paramétrica usa duas direções independentes

Com u,v independentes, R(s,t)=A+s u+t v, para s,t reais, percorre o plano. Uma direção isolada percorre apenas uma reta. Para A=(1,0,0), B=(0,1,0) e C=(0,0,1), a forma é R=(1−s−t,s,t) e a equação é x+y+z=1. Ao substituir, a soma é sempre 1.



## Pertencimento exige conferir a igualdade

Para decidir se Q pertence, calcule n·Q−d. Resíduo zero equivale a pertencer no problema exato. Para x+2y−z=3, Q=(1,1,0) pertence; Q=(1,1,1) não. Não transforme o valor do resíduo em uma distância sem levar em conta a norma da normal e a unidade das coordenadas.



## Substitua a reta e reduza a uma equação escalar

Para a reta R=P+t v, com v≠0, substituir na equação do plano dá n·P+t(n·v)=d. Se n·v≠0, existe um único parâmetro t=(d−n·P)/(n·v). Esse ponto de interseção precisa satisfazer tanto a reta quanto o plano. Não se divide antes de verificar o denominador.

t=(d−n·P)/(n·v), se n·v≠0

## Denominador zero separa dois casos diferentes

Se n·v=0, a direção da reta é paralela ao plano. Se também n·P=d, todo ponto da reta pertence e ela está contida. Caso contrário, nenhum parâmetro resolve e a reta é paralela sem interseção. Neste material, usamos os nomes contida e paralela sem interseção para evitar ambiguidade da palavra paralela.



## Um exemplo de cada caso evita decorar sem entender

No plano x+2y−z=3: a reta (0,0,0)+t(1,0,0) cruza em t=3, ponto (3,0,0). A reta (0,0,0)+t(2,−1,0) nunca cruza, pois x+2y−z permanece zero. A reta (3,0,0)+t(2,−1,0) está contida, pois o mesmo lado permanece 3 para todo t.



## Uma equação degenerada pode não ser plano

Se a=b=c=0, a equação vira 0=d. Para d=0, todo ℝ³ satisfaz; para d≠0, o conjunto é vazio. Nenhum desses casos é um plano afim de dimensão dois. A normal nula é rejeitada pelo laboratório. Analogamente, uma direção nula não é aceita como reta na classificação de incidência.



## Exatidão, tolerância e próximos problemas

A aritmética racional do laboratório verifica igualdade e casos degenerados exatamente. Para dados medidos ou arredondados, classificar um produto escalar quase zero exige critério de tolerância, escala e unidade; isso não está automaticamente resolvido por trocar igualdade por uma constante pequena. Distâncias, ângulos, interseção entre planos e posições relativas entre retas ficam para os próximos blocos.



## Exemplo resolvido

Classifique a reta R(t)=(0,0,0)+t(1,0,0) em relação ao plano x+2y−z=3 e encontre a interseção.

A normal é n=(1,2,−1), com d=3. A direção v=(1,0,0) é não nula.

n·v=1, portanto existe uma interseção única.

n·P=0 e t=(3−0)/1=3.

O ponto é (3,0,0). Substituir no plano dá 3+0−0=3.

A reta não é perpendicular ao plano só por cruzá-lo: para perpendicularidade, sua direção precisaria ser paralela à normal.

## Exercícios e resoluções

### No exemplo resolvido, qual parâmetro gera a interseção?

t=(3−0)/1=3.

### Qual a coordenada z da normal (1,2,−1)?

É o coeficiente de z na equação do plano.

### Para o plano x+2y−z=3, qual o resíduo na origem?

0+0−0−3=−3.

### No plano x+y+z=1, qual x quando y=0 e z=0?

x+0+0=1 dá x=1.

### Quantos pontos de interseção há no caso único?

n·v não nulo fornece um único t.

### Se n·v=0, a reta necessariamente está contida no plano?

Também é preciso conferir n·P=d.

### Três pontos colineares determinam um único plano?

Há planos diferentes contendo a mesma reta.

### Multiplicar toda a equação por −2 preserva o plano?

O fator não nulo preserva o conjunto de soluções.

### A equação 0x+0y+0z=0 define um plano de dimensão dois?

Ela é satisfeita por todo ℝ³.

## Preparação de aula

Construa uma normal; abra a equação; gere o plano por três pontos; substitua uma reta e separe os três casos antes de dividir; mostre a equação degenerada; peça ao aluno para verificar um ponto de interseção por dois caminhos.

## Pendências

Distâncias, ângulos, interseções entre planos e outras posições relativas. Não há certificação de domínio pessoal nem cobertura completa da geometria.
