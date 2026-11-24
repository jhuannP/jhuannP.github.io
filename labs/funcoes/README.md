# Funções para decompor um problema

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Referência temática de Computer Science (2016), com exemplos próprios em Python.

## Uma tarefa com entrada e resultado

Uma função nomeia uma operação e permite executá-la com entradas diferentes. Definir def cria a função; o corpo executa quando ela é chamada. Parâmetros são os nomes na definição; argumentos são os valores fornecidos na chamada. Em energia_cinetica(massa_kg,velocidade_m_s), as unidades nos nomes ajudam a declarar o contrato. Isso facilita revisar um cálculo sem misturá-lo com leitura do teclado ou impressão.

`definição → chamada com argumentos → execução → retorno`

## return devolve; print apresenta

return entrega um valor ao chamador e encerra aquela execução da função. print escreve uma representação na saída; seu efeito visível não substitui um retorno. Uma função que chega ao fim sem return explícito devolve None. Portanto resultado=mostrar_energia(2,3) pode imprimir 9,0 e ainda deixar resultado igual a None. Para compor cálculos, use o valor retornado por uma função de cálculo e deixe a apresentação no cliente.

`return → valor; fim sem return → None`

## Contrato antes da fórmula

Declare quais entradas fazem sentido, o significado do resultado e como erros são comunicados. A energia cinética usa massa positiva e velocidade em m/s; velocidade negativa em uma dimensão deve produzir a mesma energia que sua oposta, pois aparece ao quadrado. O código limita massa e módulo da velocidade até 10⁶ em suas unidades para o exemplo; isso é uma faixa da implementação, não da lei física. Valores fora do contrato geram ValueError, incluindo NaN e booleanos.

`entrada válida → resultado definido; entrada inválida → erro explícito`

## Exemplo físico e propriedades de conferência

A função devolve E=mv²/2 em joules. Para m=2 kg e v=3 m/s, E=9 J. Para v=0, E=0; para v=−3, continua 9 J. Dobrar a massa com velocidade fixa dobra a energia; dobrar a rapidez com massa fixa multiplica por quatro. Essas propriedades ajudam a escolher verificações que detectam erros de expoente ou unidade, além de um único número. Não demonstram, sozinhas, que qualquer implementação esteja correta.

`E(m,−v)=E(m,v); E(m,2v)=4E(m,v)`

## Nomes locais não alteram automaticamente nomes externos

O parâmetro valor em dobrar(valor) é um nome local da chamada. Se o cliente tem valor=10 e chama dobrar(3), o retorno é 6 e o nome valor no cliente continua associado a 10. Reatribuir um parâmetro cria outra associação local; não reatribui automaticamente o nome usado pelo chamador. Evite depender de variáveis globais para um cálculo que pode receber tudo de que precisa como argumentos.

`parâmetro local ≠ nome do cliente`

## Objetos mutáveis podem ser compartilhados

Um parâmetro pode referir-se ao mesmo objeto que o cliente. Se a função acrescenta um item a uma lista recebida, o cliente vê a alteração nesse objeto. Isso é diferente de fazer lista=[9] dentro da função: essa atribuição troca só o nome local, preservando o objeto anterior do cliente. Não diga que todo argumento foi copiado; diferencie alteração do objeto e alteração da associação do nome. Se houver mutação, registre-a no contrato.

`reatribuição do nome local ≠ mutação do objeto`

## Valores padrão e listas novas

Argumentos padrão são avaliados quando a definição é executada, não a cada chamada. Usar uma lista mutável como padrão pode compartilhar estado entre chamadas inesperadamente. No exemplo criar_lista, o padrão é None; dentro de cada chamada sem lista fornecida, criamos uma lista nova. Chamadas criar_lista("A") e criar_lista("B") produzem listas separadas. Se uma lista for fornecida explicitamente, o contrato do exemplo permite modificá-la.

`padrão None → criar objeto novo na chamada, quando necessário`

## Uma função de cálculo pode ser composta

Se energia_cinetica retorna um número, podemos guardar, comparar, converter unidade ou usá-lo em outro cálculo. Se apenas imprime, esses usos não recebem o número automaticamente. Composição não exige funções enormes: uma função calcula, outra escolhe apresentação, outra verifica contrato de uma tarefa maior. Escolha responsabilidades que tenham nomes claros e possam ser explicadas sem acompanhar todos os detalhes do programa.

`entrada → cálculo → valor retornado → próximo cálculo ou apresentação`

## Verificações e erros têm papéis distintos

Os assert do arquivo são conferências dos exemplos, como energia_cinetica(2,3)==9 e retorno None de uma função que só imprime. A validação do contrato usa condições e ValueError. Não confunda imprimir uma mensagem de erro com comunicar falha ao chamador; também não transforme todo erro em um resultado numérico aparentemente válido. O arquivo inclui casos de zero, sinal, entradas inválidas, escopo e mutação.

`conferência de exemplo ≠ contrato de entrada`

## Roteiro para escrever e ensinar

Descreva entrada, saída e efeitos permitidos em uma frase. Escreva a função de cálculo sem leitura/impressão desnecessária, escolha um caso conhecido e uma propriedade, depois faça um cliente que apresenta o resultado. Explique parâmetros e argumentos numa chamada concreta. Para listas, desenhe nomes apontando para objetos e diga se a função muda o objeto. Na revisão, busque dependência oculta de globais, ausência de return e estado compartilhado inesperado.

`contrato → função → casos de conferência → cliente → revisão`

## Exercícios e resoluções

Preveja o resultado antes de consultar ou executar.

### 1. Qual energia cinética a função retorna para massa=4 e velocidade=2?

Resolução: E=0.5×4×2²=8.

### 2. Uma função sem return explícito devolve:

- O último número calculado

- None

- Sempre zero

Resolução: Python devolve None quando a função termina sem devolver um valor explícito.

### 3. Qual energia em J para massa=2 kg e velocidade=−3 m/s?

Resolução: 0,5×2×(−3)²=9 J.

### 4. resultado=mostrar_energia(2,3), sendo mostrar_energia uma função que só chama print e não tem return, deixa resultado como:

- 9 automaticamente

- None

- A string energia

Resolução: A função chega ao fim sem retorno explícito e devolve None.

### 5. Se valor=10 no cliente, qual seu valor após chamar dobrar(3), cuja função apenas retorna 2×seu parâmetro local?

Resolução: O nome do cliente não foi alterado; permanece 10.

### 6. Fazer lista=[9] dentro de uma função que recebeu uma lista sempre troca o nome do cliente para essa nova lista?

- Sim

- Não; reatribui o nome local

Resolução: O cliente continua referindo-se ao objeto original, salvo uma atribuição feita pelo próprio cliente.

### 7. Uma função recebe a lista [1,2] e executa append(3) no mesmo objeto. Qual o tamanho visto pelo cliente?

Resolução: O objeto compartilhado vira [1,2,3], tamanho 3.

### 8. Um argumento padrão como lista=[] é avaliado:

- Toda vez que a função é chamada

- Quando a definição é executada

Resolução: O objeto padrão é criado na definição e pode ser reutilizado em várias chamadas.

### 9. Com massa fixa, dobrar a rapidez multiplica a energia cinética por qual fator?

Resolução: (2v)²=4v²; fator 4.

## Executar

Salve example.py e rode `python3 example.py` no seu ambiente Python. Só biblioteca padrão, sem leitura interativa nem escrita de arquivos. As verificações estão no próprio arquivo e os contratos têm limites didáticos explícitos.

## Revisão pessoal

Explique um exemplo sem ler, preveja um caso novo e compare o primeiro passo que divergir. As outras aulas e a revisão pessoal de Computação 1 continuam em preparação.
