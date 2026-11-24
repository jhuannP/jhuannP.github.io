# Custo de algoritmos: nomear a operação antes de contar

27/10/2026. Notas de aula e laboratório originais, assistidos por IA, em rascunho para revisão pessoal. Não comprova desempenho ou domínio de Jhuann.

A aula `custo-algoritmos` preserva o exemplo de pares n4/n8 e o código inicial. O contador original chamado comparacoes conta iterações, sem comparação de valores; isso agora é explicitado. n conta posições, não valores distintos. Visitas simples n e visitas a pares n(n−1)/2 não são segundos. Razão de duplicação4+2/(n−1), para n≥2. Cotas n²/4 e n²/2 provam Θ(n²); O(n³) também é verdadeiro, mas menos justo.

Busca linear retorna a primeira ocorrência e conta apenas item==alvo. Melhor caso1 para entrada não vazia, pior n e caso vazio0. Média(n+1)/2 exige alvo único e posição uniforme. Laço de divisão inteira por2 tem⌊log₂n⌋+1 passos se n>0 e0 no vazio. Custos sintéticos100n e n(n−1)/2 empatam em n positivo201; não são tempos medidos.

Guardar todos os pares usa Θ(n²) palavras no modelo; só contá-los usa quantidade constante de palavras auxiliares. Em bits, tamanho de índices/contador cresce: a aula não promete memória em bits constante para inteiros arbitrários. Python aceita inteiros grandes, mas este modelo não trata comparação/aritimética desses valores como custo real constante.

## Fonte e limite da consulta

Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, ©2017, §4.1 p.502/PDF523 e p.505/PDF526, consulta textual parcial em27/10/2026. Modelo de custo e ordens; livro usa Java, exemplos desta aula são próprios em Python. Arquivo com2016 no nome não foi interpretado como edição. Sem nova inspeção visual, leitura integral, cópia de exercícios ou distribuição do PDF privado. O acesso à página Princeton41analysis retornou403, portanto seu conteúdo não foi lido nem usado como fonte confirmada neste bloco. Júpiter não reaberto; limites do mapa curricular preservados.

## Conferências reproduzíveis

Execute `python3 labs/custo-contagem/counts.py`. Cinco testes: contagem de pares em n0..100 e armazenamento comparado a itertools.combinations até30; limites e razão de duplicação em99 tamanhos; busca em4372 combinações de listas sobre{−1,0,1}, comprimento0..6, e quatro alvos; média uniforme em40 tamanhos e divisão por2 em4097 entradas; contratos.

A referência de busca enumera todas as posições compatíveis e escolhe a primeira; a implementação retorna cedo. As verificações conferem resultado e operação contada. Não há benchmark, entrada real de produto, promessa de latência ou prova geral baseada apenas no conjunto finito. As somas e desigualdades da aula fundamentam o crescimento.

Próxima ação de20min: derivar o triângulo, explicar14/3 e comparar casos da busca. Depois distinguir memória para contar de memória para armazenar. Análise amortizada, custo de bits, recorrências e experimentos de desempenho de uma aplicação continuam pendentes. Python opcional para reconstruir as contas.
