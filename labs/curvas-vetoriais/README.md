# Curvas vetoriais: caminho, velocidade e tangente

Material original em rascunho — 16/10/2026. Escopo de CCM0123, programa consultado em 16/10 com ativação 01/01/2025; versão da turma de 2024/1 não recuperada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

## Uma função pode devolver um vetor

Uma função r:I→ℝ³ associa a cada parâmetro t um vetor posição (x(t),y(t),z(t)). O domínio I faz parte da definição. A imagem é o conjunto de pontos percorridos; a função parametrizada guarda também a maneira como o parâmetro percorre esse conjunto. Para r(t)=(t,t²,0), t∈[−1;1], a imagem é um arco da parábola y=x² no plano z=0.



## Limites vetoriais podem ser conferidos por componentes

r(t)→L significa ||r(t)−L||→0. Em dimensão finita, isso equivale a cada componente tender à componente correspondente de L: cada erro de coordenada é limitado pela norma, e a norma é limitada pela soma dos módulos dos erros. Assim três limites escalares controlam o limite vetorial. Concordância em uma tabela continua sendo ilustração, não prova.



## A derivada mede a variação vetorial por unidade de parâmetro

A definição é r′(t)=limₕ→₀[r(t+h)−r(t)]/h quando esse limite existe. Pelo critério de componentes, r′=(x′,y′,z′). A derivada não é a lista dos módulos das variações: seus sinais e direções importam. Para r=(t,t²,0), r′=(1,2t,0) e r″=(0,2,0).

r′(t)=limₕ→₀ [r(t+h)−r(t)]/h

## Velocidade vetorial e rapidez não são iguais

Se t é tempo em segundos e posição é medida em metros, r′ é velocidade em m/s, ||r′|| é rapidez e r″ é aceleração em m/s². Quando t é apenas parâmetro geométrico, use norma da derivada sem presumir essas unidades físicas. Em r=(t,t²,0), a norma da derivada é √(1+4t²), positiva em todo ponto.



## Um vetor tangente não nulo define uma reta

Se r′(t₀)≠0, uma reta tangente é R(λ)=r(t₀)+λr′(t₀). A tangente unitária é T=r′/||r′||. É preciso verificar a norma antes de dividir. Em t₀=1/2, o ponto é (1/2,1/4,0) e a direção tangente é (1,1,0). O comprimento do segmento desenhado para a direção pode ser escolhido para legibilidade, sem representar a norma da derivada.



## Mudar o parâmetro aplica a regra da cadeia

Se q(t)=r(φ(t)), então q′(t)=r′(φ(t))φ′(t), sob as hipóteses de derivabilidade. O fator pode alterar o módulo e a orientação. Para φ(t)=−t, a imagem de r sobre [−1;1] é a mesma, mas a orientação se inverte. Para φ(t)=t³, o parâmetro ainda percorre todo [−1;1], com taxa variável.

q′(t)=r′(φ(t))φ′(t)

## Derivada nula pode ser uma falha da parametrização regular

Para q(t)=(t³,t⁶,0), temos q′=(3t²,6t⁵,0), que zera em t=0. Não se pode calcular T por divisão nesse ponto. Entretanto, a imagem continua sendo a parábola, cuja tangente geométrica na origem é o eixo x, como se vê pela parametrização r(s)=(s,s²,0). Derivada zero nessa representação não implica ausência de tangente em toda representação.



## A segunda derivada também sente a mudança de parâmetro

Quando r e φ são duas vezes diferenciáveis, q″=r″(φ)(φ′)²+r′(φ)φ″, componente a componente. Para φ=t³, q″=(6t,30t⁴,0). Não basta multiplicar r″ por φ′ uma vez. Um movimento na mesma trajetória pode ter aceleração diferente ao mudar a lei temporal.



## Comprimento integra a norma, não o vetor

Para uma curva continuamente diferenciável em [a;b], o comprimento percorrido é ∫ₐᵇ||r′(t)||dt. Já ∫ₐᵇr′(t)dt=r(b)−r(a) é deslocamento vetorial. Não são a mesma quantidade. Se uma parametrização percorre um trecho mais de uma vez, o comprimento percorrido conta essas passagens. A integração e o controle de erro do comprimento serão aprofundados em aula própria.



## Uma projeção pode esconder a componente espacial

Nesta demonstração todos os modelos têm z=0, portanto o plano xy contém a curva inteira. Para uma curva com z variável, uma projeção xy não determinaria a tangente nem a rapidez em ℝ³ sem considerar z′. A interface usa escala igual em x,y e um segmento tangente normalizado; ele mostra direção, não a magnitude de velocidade.



## Um roteiro evita confundir caminho e movimento

Declare domínio e parametrização; calcule componentes e derivadas; confira regularidade; interprete direção e norma; só então atribua significado físico se t for tempo. Compare a mesma posição nas parametrizações usando parâmetros correspondentes, não necessariamente o mesmo número t. O laboratório confere as fórmulas por polinômios independentes e deixa explícito o ponto em que não há vetor tangente unitário pela fórmula.



## Exemplo resolvido

Compare r(s)=(s,s²,0) e q(t)=(t³,t⁶,0) no ponto correspondente a t=1/2.

O parâmetro correspondente de r é s=t³=1/8. Ambas dão posição (1/8,1/64,0).

r′(s)=(1,2s,0)=(1,1/4,0).

Pela cadeia, q′(t)=3t²r′(t³), logo em 1/2 vale (3/4,3/16,0).

As direções são paralelas e têm o mesmo sentido, mas os módulos diferem por fator 3/4.

Em t=0, q′=0 e não pode ser normalizada; r′(0)=(1,0,0) continua não nula.

## Exercícios e resoluções

### Para r(t)=(t,t²,0), qual a componente y de r′ em t=1/2?

2t=1.

### Qual o quadrado da norma de r′ em t=1/2?

r′=(1,1,0), então a norma ao quadrado é 2.

### Para φ(t)=t³, qual φ′(1/2)?

3×(1/2)²=3/4.

### Qual o parâmetro s correspondente a t=1/2 na composição r(t³)?

s=(1/2)³=1/8.

### Qual a componente x de q′(0), para q=(t³,t⁶,0)?

3t² em zero vale 0.

### Ter a mesma imagem obriga duas parametrizações a terem a mesma derivada?

A regra da cadeia inclui o fator φ′.

### Podemos dividir por ||q′(0)|| para normalizar q′ quando ele é zero?

A norma é zero; a fórmula não se aplica.

### Integrar o vetor velocidade sempre dá comprimento percorrido?

A integral vetorial dá deslocamento; comprimento integra a norma.

### Trocar t por −t inverte a orientação no arco deste exemplo?

φ′=−1 troca o sentido de percurso.

## Preparação de aula

Desenhe a parábola; marque parâmetros correspondentes em r(s) e r(t³); derive pela cadeia; compare norma e direção; analise t=0 sem dividir por zero; inverta o parâmetro; explique deslocamento versus comprimento.

## Pendências

Comprimento com integração e erro, curvatura, outros tipos de curvas e mais exercícios de demonstração. A aula não certifica domínio pessoal.
