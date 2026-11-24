# Taylor: cota pontual, uniforme e avaliação numérica

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Teste: python3 -m unittest labs.taylor-resto.test_experiment.

Exp em zero, N=0..12, raio 0,25..1, x=ρu, u∈[−1,1].
Cota no ponto Bp=e^max(0,x)|x|^(N+1)/(N+1)!.
Uniforme em [−ρ,ρ]: B=e^ρρ^(N+1)/(N+1)!.
O mínimo procurado satisfaz B<=10^(-p), p=2..6; não é o mínimo pelo
verdadeiro erro. Em ρ=1/p=4, N=7 é o primeiro aceito por esta cota.

O resto desenhado soma 81 termos da cauda, evitando subtração de valores
próximos. Essa estimativa não é prova nem aritmética intervalar certificada.
A cota analítica limita truncamento matemático, não todo erro de máquina.
Com |x|<=1, a razão entre termos absolutos da cauda cai rapidamente;
ainda assim não se declara precisão arbitrária ou exatidão da cauda finita.
Normalização por B muda com grau/raio: compare valores absolutos na tabela.

Quatro testes: 120 estados contra Decimal.exp com 80 dígitos e polinômio
avaliado independentemente; cotas com Decimal, sinal e ponto zero;
16 integrais do resto por Simpson com refinamento 128→256;
20 buscas de grau com verificação Decimal do escolhido e do anterior;
razão de cotas, coeficiente racional 221/200 e contratos.
As 120 referências Decimal também verificam JavaScript e suas cotas.
Exercícios originais c2-taylor-n/c preservados, sem duplicar a demonstração.

Fontes parciais em 16/10/2026:
- Apostol, Calculus I, segunda edição, Wiley 1967, 7.6/7.7,
  pp. impressas 280 e 283 (PDF 300 e 303). Página 280 inspecionada
  visualmente. Extração do exemplar gerou avisos em outras páginas;
  fórmulas usadas conferidas no trecho e página renderizada.
- [OpenStax 6.3](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series),
  definições e teorema 6.7. A aula adota hipótese suficiente C^(N+1),
  usa argumento integral próprio e não reproduz exemplos ou exercícios.

Visual: gráfico de erro ampliado por normalização, curva azul, envelope
pontual preto tracejado, ±1 cinza pontilhado, tabela dos valores absolutos.
Interação: raio muda o intervalo; grau muda aproximação/cota; tolerância
muda decisão; ponto destacado não muda garantia uniforme. Sem animação
que confunda grau com tempo. Revisão pessoal, outras funções, centros,
aplicações e análise de arredondamento continuam pendentes.
