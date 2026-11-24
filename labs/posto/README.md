# Posto e consistência — notas

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Notas pessoais não foram importadas.

## A matriz transforma combinações em saídas

Pré-requisitos: combinações lineares, independência e eliminação. Se A tem m linhas e n colunas, Ax é uma combinação das n colunas de A com coeficientes dados por x. Sua imagem é o espaço gerado por essas colunas. O posto é a dimensão desse espaço: quantas direções independentes são necessárias para representar todas as saídas possíveis. Não é o número de entradas não nulas nem o número de linhas que parecem diferentes.

`Im(A)=span(colunas de A); rank(A)=dim Im(A)`

## Por que o posto não excede linhas nem colunas

A imagem é um subespaço de R^m, então sua dimensão não excede m. Ela é gerada por n colunas, então não excede n. Por isso 0≤rank(A)≤min(m,n). A matriz zero tem posto zero. Em matrizes retangulares, “posto completo” precisa indicar se falamos do máximo possível min(m,n), de colunas independentes ou de gerar todo R^m: essas propriedades nem sempre coincidem.

`0≤rank(A)≤min(m,n)`

## Operações de linhas preservam relações entre colunas

Uma sequência de operações elementares pode ser escrita como multiplicação à esquerda por uma matriz invertível E. A relação Av=0 equivale a EAv=0, pois podemos multiplicar de volta por E⁻¹. Assim as dependências entre colunas são preservadas, e a dimensão de sua imagem permanece. As colunas transformadas podem ser vetores diferentes: operações de linhas não preservam literalmente o espaço das colunas original, mas preservam seu posto e suas relações lineares.

`Av=0 ⇔ (EA)v=0, com E invertível`

## Por que contar pivôs funciona no caso exato

Na forma reduzida, as colunas pivô têm uma entrada 1 em linhas distintas e zeros nas outras posições; são independentes. Cada coluna sem pivô é combinação dessas colunas usando seus coeficientes nas linhas pivô. Como a eliminação preserva as relações entre colunas, as colunas nas mesmas posições da matriz original também formam uma base de sua imagem. O posto é o número de pivôs. As linhas não nulas da forma reduzida também são independentes e geram o espaço das linhas, justificando a igualdade entre posto por linhas e por colunas.

`rank(A)=número de pivôs exatos`

## Consistência: a saída pedida precisa estar na imagem

Resolver Ax=b pergunta se b pode ser escrito como combinação das colunas de A. A matriz ampliada [A|b] acrescenta b ao conjunto gerador. Se b já está na imagem, a dimensão não muda; se está fora, cresce uma unidade. Isso prova o critério rank(A)=rank([A|b]) para existência de solução. Acrescentar uma só coluna pode aumentar o posto no máximo em um; não produz uma dimensão arbitrariamente maior.

`Ax=b tem solução ⇔ b∈Im(A) ⇔ rank(A)=rank([A|b])`

## Um mesmo A, dois termos independentes

Para A=[[1,1],[2,2]], as duas colunas são iguais a (1,2). A imagem é uma reta e o posto 1. b=(3,6) pertence à reta, pois é 3(1,2); a ampliada continua com posto 1. Já b=(3,7) não pertence: sua primeira coordenada exigiria coeficiente 3, cuja segunda coordenada seria 6. A ampliada tem posto 2 e o sistema é inconsistente. Na eliminação, a diferença aparece como 0=0 ou 0=1.

`A=[[1,1],[2,2]]; b=(3,6) consistente; b=(3,7) inconsistente`

## Existência e unicidade são perguntas diferentes

Se o sistema é consistente e tem n incógnitas, r pivôs deixam n−r variáveis livres. Ele tem solução única quando r=n; tem infinitas soluções reais quando r<n. Para m<n, posto completo de linhas r=m não garante unicidade, pois ainda sobram n−m variáveis livres. Para m>n e colunas independentes, r=n: pode haver solução única para b dentro da imagem, mas nem todo b de R^m será alcançado.

`consistente: número de variáveis livres=n−rank(A)`

## Exemplo retangular e o papel do núcleo

A=[[1,1,0],[0,1,1]] tem dois pivôs e três colunas, então posto 2 e uma variável livre. Para b=(2,3), uma particular é (−1,3,0), e a direção (1,−1,1) está no núcleo. Todas as soluções são (−1,3,0)+t(1,−1,1). A imagem é todo R², pois há dois pivôs para duas linhas, mas as entradas x não são identificadas unicamente: uma direção da entrada não altera a saída.

`rank(A)=2; dim Ker(A)=3−2=1`

## Um pivô muito pequeno ainda pode ser não nulo exato

Considere A_ε=[[1,1],[1,1+ε]]. Seu determinante é ε. Se ε≠0 exato, o posto é 2; se ε=0, é 1. Com ε=1/10²⁰, a aritmética racional mantém a diferença. Nesta representação usual de float do Python, 1,0+float(ε) pode arredondar para 1,0, apagando a informação antes mesmo de eliminar. Por isso converter dados exatos para float e contar zeros pode responder uma pergunta diferente da original.

`ε≠0 ⇒ rank(A_ε)=2; ε=0 ⇒ rank(A_ε)=1`

## Posto completo não garante baixa sensibilidade

Para A_εx=(2,2+δ), as equações dão y=δ/ε e x=2−δ/ε quando ε≠0. Uma mudança η no segundo termo independente muda y por η/ε. Se |ε| é pequeno, um erro pequeno pode produzir grande alteração na solução, embora o posto exato continue completo. Em problemas numéricos, posto aproximado e condicionamento precisam de escala, tolerâncias e conhecimento do erro dos dados; não se define um limiar universal nesta aula.

`Δy=η/ε`

## Ligação com dados e modelos

Em um modelo linear de dados, colunas repetidas podem representar duas entradas que produzem a mesma contribuição. As previsões dependem da soma de seus coeficientes, e não há identificação única de cada coeficiente sem informação adicional. Um sistema de dados inconsistente não significa que não possamos estudar um ajuste: mínimos quadrados responde outra pergunta, buscando reduzir resíduos. Não confunda solução exata de Ax=b com otimização de erro de um modelo.

`colunas dependentes ⇒ coeficientes podem não ser identificáveis`

## Roteiro para resolver e ensinar

Registre m e n, determine pivôs no contexto exato e compare A com [A|b]. Primeiro responda se existe solução; depois, se é única e quantas direções livres há. Confira uma particular com Ax=b e direções do núcleo com Az=0. Se os dados forem aproximados, não transfira um argumento exato sem discutir precisão. Para ensinar, mostre b dentro e fora da imagem e explique por que o posto conta direções, não uma quantidade de números diferentes.

`dimensões → pivôs → imagem → consistência → unicidade → precisão`

## Exercícios e resoluções

Tente antes de consultar; diferencie existência, unicidade e sensibilidade.

### 1. Qual o posto exato de A=[[1,1],[2,2]]?

Resolução: Há uma direção independente.

### 2. O sistema com b=(3,7) é consistente?

- Sim

- Não

Resolução: A segunda equação exigiria 6, não 7.

### 3. Para A=[[1,1],[2,2]] e b=(3,7), qual o posto da ampliada [A|b]?

Resolução: A nova coluna é independente da direção original, elevando o posto de 1 para 2.

### 4. Uma matriz 2×5 pode ter posto no máximo igual a quanto?

Resolução: min(2,5)=2.

### 5. Um sistema real consistente com 5 incógnitas e posto 3 tem quantas variáveis livres?

Resolução: 5−3=2.

### 6. Adicionar uma só coluna b pode aumentar o posto de A em:

- No máximo 1

- Sempre 2

- Uma quantidade sem limite

Resolução: Se b já pertence ao espaço gerado, não aumenta; se está fora, aumenta uma unidade.

### 7. Uma matriz 2×3 de posto 2 garante solução única para todo b?

- Sim

- Não: o sistema é consistente para todo b de R², mas há uma variável livre

Resolução: A imagem é R², mas n−r=1, portanto falta unicidade.

### 8. Um sistema quadrado de posto completo exato pode ser muito sensível a pequenas perturbações?

- Não

- Sim

Resolução: A solução y=δ/ε amplifica perturbações; posto completo não assegura bom condicionamento.

### 9. Operações invertíveis de linhas preservam literalmente o espaço original das colunas?

- Sim, todos os vetores coluna ficam iguais

- Não; preservam relações lineares e posto, mas podem mudar os vetores coluna

Resolução: EA pode ter outra imagem como conjunto de vetores, porém a dimensão e as dependências entre colunas são preservadas.

## Experimento de apoio

O código disponível é o eliminador exato da aula anterior; solve(A,b) permite conferir postos e soluções. Copie os A e b indicados nos exemplos. O exemplo de ε requer Fraction(1,10**20), pois floats são rejeitados pelo solver. As verificações de 729 sistemas e resíduos pertencem ao laboratório de eliminação; não constituem validação de um algoritmo de posto aproximado.

## Revisão pessoal

Justifique o critério por espaço das colunas, explique por que contar pivôs funciona e dê um exemplo de posto completo com sensibilidade alta. As outras aulas e a revisão do curso continuam pendentes.
