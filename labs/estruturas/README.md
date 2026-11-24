# Pilha ligada e fila circular expansível

Conteúdo original em rascunho para Jhuann, organizado pelo eixo 4.3 de Computer Science (2016). Código em Python, sem dependências.

## Contratos e representação

`LinkedStack` expõe push/pop/peek e tamanho. Um nó aponta para o anterior; o topo guarda o item mais recente. Push/pop/peek têm O(1) no modelo de operações de ponteiros, sem contar custo arbitrário do objeto ou alocador.

`CircularQueue` expõe enqueue/dequeue/peek e tamanho. A cabeça identifica o primeiro a sair, n é o número de itens, C a capacidade. O item lógico i está em (cabeça+i) mod C. 0≤n≤C e 0≤cabeça<C. Inserção escreve em (cabeça+n) mod C. Quando n=C, dobra C, copia os itens na ordem FIFO para índices 0..n−1 e reinicia cabeça=0. Não basta copiar o vetor antigo sem considerar a cabeça.

Retirada limpa o slot para liberar a referência. `None` também é um item permitido: o vazio é determinado por n, nunca pelo valor de um slot. Retirar/consultar estrutura vazia levanta IndexError sem modificar estado. Esta versão não encolhe: memória depende do maior tamanho atingido, não somente do tamanho atual.

Para aplicações reais, [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) já oferece operações eficientes nas pontas. Os tipos próprios servem para aprender a implementação; não reimplementam todos os recursos de deque.

## Por que amortizado não é pior caso

Com capacidade inicial 2 e N inserções sem retiradas, crescimentos copiam 2+4+8+… até a maior potência anterior a N. A soma é menor que 2N. Somando N escritas de inserção, são menos de 3N escritas de itens. Em N=64: 62 cópias, 64 inserções, 126 escritas. Uma operação isolada que cresce pode copiar n itens, portanto custa O(n), apesar do custo O(1) amortizado numa sequência.

Os contadores `copied`/`inserted` não são tempos nem contagem de todas as operações. Criar o vetor novo também tem custo proporcional à capacidade; isso muda constantes, preservando a soma geométrica O(N). Retiradas não encolhem a estrutura nem provocam novas cópias; numa sequência mista, crescimento também permanece limitado geometricamente. Snapshot/values percorrem a estrutura e ficam fora do custo das operações elementares.

## Executar e estudar

Salve `structures.py` e rode `python3 structures.py`. Para testes, salve `test_structures.py` na mesma pasta e execute `python3 -m unittest discover -p 'test_*.py'`.

1. Trace A,B,C em uma pilha e em uma fila; explique a diferença de contrato.
2. Reproduza as 14 operações fixas do site. Antes de avançar, preveja cabeça, capacidade e próximo item a sair.
3. Identifique a operação que cresce quando a cabeça não é zero. Mostre por que a cópia precisa seguir a ordem lógica.
4. Prove a soma geométrica das cópias. Diferencie pior caso, amortizado e média probabilística: aqui não se supõe distribuição de entradas.
5. Implemente a fila a partir do contrato e compare sequências com deque. Teste None, vazio, reutilização e crescimento após dar a volta.
6. Como extensão, projete encolhimento com histerese: dobrar quando cheio e reduzir pela metade quando n≤C/4, respeitando capacidade mínima. Explique por que reduzir logo após uma retirada pode causar repetidas cópias ao alternar inserção/retirada. Esta extensão não está implementada.

Cinco testes conferem pilha versus list, todas as 511 sequências de inserir/retirar de comprimento até 8 em três capacidades iniciais, invariantes, crescimento com cabeça não zero, None, limpeza, instâncias independentes e limites geométricos para N=1..512. Não constituem avaliação de aprendizagem; revisão conceitual/didática e aplicação em aula permanecem pendentes.
