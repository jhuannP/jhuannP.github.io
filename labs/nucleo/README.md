# Núcleo: encontrar direções invisíveis à transformação

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Notas pessoais não foram importadas.

## O núcleo responde uma pergunta sobre entradas

Para A com m linhas e n colunas, o núcleo é o conjunto dos vetores x de R^n que produzem a saída zero em R^m. Ele pertence ao domínio, não ao espaço de saída. O vetor zero sempre está no núcleo. Uma entrada não nula no núcleo é uma direção que a transformação não distingue da entrada zero. “Direção invisível” é uma interpretação, não ausência do vetor.

`Ker(A)={x∈R^n:Ax=0}`

## Por que é um subespaço

A0=0. Se Au=0 e Av=0, então A(αu+βv)=αAu+βAv=0 para quaisquer escalares reais. Portanto o núcleo contém zero e é fechado por combinações lineares. A prova usa linearidade; o conjunto de entradas que uma função não linear envia a zero não precisa ser um subespaço. A imagem e o núcleo respondem perguntas diferentes sobre a mesma matriz.

`Au=Av=0 ⇒ A(αu+βv)=0`

## Exemplo: descrever a reta inteira

Para A=[[1,1],[2,2]], Ax=0 reduz-se à equação x+y=0. Escolha x=t e y=−t: todos os vetores são t(1,−1). O vetor (1,−1) sozinho não é o núcleo; ele é uma base que gera o núcleo por todos os múltiplos. O código pode escolher (−1,1), que gera a mesma reta, com orientação oposta. Encontrar um vetor e verificar Av=0 não prova sozinho que todos os vetores do núcleo foram descritos.

`Ker(A)=span((1,−1))`

## Entradas distintas podem ter a mesma saída

Se z está no núcleo, A(u+z)=Au+Az=Au. No exemplo, u=(3,2) e u+(1,−1)=(4,1) produzem (5,10). A demonstração varia t sem alterar a saída. Mais geralmente, Au=Av equivale a u−v estar no núcleo. Assim o núcleo descreve exatamente as diferenças entre entradas indistinguíveis pela transformação.

`Au=Av ⇔ u−v∈Ker(A)`

## Injetividade e núcleo trivial

Uma transformação é injetiva quando saídas iguais implicam entradas iguais. Se o núcleo contém só zero, Au=Av implica A(u−v)=0 e u−v=0. Reciprocamente, se z não nulo está no núcleo, Az=A0 com z≠0, então a transformação não é injetiva. Não confunda núcleo trivial com núcleo vazio: zero sempre está nele.

`A injetiva ⇔ Ker(A)={0}`

## Soluções não homogêneas são uma translação do núcleo

Se Ax_p=b, então todo x_p+z com Az=0 é solução. Se Ax=b também, A(x−x_p)=0, logo toda solução tem essa forma. Portanto, quando existe solução, o conjunto é x_p+Ker(A). Para b≠0 ele normalmente não contém a origem e não é um subespaço; é um conjunto afim. Se o sistema é inconsistente, não há particular nem conjunto de soluções, embora o núcleo ainda exista.

`soluções de Ax=b: x_p+Ker(A), quando existe x_p`

## Posto–nulidade: contar as direções do domínio

Se A tem n colunas, o teorema afirma rank(A)+dim Ker(A)=n. Na eliminação, r colunas pivô deixam n−r variáveis livres. Cada parâmetro livre produz uma direção do núcleo, e elas formam uma base: são independentes porque cada uma tem um parâmetro livre diferente igual a 1, e geram todos os vetores da solução homogênea. A nulidade usa n, dimensão do domínio, não m, número de linhas.

`rank(A)+dim Ker(A)=n`

## Outra justificativa pela extensão de uma base

Escolha uma base v₁,…,v_k do núcleo e estenda-a a uma base do domínio com w₁,…,w_r. As imagens Aw_i geram a imagem de A: toda entrada é combinação de v e w, e as parcelas v desaparecem. Elas também são independentes: se uma combinação de Aw_i é zero, a correspondente combinação de w_i pertence ao núcleo, o que forçaria uma dependência na base completa, salvo se todos os coeficientes fossem zero. Logo rank(A)=r e n=k+r. Este argumento usa o fato de que uma família independente pode ser estendida a uma base em dimensão finita.

`base do domínio: k vetores do núcleo + r complementares; n=k+r`

## Matriz retangular e consequências

Para A=[[1,1,0],[0,1,1]], o posto é 2 e o domínio R³, então a nulidade é 1. Resolver Ax=0 dá t(1,−1,1). Para uma matriz m×n com n>m, rank≤m<n, portanto a nulidade é positiva e não pode haver injetividade. Uma transformação pode gerar todo o espaço de saída e ainda perder informação da entrada.

`n>m ⇒ dim Ker(A)≥n−m>0`

## Roteiro para estudar e ensinar

Identifique domínio e saída; resolva o sistema homogêneo com eliminação; separe variáveis livres e escreva a parametrização completa. Verifique Az=0 para as direções encontradas e explique por que são independentes e geram todas as soluções. Use posto–nulidade como conferência de dimensão. Para ensinar, varie a entrada ao longo do núcleo e mostre que a saída fica fixa, sem usar o desenho como substituto da identidade algébrica.

`Ax=0 → parâmetros livres → base → nulidade → injetividade`

## Exercícios e resoluções

Tente antes de consultar; declare os espaços e confira as identidades.

### 1. Para A=[[1,1],[2,2]], qual a dimensão do núcleo?

Resolução: Um parâmetro livre.

### 2. A nulidade deve ser calculada como número de linhas menos posto?

- Sim

- Não

Resolução: O teorema usa a dimensão do domínio: número de colunas.

### 3. O núcleo de uma matriz 2×3 pertence a:

- R²

- R³

- Ao conjunto de linhas da matriz

Resolução: Ax usa x∈R³; a saída pertence a R².

### 4. Uma matriz com 5 colunas e posto 3 tem qual nulidade?

Resolução: 5−3=2.

### 5. Núcleo trivial significa:

- Conjunto vazio

- Somente o vetor zero

- Somente vetores não nulos

Resolução: Ker(A)={0}, não o conjunto vazio.

### 6. Se Az=0 e z≠0, a transformação é injetiva?

- Sim

- Não

Resolução: Duas entradas distintas têm a mesma saída zero.

### 7. No exemplo, A(3,2)=(5,10). Qual a primeira coordenada de A(4,1)?

Resolução: 4+1=5; as imagens são iguais.

### 8. Se Ax=b é inconsistente, o núcleo de A deixa de existir?

- Sim

- Não: o sistema homogêneo Ax=0 continua tendo ao menos zero

Resolução: A inconsistência de Ax=b não elimina o conjunto Ker(A).

### 9. Verificar Av=0 para um único vetor não nulo basta para provar que ele gera todo o núcleo?

- Sim

- Não; ainda precisamos justificar geração e dimensão

Resolução: Isso só prova que v pertence ao núcleo; a parametrização/eliminação precisa mostrar o espaço completo.

## Experimento de apoio

O código da página inclui o eliminador racional da aula de eliminação e conferências específicas desta aula. O arquivo de apoio para baixar é o solver geral; as notas indicam os dados dos exemplos. Biblioteca padrão, int/Fraction, sem execução remota.

## Revisão pessoal

Explique geração e independência, domínio e imagem, resolva um caso inédito e confira por reconstrução. Demonstrações/provas e experiência com aluno devem ser revisadas por Jhuann. Os demais conteúdos continuam em preparação.
