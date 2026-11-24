# Transformações lineares2D

Rascunho original —27/10/2026; revisão de Jhuann pendente.

## Fixe domínio, saída e coordenadas

Pré-requisitos: vetores no plano, combinações lineares e sistemas2×2. Estudamos T:ℝ²→ℝ² usando a base canônica na entrada e na saída. A letra T nomeia a transformação e A sua matriz nessas bases. Não é uma transformação de qualquer dimensão sem adaptação; o laboratório também é limitado a2D. Os vetores e as figuras são exemplos matemáticos próprios, sem dados experimentais.

## Uma regra que preserva combinações

Linearidade exige T(αu+βv)=αT(u)+βT(v) para quaisquer vetores u,v e escalares reais α,β. Isso reúne preservação de soma e de multiplicação por escalar. Não basta verificar dois ou três vetores escolhidos. Para uma matriz fixa, a distributividade da multiplicação mostra a igualdade para vetores arbitrários; essa justificativa geral é diferente de testar uma lista finita de entradas.

T(αu+βv) = αT(u)+βT(v)

## A origem é preservada, mas esse teste não basta

Se T é linear, T(0)=T(0+0)=T(0)+T(0); subtrair T(0) dá T(0)=0. Portanto uma translação não nula já falha no teste da origem. A recíproca é falsa: H(x,y)=(x²,y) leva a origem à origem, mas H(2,0)=(4,0) difere de 2H(1,0)=(2,0). Um contraexemplo refuta linearidade; passar por esse único teste não a demonstra.

## Matriz e vetor

Escreva A=[[a,b],[c,d]]. Multiplicar A pelo vetor-coluna(x,y) dá(ax+by,cx+dy). As linhas permitem calcular cada coordenada de saída; as colunas têm outra interpretação: Ae₁=(a,c) e Ae₂=(b,d), com e₁=(1,0), e₂=(0,1). Trocar linhas por colunas sem mudar a convenção produz outra regra. A implementação original mantém vetores-coluna e produtos entre linhas e entrada.

A(x,y) = (ax+by, cx+dy)

## Por que duas imagens determinam o plano inteiro?

Todo vetor (x,y) tem uma decomposição única xe₁+ye₂. Pela linearidade, T(x,y)=xT(e₁)+yT(e₂). Assim escolher as duas imagens da base define a regra para todo vetor, e qualquer transformação linear com essas imagens precisa obedecer à mesma fórmula. No exemplo original A=[[2,1],[0,1]], as imagens são(2,0) e(1,1); logo T(x,y)=(2x+y,y). Isso explica a multiplicação matricial, em vez de apenas decorar uma operação.

T(x,y)=xT(e₁)+yT(e₂)

## Acompanhe um vetor e depois um conjunto

O exemplo original transforma(1,2) em(4,2). Para transformar um quadrado ou outro polígono, aplique a mesma regra a cada vértice. O quadrado unitário com vértices(0,0),(1,0),(1,1),(0,1) vira o paralelogramo (0,0),(2,0),(3,1),(1,1). Não basta deslocar o centro ou mudar só a altura de um desenho: cada ponto obedece a T.

## A imagem do quadrado mostra as duas colunas

A figura mantém uma única escala nos dois eixos. O lado inferior da imagem é T(e₁)=(2,0) e o outro lado a partir da origem é T(e₂)=(1,1). O paralelogramo tem base 2 e altura 1, portanto área 2, enquanto o quadrado de referência tem área 1. Isso não significa que todos os comprimentos dobraram: e₂ tinha comprimento 1 e sua imagem tem comprimento √2.

## Área e degeneração

Para A=[[a,b],[c,d]], det(A)=ad−bc. Seu módulo é o fator de área, e seu sinal informa se a orientação é preservada ou invertida, quando o determinante é não nulo. Para o exemplo original, det=2: a área dobra com orientação preservada. Para diag(−1,2), det=−2: a área também dobra, mas a orientação se inverte. Área geométrica não é negativa; a área orientada pode ter sinal.

det(A) = ad−bc

## Uma conta justifica o fator de área

Para dois vetores u=(p,q) e v=(r,s), a área orientada do paralelogramo que geram é ps−qr. Após aplicar A, ela é(ap+bq)(cr+ds)−(ar+bs)(cp+dq). Expandir e agrupar produz(ad−bc)(ps−qr). Portanto toda área orientada de paralelogramo é multiplicada por det(A), não apenas a do quadrado desenhado. Triângulos têm metade dessa área e polígonos simples podem ser decompostos em triângulos. A enumeração do laboratório confere a implementação, enquanto essa álgebra sustenta a relação geral.

det[Au,Av]=det(A)det[u,v]

## Determinante zero perde uma direção ou todas

Considere B=[[1,2],[2,4]]. A regra é B(x,y)=(x+2y,2x+4y)=(x+2y)(1,2). A imagem é a reta gerada por(1,2): não é o plano inteiro, embora B não seja nula. O vetor (−2,1) vai para zero. A matriz nula, por sua vez, leva tudo ao ponto zero. Para uma transformação2×2, determinante zero indica colunas dependentes e imagem com dimensão menor que2, mas não distingue sozinho reta de ponto.

B(x,y)=(x+2y)(1,2)

## Núcleo e imagem respondem perguntas complementares

O núcleo contém as entradas que chegam a zero; a imagem contém todas as saídas alcançáveis. No caso B, o núcleo é a reta{t(−2,1)} e a imagem é a reta{r(1,2)}. Ambos são subespaços, mas pertencem a lados diferentes da transformação. Um núcleo não trivial explica a perda de informação: B(v+t(−2,1))=B(v) para qualquer t. Assim várias entradas distintas podem ter a mesma saída.

ker(B)=span{(−2,1)}; Im(B)=span{(1,2)}

## Resolver uma pré-imagem também testa alcançabilidade

Para B(x,y)=(3,6), basta x+2y=3; todas as entradas(3−2t,t) servem. Para a saída (3,5), não existe entrada, porque a segunda coordenada de uma imagem de B precisa ser o dobro da primeira. A frase “matriz singular” não diz, sozinha, que um sistema particular é impossível: pode haver nenhuma ou várias soluções. Para a matriz original A, det=2 e cada saída tem uma única pré-imagem; para(5,−1), obtemos y=−1 e x=3.

## Nem toda regra com fórmula de reta é linear

A transformação afim F(v)=Av+b, com b constante não nulo, não é linear porque F(0)=b. Ela é útil em geometria, mas deve ser nomeada corretamente. Já T(p+tu)=T(p)+tT(u) mostra que uma transformação linear leva uma reta a uma reta ou a um ponto. Não se conclui daí que preserve ângulos, comprimentos ou áreas; cada propriedade exige condições adicionais. Uma matriz depende das bases escolhidas: mudar coordenadas não significa necessariamente mudar a transformação física ou geométrica.

## O painel aproxima; o laboratório usa frações exatas

O painel começa na identidade e transforma o quadrado com quatro controles. Para reproduzir o exemplo, use a=2,b=1,c=0,d=1; para ver uma perda de direção, escolha colunas dependentes. O painel usa ponto flutuante. O laboratório baixável aceita matrizes e vetores racionais2D, confere áreas por polígonos e calcula pré-imagem apenas quando det≠0. Uma falha dessa última função em B não é prova de que toda saída seja impossível. Determinante pequeno ou arredondado para zero também não é, sozinho, uma análise de condicionamento.

## Revisão em duas sessões e próximos passos

Na primeira sessão de vinte minutos, reconstrua a matriz pelas imagens de e₁,e₂ e explique o paralelogramo. Na segunda, descreva núcleo, imagem e as pré-imagens de(3,6) e(3,5) no caso B. Registre sua própria demonstração antes de apresentar domínio do tema. Composição, mudança de base completa, inversa, autovalores e condicionamento têm aulas ou recortes próprios e ainda precisam de aprofundamento. Esta aula permanece em rascunho para revisão pessoal.

## Exercícios e resoluções

Qual é o determinante de [[3,0],[0,2]]?

**Resolução:** det(A)=3×2−0×0=6.

Se det(A)=0, a matriz 2×2:

**Resolução:** Uma matriz quadrada é inversível se e somente se seu determinante é não nulo.

Para A=[[2,1],[0,1]], qual é a primeira coordenada de A(1,2)?

**Resolução:** 2×1+1×2=4.

Qual é a primeira coordenada de A(e₂), para a mesma A?

**Resolução:** e₂=(0,1); sua imagem é a segunda coluna(1,1).

Na mesma A, se a saída é(5,−1), qual é a primeira coordenada da entrada?

**Resolução:** y=−1 e2x+y=5, logo x=3.

Qual é o determinante de diag(−1,2)?

**Resolução:** −1×2=−2; orientação invertida.

Qual é o fator de área geométrica de diag(−1,2)?

**Resolução:** É o módulo do determinante,2.

Em B=[[1,2],[2,4]], qual é x para que B(x,1)=0?

**Resolução:** x+2=0 dá x=−2.

Para a mesma B, qual é a segunda coordenada de B(1,1)?

**Resolução:** 2×1+4×1=6.

A saída (3,5) pertence à imagem de B=[[1,2],[2,4]]?

**Resolução:** A segunda coordenada teria de ser6.

F(v)=Av+(1,0) é linear?

**Resolução:** F(0)=(1,0)≠0, o que já refuta a linearidade.

Se H(0)=0, isso basta para provar que H é linear?

**Resolução:** H(x,y)=(x²,y) passa nesse teste e falha em H(2,0)=2H(1,0).

## Referência e limites

Elon Lages Lima, Álgebra Linear, IMPA2014, exemplar identificado no inventário como complementar, não integrante da bibliografia oficial confirmada deCCM0213. Consulta textual parcial em 27/10/2026: §4 pp.38–39/PDF49–50, §6 pp.58–61/PDF69–72 em trechos selecionados e §8 p.83/PDF94. P.38/PDF49 visualmente inspecionada; offset reconferido em p.39 e61. Não se afirma leitura integral dos capítulos ou localização dos livros oficiais ainda não identificados. Exemplos, demonstrações numéricas, figura e código próprios; PDFs privados não distribuídos.

## Laboratório e continuidade

`python3 -m unittest discover -s labs/transformacao-2d -t .` e `python3 labs/transformacao-2d/linear.py`. API aceita int/Fraction, rejeita bool/float e dimensões diferentes de 2×2/2. Operações mantêm a entrada. preimage_invertible rejeita determinante zero e não distingue sistema incompatível de família de soluções. area retorna área orientada da cadeia de vértices; para área geométrica de polígono simples, tome módulo. Não é classificador geral de polígonos ou diagnóstico de estabilidade.

Cinco testes: exemplo original/família singular; colunas e linearidade em 81 matrizes e25 vetores, com combinação racional; áreas por fórmula de polígono em 243 pares matriz/polígono; pré-imagens em matrizes invertíveis e contraexemplo afim; contratos. As relações gerais são justificadas na aula, não por enumeração finita. O laboratório anterior de área/determinante não foi alterado ou revalidado globalmente.

Próxima revisão: imagens da base e singularidade sem concluir incompatibilidade automática. Próxima elaboração: composição, mudança de base e inversa com os recortes próprios; alternar com outras disciplinas.
