# Superfícies parametrizadas — paraboloide

16/10/2026. Rascunho para revisão de Jhuann.

## Uma superfície é descrita por dois parâmetros

Uma aplicação s(u,v) associa uma região D do plano a pontos no espaço. Para calcular uma integral sem contar partes repetidas, escolha uma parametrização que cubra a região uma vez, salvo fronteiras ou conjuntos de área nula. Suponha derivadas contínuas e s_u×s_v não nulo no interior.

## O produto vetorial fornece área local e orientação

As derivadas s_u e s_v geram o paralelogramo tangente a um pequeno retângulo de parâmetros. Sua área, em primeira aproximação, é ||s_u×s_v|| du dv. Assim, dS=||s_u×s_v|| du dv; a normal unitária é n=±(s_u×s_v)/||s_u×s_v||.

## Integral escalar e fluxo têm integrandos distintos

Uma integral escalar soma f(s(u,v))||s_u×s_v|| du dv. Para f=1, obtém-se a área; uma densidade superficial em kg/m² fornece massa em kg. O fluxo usa F(s)·n dS. Trocar a normal inverte o fluxo, mas preserva a integral escalar.

## Um paraboloide permite fazer as contas à mão

Use s(u,v)=(u,v,a(u²+v²)/2), com u²+v²≤R², a≥0. As coordenadas u,v,R estão em metros e a em m⁻¹. s_u=(1,0,au), s_v=(0,1,av); portanto s_u×s_v=(−au,−av,1), sempre não nulo. A orientação positiva aponta para cima.

## A medida não é a área da projeção

Aqui dS=√(1+a²(u²+v²)) du dv. A projeção sobre o plano xy tem área πR². Para a>0, a superfície tem área maior: o peso é maior que 1 fora da origem. Substituir dS por du dv descartaria a inclinação.

## Polares simplificam a integral, com outro Jacobiano

No disco, u=ρ cosθ e v=ρ senθ, de modo que du dv=ρ dρ dθ. Assim A=2π∫₀ᴿ ρ√(1+a²ρ²)dρ. O fator ρ vem da mudança no plano, e a raiz vem da superfície. A parametrização polar degenera na origem; esse ponto e a costura angular têm área nula.

## A primitiva tem um limite plano

Para a>0, a substituição w=1+a²ρ² dá A=2π[(1+a²R²)^(3/2)−1]/(3a²). Para a=0, a superfície é o disco e A=πR². A expressão com divisão por a² não deve ser avaliada diretamente em zero.

## Uma forma equivalente melhora o cálculo perto de zero

Defina q=√(1+a²R²). Como q³−1=(q−1)(q²+q+1) e q−1=a²R²/(q+1), obtemos A=(2πR²/3)(q²+q+1)/(q+1). Essa forma evita a subtração de números quase iguais e já vale em a=0. Trata-se de estabilidade numérica, não de uma nova área.

## O fluxo vertical cancela o peso da inclinação

Escolha F=(0,0,1) m/s. Na orientação positiva, F·(s_u×s_v)=1 m/s, logo Φ=∬_D 1 du dv=πR² m³/s. A normal unitária tem componente vertical 1/√(1+a²ρ²), que cancela a raiz de dS. Esse resultado depende do campo escolhido e não é uma identidade para qualquer F.

## A mesma geometria pode ter massa e fluxo diferentes

Para densidade constante σ=2 kg/m², M=2A em kg. Ao mudar a com R fixo, a área e a massa mudam, mas o fluxo deste campo vertical continua πR². Inverter a orientação troca Φ por −Φ, preservando A e M. Superfície aberta pede orientação declarada; não há um exterior único dado por volume fechado.

## Não multiplique o fator de área duas vezes

Há duas formas equivalentes para fluxo: F·n ||s_u×s_v|| du dv, com n unitária, ou ±F·(s_u×s_v) du dv. Usar o produto vetorial não normalizado e ainda multiplicar pela sua norma contaria o fator de área duas vezes.

## Verificação numérica é uma comparação controlada

O laboratório compara a expressão fechada com Simpson na integral radial e confere normais, orientação e reescala. A figura mostra uma seção meridiana da superfície, sem renderização 3D ou dados experimentais. Outras superfícies, campos variáveis e provas gerais de invariância por reparametrização precisam de desenvolvimento próprio.

## Resoluções

Para a=0 e R=2 m, qual A/π em m²?

A=πR²=4π m².

Para R=1 m e normal positiva, qual Φ/π em m³/s no campo F=(0,0,1) m/s?

Φ=πR² m³/s, independentemente de a nesta família.

No mesmo campo e R=1 m, qual Φ/π com orientação invertida?

A normal troca de sinal: Φ=−π m³/s.

Para a=1 m⁻¹, R=1 m, qual A/π em m²? Arredonde a 6 casas.

A/π=2(2√2−1)/3≈1,218951 m².

Para a=0, R=1 m e σ=2 kg/m², qual M/π em kg?

M=σA=2π kg.

Inverter a orientação muda a área da superfície?

A medida escalar usa a norma, que não muda de sinal.

Para a>0, a área deste paraboloide é igual à área de sua projeção?

O peso √(1+a²ρ²) é maior que 1 fora da origem.

Qual expressão correta usa a normal unitária?

A normal unitária precisa ser acompanhada do elemento de área.

O fluxo vertical calculado vale para todo campo F sem recalcular o produto escalar?

O cancelamento usa especificamente F=(0,0,1).

## Fontes e roteiro

Escopo: mapa de CCM0223, programa oficial consultado em 16/10. Apoio conceitual: [MIT OCW, V9 Surface Integrals](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/resources/surface_integrls/), PDF consultado em 16/10/2026 sobre medida escalar e fluxo orientado. Fórmulas são relações matemáticas usuais; parametrização, exercícios, derivação para esta família e laboratório foram produzidos para o site, sem reproduzir exemplos da fonte.

Pré-requisitos: produto vetorial, derivadas parciais, integrais duplas e polares. Roteiro: calcular as duas derivadas; construir produto vetorial/norma; prever orientação; integrar área/massa; comparar fluxo; validar por quadratura. Produto: conta comentada e análise de uma troca de orientação, sem dados experimentais ou competência pessoal presumida.

Pendentes: densidades e campos variáveis, mapas gerais e reparametrização, cilindro/esfera, mais geometrias e demonstrações com hipóteses completas. A comparação de Simpson é evidência computacional para a família, não prova geral de integração.
