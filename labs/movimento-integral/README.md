# Movimento por integração

Rascunho original —27/10/2026; revisão pessoal de Jhuann pendente.

## O eixo, o relógio e as unidades vêm antes da integral

Pré-requisitos: posição e velocidade em uma dimensão, sinal de funções, primitivas e Teorema Fundamental do Cálculo. Descrevemos uma partícula numa reta, com eixo fixo e relógio crescente. Nas expressões numéricas destas notas, t é o valor do tempo em segundos, v é o valor da velocidade em m/s e s é o valor da posição em metros; os coeficientes carregam as unidades correspondentes. São trajetórias didáticas, sem medições ou hipótese de força. Tempo físico será percorrido com 0≤a≤b.

## Acumular uma taxa conserva o sinal

No exemplo original v(t)=2t−2, entre 0 e2 segundos, v<0 antes de 1 e v>0 depois de 1. A velocidade tem sinal porque é uma componente no eixo escolhido. A integral soma incrementos orientados: uma contribuição negativa diminui a posição, uma positiva aumenta. A primitiva F(t)=t²−2t fornece F(2)−F(0)=0 m, embora o corpo tenha se movido durante o intervalo.

Δs=∫_0^2 (2t−2)dt=0

## Por que integrar a velocidade recupera a posição?

Assuma v contínua em[a,b] e s′=v. Pelo Teorema Fundamental, s(b)−s(a)=∫ₐᵇv(t)dt. De modo equivalente, dada a posição inicial s(a), defina s(t)=s(a)+∫ₐᵗv(u)du: a derivada dessa função é v(t). A constante inicial é necessária para localizar a trajetória. O deslocamento Δs é uma diferença de posições; não é a posição final, salvo quando s(a)=0.

s(t)=s(a)+∫ₐᵗv(u)du

## Distância usa módulo

A rapidez instantânea é |v(t)|, sempre não negativa. Em cada trecho de sinal fixo, a posição é monótona e o comprimento percorrido é o módulo de sua variação. Somar esses comprimentos equivale a integrar |v|. No exemplo original, divida em t=1: no primeiro trecho integramos−v e obtemos1 m; no segundo integramos v e obtemos1 m. A distância total é2 m. Não tome o módulo somente depois de integrar: |∫v|=0 m neste caso.

distância=∫|v|dt=2

## Escolher referência de posição

Uma posição compatível é s(t)=t²−2t+s₀. Derivar recupera v(t)=2t−2. Com s₀=5 m, as posições nos tempos0,1,2 são5,4,5 m. O deslocamento continua0 m e o percurso continua2 m. Transladar a origem soma uma constante às posições, que cancela nas diferenças. Isso não é o mesmo que trocar para um observador em movimento, situação que não modelamos aqui.

s′=v; unidade: velocidade×tempo=comprimento

## Média com sinal e rapidez média respondem perguntas diferentes

Para uma duração b−a>0, a velocidade média é Δs/(b−a); a rapidez média é D/(b−a). No exemplo de 0 a 2 s, resultam0 m/s e1 m/s. A média não é, em geral, a média aritmética das velocidades nas pontas. Essa coincidência vale para v afim, por área de trapézio; não é uma propriedade de toda velocidade variável. Num intervalo de duração zero, as duas razões ficam sem denominador positivo.

v_média=Δs/(b−a); rapidez média=D/(b−a)

## A distância nunca é menor que o módulo do deslocamento

Chame P a soma dos comprimentos no sentido positivo e B a soma dos comprimentos no sentido negativo, ambos não negativos. Então Δs=P−B e D=P+B. Como |P−B|≤P+B, obtemos |Δs|≤D. A igualdade vale quando P=0 ou B=0; no modelo contínuo, quando não há contribuição de movimento em ambos os sentidos. Assim D=|Δs| não exige repouso, e Δs=0 não exige D=0.

|Δs| ≤ D

## Velocidade zero nem sempre significa inversão

Agora use v(t)=(t−1)²(t−3), em 0≤t≤4, com a convenção de unidades numéricas declarada. O fator quadrado é positivo fora de 1 e não muda de sinal ali. Para0≤t<3, v é negativa, exceto pelo zero em 1; depois de 3, é positiva. Portanto t=1 é um instante de velocidade zero sem mudança de sentido. Em t=3 ocorre inversão. Encontrar zeros é o início da análise: o sinal nos intervalos decide o movimento. Não se supõe aceleração constante neste exemplo.

v(t)=(t−1)²(t−3)

## A primitiva do novo exemplo pode ser conferida por derivação

Expanda v=t³−5t²+7t−3. Integrar termo a termo dá F(t)=t⁴/4−5t³/3+7t²/2−3t. Sua derivada recupera a expressão expandida da velocidade. Com posição inicial zero, s=F e temos F(0)=0, F(1)=−11/12, F(3)=−9/4 e F(4)=4/3, em metros. A passagem por velocidade zero em 1 não produz mínimo da posição: a posição continua diminuindo dos dois lados. O mínimo no intervalo está em 3.

F(t)=t⁴/4−5t³/3+7t²/2−3t

## No novo exemplo, integrar antes ou depois do módulo dá respostas distintas

O deslocamento de 0 a 4 s é F(4)−F(0)=4/3 m. Para a distância, a troca de sinal em 3 divide o cálculo: −[F(3)−F(0)]+[F(4)−F(3)]=9/4+43/12=35/6 m. Dividir adicionalmente em 1 é permitido, mas não muda o sinal usado nos dois trechos negativos. De fato, os módulos dos incrementos de 0 a 1 e de 1 a 3 são11/12 e4/3, cuja soma é9/4. A velocidade média é1/3 m/s e a rapidez média35/24 m/s.

Δs=4/3 m; D=35/6 m

## Leia áreas no gráfico de velocidade, não alturas de posição

A curva representa v, não s. A área negativa de 0 a 3 s é−9/4 m; a positiva de 3 a 4 s é43/12 m. O primeiro zero, em 1, toca o eixo sem atravessá-lo. O segundo, em 3, separa sinais opostos. A altura da curva em um instante tem unidade m/s; a área de um intervalo tem unidade m. O desenho ajuda a interpretar; os valores de área vêm da primitiva, não de medir pixels.

## Trocar a orientação do eixo preserva o caminho

Se a nova posição for −s, a nova velocidade será−v e o deslocamento mudará de sinal. O módulo da velocidade e a distância permanecerão iguais. Já trocar limites de uma integral orientada, de∫ₐᵇ para∫ᵦₐ, muda seu sinal matemático; isso não é uma distância física negativa. Para computar tempo transcorrido, o laboratório exige início≤fim. Em duas ou três dimensões, a rapidez é a norma do vetor velocidade; integrar o módulo de apenas uma componente não mede em geral o comprimento da trajetória.

## Verifique unidades e não confie apenas nas pontas

Se v estiver em km/h e o tempo em segundos, converta antes de integrar: por exemplo,3,6 km/h=1 m/s e em 2 s o percurso uniforme é2 m. No exemplo cúbico, v(0)=−3 e v(4)=9 m/s. A área do trapézio construído apenas com as pontas seria12 m, enquanto o deslocamento exato é4/3 m: o gráfico não é uma reta. Conhecer velocidades nos extremos não determina toda a função no intervalo. Tampouco encontrar v=0 decide sozinho se houve inversão.

## O laboratório resolve dois modelos declarados

O arquivo baixável usa Fraction e primitivas exatas para o modelo linear original e o cúbico. As raízes são conhecidas previamente; ele não encontra zeros de uma função arbitrária nem integra medições. Cada intervalo é separado pelos zeros interiores e a distância soma módulos das variações de posição. Em duração zero retorna deslocamento e distância0, mas médias indefinidas. Testes com uma quadratura independente exata para esses polinômios conferem os cálculos; isso não valida um modelo físico real.

## Uma revisão em duas sessões, com evidência própria

Primeira sessão de 20min: para v=2t−2 e s₀=5, reconstruir posições, áreas, deslocamento e rapidez média. Segunda sessão: analisar o sinal de(t−1)²(t−3), derivar a primitiva para conferi-la e obter4/3 m e35/6 m sem consultar a resolução. Registrar sua explicação e suas dúvidas é uma demonstração de estudo a construir, não uma competência já certificada. Movimento com dados ruidosos, força e trabalho, trajetórias vetoriais e modelos por trechos com eventos físicos continuam como próximos recortes.

## Exercícios e resoluções

Para v(t)=2t−2, com t em segundos e v em m/s, qual é a distância entre 0 e2 s, em metros?

**Resolução:** 1+1=2.

Deslocamento zero implica ausência de movimento?

**Resolução:** Trechos em sentidos opostos podem se cancelar.

No modelo linear v=2t−2, com s(0)=5 m, qual é s(1), em metros?

**Resolução:** s(1)=1−2+5=4 m.

No mesmo modelo linear, qual é a rapidez média de 0 a 2 s, em m/s?

**Resolução:** Distância2 m dividida pela duração2 s:1 m/s.

No modelo cúbico v=(t−1)²(t−3), em que instante entre 0 e4 s ocorre inversão de sentido? Responda em segundos.

**Resolução:** O quadrado não muda de sinal em 1; o fator t−3 muda em 3.

Com posição inicial zero no modelo cúbico, qual é s(1), em metros?

**Resolução:** F(1)=1/4−5/3+7/2−3=−11/12.

No modelo cúbico, qual é o deslocamento de 0 a 4 s, em metros?

**Resolução:** F(4)−F(0)=4/3 m.

Qual é o comprimento percorrido de 0 a 3 s no modelo cúbico, em metros?

**Resolução:** A velocidade é não positiva; distância=−[F(3)−F(0)]=9/4 m.

Qual é o comprimento percorrido de 3 a 4 s no modelo cúbico, em metros?

**Resolução:** F(4)−F(3)=4/3+9/4=43/12 m.

Qual é a distância total de 0 a 4 s no modelo cúbico, em metros?

**Resolução:** 9/4+43/12=35/6 m.

Qual é a velocidade média de 0 a 4 s no modelo cúbico, em m/s?

**Resolução:** (4/3)/4=1/3 m/s.

Um corpo mantém rapidez3,6 km/h por 2 s. Qual é a distância em metros?

**Resolução:** 3,6 km/h=1 m/s;1×2=2 m.

## Fonte e autoria

[OpenStax Calculus Volume1, §5.4](https://openstax.org/books/calculus-volume-1/pages/5-4-integration-formulas-and-the-net-change-theorem), consulta parcial em 27/10/2026: teorema5.6, variação líquida e distinção entre integrar velocidade e rapidez. Sem leitura integral ou nova consulta ao Apostol. As duas trajetórias, números, deduções, exercícios, figura e código são próprios; não são reprodução de exemplos ou figuras do livro.

## Laboratório e limites

`python3 -m unittest discover -s labs/movimento-integral -t .` e `python3 labs/movimento-integral/motion.py`. Modelos fixos linear/cubic. travel exige0≤início≤fim, valores int/Fraction sem bool/float. Em duração zero, médias None. Separa raízes interiores conhecidas; não é algoritmo geral de raízes, integração numérica de medições ou simulador de forças. Unidades físicas não são validadas automaticamente.

Seis testes: referências exatas;306 intervalos contra Simpson racional, exato para os polinômios por trechos de sinal fixo; aditividade e limite |Δs|≤D; zero sem inversão e zero com inversão; translação/orientação; contratos e duração zero. As provas analíticas da aula, e não a enumeração finita, justificam as relações gerais.

Próxima revisão em duas sessões: reconstruir o linear com origem5 e o cúbico com zero em 1 sem inversão. Próximo desenvolvimento: outras aplicações de integração e eventos por trechos, respeitando lacunas das demais trilhas. Notas Samsung e evidência pessoal de estudo ainda pendentes.
