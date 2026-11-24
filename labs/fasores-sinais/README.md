# Complexos, fasores e sinais reais

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão de Jhuann.

## Um complexo guarda duas coordenadas

Escreva Z=a+ib, com a e b reais e i²=−1. Seu módulo é A=√(a²+b²); quando Z≠0, um argumento φ satisfaz a=A cosφ e b=A sinφ. A fase é determinada apenas módulo 2π. No plano complexo, a e b são coordenadas da representação, não duas posições físicas de um objeto. No exemplo abaixo, ambas têm unidade de centímetro porque representam a amplitude de um deslocamento.

Z=A exp(iφ)

## O quadrante e o caso zero fazem parte da definição

Para Z=3+4i, A=5 e φ=atan2(4,3). A função atan2 recebe as duas coordenadas e preserva o quadrante; usar apenas arctan(b/a) falha quando a=0 e pode confundir Z com −Z. Se Z=0, a amplitude é zero e qualquer ângulo produziria o mesmo complexo: não há uma fase única. O laboratório retorna None nesse caso, mesmo que alguma biblioteca escolha numericamente o valor zero.

A=√(a²+b²)

## Declare qual sinal real o fasor representa

Adotamos a convenção q(t)=Re[Z exp(iωt)], com frequência angular comum ω>0. Pela identidade de Euler, exp(iθ)=cosθ+i sinθ. Multiplique (a+ib)(cosωt+i sinωt) e separe a parte real: q(t)=a cosωt−b sinωt. O sinal negativo da parcela de seno vem de i²=−1. Se q está em cm, Z também está em cm; t está em segundos e ω em rad/s. O argumento ωt é um ângulo em radianos.

q(t)=a cos(ωt)−b sin(ωt)

## Exemplo resolvido: reconstruir a oscilação

Tome Z=3+4i cm e ω=2 rad/s. O sinal é q(t)=3 cos(2t)−4 sin(2t), em cm. A amplitude de pico é 5 cm, não o valor q(0)=3 cm. Em t=π/4 s, o ângulo é π/2: o cosseno zera e o seno vale um, dando q=−4 cm. Esse valor negativo indica o sentido do deslocamento no eixo físico, sem tornar a amplitude negativa. A forma polar equivalente é 5 cos(2t+φ), com φ=atan2(4,3).

q(π/4 s)=−4 cm

## Somar sinais de frequência comum

Se q₁(t)=Re[Z₁ exp(iωt)] e q₂(t)=Re[Z₂ exp(iωt)], a linearidade da parte real permite reunir o fator exp(iωt): q₁+q₂=Re[(Z₁+Z₂)exp(iωt)]. Portanto somamos as coordenadas complexas e só depois calculamos módulo e fase. Isso descreve a soma matemática dos sinais; uma aplicação física por superposição exige que o modelo permita essa soma. As duas amplitudes precisam ter unidades compatíveis.

Ztotal=Z₁+Z₂

## Dois módulos cinco podem produzir módulo oito

Considere Z₁=3+4i cm e Z₂=−3+4i cm na mesma frequência ω=2 rad/s. Cada módulo é 5 cm. Somando coordenadas, as partes reais se cancelam e as imaginárias dão 8i cm. O módulo total é 8 cm e a fase é π/2, módulo 2π. O sinal resultante é −8 sin(2t) cm. Somar apenas os módulos produziria 10 cm e perderia a fase relativa. Em t=0, ambos os sinais somam zero, embora a amplitude total seja oito.

Ztotal=8i cm; |Ztotal|=8 cm

## A parcela cruzada explica a interferência

Expanda (Z₁+Z₂)(Z₁+Z₂)*, onde o asterisco indica conjugação complexa: o quadrado do módulo total é a soma dos quadrados dos módulos mais 2Re(Z₁Z₂*). No exemplo, Z₁Z₂*=7−24i cm². Assim 25+25+2×7=64 cm² e a amplitude é √64=8 cm. Em forma polar, o termo cruzado é 2A₁A₂ cos(φ₁−φ₂). A soma direta dos módulos ocorre quando as fases estão alinhadas e as amplitudes são não negativas.

|Z₁+Z₂|²=|Z₁|²+|Z₂|²+2Re(Z₁Z₂*)

## Cancelamento não deixa uma fase observável

Os fasores 1 e −1 têm módulos um, mas a soma é zero. Com a mesma frequência, os sinais se cancelam em todos os instantes e a fase do resultado fica indefinida. Um valor muito pequeno por arredondamento não é matematicamente igual a zero. O laboratório usa None apenas para zero exato; não transforma um critério numérico arbitrário em definição de fase. Perto do cancelamento, pequenas perturbações relativas podem alterar bastante o argumento.

1+(−1)=0

## Derivar o sinal mantém a convenção

Derivar exp(iωt) em relação ao tempo multiplica por iω. Logo a amplitude complexa da velocidade é iωZ e a da aceleração é −ω²Z. Isso também se verifica derivando os termos de seno e cosseno. Para Ztotal=8i cm e ω=2 rad/s, iωZtotal=−16 cm/s. Assim a velocidade em t=0 é −16 cm/s. Não confunda a derivada temporal de uma oscilação com a derivada de uma função complexa em todas as direções, tema da próxima aula.

Amplitude da velocidade: iωZ

## A origem do tempo muda a fase de referência

Se τ=t−t₀, então t=τ+t₀. Substituindo no sinal, o novo fasor é Znovo=Z exp(iωt₀), pois o fator exp(iωτ) fica separado. O módulo não muda, mas a fase ganha ωt₀. Uma mudança comum de origem preserva a diferença de fase entre sinais de mesma frequência. Por isso uma fase isolada precisa de uma referência temporal; amplitudes complexas não devem ser comparadas sem verificar a convenção utilizada.

Znovo=Z exp(iωt₀)

## Frequências diferentes não compartilham um único fator

Compare cos(t)+cos(2t). Em t=0 a soma é dois; em t=π ela é zero. Somar os dois coeficientes como se ambos tivessem frequência um produziria 2cos(t), que vale −2 em t=π: outra função. Mantenha um fasor por frequência e some os sinais reconstruídos. A redução a uma única frequência exige condições especiais, como componentes que se anulem; não é autorizada apenas por haver uma soma. Também não foi adotada aqui a convenção de amplitudes eficazes (RMS).

cos(π)+cos(2π)=0

## O que conferir no laboratório

O código reconstrói sinais reais, calcula módulo e fase e verifica a superposição com frequência comum. A derivada analítica é comparada a diferenças centrais; essa comparação numérica não substitui a derivação. Uma mudança da origem do tempo é conferida nas duas representações. Os números usam ponto flutuante, com tolerâncias explícitas nos testes, e não demonstram precisão para amplitudes ou frequências arbitrariamente grandes. Transientes, resposta de circuitos, impedância, frequências múltiplas gerais e analiticidade continuam fora deste recorte.

## Exercícios e resoluções

- Qual quadrado do módulo do exemplo? **Resolução:** 1²+1²=2.
- O fasor zero tem uma fase física unicamente determinada? **Resolução:** A fase na origem é indeterminada.
- Qual a amplitude de pico, em cm, de Z=3+4i cm? **Resolução:** √(3²+4²)=5 cm.
- Para Z=3+4i cm e ω=2 rad/s, quanto é q(0), em cm? **Resolução:** q(0)=3cos0−4sin0=3 cm.
- No mesmo sinal, quanto é q(π/4 s), em cm? **Resolução:** O argumento é π/2: 3×0−4×1=−4 cm.
- Some Z₁=3+4i e Z₂=−3+4i, em cm. Qual a parte real do total, em cm? **Resolução:** 3+(−3)=0.
- Na mesma soma, qual a parte imaginária do total, em cm? **Resolução:** 4+4=8 cm.
- Qual a amplitude de pico, em cm, da soma Ztotal=8i cm? **Resolução:** |8i|=8 cm, embora cada fasor inicial tenha módulo cinco.
- No exemplo, Re(Z₁Z₂*) vale quanto, em cm²? **Resolução:** (3+4i)(−3−4i)=7−24i; a parte real é sete.
- Para Ztotal=8i cm e ω=2 rad/s, qual a velocidade em t=0, em cm/s? **Resolução:** iωZtotal=i×2×8i=−16 cm/s.
- Com mesma frequência, qual o módulo da soma dos fasores 1 e −1? **Resolução:** A soma é zero e seu módulo é zero; a fase do resultado não é única.
- Os coeficientes de cos(t) e cos(2t) podem ser somados diretamente para formar 2cos(t)? **Resolução:** As frequências são diferentes. Em t=π, a soma real é zero e 2cos(t) vale −2.

## Fonte e execução

[MIT 18.03, Lecture Note 6](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/mit18_03s10_c06/), seção [2], página PDF2; consulta parcial em 22/10/2026 para identidade de Euler e interpretação geométrica. Exemplos, deduções de soma e referência temporal, figura e código próprios; sem reprodução de notas ou exercícios.

Na raiz do site: python3 -m labs.fasores-sinais.experiment; testes: python3 -m unittest discover -s labs/fasores-sinais -t .

Convenção exp(+iωt), amplitude de pico, ω>0. Números no laboratório representam coordenadas em cm, segundos e rad/s nos exemplos. Não há ajuste a dados reais, modelo de circuito ou evolução de fasores com frequências distintas em um único coeficiente.


## Complexos e fasores — 22/10/2026

Aula complexos-fasores ampliada de três seções/dois exercícios para 12 seções/12 exercícios, preservando o exemplo 1+i, código e desafio anteriores. Nova sequência: coordenadas, módulo e quadrante; fase zero indeterminada; convenção exp(+iωt), sinal real, frequência comum e unidades; soma e termo cruzado; cancelamento; derivada temporal; referência de tempo e limites. As amplitudes são de pico, não eficazes. Não se presume que qualquer sistema físico satisfaça superposição.

Fonte primária consultada parcialmente: [MIT 18.03, Spring 2010, Lecture Note 6](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/mit18_03s10_c06/), seção [2] Complex exponential, página PDF2, identidade de Euler e interpretação geométrica. Consulta em 22/10/2026; sem leitura integral, transcrição de exercícios ou reprodução de figura. Aplicações, exemplos numéricos, derivações, diagrama e laboratório locais são originais.

Exemplo em cm e rad/s: Z₁=3+4i e Z₂=−3+4i têm módulo cinco cada, mas somam 8i de módulo oito. Re(Z₁Z₂*)=7; 25+25+14=64 confirma o quadrado do módulo. Para ω=2, q(t)=−8sin(2t), q(0)=0 e q'(0)=−16 cm/s. A fase depende da origem do tempo; mudar τ=t−t₀ produz Znovo=Z exp(iωt₀). Frequências distintas são mantidas separadas; cos(t)+cos(2t) não é 2cos(t).

Laboratório em labs/fasores-sinais/: reconstrução de sinal, forma polar, derivada temporal e figura original. Cinco testes novos aprovados: superposição e identidade do termo cruzado para grade de coordenadas; reconstrução polar em quadrantes, fase nula e fase de pequeno fasor não nulo; derivada comparada à diferença central e mudança da origem; valores da aula e contraexemplo de frequências diferentes; entradas inválidas e não finitas. Doze testes de catálogo aprovados; 532 estruturas MathML conferidas antes da figura, sem alteração posterior de MathML. Catálogo revalidado após inclusão da figura. Suíte global e modelos JavaScript não foram alterados nem revalidados integralmente.

Navegador: figura e texto inspecionados em 390 px, largura da página igual à tela, nenhum erro de console observado. Na questão de velocidade, +16 foi rejeitado e −16 aceito. Prévia: fasores-sinais-mobile.jpg. Conteúdo continua em rascunho assistido por IA, com revisão pessoal de Jhuann pendente. Não comprova resultado da IC, experiência profissional ou domínio do tema.

Estado: Física Matemática é percurso próprio com 25 aulas/70 exercícios, dois recortes desenvolvidos e 23 introduções curtas; sem equivalência automática com uma disciplina USP. Catálogo global: 500 aulas/2992 exercícios. Próxima revisão pessoal: reconstruir o sinal 3cos(2t)−4sin(2t), conferir a soma vetorial e explicar o sinal de q'(0). Próximo bloco global: retomar uma lacuna de disciplina formal do ciclo básico, como circuitos em Física III, conferindo fontes e hipóteses. Saldo semanal: 93%; parada operacional em 65%.
