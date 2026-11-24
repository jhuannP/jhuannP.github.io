# Mínimos quadrados discretos por QR

Rascunho original, pendente da revisão de Jhuann. Exemplos adimensionais e sintéticos. A experiência não é um resultado pessoal de pesquisa.

## Fontes consultadas em 16/10/2026

- Burden/Faires/Burden, tradução da 10ª edição: sumário e páginas impressas 557–558 (PDF 570–571), início de 8.1, lidos visualmente. Critério de ajuste linear e equações normais; não houve leitura integral da seção ou do capítulo de Householder. A 7ª edição indicada no programa oficial não é presumida equivalente em páginas e exercícios.
- [LAPACK Users Guide: Linear Least Squares](https://www.netlib.org/lapack/lug/node27.html): formulação, posto completo e distinção entre métodos QR e tratamento de posto deficiente.
- [SciPy lstsq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html): contrato de mínimos quadrados, posto efetivo e métodos disponíveis. O laboratório não usa SciPy/LAPACK.

Texto, identidades do experimento, dados, exercícios, gráfico e código próprios. Nenhuma figura ou exercício da fonte reproduzido; nenhum livro privado copiado ao protótipo.

## Algoritmo e reprodução

`qr_fit(A,y)` usa reflexões de Householder sem pivotamento de colunas. Requer matriz real finita m>=p, pequena e de escala moderada, e vetor compatível. Retorna R, Q transposto, coeficientes, previsões, resíduos, SSE e Aᵀr; recusa uma cauda de coluna abaixo de 10^-12 vezes a maior norma de coluna original. Não determina posto por SVD e não retorna mínima norma. Os limites de overflow/subfluxo para entradas extremas não são tratados como numa biblioteca de produção.

`normal_fit` é somente um comparador para os dados curados deste roteiro: forma AᵀA e usa eliminação com pivotamento de linhas e limiar relativo à própria matriz. Os limiares de QR e equações normais têm escalas distintas; não são testes equivalentes de posto. Recusa normal em ε=10^-8 não prova dependência exata da matriz original.

Na raiz: `python3 -m unittest discover -s labs/minimos-quadrados-qr -t .`. Os quatro testes verificam ortogonalidade e fatoração, solução fechada, identidade de mínimo, mudanças de base, pesos positivos e recusa de dependência exata. `reference.json` tem 18 configurações distintas para comparação JS/Python; essa comparação não substitui as referências analíticas independentes.

## Dois conjuntos separados

O exemplo resolvido preservado usa (0,1),(1,2),(2,4), com intercepto 5/6, inclinação 3/2 e SSE 1/6. A ordem na base [1,x] é [intercepto,inclinação].

A demonstração usa cinco x: -2,-1,0,1,2. Os dados são y=1+x/2+x²/2, adicionando δ somente em x=0. δ é uma perturbação determinística, não desvio-padrão ou ruído amostrado.

Na base quadrática a referência fechada é β=[1+17δ/35,1/2,1/2-δ/7], SSE=18δ²/35. Na base de reta: β=[2+δ/5,1/2], SSE=7/2-2δ+4δ²/5. Verifique por substituição e ortogonalidade, sem repetir Householder.

## Experimento com as bases

1. Compare reta e quadrática, com δ=0 e depois δ=1. Menor SSE no treino não valida generalização.
2. Escolha a base acoplada [1,x,x+εx²]. Para ε>0 ela gera o mesmo espaço das quadráticas; os coeficientes são [β0,β1-β2/ε,β2/ε].
3. Os níveis 0,1,2,3 correspondem a ε=1,10^-4,10^-8,0. Observe coeficientes grandes e cancelamento nas previsões. QR não elimina o condicionamento da parametrização.
4. Em ε=0 há duas colunas iguais. Previsões ótimas ainda são únicas no espaço das retas; coeficientes não são. O laboratório interrompe sem inventar coeficientes ou alegar ausência de ajuste.
5. Pesos positivos podem ser aplicados multiplicando cada linha e y por sqrt(w). Os controles usam pesos iguais; teste ponderado usa dados exatamente lineares.

## Ainda pendente

Pivotamento de colunas, SVD, solução de mínima norma, matrizes grandes/esparsas, mínimos quadrados não lineares, análise de erro geral, seleção de modelo e inferência estatística. O tópico e a disciplina continuam parciais. Código gerado e testes não comprovam competência pessoal sem revisão e demonstração de Jhuann.

## Verificação independente adicional

`verify_svd.py` é opcional e requer NumPy já instalado. Compara previsões e posto das 18 configurações com `numpy.linalg.lstsq`, via SVD, sem usar o algoritmo QR do laboratório como referência. Executado no runtime local em 16/10/2026: maior diferença absoluta nas previsões 5,303795447275661e-8, abaixo do limite declarado de 2e-7. Não é uma garantia para outras matrizes ou para coeficientes mal condicionados. Não instala dependências.
