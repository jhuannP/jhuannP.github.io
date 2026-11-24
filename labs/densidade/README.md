# Densidade e distribuição acumulada: integrar uma probabilidade

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Distinguir altura da densidade de probabilidade integrada.
- Construir uma CDF e obter probabilidades de intervalos.
- Reconhecer o papel de átomos e da convenção de extremos.
- Conferir suporte, normalização e unidades antes de calcular.

## A acumulada serve para diferentes tipos de distribuição

F(x)=P(X≤x) é a função de distribuição acumulada. Ela é não decrescente, contínua pela direita, com limites 0 quando x vai a −∞ e 1 quando x vai a +∞. Pode ter saltos quando há massa em pontos. Ter uma CDF não significa que toda distribuição possa ser descrita por uma densidade usual.

F(x)=P(X≤x)

## Densidade significa probabilidade por integração

Para as distribuições com densidade tratadas aqui, f(x) é não negativa e sua integral total é 1. A probabilidade de um intervalo é uma área sob a curva. O valor f(x) isolado não é P(X=x). Uma altura maior que 1 pode ser válida, desde que a área total seja 1.

P(a≤X≤b)=∫ₐᵇ f(t)dt, para a≤b

## Construa a CDF somando área à esquerda

Com densidade f, F(x)=∫₋∞ˣ f(t)dt. Na uniforme em [0;w], com w>0, F(x)=0 para x≤0, x/w para 0<x<w, e 1 para x≥w. A altura f=1/w é constante no suporte e zero fora dele. Valores atribuídos à densidade exatamente nos extremos não mudam a integral.

F(x)=∫₋∞ˣ f(t)dt

## Uma uniforme curta pode ter altura 2

Escolha w=0,5. A altura é 1/w=2, mas a área total é 2×0,5=1. Para o intervalo [0;0,1], a área é 2×0,1=0,2. A probabilidade fica entre 0 e 1; a altura não precisa. Na demonstração, a região preenchida representa a sobreposição do intervalo escolhido com o suporte.

f=1/w no suporte

## Interseção com o suporte evita área inventada

Para X uniforme em [0;0,5], o evento 0,4≤X≤0,8 só inclui [0,4;0,5]. Seu comprimento é 0,1 e sua probabilidade 0,2. Não integre a altura constante fora do suporte. Um intervalo inteiramente externo tem probabilidade zero; um intervalo que cobre o suporte inteiro tem probabilidade 1.

## Convenções de extremos fazem diferença quando há átomos

Para a<b, a fórmula geral P(a<X≤b)=F(b)−F(a) exclui a e inclui b. Para incluir também a, use F(b)−F(a−), onde F(a−) é o limite pela esquerda. Se não há massas nos extremos, as quatro escolhas aberto/fechado têm a mesma probabilidade. No modelo com densidade, P(X=x)=0.

P(a<X≤b)=F(b)−F(a)

## Um salto tem massa, não uma altura finita de densidade

Se X é 0 com probabilidade 1/2 e, com probabilidade 1/2, tem distribuição uniforme em [0;1], então F tem salto 1/2 em zero. A parte com densidade 1/2 no intervalo integra apenas 1/2; ela não representa o átomo restante. Uma probabilidade pontual positiva precisa ser tratada como massa, não como valor comum de f(0).

P(X=x)=F(x)−F(x−)

## Não confunda derivada, função e normalização

Quando a representação por densidade é válida e f é contínua no ponto, F′(x)=f(x), pelo Teorema Fundamental do Cálculo. Nem todo ponto precisa ter essa derivada, e diferenciar uma CDF com saltos não recupera suas massas como uma função usual. Para conferir um modelo, examine suporte, não negatividade e integral total.

## A unidade da densidade é inversa à de X

Se X é um tempo em segundos, a densidade tem unidade s⁻¹. Em Y=1000X, medido em milissegundos, a mesma uniforme vira [0;500] com altura 0,002 ms⁻¹. A probabilidade do evento correspondente, [0;100], continua 0,2. O eixo muda de unidade; a área de probabilidade é preservada.

2 s⁻¹×0,1 s = 0,002 ms⁻¹×100 ms = 0,2

## Intervalo vazio não é integral orientada negativa

Se o limite inferior excede o superior, não há valor satisfazendo as duas desigualdades: o evento tem probabilidade zero. Já uma integral orientada pode ser negativa ao inverter limites. Na interface, não trocamos os limites silenciosamente; informamos o evento vazio. F(b)−F(a) com b<a não deve ser interpretada como probabilidade.

## Densidade do modelo e histograma são objetos distintos

Um histograma de amostra pode estimar uma densidade, mas sua altura depende da largura das classes e da normalização. Na convenção de densidade, as áreas das barras somam 1; na convenção de contagens, as alturas representam outra grandeza. A curva desta aula é uma distribuição escolhida, não ajuste de dados ou validação empírica.

## Exemplo resolvido

Na uniforme [0;0,5], qual P(0,4≤X≤0,8)?

1. A densidade é 2 dentro do suporte e zero fora dele.
2. A interseção do evento com o suporte é [0,4;0,5].
3. Comprimento 0,1; área 2×0,1=0,2.
4. Pela CDF: F(0,8)=1 e F(0,4)=0,8; diferença 0,2.
5. Extremos isolados não têm massa neste modelo com densidade.

## Exercícios e resoluções

### Na uniforme [0;0,5], qual P(0≤X≤0,1)?

2×0,1=0,2.

### Densidade maior que 1 é necessariamente inválida?

Sim
Não

A normalização é pela integral.

### No mesmo modelo, quanto vale F(0,4)?

0,4/0,5=0,8.

### No mesmo modelo, quanto vale P(0,4≤X≤0,8)?

Apenas [0,4;0,5] pertence ao suporte; probabilidade 0,1/0,5=0,2.

### No mesmo modelo com densidade, quanto vale P(X=0,25)?

Um ponto tem comprimento zero; a probabilidade pontual é zero.

### Se a uniforme [0;0,5] está em segundos, qual altura da densidade em milissegundos?

O suporte tem 500 ms; altura 1/500=0,002 ms⁻¹.

### A diferença F(b)−F(a), com a<b, corresponde em geral a:

P(a<X≤b)
P(a≤X≤b) sem qualquer ressalva

A CDF em a já inclui a massa de a; subtraí-la exclui esse extremo.

### Se a>b, o evento a≤X≤b tem:

Probabilidade negativa
Probabilidade zero

O evento é vazio; não confundir com integral orientada.

### Uma massa de 1/2 em zero pode ser representada só por uma altura finita f(0)?

Sim
Não

Uma altura finita em um único ponto não fornece área positiva; é necessário tratar o átomo.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão, fórmulas analíticas sintéticas, sem ler dados privados ou escrever resultados externos. A implementação usa ponto flutuante e contratos de parâmetros documentados.

## Proposta de condução

Peça ao aluno identificar qual curva está vendo e suas unidades; prever uma probabilidade antes de mudar controles; calcular por duas formas; concluir com um caso em que a hipótese do modelo falha. A condução precisa de revisão didática de Jhuann.

## Hipóteses e limites

- Distribuição uniforme com largura positiva para as contas de área.
- CDF é geral; a representação por densidade aqui exige probabilidade por integração.
- Convenção dos extremos deve considerar massas pontuais.
- Curvas são modelos sintéticos, não histogramas ou ajustes de dados.
