# Trigonometria escolar — triângulo, círculo e unidade angular

## Escolha o ângulo antes de nomear os catetos

Em um triângulo retângulo, a hipotenusa é o lado oposto ao ângulo reto. Para um dos ângulos agudos θ, o cateto oposto fica em frente a θ, e o adjacente liga esse vértice ao ângulo reto. Ao escolher o outro ângulo agudo, os papéis dos catetos trocam. A hipotenusa permanece a mesma. Portanto “oposto” não é um nome fixo de um lado sem a indicação do ângulo.

## As razões não dependem do tamanho do triângulo

Para θ agudo, sin θ=oposto/hipotenusa, cos θ=adjacente/hipotenusa e tan θ=oposto/adjacente. Triângulos semelhantes preservam os ângulos e multiplicam todos os lados pelo mesmo fator; esse fator cancela nas razões. Se os três lados estão em centímetros, as unidades também cancelam. Misturar um lado em metros com outro em centímetros antes de dividir impediria essa interpretação.

sin θ=o/h; cos θ=a/h; tan θ=o/a

## Um triângulo 3–4–5 permite conferir as três razões

Escolha θ oposto ao cateto de comprimento 3; o adjacente tem comprimento 4 e a hipotenusa 5, na mesma unidade. Então sin θ=3/5, cos θ=4/5 e tan θ=3/4. Para o outro ângulo agudo, o seno é 4/5 e o cosseno 3/5. A conta (3/5)²+(4/5)²=9/25+16/25=1 recupera Pitágoras dividido por 5². Esse exemplo é geométrico e não representa uma medição de campo.

## Graus contam partes de uma volta; radianos comparam arco e raio

Uma volta completa corresponde a 360°. Em um círculo de raio r, um arco de comprimento s corresponde ao ângulo θ=s/r em radianos. A volta tem comprimento 2πr, portanto mede 2π rad. Assim meia volta é 180°=π rad. A razão entre arco e raio usa a mesma unidade de comprimento; o radiano é dimensionalmente uma razão, mas escrever rad ajuda a identificar a grandeza angular. Para orientação, adotamos aqui o sentido anti-horário como positivo.

θ_rad=θ_graus×π/180

## Converta a unidade antes de usar uma fórmula

Para 30°, a medida em radianos é 30π/180=π/6. Para 90°, é π/2; para π/3 rad, a conversão de volta fornece 60°. Na relação s=rθ, θ deve estar em radianos. Se r=2 m e θ=π/3 rad, o arco tem comprimento 2π/3 m. Usar o número 60 nessa multiplicação trataria graus como se fossem radianos e produziria um resultado sem a interpretação geométrica correta.

## O círculo amplia a definição para além de ângulos agudos

No plano, coloque o centro do círculo unitário na origem e o lado inicial do ângulo no eixo x positivo. Após girar θ, o ponto do círculo é P=(cos θ,sin θ). No primeiro quadrante isso concorda com as razões do triângulo, pois a hipotenusa vale 1. Nos demais quadrantes, as coordenadas podem ser negativas; não são comprimentos negativos de catetos. Esta definição permite trabalhar com ângulos negativos e com mais de uma volta.

P=(cos θ,sin θ); cos²θ+sin²θ=1

## Os eixos e quadrantes determinam sinais

Em 0°, o ponto é (1,0); em 90°, (0,1); em 180°, (−1,0); em 270°, (0,−1). No segundo quadrante, x é negativo e y positivo: cosseno negativo e seno positivo. No terceiro, ambos são negativos; no quarto, só o seno é negativo. Por exemplo, 120° tem ângulo de referência de 60° e está no segundo quadrante, então cos 120°=−cos 60°=−1/2. A tangente é sin θ/cos θ e não está definida quando cos θ=0.

## Ângulos notáveis podem ser reconstruídos

Divida ao meio um triângulo equilátero de lado 2: cada triângulo retângulo tem hipotenusa 2 e um cateto de comprimento 1. Isso fornece sin 30°=1/2 e cos 60°=1/2; Pitágoras dá o outro cateto √3. Em um triângulo retângulo isósceles de catetos 1, a hipotenusa é √2 e sin 45°=cos 45°=√2/2. Reconstruir esses valores permite conferir uma tabela em vez de apenas decorá-la.

## Uma volta preserva o ponto, mas não apaga a rotação realizada

Somar 360° ou 2π rad retorna ao mesmo ponto do círculo, então seno e cosseno se repetem. Assim sin 390°=sin 30°=1/2. Um ângulo negativo gira no sentido horário; a reflexão do círculo dá sin(−30°)=−sin 30°=−1/2 e cos(−30°)=cos 30°. Os ângulos 0° e 360° têm as mesmas coordenadas finais, embora representem rotações diferentes. Em aplicações, declare também a convenção de orientação utilizada.

## Explore o painel procurando primeiro uma previsão

Antes de mover o controle, preveja os sinais em 120°, as coordenadas em 90° e o que acontece em −30°. O painel usa passos de 15° e mostra a conversão em múltiplos de π, seno, cosseno e tangente. As projeções pontilhadas acompanham as coordenadas com sinal. Em 90° e 270°, a tangente aparece como não definida; não é um número extremamente grande produzido por arredondamento. Para operar pelo teclado, dê foco ao controle e use as setas.

## O código recebe radianos e devolve aproximações

As funções sin e cos do módulo math de Python recebem a medida em radianos. sin(30) interpreta 30 rad, e não 30°. A chamada sin(radians(30)) fornece uma aproximação de 1/2. Valores calculados em ponto flutuante podem ficar muito próximos de zero sem serem exatamente zero. No painel, os pontos dos eixos são tratados exatamente quando o ângulo inteiro é múltiplo de 90°; outros pontos são aproximações numéricas, sem alegação de uma prova por amostragem.

## Uma conta trigonométrica deve terminar com uma conferência

Confira se a razão seno/cosseno está entre −1 e 1, se o sinal concorda com o quadrante e se a unidade angular foi convertida. Para tangente, verifique se o cosseno é zero antes de dividir. Em um problema de triângulo retângulo, desenhe o ângulo e confira a unidade dos lados. Identidades de soma de ângulos, equações trigonométricas gerais e funções trigonométricas inversas ainda exigem outros recortes; esta aula não encerra a trigonometria.

## Exercícios e resoluções originais

- No triângulo retângulo 3–4–5, qual o seno do ângulo oposto ao cateto 3? **Resolução:** Cateto oposto 3 e hipotenusa 5, portanto seno 3/5=0,6.
- sin(30) em Python calcula diretamente seno de 30 graus? **Resolução:** Python usa radianos.
- No mesmo triângulo e ângulo oposto ao cateto 3, qual o cosseno? **Resolução:** Adjacente 4 e hipotenusa 5: 4/5=0,8.
- No mesmo ângulo do triângulo 3–4–5, qual a tangente? **Resolução:** Oposto/adjacente=3/4=0,75.
- Escreva 90° como cπ rad. Qual c? **Resolução:** 90/180=1/2, então π/2 rad.
- Escreva 30° como cπ rad. Qual c? **Resolução:** 30/180=1/6, portanto π/6 rad.
- Quantos graus correspondem a π/3 rad? **Resolução:** (π/3)×180/π=60°.
- Com r=2 m e θ=π/3 rad, escreva s=cπ m. Qual c? **Resolução:** s=rθ=2π/3 m, então c=2/3.
- Quanto é cos 120°? **Resolução:** No segundo quadrante, cos 120°=−cos 60°=−1/2.
- Quanto é sin 390°? **Resolução:** 390°=360°+30°: o seno repete 1/2.
- Quanto é sin(−30°)? **Resolução:** A reflexão muda o sinal do seno: −1/2.
- O que ocorre com tan 90° nos reais? **Resolução:** Tangente é seno/cosseno; em 90° o denominador é zero.

## Modelo, fontes e limites

Teste: `node labs/circulo-unitario/test_model.cjs` na raiz do site. angleState aceita graus inteiros entre −360 e +360; o controle escolar usa passo 15°. Coordena eixos com valores exatos e usa Math.sin/cos nos outros pontos; tangente retorna null para os eixos verticais. A conversão em múltiplos de π é reduzida por máximo divisor comum. Testes percorrem 721 ângulos, verificando norma, reflexão, periodicidade, contratos e 49 estados renderizados. Não validam acessibilidade por leitor de tela real ou aprendizagem pessoal.

Referência primária consultada parcialmente em 22/10/2026: Jay Abramson, Precalculus 2e (OpenStax, 2021), [§5.1](https://openstax.org/books/precalculus-2e/pages/5-1-angles), [§5.2](https://openstax.org/books/precalculus-2e/pages/5-2-unit-circle-sine-and-cosine-functions), [§5.4](https://openstax.org/books/precalculus-2e/pages/5-4-right-triangle-trigonometry). Consulta HTML, sem paginação impressa conferida. Texto, painel e exercícios próprios; sem reprodução de exemplos ou imagens do livro.

Aula existente aprofundada de três para 12 seções e de dois para 12 exercícios, preservando IDs e corrigindo pergunta numérica ambígua. Rascunho assistido por IA para revisão pessoal. Próxima revisão: prever sinais em 120°, interpretar 90° e comparar 30°/30 rad. Identidades de soma, equações gerais e trigonométricas inversas continuam pendentes.

Verificação do bloco: teste JavaScript do círculo aprovado para 721 ângulos e 49 estados renderizados; sintaxe de simulations.js conferida. Treze testes de catálogo e 563 estruturas MathML aprovados. No navegador a 390 px, controle operado por ArrowRight de 30° a 90° (tangente não definida) e depois 120° (cosseno negativo). Relatório textual e figura inspecionados, página sem transbordamento horizontal; console sem erros observados. Exercício 9 rejeitou +0,5 e aceitou −1/2. Prévia circulo-unitario-mobile.jpg. Navegador recarregado para incorporar o novo script. Leitor de tela real e suite global de todos os outros modelos não verificados. Catálogo 507 aulas/3261 exercícios, 257 aulas com até três seções; cobertura recalculada. Saldo semanal confirmado após bloco: 90%; parada em 65%. Próxima revisão pessoal: prever sinais e conversões antes de usar o painel. Próximo bloco do percurso: geometria/escala ou contagem; identidades e equações trigonométricas permanecem pendentes.
