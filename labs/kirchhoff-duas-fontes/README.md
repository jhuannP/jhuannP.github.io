# Kirchhoff: duas fontes e uma referência de potencial

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão de Jhuann.

## Primeiro declare o circuito e o regime

Nesta aula, fontes ideais mantêm tensões constantes e resistores ôhmicos têm resistências positivas e constantes. Fios ideais conectam pontos de mesmo potencial. Trabalhamos em regime estacionário, sem acúmulo relevante de carga nos nós, efeitos indutivos ou propagação. O circuito é um modelo concentrado: cada elemento tem tensão e corrente bem definidas. A escolha dessas hipóteses antecede as equações. Circuitos são apoio editorial desta trilha, não um bloco autônomo confirmado no programa oficial.

## Escolher um sentido não fixa o resultado

Uma corrente recebe um sentido de referência antes do cálculo. Se o resultado é positivo, o fluxo de carga positiva ocorre no sentido escolhido; se é negativo, ocorre no oposto. Inverta a seta e o valor algébrico também muda de sinal, sem alterar o circuito. Não apague um sinal negativo para forçar a resposta a concordar com o desenho. Na convenção de um resistor, a diferença de potencial no sentido de referência da corrente é uma queda RI.

ΔV no percurso da corrente de referência=−RI

## A regra dos nós expressa conservação de carga

Para um nó sem acumulação relevante, a soma orientada das correntes é zero. No desenho abaixo, I₁ e I₂ têm setas entrando no nó superior e I₃ sai para a resistência central. Escrevemos I₁+I₂−I₃=0, mesmo antes de saber seus sinais. A relação é uma restrição de conservação e não determina as correntes sozinha: também precisamos das relações dos elementos e de suas conexões.

I₁+I₂=I₃

## A referência zero ajuda a escrever as malhas

Fixe o nó inferior como potencial zero. Uma fonte ideal com polo positivo acima estabelece o potencial do terminal superior em E. Percorrer a fonte de baixo para cima produz +E; atravessá-la no sentido contrário produz −E. Para o exemplo antigo de 12 V e resistores de 2 Ω e 4 Ω em série, a volta orientada dá 12−2I−4I=0 e I=2 A. As quedas 4 V e 8 V confirmam a soma. Não some apenas módulos sem acompanhar o percurso.

12−2I−4I=0

## Agora o nó superior é a incógnita

O novo circuito tem dois ramos de alimentação. O terminal superior da fonte E₁=12 V liga-se ao nó U por R₁=2 Ω; o terminal superior de E₂=6 V liga-se ao mesmo nó por R₂=3 Ω. As duas fontes têm seu terminal inferior no nó zero e polo positivo acima. Um terceiro resistor R₃=6 Ω liga U diretamente ao nó zero. Defina I₁=(E₁−U)/R₁ e I₂=(E₂−U)/R₂, entrando em U, e I₃=U/R₃ saindo dele. Essas definições fixam todos os sinais.

I₁=(E₁−U)/R₁; I₂=(E₂−U)/R₂; I₃=U/R₃

## Resolver uma equação de nó

Substitua as três relações no balanço: (12−U)/2+(6−U)/3=U/6. Multiplique por 6 Ω para eliminar os denominadores: 3(12−U)+2(6−U)=U, com as tensões medidas em volts. Abra os parênteses: 36−3U+12−2U=U. Portanto 48=6U e U=8 V. Em forma geral, U é a soma E₁/R₁+E₂/R₂ dividida pela soma das três condutâncias 1/R₁+1/R₂+1/R₃. O numerador tem unidade de ampère e o denominador de siemens; a razão é volt.

U=8 V

## Interpretar cada corrente e conferir as malhas

Com U=8 V, I₁=(12−8)/2=2 A, I₂=(6−8)/3=−2/3 A e I₃=8/6=4/3 A. O sinal de I₂ indica fluxo do nó de 8 V para o ramo da fonte de 6 V. O balanço é 2−2/3=4/3. As duas voltas também fecham: 12−2×2−8=0 e 6−3×(−2/3)−8=0. No segundo ramo, percorrer o resistor no sentido escolhido aumenta o potencial em 2 V porque a corrente real tem sentido contrário.

6−3×(−2/3)−8=0

## Uma fonte pode absorver potência

Defina potência fornecida por cada fonte como EᵢIᵢ, com Iᵢ orientada para fora de seu terminal positivo. Valor positivo significa fornecimento; negativo significa absorção. No exemplo, a fonte de 12 V fornece 24 W, e a de 6 V tem potência fornecida −4 W: absorve 4 W. Isso é uma interpretação do modelo ideal, sem especificar tecnologia ou um procedimento para carregar uma bateria real. A convenção passiva, com corrente entrando no terminal positivo, usa potência absorvida e inverte esse sinal.

Pfornecida,2=6×(−2/3)=−4 W

## A dissipação oferece uma conferência independente

Em cada resistor, P=RI² é não negativa. Os valores são P₁=2×2²=8 W, P₂=3×(−2/3)²=4/3 W e P₃=6×(4/3)²=32/3 W. A soma é 20 W. As fontes fornecem, em termos líquidos, 24−4=20 W. O balanço também pode ser deduzido: substitua E₁=R₁I₁+U e E₂=R₂I₂+U em E₁I₁+E₂I₂; o termo U(I₁+I₂) vira UI₃=R₃I₃² pela regra do nó. Assim a identidade não é apenas uma coincidência numérica.

ΣPfornecida=ΣRI²=20 W

## Nós e malhas são duas formas de organizar a mesma rede

Elimine U usando U=R₃(I₁+I₂). As equações das fontes ficam E₁=(R₁+R₃)I₁+R₃I₂ e E₂=R₃I₁+(R₂+R₃)I₂. Resolver esse sistema fornece as mesmas correntes que a equação do nó. O determinante é R₁R₂+R₁R₃+R₂R₃, estritamente positivo quando os três resistores são positivos; portanto há solução única nesta rede. Isso não demonstra solvabilidade de qualquer circuito com fontes ideais ou elementos não lineares.

Determinante=R₁R₂+R₁R₃+R₂R₃>0

## Os limites do modelo fazem parte da solução

Se há variação relevante de fluxo magnético, a descrição deve incluir a fem induzida e os elementos correspondentes; não se deve impor circulação eletrostática nula a uma situação regida por Faraday. Capacitores em transiente podem acumular carga, exigindo relações dependentes do tempo. Fios extensos e frequências altas também podem exigir uma descrição distribuída. A solução algébrica desta aula é estacionária e não responde a essas situações. O exemplo RC da trilha tem hipóteses e balanço próprios.

## O que o laboratório verifica

O código resolve apenas esta topologia de duas fontes e três resistores, com inteiros ou frações exatas e resistências positivas. Compara o método de nós a uma solução independente do sistema de malhas e confere conservação, sinais, escalas e potência. As fontes podem ter tensão negativa, interpretada em relação à orientação desenhada. Nenhuma corrente foi medida, nenhum dispositivo foi construído e nenhuma escolha de parâmetros demonstra segurança ou desempenho de um circuito real. O material permanece em rascunho para revisão pessoal.

## Exercícios e resoluções

- Qual corrente em A? **Resolução:** 12/(2+4)=2.
- Corrente negativa calculada significa necessariamente erro? **Resolução:** Pode indicar sentido oposto ao assumido.
- Na rede de duas fontes 12 V e 6 V com R₁=2 Ω, R₂=3 Ω e R₃=6 Ω, qual é U, em V? **Resolução:** (12−U)/2+(6−U)/3=U/6 leva a U=8 V.
- Com U=8 V, qual é I₁=(12−U)/2, em A? **Resolução:** I₁=4/2=2 A.
- Com U=8 V, qual é I₂=(6−U)/3, em A, no sentido escolhido? **Resolução:** I₂=−2/3 A; a corrente real está no sentido oposto à seta.
- Com U=8 V, qual é I₃=U/6, em A? **Resolução:** I₃=8/6=4/3 A.
- Quanto é I₁+I₂−I₃, em A, na solução? **Resolução:** 2−2/3−4/3=0: não há acumulação no nó.
- Qual a potência fornecida pela fonte de 12 V, em W? **Resolução:** 12×2=24 W.
- Qual a potência fornecida pela fonte de 6 V, em W, com I₂=−2/3 A? **Resolução:** 6×(−2/3)=−4 W; a fonte absorve quatro watts.
- Quanto dissipa o resistor R₂=3 Ω, em W, com I₂=−2/3 A? **Resolução:** RI²=3×4/9=4/3 W, não negativo.
- Qual a potência total dissipada pelos três resistores, em W? **Resolução:** 8+4/3+32/3=20 W, igual a 24−4 das fontes.
- Esta solução estacionária pode ser aplicada diretamente a qualquer circuito com fluxo magnético variável, sem incluir indução? **Resolução:** A indução relevante precisa entrar na descrição; as hipóteses desta rede resistiva não cobrem qualquer situação variável.

## Fontes e execução

[OpenStax, University Physics Volume 2, §10.3](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules), regras e convenções de sinais; [Feynman II, §22–1](https://www.feynmanlectures.caltech.edu/II_22.html), aproximações de circuitos. Consulta parcial em 22/10/2026. Topologia, dados, figura e código locais são originais. Nada foi construído ou medido. Este recorte é apoio editorial e não comprova cobertura integral do programa de Física III.

Na raiz do site: python3 -m labs.kirchhoff-duas-fontes.experiment; testes: python3 -m unittest discover -s labs/kirchhoff-duas-fontes -t .

Entradas em V e Ω como int ou Fraction; correntes em A, potências em W. Apenas resistências positivas. A topologia é fixa; solve não é um analisador de circuitos arbitrários. Fontes negativas significam tensão invertida relativamente à orientação de referência.


## Kirchhoff: rede de duas fontes — 22/10/2026

Aula f3-kirchhoff ampliada de três seções/dois exercícios para 12 seções/12 exercícios. Exemplo antigo de resistores em série, código, dois IDs e desafio preservados. Novo circuito estacionário: duas fontes ideais ao nó zero, resistores de alimentação e carga; equação de nó, malhas equivalentes, corrente com sinal e balanço de potência. A etapa continua sendo apoio editorial de circuitos e não fecha lacunas da ementa de Física III.

Dados originais: E₁=12 V, E₂=6 V, R₁=2 Ω, R₂=3 Ω, R₃=6 Ω. Resultado U=8 V; correntes orientadas I₁=2 A e I₂=−2/3 A entrando no nó, I₃=4/3 A saindo. Potências fornecidas pelas fontes 24 W e −4 W; resistor dissipa 8 W, 4/3 W e 32/3 W, total 20 W. Fonte 2 absorve 4 W sob a convenção declarada. Resultado de modelo ideal, sem dispositivo construído ou medido.

Fontes primárias consultadas parcialmente em 22/10/2026: [OpenStax, University Physics Volume 2, §10.3](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules), regras e convenções; [Feynman II, §22–1](https://www.feynmanlectures.caltech.edu/II_22.html), hipóteses de circuitos. Não se afirma leitura integral. Topologia, exemplo, figura, deduções e código locais são originais. Programa e situação acadêmica não foram alterados.

Laboratório: labs/kirchhoff-duas-fontes/. Cinco testes novos aprovados: valores do exemplo, comparação independente com sistema de duas malhas em 432 conjuntos racionais, conservação de carga/malhas/potência em 432 conjuntos inteiros, escala/troca de fontes/caso nulo e contratos. Doze testes de catálogo e 533 estruturas MathML aprovados após a figura. Suíte global não repetida; nenhum modelo interativo JavaScript alterado.

Navegador: esquema legível a 390 px, largura da página igual à tela, nenhum erro de console observado. Resposta −2/3 aceita para I₂; na potência fornecida da fonte 2, +4 rejeitado e −4 aceito. Prévia: kirchhoff-duas-fontes-mobile.jpg. O material permanece em rascunho assistido por IA para revisão de Jhuann.

Estado: Física III tem 14 aulas/95 exercícios, sete recortes desenvolvidos e sete introduções. Nove etapas, sete grupos parciais e duas lacunas; nenhum grupo completo. Catálogo global: 500 aulas/3002 exercícios em rascunho. Próxima revisão pessoal: reconstruir U, interpretar I₂ e conferir 24−4=20 W. Próximo aprofundamento global: retomar assunto de Matemática II, conferindo pré-requisitos e fonte. Notas pessoais e validação de domínio continuam pendentes. Saldo semanal: 93%; parada operacional em 65%.
