# Covariância: associação linear não é independência ou causa

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Calcular covariância e correlação em uma distribuição conjunta finita.
- Justificar efeito de translação/escala e limites da correlação.
- Construir dependência com correlação zero e tratar variância nula.
- Interpretar melhor reta e matriz de covariância sem inferir causalidade.

## Centralizar revela variação conjunta

Cov(X,Y)=E[(X−E[X])(Y−E[Y])]. Desvios com o mesmo sinal contribuem positivamente; sinais opostos, negativamente. Precisamos de momentos pertinentes, como segundos momentos finitos. Covariância não mede apenas se Y depende de X: relações não lineares podem produzir cancelamento.

Cov(X,Y)=E[(X−E[X])(Y−E[Y])]

## Expanda para obter outra identidade

Expandir o produto centrado e tomar esperança dá Cov(X,Y)=E[XY]−E[X]E[Y]. A covariância é simétrica e Cov(X,X)=Var(X). A identidade matemática não garante estabilidade em ponto flutuante quando os produtos grandes quase se cancelam; o laboratório racional fornece referências.

Cov(X,Y)=E[XY]−E[X]E[Y]

## Unidades e transformações afins

Se X está em metros e Y em segundos, a covariância tem unidade metro×segundo. Somar constantes não altera os desvios. Multiplicar por escalas a e b dá Cov(aX+c,bY+d)=abCov(X,Y). Um sinal negativo em apenas uma escala inverte o sinal da covariância.

Cov(aX+c,bY+d)=abCov(X,Y)

## Correlação remove escala quando ambas as variâncias são positivas

Defina ρ=Cov(X,Y)/(σₓσᵧ) quando σₓ>0 e σᵧ>0. Ela é sem dimensão. Translações não alteram ρ; escalas positivas mantêm o valor e uma escala negativa inverte o sinal. Se uma variável tem variância zero, a divisão é indefinida: não informe correlação zero como substituto.

ρ=Cov(X,Y)/(σₓσᵧ)

## Por que a correlação fica entre −1 e 1

Padronize U=(X−E[X])/σₓ e V=(Y−E[Y])/σᵧ. Suas variâncias são 1 e Cov(U,V)=ρ. Como Var(U+V)=2+2ρ≥0 e Var(U−V)=2−2ρ≥0, segue −1≤ρ≤1. Se ρ=1, U−V tem variância zero; se ρ=−1, U+V tem variância zero. Isso explica relações afins perfeitas, sob essas hipóteses.

−1≤ρ≤1

## Um modelo quadrático fornece um contraexemplo

Escolha X equiprovável em {−2;−1;0;1;2} e Y=X². Então E[X]=0, E[Y]=2 e E[XY]=E[X³]=0. A covariância e a correlação são zero, mas Y é determinado por X. Mais diretamente, P(X=0,Y=0)=1/5, diferente do produto P(X=0)P(Y=0)=1/25. A fatoração de independência falha.

## Independência implica covariância zero, com momentos

Se X e Y são independentes e os momentos usados existem, E[XY]=E[X]E[Y], então Cov=0. A recíproca não vale em geral. Uma hipótese especial de normal conjunta permite conclusões adicionais, mas marginais normais separadas não justificam assumir normal conjunta ou independência. Sempre identifique a distribuição conjunta.

## A matriz de covariância conecta estatística e álgebra

Para duas variáveis, Σ tem variâncias na diagonal e covariância nos dois elementos fora dela. Para qualquer vetor de coeficientes (u,v), (u,v)Σ(u,v)ᵀ=Var(uX+vY)≥0; portanto Σ é positiva semidefinida. Ter uma matriz diagonal não prova independência geral: o exemplo quadrático tem covariância zero e dependência.

Σ=[[Var(X),Cov(X,Y)],[Cov(X,Y),Var(Y)]]

## A melhor reta é uma projeção linear

Para minimizar E[(Y−α−βX)²] com Var(X)>0, as condições de primeira ordem dão β=Cov(X,Y)/Var(X) e α=E[Y]−βE[X]. No exemplo Y=X² simétrico, β=0 e a melhor reta é constante, apesar da relação não linear exata. Melhor reta não significa melhor função entre todas as possíveis.

β=Cov(X,Y)/Var(X)

## Modelo populacional e estimativa amostral não são a mesma coisa

A demonstração atribui peso 1/5 a cada ponto e calcula momentos do modelo. Em uma amostra real, covariância e correlação são estimadas e variam entre coletas. Usar o mesmo divisor n ou n−1 nas covariâncias e variâncias amostrais produz a mesma razão de correlação quando os desvios são não nulos, mas isso não elimina viés de seleção ou incerteza.

## Causalidade, diagnóstico e validação

Uma reta ajustada ou correlação alta não prova efeito causal. Variáveis omitidas, seleção, dependência temporal e outliers podem mudar a interpretação. Examine a relação no gráfico, a distribuição e o desenho da coleta. Os pontos e funções desta aula são sintéticos e não representam uma conclusão sobre dados da pesquisa.

## Exemplo resolvido

X equiprovável em cinco pontos e Y=X²: qual a covariância e por que há dependência?

1. Valores de X: −2,−1,0,1,2; valores de Y: 4,1,0,1,4.
2. E[X]=0 e E[Y]=2.
3. E[XY]=E[X³]=0 por simetria.
4. Cov(X,Y) = 0 − 0 × 2 = 0; as duas variâncias são positivas, logo ρ=0.
5. P(X=0,Y=0)=1/5, mas P(X=0)P(Y=0)=1/25.
6. Portanto, covariância zero não implica independência. A melhor reta é Y≈2 e não captura a parábola.

## Exercícios e resoluções

### Para X equiprovável em {−2;−1;0;1;2} e Y=X², qual Cov(X,Y)?

Simetria dá zero.

### Covariância zero sempre prova independência?

Sim
Não

Y=X² no exemplo é dependente.

### No mesmo modelo, quanto vale E[Y]?

(4+1+0+1+4)/5=2.

### No mesmo modelo, quanto vale Var(X)?

E[X]=0 e E[X²]=2.

### Se Cov(X,Y)=1, quanto vale Cov(3X+4,−2Y+10)?

As escalas multiplicam a covariância: 3×(−2)×1=−6.

### No modelo quadrático simétrico, qual a inclinação da melhor reta?

β=Cov(X,Y)/Var(X)=0/2=0.

### Se Y é constante, a correlação de Pearson com X é:

Automaticamente zero
Indefinida pela divisão por desvio zero

Covariância é zero, mas σᵧ=0 impede definir essa correlação.

### Uma matriz de covariância diagonal prova independência em qualquer distribuição?

Sim
Não

O exemplo quadrático tem matriz diagonal e dependência.

### Uma correlação alta prova que X causa Y?

Sim
Não

Associação não identifica sozinha o mecanismo causal ou o efeito de uma intervenção.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`, usando biblioteca padrão. p-valores por erfc e momentos conjuntos por frações; a correlação final usa ponto flutuante e retorna None para desvio zero. Sem ler dados privados ou escrever resultados externos.

## Proposta didática

Peça uma previsão antes de mudar controles; identifique hipótese ou distribuição conjunta; resolva um caso à mão; encerre com um contraexemplo à interpretação indevida. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Distribuição conjunta finita e equiprovável na demonstração.
- Momentos de segunda ordem finitos; correlação exige variâncias positivas.
- Reta minimiza erro quadrático dentro da classe afim, não de todas as funções.
- Dados sintéticos; associação não é inferência causal.
