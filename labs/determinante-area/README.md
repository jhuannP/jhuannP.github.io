# Determinante e área orientada

Material original em rascunho para revisão de Jhuann. Não são notas pessoais importadas ou evidência de domínio atual.

## Fontes consultadas em 16/10/2026

- [MIT OCW, Calculus with Applications, texto 4.1](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter04/section01.html): geometria e propriedades definidoras.
- [MIT OCW, texto 32.4](https://www.ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter32/section04.html): propriedades, operações e composição. Consulta parcial, sem reprodução de exercícios ou figuras.

A bibliografia oficial e os livros já identificados no acervo continuam no mapa de Matemática III/Álgebra linear. Não houve nova leitura desses exemplares neste bloco; fontes online indicadas apoiam o texto original.

## Modelo e figura

A=s[[1,k],[0,t]], s de 0,25 a 2, k e t de −2 a 2. Colunas opcionalmente trocadas. Determinante ±s²t; área s²|t|. A imagem do quadrado unitário tem vértices ordenados 0,u,u+v,v. O contorno cinza tracejado é o quadrado de referência; azul a imagem, seta azul u e segmento escuro tracejado v. A janela se ajusta à figura, com escala igual nos dois eixos; compare áreas pelo quadrado unitário e pelos valores, não apenas pelo tamanho em pixels. Sem unidade física atribuída.

Cisalhamento não muda área; altura negativa inverte orientação; t=0 colapsa a figura; troca de colunas mantém a região e inverte a ordem. A família não representa toda matriz 2×2 nem calcula condicionamento. Determinante pequeno não prova má condição: 10⁻⁸I tem κ₂=1. Determinante 1 não garante boa condição: diag(10⁸,10⁻⁸) tem κ₂=10¹⁶.

## Verificação

Na raiz: `python3 -m unittest discover -s labs/determinante-area -t .`.

Quatro testes: 120 configurações com aritmética racional, área da borda e base/altura; composição em 6561 pares de matrizes inteiras e operações de coluna/escala; diagonais de condição conhecida e cancelamento Decimal/float; orientação, degeneração e domínio. `reference.json` contém 54 configurações JS/Python. Conferir dois algoritmos não prova um teorema geral; a justificativa conceitual está na aula.

O exemplo Decimal usa string 1.000000000000000001 com 50 dígitos de precisão e det exato 10⁻¹⁸; convertido a float, esse valor pode arredondar para 1 e perder a diferença. A precisão extra não restaura dados já arredondados. O painel usa uma família pequena e controlada, sem teste genérico de posto por limiar.

## Pendências

Multilinearidade e unicidade em dimensão geral, expansão por cofatores, pivoteamento e log-determinantes, orientação de bases gerais, volumes 3D, Jacobianos com hipóteses de mudança de variáveis e condicionamento por SVD. Curso continua parcial e aguarda revisão pessoal.
