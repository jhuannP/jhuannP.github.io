# Mergesort: correção, estabilidade e contagem

27/10/2026. Rascunho original de12 seções/12 exercícios, aguardando revisão de Jhuann. Pré-requisitos: listas, índices, laços, funções, recursão e contagem de operações.

## Revisão em dois blocos

1. Intercale [1,4] e [2,3], escrevendo o invariante antes de cada escolha. Depois ordene os registros (2,A),(1,B),(2,C),(1,D) apenas pela chave numérica e explique por que B precede D e A precede C.
2. Reconstrua o custo por níveis. Para oito itens, o máximo de comparações de chaves é17 e a entrada já ordenada desta implementação usa12. Explique quais operações não foram contadas e por que alocação acumulada não é pico de memória viva.

## Código e contrato

Execute `python3 labs/mergesort-estavel/sorting.py` na pasta do protótipo. `sort_count` devolve uma lista nova e estatísticas. Implementação Python própria, recursiva, com fatias e cópia rasa, comparando apenas a chave. O teste<= escolhe a esquerda nos empates. `key` deve ser pura e gerar uma comparação total consistente; não se faz validação geral de comparadores arbitrários.

A instrumentação conta comparações de chaves e chamadas, não segundos, custo de key, operações de índice ou memória real. `sorted` é oráculo independente de resultado, sem atribuir a ele o mesmo algoritmo ou custo. Conferências incluem multiconjunto, estabilidade e entrada preservada. A enumeração finita não substitui a prova por invariante e indução.

A figura mostra três estados de um exemplo original; não é execução filmada ou resultado de cliente. A implementação anterior da aula permanece disponível, e o novo laboratório é uma variante instrumentada.

## Fontes e limites

Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, copyright2017, §4.2 pp.550–553/PDF571–574, consulta textual parcial do acervo autorizado em27/10/2026. O nome do arquivo pode trazer2016; paginação não deve ser transferida para Introduction to Programming in Java2008. Lidos recortes de divisão, intercalação e custo por níveis; sem leitura integral, nova inspeção visual, cópia do programa Java ou distribuição do PDF privado.

A página complementar da editora/autores em Princeton foi tentada e retornou403 nesta rodada; não é apresentada como consulta bem-sucedida. O apoio efetivo veio do exemplar autorizado.

Ordenação externa, versão iterativa, paralelismo, comparadores de custo variável e medições de desempenho permanecem pendentes. Memória auxiliar O(n) descreve posições vivas do algoritmo sequencial, com pilha O(log n), sem exigir o mesmo comportamento do alocador e do coletor de Python. Conteúdo preparado não certifica domínio pessoal ou experiência de produção.
