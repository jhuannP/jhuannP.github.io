# Árvore de busca: altura, caminho e ordem de inserção

Material original em rascunho, referência temática 4.4 de Computer Science (2016). Conjunto de chaves inteiras; duplicatas são ignoradas. Sem valores associados, remoção, rotações ou balanceamento automático.

## Invariante e custo

Todo descendente esquerdo precisa ser menor que o nó; todo descendente direito, maior. Conferir só os filhos imediatos é insuficiente: uma chave pode respeitar o pai imediato e violar um ancestral.

Inserção/busca seguem um ramo a cada nó. O traçado conta nós visitados, não todas as operações Python de == e <. Com altura H em **número de nós**, são no máximo H nós visitados. Vazia tem H=0, um nó sozinho H=1. Outros textos podem contar arestas: declare a convenção antes de comparar resultados.

Para sete chaves, inserção crescente produz H=7; ordem [4,2,6,1,3,5,7] produz H=3. Procurar 7 visita [1,2,3,4,5,6,7] na primeira e [4,6,7] na segunda. Mesmo conjunto, formas e custos distintos.

Uma árvore binária de H níveis pode comportar até 2^H−1 nós. Assim, para n nós, H≥ceil(log₂(n+1)); essa é uma **cota inferior**, não garantia de altura pequena. Nesta árvore sem balanceamento H pode chegar a n. Uma ordem favorável não substitui um algoritmo balanceado.

Inserir n chaves crescentes visita aproximadamente 0+1+…+(n−1)=n(n−1)/2 nós antes de criar os novos nós: custo total quadrático. Percurso em ordem visita todos uma vez, O(n), mais espaço auxiliar dependente da altura. A implementação iterativa evita limite de recursão, sem eliminar o custo linear da cadeia.

## Executar

Salve tree.py e execute `python3 tree.py`. Salve também test_tree.py ao lado para rodar `python3 -m unittest discover -p 'test_*.py'`. Só biblioteca padrão; sem escrita de arquivos.

## Estudar e ensinar

1. Desenhe as árvores das três ordens; calcule altura antes de usar o site.
2. Busque 7 e depois 0. Explique caminho bem-sucedido e ausente.
3. Insira apenas um prefixo de cada ordem; lembre que os conjuntos parciais podem diferir. Compare formas para o mesmo conjunto completo.
4. Mostre um invariante global: raiz 10, esquerda 5, filho direito de 5 com chave 12 viola a raiz, apesar de ser maior que 5.
5. Derive a cota 2^H−1 e explique por que ela não dá H≤log₂(n).
6. Implemente busca/percurso iterativos e confronte com sorted(set(chaves)).
7. Como extensão futura, estude rotações e árvore balanceada; esta versão não as implementa.

Quatro testes verificam as 120 ordens de inserção de cinco chaves, regras globais e buscas; formas/caminhos conhecidos e duplicata; árvore vazia e cadeia de 1.200 nós sem recursão; entradas inválidas. São verificações do material, não prova de aprendizagem de Jhuann.

Revisão pessoal, exercícios graduais de rotações/remoção e avaliação com aluno permanecem pendentes.
