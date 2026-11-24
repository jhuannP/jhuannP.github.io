# Esperança e variância

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Distinguir resultado, variável aleatória e distribuição dos valores.
- Calcular esperança, segundo momento, variância e desvio padrão.
- Justificar linearidade e transformação afim dos momentos.
- Separar identidade matemática, precisão numérica e estimativa amostral.

## A variável atribui um número ao resultado

Uma variável aleatória X é uma função dos resultados do experimento. Em duas moedas, o resultado pode ser (cara,coroa), enquanto X pode contar caras e valer 1. Resultados diferentes podem produzir o mesmo X. Para obter P(X=x), some as probabilidades de todos os resultados que recebem esse valor. No modelo finito desta aula, não há dificuldade de existência dos momentos.

X: Ω→ℝ

## Esperança é uma média ponderada do modelo

Se X assume valores xᵢ com massas pᵢ, E[X]=Σᵢ xᵢpᵢ. Os pesos são probabilidades não negativas com soma 1; não são uma lista arbitrária de números. A média pode nem ser um valor possível de X: se X vale 0 ou 2 com pesos iguais, E[X]=1, embora X nunca seja 1. Uma realização ou amostra pequena não precisa igualar essa média.

E[X]=Σᵢ xᵢpᵢ

## Transforme os valores antes de fazer a média

Para calcular E[g(X)], aplique g a cada valor e depois some com os mesmos pesos. Em geral E[g(X)] não é g(E[X]). No exemplo {0,2}, E[X²]=2 e (E[X])²=1. Confundir esses dois objetos apagaria a dispersão.

E[g(X)]=Σᵢ g(xᵢ)pᵢ

## A linearidade não exige independência

Para variáveis no mesmo espaço finito, a soma ponderada de aX+bY+c se distribui: E[aX+bY+c]=aE[X]+bE[Y]+c. Nenhuma fatoração da distribuição conjunta foi usada. Já a identidade E[XY]=E[X]E[Y] precisa de hipóteses adicionais, como independência com integrabilidade pertinente.

E[aX+bY+c]=aE[X]+bE[Y]+c

## Variância mede o desvio quadrático à média

Defina μ=E[X]. A variância é E[(X−μ)²], não a média dos desvios com sinal, que se cancelam. É não negativa. Se X tem unidade metro, a variância tem m²; o desvio padrão √Var(X) tem metro. Com pesos positivos, variância zero implica que todos os valores com massa positiva são iguais à média.

Var(X)=E[(X−μ)²]

## Demonstre a identidade do segundo momento

Expanda (X−μ)²=X²−2μX+μ² e use linearidade. Como μ é constante e E[X]=μ, obtemos E[X²]−2μ²+μ²=E[X²]−μ². A identidade é exata na matemática. Não resulta em variância negativa no modelo; um valor negativo no cálculo aproximado exige investigar arredondamento ou implementação.

Var(X)=E[X²]−(E[X])²

## Translação não muda a dispersão; escala participa ao quadrado

Para Y=aX+b, a média é aμ+b. O desvio Y−E[Y] é a(X−μ), de modo que Var(Y)=a²Var(X). Somar uma constante desloca os valores e a média juntos. Multiplicar por −2 espelha os valores, mas multiplica a variância por 4; o desvio padrão é multiplicado por |a|.

E[aX+b]=aE[X]+b; Var(aX+b)=a²Var(X)

## Na soma, a covariância entra

Expandir o quadrado do desvio da soma fornece Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y). Para independência com momentos finitos, a covariância é zero e as variâncias somam. Sem essa condição, não descarte o termo: se Y=X, Var(X+Y)=4Var(X), não 2Var(X).

Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)

## O cancelamento numérico pode esconder uma variância pequena

Considere dois valores igualmente prováveis, 10⁸−1 e 10⁸+1. A média é 10⁸ e a variância exata é 1. Na representação de ponto flutuante testada, a diferença dos dois grandes momentos arredondados deu zero; a soma dos desvios quadrados deu 1. Usar uma forma centrada ajuda nesse caso, mas não garante precisão para todo conjunto: valores já arredondados também podem ter perdido informação. O laboratório usa frações exatas para fornecer a referência.

Identidade exata ≠ algoritmo sempre estável

## Parâmetro do modelo não é variância amostral

Aqui somamos massas de uma distribuição especificada. Para observações x₁,…,xₙ, precisamos escolher uma regra de estimação; divisores n e n−1 respondem a convenções e objetivos diferentes. O uso de n−1 como correção não transforma qualquer amostra enviesada ou dependente em um estimador adequado. Esta aula não estima variância de arquivos reais.

## Um modelo de dois estados conecta as ideias

Nos estados 0 e 1, defina X=a e X=a+d, com probabilidades 1−p e p. A média é a+dp e a variância d²p(1−p). Se d=0, os dois estados têm o mesmo valor e a variável é constante. Se p=0 ou p=1, apenas um estado tem massa positiva. A demonstração permite mudar origem, distância e pesos separadamente.

E[X]=a+dp; Var(X)=d²p(1−p)

## Exemplo resolvido

X vale 0 com probabilidade 3/4 e 4 com probabilidade 1/4. Quais os momentos?

1. E[X]=0×3/4+4×1/4=1.
2. E[X²]=0²×3/4+4²×1/4=4.
3. Var(X)=4−1²=3.
4. Pela forma centrada: (0−1)²×3/4+(4−1)²×1/4=3.
5. O desvio padrão é √3 na unidade de X.
6. Se Y=2X+10, E[Y]=12 e Var(Y)=12.

## Exercícios e resoluções

### Uma variável vale −1 e 1 com probabilidades iguais. Qual é sua média?

E[X]=(−1)/2+1/2=0.

### Para essa mesma variável, qual é a variância?

A média é 0 e os desvios quadrados são 1, então a variância é 1.

### X vale 0 com peso 3/4 e 4 com peso 1/4. Quanto vale E[X²]?

0²×3/4+4²×1/4=4.

### No mesmo modelo, qual Var(X)?

E[X]=1; 4−1²=3.

### Se E[X]=1 e Var(X)=3, qual Var(−2X+10)?

(−2)²×3=12; a constante não altera a variância.

### Se Var(X)=3 e Y=X, qual Var(X+Y)?

X+Y=2X; a variância é 4×3=12.

### A linearidade E[X+Y]=E[X]+E[Y] precisa de independência no modelo finito?

Sim
Não

Somar termos ponderados não exige fatoração da conjunta.

### Se X é medido em metros, a variância tem unidade:

Metro
Metro ao quadrado

Os desvios são elevados ao quadrado.

### E[X] precisa ser um valor possível de X?

Sim
Não

X em {0,2} com pesos iguais tem média 1, que não é valor possível.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`, usando apenas biblioteca padrão. Modelos racionais finitos e comparação de cancelamento em ponto flutuante. Sem leitura de arquivos privados ou escrita de resultados externos.

## Proposta didática

Peça uma previsão antes de alterar os controles; calcule um caso manualmente; compare média, dispersão e uma realização possível; encerre verificando uma hipótese do modelo. A condução e a duração precisam de revisão de Jhuann.

## Hipóteses e limites

- Modelo finito com pesos não negativos e soma 1.
- Momentos finitos; não extrapolar automaticamente para distribuições com momentos inexistentes.
- Momentos do modelo, não estatísticas de uma amostra observada.
- Referência racional exata; cálculos em ponto flutuante podem sofrer cancelamento.
