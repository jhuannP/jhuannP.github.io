# Recursão, pilha e reutilização

Material original em rascunho, 16/10/2026. Execute experiment.py com Python 3.
Na raiz do protótipo: python3 -m unittest labs.recursao.test_experiment.

O painel usa n de 0 a 10, base zero, execução sequencial e passo lógico.
Cada chamada gera entrada e retorno; fim mostra pilha vazia. O retorno é
registrado antes de desempilhar. Quadros externos mantêm seus argumentos.
trace copia quadros para permitir voltar: esse histórico é custo do
visualizador, não do algoritmo original.

Fatorial: n+1 chamadas, n+1 de pico, n multiplicações.
Potência reutilizada: b+1 chamadas/pico, b+popcount(n) multiplicações;
b=n.bit_length(). Conta inclusive fatores 1. n=0 tem b=0.
Não mede tempo nem bits. Expoente zero retorna 1, inclusive para base zero,
pela convenção declarada de produto vazio.

Quatro testes: fatorial versus math.factorial, soma versus fórmula fechada,
726 potências versus pow, replay independente dos eventos em pilha explícita,
contagens por bits, snapshots, fim vazio e contratos. O painel permanece
na faixa exata de Number; Python usa inteiros de precisão arbitrária.

Fontes parciais, consulta em 16/10/2026:
- Computer Science, exemplar nomeado 2016 do acervo, seção 2.3, páginas
  impressas 264–265 e 281 (PDF 285–286 e 302). Página 264 inspecionada
  visualmente, em Java. O arquivo contém material de versões distintas;
  não se generaliza a paginação. Identificação editorial em reconciliação.
- [Página oficial dos autores, Python 2.3](https://introcs.cs.princeton.edu/python/23recursion/):
  consulta por busca indexada; abertura direta retornou 403.
- [Python sys.getrecursionlimit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit):
  limite da pilha, sem mudar a configuração.

Exemplos, exercícios e visualização próprios, sem reprodução do livro.
Prática e revisão pessoal, outros padrões recursivos, integração adaptativa
e análise sistemática de custo em bits continuam pendentes.
