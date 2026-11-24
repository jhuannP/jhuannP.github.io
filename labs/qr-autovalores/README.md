# QR explícito e quatro comportamentos espectrais

Material didático original em rascunho para revisão de Jhuann. Complemento do percurso: QR não aparece explicitamente no programa oficial consultado de Computação IV. Não comprova conteúdo cursado ou resultado da IC.

## Fontes consultadas em 16/10/2026

- Burden/Faires/Burden, Análise Numérica, tradução da décima edição: sumário PDF 13 confirma 9.5; páginas impressas 671–673 (PDF 683–685) lidas visualmente. Similaridade, contexto simétrico/tridiagonal e rotações. Leitura parcial, não capítulo integral ou implementação completa do algoritmo do livro. Não se presumiu um deslocamento fixo entre paginações.
- [LAPACK Users’ Guide, problemas não simétricos](https://www.netlib.org/lapack/lug/node31.html): forma de Schur real com blocos 1×1/2×2 e diferença entre vetores de Schur/autovetores.
- [LAPACK, etapas computacionais](https://www.netlib.org/lapack/lug/node50.html): Hessenberg, Schur e cálculo de autovetores. Não executamos o solver LAPACK no painel.
- [MIT 18.335, soluções do conjunto 3](https://math.mit.edu/~stevenj/18.335/pset3sol-s15.pdf): trechos do problema 2 usados para identidade de similaridade e rotações. Nenhuma solução reproduzida; não se toma a menção abreviada de convergência como garantia sem condições para toda matriz hermitiana.

Quatro casos, exercícios, derivação racional, código e gráficos próprios. Nenhum PDF privado, figura ou exercício protegido servido.

## Convenção e casos

QR real 2×2 por rotação, R11 não negativo. Primeira coluna zero usa Q=I. R21 é fixado em zero após a rotação e a reconstrução QR−A é conferida. Atualização A seguinte=RQ; U acumula Q na ordem. Sem deslocamentos, deflação, Hessenberg, aritmética complexa ou seleção adaptativa de parada.

1. [[2,1],[1,2]]: autovalores 3 e 1, aproximação diagonal. Referência independente: A11=(3·9^k+1)/(9^k+1), A22=(9^k+3)/(9^k+1), A12=A21=2·3^k/(9^k+1).
2. [[0,1],[1,0]]: espectro ±1; na convenção adotada alterna sinais em ciclo de dois passos, sem redução da subdiagonal.
3. [[0,−1],[1,0]]: espectro ±i; mantém bloco real 2×2. Diagonal zero não é o espectro; bloco complexo não precisa ser diagonal real.
4. [[2,6],[0,1]]: já triangular, espectro 2 e 1. U=I não é uma base inteira de autovetores; a segunda coluna tem resíduo não zero.

## Diagnósticos e verificações

Na raiz: `python3 -m unittest discover -s labs/qr-autovalores -t .`.

Quatro testes: reconstrução/ortogonalidade em 81 matrizes inteiras, incluindo singulares; referência racional em 21 passos do caso positivo; invariantes e três contraexemplos em 84 estados; domínio e primeira coluna nula. Vinte configurações JS/Python em `reference.json`.

Resíduos: ‖A0U−UAk‖F/‖A0‖F, ‖UᵀU−I‖F, reconstrução QR relativa e resíduo de A0U−Udiag(Ak). O último só avalia a tentativa de usar colunas de U com a diagonal como autovetores; pode ser grande numa triangular correta. Curvas mostram subdiagonal e termos fora da diagonal, normalizados por ‖A0‖F. Escala linear não prova zero; notação científica preserva valores pequenos.

## Pendências

Provas gerais com hipóteses de convergência, deslocamentos/deflação, métodos implícitos e estruturados, solvers robustos para matrizes grandes, sensibilidade de espectro e autovetores. Resíduo pequeno não é garantia universal de erro direto pequeno. Revisão pessoal pendente; curso continua incompleto.
