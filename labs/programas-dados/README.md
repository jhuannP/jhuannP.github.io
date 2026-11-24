# Programas como dados — linguagem afim e universalidade

## Uma descrição de programa pode ser entrada

O mesmo interpretador pode receber diferentes programas como dados. No exemplo original, a lista [("ADD",3),("MUL",2)] descreve operações sobre um acumulador. A lista não executa por existir na memória; um procedimento precisa lê-la e aplicar o significado de cada instrução. Essa separação permite armazenar, transmitir, inspecionar e transformar descrições de programas. Todos os exemplos desta aula são próprios e não representam um produto ou pesquisa já realizado por Jhuann.

## Sintaxe válida e significado são verificações diferentes

A linguagem baixável admite apenas pares (operação,constante inteira), com operação ADD, SUB ou MUL. ADD c soma c; SUB c subtrai c; MUL c multiplica pela constante c. Não há referência à variável original dentro do operando: MUL x não é uma instrução desta sintaxe. Uma descrição malformada ou operação desconhecida é recusada antes da execução. Uma descrição válida ainda precisa ter sua sequência interpretada para determinar a função calculada.

## Uma semântica explícita produz um traço verificável

Parta do acumulador x. A cada instrução, atualize o acumulador e avance na lista. Com x=0, ADD 3 seguido de MUL 2 produz o traço 0→3→6. Com x=4, o mesmo programa produz 4→7→14. A lista vazia preserva o acumulador, portanto calcula a identidade, não necessariamente a constante zero. O interpretador devolve o resultado e o traço; a função simples preservada do exemplo antigo devolve apenas o resultado.

P(0)=6; P(4)=14

## Serializar preserva uma descrição, não cria sua execução

O arquivo program.json contém a lista [["ADD",3],["MUL",2]]. encode gera uma representação JSON; decode lê a estrutura e valida seus pares. Para programas válidos, decode(encode(P)) devolve a mesma sequência normalizada. Só depois execute aplica a semântica. Alterar uma constante muda o programa; representar os mesmos pares com outra formatação de espaços não muda sua sequência. O laboratório não usa eval para dar significado ao texto.

## Um invariante permite interpretar simbolicamente

Após qualquer prefixo da lista, o acumulador tem forma a x+b, onde x é a entrada inicial. Antes da primeira instrução, a=1 e b=0. ADD c mantém a e troca b por b+c; SUB c troca b por b−c; MUL c troca ambos por ca e cb. Uma indução no comprimento do programa prova que essas atualizações preservam o significado para toda entrada inteira, não apenas para um conjunto de testes.

ADD c: (a,b)→(a,b+c); MUL c: (a,b)→(ca,cb)

## A classe calculada é exatamente a das funções afins inteiras

O invariante mostra que todo programa válido calcula a x+b, com a,b inteiros. No sentido inverso, qualquer par inteiro (a,b) pode ser implementado por MUL a seguido de ADD b. Portanto conhecemos toda a classe de funções desta linguagem sob a semântica declarada. Para ADD 3,MUL 2, compile_affine devolve (2,6), representando 2x+6. Essa simplificação evita repetir a lista para cada entrada, mas continua limitada à classe provada.

P(x)=ax+b, a,b∈ℤ

## Composição respeita a ordem dos programas

Se P(x)=a₁x+b₁ e Q(y)=a₂y+b₂, executar P e depois Q calcula a₂a₁x+a₂b₁+b₂. A concatenação das listas tem essa mesma semântica. ADD 3 seguido de MUL 2 dá 2x+6; inverter as duas instruções dá 2x+3. A função compose recebe primeiro o programa a executar primeiro. A multiplicação dos coeficientes não autoriza trocar a ordem dos programas completos.

(Q∘P)(x)=a₂a₁x+a₂b₁+b₂

## Uma limitação pode ser provada sem testar todas as entradas

A função quadrado x↦x² não pertence a essa classe. Se a x+b coincidisse com x² em toda entrada inteira, x=0 exigiria b=0 e x=1 exigiria a=1. Mas em x=2, a expressão afim daria 2, enquanto o quadrado vale 4: contradição. O teste nesses três pontos serve a uma prova com coeficientes forçados; observar vários exemplos isolados sem esse argumento não caracteriza todas as funções possíveis. Sob a entrada e saída inteiras declaradas, o interpretador não torna a linguagem universal.

## Programa finito não significa execução sempre curta

Uma máquina de Turing universal tem uma descrição finita, mas pode repetir operações por um número de passos que depende da máquina simulada e da entrada, sem limite único pré-fixado. Na nossa linguagem, a execução percorre cada instrução da lista uma vez e não contém desvios ou repetição controlados pelos dados. A limitação de classe foi demonstrada pelo invariante afim, não apenas pela observação de que a lista de instruções é finita.

## Universalidade exige uma máquina fixa e todos os programas do modelo

No sentido estudado, existe uma máquina U que recebe uma codificação de outra máquina M e de sua entrada w e simula M sobre w. A máquina U é fixa; a descrição de M varia como dado. A afirmação precisa valer para qualquer descrição válida do modelo e entrada admitida, com recursos potencialmente sem limite fixo de antemão. Interpretar dois programas ou admitir muitas operações não prova esse quantificador geral. A referência consultada descreve a ideia, mas também não apresenta ali uma construção completa de U.

U(⟨M,w⟩) simula M(w)

## Simular comportamento não decide automaticamente quando ele termina

Se M termina, uma simulação correta deve reproduzir seu resultado sob a codificação escolhida; se M continua executando, a simulação sem orçamento também continua. Um simulador limitado a k passos só informa o que ocorreu até esse orçamento. O laboratório anterior de Turing ilustra essa diferença. A existência de uma máquina universal não fornece, por si só, um algoritmo que responda em tempo finito se qualquer programa vai terminar. A prova do problema da parada pertence ao próximo tema.

## A tese de Church–Turing e a eficiência respondem a perguntas diferentes

A tese relaciona procedimentos efetivos, entendidos informalmente, ao modelo matemático de computação. Ela não é um teorema obtido apenas por definir um interpretador. Também não afirma que toda simulação tem o mesmo tempo, a mesma memória ou utilidade prática. Nesta aula usamos essa leitura sobre procedimentos efetivos; o trecho da obra discute ainda uma formulação física mais forte, que não demonstramos nem usamos para concluir como todo sistema natural pode computar.

## O laboratório verifica equivalências dentro da classe declarada

O código compara execução e forma afim, serialização e composição, com inteiros de precisão arbitrária do Python. Conta instruções, não custo em bits: multiplicar números muito grandes pode custar mais que somar números pequenos. Os testes finitos conferem a implementação; a prova do invariante e a obstrução ao quadrado aparecem no texto. Não foi construída uma máquina universal do modelo, uma prova geral de compilador ou um processador físico. Percurso complementar próprio, distinto de CCM0128; revisão de Jhuann pendente.

## Exercícios originais e resoluções

Começando em 1, ADD 4 seguido de MUL 3 produz quanto? **Resolução:** (1+4)×3=15.

Todo interpretador pequeno é automaticamente uma máquina universal? **Resolução:** É preciso especificar o modelo e mostrar a capacidade de simulação.

No programa ADD 3,MUL 2, qual o coeficiente a em P(x)=ax+b? **Resolução:** x→x+3→2x+6, logo a=2.

No mesmo programa, qual a constante b? **Resolução:** Multiplicar o acumulador por2 também multiplica a parcela3: b=6.

Quanto o programa ADD 3,MUL 2 devolve ao receber x=4? **Resolução:** (4+3)×2=14, igual a2×4+6.

Partindo de zero, quanto produz MUL 2 seguido de ADD 3? **Resolução:** 0×2+3=3; a lista invertida não produz6.

MUL 0 seguido de ADD 7 recebe x=999. Qual a saída? **Resolução:** A primeira instrução zera o acumulador; depois soma7.

MUL −2 seguido de ADD 5 recebe x=3. Qual a saída? **Resolução:** −2×3+5=−1.

Uma função afim coincide com o quadrado em 0 e1. Qual valor ela é forçada a ter em 2? **Resolução:** b=0 e a=1, portanto em 2 vale2, diferente de4.

Quantas instruções executa ADD 5,SUB 2,MUL 3, qualquer que seja a entrada inteira? **Resolução:** A lista tem três instruções e cada uma é percorrida uma vez.

Apenas ADD,SUB,MUL por constantes inteiras, sem outras construções, calculam x² para toda entrada inteira? **Resolução:** Todas as funções calculadas são afins; a contradição nos pontos0,1,2 exclui o quadrado.

Uma máquina universal que simula programas é, por essa razão apenas, um decisor que sempre responde se eles param? **Resolução:** A simulação pode continuar quando o programa simulado continua; simular e decidir término são problemas diferentes.

## Fonte e laboratório

Sedgewick e Wayne — Computer Science: An Interdisciplinary Approach, exemplar autorizado com copyright Pearson2017; nome de arquivo2016 não estabelece ano editorial.

§5.3: recortes textuais de pp.786–789/PDF807–810 e p.791/PDF812 consultados parcialmente em 26/10/2026. Não se leu a seção inteira nem se reproduz uma construção completa de U. A obra discute também uma formulação física mais forte da tese; a aula delimita a leitura sobre procedimentos efetivos. Linguagem afim, codificação, prova, figura e testes próprios.

`execute(program,x=0)` retorna resultado, contagem de instruções e traço. `compile_affine(program)` retorna(a,b); `compose(first,second)` significa executar first antes de second. `encode/decode` usam JSON e validam pares, operações e inteiros; bool e float não são operandos. Não há eval, saltos ou execução de texto arbitrário. O exemplo simples anterior suporta ADD/MUL; o laboratório inclui SUB, completando o desafio.

Executar: `python3 -m unittest discover -s labs/programas-dados -t .`. Testes com 3616 programas curtos e sete entradas inteiras conferem implementação; a prova geral está no invariante, não no total de testes. Sem páginas do livro, construção física, resultado de pesquisa ou domínio pessoal reivindicado. Rascunho assistido por IA para revisão de Jhuann.
