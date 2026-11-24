# Eliminação e sistemas lineares — notas

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Não são notas importadas do Samsung Notes.

## Restrições simultâneas e matriz ampliada

Pré-requisitos: equações, vetores e aritmética de frações. O sistema x+y=3 e x−y=1 pede um mesmo par que satisfaça as duas restrições. Na matriz ampliada [A|b], cada linha representa uma equação: coeficientes à esquerda, termo independente à direita. Uma operação numa equação precisa alterar também seu termo independente. A linha da matriz não é um vetor solução; ela registra uma restrição sobre as incógnitas.

`[A|b]=[[1,1,3],[1,−1,1]]`

## Três operações, todas reversíveis

Podemos trocar duas linhas, multiplicar uma linha por um escalar não nulo e somar a uma linha um múltiplo de outra. Cada operação tem inversa: trocar novamente, multiplicar pelo recíproco e subtrair o mesmo múltiplo. Se um vetor satisfaz as equações originais, satisfaz as transformadas; aplicando a inversa, vale também a volta. É essa equivalência que preserva o conjunto solução. Multiplicar uma linha por zero pode apagar uma restrição e não é permitido.

`L_i↔L_j; L_i←λL_i (λ≠0); L_i←L_i+λL_j (i≠j)`

## Exemplo de eliminação com solução única

Subtraia a primeira linha da segunda no sistema inicial. Obtemos x+y=3 e −2y=−2. A segunda equação dá y=1; substituindo na primeira, x=2. Se normalizarmos a segunda linha por −1/2 e eliminarmos y na primeira, chegamos à forma reduzida que registra x=2 e y=1. Confira ambas as equações originais: 2+1=3 e 2−1=1. A conferência não substitui a equivalência das operações, mas detecta erros de conta.

`[[1,1,3],[1,−1,1]] → [[1,1,3],[0,−2,−2]] → [[1,0,2],[0,1,1]]`

## Pivô zero não autoriza divisão

Um pivô é uma entrada não nula usada para eliminar entradas na sua coluna. Se a posição escolhida contém zero, procure uma linha disponível abaixo com entrada não nula e troque as linhas. Se a coluna inteira restante for zero, não existe pivô ali: siga para outra coluna. Isso pode deixar uma variável livre, em vez de significar automaticamente que todo o sistema é impossível. No sistema y=1 e x+y=3, uma troca de linhas permite começar pelo pivô de x.

`pivô≠0; coluna sem pivô pode corresponder a variável livre`

## Forma escalonada e forma reduzida

Na forma escalonada, pivôs avançam para a direita ao descer linhas e as entradas abaixo de cada pivô são zero. Isso permite substituição de baixo para cima. Na forma escalonada reduzida, cada pivô é 1 e sua coluna tem zeros também acima: fica mais direto expressar as variáveis pivô em função das livres. O código prepara a forma reduzida com frações exatas e mantém uma lista de colunas pivô; não decide posto numérico por tolerância.

`escalonada: zeros abaixo; reduzida: pivô 1 e zeros na coluna`

## Uma linha redundante não é uma contradição

No sistema x+y=3, 2x+2y=6, subtrair duas vezes a primeira equação da segunda produz 0=0. Essa linha não acrescenta restrição. Escolha y=t livre e obtenha x=3−t. Há infinitos pares (3−t,t). Se o segundo termo independente fosse 7, a mesma operação produziria 0=1, que é impossível. Neste segundo caso não existem soluções, apesar de as linhas dos coeficientes serem as mesmas.

`b=(3,6): (x,y)=(3−t,t); b=(3,7): 0=1`

## Pivôs, posto e quantidade de soluções

O posto exato pode ser lido como número de pivôs da matriz de coeficientes. Se uma linha reduzida tem todos os coeficientes zero e termo independente não zero, o posto da ampliada é maior e o sistema é inconsistente. Quando os postos coincidem, uma variável para cada coluna sem pivô pode ser escolhida livremente. Com n incógnitas e posto n, a solução é única; com posto menor que n, há infinitas soluções no contexto real desta aula. Essas contagens não exigem que A seja quadrada.

`consistente ⇔ rank(A)=rank([A|b]); única ⇔ consistente e rank(A)=n`

## Solução particular mais direções livres

Num sistema consistente, escrevemos todas as soluções como x=x_p+z, onde Ax_p=b e Az=0. Para x+y=3, uma particular é (3,0) e a direção livre é (−1,1): x=(3,0)+t(−1,1). O conjunto solução é uma reta afim que, quando b≠0 neste exemplo, não passa pela origem. As direções livres formam o núcleo da transformação; a aula seguinte aprofunda essa ligação. Não confunda o vetor particular com uma base do núcleo.

`Ax_p=b; Az=0 ⇒ A(x_p+z)=b`

## Sistemas retangulares e exemplo com três incógnitas

Mais equações que incógnitas não garantem inconsistência: elas podem ser redundantes. Menos equações que incógnitas impedem solução única se o sistema for consistente, pois não pode haver pivô em todas as colunas. Para x+y=2 e y+z=3, escolha z=t: y=3−t e x=−1+t. As soluções são (−1,3,0)+t(1,−1,1). O código retorna a particular e uma base das direções livres, sem escolher um valor arbitrário para o parâmetro.

`(x,y,z)=(−1,3,0)+t(1,−1,1)`

## Exatidão algébrica e limites do cálculo

O experimento aceita int e Fraction para manter aritmética racional exata; rejeita floats e limita tamanho didático. Isso não significa que toda matriz observada no mundo tenha coeficientes exatos. Em dados aproximados, distinguir zero de quase zero exige escala, tolerância, condicionamento e análise de erro. Frações podem crescer bastante durante a eliminação, então esta implementação não é um solver de alto desempenho. A ponte para análise numérica aparece em Computação 3.

`coeficientes exatos ≠ dados aproximados sem erro`

## Roteiro para resolver e ensinar

Escreva [A|b]; indique cada operação de linha, incluindo b; escolha pivôs sem dividir por zero; identifique contradições ou redundâncias. Em caso consistente, separe variáveis pivô/livres, escreva a solução completa e confira Ax=b. Confira também Az=0 para cada direção livre. Para ensinar, explique a reversibilidade antes de apresentar a receita mecânica e relacione o resultado à interseção das restrições geométricas.

`representação → operações → pivôs → consistência → parametrização → conferência`

## Exercícios e resoluções

Tente antes de consultar; justifique operações e confira nas equações originais.

### 1. No sistema x+y=3 e x−y=1, qual x?

Resolução: Substituição após eliminar dá 2.

### 2. A linha 0=1 representa uma equação redundante?

- Sim

- Não

Resolução: É uma contradição.

### 3. Qual operação de linha pode apagar uma restrição e não é elementar reversível?

- Trocar duas linhas

- Multiplicar uma linha por zero

- Somar a uma linha um múltiplo de outra

Resolução: Multiplicar por zero não tem inversa e pode alterar o conjunto solução.

### 4. No sistema x+y=3, 2x+2y=6, escolhendo y=2, qual x?

Resolução: x=3−2=1; ambas as equações são satisfeitas.

### 5. A linha 0=0 na forma reduzida significa:

- Uma contradição

- Uma restrição redundante

- Solução única garantida

Resolução: A linha não acrescenta restrição; outras linhas e pivôs ainda precisam ser examinados.

### 6. Um sistema real consistente tem 4 incógnitas e posto 2. Quantas variáveis livres há?

Resolução: 4−2=2 variáveis livres.

### 7. Uma coluna restante sem pivô implica sempre que o sistema é inconsistente?

- Sim

- Não; pode indicar variável livre num sistema consistente

Resolução: Ausência de pivô numa coluna não é a mesma coisa que contradição.

### 8. Para x+y=2 e y+z=3, escolhendo z=1, qual x?

Resolução: y=2 e x=0.

### 9. Se Ax_p=b e Az=0, então A(x_p+z) é:

- b

- 0 sempre

- b+z

Resolução: A(x_p+z)=Ax_p+Az=b+0=b.

## Executar

Salve experiment.py e rode `python3 experiment.py`. Com test_experiment.py ao lado, execute `python3 -m unittest discover -p 'test_*.py'`. Não grava arquivos. solve(A,b) retorna status, forma reduzida, pivôs/livres, postos, particular (None se inconsistente) e base do núcleo. Retorna a base do núcleo também no caso inconsistente; isso não cria uma solução de Ax=b.

## Verificação e revisão

Quatro testes verificam casos únicos/livres/inconsistentes, 729 sistemas 2×2 versus menores independentes, resíduos exatos, troca de linhas, frações, matrizes retangulares e preservação das entradas. Explique operações e resolva um caso inédito sem consultar a referência. As outras aulas e a revisão pessoal do curso continuam pendentes.
