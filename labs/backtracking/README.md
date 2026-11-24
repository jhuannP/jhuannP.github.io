# Backtracking: escolher, podar e restaurar estado

Material original em rascunho — 16/10/2026. Escopo relacionado a CCM0118, programa consultado em 16/10 com ativação 15/07/2024; versão da turma de 2023 não recuperada. https://uspdigital.usp.br/jupiterweb/jupDisciplina?sgldis=CCM0118

## Recursão com escolhas exige voltar ao estado anterior

Backtracking explora uma árvore de escolhas. Em cada nó, escolha uma opção, atualize o estado, resolva o restante e desfaça a atualização antes da próxima opção. A recursão organiza a busca; a poda evita explorar prefixos que já não podem levar a uma solução. Isso não torna toda busca eficiente.

## Defina primeiro o problema e a representação

Queremos colocar n rainhas num tabuleiro n×n, sem duas na mesma linha, coluna ou diagonal. Colocamos uma por linha. O prefixo escolhido guarda, em cada posição r, a coluna da rainha da linha r. O Python usa índices de zero a n−1. A demonstração numera linhas e colunas de 1 a n para leitura.

## O invariante descreve um prefixo válido

Ao entrar em visit, len(chosen) é o número de linhas preenchidas, cada coluna está no tabuleiro e nenhuma dupla no prefixo se ataca. Se o prefixo tiver r elementos, a próxima rainha pertence à linha r. O prefixo vazio satisfaz o invariante e inicia a busca.

## Uma poda precisa ser uma rejeição segura

Uma candidata na coluna c da linha r conflita com uma rainha anterior na linha i, coluna p, se c=p ou |c−p|=r−i. Esse ataque não desaparece ao adicionar outras rainhas: o prefixo inteiro pode ser descartado. Podar por uma preferência estética ou por um resultado aparentemente ruim poderia eliminar soluções corretas.

## Escolher, explorar e desfazer são três passos distintos

Se a coluna passa na verificação, faça chosen.append(c), visite o próximo nível e faça chosen.pop(). O pop restaura exatamente o prefixo da entrada, permitindo testar outra coluna. No Python, try/finally garante a restauração mesmo se a visita levantar uma exceção; ele não significa que a busca concluiu normalmente nessa situação.

## O caso base precisa guardar uma cópia

Quando len(chosen)=n, todas as linhas estão preenchidas e o invariante garante uma solução. Guarde tuple(chosen), não a própria lista escolhida, pois a busca continuará removendo elementos. Se várias soluções apontassem para a mesma lista mutável, o resultado final poderia conter cópias aparentes do estado vazio.

## Por que encontra todas as soluções sem repetir

Toda solução válida tem uma coluna por linha. Em cada prefixo dessa solução, sua próxima coluna não conflita e será testada pelo laço; logo o caminho até a solução será visitado. Cada sequência de colunas corresponde a um único caminho na árvore, então não é gerada duas vezes. Soluções relacionadas por simetria são sequências distintas e continuam contadas separadamente.

## Progresso e custo têm argumentos diferentes

Cada chamada recursiva aceita uma rainha a mais, então a profundidade é no máximo n e cada laço é finito. Isso prova término nesta busca. O número de prefixos pode crescer rapidamente; mesmo impedindo colunas repetidas, há até n! permutações completas. O teste de conflito percorre o prefixo. Medir poucos tamanhos não estabelece uma classe de complexidade melhor.

## Métricas precisam de definições comparáveis

No laboratório, nó é uma chamada com prefixo válido, incluindo raiz e soluções; tentativa é uma coluna testada; poda é uma tentativa rejeitada. Em n=4, há 17 nós, 60 tentativas e 44 podas. Cada tentativa aceita cria uma chamada nova, por isso tentativas=nós−1+podas. Não compare tentativas com permutações completas como se fossem a mesma unidade de trabalho.

## Uma referência independente ajuda a encontrar erros

A referência gera todas as permutações de colunas, que já evitam repetições de linha e coluna, e verifica se as somas r+c e diferenças r−c são distintas. Esse critério de diagonais é independente do teste incremental por distância. Os conjuntos ordenados de soluções são comparados para n=1 até 8. Isso aumenta a confiança no código, sem substituir a justificativa de correção.

## Sem solução também é um resultado

Em n=2 e n=3, a busca exaure todas as escolhas e retorna lista vazia. Isso é diferente de interrupção, exceção ou atingir orçamento de execução. O laboratório termina a enumeração para os tamanhos permitidos; não implementa limite de tempo que pudesse deixar a busca incompleta. Antes de generalizar, registre restrições de tamanho e como distinguir parada de exaustão.

## Exemplo resolvido

No tabuleiro 4×4, siga o prefixo [1,3] com índices desde zero. Qual pode ser a próxima coluna?

As rainhas ocupam as posições (0,1) e (1,3). A próxima linha é 2.

As colunas 1 e 3 já estão usadas.

A coluna 2 conflita na diagonal com (1,3).

A coluna 0 não conflita: é uma escolha válida, formando [1,3,0].

A linha seguinte permite coluna 2, produzindo [1,3,0,2].

Guarde uma cópia da solução e desfaça as escolhas para explorar os outros caminhos. Existe ainda a solução [2,0,3,1].

## Exercícios e resoluções

### Quantas soluções tem o tabuleiro 4×4, contando simétricas separadamente?

[1,3,0,2] e [2,0,3,1], com índices desde zero.

### Quantas soluções tem o tabuleiro 2×2?

Todas as escolhas entram em conflito.

### No prefixo [1,3], qual é o índice da próxima linha?

len(prefix)=2, então a próxima linha é 2.

### Se há 17 nós e 44 podas, quantas tentativas foram feitas?

17−1+44=60.

### Qual a profundidade máxima de rainhas colocadas num tabuleiro 4×4?

Cada nível coloca uma rainha; não pode passar de quatro.

### Pode-se guardar a própria lista chosen e continuar removendo elementos sem afetar o resultado guardado?

É preciso copiar; tuple(chosen) preserva o conteúdo da solução.

### Um ataque entre duas rainhas já colocadas pode desaparecer ao adicionar outras?

As posições antigas continuam atacando-se, então a poda é segura.

### Demonstrar término também demonstra que o algoritmo é rápido para qualquer n?

A profundidade é finita, mas o número de ramos pode crescer rapidamente.

### Lista vazia depois de enumeração completa significa que não houve solução nesse domínio?

Sim; é diferente de execução interrompida antes de terminar.

## Preparação de aula

Trace as escolhas no caso 4×4; mostre um conflito; acompanhe append/pop; provoque o erro de guardar uma referência mutável; explique completude e término; compare a enumeração de permutações e as métricas sem confundir unidades.

## Pendências

Outros problemas com poda, heurísticas de ordenação e exercícios de prova precisam de aprofundamento. Não é certificação de domínio pessoal nem cobertura integral da disciplina.
