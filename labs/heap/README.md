# Heap mínimo estável — notas originais em elaboração

16/10/2026. Revisão de Jhuann pendente.

## A prioridade muda o contrato de retirada

Uma fila FIFO retira o elemento mais antigo. Uma fila de prioridade mínima retira um elemento com a menor chave de prioridade. Nesta implementação, a prioridade é um inteiro, valores menores saem primeiro e empates saem por ordem de inserção. Números negativos são permitidos. Esse desempate está no contrato: heaps em geral não são automaticamente estáveis.

## Separe prioridade, bilhete e objeto

Cada entrada guarda (prioridade, bilhete, valor). O bilhete cresce a cada inserção e desempata prioridades iguais. Comparamos apenas os dois primeiros campos; o valor pode ser dicionário, lista ou outro objeto sem ordem definida. Comparar a tupla inteira sem garantir o desempate pode tentar ordenar objetos incompatíveis. O cliente não pode alterar a prioridade de uma entrada já inserida por este contrato.

## Um vetor representa uma árvore completa

Com índices começando em zero, o pai de i>0 é ⌊(i−1)/2⌋, e os filhos são 2i+1 e 2i+2 quando menores que n. Os elementos ocupam posições consecutivas, logo a árvore fica preenchida por níveis. A forma completa garante altura O(log n). É uma representação lógica; não alocamos nós ligados separados.

## O invariante é local, mas garante um mínimo global

Para cada aresta, a chave do pai é menor ou igual à do filho. Seguindo o caminho da raiz até qualquer nó e usando transitividade, a raiz é menor ou igual a todos. Não existe exigência de que irmãos ou posições consecutivas estejam ordenados. Por exemplo, prioridades [1,2,1,3] formam heap, embora 2 venha antes de 1 no vetor.

## Inserir restaura a ordem subindo

Acrescente a entrada no fim, preservando a forma completa. A única possível violação está no caminho desse novo nó até a raiz. Enquanto sua chave for menor que a do pai, troque os dois e prossiga no pai. Os demais ramos continuam ordenados. Ao parar na raiz ou diante de pai menor ou igual, o invariante está restaurado.

## Retirar restaura a ordem descendo pelo menor filho

Guarde a raiz, remova o último elemento e, se houver elementos restantes, coloque-o na raiz. A forma completa permanece. Compare com o menor filho; se esse filho for menor, troque e continue por ele. Escolher o filho maior pode deixar o menor acima do pai e quebrar o heap. Quando não há filhos ou a chave já é menor ou igual a ambos, o reparo termina.

## O vazio e o singleton merecem tratamento explícito

peek e pop em vazio lançam IndexError antes de alterar estado. Ao retirar de tamanho um, o vetor simplesmente fica vazio; não se tenta escrever em posição zero inexistente. Depois pode-se inserir novamente. Consultar peek devolve prioridade e valor sem remover; entries é um retrato raso da representação para ensino, não uma sequência ordenada de serviço.

## Desempate estável não impede novas urgências

Insira A com prioridade 3, B com 1, C com 1 e D com 2. Saem B antes de C pelo bilhete, depois D e A se nada novo entrar. Se E com prioridade 0 chega após a retirada de B e C, ele sai antes de D. Estabilidade trata empates; não obriga uma tarefa antiga menos prioritária a sair antes de uma nova mais prioritária. Uma política assim pode sofrer inanição sob novas chegadas, problema que o heap sozinho não resolve.

## A altura controla os reparos, não todos os custos do sistema

Subir ou descer atravessa no máximo a altura: O(log n) comparações no pior caso. peek é O(1), armazenamento O(n) e validate/entries são O(n). O modelo supõe comparação e movimento de referências com custo unitário. Python usa vetor dinâmico: append tem custo amortizado O(1), mas uma realocação isolada pode custar O(n). Não prometa latência estrita O(log n) para a operação inteira com essa alocação.

## Conferir contra ordenação fornece uma referência diferente

Os testes geram 4096 traços de seis operações com inserções de prioridades 0/1, retirada e consulta, comparando com uma lista de referência cuja menor chave é escolhida diretamente. Eles conferem multiconjunto de entradas, tamanho, exceções e invariante. Outro teste usa valores sem comparação e prioridades negativas. A interface reproduz o mesmo traço do Python em JavaScript; concordância entre implementações não substitui prova geral.

## Heap não resolve sozinho todo problema de caminho mínimo

Uma fila de prioridade pode apoiar Dijkstra quando as hipóteses do algoritmo forem atendidas, mas a prova do caminho mínimo e o tratamento de arestas pertencem a outra aula. Esta fila não tem decrease-key, remoção arbitrária, construção linear em lote ou concorrência. Uma estratégia futura é inserir novas entradas e descartar as antigas com checagem de versão; não use essa ideia sem analisar correção e custo.

## Resoluções

Qual o índice do pai de i=6 num heap com índices a partir de zero?

⌊(6−1)/2⌋=2.

Qual o índice do filho esquerdo de i=2?

2×2+1=5.

Qual o índice do filho direito de i=2?

2×2+2=6.

No vetor de prioridades [1,2,1,3], qual a menor prioridade?

A raiz tem prioridade 1.

Quantas entradas restam após quatro inserções e duas retiradas válidas?

4−2=2.

Um heap precisa estar totalmente ordenado no vetor?

Basta ordem em cada aresta pai–filho.

Para reparar descendo, qual filho deve ser escolhido?

A chave deve ficar abaixo de ambos, então é preciso começar pelo menor filho.

Com B:1 inserido antes de C:1, quem sai primeiro nesta implementação?

O bilhete menor desempata a prioridade 1.

O diagnóstico validate tem custo O(1)?

Ele percorre as arestas, com custo O(n).

## Roteiro didático e evidência

Pré-requisitos: ADT, vetores, comparação de chaves e logaritmos. Desenhar índices e árvore; pedir um vetor que é heap sem estar ordenado; justificar por que escolher o menor filho preserva a ordem. Produto de compreensão: traço comentado com empates e um teste que rejeite reparo pelo filho errado. Não inferir domínio pessoal a partir da geração desta aula.

## Fontes e pendências

Escopo: [CCM0128](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0128), consultado em 16/10/2026, ativação 2025 posterior à turma. Algorithms, quarta edição (2011), identificado no acervo; código e exemplos próprios, sem disponibilizar o PDF. Ainda faltam heapify linear, decrease-key, estratégias de atualização e aplicações em grafos.
