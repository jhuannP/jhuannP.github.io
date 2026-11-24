# Inserção: invariantes, inversões e estabilidade

27/10/2026. Material original com apoio de IA, em rascunho para revisão pessoal. Aprofundamento em Computação I; não comprova prática ou domínio de Jhuann.

## Contrato e prova

Entrada finita, chaves com ordem coerente e constante durante a execução, sem NaN. Saída ordenada e permutação dos itens com multiplicidades preservadas. Inicialmente prefixo de comprimento 1 ordenado. Antes da passagem i: prefixo a[:i] ordenado e permutação dos primeiros i itens originais; sufixo não processado preservado. Guardar chave antes de deslocar mantém o multiconjunto na lista útil mais a variável temporária; reinserir amplia prefixo ordenado. j diminui e i aumenta em intervalos finitos. Ao final o prefixo cobre a lista.

Exemplo preservado [4,1,3,2]: estados [1,4,3,2], [1,3,4,2], [1,2,3,4]. Deslocamentos 1+1+2=4; comparações entre chaves 1+2+3=6; escritas 4+3=7, incluindo reinserções. Excluídos dos contadores: cópia, cache, checagem de índice, acesso e histórico.

Inversões: pares p<q com valor[p]>valor[q]; cada deslocamento remove exatamente uma inversão, portanto shifts=I. Para n≥1, I≤C≤I+n−1, W=I+n−1. Ordenada/iguais: I=0,C=n−1; distintos reversos: I=C=n(n−1)/2. Núcleo com operações de custo constante: O(n+I). Com chaves de custo variável é necessário rever esse modelo.

Estabilidade: teste > impede atravessar iguais. Registros (2,A),(1,B),(2,C),(1,D), ordenados por primeiro campo, dão (1,B),(1,D),(2,A),(2,C). Comparar tuplas inteiras considera o segundo campo, outro contrato. Cópia de lista é externa, não clona dicionários/objetos internos. Tuplas do histórico copiam posições, não versões profundas de objetos.

## Fonte e diferenças de implementação

Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, exemplar identificado ©2017: §4.2 pp.543–544/PDF564–565, prefixo/casos; programa 4.2.4 p.547/PDF568, inspecionado visualmente em 27/10/2026. Consulta parcial, sem leitura integral. Arquivo e bibliografia usam 2016; copyright não confirma impressão. Página pública de apoio retornou 403; não foi tratada como fonte lida. Exemplar privado não distribuído.

Fonte usa Java e trocas adjacentes; versão anterior da aula em Python por deslocamentos e cópia foi preservada. Instrumentação, prova escrita, números, figura e exercícios próprios. Não equiparar contagem de troca com todas as atribuições de um algoritmo por deslocamento.

## Código e verificação

`insertion.py` faz uma cópia externa, calcula key uma vez por item e guarda cache O(n). Aceita chave chamável e capture booleano. Não valida globalmente a relação de ordem; erros de comparabilidade propagam. Não faz benchmark nem ordenação de produção. Resultado contém itens, comparações entre chaves, deslocamentos, escritas e traço opcional. Sem capture, não guarda estados; com capture, n posições por passagem dão O(n²) espaço/trabalho adicional, mesmo com I=0. O núcleo tradicional dentro de uma lista usa O(1) extra, mas essa não é a memória total deste invólucro.

Da raiz: `python3 -m unittest discover -s labs/insercao-invariantes -t .`. Cinco testes: 1093 entradas com valores 0,1,2/comprimento até 6 contra sorted, multiconjuntos, inversões e contadores; traço/prefixo; estabilidade e avaliação única de key; melhores/piores/iguais; cópia rasa e contratos. Evidência finita complementa a prova, sem cobrir todos os comparadores.

Preservados IDs oi1/oi2, exemplo [4,1,3,2], Python, desafio e painel insertionSort. Dez respostas novas: 4 inversões;4 deslocamentos;6 comparações;7 escritas;10 deslocamentos reversos com n=5;0 para iguais; preservar permutação; comparação estrita; histórico quadrático; cópia rasa. Resoluções na aula.

Revisão proposta em duas sessões: traçar e justificar o invariante; depois explicar estabilidade, inversões e custo do histórico. Pendentes: comparadores especiais, ordenação de produção, sequência ampla de análise e revisão/execução pessoal.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 758 fórmulas MathML conferidas. Em 390 px, oi5 rejeitou quatro e aceitou seis comparações pelo Enter; custo do histórico aceito. Painel no final mostrou [1,2,3,4]; figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
