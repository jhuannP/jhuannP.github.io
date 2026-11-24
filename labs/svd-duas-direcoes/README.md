# SVD — duas direções, sensibilidade e truncamento

Família original A_η com linhas(9/5,12/5),(−4η/5,3η/5),(0,0),0≤η≤3. Direções de entrada v1=(3/5,4/5),v2=(−4/5,3/5), ortonormais; saída nos dois primeiros eixos de R³. Valores singulares3,η; parâmetros e componentes adimensionais. Sem algoritmo geral de SVD.

Paraη>0, a solução de mínimos quadrados é(b1/3)v1+(b2/η)v2; paraη=0 escolhe a solução de menor norma. O truncamento também zera a segunda componente quandoη>0, introduzindo viés. A comparação de ruído é sintética, com verdade conhecida no exercício, e não decide um corte universal.

## Fontes parcialmente consultadas —27/10/2026

[LAPACK Users’ Guide, SVD](https://netlib.org/lapack/lug/node32.html): definição, dimensões, ordenação e relações entre vetores. [LAPACK Users’ Guide, LLS](https://netlib.org/lapack/lug/node27.html): mínimos quadrados, posto e norma mínima. Conteúdo conceitual consultado; não se executaram drivers ou reproduziram tabelas.

[MIT18.06, Lecture29](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-29-singular-value-decomposition/): somente descrição pública lida; vídeo não assistido e transcrição integral não acessada. Não presume equivalência entre gravação1999, edição do curso2010 e livro indicado2016. Nenhum livro privado relido neste bloco.

A prova de existência via AᵀA, a família, a prova de optimalidade de posto1 restrita à família, os exemplos e código foram desenvolvidos localmente. Não reproduzimos figuras ou exercícios. Formar AᵀA na demonstração não é recomendação de algoritmo numérico em float.

## Código e verificação

Biblioteca padrão, Fraction; aceita int/Fraction e rejeita bool/float. `matrix`, `apply`, `pseudoinverse` e `fit` só representam essa família. `condition` retorna None na perda de posto: não significa inexistência de pseudoinversa; a recuperação da entrada inteira deixa de ser identificável. O truncamento não é apresentado como solução de mínimos quadrados completa quandoη>0.

Na raiz: `python3 -m unittest discover -s labs/svd-duas-direcoes -t .`.

Verificações: direções e Gram, reconstrução, quatro identidades de Moore–Penrose por multiplicação independente, mínimo e norma mínima, erro da aproximação de posto1, caso de ruído/viés e contratos. Provas estão no texto; amostras não substituem a demonstração geral.

Próxima revisão de20min: conferir ação em v1/v2 e mínimo para b=(3,1,2). Depois explicar por que resíduo zero pode coexistir com erro de entrada maior e por que truncamento também perde informação. Algoritmos gerais, limiar com dados, matrizes complexas, leitor de tela, Windows real e revisão pessoal pendentes.

Conferência em27/10/2026: cinco testes locais e14 do catálogo aprovados;819 estruturas MathML globais. Interface390px: erro da entrada rejeitou0 e aceitou2 pelo Enter; distinção de corte/viés aceita. Figura inspecionada, largura390px e console sem erros; captura na raiz `svd-duas-direcoes-mobile.jpg`.
