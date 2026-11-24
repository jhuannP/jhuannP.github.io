# Trocar a ordem mantendo a região

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão de Jhuann.

## Ordem de integração é uma forma de descrever fatias

Uma integral dupla soma valores do integrando ponderados por áreas. Uma integral iterada calcula essa soma por integrações sucessivas. Na ordem dy dx, fixamos x enquanto integramos em y; na ordem dx dy, fixamos y enquanto integramos em x. A troca deve manter o mesmo conjunto de pontos. Os limites internos podem depender da variável externa, mas não da variável que está sendo integrada naquele momento.

## Retomar o triângulo do exemplo inicial

No triângulo 0≤y≤x≤1, uma fatia vertical tem x entre zero e um e y de zero até x. Para a fatia horizontal, y varia de zero a um e x vai de y até um. Com f=x+y, a ordem dy dx fornece ∫₀¹(3x²/2)dx=1/2; na ordem dx dy, a integral interna é 1/2+y−3y²/2, cuja integral de zero a um também é 1/2. O exemplo resolvido antigo abaixo continua usando esse triângulo.

Triângulo: x fixo → 0≤y≤x

## Antes da troca, confira as hipóteses

Neste recorte, trabalhamos com funções contínuas em regiões fechadas e limitadas descritas por fronteiras simples, como o triângulo e a região entre as duas curvas abaixo. É um caso suficiente para calcular a mesma integral dupla por ambas as ordens apresentadas. As hipóteses não são decoração: problemas com singularidades, intervalos infinitos ou integrabilidade não absoluta exigem análise própria. Não deduzimos aqui um teorema geral para qualquer integral imprópria.

## Uma nova região entre reta e parábola

Considere D dado por 0≤x≤1 e x²≤y≤x, com coordenadas adimensionais. As fronteiras y=x² e y=x se encontram em x=0 e x=1. Entre esses pontos, x²≤x; a parábola fica abaixo da reta. Para x=1/2, a fatia vertical começa em y=1/4 e termina em y=1/2. Desenhar a região e testar uma fatia ajuda a conferir a desigualdade antes de escrever a integral.

D: 0≤x≤1, x²≤y≤x

## Resolver as desigualdades para a outra fatia

Fixe y. A desigualdade y≤x dá o limite inferior x=y. De x²≤y e x≥0, obtemos x≤√y. Como a projeção vertical da região é de zero a um, a nova descrição é 0≤y≤1 e y≤x≤√y. Para y=1/4, a fatia horizontal vai de x=1/4 até x=1/2. A raiz negativa não faz parte deste domínio de primeiro quadrante.

0≤y≤1, y≤x≤√y

## Calcular primeiro na ordem dy dx

Escolha f(x,y)=x+2y. Com x fixo, uma primitiva em y é xy+y². Entre y=x² e y=x, ela produz (x²+x²)−(x³+x⁴)=2x²−x³−x⁴. Agora integre em x de zero a um: I=2/3−1/4−1/5=13/60. O integrando é contínuo e não negativo na região; o resultado positivo é coerente. Não se reutilizam os limites do triângulo anterior, pois D é outra região.

I=2/3−1/4−1/5=13/60

## Conferir pela ordem dx dy

Com y fixo, uma primitiva em x é x²/2+2yx. Avalie entre x=y e x=√y: o limite superior dá y/2+2y^(3/2), enquanto o inferior dá y²/2+2y²=5y²/2. Integre o resultado em y de zero a um: I=1/4+4/5−5/6=13/60. A igualdade foi conferida por duas contas de uma mesma função sobre uma mesma região; escolher limites que descrevem outra região não é uma troca de ordem válida.

I=1/4+4/5−5/6=13/60

## A área ajuda, mas não identifica sozinha uma região

Usando f=1 em D, a área é ∫₀¹(x−x²)dx=1/2−1/3=1/6. Na outra ordem, ela é ∫₀¹(√y−y)dy=2/3−1/2=1/6. Essa é uma boa conferência, mas não uma prova de igualdade de regiões: conjuntos diferentes podem ter a mesma área. Precisamos verificar também quais pontos pertencem ao conjunto e quais curvas formam suas fronteiras.

Área(D)=1/6

## Um erro que passa na conferência da área

Se escrevermos 0≤y≤1 e y²≤x≤y, teremos a região espelhada em relação à diagonal, não D. Ela também tem área 1/6. Mas o ponto (1/2,3/8) pertence a D e não a essa região. Para f=x+2y, a integral na região errada vale 7/30, diferente de 13/60. Isso pode ser conferido trocando x e y no integrando sobre D: a integral de y+2x é 1/15+2(1/12)=7/30. Uma igualdade para f=1 não garante igualdade para todo integrando.

Região errada: I=7/30 ≠ 13/60

## Generalizar a conferência para monômios

Para f=xᵃyᵇ, com inteiros a,b≥0, integrar primeiro em y fornece [1/(b+1)]×[1/(a+b+2)−1/(a+2b+3)]. Integrar primeiro em x fornece [1/(a+1)]×[2/(a+2b+3)−1/(a+b+2)]. As duas expressões se reduzem a 1/[(a+b+2)(a+2b+3)]. Isso prova a igualdade desta família no domínio indicado, sem substituir o teorema geral de integração. Por linearidade, podemos somar um número finito desses monômios.

Momento=1/[(a+b+2)(a+2b+3)]

## Uma aproximação numérica usa também o peso da fatia

No laboratório, x percorre pontos médios de subintervalos de [0,1]. Para cada x, escrevemos y=x²+(x−x²)s, com 0≤s≤1. O comprimento vertical da fatia é x−x², que multiplica a contribuição numérica; ignorá-lo aproximaria outro problema. Refinar o número de subdivisões aproxima o valor exato 13/60 para este integrando. A concordância numérica é uma checagem da implementação, não uma prova das hipóteses de Fubini.

## Regiões mais gerais podem exigir divisão

Uma região pode não admitir uma única descrição simples em uma das ordens. Nesse caso, divida em partes e acompanhe onde cada fronteira passa a valer, evitando sobreposição de interiores ou partes omitidas. Trocar a ordem é uma estratégia para facilitar o cálculo, não uma obrigação. Mudanças de variáveis e seus jacobianos pertencem a outro assunto; aqui mantemos as coordenadas e a mesma região.

## Escopo e limites do laboratório

As coordenadas do exemplo são adimensionais. Em uma aplicação de densidade superficial, o elemento de área e as unidades do integrando precisam ser especificados para obter massa; a mesma expressão numérica não fixa essas unidades. O código trata polinômios finitos neste domínio específico, com coeficientes racionais e expoentes limitados para o uso didático. Não detecta regiões automaticamente, não decide integrabilidade geral e não estende a troca a singularidades sem análise. Material em rascunho assistido por IA para revisão pessoal.

## Exercícios e resoluções

- Qual limite inferior? **Resolução:** x≥y=0,3.
- Basta trocar dx e dy mantendo todos os limites? **Resolução:** É necessário redescrever a região.
- Na nova região, para y=1/4, qual o limite inferior de x? **Resolução:** x começa em y=1/4.
- Para o mesmo y=1/4, qual o limite superior de x? **Resolução:** x termina em √(1/4)=1/2.
- Para x=1/2, qual a largura vertical da fatia, ysuperior−yinferior? **Resolução:** 1/2−1/4=1/4.
- Qual a área da região entre y=x² e y=x para x de zero a um? **Resolução:** ∫₀¹(x−x²)dx=1/6.
- Quanto vale a integral de x+2y em D, calculada primeiro em y? **Resolução:** 2/3−1/4−1/5=13/60.
- Quanto deve valer a mesma integral, na ordem dx dy corretamente reescrita? **Resolução:** 1/4+4/5−5/6=13/60.
- Qual valor a região espelhada errada produz para o integrando x+2y? **Resolução:** A integral de y+2x sobre D vale 1/15+2/12=7/30.
- Duas regiões com área 1/6 são necessariamente a mesma região? **Resolução:** O exemplo espelhado mantém a área e altera quais pontos pertencem ao domínio.
- Na região D, a fatia horizontal deve incluir o ramo x=−√y? **Resolução:** A região original impõe x≥0; apenas o ramo não negativo pertence ao domínio.
- Os cálculos desta aula autorizam trocar a ordem de qualquer integral imprópria sem conferir hipóteses? **Resolução:** O recorte usa integrandos contínuos em regiões limitadas; singularidades e integrais impróprias pedem análise própria.

## Fontes e execução

Apostol, Cálculo II, edição em português do acervo, §11.6, pp.403–404: PDF414 e PDF417, consultados parcialmente por texto em 22/10/2026. O arquivo tem páginas fora da sequência; não aplicar deslocamento fixo nesta faixa. [OpenStax, Calculus Volume 3, §5.2](https://openstax.org/books/calculus-volume-3/pages/5-2-double-integrals-over-general-regions), regiões gerais e hipóteses, consulta parcial. A tentativa inicial em /5-3 foi indisponível; a seção correta /5-2 foi consultada. Não se afirma leitura integral ou reprodução de exercícios/figuras.

Na raiz: python3 -m labs.fubini-regiao.experiment; testes: python3 -m unittest discover -s labs/fubini-regiao -t .

Momentos exatos para D específico; a aproximação midpoint_example integra x+2y, com N de um a 256. Nenhum dado real ou resultado de pesquisa.


## Troca de ordem em região curvilínea — 22/10/2026

Aula c3-fubini ampliada de três seções/dois exercícios para 13 seções/12 exercícios. Exemplo triangular inicial, IDs, cálculos Python e desafio preservados, agora com identificação explícita do domínio antigo. Novo recorte: D={0≤x≤1, x²≤y≤x}, coordenadas adimensionais; na outra ordem, D={0≤y≤1, y≤x≤√y}. Para f=x+2y, ambas as contas dão 13/60. Área é 1/6; a região espelhada errada tem a mesma área, mas integral 7/30 e pontos diferentes. A conferência de área isolada não identifica o domínio.

Fontes primárias consultadas parcialmente em 22/10/2026: Apostol, Cálculo II, edição em português do acervo, §11.6, pp.403–404, correspondendo a PDF414 e PDF417. Há páginas fora da sequência no arquivo: não usar um deslocamento fixo nessa faixa. Foram lidas as hipóteses da integração repetida e a discussão de troca de ordem. [OpenStax, Calculus Volume 3, §5.2](https://openstax.org/books/calculus-volume-3/pages/5-2-double-integrals-over-general-regions), regiões gerais e hipóteses, consultado parcialmente. Sem leitura integral, reprodução de exercícios ou figuras. Identidades de momentos, exemplo e código locais originais.

Laboratório labs/fubini-regiao/: momentos racionais exatos nas duas ordens para monômios, combinação polinomial finita e aproximação de ponto médio para x+2y. Cinco testes novos aprovados: 169 pares de expoentes nas duas ordens e momentos conhecidos; resultado e domínio espelhado; equivalência das desigualdades em grade racional; refinamento numérico independente; linearidade e contratos. Resultados de ponto médio N=10,20,40: aproximadamente 0,21791375; 0,2169789844; 0,2167447803, convergindo ao exato 13/60. Não é prova numérica do teorema geral.

Treze testes de catálogo e 538 estruturas MathML aprovados; catálogo revalidado após figura e clarificação do exemplo antigo. Figura com dimensões 440×440 para reservar espaço. Nenhum modelo JavaScript alterado; suíte global não repetida. Hipóteses de continuidade/região limitada não foram estendidas automaticamente a integrais impróprias ou singularidades.

Navegador: figura e texto legíveis em 390 px, largura da página igual à tela, nenhum erro de console observado. Na atividade do domínio correto, 7/30 rejeitado e 13/60 aceito. Prévia fubini-regiao-mobile.jpg. Material assistido por IA em rascunho para revisão pessoal.

A trilha agregada Cálculo 3 tem 16 aulas/109 exercícios, oito recortes desenvolvidos e oito introduções. Integração múltipla apoia Matemática IV; os cinco grupos oficiais continuam parciais. O aprofundamento não altera situação acadêmica nem comprova domínio pessoal. Catálogo global: 501 aulas/3064 exercícios.

Próxima revisão pessoal: redescrever as fatias, reconstruir as contas e explicar o exemplo de área igual com domínio diferente. Próximo bloco global: reconciliar contagens e resumos das trilhas com o catálogo, procurando projeções editoriais antigas sem elevar status de cobertura. Saldo semanal após bloco: 92%; parada operacional em 65%.

## Extensão de28/10/2026 — um contraexemplo singular clássico

f=(x²−y²)/(x²+y²)² em0<x,y≤1, exemplo clássico identificado em [Lebl, Basic Analysis,§10.2,exercício10.2.6](https://www.jirka.org/ra/html/sec_iteratedints.html). Consulta parcial online em28/10/2026 ao caso contínuo e identificação do exemplo; não se atribui sua invenção ao autor das notas. As contas e extensão parametrizada abaixo foram desenvolvidas nestas notas. A tentativa de abrir a fonte UPenn retornou403 e não foi usada como leitura confirmada.

Primitiva em y: y/(x²+y²). Integrar y primeiro e depois x dáπ/4. Primitiva em x:−x/(x²+y²). Integrar x primeiro e depois y dá−π/4. Intervalos abertos junto da origem interpretados por limites unilaterais; não se exige integrar a seção singular do eixo.

No quarto de anel ε≤r≤1, f dA=cos(2θ)dr/r dθ. Integral angular do módulo=1; integral absoluta=log(1/ε). Partes positiva e negativa têm cada uma metade desse valor e divergem. Não existe integral assinada de Lebesgue finita; subtrair∞−∞não a define. Isso não contradiz os casos de Fubini sob integrabilidade adequada.

I(a,b) no retângulo[a,1]×[b,1],a,b>0,é regular e valeπ/4−atan(a)−atan(1/b)+atan(a/b). Com a=λb→0: limite atan(λ)−π/4. λ1→0,λ2→aproximadamente0,321751,λ1/2→oposto. Cortes simétricos dão0,sem comprovar integral convergente independente do procedimento. Remover b antes de a ou a antes de b recupera os dois valores iterados.

`cutoff.py` usa atan2 para evitar divisão direta nas razões. Compara a expressão de cortes finitos com ponto médio em x após integração analítica em y; não é quadratura2D ou detector de singularidades. Float tem precisão finita; testes não equivalem a limites matemáticos. Código anterior de polinômios/região entre curvas preservado.

Da raiz: `python3 labs/fubini-regiao/cutoff.py` e `python3 -m unittest discover -s labs/fubini-regiao -t .`. Nove testes,cinco anteriores e quatro da extensão: quadratura em quatro retângulos,simetria/caminhos,limites iterados/divergência e contratos. Novos seis exercícios na aula. Revisão pessoal pendente; teoria geral de medida,critérios de integrabilidade e outras singularidades continuam fora deste recorte.
