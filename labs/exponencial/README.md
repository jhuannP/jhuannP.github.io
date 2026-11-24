# Exponencial: tempo de espera e taxa

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Distinguir densidade, CDF, sobrevivência e taxa.
- Derivar média, variância e falta de memória da exponencial.
- Converter corretamente taxa e escala com unidades.
- Reconhecer limites do modelo e calcular quantis por inversão.

## Declare suporte e parametrização

T representa um tempo não negativo. Na parametrização por taxa λ>0, f(t)=λe⁻λᵗ para t≥0 e f(t)=0 para t<0. λ tem unidade inversa de tempo. A escala θ=1/λ tem unidade de tempo. A taxa é parâmetro do modelo, não uma probabilidade que precise ser menor que 1.

f(t)=λe⁻λᵗ, t≥0

## A integral confirma a normalização

Integrar λe⁻λᵗ de 0 até um limite b dá 1−e⁻λᵇ. Como λ>0, a exponencial tende a zero quando b tende a infinito, e a área total é 1. A densidade pode superar 1 perto da origem se λ>1 na unidade escolhida; a integral permanece uma probabilidade.

## Acumulada e sobrevivência respondem a perguntas complementares

Para t≥0, F(t)=P(T≤t)=1−e⁻λᵗ e S(t)=P(T>t)=e⁻λᵗ. Para t<0, F(t)=0 e S(t)=1. O gráfico desta aula mostra sobrevivência, com valores de sobrevivência entre 0 e 1; não mostra a densidade λe⁻λᵗ. Densidade e sobrevivência têm unidades diferentes.

S(t)=e⁻λᵗ; F(t)=1−S(t)

## Probabilidades de intervalos são diferenças de sobrevivência

Para 0≤a≤b, P(a<T≤b)=F(b)−F(a)=e⁻λᵃ−e⁻λᵇ. Os extremos têm probabilidade zero neste modelo. A expressão equivalente e⁻λᵃ(1−e⁻λ⁽ᵇ⁻ᵃ⁾) ajuda a evitar subtrair dois números quase iguais quando o intervalo é curto.

P(a<T≤b)=S(a)−S(b)

## A média vem da área sob a sobrevivência

Para T≥0, E[T]=∫₀∞ S(t)dt. Inserindo S(t)=e⁻λᵗ, a integral vale 1/λ. A área da sobrevivência tem unidade de tempo e não precisa ser 1; quem integra 1 é a densidade. Esta distinção explica por que duas curvas exponenciais parecidas respondem a perguntas distintas.

E[T]=1/λ

## Segundo momento e variância

Usando E[T²]=2∫₀∞ tS(t)dt e integração por partes, obtemos 2/λ². Subtrair (E[T])² fornece Var(T)=1/λ². O desvio padrão é 1/λ, igual à média neste modelo. Essa igualdade caracteriza aqui um cálculo da exponencial, não todos os tempos de espera.

E[T²]=2/λ²; Var(T)=1/λ²

## Demonstre a falta de memória

Para s,t≥0, o evento T>s+t está contido em T>s. A probabilidade condicional é S(s+t)/S(s). Como S(s)>0 para s finito, a divisão é válida; substituir as exponenciais dá e⁻λᵗ=S(t). O tempo adicional tem a mesma distribuição condicionada a ter esperado s, neste modelo.

P(T>s+t|T>s)=S(s+t)/S(s)=S(t)

## Uma uniforme mostra que a propriedade não é universal

Se T é uniforme em [0;2], P(T>0,5)=3/4. Depois de esperar 1 sem o evento ocorrer, a chance de esperar mais 0,5 é P(T>1,5|T>1)=(1/4)/(1/2)=1/2, diferente de 3/4. Há memória no sentido dessa comparação. Não atribua falta de memória a uma espera real apenas porque ela é aleatória.

## Taxa de ocorrência e risco instantâneo

Para a exponencial, f(t)/S(t)=λ, uma taxa constante. Isso compara a massa em um intervalo curto com a chance de ainda não ter ocorrido o evento. É uma taxa por unidade de tempo, não P(T=t), que vale zero. Em modelos com taxa dependente do tempo ou de um estado, a forma exponencial simples pode ser inadequada.

f(t)/S(t)=λ

## A relação com Poisson depende do modelo escolhido

Em um processo de Poisson homogêneo com taxa λ, a espera pelo primeiro evento excede t exatamente quando N(t)=0. Como P(N(t)=0)=e⁻λᵗ, essa espera é exponencial. Isso não transforma todo primeiro tempo de saída de uma dinâmica física em uma exponencial: é necessário justificar as hipóteses do processo e avaliar o fenômeno.

## Quantis e transformação inversa

Resolver u=F(t) para 0≤u<1 dá t=−ln(1−u)/λ. Para u=1/2, a mediana é ln(2)/λ, diferente da média 1/λ. Se U for uniforme adequadamente gerado, essa transformação pode produzir uma amostra exponencial. O laboratório confere a inversão para valores determinados de u; não testa um gerador aleatório. Não substitua u=1 por outro valor silenciosamente: a inversão não dá tempo finito nesse extremo.

F⁻¹(u)=−ln(1−u)/λ

## Unidades, precisão e limites do laboratório

λ=2 por hora dá média 0,5 hora, ou 30 minutos. Em minutos, a taxa é 1/30 por minuto. No código, expm1 e log1p ajudam para probabilidades pequenas e quantis próximos da origem. Sobrevivência muito pequena pode arredondar para zero na exibição sem ser zero na teoria. O laboratório limita a taxa a [0,01;100]; a interface usa [0,25;4], limites práticos e não teóricos.

## Exemplo resolvido

Taxa 2 por hora: qual média e chance de esperar mais 0,4 hora após 0,3 hora?

1. A média é 1/2 hora, ou 30 minutos.
2. A condição é T>0,3; queremos P(T>0,7|T>0,3).
3. S(0,7) / S(0,3) = exp(−1,4) / exp(−0,6) = exp(−0,8) ≈ 0,449329.
4. É igual a P(T>0,4), pela falta de memória do modelo.
5. A chance de ocorrer até 0,4 hora é 1−exp(−0,8)≈0,550671.
6. A conclusão decorre dos parâmetros hipotéticos; não valida uma espera observada.

## Exercícios e resoluções

### Com taxa λ=2 por hora, qual a média em horas?

1/2.

### Toda espera real tem automaticamente falta de memória?

Sim
Não

É uma propriedade do modelo exponencial.

### Com λ=2 por hora, qual a variância em horas ao quadrado?

1/λ²=1/4 h².

### Com λ=2, qual P(T>0,4)?

e^(−2×0,4)=e^(−0,8)≈0,449329.

### Com λ=2, qual P(T>0,7|T>0,3)?

S(0,7)/S(0,3)=e^(−0,8), igual a P(T>0,4).

### Com λ=2, qual a mediana na unidade de tempo adotada?

Resolva F(t)=1/2: t=ln(2)/2≈0,346574.

### Para T uniforme em [0;2], qual P(T>1,5|T>1)?

(1/4)/(1/2)=1/2; não é P(T>0,5)=3/4.

### Aumentar λ na mesma unidade de tempo faz a média:

Aumentar
Diminuir

A média é 1/λ; taxa e escala são inversas.

### A área total sob a sobrevivência exponencial é:

Sempre 1
A média 1/λ

A densidade integra 1; a sobrevivência integra o tempo médio.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão, fórmulas analíticas sintéticas, sem ler dados privados ou escrever resultados externos. A implementação usa ponto flutuante e contratos de parâmetros documentados.

## Proposta de condução

Peça ao aluno identificar qual curva está vendo e suas unidades; prever uma probabilidade antes de mudar controles; calcular por duas formas; concluir com um caso em que a hipótese do modelo falha. A condução precisa de revisão didática de Jhuann.

## Hipóteses e limites

- Modelo exponencial com taxa constante positiva e suporte não negativo.
- Falta de memória é deduzida do modelo, não presumida para toda espera.
- Taxa e escala têm unidades recíprocas.
- Laboratório sintético; não representa ajuste, validação ou resultado da IC.
