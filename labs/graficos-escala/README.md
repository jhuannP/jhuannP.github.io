# Leitura de gráficos — escala, variações e áreas

## Identifique variável, unidade e fonte antes de comparar alturas

O painel usa quantidades hipotéticas 100 e 110 em dois períodosA eB, na mesma unidade. Esses números são dados sintéticos, não medições reais de um trabalho. Antes de ler uma conclusão, procure o significado dos eixos, unidade, períodos ou categorias, fonte e tamanho do conjunto. O gráfico não contém automaticamente informação sobre como os dados foram coletados.

## Uma escala linear transforma diferenças em distâncias

Num eixo linear entre limites L e U, uma diferença numérica d ocupa uma fração d/(U−L) do comprimento desenhado. Intervalos igualmente espaçados no papel representam diferenças numéricas iguais. Confira marcas e limites: mudar a faixa exibida pode ampliar uma diferença sem alterar os valores. Linhas de grade ajudam a ler, mas não substituem rótulos claros e unidades.

fração do eixo=d/(U−L)

## Diferença absoluta e relativa usam referências diferentes

De 100 para 110, a diferença absoluta é 10 unidades. A mudança relativa usa a base inicial: (110−100)/100=1/10, ou 10%. De 10 para 20, a mesma diferença absoluta 10 representa 100%. Assim o tamanho de uma variação precisa ser comunicado com sua base, não apenas com uma porcentagem isolada.

variação percentual=100(final−inicial)/inicial

## Base zero não permite a mesma divisão percentual

A fórmula anterior pressupõe inicial>0 nesta aula de quantidades não negativas. De 0 para 10, a mudança absoluta é 10, mas dividir por 0 não define uma taxa percentual finita por essa expressão. De 100 para 0, a redução relativa é−100%. Com bases negativas ou medidas cujo zero é arbitrário, porcentagens exigem uma interpretação adicional; o laboratório mantém o domínio explícito e recusa esses casos em vez de improvisar uma taxa.

## Inverter a comparação troca a base

Subir de 100 para 110 dá 10%, mas voltar de 110 para 100 dá−10/110=−1/11, aproximadamente−9,09%. A diferença absoluta tem o mesmo módulo, porém a referência inicial mudou. Por isso uma redução percentual não é obtida sempre por apenas trocar o sinal do aumento. Compare a direção e a base antes de calcular.

## Pontos percentuais não são aumento percentual

Uma taxa que passa de 20% para 25% sobe 5 pontos percentuais. A mudança relativa é(25−20)/20=1/4, ou 25%. Os números 5 e 25 respondem a perguntas distintas. Se a taxa inicial for 0%, a diferença em pontos ainda é definida, enquanto a mudança relativa pela divisão anterior fica indefinida.

20%→25%: +5 pontos percentuais; +25% relativo

## Barras cortadas podem dobrar de altura sem dobrar os valores

No eixo que começa em 0, as alturas de barras para 100 e 110 são proporcionais a esses valores: razão 110/100=1,1. Se a origem passa a 90, as partes desenhadas têm alturas proporcionais a 100−90=10 e 110−90=20, com razão 2. O segundo valor não dobrou; o que dobrou foi a distância desenhada acima da base cortada. Para origem b abaixo dos dois valores, a razão visual é(final−b)/(inicial−b).

razão visual=(final−b)/(inicial−b)

## Escolher o gráfico também resolve um problema de escala

A orientação consultada da ONS recomenda que eixos de gráficos de barras/colunas comecem em zero, para preservar a leitura por comprimento. Para destacar diferenças pequenas, pode ser melhor usar outro tipo, como pontos ou linhas, com limites explícitos. O painel cortado é um contraexemplo didático, marcado por uma quebra; não é uma recomendação de apresentação. Um eixo não nulo em um gráfico de linhas também exige leitura cuidadosa, mas a comparação não se baseia no comprimento de uma barra desde a origem.

## Uma inclinação exige o intervalo real de tempo

Imagine valores 100,110,120 nos tempos 0h,1h,3h. O primeiro trecho cresce 10 unidades em 1h: taxa média 10 unidades/h. O segundo cresce 10 em 2h: taxa média 5 unidades/h. Desenhar as três marcas temporais igualmente espaçadas como se representassem intervalos iguais distorceria a leitura da velocidade de mudança. Uma linha entre amostras não demonstra que a evolução real foi linear entre elas.

taxa média=(y₁−y₀)/(t₁−t₀)

## Em uma escala logarítmica, distância igual representa fator igual

No eixo logarítmico de base 10, os valores 1,10,100 ficam igualmente espaçados porque seus logaritmos são 0,1,2. Os acréscimos originais,9 e 90, são diferentes, mas os fatores são ambos 10. Essa escala ajuda a comparar ordens de grandeza; ela não usa a mesma regra de alturas do painel linear. Zero e números negativos não têm posição nesse eixo logarítmico real. Sempre confira qual transformação o eixo declara.

## Histograma usa intervalos e áreas, não apenas alturas

Barras de categorias e histogramas de intervalos não têm a mesma leitura. No histograma de densidade relativa, a área de cada retângulo é a frequência relativa da faixa. Se quatro observações se dividem em duas nas faixas[0,1) e duas em[1,3], cada área deve ser 1/2. As larguras 1 e 2 exigem alturas 1/2 e 1/4. Usar alturas iguais produziria áreas diferentes. A soma das áreas é 1; a altura tem unidade inversa da variável. O código recebe contagens prontas e não decide a regra de classificação nas bordas.

densidade=frequência relativa/largura

## Valor ausente é diferente de valor zero

Se falta uma observação num período, não sabemos que a quantidade foi zero. Registrar 0 sem evidência muda diferenças, médias e linhas. A orientação da ONS consultada recomenda deixar claro o intervalo sem dado e anotar a ausência. Também não devemos preencher uma lacuna com uma linha contínua sem explicar a suposição de interpolação. Compare categorias, períodos e amostras compatíveis antes de atribuir significado a diferenças.

## Associação desenhada não prova uma causa

Duas séries que crescem juntas podem refletir tendência compartilhada, mudança de coleta, outros fatores ou coincidência. Um desenho ajuda a explorar a associação; não demonstra sozinho que uma variável causou a outra. A conclusão deve acompanhar os dados realmente disponíveis, a origem das observações e as hipóteses de análise. Nesta aula não inferimos causalidade ou representatividade populacional.

## O painel conserva os dados; o laboratório confere as contas

Use o controle para alternar a origem entre 0 e 90. Os valores 100 e 110, a diferença 10 e o aumento 10% permanecem iguais; a razão das alturas muda. Há rótulos, marca de quebra e relatório textual para acompanhar a figura por teclado. O Python usa Fraction para variações, pontos percentuais, taxas em intervalos reais e densidades de histograma. Testes de exemplos não certificam qualquer gráfico, desenho de coleta ou domínio pessoal. Notas assistidas por IA, pendentes de revisão de Jhuann e uso com aluno.

## Exercícios originais e resoluções

Qual o aumento percentual de 100 para 110? **Resolução:** 100×10/100=10%.

Eixo vertical cortado muda a porcentagem real dos dados? **Resolução:** Muda o desenho, não os valores.

De 100 para 110, qual a mudança absoluta em unidades? **Resolução:** 110−100=10 unidades. Isso não é ainda uma porcentagem.

Qual o aumento percentual de 10 para 20? **Resolução:** 100×(20−10)/10=100%.

No eixo iniciado em 90, qual a razão entre as alturas desenhadas para 110 e 100? **Resolução:** (110−90)/(100−90)=20/10=2.

Qual a razão entre os valores 110 e 100, independentemente do eixo? **Resolução:** 110/100=1,1. A razão das alturas cortadas não substitui essa conta.

Uma taxa passa de 20% para 25%. Quantos pontos percentuais ela sobe? **Resolução:** 25−20=5 pontos percentuais.

Na mesma passagem 20%→25%, qual o aumento relativo em porcentagem? **Resolução:** 100×(25−20)/20=25%.

Qual a variação percentual de 110 para 100? Pode responder como fração em unidades de porcentagem. **Resolução:** 100×(100−110)/110=−100/11%, aproximadamente−9,09%.

Entre t=1h e t=3h, um valor sobe de 110 para 120. Qual a taxa média em unidades/h? **Resolução:** (120−110)/(3−1)=5 unidades/h.

Metade das observações está numa faixa de largura 2. Qual a densidade relativa de frequência nessa faixa? **Resolução:** (1/2)/2=1/4. A área do retângulo continua 1/2.

Um período sem observação pode ser registrado como zero apenas porque falta o dado? **Resolução:** Ausência não informa valor zero. O registro exige esclarecer o que não foi observado e a política aplicada.

## Referências e laboratório

Magalhães e Lima — Noções de Probabilidade e Estatística,7ª edição; orientação pública da Office for National Statistics sobre gráficos de colunas.

Magalhães/Lima §1.2, recortes pp.13–15/PDF 28–30, consulta textual parcial em 26/10/2026: proporção visual, barras e área de histograma. ONS, Column chart, seções Axis e Irregular and missing data, consulta direta na mesma data. Sem leitura integral do capítulo; números, demonstração, cálculos e código originais.

[ONS: Column chart](https://service-manual.ons.gov.uk/data-visualisation/chart-types/column-chart). O livro foi consultado em exemplar autorizado; páginas e figuras não distribuídas.

`relative_change` exige base positiva e final não negativo; retorna fração, não o número em porcentagem. `bar_comparison` exige origem não negativa abaixo de ambos os valores. `rate_change` distingue pontos e variação relativa; taxa inicial zero deixa relativa None. `secant` usa tempos reais crescentes. `histogram_density` recebe bordas crescentes e contagens inteiras não negativas de total positivo; não atribui observações às faixas.

Executar: `python 3 -m unittest discover -s labs/graficos-escala -t .` e `node labs/graficos-escala/test_axis.cjs`. O modelo interativo integrado permanece em schoolmath-models.js, com controle cut preservado e relatório ampliado. Não houve nova medição real, inferência causal ou certificação de competência. Rascunho assistido por IA para revisão pessoal.
