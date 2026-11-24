# Riemann e Darboux — partições e malha

## Uma partição identifica todas as larguras usadas

Uma partição P de [a,b], com a<b, é uma lista a=x₀<x₁<…<xₙ=b. A faixa i tem largura Δxᵢ=xᵢ−xᵢ₋₁, sempre positiva. A malha ||P|| é a maior dessas larguras. As faixas não precisam ser iguais. Quando são uniformes, Δx=(b−a)/n; a expressão 1/n usada no exemplo [0,1] é um caso particular, não a definição geral de largura.

## O ponto marcado escolhe uma altura dentro de cada faixa

Escolha ξᵢ em [xᵢ₋₁,xᵢ] e forme S(f,P,ξ)=Σᵢ f(ξᵢ)Δxᵢ. O ponto pode ser esquerdo, direito, médio ou outro ponto da faixa. A função é avaliada no ponto marcado e multiplicada pela largura daquela faixa. Em uma partição não uniforme, dividir a soma das alturas apenas pelo número de faixas geralmente usa pesos errados.

S(f,P,ξ)=Σᵢ f(ξᵢ)Δxᵢ

## Somas inferior e superior precisam limitar toda a faixa

Suponha f limitada em [a,b]. Em cada faixa, tome mᵢ como o ínfimo de f e Mᵢ como seu supremo. Defina L(f,P)=ΣᵢmᵢΔxᵢ e U(f,P)=ΣᵢMᵢΔxᵢ. Como mᵢ≤f(ξᵢ)≤Mᵢ e as larguras são positivas, qualquer soma marcada fica entre L e U. Ínfimo e supremo permitem a definição mesmo quando a função não atinge seus extremos; não são sempre os valores das pontas.

L(f,P)≤S(f,P,ξ)≤U(f,P)

## Refinar significa conservar os pontos e acrescentar novos

Uma partição Q refina P quando contém todos os pontos de P. Dividir faixas não diminui a soma inferior nem aumenta a superior: L(f,P)≤L(f,Q)≤U(f,Q)≤U(f,P). Uma soma marcada específica pode aumentar ou diminuir; as cotas é que se comportam assim. Duas partições têm refinamento comum obtido pela união ordenada dos seus pontos. Trocar uma lista por outra com mais pontos, mas sem conservar os anteriores, não é necessariamente um refinamento.

## Integrabilidade exige fechar o intervalo entre cotas

A integral inferior é o supremo de todas as somas inferiores, e a superior é o ínfimo de todas as somas superiores. Uma função limitada é integrável no sentido de Riemann quando esses dois números coincidem. Equivalentemente, para todo ε>0 existe uma partição com U−L<ε. Se as integrais coincidem, escolha cotas próximas de cada lado e um refinamento comum; se há partições com diferença arbitrariamente pequena, a diferença entre as integrais não pode ser positiva. Isso justifica o critério.

## Para x² em [0,1], as pontas são os extremos corretos

A função x² é crescente nesse intervalo. Em cada faixa, a menor altura é a do extremo esquerdo e a maior a do direito. Para n=2 faixas uniformes, L₂=(0²+(1/2)²)/2=1/8 e U₂=((1/2)²+1²)/2=5/8. Pontos médios dão outra soma: S=(1/2)[(1/4)²+(3/4)²]=5/16, ainda dentro das cotas. Essa soma de pontos médios é diferente de calcular o ponto médio entre L₂ e U₂.

## As somas uniformes permitem calcular a integral sem antiderivada

Para n faixas, Uₙ=(1/n³)Σ de k=1 a n de k². A identidade Σk²=n(n+1)(2n+1)/6 pode ser obtida somando k³−(k−1)³=3k²−3k+1 e usando Σk=n(n+1)/2. Substituindo, Uₙ=1/3+1/(2n)+1/(6n²). Como Uₙ−Lₙ=1/n, Lₙ=1/3−1/(2n)+1/(6n²). Ambas convergem para 1/3; pelo critério das cotas, ∫₀¹x²dx=1/3. Não usamos previamente a regra de integração de potências.

Uₙ−Lₙ=1/n; lim Lₙ=lim Uₙ=1/3

## Para partições não uniformes, a maior largura controla o erro entre cotas

Na faixa [u,v] dentro de [0,1], v²−u²=(v−u)(u+v)≤2(v−u). Logo a contribuição à diferença U−L é no máximo 2(Δxᵢ)². Somando e usando Δxᵢ≤||P||, obtemos U−L≤2||P||ΣΔxᵢ=2||P||. Portanto, quando a malha tende a zero, todas as somas marcadas ficam entre cotas que se aproximam do mesmo valor. Para P={0,1/4,1/2,1}, L=9/64, U=37/64 e ||P||=1/2.

U(f,P)−L(f,P)≤2||P|| para f(x)=x² em [0,1]

## Apenas os valores das pontas podem falhar para outra função

Para f(x)=4x(1−x) em [0,1], os dois extremos têm valor zero, mas f(1/2)=1. Com uma única faixa, usar o maior valor das pontas como se fosse o supremo daria uma cota superior falsa. A soma superior correta precisa considerar toda a faixa. O laboratório desta aula é específico para x² crescente; não é um algoritmo que encontra extremos de qualquer função.

## Mais pontos não bastam se uma faixa larga continuar sem dividir

Imagine dividir [0,1/2] em cada vez mais faixas, mantendo [1/2,1] inteira. O número total de faixas cresce, mas a malha permanece 1/2. Só a última faixa contribui (1²−(1/2)²)(1/2)=3/8 para U−L. Assim as cotas não fecham, por mais pontos que sejam acrescentados à primeira metade. Para obter garantia pelo refinamento da malha, todas as partes precisam ficar suficientemente estreitas.

## Uma função limitada pode não ser integrável de Riemann

Considere f=1 nos racionais e f=0 nos irracionais de [0,1]. Todo subintervalo de comprimento positivo contém números dos dois tipos; portanto mᵢ=0 e Mᵢ=1 em toda faixa. Qualquer partição produz L=0 e U=1. O critério falha: não existe integral de Riemann dessa função nesse intervalo. Isso é um argumento teórico baseado em densidade, não algo que um teste de racionalidade de floats possa demonstrar.

## A integral usa valores com sinal e conserva as unidades

Se x representa tempo e f representa velocidade, cada produto f(ξᵢ)Δxᵢ representa uma contribuição de deslocamento. Velocidade negativa produz contribuição negativa. A área geométrica total exige outra interpretação, como integrar o módulo quando isso faz sentido. No exemplo x² em [0,1], a função é não negativa e a integral coincide com a área sob o gráfico. O produto sempre tem unidade da função vezes unidade da variável.

## O laboratório confere o caso declarado e mantém o painel existente

O núcleo Python recebe uma partição racional de [0,1], com pontos estritamente crescentes, e calcula as cotas de x². tagged_sum recebe exatamente uma amostra racional por faixa, conferindo se ela pertence ao intervalo correto. O painel da aula continua com faixas uniformes e valores aproximados; o código baixável usa Fraction. Testes com 128 partições de uma grade e escolhas esquerda/direita/meio conferem as contas, sem substituir o critério de integrabilidade.

## A revisão deve reconstruir as hipóteses antes dos números

Refaça as cotas para duas faixas, explique a largura de cada faixa não uniforme e justifique por que o exemplo com faixa larga não oferece a garantia desejada. A apresentação por ínfimos/supremos corresponde à abordagem por funções em escada e integrais superior/inferior consultada parcialmente no Apostol; não se leu todo o capítulo. Provas, contraexemplos explicados, figura e exercícios são notas próprias assistidas por IA para revisão. Integrabilidade e experiência pessoal não são certificadas por testes finitos.

## Exercícios e resoluções originais

- Para f(x)=x² em [0,1] e duas faixas iguais, qual a soma esquerda L₂? **Resolução:** (1/2)[0²+(1/2)²]=1/8.
- No exemplo, a soma à direita é cota superior? **Resolução:** x² é crescente em [0,1].
- Nas mesmas duas faixas, qual a soma direita U₂? **Resolução:** (1/2)[(1/2)²+1²]=5/8.
- Com quatro faixas uniformes para x² em [0,1], qual L₄? **Resolução:** (0²+(1/4)²+(1/2)²+(3/4)²)/4=7/32.
- Qual U₄ no mesmo caso? **Resolução:** L₄+1/4=7/32+8/32=15/32.
- Qual a malha de P={0,1/4,1/2,1}? **Resolução:** As larguras são 1/4,1/4,1/2; a maior é 1/2.
- Quanto é U₄−L₄ para as quatro faixas uniformes? **Resolução:** 1/4.
- Para duas faixas uniformes, qual soma marcada nos pontos médios 1/4 e 3/4? **Resolução:** (1/2)[1/16+9/16]=5/16.
- Para x² e P={0,1/4,1/2,1}, qual a soma inferior? **Resolução:** 0×1/4+(1/4)²×1/4+(1/2)²×1/2=1/64+1/8=9/64.
- Qual a soma superior para essa partição não uniforme? **Resolução:** (1/4)²×1/4+(1/2)²×1/4+1²×1/2=37/64.
- Qual ∫₀¹x² dx obtida pelo limite das cotas? **Resolução:** As duas fórmulas de somas convergem para 1/3.
- Mantendo [1/2,1] sem dividir, qual sua contribuição fixa para U−L no caso x²? **Resolução:** (1−1/4)×1/2=3/8.

## Laboratório e fonte

Na raiz: `python3 -m unittest discover -s labs/riemann-particoes -t .` e `python3 -m labs.riemann-particoes.partitions`. Biblioteca padrão, sem dependência do painel. Partições list/tuple com início 0, fim 1 e ordem estrita, valores int/Fraction sem bool/float/texto. Tags list/tuple com uma amostra por faixa, dentro dos respectivos intervalos fechados. Calcula somente x², sem supremo automático de função arbitrária.

Testes: fórmulas uniformes para n=1..40; todas as 128 partições da grade de oitavos, com 384 escolhas de tags esquerda/direita/meio e refinamentos por pontos médios; exemplo não uniforme; faixa larga persistente; contratos. Não se testa racionalidade de floats ou integrabilidade por amostragem.

Fonte do acervo autorizado: Apostol, Calculus I, 2ª ed. (1967), §1.9 pp.61–62 (PDF81–82), §§1.16–1.17 pp.72–74 (PDF92–94) e §1.21 pp.77–78 (PDF97–98), consulta textual parcial em 22/10/2026. A fonte constrói integrais por funções em escada; a exposição por somas de Darboux, provas de x² e contraexemplos explicados aqui são próprios e não reproduzem figuras/exercícios. Mantida limitação de avisos/OCR; nenhum PDF pessoal distribuído.

Aula existente ampliada de três para 14 seções e de dois para 12 exercícios; IDs e painel riemannBounds preservados, enunciado genérico esclarecido e sums(n) inline agora rejeita bool. Rascunho assistido por IA. Curso segue com 24 aulas e agora 214 exercícios; duas aulas curtas permanecem. Próxima revisão pessoal: explicar por que 1/n não é largura geral e por que muitos pontos podem deixar malha grande. Continuar distribuindo o avanço entre os demais temas, sem declarar Cálculo I completo.

Verificação: cinco testes locais aprovados, incluindo 128 partições, 384 escolhas de tags, refinamentos e 40 somas uniformes; 13 testes de catálogo e 576 estruturas MathML aprovados. Navegador a 390 px: documento 375 px, figura inspecionada; questão 9 rejeitou 5/48 e aceitou 9/64. Painel uniforme preservado: teclado alterou n=4 para 5 e o relatório passou a cotas 0,24/0,44, diferença 0,2. Console sem erros observados. Prévia riemann-particoes-mobile.jpg. Catálogo 509 aulas/3325 exercícios, 253 aulas com até três seções; cobertura recalculada. Não houve leitura integral do livro ou repetição da suíte global dos demais laboratórios. Saldo semanal após bloco: 89%; parada em 65%. Próxima revisão pessoal: reconstruir o critério e o contraexemplo de malha persistente; próximo desenvolvimento deve alternar para outra disciplina básica/complementar.
