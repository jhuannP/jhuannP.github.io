# Substituição de variáveis — notas para revisão

Aprofundamento original de 13/10/2026, com apoio de IA para revisão de Jhuann. Não são notas importadas do Samsung Notes.

## A ideia: uma derivada composta em sentido inverso

Pré-requisitos: regra da cadeia, primitiva, integral orientada e Teorema Fundamental. Se F′(u)=f(u), então a cadeia dá dF(g(x))/dx=f(g(x))g′(x). Integrar essa expressão recupera F(g(x)) mais uma constante. A escolha de u deve simplificar uma composição e encontrar sua taxa interna no integrando; não é somente renomear uma expressão.

`∫ f(g(x))g′(x)dx = F(g(x))+C`

## Versão definida e hipóteses

Se f é contínua em um intervalo que contém a imagem de g em [a,b] e g é continuamente diferenciável em [a,b], a cadeia produz uma primitiva F∘g do integrando. Pelo Teorema Fundamental, a integral em x é F(g(b))−F(g(a)), igual à integral em u de g(a) a g(b). Esta é uma versão suficiente, não a forma mais geral. Os intervalos e domínios precisam conter todos os valores utilizados.

`∫_a^b f(g(x))g′(x)dx = ∫_{g(a)}^{g(b)} f(u)du`

## O que a escrita du representa

Escrever u=g(x) e du=g′(x)dx registra o fator que a cadeia exige. Para a identidade acima, não precisamos dividir por g′ nem exigir que g seja injetiva: a justificativa usa uma primitiva da composição. Se o problema exigir expressar x em função de u e trocar um integrando geral, a existência de uma inversa local ou a separação em ramos deve ser examinada. As duas situações não devem ser confundidas.

`f(g(x))g′(x) é um padrão completo; não exige cancelar g′(x)`

## Exemplo 1: polinômio com nova fronteira

Em ∫_0^1 2x(1+x²)dx, escolha u=1+x² e du=2x dx. As fronteiras em u são 1 e 2; a integral vira ∫_1^2 u du=(4−1)/2=3/2. Pela expansão, o integrando é 2x+2x³ e a primitiva x²+x⁴/2 dá o mesmo valor. A primitiva (1+x²)²/2 também serve: as duas diferem pela constante 1/2, que desaparece na avaliação definida.

`x: 0→1; u: 1→2; integral=3/2`

## Exemplo 2: um fator constante que não pode sumir

Em ∫_0^1 x exp(x²)dx, a escolha u=x² dá du=2x dx. Portanto x dx=du/2, e a integral é metade de ∫_0^1 exp(u)du: resultado (e−1)/2. O fator 1/2 vem da diferença entre a taxa interna e o que aparece no integrando. Derivar exp(x²)/2 confirma x exp(x²). Omitir esse fator dobra o resultado.

`∫_0^1 x exp(x²)dx = (e−1)/2`

## Exemplo 3: domínio e logaritmo

Em ∫_0^2 2x/(1+x²)dx, escolha u=1+x². Como 1+x²>0 em todo o intervalo, o logaritmo real é adequado. Fronteiras 1 e 5 produzem ∫_1^5 du/u=ln(5)−ln(1)=ln(5). Para uma integral indefinida de 1/u em intervalos que não cruzam zero, a primitiva geral é ln|u|; o domínio não pode ser ignorado.

`∫_0^2 2x/(1+x²)dx = ln 5`

## Orientação numa transformação afim

No experimento, f(u)=u² e u=1+αx. A integral ∫_0^b α(1+αx)²dx transforma-se em ∫_1^{1+αb}u²du. Para α<0 e b>0, a fronteira final em u é menor que a inicial; não reordene os limites sem inverter o sinal. Para α=0, o integrando em x é zero e as duas fronteiras em u coincidem. Essa identidade ainda vale, embora o mapa constante não forneça uma mudança inversível para problemas gerais.

`I=[(1+αb)³−1]/3 = αb+α²b²+α³b³/3`

## Não monotonia não invalida automaticamente a identidade

Em ∫_{−1}^1 2x exp(x²)dx, g(x)=x² não é injetiva no intervalo. Ainda assim, o padrão f(g(x))g′(x) está presente. A primitiva exp(x²) vale e nas duas fronteiras, dando zero; em u, a integral orientada de 1 a 1 também é zero. As contribuições dos dois ramos se cancelam. Não interprete os limites iguais como intervalo original de comprimento zero: eles representam cancelamento ponderado pelo fator 2x.

`∫_{−1}^1 2x exp(x²)dx=e−e=0`

## Uma troca inválida revela o fator ausente

Na integral ∫_{−1}^1 1 dx=2, escolher u=x² e apenas trocar as duas fronteiras por 1 produziria zero, uma resposta errada. O integrando não tem o fator g′(x)=2x para usar diretamente a identidade. Tentar expressar dx por du requer lidar com x=−sqrt(u) e x=+sqrt(u), suas orientações e a singularidade da inversa em zero. Separar os ramos é necessário para essa mudança geral; nesta aula basta reconhecer por que a troca ingênua não vale.

`mesmas fronteiras transformadas não autorizam descartar a transformação do integrando`

## Indefinida e definida: não misturar variáveis

Na integral indefinida, transforme para u, encontre uma primitiva e substitua u de volta por g(x). Na definida, pode mudar também as fronteiras e permanecer em u até o fim; ou retornar a x antes de avaliar nas fronteiras originais. O erro é escrever uma primitiva em u e avaliá-la em números que ainda representam x. A constante C aparece na família de primitivas; ela cancela no resultado definido.

`em u: avaliar g(a),g(b); em x: avaliar a,b`

## Roteiro para resolver e ensinar

Declare o domínio; identifique a expressão interna; calcule sua derivada; confira se o fator aparece ou pode ser ajustado por uma constante. Transforme o integrando inteiro e as fronteiras mantendo a orientação. Integre, avalie e confira por derivação ou expansão quando possível. Explique o fator que faz a igualdade funcionar. Testes numéricos ajudam a localizar erros de sinal e fator, mas a validade da mudança depende das hipóteses e da justificativa matemática.

`escolher u → calcular g′ → transformar tudo → avaliar → conferir`

## Exercícios e resoluções

Tente antes de consultar; explique o fator interno e a orientação.

### 1. Qual ∫_0^1 2x(1+x²)dx?

Resolução: 3/2.

### 2. Deve transformar fronteiras ao escrever a integral inteira na nova variável?

- Sim

- Não

Resolução: As fronteiras precisam se referir à variável de integração.

### 3. Com u=1+x² e x de 0 a 2, qual a fronteira final em u?

Resolução: 1+2²=5.

### 4. Qual ∫_0^1 x exp(x²)dx?

- e−1

- (e−1)/2

- 2(e−1)

Resolução: x dx=du/2; resultado (e−1)/2.

### 5. Para u=1−2x e x de 0 a 1, qual a fronteira final em u?

Resolução: u(1)=1−2=−1; a integral em u vai de 1 para −1.

### 6. Qual ∫_0^1 −2(1−2x)²dx?

Resolução: [u³/3]_1^{−1}=−1/3−1/3=−2/3.

### 7. Qual ∫_{−1}^1 2x exp(x²)dx?

Resolução: exp(1)−exp(1)=0; a identidade não exige injetividade neste padrão.

### 8. É válido calcular ∫_{−1}^1 dx usando u=x² e apenas trocar as fronteiras para 1 e 1?

- Sim, o resultado é zero

- Não, falta transformar o integrando e tratar os ramos

- Sim, pois x² nunca é negativo

Resolução: A identidade exige o fator g′ quando usada diretamente. Uma mudança geral por inversa exige tratar os ramos.

### 9. No exemplo u=1+x², escrever ∫u du e avaliar a primitiva nas fronteiras 0 e 1 de x é:

- Correto

- Incorreto: as fronteiras em u são 1 e 2

- Correto se acrescentar C

Resolução: Permaneça em u com fronteiras 1 e 2, ou volte para x antes de avaliar 0 e 1.

## Revisão pessoal

Justifique a identidade pela cadeia e pelo Teorema Fundamental; resolva um exemplo com orientação invertida e explique por que ∫dx não admite a troca ingênua u=x² de −1 a 1. Os demais temas e a revisão do curso continuam pendentes.
