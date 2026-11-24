# Hermite: escala, regularidade e dados

Expansão original de `hermite-cubico`, mantendo as três primeiras seções, IDs, exemplo e código anteriores. Rascunho para revisão de Jhuann, sem comprovação de domínio pessoal.

## Existência e unicidade

h=b−a>0, t=(x−a)/h. As quatro bases são H00=2t³−3t²+1, H10=t³−2t²+t, H01=−2t³+3t² e H11=t³−t². Suas combinações H00*y0+H10*h*d0+H01*y1+H11*h*d1 satisfazem os valores e derivadas em x. A multiplicação por h vem de dp/dt=h dp/dx. Cada base pode ser derivada impondo quatro condições aos seus coeficientes. Existência é dada pela fórmula; para unicidade, diferença de duas soluções de grau≤3 tem raízes duplas a,b e seria divisível pelo polinômio de grau4 (x−a)²(x−b)². Logo é zero.

## Erro da função exata

Se f∈C4[a,b], para cada x interior, tome w(s)=(s−a)²(s−b)² e K=(f(x)−H(x))/w(x). F=f−H−Kw tem zeros duplos nos extremos e um zero em x. Rolle repetido fornece F⁽⁴⁾(ξ)=0: F' tem quatro zeros (dois extremos, dois interiores), F″ ao menos três, F‴ dois e F⁽⁴⁾ um. H⁽⁴⁾=0 e w⁽⁴⁾=24, então K=f⁽⁴⁾(ξ)/24. Nos extremos o erro já é zero. Se |f⁽⁴⁾|≤M, |f−H|≤M h⁴/384, pois |(x−a)(x−b)|≤h²/4. É limite suficiente para função regular e dados exatos, não certificado obtido a partir de apenas quatro números.

## Construções próprias

f=x⁴ em[-1,1], valores1,1 e derivadas−4,4 → H=2x²−1. Erro=(x²−1)²; no centro, f=0,H=−1 e erro1, atingindo M h⁴/384 com M=24,h=2. Hermite não garante positividade ou ausência de extremos espúrios.

Para isolar ruído, use f=x³ em[0,2], dados(0,8,0,12). O interpolante é exato. Perturbar apenas a derivada inicial em1/4 muda o valor central de1 para17/16: deslocamento1/16. Em geral, com erros de derivada ε0,ε1, ΔH=h(H10 ε0+H11 ε1). No intervalo normalizado, |H10|,|H11|≤4/27; logo |ΔH|≤4h(|ε0|+|ε1|)/27. No centro, ΔH=h(ε0−ε1)/8. Erros iguais cancelam nesse ponto, sem cancelar em todo o intervalo.

Se também há erros de valores η0,η1, H00,H01≥0 e H00+H01=1 dão contribuição≤max(|η0|,|η1|). Some as parcelas para limite total. Ordem4 do erro de interpolação não implica ordem4 com qualquer estimativa de derivada: ε=O(h³) é condição suficiente para a contribuição hε ser O(h⁴). Não inferimos distribuição estatística do ruído.

## Código e verificação

`python3 labs/hermite-dados/hermite.py`

`python3 -m unittest discover -s labs/hermite-dados -t .`

Fraction mantém aritmética racional; a nova rotina rejeita extrapolação, diferentemente da rotina flutuante antiga preservada na aula. Isso é fronteira do laboratório, não mudança silenciosa no exemplo anterior. Quatro testes: 81 cúbicos em3 intervalos e5 pontos (1215 pares valor/derivada); erro quártico em81 pontos e razão16 no refino; 225 cenários de perturbação; contratos. Testes em pontos não substituem a prova para todos os dados.

Não implementa diferenças confluentes para muitos nós, spline global C2, tratamento de medidas ou seleção automática de derivadas. Compartilhar derivadas em nós fornece C1 por trechos, sem garantir continuidade de segunda derivada.

## Fontes e limites

Burden, Faires e Burden, Análise Numérica, 10ª edição em português (2016), §3.4: início da seção na p.149/PDF163; definição3.8 e teorema3.9 na p.150/PDF164; trecho da demonstração na p.151/PDF165, conferidos visualmente em29/10/2026. O PDF não forneceu texto extraível nessas páginas; não alegamos leitura integral nem reproduzimos seus exemplos. LeMesurier e Roberts, notas universitárias §3.4.4, consulta parcial na mesma data para contexto e erro. Construção de dois nós, prova, exemplos, figura e código aqui são próprios.

[Notas universitárias, §3.4.4](https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python/docs/main/piecewise-polynomial-approximation-and-splines.html#hermite-cubic-approximation)

As notas públicas contêm aparentes lapsos de índices/coeficientes em fórmulas intermediárias; as bases daqui foram derivadas e verificadas independentemente pelas condições. Sem copiar os exemplos ou código da fonte. PDFs privados e páginas renderizadas não são distribuídos pelo site.
