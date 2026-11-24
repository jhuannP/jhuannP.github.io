# Base e dimensão: gerar sem redundância

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Notas pessoais não foram importadas.

## Gerar e ser independente são exigências diferentes

Uma família gera um espaço quando todo vetor desse espaço é uma combinação linear dela. É independente quando a única combinação que produz zero tem todos os coeficientes zero. Uma base satisfaz as duas propriedades. Gerar sem independência deixa redundância; independência sem gerar deixa vetores fora do alcance. As propriedades são sempre relativas ao espaço que queremos representar.

`base = geração + independência`

## Por que as coordenadas são únicas

Se v tem duas representações numa família, v=Σα_i b_i=Σβ_i b_i, subtrair dá Σ(α_i−β_i)b_i=0. Independência força α_i=β_i para todos os índices. A geração garante existência e a independência garante unicidade. Uma família geradora dependente pode representar o mesmo vetor de maneiras diferentes, sem que o vetor tenha mudado.

`Σα_i b_i=Σβ_i b_i ⇒ α_i=β_i numa base`

## Duas bases do plano

A base padrão e₁=(1,0), e₂=(0,1) representa (3,2) com coordenadas (3,2). Outra base é b₁=(1,0), b₂=(1,1): temos (3,2)=1b₁+2b₂, então as coordenadas são (1,2). O vetor geométrico permanece igual. Colocar os vetores da base nas colunas de B permite escrever Bc=v; c são as coordenadas na base escolhida. Não confunda c com v quando B não é a identidade.

`v=(3,2)=1(1,0)+2(1,1)`

## Um conjunto que gera, mas não é base

A família e₁,e₂,w=(1,1) gera R², mas w=e₁+e₂. A relação e₁+e₂−w=0 tem coeficientes não todos nulos, portanto a família é dependente. Podemos retirar w sem perder geração. O vetor zero também torna qualquer família que o contenha dependente, pois 1·0=0 é uma relação não trivial.

`e₁+e₂−w=0`

## Uma família independente pode gerar um subespaço menor

Os vetores (1,0,0) e (0,1,0) são independentes em R³, mas não geram todo R³. Eles formam uma base do plano z=0, de dimensão 2. Dimensão ambiente 3 e dimensão do subespaço 2 são coisas diferentes. Para que sejam base de R³ falta uma terceira direção fora desse plano, como (0,0,1).

`span((1,0,0),(0,1,0))={vetores com z=0}`

## Dimensão não depende da escolha da base

Em um espaço de dimensão finita, todas as bases têm a mesma quantidade de vetores. Esse resultado estrutural vem do princípio de troca: uma família independente não pode ter mais vetores que uma família geradora do mesmo espaço; aplicando-o às duas bases, as quantidades coincidem. A dimensão é esse número comum, não o comprimento de um vetor nem a quantidade de coordenadas de um vetor ambiente. Uma base não precisa ser ortogonal nem normalizada.

`duas bases do mesmo espaço têm a mesma cardinalidade`

## Como retirar redundância por eliminação

Coloque os vetores candidatos nas colunas de M e encontre as colunas pivô. Os vetores nas mesmas posições da matriz original formam uma base do espaço gerado. Use as colunas originais, não simplesmente as colunas da matriz após operações de linhas: essas operações podem mudar os vetores, embora preservem relações e posto. Para M=[[1,2,0],[2,4,1]], pivôs nas colunas 1 e 3 (numeração humana) escolhem (1,2) e (0,1); a segunda coluna é redundante.

`base da imagem: colunas pivô da matriz original`

## Completar uma família independente

Se uma família independente ainda não gera o espaço desejado, acrescente um vetor fora do espaço que ela gera. A família continua independente: se o coeficiente do novo vetor numa relação fosse não nulo, ele seria combinação dos anteriores, contradizendo a escolha. Em dimensão finita podemos repetir até obter uma base. Isso também justifica estender uma base do núcleo a uma base do domínio na demonstração de posto–nulidade.

`vetor fora do span anterior → independência preservada`

## O subespaço zero tem dimensão zero

O espaço {0} é gerado pela família vazia: a soma vazia é zero. Essa família é independente, pois não existem coeficientes que criem uma relação não trivial. Portanto a base do espaço zero é vazia e sua dimensão é 0. A família que contém um vetor zero não é uma base, embora também gere {0}. O conjunto de vetores do espaço não é a mesma coisa que sua base.

`base de {0}: família vazia; dim{0}=0`

## Bases do núcleo e da imagem pertencem a espaços distintos

Para A m×n, uma base do núcleo contém vetores em R^n; uma base da imagem contém vetores em R^m. Elas não são listas intercambiáveis. Se r é o posto, a base da imagem tem r vetores e a do núcleo tem n−r. Quando um sistema é consistente, a solução particular desloca o núcleo; ela não se torna automaticamente um vetor de sua base.

`dim Im(A)=r; dim Ker(A)=n−r`

## Roteiro para estudar e ensinar

Declare o espaço desejado e o ambiente. Confira geração e independência separadamente; use uma relação explícita para mostrar redundância ou pivôs para selecionar uma base. Resolva Bc=v para encontrar coordenadas e reconstrua o vetor. Explique qual espaço cada vetor representa antes de contar dimensão. Revisão e provas do princípio de troca/extensão podem ser aprofundadas na preparação pessoal.

`espaço → geração → independência → base → coordenadas`

## Exercícios e resoluções

Tente antes de consultar; declare os espaços e confira as identidades.

### 1. Qual a dimensão do plano z=0 gerado por (1,0,0) e (0,1,0)?

Resolução: Dois vetores independentes geram o plano.

### 2. Uma família redundante pode ser uma base?

- Sim

- Não

Resolução: Uma base deve ser independente.

### 3. Na base b₁=(1,0), b₂=(1,1), qual o primeiro coeficiente de v=(3,2)?

Resolução: v=1b₁+2b₂, então o primeiro coeficiente é 1.

### 4. Uma família independente sempre é base de todo o espaço ambiente?

- Sim

- Não; pode gerar somente um subespaço próprio

Resolução: É base de seu span, mas precisa gerar o espaço escolhido para ser base dele.

### 5. A família contendo apenas o vetor zero é base de {0}?

- Sim

- Não; é dependente, enquanto a base de {0} é vazia

Resolução: O espaço zero tem base vazia e dimensão zero.

### 6. Uma matriz 3×5 de posto 2 tem uma base do núcleo com quantos vetores?

Resolução: 5−2=3.

### 7. Para extrair uma base da imagem após eliminar linhas, devemos selecionar:

- As colunas pivô da matriz original

- Sempre todas as colunas reduzidas

- Qualquer coluna que não seja zero

Resolução: As posições pivô identificam colunas independentes na matriz original.

### 8. Uma base precisa ser ortonormal?

- Sim

- Não; independência e geração bastam

Resolução: Ortonormalidade é uma propriedade adicional útil, não exigência da definição.

### 9. Qual a dimensão do espaço {0}?

Resolução: A base é vazia; dimensão zero.

## Experimento de apoio

O código da página inclui o eliminador racional da aula de eliminação e conferências específicas desta aula. O arquivo de apoio para baixar é o solver geral; as notas indicam os dados dos exemplos. Biblioteca padrão, int/Fraction, sem execução remota.

## Revisão pessoal

Explique geração e independência, domínio e imagem, resolva um caso inédito e confira por reconstrução. Demonstrações/provas e experiência com aluno devem ser revisadas por Jhuann. Os demais conteúdos continuam em preparação.
