# Teorema Fundamental do Cálculo — notas

Texto original de 13/10/2026, preparado com apoio de IA para revisão de Jhuann. Não são anotações importadas do Samsung Notes.

## Três objetos que precisam de nomes diferentes

Pré-requisitos: integral de Riemann, continuidade, derivada e regra da cadeia. Uma integral definida com fronteiras fixas é um número. A(x)=∫_a^x f(t)dt é uma função: cada x escolhe uma fronteira e produz um número. Uma primitiva F é uma função cuja derivada é f. O teorema mostra como esses objetos se relacionam. A letra t dentro da integral é uma variável de integração; trocar t por s não muda o resultado. O x que determina a fronteira permanece livre.

`número: ∫_a^b f(t)dt; função: A(x)=∫_a^x f(t)dt; primitiva: F′=f`

## Primeira parte: a taxa da acumulação

Na versão clássica usada aqui, f é contínua no intervalo fechado [a,b]. Defina A(x)=∫_a^x f(t)dt. Então A é diferenciável no interior e A′(x)=f(x). Nas fronteiras, podemos discutir derivadas laterais apropriadas, em vez de pressupor uma vizinhança dos dois lados. A continuidade é uma hipótese suficiente para essa versão; não estamos afirmando a forma mais geral do teorema.

`A′(x)=f(x), para a<x<b`

## Justificar pela média de uma faixa pequena

Pela aditividade, A(x+h)−A(x)=∫_x^{x+h} f(t)dt. Dividir por h dá a média orientada de f nessa faixa. Subtraindo f(x), o erro absoluto é no máximo a maior diferença |f(t)−f(x)| entre x e x+h. A continuidade em x faz esse máximo tender a zero quando h→0. O argumento funciona para h positivo e negativo: a orientação da integral acompanha o sinal de h. Assim o quociente incremental tende a f(x), sem precisar conhecer uma primitiva.

`|[A(x+h)−A(x)]/h − f(x)| ≤ sup_{t entre x e x+h}|f(t)−f(x)| → 0`

## Segunda parte: avaliar pela diferença de uma primitiva

Ainda com f contínua em [a,b], seja F contínua nas fronteiras e diferenciável no interior, com F′=f. A primeira parte fornece A′=f; logo (F−A)′=0. Pelo Teorema do Valor Médio, F−A é constante no intervalo. Como A(a)=0, temos F(x)−A(x)=F(a), portanto A(b)=F(b)−F(a). Qualquer constante adicionada a F cancela na diferença. Essa é uma justificativa para avaliar nas duas fronteiras, e não somente na superior.

`∫_a^b f(t)dt = F(b)−F(a)`

## Exemplo: orientação e sinal

Para f(t)=t, uma primitiva é t²/2. A integral de 0 a 2 vale 2−0=2; de 2 a 0, vale −2. De −1 a 0, o integrando é negativo e a integral vale −1/2. De 0 a −1, a orientação se inverte e o valor é +1/2. Assim ∫_0^x t dt=x²/2 pode ser positiva quando x<0, enquanto sua derivada A′(x)=x é negativa. A função acumulada está diminuindo quando x cresce nessa região.

`∫_b^a f=−∫_a^b f; A(x)=x²/2 e A′(x)=x`

## Uma fronteira composta: combinar teorema e cadeia

Se g é diferenciável e f contínua na faixa relevante, B(x)=∫_a^{g(x)} f(t)dt é A(g(x)). Primeiro o teorema dá A′(u)=f(u); depois a cadeia dá B′(x)=f(g(x))g′(x). Para B(x)=∫_0^{x²} t dt, B′(x)=x²·2x=2x³. A integral pode ser calculada diretamente como x⁴/2, confirmando o resultado. Em x=−1, a acumulação é 1/2 e sua taxa −2.

`d/dx ∫_a^{g(x)} f(t)dt = f(g(x))g′(x)`

## Duas fronteiras móveis: duas contribuições

Escolha uma fronteira fixa c na região em que f é contínua. Escreva ∫_{u(x)}^{v(x)} f(t)dt=A(v(x))−A(u(x)), usando orientação e aditividade. Derive os dois termos pela cadeia: a fronteira superior contribui com f(v)v′; a inferior aparece subtraindo f(u)u′. A fórmula continua válida se as fronteiras trocam de ordem, desde que o integrando e a composição estejam definidos. Não se deve reordenar as fronteiras sem mudar o sinal.

`d/dx ∫_{u(x)}^{v(x)} f(t)dt = f(v(x))v′(x)−f(u(x))u′(x)`

## Exemplo com as duas fronteiras

Para C(x)=∫_x^{2x} t dt, a derivada é (2x)·2−x·1=3x. Pela primitiva, C(x)=((2x)²−x²)/2=3x²/2, cuja derivada também é 3x. Em x=2, C=6 e C′=6; a coincidência numérica nesse ponto não torna valor e taxa a mesma coisa. Em x=1, C=1,5 e C′=3. Se f representasse uma taxa física, a acumulação e sua derivada teriam unidades diferentes.

`C(x)=3x²/2; C′(x)=3x`

## Derivar sem ter uma primitiva elementar

Para D(x)=∫_0^{x²} cos(t²)dt, não precisamos calcular a integral em forma elementar para obter D′(x)=2x cos(x⁴). O teorema e a cadeia bastam, pois o integrando é contínuo. Isso é diferente de ∫_0^1 cos(t²)dt, que é um número independente de x: sua derivada em relação a x é zero. Observe as fronteiras e as variáveis livres antes de aplicar qualquer regra.

`D′(x)=2x cos((x²)²)=2x cos(x⁴)`

## Hipóteses não podem ser esquecidas

Considere f(t)=0 para t<0 e f(t)=1 para t≥0. A(x)=∫_{−1}^x f(t)dt vale zero até x=0 e x depois disso. Em zero, a taxa lateral esquerda é 0 e a direita 1; não há derivada. A continuidade que sustentava o argumento falha ali. Outro cuidado: ln|t| tem derivada 1/t somente onde t≠0. Usar F(1)−F(−1) não calcula uma integral ordinária de 1/t sobre [−1,1], porque a singularidade interrompe as hipóteses.

`no salto: A′_esq(0)=0, A′_dir(0)=1`

## Aplicação ao movimento e roteiro de explicação

Se v é uma velocidade contínua, a posição satisfaz s(t)=s(t₀)+∫_{t₀}^t v(τ)dτ e s′=v. A integral de v dá deslocamento assinado, enquanto a integral de |v| dá distância percorrida. Antes de resolver: identifique número ou função; declare integrando e domínio; registre fronteiras e orientação; escolha a parte do teorema; use cadeia se necessário; só então substitua valores. Para ensinar, explique a faixa pequena da primeira parte e por que a diferença de primitivas surge na segunda.

`deslocamento=∫v; distância percorrida=∫|v|`

## Exercícios e resoluções

Tente antes de ler a resposta; justifique domínio, orientação e fatores da cadeia.

### 1. Qual ∫_0^2 t dt?

Resolução: (2²−0²)/2=2.

### 2. Na fronteira x², a derivada é só f(x²)?

- Sim

- Não

Resolução: Há o fator 2x da cadeia.

### 3. Qual ∫_0^{−1} t dt?

Resolução: 1/2−0=1/2. A orientação é de 0 para −1.

### 4. Para A(x)=∫_0^x (t²+1)dt, qual A′(2)?

Resolução: A′(x)=x²+1; em 2, vale 5.

### 5. Para B(x)=∫_0^{x²}t dt, qual B′(−1)?

Resolução: B′(x)=2x³; em −1, vale −2.

### 6. Para C(x)=∫_x^{2x}t dt, qual C′(2)?

Resolução: C′=(2x)2−x=3x; em 2, vale 6.

### 7. Qual a derivada de D(x)=∫_0^{x²}cos(t²)dt?

- cos(x²)

- 2x cos(x⁴)

- 2x cos(2x)

Resolução: f(x²)=cos((x²)²)=cos(x⁴), e a cadeia dá 2x cos(x⁴).

### 8. Qual a derivada em relação a x do número ∫_0^1 cos(t²)dt?

Resolução: É uma constante em relação a x, portanto derivada zero.

### 9. No exemplo de salto f(t)=0 à esquerda de zero e 1 à direita, a acumulação A tem derivada em zero?

- Sim, sempre igual a f(0)

- Não: taxas laterais 0 e 1 discordam

- Sim, porque a integral existe

Resolução: A(x)=0 para x≤0 e A(x)=x para x≥0 nessa região. As taxas laterais discordam.

## Experimento

Salve experiment.py e execute `python3 experiment.py`. Para os testes, salve test_experiment.py ao lado e rode `python3 -m unittest discover -p 'test_*.py'`. Biblioteca padrão, sem escrita de arquivos. As funções aceitam também Fraction para conferir identidades exatas.

## Revisão pessoal

Explique o argumento da faixa pequena, a diferença F(b)−F(a) e duas fronteiras móveis sem ler; resolva exemplos inéditos. Outras aulas e notas pessoais ainda precisam de preparação.
