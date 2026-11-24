# Limites, assíntotas e esboço

Rascunho didático original — 27/10/2026. Revisão de Jhuann pendente.

## Primeiro, identifique o que vai para infinito

Pré-requisitos para os limites: domínio, frações algébricas e limites laterais. A parte final de esboço usa regras de derivação e sinais da primeira e segunda derivadas; você pode retomá-la depois dessas aulas. Em x→+∞, estudamos entradas arbitrariamente grandes. Em f(x)→+∞ quando x→0⁺, as entradas se aproximam de um ponto finito e as saídas crescem sem limite. Infinito não é um número real para substituir na expressão ou um valor atingido no ponto.

## Entradas grandes pedem outra comparação

Preservamos o exemplo f(x)=(2x²+1)/(x²+3). Seu domínio é ℝ: x²+3 nunca se anula. Para x≠0, divida numerador e denominador por x². As parcelas 1/x² e3/x² tendem a zero tanto para x→+∞ quanto para x→−∞. O denominador normalizado tende a1, que é diferente de zero; logo ambos os limites são2. A divisão auxiliar não remove x=0 do domínio original.

(2+1/x²)/(1+3/x²)→2

## O que significa ficar perto para sempre?

Para lim x→+∞ f(x)=L, cada tolerância ε>0 deve admitir um limiar M tal que toda entrada do domínio com x>M satisfaça |f(x)−L|<ε. Para −∞, exigimos x<−M. O limiar pode depender de ε, mas não da entrada que será escolhida depois dele. Uma tabela com três valores não satisfaz esse “toda”: precisamos controlar a cauda inteira da função.

## Uma assíntota horizontal não é barreira

Ter limite2 no infinito descreve a aproximação na cauda. Para o exemplo f, subtrair2 dá [2x²+1−2(x²+3)]/(x²+3)=−5/(x²+3). Como o denominador é positivo, f(x)<2 em todo x real: esta curva não cruza y=2. Essa conclusão vem do sinal da diferença; não é uma proibição imposta pela definição de assíntota horizontal.

f(x)−2=−5/(x²+3)

## Uma garantia de erro, não apenas uma tabela

O erro absoluto da aproximação f(x)≈2 é E(x)=5/(x²+3). Para ε=1/100, resolva 5/(x²+3)<1/100. Multiplicar por100(x²+3), que é positivo, preserva a desigualdade: 500<x²+3, ou x²>497. Para |x|≥23, temos x²≥529>497. Já em |x|=22, x²=484<497. Portanto23 é o menor inteiro positivo N cuja cauda |x|≥N garante erro estritamente menor que0,01. O valor exato em23 é5/532; em22 é5/487.

|x| ≥ 23 ⇒ |f(x)−2| < 1/100

## Uma curva que realmente cruza a assíntota

Considere g(x)=2+x/(x²+1), definida em ℝ. Como |g(x)−2|=|x|/(x²+1)≤1/|x| para x≠0, a diferença tende a zero nos dois extremos. Em x=0, g(0)=2; para x<0 a diferença é negativa, e para x>0 é positiva. Assim a curva cruza sua assíntota em(0,2). Uma reta assintótica descreve o comportamento no infinito, sem determinar todos os encontros em entradas finitas.

g(x)−2 = x/(x²+1)

## Compare curvas nos mesmos eixos

A linha contínua mostra f e a tracejada, g. A reta pontilhada é y=2. A janela de−8 a8 ajuda a localizar o mínimo de f e o cruzamento de g; ela não mostra todo o domínio e não prova os limites. Os argumentos de erro anteriores é que controlam as caudas, inclusive fora da imagem.

## Um polo pode ter sinais distintos

Para 1/x, o lado direito diverge para +∞ e o esquerdo para −∞. Não há limite real finito em zero, nem um único limite infinito com sinal comum.

lim_{0+}1/x=+∞; lim_{0−}1/x=−∞

## A divergência lateral também tem uma garantia

Para todo nível H>0, escolher 0<x<1/H produz 1/x>H. À esquerda, −1/H<x<0 implica 1/x<−H. Essas desigualdades controlam todos os pontos suficientemente próximos de zero pelo lado indicado. A reta x=0 é assíntota vertical de1/x porque há divergência lateral. O limite bilateral não é+∞ nem−∞, pois os lados discordam. Para1/x², ambos os lados tendem a+∞; mesmo assim não existe valor real “infinito” a atribuir em zero. Limites laterais não dependem do valor que se escolha isoladamente no ponto.

## Denominador zero não prova assíntota vertical

A função h(x)=(x²−1)/(x−1) só está definida para x≠1. Nesse domínio, fatorar e cancelar dá h(x)=x+1. Assim lim x→1 h(x)=2, um valor finito. O ponto ausente é uma descontinuidade removível, não uma divergência. O cancelamento é uma identidade fora de1: não torna a fração original definida em1. Para f, cujo denominador x²+3 nunca se anula, não há assíntota vertical.

h(x)=x+1, x≠1; lim x→1 h(x)=2

## A assíntota oblíqua vem de uma diferença pequena

Para r(x)=(x²+x+1)/(x+1), x≠−1, a divisão polinomial dá r(x)=x+1/(x+1). A diferença r(x)−x tende a zero para x→±∞: y=x é a assíntota oblíqua. A mesma função tem divergência vertical em x=−1, pois o termo1/(x+1) diverge enquanto x fica limitado. Comparar apenas r(x)/x não bastaria para identificar a reta: por exemplo, x+1 tem razão por x tendendo a1, mas sua diferença para x é sempre1.

r(x)−x = 1/(x+1) → 0

## Uma raiz quadrada exige conservar o sinal

Considere q(x)=x/√(x²+1). Para x≠0, escreva √(x²+1)=|x|√(1+1/x²). Logo q(x)=(x/|x|)/√(1+1/x²). O fator x/|x| vale1 no lado positivo e−1 no negativo. Portanto os limites são1 em+∞ e−1 em−∞. A função possui assíntotas horizontais diferentes nos dois extremos. Trocar √(x²) por x perderia o sinal do segundo limite.

√(x²)=|x|

## A comparação de graus tem hipóteses

Para um quociente de polinômios não nulos com coeficientes líderes a e b, b≠0: grau do numerador menor que o do denominador dá limite0; graus iguais dão a/b. Se a diferença de graus é1, a divisão fornece uma reta mais um resto que tende a zero. Diferenças maiores podem produzir aproximação por um polinômio de grau maior, não uma assíntota oblíqua reta. A função só é analisada onde o denominador é não nulo; cancelamentos preservam exclusões do domínio original. Essas regras não são receitas para funções arbitrárias com raízes ou oscilações.

## A primeira derivada decide como f se aproxima

Retome f=(2x²+1)/(x²+3). Pela regra do quociente, f′=[4x(x²+3)−2x(2x²+1)]/(x²+3)²=10x/(x²+3)². O denominador é positivo; o sinal vem de x. A função decresce em(−∞,0) e cresce em(0,+∞), com mínimo global f(0)=1/3. Ela é par, pois só depende de x²; isso confere a simetria do gráfico. Essas informações explicam a aproximação por baixo a2 nos dois extremos.

f′(x) = 10x/(x²+3)²

## A segunda derivada acrescenta a concavidade

Derive10x(x²+3)⁻²: f″=10(x²+3)⁻²−40x²(x²+3)⁻³. Colocando sobre o denominador comum, resulta30(1−x²)/(x²+3)³. É positiva para|x|<1 e negativa para|x|>1. Há mudança de concavidade em x=−1 e1, pontos do domínio onde f é contínua; ambas as ordenadas são3/4. O esboço reúne domínio, simetria, mínimo, inflexões e limites. Apenas encontrar zeros de f″, sem verificar mudança de sinal e continuidade, não daria essa conclusão.

f″(x) = 30(1−x²)/(x²+3)³

## Amostras numéricas precisam de uma referência

O exemplo Python original calcula três entradas com ponto flutuante; serve para explorar, não para provar limite ou igualdade exata. O desafio confere uma identidade com tolerância1e−12. No laboratório para baixar, Fraction mantém erro, valores e derivadas racionais exatos, e o limiar inteiro é calculado sem raiz de float. Uma impressão arredondada de2 não significa que f atingiu2. As amostras e testes verificam a implementação; as desigualdades e os argumentos de sinal sustentam as conclusões matemáticas.

## Revisão pessoal e limites deste recorte

Em vinte minutos, refaça a subtração f−2, obtenha o limiar23 e explique o cruzamento de g sem consultar a figura. Em outra sessão, derive f e reconstrua mínimo e inflexões. Esse trabalho é evidência que você poderá produzir; não é uma habilidade pessoal já certificada. Oscilações, outros ritmos de crescimento, aproximações polinomiais gerais e mais problemas de modelagem continuam pendentes. A aula e a disciplina permanecem em elaboração.

## Exercícios e resoluções

Para f(x)=(2x²+1)/(x²+3), qual é o limite quando x→+∞?

**Resolução:** Dividindo por x², obtém-se(2+1/x²)/(1+3/x²)→2.

Os dois lados de 1/x em zero divergem com o mesmo sinal?

**Resolução:** Direita positiva, esquerda negativa.

Para a função f da aula, qual é |f(1)−2|?

**Resolução:** 5/(1+3)=5/4.

Para f, qual é |f(10)−2|? Responda como fração ou decimal.

**Resolução:** 5/(100+3)=5/103.

Qual é o menor inteiro positivo N que garante |f(x)−2|<0,01 para todo |x|≥N?

**Resolução:** A condição é x²>497. Temos22²=484 e23²=529.

Em que abscissa g(x)=2+x/(x²+1) cruza a reta y=2?

**Resolução:** O denominador é positivo; x/(x²+1)=0 exige x=0 e o sinal muda ali.

Qual é lim x→1 (x²−1)/(x−1)?

**Resolução:** Para x≠1, a função é x+1; o limite é2.

Para r(x)=(x²+x+1)/(x+1), qual é o coeficiente angular da assíntota oblíqua?

**Resolução:** r(x)=x+1/(x+1); a reta é y=x, de inclinação1.

Para a mesma r, qual é r(1)−1?

**Resolução:** O resto é1/(1+1)=1/2.

Qual é o valor mínimo de f(x)=(2x²+1)/(x²+3) em ℝ?

**Resolução:** O sinal de f′ muda de negativo para positivo em0; f(0)=1/3.

Qual é a ordenada de f no ponto de inflexão de abscissa positiva?

**Resolução:** A mudança de concavidade ocorre em x=1; f(1)=3/4.

Qual é f′(1), para a mesma f?

**Resolução:** 10/(1+3)²=10/16=5/8.

## Fontes e autoria

Consulta parcial em27/10/2026: [OpenStax Calculus1, §2.2](https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function), trechos de limites laterais/infinitos e definição de assíntota vertical; [§4.6](https://openstax.org/books/calculus-volume-1/pages/4-6-limits-at-infinity-and-asymptotes), definições de limite no infinito/horizontal, diferença para reta oblíqua e roteiro de esboço. Apoio complementar: não é nova leitura do Apostol ou confirmação da versão curricular da turma. As funções f,g,h,r, estimativa de erro, deduções, exercícios, código e figura desta aula são elaborações próprias; não se reproduzem figuras ou listas dos livros.

Precisão de convenção: usamos a definição de assíntota vertical por pelo menos um limite lateral infinito. O valor eventualmente atribuído isoladamente em x=a não altera esses limites; não usamos uma regra universal de que uma curva jamais possa ter ponto sobre uma assíntota vertical.

## Laboratório e limites

`python3 -m unittest discover -s labs/assintotas-limites -t .` e `python3 labs/assintotas-limites/limits.py`. Cinco testes: identidades/erro em201 racionais e inteiros de1001 algarismos; limiar em203 tolerâncias contra busca inteira independente; cruzamento, polo e ponto removível; derivadas comparadas à regra do quociente; contratos. `positive_integer_cutoff` retorna o menor inteiro POSITIVO N para a cauda fechada |x|≥N e erro estritamente menor queε. Exigeε>0, int/Fraction; rejeita bool/float. O domínio removível continua excluído nas funções. A raiz do exemplo q é tratada analiticamente na aula, não implementada como função racional.

A figura tem801 amostras em cada curva e é apenas uma visualização finita. Não prova caudas ou classifica funções arbitrárias. Testes conferem cálculos; revisão didática e reconstrução por Jhuann pendentes.

Próxima revisão20min: f−2, erro0,01, cruzamento de g. Próxima elaboração da trilha: movimento, distância e deslocamento por integração.
