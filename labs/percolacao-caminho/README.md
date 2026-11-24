# Percolação: reconstruir um caminho

Extensão original assistida por IA para revisão pessoal. Preserva o laboratório anterior de ensemble em ../percolacao/; não modifica experiment.py, suas saídas ou pacote ZIP. Caminho por BFS é novo exemplo Python, não transcrição da implementação recursiva Java do livro.

Grade retangular não vazia com bool ou inteiros0/1; quatro vizinhos, sem diagonais, bordas abertas, todas as origens abertas da primeira linha com distância0. Objetivo: qualquer célula da última linha. BFS com deque e marcação ao descobrir; guardar pai e distância, reconstruir a partir do primeiro alvo retirado. Cada pai tem distância uma unidade menor: cadeia termina numa origem. Fila processa distâncias não decrescentes, de modo que a primeira descoberta já usa menor número de arestas. Outro desempate pode retornar outro caminho de mesmo comprimento.

Uma linha aberta atravessa com uma célula e zero arestas. None representa ausência de travessia; não equivale a caminho de comprimento zero. Descobertos/retirados são apenas a busca até a parada, não todos os sítios abertos ou todos os alcançáveis. Custo de validar/explorar R×C é O(RC) no modelo usual de operações de dicionário em tempo esperado constante; espaço O(RC). Limite operacional30×30. Não inferir tempo físico, vazão, condutividade ou probabilidade de uma grade.

```
python3 -m unittest discover -s labs/percolacao-caminho -t .
python3 labs/percolacao-caminho/path.py
```
Quatro testes:682grades1..3por1..3 contra relaxação síncrona independente e booleano anterior;integridade de caminho/entrada;fixtures/empates;abrir sítios não destrói nem alonga o menor caminho;contratos. A enumeração pequena testa código, não substitui a prova geral de BFS.

## Referências — consulta parcial em28/10/2026

- Júpiter CCM0118: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0118 — reaberto,ativação15/07/2024;programa efetivamente ministrado em2023/2 não recuperado. Conectividade é estudo de caso editorial de programação, não item explícito da ementa ou experiência pessoal certificada.
- Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, exemplar privado©2017,ISBN978-0-13-407642-3: §2.4 pp.300–302/PDF321–323 consultados textualmente em28/10/2026 para representação,quatro vizinhos e decomposição modular. Edição do cadastro indicada2016,sem presumir data de impressão pelo copyright. Sem nova inspeção visual ou leitura integral;figuras/exercícios não reproduzidos,PDF não distribuído. Página web24percolation recusou acesso403,não lida.
- Python collections.deque: https://docs.python.org/3/library/collections.html#collections.deque — consulta parcial para fila nas extremidades,append/popleft. Fonte aberta redireciona à documentação corrente;programa usa somente operações básicas da biblioteca padrão e foi executado localmente.

Material e provas didáticas próprias;revisão de Jhuann pendente. Modelagem física,limiar crítico,grandes redes ponderadas e análise experimental fora do recorte.
