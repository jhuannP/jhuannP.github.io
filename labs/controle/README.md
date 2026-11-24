# Decisões, repetições e o estado de um programa

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Referência temática de Computer Science (2016), com exemplos próprios em Python.

## O programa muda de estado, uma instrução por vez

O estado registra os valores associados aos nomes naquele momento. Em soma+=i, lemos os valores atuais, calculamos soma+i e associamos o resultado novamente a soma. A ordem importa: inicializar soma dentro do laço apagaria o acumulado a cada passo. Antes de executar, escreva uma tabela com i, soma antes e soma depois; compare sua previsão com a saída.

`estado anterior → instrução → estado posterior`

## Condição e ordem dos ramos

if/elif/else testa condições na ordem escrita e executa somente o primeiro ramo verdadeiro, ou o else se nenhum for verdadeiro. Vários if independentes podem executar vários blocos, por isso não são sempre equivalentes a elif. Use == para comparar igualdade e = para atribuir. Em Python, a indentação define qual instrução pertence a cada bloco; não depende apenas da posição visual aproximada.

`if → elif → else: primeiro ramo satisfeito`

## Prever fronteiras antes de testar

Classificar uma temperatura exige decidir como tratar o valor zero. O exemplo usa negativa para valor<0, zero para valor==0 e positiva no restante. Teste um valor de cada ramo e exatamente a fronteira, como −1,0,1. Uma condição muito ampla no primeiro ramo pode impedir que um ramo posterior seja alcançado. Não confunda um resultado inesperado com falha do interpretador antes de ler a ordem das condições.

`casos: abaixo da fronteira, na fronteira, acima da fronteira`

## range exclui a fronteira final

range(início,fim,passo) produz inteiros sem incluir fim. range(2,7) produz 2,3,4,5,6. range(5,0,−2) produz 5,3,1. O passo precisa ser não nulo; sua direção deve permitir avançar até a fronteira. range(1,1) é vazio. Para somar de 1 até n inclusive, use range(1,n+1). Uma sequência vazia pode ser um caso correto, como n=0; não invente uma iteração que não existe.

`range(1,n+1): 1,2,…,n`

## Traçar uma soma pequena

Comece com soma=0. Para i=1, a soma vira 1; para i=2, vira 3; para i=3, vira 6. O valor anterior da soma carrega o trabalho já feito. Inicializar soma antes do laço permite acumular; inicializá-la novamente a cada iteração faria o resultado final depender apenas do último i. O traçado da demonstração mostra um prefixo das iterações, distinguindo soma parcial de resultado final.

`(i, antes, depois): (1,0,1),(2,1,3),(3,3,6)`

## Justificar o invariante

Antes da iteração i, soma contém 1+2+…+(i−1). Inicialização: antes de i=1, a soma vazia é 0. Preservação: somar i produz 1+…+i, que será a hipótese da próxima iteração. Ao terminar após n, soma contém 1+…+n. Essa frase é um invariante: descreve o que permanece verdadeiro em cada etapa. Conferir algumas saídas ajuda, mas não demonstra a propriedade para todos os n.

`depois de i: soma=i(i+1)/2`

## while: reavaliar e progredir

Uma versão equivalente usa contador=1 e repete enquanto contador≤n: soma contador e depois incrementa contador. A condição é testada antes de cada corpo; para n=0, o corpo não executa. Neste exemplo, n+1−contador diminui uma unidade a cada iteração até a condição ficar falsa. Se esquecer o incremento, o laço pode não terminar. Não execute um exemplo sabidamente infinito só para confirmar esse erro: explique-o pelo estado que não progride.

`contador aumenta; n+1−contador diminui`

## continue e break alteram caminhos específicos

continue pula o restante da iteração atual e segue para a próxima. break encerra o laço mais interno. No exemplo com i de 1 a 5, ignorar i=3 com continue e parar antes de somar i=5 com break produz 1+2+4=7. Em while, colocar continue antes da atualização que garante progresso pode causar repetição sem término. Um salto também precisa ser analisado em relação ao invariante.

`continue: próxima iteração; break: sair do laço`

## Contrato, limites e revisão

A soma trabalhada pressupõe n inteiro não negativo. O arquivo didático limita n até 1000 e rejeita booleanos, pois em Python bool é um subtipo de int, embora True não represente a contagem pretendida. O limite é da implementação, não da identidade matemática. O primeiro trecho do arquivo usa laços no nível principal; os exemplos reutilizáveis seguintes usam funções, tema da próxima aula. As verificações assert conferem exemplos; validação de entrada é feita com ValueError.

`entrada válida + invariante + término → resultado justificado`

## Roteiro para ensinar e depurar

Preveja a saída em um caso pequeno; trace estado e ramos; confira zero, fronteiras e sequência vazia. Identifique onde cada variável é inicializada e atualizada. Para laços, escreva o invariante e explique o progresso para o término. Se o resultado estiver errado, encontre o primeiro passo que difere da previsão, em vez de alterar várias linhas sem hipótese. Só então amplie o caso e compare com uma referência conhecida.

`previsão → traçado → primeira divergência → correção → conferência`

## Exercícios e resoluções

Preveja o resultado antes de consultar ou executar.

### 1. Quantas iterações existem em range(2,7)?

Resolução: São 2,3,4,5,6: cinco iterações.

### 2. Qual é a soma de 1 até 4 produzida pelo acumulador?

Resolução: 1+2+3+4=10.

### 3. Um while cujo estado nunca faz a condição se tornar falsa pode:

- Sempre terminar depois de dez passos

- Não terminar

- Ser equivalente a print

Resolução: O laço precisa de progresso para uma condição de parada.

### 4. Quantos valores há em range(5,0,−2)?

Resolução: 5,3,1: três valores.

### 5. Qual soma de 1 até n quando n=0 e o acumulador começa em zero?

Resolução: Nenhuma atualização; o acumulador permanece 0.

### 6. Se soma=0 é executado dentro de cada iteração antes de soma+=i, o acumulador:

- Mantém a soma de todas as iterações

- É reiniciado e perde as parcelas anteriores

- Sempre gera erro de sintaxe

Resolução: Reiniciar dentro do laço apaga o acumulado.

### 7. Somando i=1..5, pulando 3 com continue e saindo com break antes de somar 5, qual total?

Resolução: 1+2+4=7.

### 8. Após i iterações da soma de 1 até n, qual invariante é correto?

- soma=1+…+i

- soma sempre igual a n

- soma sempre zero

Resolução: Depois da iteração i, todas as parcelas de 1 a i foram acumuladas.

### 9. Trocar uma sequência if/elif por vários if independentes sempre preserva o comportamento?

- Sim

- Não; mais de um if pode executar

Resolução: Os contratos de seleção diferem quando várias condições são verdadeiras.

## Executar

Salve example.py e rode `python3 example.py` no seu ambiente Python. Só biblioteca padrão, sem leitura interativa nem escrita de arquivos. As verificações estão no próprio arquivo e os contratos têm limites didáticos explícitos.

## Revisão pessoal

Explique um exemplo sem ler, preveja um caso novo e compare o primeiro passo que divergir. As outras aulas e a revisão pessoal de Computação 1 continuam em preparação.
