# Cinemática 1D — sinais, inversão e distância

## Escolha o eixo antes de interpretar os sinais

Descrevemos uma partícula numa reta. A posição x é medida em relação a uma origem, e o sentido positivo do eixo é uma escolha. O relógio começa em t=0, com posição x₀ e velocidade v₀. O exemplo original usa x₀=0, v₀=2 m/s e aceleração constante a=1 m/s². Nestas notas, x e s do exemplo anterior representam a mesma coordenada de posição, não distância total percorrida. Números e trajetórias são modelos didáticos, sem dados experimentais.

## Velocidade média usa deslocamento, não o caminho inteiro

Num intervalo t₁>t₀, a velocidade média é [x(t₁)−x(t₀)]/(t₁−t₀). Ela tem sinal e pode ser zero apesar de o corpo ter se movido. Rapidez média é distância percorrida dividida pelo mesmo tempo e é não negativa. Se o movimento muda de sentido, substituir a distância pelo módulo do deslocamento pode dar resultado errado.

v_média=Δx/Δt; rapidez média=distância/Δt

## Velocidade e aceleração são inclinações de gráficos diferentes

A velocidade instantânea é o limite de velocidades médias para um intervalo cada vez menor, quando o limite existe: v=dx/dt. No gráfico x versus t, ela é a inclinação da tangente; não a altura do gráfico. A aceleração a=dv/dt é a inclinação do gráfico v versus t. Posição zero não exige velocidade zero. Velocidade zero em um instante não exige aceleração zero. As unidades são m, m/s e m/s², respectivamente.

v=dx/dt; a=dv/dt

## Aceleração constante permite integrar a velocidade

Assuma que a mantém o mesmo valor durante todo o intervalo. A variação da velocidade é a área com sinal sob o gráfico de a: v(t)−v₀=at, portanto v(t)=v₀+at. Isso recupera v(0)=v₀ e produz um gráfico de velocidade linear. Se a variar, essa expressão com um único valor de a deixa de descrever o movimento em geral.

v(t)=v₀+at

## A posição é a acumulação da velocidade com sinal

Integre v₀+aτ desde τ=0 até τ=t. A parcela v₀ acumula v₀t; a parcela linear aτ acumula at²/2. Assim x(t)=x₀+v₀t+at²/2. Derivar essa expressão devolve v₀+at; derivar novamente dá a. Todos os termos somados à posição têm unidade de comprimento. O valor inicial x₀ não desaparece ao integrar: é uma condição do problema.

x(t)=x₀+v₀t+at²/2

## A média das velocidades nas pontas tem uma hipótese

Para um gráfico v versus t linear, a área orientada no intervalo é a área do trapézio: Δx=[v(t₀)+v(t₁)]Δt/2. Logo a velocidade média coincide com a média aritmética das velocidades das pontas. No exemplo original, v(0)=2 e v(3)=5 m/s, então v_média=3,5 m/s e Δx=10,5 m. Essa regra não vale para uma velocidade arbitrária: v=t² entre 0 e 1 tem média 1/3, enquanto a média das pontas é 1/2.

a constante ⇒ v_média=[v(t₀)+v(t₁)]/2

## Aceleração negativa pode aumentar a rapidez

Aceleração negativa significa que v diminui algebricamente. Se v também é negativa, seu módulo cresce: por exemplo, passar de −2 para −4 m/s aumenta a rapidez de 2 para 4 m/s. Onde v≠0, v e a com sinais iguais aumentam a rapidez; sinais opostos a diminuem. Uma verificação é d(v²)/dt=2va. No instante de inversão v=0, esse teste de sinais não fornece sozinho o comportamento dos dois lados; examine antes e depois.

d(v²)/dt=2va

## Velocidade zero não significa ficar parado dali em diante

Use um segundo modelo x₀=0, v₀=6 m/s e a=−2 m/s². Então v=6−2t e x=6t−t². Em t=3 s, v=0 e x=9 m. Antes disso, v>0; depois, v<0. O corpo muda de sentido, pois a aceleração continua negativa. Para permanecer parado seria necessário mudar a aceleração após esse evento; isso seria outro modelo, não consequência da fórmula.

t_inversão=3 s; x_inversão=9 m

## A distância precisa separar os trechos de sentidos diferentes

Entre 0 e 6 s no segundo exemplo, o corpo vai de x=0 a x=9 m e volta a x=0. O deslocamento é zero, mas a distância é |9−0|+|0−9|=18 m. A velocidade média é 0/6=0 m/s e a rapidez média é 18/6=3 m/s. Geometricamente, a área de v acima do eixo t e a área abaixo têm sinais opostos: cancelam no deslocamento, mas somam em módulo para a distância.

Δx=0 m; distância=18 m; rapidez média=3 m/s

## A mesma posição pode ocorrer com velocidades diferentes

A equação x=8 m no segundo modelo dá 6t−t²=8, ou (t−2)(t−4)=0. O corpo passa por x=8 m em t=2 s, indo no sentido positivo com v=2 m/s, e em t=4 s, voltando com v=−2 m/s. Uma posição isolada não determina o estado de movimento. Ao resolver uma equação para o tempo, confira todas as raízes e o intervalo em que o modelo foi assumido.

## Eliminar o tempo não elimina a convenção de sinais

Para aceleração constante, a derivada de v²−2ax é 2va−2av=0. Assim v²−v₀²=2a(x−x₀). Essa relação é útil, mas contém o quadrado da velocidade: para x=8 m, fornece v²=4, permitindo +2 ou −2 m/s. A história do movimento escolhe o ramo. Para a=0 ela também é válida, mas a igualdade de quadrados sozinha não substitui a informação de velocidade constante.

v²−v₀²=2a(x−x₀)

## Mudar a origem não muda deslocamento nem velocidade

Se a nova coordenada é x′=x+c, com c constante, todas as posições recebem o mesmo acréscimo. A diferença x′(t₁)−x′(t₀) permanece igual à anterior, e derivar a constante dá zero. Já inverter o sentido do eixo muda os sinais das componentes de posição, velocidade e aceleração. Distância e rapidez não dependem dessa orientação. Uma translação de origem fixa não é uma mudança para um observador em movimento.

## O intervalo de validade faz parte da resposta

As expressões podem ser avaliadas matematicamente em muitos tempos, mas não incluem automaticamente paredes, colisões, propulsão que desliga ou frenagem que termina. O segundo exemplo representa um movimento sob aceleração negativa mantida, inclusive após t=3 s. Não o interprete como um veículo que freia e fica estacionado. Para gravidade uniforme sem arrasto, a componente vertical de projéteis reutiliza essa cinemática com a=−g, junto ao tempo comum dos dois eixos.

## O laboratório calcula distância por trechos exatos

O código racional recebe condições iniciais e tempos não negativos. No intervalo, calcula se v=0 ocorre no interior; nesse caso separa os dois trechos antes de somar comprimentos. Retorna deslocamento, distância, velocidade média e rapidez média. Aceita também a=0 e repouso. O painel existente usa valores aproximados; o arquivo baixável usa Fraction. Unidades e validade física são responsabilidade de quem escolhe os parâmetros. Movimento com aceleração variável e inferência a partir de medições permanecem pendentes.

## Exercícios originais e resoluções

Com s₀=0, v₀=0 e a=2 m/s², qual é a posição em t=4 s, em metros? **Resolução:** s=0.5×2×4²=16 m.

Velocidade negativa e aceleração negativa fazem a rapidez: **Resolução:** A velocidade se torna mais negativa e seu módulo cresce.

No exemplo original v₀=2 m/s, a=1 m/s², qual v em t=3 s, em m/s? **Resolução:** 2+1×3=5 m/s.

Com x₀=0, v₀=2 m/s e a=1 m/s², qual a velocidade média de 0 a 3 s, em m/s? **Resolução:** Δx=10,5 m; divida por 3 s: 3,5 m/s.

Para x=6t−t² em metros, quanto tempo até a mudança de sentido, em s? **Resolução:** v=6−2t=0 dá t=3 s, com troca de sinal.

No modelo x=6t−t², qual a posição em t=3 s, em m? **Resolução:** 18−9=9 m.

No mesmo modelo, qual o deslocamento entre t=0 e t=6 s, em m? **Resolução:** x(6)=0 e x(0)=0; a diferença é zero.

No mesmo modelo, qual a distância percorrida entre t=0 e t=6 s, em m? **Resolução:** Vai até 9 m e retorna: 9+9=18 m.

Qual a rapidez média nesse percurso de 0 a 6 s, em m/s? **Resolução:** 18 m/6 s=3 m/s.

Para x=6t−t², qual a velocidade em t=4 s, em m/s? **Resolução:** 6−2×4=−2 m/s; o corpo está voltando.

Para x=6t−t², qual a posição em t=2 s, em m? **Resolução:** 12−4=8 m, mesma posição de t=4 s, com outra velocidade.

No instante de inversão do modelo x=6t−t², qual a aceleração em m/s²? **Resolução:** A segunda derivada é −2 em todos os instantes do modelo, inclusive t=3 s.

## Referência e laboratório

H.M.Nussenzveig — Curso de Física Básica, vol.1, Mecânica,5ª edição revista e atualizada, Blucher2013,4ª reimpressão2017; exemplar autorizado.

Consulta textual parcial em26/10/2026: §§2.1–2.3, pp.41–47 (PDF42–48), e §§2.4–2.5, pp.50–53 (PDF51–54). Sem leitura integral do capítulo. Derivações, segundo exemplo, figura e testes são próprios.

`state(t,x0=0,v0=2,a=1)` retorna posição, velocidade e aceleração. `interval(t0,t1,...)` exige 0≤t0<t1 e retorna deslocamento, distância, velocidade média e rapidez média. Inteiros e Fraction apenas, sem bool ou floats. Não há colisão, frenagem com parada, unidades automáticas ou validação experimental.

Executar: `python3 -m unittest discover -s labs/cinematica-sinais -t .`. O oráculo de distância usa um caminho poligonal em grade1/12s para parâmetros inteiros escolhidos cujo instante de inversão pertence à grade. Isso confere esses casos finitos e não prova a validade para qualquer movimento. Exemplos e painel preservados; revisão de Jhuann pendente.
