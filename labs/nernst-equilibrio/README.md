# Nernst e equilíbrio de uma espécie — notas de aula

Rascunho original para revisão pessoal.

## Por que um gradiente de concentração pode persistir

Difusão e efeito elétrico podem favorecer sentidos opostos de movimento de um íon. Uma diferença de potencial pode compensar o gradiente químico sem igualar concentrações. A pergunta desta aula é qual diferença de potencial equilibra um único íon ideal, e qual sentido de transferência passiva seria energeticamente favorecido fora desse ponto. Não calculamos a rapidez do movimento.



## Fixar interior, exterior e sinal da voltagem

Defina V=V_in−V_out. Um V negativo significa interior com potencial elétrico menor que o exterior. c_in e c_out são concentrações positivas da mesma espécie, nas mesmas unidades; z é o número de carga, positivo para cátion e negativo para ânion. A diferença de potencial é propriedade entre os lados, não o potencial absoluto de uma face.

V=V_in−V_out

## Uma relação termodinâmica para o íon ideal

Para soluções ideais com a mesma referência química nos dois lados, escrevemos a diferença de potencial eletroquímico molar como Δμ=μ_in−μ_out=RT ln(c_in/c_out)+zFV. O primeiro termo é químico; o segundo é elétrico. R tem unidade J/(mol K), T está em K, F em C/mol e V em volts; ambos os termos resultam em J/mol. Essa expressão é o modelo termodinâmico usado para justificar o balanço, não uma taxa de fluxo.

Δμ=RT ln(c_in/c_out)+zFV

## Derivar o potencial de Nernst

No equilíbrio desse íon, Δμ=0. Isolar V dá E=(RT/zF)ln(c_out/c_in). Inverter a razão troca o sinal do logaritmo; trocar z também muda o sinal. Usar log₁₀ requer o fator ln10, aproximadamente 2,302585. O índice que distingue concentrações externa/interna é parte da convenção e não pode ser trocado silenciosamente.

E=(RT/zF)ln(c_out/c_in)

## O número calculado não é uma constante universal

Neste laboratório, T=310 K, R=8,314 J/(mol K) e F=96485 C/mol são valores fixados e arredondados. Assim, para z=1, uma razão externa/interna de dez produz E≈61,5 mV. A temperatura precisa estar explícita: não transportamos automaticamente um coeficiente numérico para outra temperatura. As razões do painel são sintéticas, sem identificar concentrações de um neurônio específico.



## Exemplo: cátion mais concentrado no interior

Use z=+1 e c_in/c_out=10. A contribuição química é RT ln10>0. Em V=0, μ_in>μ_out, de modo que transferir esse íon para fora reduz o potencial eletroquímico, se houver via passiva. O equilíbrio requer V negativo, aproximadamente −61,5 mV: a parcela elétrica negativa compensa a química positiva. No laboratório, as concentrações são parâmetros fixos; não se simula como a membrana chega a essa voltagem.

E≈−61,5 mV para z=1 e c_in/c_out=10

## Para o ânion, confira novamente a carga

Mantendo a mesma razão c_in/c_out=10, mas z=−1, E muda para aproximadamente +61,5 mV. Em V=0, o gradiente químico ainda favorece saída de partículas; o sinal da carga muda a influência elétrica. Com concentrações iguais e V positivo, um ânion tem μ_in−μ_out<0 e sua entrada é favorecida. O sentido de movimento da espécie não é a mesma convenção de sinal de corrente elétrica.



## Usar E para interpretar uma voltagem qualquer

Substitua RT ln(c_in/c_out)=−zFE na expressão original. Obtemos Δμ=zF(V−E). Se Δμ>0, o interior está em potencial eletroquímico maior e a saída passiva é favorecida; se Δμ<0, a entrada é favorecida. Para z negativo, o sinal de V−E sozinho não fornece o sentido de movimento da espécie. O painel calcula Δμ antes de nomear o sentido.

Δμ=zF(V−E)

## Equilíbrio não significa que os íons parem

Em equilíbrio há balanço sem transporte líquido direcionado desse íon. Isso não exige ausência de movimentos microscópicos. Tampouco a ausência de corrente por uma membrana impermeável demonstra equilíbrio: sem canais ou outra via, pode haver força motriz e fluxo impedido. Uma previsão de tendência energética pressupõe uma via passiva disponível.



## Nernst não calcula permeabilidade ou velocidade

A equação usa carga, temperatura e razão de concentrações; não fornece número de canais, condutância ou cinética de abertura. Para obter uma corrente, é necessário um modelo de transporte e seus parâmetros. Não acrescentamos uma condutância artificial e não chamamos o gráfico de corrente–voltagem: o eixo vertical é energia molar.



## Um íon não determina sozinho o repouso completo

Uma membrana real pode conduzir várias espécies com potenciais de equilíbrio diferentes. Nessa situação, uma voltagem estacionária com corrente total nula não precisa coincidir com o equilíbrio individual de cada espécie. Bombas e transportadores podem manter gradientes consumindo energia. O painel não implementa essas correntes, a equação de Goldman, bombas ou potencial de ação.



## Carregar a membrana não esvazia todo o citosol

A separação de carga responsável pela voltagem se concentra junto à membrana; o volume de solução pode continuar aproximadamente eletroneutro. Não inferimos que um interior negativo tenha todos os seus íons negativos ou que o gradiente desapareça para formar E. O modelo considera concentrações fornecidas e não resolve inventário, capacitância ou evolução da carga.



## Como ler o painel e conferir unidades

Escolha o tipo de íon, q=log₁₀(c_in/c_out) e V em mV. A linha azul mostra Δμ total em kJ/mol, o tracejado preto mostra a contribuição química e o zero marca o balanço. E é o ponto onde a linha azul cruza zero; o outro ponto marca a voltagem escolhida. A conversão mV→V e J/mol→kJ/mol ocorre explicitamente no cálculo. Nem o eixo horizontal nem os controles representam tempo.



## O que deve ser verificado antes de generalizar

São soluções ideais, temperatura uniforme e referência química compatível entre os lados. Em soluções não ideais, atividades substituem concentrações na relação termodinâmica. Gradientes mantidos, permeabilidade e outros mecanismos precisam de modelos próprios. As referências do laboratório testam sinais, inversões e balanço, sem validar uma célula real ou demonstrar domínio pessoal.



## Exercícios e resoluções

### Com concentrações iguais, qual é E em mV, para qualquer z não nulo?

ln1=0, portanto E=0.

### Usando as constantes da aula, z=+1 e c_in/c_out=10, calcule E em mV.

E=−1000RT ln10/F≈−61,507433 mV.

### Para a mesma razão, trocando z de +1 para −1, calcule E em mV.

A inversão da carga troca o sinal do potencial de equilíbrio.

### Para ci/co=1, z=+1 e V=10 mV, quanto é Δμ em J/mol?

Δμ=F×0,010=964,85 J/mol.

### Para ci/co=1, z=−1 e V=10 mV, quanto é Δμ em J/mol?

A parcela elétrica muda de sinal: −964,85 J/mol.

### Dobrando a temperatura absoluta com razão e z fixos, por qual fator E é multiplicado?

E é proporcional à temperatura absoluta.

### Para z=−1, concentrações iguais e V positivo, qual transferência passiva da espécie é favorecida?

Δμ=zFV<0: μ_in<μ_out, portanto entrada é favorecida se houver via passiva.

### Conhecer E determina a quantidade de canais e a velocidade de transporte?

Esses parâmetros e uma lei cinética não estão na equação de Nernst.

### Em equilíbrio eletroquímico, todos os movimentos microscópicos precisam cessar?

O transporte direcionado líquido se anula, sem exigir imobilidade microscópica.

### Uma membrana impermeável sem corrente prova Δμ=0?

Pode haver força motriz com fluxo impedido por ausência de via.

### Um V de repouso com corrente total nula exige que cada íon esteja em seu equilíbrio individual?

Correntes de espécies diferentes podem se compensar; o painel não resolve esse sistema.

### Podemos trocar ln por log₁₀ sem mudar o coeficiente?

ln r=ln10 × log₁₀r; o fator precisa ser incluído.


## Equilíbrio iônico e Nernst — 22/10/2026

Nova aula `b4-nernst-equilibrio`: 14 seções/12 exercícios, duas fórmulas MathML, Python e desafio. Introduz V=V_in−V_out, z, razão de concentrações, diferença eletroquímica molar, derivação de E, inversões de sinal, unidades, tendência de transferência e limites de um modelo de uma espécie. Distingue corrente, via de passagem, rapidez e equilíbrio; não calcula repouso multi-iônico, Goldman, bombas ou potencial de ação.

Fonte privada consultada parcialmente: Bear, Connors e Paradiso, Neurociências: Desvendando o Sistema Nervoso, quarta edição brasileira, Artmed 2017, capítulo 3 pp.66–71/PDF108–113. Quadro 3.2 p.70/PDF112 inspecionado visualmente para conferir Nernst, carga e logaritmo. A correspondência +42 foi confirmada neste recorte, não generalizada ao livro todo. Metadados editoriais permanecem os verificados anteriormente. A expressão do potencial eletroquímico e a derivação são uma extensão didática própria para justificar o balanço. Não reproduzidas figuras, tabelas de concentrações, dados ou PDF do livro. Programa oficial não reaberto; seleção efetiva dos sistemas pela turma continua não confirmada.

Exemplo próprio com T=310 K, R=8,314 J/(mol K), F=96485 C/mol, razão ci/co=10: para z=+1, E≈−61,507433 mV; para z=−1, sinal oposto. Não se adota automaticamente o coeficiente arredondado do livro para outra temperatura. Modelo Δμ=RT ln(ci/co)+zFV=zF(V−E); Δμ>0 favorece saída da espécie, Δμ<0 entrada, se houver via passiva. Para ânion com concentrações iguais e interior positivo, entrada é favorecida, sem confundir movimento de partículas e sinal da corrente.

Laboratório `python3 labs/nernst-equilibrio/experiment.py`; testes `python3 -m unittest discover -s labs/nernst-equilibrio -t .`. API geral aceita concentrações/T positivas finitas e z inteiro não nulo. Painel restrito a z ±1, q=log10(ci/co) entre −2 e 2 e V entre −150 e 150 mV. Concentrações são parâmetros fornecidos, não resultados de conservação resolvida. Não há tempo, fluxo ou número de canais. As curvas mostram energia molar; não são corrente–voltagem ou carregamento capacitivo.

Novo `nernst-equilibrium-models.js`, namespace NernstEquilibriumModels/painel nernstEquilibrium. Azul Δμ, preto tracejado parcela química, linha pontilhada zero. Pontos distinguem E no zero e V selecionado, descritos por texto/valores. Conversões mV→V e J/mol→kJ/mol explícitas. Exibição de zero normalizada para evitar −0 em quantidades nulas, sem modificar os valores físicos do modelo.

Cinco testes novos: equilíbrio e deslocamentos em 56 estados; troca dos lados, sinal/carga, escala de concentração e temperatura; recuperação independente da razão por exponencial de Boltzmann e exemplos; resposta afim à voltagem/sinal do ânion; contratos. Trinta referências Decimal de 60 dígitos comparadas no JS, incluindo potenciais e contribuições. Suíte completa: 802 testes Python, 285 demonstrações/855 cenários JS e 472 estruturas MathML aprovados. Após corrigir somente exibição de zero, JS repetido; após ajustar texto da resolução em português, catálogo repetido. Não se afirma validação de uma célula real.

Navegador: teclado confirmou igualdade de concentrações/V=0 como equilíbrio e ânion/V=+150 mV com entrada favorecida. Resposta −61,507433 aceita na questão 2. Layout 390 px com curva, controles e valores legíveis, sem transbordamento horizontal e console sem erros observados. Prévia `nernst-equilibrio-mobile.jpg`; viewport restaurado. Material em rascunho para revisão de Jhuann.

Biologia IV: cinco aulas próprias/58 exercícios; quatro grupos parciais/dezoito lacunas em 22 subitens, nenhum completo. Nernst amplia o recorte de células/comunicação, sem marcar novos sistemas completos ou reivindicar fisiologia integrada. Percurso neural e bibliografia atualizados, preservando a diferença entre material preparado e notas pessoais. Catálogo global: 489 aulas/2643 exercícios.

Próxima revisão pessoal: reconstruir o sinal de E para cátion/ânion, explicar Δμ e responder por que a ausência de corrente numa membrana impermeável não prova equilíbrio. Próxima unidade neural: repouso multi-iônico, após leitura específica de fontes. Próxima alternância global: sequência e lacunas de Química IV. Samsung Notes, materiais da turma e objetivo integral permanecem pendentes. Saldo semanal após bloco: 98%; parada operacional: 65%.
