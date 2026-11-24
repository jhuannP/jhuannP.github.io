# Laboratório de redes: distâncias e agrupamento

Rascunho original, referência temática 4.5 de Computer Science (2016). Código Python sem dependências; grafos sintéticos não dirigidos, simples e sem pesos.

## Modelo e medidas

O anel tem 8–40 vértices e liga cada um aos dois vizinhos mais próximos em cada direção. Grau inicial 4, número inicial de arestas 2n. Atalhos são pares distintos ainda não ligados. Ordenamos candidatos lexicograficamente, embaralhamos Fisher–Yates e selecionamos um prefixo; assim uma mesma semente gera redes aninhadas ao aumentar o número de atalhos.

Gerador compartilhado: s←(1664525s+1013904223) mod 2³², u=s/2³². É um gerador didático, não criptográfico e sem validação estatística para pesquisa. A semente registra a construção, não torna a amostra representativa de redes reais.

L é a média de distâncias por arestas entre todos os pares distintos, calculadas por BFS a partir de cada origem. Grafo desconectado retorna L=None, evitando tratar distância ausente como zero ou excluir pares silenciosamente. [Definição de distância média no NetworkX](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.average_shortest_path_length.html).

Agrupamento local cᵤ é a fração dos pares de vizinhos de u que têm ligação entre si: 2Tᵤ/[kᵤ(kᵤ−1)]. Definimos zero quando kᵤ<2. C é a média aritmética desses coeficientes, **não** a transitividade global ponderada por triplas. [Definição de agrupamento no NetworkX](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.clustering.html). Código próprio; não usa nem instala NetworkX.

## Referências que podemos conferir

No anel de quatro vizinhos, para n≥8, cada vértice tem três ligações entre seus seis pares de vizinhos: cᵤ=3/6=0,5. Sua distância de 0 a j é ceil(min(j,n−j)/2), portanto L é a média desses valores para j=1..n−1. Num grafo completo, L=1 e C=1.

Ao acrescentar arestas mantendo as anteriores, nenhum menor caminho piora; L não aumenta. C pode subir ou cair, porque o número de pares possíveis de vizinhos também muda. O experimento aumenta a quantidade de arestas/graus: isso é um fator de confusão ao comparar modelos. Não representa religação preservando o número de arestas de Watts–Strogatz e não demonstra, sozinho, classificação de pequeno mundo.

## Executar e explorar

Salve network.py e rode `python3 network.py`: compara 0,2,4,8,12 atalhos em n=12 e semente 42. Com test_network.py ao lado, rode `python3 -m unittest discover -p 'test_*.py'`. Não grava arquivos.

1. Derive L e C do anel antes de adicionar conexões.
2. Compare redes aninhadas na mesma semente: confira que L não aumenta.
3. Repita sementes e tamanhos. Registre L, C e número de arestas, sem escolher só um resultado favorável.
4. Explique por que o comprimento das linhas desenhadas não é o peso das arestas.
5. Experimente um vértice isolado fora do gerador e confira L=None.
6. Para aprofundar, construa ensemble com várias sementes e controles de tamanho/grau; só então discuta modelos de pequeno mundo com referências adequadas. Esse estudo comparativo ainda não está concluído.

Quatro testes comparam BFS com Floyd–Warshall independente nos 64 grafos simples de quatro nós; verificam anel, clique e caminho; reprodução, ausência de arestas repetidas e monotonicidade de L em 117 configurações; contratos. Revisão pessoal e avaliação com aluno continuam pendentes.
