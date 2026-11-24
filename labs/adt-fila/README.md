# ADT e fila ligada — notas originais em elaboração

16/10/2026. Revisão de Jhuann pendente.

## O tipo abstrato descreve comportamento

Um tipo abstrato de dados define valores possíveis e operações observáveis, sem fixar a representação. Aqui uma fila é uma sequência finita Q. enqueue(x) acrescenta x ao fim; dequeue remove e devolve o primeiro; peek consulta o primeiro sem remover; len informa o tamanho. FIFO é uma regra de comportamento, não o nome de uma estrutura de memória.

## O contrato precisa definir o caso vazio

Se Q=(a,b), enqueue(c) produz (a,b,c), dequeue devolve a e deixa (b). Para Q=(), dequeue e peek lançam IndexError e preservam a fila. Retornar None para vazio seria ambíguo, pois None é um valor permitido. As operações trabalham com referências aos objetos recebidos, sem copiá-los profundamente.

## Uma classe não garante um ADT correto

Ter métodos com os nomes certos é insuficiente. A implementação deve satisfazer as pós-condições em todas as sequências válidas de chamadas, incluindo esvaziar e reutilizar a fila. O código usa nós ligados, mas um buffer circular também pode cumprir o mesmo contrato FIFO. Clientes não devem depender de atributos internos.

## A representação tem um invariante

Os campos internos são cabeça, cauda e tamanho. A cadeia deve ser finita e sem ciclos; o número de nós alcançáveis deve ser o tamanho; a cauda deve ser o último nó, com próximo nulo. Na fila vazia, cabeça e cauda são ambas nulas e tamanho é zero. Um ponteiro de cauda antigo pode fazer uma inserção desaparecer da cadeia observável.

## A função de abstração liga memória e significado

Para uma representação válida, percorra os nós da cabeça até o fim e leia seus valores: essa sequência é AF(rep). A correção consiste em preservar o invariante e fazer cada operação concreta corresponder à operação sobre a sequência abstrata. Representações diferentes podem ter a mesma AF. Uma representação com ciclo não tem a sequência finita pretendida.

## Inserir tem dois casos que preservam a cadeia

Crie um nó com próximo nulo. Se a fila estava vazia, faça cabeça apontar para ele. Caso contrário, ligue a antiga cauda ao nó. Atualize cauda e incremente tamanho. Em ambos os casos a sequência anterior recebe exatamente um novo elemento no fim, sem alterar os anteriores.

## Retirar o último exige limpar a cauda

Se vazia, lance a exceção antes de alterar o estado. Caso contrário, guarde o valor da cabeça, avance cabeça para o próximo nó e reduza tamanho. Se a nova cabeça for nula, a fila ficou vazia e cauda também deve virar nula. A abstração perde apenas o primeiro elemento. Este caso de fronteira é essencial para uma inserção posterior.

## O custo faz parte da escolha da representação

Com cabeça e cauda, enqueue, peek e dequeue fazem trabalho O(1) no modelo de custo unitário de ponteiros e alocação; o tamanho também é O(1). Espaço é O(n), com um nó por elemento. validate e values percorrem a cadeia e custam O(n). Não chame o diagnóstico em toda operação e depois afirme que o programa instrumentado continua O(1). Custos de copiar ou processar o objeto armazenado não entram aqui.

## Uma fotografia rasa não congela os objetos

values retorna uma tupla com referências aos valores, não aos nós, mas não faz cópia profunda. Se um valor for uma lista mutável e o cliente a alterar, a mudança aparece no retrato e na consulta. Isso não altera a ordem nem o tamanho da fila. O contrato deve declarar essa escolha; imutabilidade do recipiente não implica imutabilidade de seu conteúdo.

## Testar traços é mais forte que conferir um exemplo

Os testes comparam todas as 4096 sequências de seis operações pequenas com collections.deque: inserir 0, inserir 1, retirar e consultar. Conferem valores, exceções, tamanho e diagnóstico após cada passo. Também testam reutilização e detectam ciclos/cauda inconsistente. Essa verificação finita encontra erros concretos, mas não substitui a justificativa geral pelas invariantes.

## A interface pode sobreviver à troca de estrutura

Um cliente que depende só do contrato FIFO pode substituir fila ligada por buffer circular sem mudar a ordem esperada. Desempenho, uso de memória, limites e política de cópia ainda precisam ser comparados. Este laboratório é sequencial e não fornece segurança de concorrência; filas de prioridade obedecem outro contrato de retirada e serão estudadas separadamente.

## Resoluções

Após inserir 1, inserir 2 e retirar uma vez, qual valor saiu?

FIFO devolve o primeiro inserido, 1.

Após inserir A, inserir B, retirar e inserir C, qual o tamanho?

Restam B e C, total 2.

Quantas sequências de seis operações existem com quatro opções por passo?

4⁶=4096.

Se uma fila tem zero elementos e recebe um, qual o tamanho?

O tamanho aumenta de zero para um.

O contrato FIFO exige nós ligados?

O contrato define a ordem; buffer circular também pode cumpri-lo.

Ao retirar o último elemento, o que acontece com a cauda?

A fila vazia deve ter cabeça e cauda nulas.

Qual o custo de percorrer toda a cadeia em validate?

Cada nó alcançável é visitado.

A tupla de values torna imutáveis os objetos guardados?

O retrato é raso; os objetos podem ser mutáveis.

4096 traços aprovados provam correção para todos os programas clientes?

São evidências finitas; a justificativa geral exige contrato e invariantes.

## Roteiro de ensino e evidência

Pré-requisitos: funções, classes, referências e raciocínio de custo. Primeiro descrever a sequência abstrata; depois desenhar cabeça, cauda e nós; por fim conferir as quatro transições: inserção em vazia/não vazia, retirada de um/vários nós. Pedir uma explicação própria da função de abstração e um teste que falhe ao manter a cauda antiga. Nenhum resultado comprova domínio pessoal sem revisão e explicação de Jhuann.

## Fonte curricular e bibliografia

[CCM0128 no Júpiter](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0128), consulta direta em 16/10/2026, ativação 2025 posterior à turma. Algorithms, quarta edição (2011), identificado nas páginas iniciais do acervo. Texto e código próprios; PDFs não são publicados. Pendentes: fila de prioridade, ordenação linear e caminhos ponderados, além do aprofundamento e revisão dos outros tópicos.
