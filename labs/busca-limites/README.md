# Busca binária: contrato, limite inferior e contagem

22/10/2026. Rascunho original para revisão pessoal, aprofundando `busca-binaria`. Preserva IDsbb1/bb2/bb3, exemplo original e painel inclusivo `binarySearch`. Novo painel `binaryLowerBound` é adicional, não troca silenciosa de algoritmo.

## Referências consultadas

- Sedgewick/Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar autorizado do acervo nomeado2016, com identificação editorial já registrada como pendente. Corpo §4.2, pp.538–539/PDF559–560, consulta parcial por texto em22/10/2026: busca em sequência ordenada, intervalo semiaberto e contrato de alguma ocorrência. Não foi traduzido o programa Java ou cliente do livro. Extração incluiu537/540, sem usar a busca contínua de função/inverseCDF ou filtro de entradas como conteúdo desta unidade. Não se afirma leitura integral ou equivalência de edições.
- [Python — bisect](https://docs.python.org/3/library/bisect.html), consulta direta parcial22/10/2026: contrato de `bisect_left`, partição antes de iguais, comparação `<` e distinção entre busca e inserção. São APIs de referência; implementação didática própria em Python. A documentação consultada é a versão corrente do site, não afirmação de versão do interpretador local.
- Página oficial dos autores para Python4.2 retornou403. Não foi usada como leitura direta confirmada, nem contornada. O recorte do livro local e a documentaçãoPython sustentam o material.

O tópico permanece parcial no programa CCM0118: uma prova para estes algoritmos não cobre toda correção/complexidade ou experiência de depuração. Nenhum PDF, figura ou exercício privado distribuído.

## Dois contratos e dois intervalos

`busca_binaria`: limites inclusivos, retorna algum índice ou−1. O exemplo11 em [1,3,5,7,9,11,13,15] consulta os meios3/5, duas sondagens, mas realiza três comparações primitivas entre chave/elemento no código com igualdade e depois menor:7==11,7<11,11==11. A pergunta bb2 foi esclarecida como número de sondagens (resposta2 preservada); bb4 pergunta pelas três comparações primitivas.

`lower_bound`: núcleo não validado com intervalo semiaberto [lo,hi). Retorna p entre0 e n, particionando valores em menores que o alvo à esquerda e maiores/iguais à direita. Para presença, verificar p<n antes de a[p]==alvo; primeira ocorrência ou−1 é outro retorno derivado. Duplicatas: [1,3,3,3,5,7,7,9], alvo3 → alguma ocorrência3 no algoritmo original; limite inferior1 e primeira ocorrência1. Alvo4 → posição4 e ocorrência−1; alvo16 → posição8, sem acessar a[8]. Lista vazia → posição0 e ocorrência−1.

## Invariante e término

0≤lo≤hi≤n; a[:lo]<alvo; a[hi:]≥alvo. A fronteira p está em[lo,hi], incluindo hi: não é necessariamente um elemento ativo em[lo,hi). Se a[m]<alvo, lo=m+1; caso contrário hi=m. A ordem preserva as condições de prefixo/sufixo. No segundo ramo m continua possível como fronteira.

Comprimento L>0 cai para no máximo⌊L/2⌋. Inteiro não negativo estritamente decrescente prova término; lo==hi identifica p. Para n>0, no máximo⌊log₂n⌋+1 comparações ordenadas; para n0, zero. Alguns caminhos atingem o limite, outros não. Soma-se uma comparação de igualdade se p<n quando a pergunta é presença/primeira ocorrência. Não entram nessas contagens guarda do laço, índices, aritmética ou validação.

## Custo do cliente e hipóteses

Comparações com custo unitário e acesso direto são hipóteses. Núcleo iterativo: O(log(n+1)) comparações, O(1) palavras auxiliares; isso não é O(1) bits para qualquer tamanho de índice. Chaves longas/inteiros extensos podem tornar comparação não unitária. Cliente `trace` valida tipos e ordem em O(n), e registra O(log(n+1)) linhas. Assim o cliente completo não tem custo total apenas logarítmico. Não ordena ou modifica a entrada. Inserção em lista é operação separada, tipicamente linear. Sem NaN/comparador inconsistente/mutação concorrente no contrato.

## Executar

```sh
python3 labs/busca-limites/experiment.py
python3 -m unittest discover -s labs/busca-limites -t .
```

Quatro testes novos:3465combinações de listas não decrescentes/alvos contra contagem linear e `bisect_left`; invariantes e progresso em68cenários das quatro listas; pior caso para129tamanhos0..128 e8514buscas, instrumentação separada; contratos e exemplo original. Lista fora de ordem usada deliberadamente como contraexemplo da pré-condição, não como caso válido do núcleo.

136referências (68cenários com etapa inicial/final solicitada) comparam todos os retornos, linhas e contagens JS/Python. Pedido de etapa8 é limitado ao fim do traço; lista vazia/unitária e troca de lista ajustam o controle. Valores do painel pequenos e exatos em Number; sem benchmark ou introspecção de execução real.

## Próximas lacunas

Revisão pessoal pendente. Busca por intervalos/right bound, comparadores, busca em arquivos/estruturas de acesso não constante e projetos de uso ainda faltam. Provas de ordenação e depuração geral seguem parciais; alternar com outras disciplinas antes de aprofundar indefinidamente esta unidade.
