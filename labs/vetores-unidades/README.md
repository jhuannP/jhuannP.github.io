# Vetores e unidades — notas de aula

## Uma grandeza tem dimensão física

Uma medida combina valor numérico e unidade. Comprimento tem dimensão L e tempo tem dimensão T; metros e centímetros são unidades diferentes da mesma dimensão. Rapidez é escalar; deslocamento e força são vetores, com direção e sentido. Um escalar pode ser negativo, como uma energia potencial relativa a um nível de referência: ser escalar não significa ser sempre positivo. Somar comprimento a tempo não faz sentido. Antes da conta, identifique qual grandeza cada símbolo representa.

[v]=L/T; [a]=L/T²

## Consistência dimensional não determina a lei

Em Δx=v₀t+(1/2)at², os dois termos têm dimensão L: (L/T)T=L e (L/T²)T²=L. A mesma verificação seria aprovada com fator 2 no lugar de 1/2, embora esse coeficiente estivesse errado para aceleração constante. As unidades ajudam a rejeitar expressões incompatíveis; a lei e seus coeficientes exigem modelo e dedução. Não podemos somar v₀t a at, pois o segundo termo teria dimensão de velocidade.

## Converter a unidade conserva a grandeza

36 km/h significa 36×1000 m em 3600 s: o mesmo valor físico é 10 m/s. Converter apenas o número sem os fatores correspondentes muda a grandeza. Para componentes de um mesmo vetor, use uma unidade comum antes de somar. Mais tarde, num produto de força em N por deslocamento em cm, o resultado está em N cm; divida o número por 100 para expressá-lo em J.

36 km/h=36×1000/3600 m/s=10 m/s

## Posição é um ponto referido a uma origem; deslocamento liga dois pontos

No plano, o corpo sai de P=(1,2) m e chega a Q=(4,6) m, no mesmo referencial. O deslocamento é a diferença Q−P=(3,4) m. Trocar a origem por uma translação altera as duas posições, mas o termo comum cancela na diferença: (Q+c)−(P+c)=Q−P. Isso não descreve mudar para um referencial em movimento nem girar fisicamente a trajetória.

Δr=r_final−r_inicial=(3,4) m

## Componentes são coeficientes em uma base

Escolha vetores unitários eₓ e eᵧ, perpendiculares entre si. Escrevemos u=uₓeₓ+uᵧeᵧ. As componentes uₓ e uᵧ carregam a unidade de u; os vetores da base indicam direções e são adimensionais. A representação por dois números só é interpretável quando sabemos a base e a unidade. As fórmulas de soma de quadrados e produto escalar usadas nestas notas dependem da base ortonormal.

u=uₓeₓ+uᵧeᵧ; eₓ·eᵧ=0; |eₓ|=|eᵧ|=1

## O módulo vem da geometria e não da soma de componentes

Na base ortonormal, Pitágoras dá |u|²=uₓ²+uᵧ². Para Δr=(3,4) m, o módulo é √(9+16)=5 m. Não é 3+4. O módulo é não negativo; uma componente negativa informa sentido contrário ao eixo, sem tornar o comprimento negativo. Para (−3,4) m, o módulo continua sendo 5 m.

|u|=√(uₓ²+uᵧ²)

## Soma vetorial e distância percorrida respondem a perguntas diferentes

Uma etapa de (3,0) m seguida de (0,4) m produz deslocamento total (3,4) m por soma de componentes. O caminho percorrido tem comprimento 3+4=7 m, enquanto o módulo do deslocamento é 5 m. Duas etapas em sentidos opostos podem até cancelar o deslocamento sem cancelar a distância. Multiplicar um vetor por −1 conserva o módulo e inverte seu sentido; multiplicá-lo por 2 dobra seu módulo.

(3,0)+(0,4)=(3,4); distância=7 m; |Δr|=5 m

## Girar os eixos muda as componentes, não o vetor físico

Gire a base em +90° no sentido anti-horário, conservando o vetor e a origem. Então eₓ′=eᵧ e eᵧ′=−eₓ. As novas componentes são uₓ′=uᵧ e uᵧ′=−uₓ. Assim (3,4) vira (4,−3) e seu módulo continua 5. É uma mudança passiva de coordenadas. Girar o próprio vetor em +90° mantendo os eixos daria (−4,3), outro vetor físico. Não confunda as duas operações.

Eixos +90°: (uₓ,uᵧ) → (uᵧ,−uₓ)

## O produto escalar usa a ortogonalidade da base

Expanda a·b=(aₓeₓ+aᵧeᵧ)·(bₓeₓ+bᵧeᵧ). Os termos cruzados somem porque eₓ·eᵧ=0, e os termos de mesmo eixo usam eₓ·eₓ=eᵧ·eᵧ=1. Resta aₓbₓ+aᵧbᵧ. Para vetores não nulos, isso também é |a||b|cosθ, com θ o ângulo entre eles. Por isso o resultado é positivo para ângulo agudo, zero para perpendicular e negativo para obtuso.

a·b=aₓbₓ+aᵧbᵧ=|a||b|cosθ

## Projetar exige escolher uma direção não nula

Para d=(3,4) m, a direção unitária é ê=d/|d|=(3/5,4/5). A componente escalar da força F=(2,−1) N nessa direção é F·ê=2/5 N. A projeção vetorial é (F·ê)ê=(6/25,8/25) N. Subtraindo-a de F, sobra (44/25,−33/25) N, perpendicular a d: seu produto com (3,4) é 132/25−132/25=0. Projeção escalar e vetor projetado são objetos diferentes.

proj_d F=[(F·d)/(d·d)]d

## Trabalho de força constante é produto escalar

Se F é constante ao longo do percurso, o trabalho é W=F·Δr. Para F=(2,−1) N e Δr=(3,4) m, W=6−4=2 N m=2 J. A componente da força perpendicular ao deslocamento não contribui para esse produto. Como W=(F·ê)|Δr|, o exemplo também dá (2/5 N)(5 m)=2 J. Força variável exige somar contribuições ao longo do caminho, chegando à integral de linha; isso não está resolvido por uma única força escolhida arbitrariamente.

W=F·Δr=FₓΔx+FᵧΔy=2 J

## O sinal do trabalho não é o módulo da força

Uma força (−2,0) N num deslocamento (3,0) m realiza −6 J; F=(0,2) N no mesmo deslocamento realiza zero. Trabalho zero não significa força zero. O vetor zero tem módulo zero, mas não define direção nem ângulo. O produto escalar com ele continua definido e é zero; já dividir por seu módulo para criar um vetor unitário é inválido. O código recusa projetar sobre uma direção nula.

## Conferir em outra base testa a mesma grandeza

Com os eixos girados em +90°, F=(2,−1) N passa a (−1,−2) N e Δr=(3,4) m passa a (4,−3) m. O novo produto é (−1)4+(−2)(−3)=2 J. Em geral, a′·b′=aᵧbᵧ+(−aₓ)(−bₓ)=a·b. A transformação também conserva uₓ²+uᵧ². Isso é uma verificação algébrica do produto escalar e da norma, sem alegar que mudar uma base implica mudar o observador físico.

F′·Δr′=−4+6=2 J

## O laboratório numérico não fiscaliza unidades

O laboratório Python usa inteiros ou Fraction e vetores de duas componentes. Ele calcula soma, escala, produto, norma ao quadrado, projeção e a mudança de base de +90°, sem aproximar raízes. Os números não carregam unidades automaticamente: atribuir N e cm sem converter ainda exige revisão humana. Testes exatos verificam invariantes e projeções no modelo, sem comprovar um experimento ou domínio pessoal. Produtos vetoriais, coordenadas não ortonormais, rotações gerais e movimento em três dimensões permanecem pendentes.

## Exercícios originais e resoluções

Para força constante F=(2,−1) N e deslocamento Δr=(3,4) m na mesma base ortonormal, qual o trabalho em J? **Resolução:** F·Δr=2 J.

Verificar unidades sozinho prova que uma fórmula é fisicamente correta? **Resolução:** Fatores e dependências ainda podem estar errados.

Converta 36 km/h para m/s; responda o valor numérico. **Resolução:** 36×1000/3600=10.

De P=(1,2) m para Q=(4,6) m, qual a componente x do deslocamento em m? **Resolução:** 4−1=3 m.

Qual o módulo de (−3,4) m, em m? **Resolução:** √(9+16)=5 m.

Um percurso tem etapas (3,0) m e (0,4) m. Qual a distância percorrida em m? **Resolução:** Comprimentos das etapas: 3+4=7 m. O módulo do deslocamento é outro valor, 5 m.

Ao girar os eixos em +90° e conservar o vetor (3,4), qual sua nova componente y? **Resolução:** A nova base tem eᵧ′=−eₓ, logo uᵧ′=−3.

Para F=(2,−1) N, qual a componente escalar em N na direção unitária ê=(3/5,4/5)? **Resolução:** 2×3/5−4/5=2/5 N.

Qual a componente x da projeção vetorial da mesma força na reta de direção (3,4), em N? **Resolução:** (F·d)/(d·d)=2/25; multiplicando pela componente 3, resulta 6/25 N.

F=(−2,0) N é constante e Δr=(3,0) m. Qual o trabalho em J? **Resolução:** (−2)×3+0=−6 J.

F=(0,2) N é constante e Δr=(3,0) m. Qual o trabalho em J? **Resolução:** 0×3+2×0=0 J; a força não é nula.

Com F′=(−1,−2) N e Δr′=(4,−3) m, qual o trabalho em J? **Resolução:** −4+6=2 J, igual à conta na base original.

## Referência e limites

H. M. Nussenzveig — Curso de Física Básica, vol.1, Mecânica, 5ª edição revista e atualizada, Blucher2013, 4ª reimpressão2017; exemplar autorizado.

Consulta textual parcial em 26/10/2026: §§3.2–3.3, pp.63–68 (PDF64–69), e §7.1, pp.161–163 (PDF162–164). Recortes extraídos localmente; não se leu todo o capítulo. Derivações, valores, figura, exercícios e laboratório originais. Referência temática não comprova domínio de Jhuann.

Rascunho assistido por IA para revisão de Jhuann. Sem dados experimentais, comprovação de docência ou distribuição do exemplar. Pré-requisitos: coordenadas cartesianas, Pitágoras e trigonometria básica.

Executar: `python3 -m unittest discover -s labs/vetores-unidades -t .`. O núcleo exige listas/tuplas de duas componentes inteiras ou Fraction, exclui bool e float e recusa direção nula na projeção. A norma ao quadrado evita aproximar raízes. O chamador deve fornecer unidades consistentes; o código não as infere nem valida.
