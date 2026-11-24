# Tabela hash: colisões, carga e crescimento

Laboratório original em rascunho, referência temática do eixo 4.4 de Computer Science (2016). Tipos didáticos em Python, sem dependências. Não é uma implementação do dict interno do Python.

## Contrato

HashTable recebe strings como chaves e valores arbitrários, incluindo None. put atualiza se a chave já existe; isso não altera n nem provoca crescimento. get/delete de chave ausente levantam KeyError. Cada balde é uma lista de pares, e a consulta compara a chave inteira. A capacidade inicial é pelo menos 2; limite de carga entre 0,5 e 2. Encadeamento permite carga maior que 1, pois um balde admite vários pares.

Nova inserção cresce se n+1>limite×C: dobra C, calcula novamente h(chave) mod C e transfere todos os pares. Apenas copiar o vetor de baldes deixa pares em índices errados. Remoção não encolhe; memória depende da maior capacidade alcançada. Snapshot copia a estrutura dos baldes, preservando referências dos valores; não é cópia profunda de objetos arbitrários.

## Hashes e limites

- Soma de códigos Unicode: expõe colisões, pois permutações da mesma palavra têm a mesma soma.
- Polinomial base 31, acumulador módulo 2³²: distingue ab de ba neste exemplo, sem garantir ausência de colisões ou segurança.
- Constante zero: caso adversarial que reúne todos no mesmo balde, mesmo com redimensionamento.

Com n pares e C baldes, α=n/C é comprimento médio dos baldes, não a proporção de baldes não vazios. Sob uma hipótese de distribuição uniforme, custo esperado de busca é O(1+α) comparações. Essa hipótese não é garantida pelos hashes didáticos. Pior caso percorre n pares. Hash de chave com L caracteres custa O(L); comparar strings também pode depender de L. Portanto custo constante pressupõe controlar também comprimento/custo das chaves.

Redimensionar é O(n+C) nesta representação, porque percorre os baldes e transfere os pares. O número de transferências cresce geometricamente; isto limita o custo de crescimento numa sequência. Ainda assim, colisões podem produzir custo quadrático de comparações ao inserir muitas chaves num único balde. Contador migrated não mede todas as comparações, caracteres, alocações ou tempo.

## Executar

Salve table.py e rode `python3 table.py`. Para testes, salve test_table.py ao lado e execute `python3 -m unittest discover -p 'test_*.py'`. Operações não escrevem arquivos.

## Roteiro

1. Calcule os índices de ab, ba e ad com C=4. Mostre a colisão ab/ba.
2. Insira x com limite 0,75. A capacidade muda para 8; ad precisa mudar de índice 1 para 5.
3. Atualize ab. Confirme que n e capacidade não mudam.
4. Apague ba. Mostre que ab permanece consultável.
5. Compare limites 0,75 e 2. Explique memória, comprimento dos baldes e crescimento, sem prometer latência a partir desse traçado curto.
6. Use hash constante; depois as 24 permutações de abcd com hash por soma. Explique por que crescer não melhora essa colisão.
7. Implemente o contrato sem copiar a referência; compare milhares de operações com dict. Teste chave vazia, Unicode, None, ausentes e atualização.
8. Escreva a diferença entre custo amortizado do crescimento e custo esperado da busca. São argumentos diferentes.

Cinco testes verificam colisões/atualização/remoção, rehash após crescimento, 9 mil operações contra dict em três hashes/três limites, caso adversarial de 24 permutações e contratos/independência do snapshot. Os traçados interativos/Python usam a mesma especificação; isso não certifica formação.

Pendentes: revisão pessoal, desafios graduais de implementação, encolhimento com histerese e comparação sistemática de distribuições com dados maiores. Os exemplos são sintéticos e não servem para hash criptográfico.
