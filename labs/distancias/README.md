# Distâncias e projeções: normalizar antes de medir

Material original em rascunho — 16/10/2026. Escopo de CCM0123, consultado em 16/10, ativação 01/01/2025; versão da turma de 2024/1 não recuperada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

## Distância é o menor comprimento permitido

No espaço euclidiano, a distância de R a um conjunto é o ínfimo de ||R−T|| para T no conjunto. Para uma reta ou plano não degenerados, existe um ponto H que realiza esse mínimo: o pé da projeção ortogonal. A distância é não negativa e vale zero exatamente quando R pertence à reta ou ao plano considerado.



## Resíduo de uma equação não é medida geométrica invariável

No plano n·T=d, o resíduo de R é e=n·R−d. Multiplicar n e d por λ≠0 multiplica e por λ, embora o plano permaneça o mesmo. Portanto |e| sozinho não pode representar a distância de maneira independente da equação escolhida. É preciso dividir pela norma da normal.



## A normal unitária fornece a escala correta

A distância de R ao plano é |n·R−d|/||n||, com n≠0. A versão assinada (n·R−d)/||n|| depende da orientação escolhida para n; ao inverter n e d, seu sinal troca. A distância sem sinal permanece igual. Se coordenadas são comprimentos e n é tratado como coeficiente adimensional, a distância tem unidade de comprimento.

dist(R,π)=|n·R−d|/||n||

## Encontre o pé impondo pertencimento

O deslocamento R−H deve ser paralelo a n. Escreva H=R−αn. Impor n·H=d dá α=(n·R−d)/(n·n). Assim H está no plano e o deslocamento é normal a ele. Note que a fórmula do pé divide pela norma ao quadrado; a fórmula da distância divide pela norma.

H=R−[(n·R−d)/(n·n)]n

## Pitágoras demonstra o mínimo global

Para qualquer T no plano, H−T é perpendicular a R−H. Logo ||R−T||²=||R−H||²+||H−T||²≥||R−H||². Isso prova que H minimiza a distância e que a igualdade exige T=H. A mesma justificativa vale para a projeção numa reta, quando o resíduo é perpendicular à sua direção.



## Um exemplo de plano preserva frações exatas

Para R=(1,1,1) e plano x+y+z=1, n=(1,1,1), e=2 e n·n=3. O pé é H=(1/3,1/3,1/3). A distância é 2/√3 e seu quadrado é 4/3. O laboratório retorna o quadrado racional exato, sem apresentar uma aproximação decimal da raiz como igualdade exata.



## Na reta, projete o deslocamento na direção

Para a reta P+t v, v≠0, forme w=R−P. O parâmetro do pé é t*=w·v/(v·v). Então H=P+t*v e o resíduo R−H é perpendicular a v. A distância é ||R−H||. Trocar v por múltiplo não nulo muda o parâmetro, mas preserva o pé e a distância.

t*=[(R−P)·v]/(v·v)

## A norma do resíduo confere o cálculo

Para R=(3,4,0) e o eixo x, escolha P=(0,0,0), v=(1,0,0). t*=3, H=(3,0,0), resíduo (0,4,0) e distância 4. Não confunda ||w||=5, distância até P, com a distância até a reta: o ponto mais próximo não precisa ser o ponto de apoio escolhido.



## Projetar em uma reta não é projetar em qualquer segmento

O parâmetro minimizador da reta pode cair fora do segmento P+t v, 0≤t≤1. No segmento, se t*<0 use a extremidade inicial; se t*>1 use a final. Por exemplo, a projeção de (3,4,0) no eixo x ocorre em x=3, mas no segmento de x=0 até x=1 o ponto mais próximo é (1,0,0). A fórmula da reta precisa ser adaptada ao domínio restrito.



## Normais nulas e tolerâncias não podem ser escondidas

O vetor normal zero não define um plano; direção zero não define uma reta. Ambos são rejeitados. Com dados de medição ou aritmética aproximada, um vetor quase nulo exige escala e tolerância justificadas. Os experimentos usam dados pequenos e racionalidade exata; não implementam tratamento geral de dados ruidosos ou numericamente mal condicionados.



## A demonstração é uma seção plana de um caso em ℝ³

A interface usa o plano x−y=0 e pontos R=(x,y,0). O pé fica H=((x+y)/2,(x+y)/2,0), de modo que ponto, pé e normal podem ser vistos na seção z=0. O desenho usa a mesma escala nos eixos x,y. Mudar o fator ou orientação da equação não altera o pé; a tabela e os valores distinguem resíduo, distância assinada e distância sem sinal.



## Exemplo resolvido

Projete R=(1,1,1) no plano x+y+z=1 e confira a distância.

n=(1,1,1), d=1. O resíduo é 3−1=2 e n·n=3.

H=R−(2/3)n=(1/3,1/3,1/3).

Conferência: a soma das coordenadas de H é 1.

R−H=(2/3,2/3,2/3) é paralelo a n.

A distância ao quadrado é 3×(2/3)²=4/3, portanto a distância é 2/√3.

Com a equação 3x+3y+3z=3, resíduo 6 e norma 3√3 dão a mesma distância.

## Exercícios e resoluções

### Qual o quadrado da distância de (1,1,1) ao plano x+y+z=1?

e²/(n·n)=4/3.

### Qual a coordenada x do pé no exemplo resolvido?

1−2/3=1/3.

### Qual a distância de (3,4,0) ao eixo x?

O pé é (3,0,0) e o resíduo tem norma 4.

### Qual a distância de (3,0,0) ao plano x=0?

|3|/1=3.

### Qual o parâmetro do pé de (3,4,0) na reta (t,0,0)?

O parâmetro ótimo é 3.

### Multiplicar toda a equação do plano por 3 triplica a distância geométrica?

Resíduo e norma escalam juntos; a razão não muda.

### Inverter a normal pode trocar o sinal da distância assinada?

A orientação muda, mas a distância sem sinal não.

### O pé na reta pertence necessariamente a um segmento restrito dessa reta?

O parâmetro ótimo pode estar fora de [0;1].

### A fórmula do pé usa n·n no denominador?

Sim; a distância, por sua vez, divide pela norma de n.

## Preparação de aula

Mostre o problema do resíduo sob reescala; construa o pé na normal; confira pertencimento; prove o mínimo por Pitágoras; compare projeção em reta e segmento; encerre com a mesma equação multiplicada por um fator negativo.

## Pendências

Ângulos, distâncias entre retas, interseção entre planos e mais problemas aplicados. Não é cobertura integral nem certificação de domínio pessoal.
