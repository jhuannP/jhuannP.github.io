# Listas, índices e matrizes sem perder o estado

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: expressões, atribuição e laços básicos. O laboratório retoma funções e testes.

## Uma sequência indexada

Uma lista mantém itens em ordem. Para três medições, os índices são 0,1,2. O índice -1 acessa o último item. Um índice fora do intervalo causa IndexError; não é um valor zero implícito. len fornece o tamanho.

medidas = [2.0, 4.0, 6.0]

## Dois nomes podem apontar para a mesma lista

Depois de b=a, os nomes apontam para o mesmo objeto. Alterar b[0] também é visível por a. a.copy() cria outra lista, mas a cópia é rasa: objetos internos ainda podem ser compartilhados. Use uma lista nova quando precisar preservar a entrada de um cálculo.

b = a.copy()

## Matrizes exigem atenção às linhas

Uma lista de listas pode representar uma matriz. [[0]*3 for _ in range(2)] cria duas linhas distintas. Já [[0]*3]*2 repete a referência à mesma linha: alterar uma posição aparece nas duas. Não confunda essa estrutura com uma matriz numérica otimizada.

A[i][j] = elemento da linha i, coluna j

## Uma matriz de listas precisa de um contrato

Listas de Python podem misturar tipos e ter linhas de tamanhos diferentes. Para representar uma tabela retangular m×n, escolhemos um contrato: m linhas de n colunas, ambas as contagens positivas. A[i] é a linha i; A[i][j] acessa a coluna j dessa linha. len(A) conta linhas, não todos os números. Em A=[[2,10],[4,14],[6,12]], temos três linhas e duas colunas.

m = len(A); n = len(A[0]), após validar a estrutura

## Índices e fatias respondem perguntas diferentes

Para uma linha com n itens, índices não negativos válidos vão de 0 a n−1. Os negativos contam a partir do fim; −1 é o último em lista não vazia. Já uma fatia inclui o início e exclui o fim. A[:] cria uma lista externa nova, mas guarda referências às mesmas linhas. Um índice fora do intervalo gera erro; uma fatia além do fim pode ser truncada.

[2,4,6][0:2] → [2,4]

## Reatribuir um nome difere de modificar o objeto

Se a=[2,4] e b=a, ambos designam a mesma lista. Fazer b[0]=9 muda essa lista e aparece por a. Em outro cenário, b=[9,4] apenas liga b a outra lista; a continua na anterior. a==b compara valores conforme o tipo; a is b pergunta se são o mesmo objeto. Duas listas distintas podem ter valores iguais. Não use valores numéricos de id como parte de um algoritmo de cópia.



## A cópia externa compartilha as linhas

Com A=[[1,2],[3,4]] e B=A.copy(), A is B é falso, mas A[0] is B[0] é verdadeiro. B[0][0]=9 altera uma linha compartilhada e aparece em A. Já B[1]=[-1,-1] substitui uma referência apenas na lista externa B. Para uma matriz de números imutáveis, [linha.copy() for linha in A] cria outras linhas e permite editar posições sem alterar A. Isso não é cópia profunda geral: células que contenham listas ou outros objetos mutáveis ainda podem compartilhar conteúdo.



## Repetir uma linha não constrói novas linhas

Em [[0,0]]*2, só uma linha foi criada: as duas posições externas guardam referência a ela. Uma compreensão como [[0,0] for _ in range(2)] cria uma linha a cada iteração. Compartilhar os próprios zeros, que são imutáveis, não é o problema; compartilhar uma linha mutável é. O desenho compara o estado depois de escrever 7 em uma posição.



## Percorra a dimensão que a pergunta exige

No exemplo de três linhas e duas colunas, a primeira coluna é 2,4,6 e a segunda é 10,14,12. Para a coluna j, some A[i][j] enquanto i percorre as m linhas; divida por m para obter sua média. Somar cada linha responde a outra pergunta. Colunas podem representar variáveis com unidades diferentes: somá-las indiscriminadamente pode não fazer sentido físico.

médias por coluna: [4,12]

## Centralize as colunas preservando a entrada

Centralizar uma coluna é subtrair de cada valor a média daquela coluna. Para A=[[2,10],[4,14],[6,12]], as médias são [4,12] e a saída é B=[[-2,-2],[0,2],[2,0]]. Cada coluna de B soma zero na aritmética exata, preservando sua unidade. Isso não normaliza a variância nem divide pelo desvio padrão. Aqui usamos toda a tabela; em aprendizado de máquina, quais dados podem estimar a média depende do protocolo de treino e validação.

B[i][j] = A[i][j] − média_da_coluna_j

## Construa a saída sem contaminar o que ainda será lido

O laboratório calcula as médias e depois cria uma linha nova para cada linha da saída. A tabela original permanece disponível para conferir o resultado. Em atualizações sucessivas de uma grade, misturar estado antigo e novo pode mudar o método numérico. Separar estruturas torna a escolha explícita, mas ainda precisamos definir o algoritmo e o modelo físico.



## Valide antes de calcular uma média

O laboratório exato aceita listas retangulares não vazias de int ou Fraction e recusa bool, float e células mutáveis. É uma escolha didática, não restrição geral das listas. [], [[]] e [[1],[2,3]] violam seu contrato. Medições reais exigem regras adicionais para valores ausentes, finitude, unidades, precisão e incerteza. Não atribua média zero à lista vazia nem corte linhas silenciosamente.



## Estime o custo e o limite de uma cópia

Validar a tabela, calcular médias e construir a saída percorre um número de posições proporcional a mn. A saída armazena mn referências numéricas, além das listas de linhas. Essa contagem trata operações aritméticas como unidades; o custo de Fraction também depende do tamanho dos inteiros. Listas não garantem representação compacta ou operações vetorizadas. NumPy e comparação de desempenho ficam para outro recorte.



## Teste valores e também relações entre objetos

B==resultado_esperado não detecta todo compartilhamento indevido. Confira os valores de A depois do cálculo, a identidade da lista externa e a independência de cada linha da saída. Modifique depois uma posição de B e verifique A. O laboratório inclui um contraexemplo de cópia rasa e uma entrada cujas duas linhas já são o mesmo objeto. O desafio anterior de centralizar uma lista continua como primeira prática.



## Exercícios e resoluções

1. Qual é o índice do último item de uma lista com 5 itens, usando índices não negativos?

   Resolução: Os índices vão de 0 até 4.

2. Após b=a, modificar b pode modificar o que vemos por a porque:

   Resolução: A atribuição compartilha a referência; não cria uma cópia.

3. Em A=[[2,10],[4,14],[6,12]], quantas linhas existem?

   Resolução: len(A)=3; cada linha tem duas colunas.

4. Na mesma tabela, qual é a média da segunda coluna?

   Resolução: (10+14+12)/3=12.

5. Depois de centralizar as colunas, quanto vale B[1][1]?

   Resolução: 14 menos a média 12 resulta em 2.

6. Em M=[[0,0]]*2, após M[0][1]=7, quanto vale M[1][1]?

   Resolução: As posições externas referem-se à mesma linha.

7. Em M=[[0,0] for _ in range(2)], após M[0][1]=7, quanto vale M[1][1]?

   Resolução: A compreensão cria uma linha distinta a cada iteração.

8. A=[[1,2],[3,4]]; B=A.copy(). A[0] e B[0] são o mesmo objeto?

   Resolução: A cópia externa mantém referências às mesmas linhas.

9. a=[2,4]; b=a; b=[9,4]. Quanto vale a[0]?

   Resolução: Reatribuir b não altera a lista anterior.

10. Copiar cada linha é uma cópia profunda geral, mesmo quando as células contêm listas?

   Resolução: Objetos dentro das células ainda podem ser compartilhados.

11. [[1],[2,3]] cumpre o contrato de tabela retangular desta aula?

   Resolução: As linhas têm tamanhos diferentes.

12. Subtrair a média também garante variância igual a 1?

   Resolução: Centralização não divide pelo desvio padrão.

## Fontes e limites

Consulta parcial em 22/10/2026: Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, §1.4, pp.106–108 (PDF127–129), matrizes como linhas e médias por linha/coluna. Título, autores, ©2017 e ISBN 978-0-13-407642-3 identificados nas páginas iniciais do exemplar privado. O arquivo e o programa USP usam 2016; copyright não é identificado aqui com ano de impressão. O livro usa Java; a semântica de listas em Python vem de fontes próprias da linguagem.

- [Programa CCM0118](https://uspdigital.usp.br/jupiterweb/jupDisciplina?sgldis=CCM0118): vetores, matrizes e textos; prática e depuração. Página recuperada pela ferramenta web em 22/10/2026, com rastreamento indicado há dois meses e ativação 15/07/2024. Não é a versão verificada da turma de 2023.
- [Python: estruturas de dados](https://docs.python.org/3/tutorial/datastructures.html): listas, cópia rasa e compreensões.
- [Python: copy](https://docs.python.org/3/library/copy.html): atribuição, cópia rasa e profunda.
- [Python FAQ: lista multidimensional](https://docs.python.org/3/faq/programming.html#how-do-i-create-a-multidimensional-list): repetição de referências versus linhas novas.

Consultas parciais. Nenhuma página, figura, exercício ou solução do livro foi distribuída. A documentação /3 consultada se apresentou como 3.15.1; o código foi executado no Python local, sem instalar ou atualizar o interpretador.

## Reprodução

Na raiz do site, execute python3 -m labs.matrizes-referencias.experiment e python3 -m unittest discover -s labs/matrizes-referencias -t .

O contrato do laboratório é uma tabela retangular não vazia com int/Fraction, sem bool. Não há importação de dados reais ou afirmação de resultado científico. Valores ausentes, ponto flutuante e células mutáveis exigem outro contrato; copiar linhas não resolve todo grafo de objetos.

## Verificação de 22/10/2026

Cinco testes novos aprovados, incluindo enumeração de 840 tabelas. Suíte global: 834 testes Python aprovados. No navegador, respostas 7 e 0 aceitas; desenho inspecionado em 390 px sem rolagem horizontal e sem erros de console observados. Revisão de Jhuann pendente.
