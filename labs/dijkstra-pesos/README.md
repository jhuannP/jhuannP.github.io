# Dijkstra: um caminho mínimo com pesos não negativos

22/10/2026. Aula ccm0128-dijkstra,14 seções/12 exercícios; rascunho para revisão de Jhuann. Texto, grafo e implementação próprios com apoio de IA. Integra CCM0128, disciplina de algoritmos, separada do percurso complementar cujo ID computacao-2 corresponde a teoria/arquitetura.

## Problema e exemplo

Grafo dirigido finito, pesos aditivos não negativos. Queremos distâncias mínimas desde uma origem e um caminho até cada vértice alcançável. BFS minimiza número de arestas, não soma geral de pesos diferentes.

Exemplo próprio:
A→B4, A→C1, A→D10, C→B2, C→D5, B→D1. E isolado.
Finalizar A0 cria B4,C1,D10; finalizar C1 melhora B3,D6; finalizar B3 melhora D4; finalizar D4 conclui os alcançáveis. Caminho A,C,B,D custa4, enquanto a aresta direta custa10. None marca ausência de caminho, distinto do caminho vazio da origem de custo0. grafo-custos.svg é original, não é desenho do exemplo do livro.

## Contrato e representação

dijkstra(graph,source) recebe um dict não vazio, chaves strings não vazias e adjacências em listas/tuplas de pares(destino,peso). Todo destino já deve ser uma chave. Peso int/Fraction não negativo, sem bool/float. Valida todas as arestas, incluindo componentes inalcançáveis; aceita laços e arestas paralelas. Não modifica o grafo.

Retorna um dicionário com origem, distâncias, predecessores(pai,peso) e ordem de finalização. path_to(result,target) reconstrói um caminho a partir desse resultado ou devolve None para inalcançável. Não é uma API de validação de resultados forjados ou alterados à mão; preserve o resultado para consultar. O algoritmo não aceita pesos negativos, não calcula todos os caminhos empatados e não escolhe automaticamente outro método.

## Relaxação, prioridade e correção

Candidato por u→v é d[u]+w. Só melhora estrita atualiza distância/predecessor. Retirar o candidato mínimo permite finalizar sua distância por causa da não negatividade: um caminho hipoteticamente menor teria um primeiro vértice não finalizado cujo prefixo já produziria candidato menor, contradizendo a escolha.

heapq não é uma fila indexada com decrease-key neste código. Cada melhora insere nova entrada(distância,contador,vértice). Uma retirada com distância diferente da atual é antiga e é descartada. O contador desempata pela ordem de inserção; não se promete caminho lexicograficamente mínimo ou único. Custo zero é permitido, inclusive ciclos; melhora estrita evita reescrever predecessores por empate.

Validação O(V+E), até E melhoras e entradas antigas no heap de tamanho O(E+1). Cota segura de operações O((V+E)log(V+E+2)), espaço auxiliar O(V+E). Não é a mesma estrutura da versão indexada do livro. A análise conta operações abstratas; somas/comparações de inteiros e frações exatas dependem também do tamanho dos números.

## Executar e testar

Na raiz do site, biblioteca padrão:
    python3 -m labs.dijkstra-pesos.experiment
    python3 -m unittest discover -s labs/dijkstra-pesos -t .

Cinco testes: exemplo/counterexample BFS; todos os4096 grafos dirigidos simples de três vértices com arestas ausentes ou pesos0,1,3, para cada uma das três origens(12288 casos), comparando com referência independente Bellman–Ford por V−1 varreduras síncronas; zero, paralelas e frações; escala, componente inalcançável e preservação; contratos inclusive peso negativo inalcançável.

A referência de teste não é uma implementação de Bellman–Ford para uso geral com ciclos negativos; é apenas um oráculo independente para a família não negativa enumerada. Testes também conferem caminho/custo e ausência de finalização duplicada. Eles não substituem a prova ou validam um problema físico.

## Fontes e limites

Programa CCM0128: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0128, aberto em22/10/2026; ferramenta retorna captura de quatro semanas antes. Ativação01/01/2025 posterior à turma2024/1; versão ministrada não recuperada. Aprovação em2024/1 é a já registrada no panorama, sem nova inspeção do histórico.

Sedgewick e Wayne, Algorithms, quarta edição2011, exemplar privado: consulta textual parcial de §4.4 pp.646–647/PDF659–660 (relaxação), p.652/PDF665 (Dijkstra, não negatividade e fila indexada) e p.654/PDF667 (análise e variantes). O sumário localiza §4.4 p.638; isso não é leitura integral da seção. Não houve renderização nova de páginas ou distribuição do PDF. O site https://algs4.cs.princeton.edu/44sp/ retornou403; a consulta de corpo foi pelo exemplar autorizado.

O livro usa uma fila indexada; o código Python, a prova em prosa e o grafo desta aula são próprios. Nenhum código Java, tabela ou figura do livro foi reproduzido.

## Continuidade

Revisão pessoal: reconstituir as relaxações, explicar por que o peso final da aresta não basta como prioridade e resolver o caso com nova aresta A→D2. Depois: pesos negativos com outra referência, aplicações justificadas e demais grupos da disciplina. Novo roteiro curricular de sete etapas liga ADTs, ordenação, heap, símbolos/texto, grafos, aplicações e revisão pessoal. Nenhuma etapa ou aula equivale a domínio certificado.

Verificação do bloco:884 testes Python aprovados, incluindo os cinco testes novos de Dijkstra;507 estruturas MathML conferidas. Após ajustes de clareza e de título do módulo,12 testes de catálogo/correção repetidos e aprovados. Navegador: etapa5 do novo roteiro abriu por teclado e levou à aula; resposta5/6 aceita na questão7. Grafo e leitura móvel a390px inspecionados sem transbordamento horizontal ou erros de console observados; viewport restaurado. Prévia dijkstra-pesos-mobile.jpg. Nenhum modelo JavaScript alterado. Catálogo496 aulas/2826 exercícios em rascunho,287 introduções com até três seções. Próxima revisão pessoal: reconstituir a fila e explicar o papel da não negatividade. Próximo preparo global: conferir lacunas e fontes de Matemática III. Saldo semanal96%, parada operacional65%.
