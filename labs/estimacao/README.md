# Estimador e estimativa: separar regra e resultado

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Distinguir estimador, estimativa e parâmetro.
- Derivar a decomposição do erro quadrático médio.
- Justificar o divisor n−1 sob iid com variância finita.
- Comparar critérios de qualidade sem confundir não viés com exatidão.

## Parâmetro, regra e resultado têm papéis diferentes

O parâmetro θ descreve a distribuição populacional escolhida, por exemplo μ ou σ². O estimador T é uma função dos dados aleatórios antes de observá-los. A estimativa t é o valor dessa função na amostra coletada. Para dados 1,2,3, a regra média amostral produz 2; o valor 2 não se torna automaticamente a média da população.

T=T(X₁,…,Xₙ); t=T(x₁,…,xₙ)

## A distribuição do estimador permite avaliar a regra

Repetir o desenho de coleta produz valores diferentes de T. A média amostral iid tem esperança μ e variância σ²/n. Essas propriedades pertencem ao procedimento sob um modelo, não são erros conhecidos de uma estimativa particular. Uma amostra observada não fornece, sozinha, todas as repetições que definem esse risco.

## Viés é deslocamento da esperança

Defina Bias(T)=E[T]−θ quando a esperança existe. Não viesado significa E[T]=θ, e não T=θ em toda amostra. Um estimador pode ter variância grande sem viés; outro pode introduzir um deslocamento pequeno e ter menor dispersão. A comparação precisa declarar o parâmetro, o modelo e o critério de perda.

Bias(T)=E[T]−θ

## Demonstre a decomposição do erro quadrático médio

Escreva T−θ=(T−E[T])+(E[T]−θ). Ao elevar ao quadrado e tomar esperança, o termo cruzado desaparece porque E[T−E[T]]=0. Portanto E[(T−θ)²]=Var(T)+Bias(T)². A identidade exige os momentos usados. Erro quadrático médio, viés e variância não são intercambiáveis.

MSE(T)=Var(T)+Bias(T)²

## Na amostra, dois divisores respondem a convenções distintas

A soma SS=Σᵢ(xᵢ−x̄)² descreve os desvios à média observada. Dividir por n dá a variância descritiva dessa lista. Dividir por n−1, para n>1, corresponde à regra usual de estimação não viesada da variância populacional sob iid. Nos dados 1,2,3, SS=2, então as duas respostas são 2/3 e 1.

Vₙ=SS/n; s²=SS/(n−1)

## Por que o divisor n−1 remove o viés sob iid

No modelo iid de média μ e variância σ² finita, a identidade SS=Σᵢ(Xᵢ−μ)²−n(X̄−μ)² dá E[SS]=nσ²−n(σ²/n)=(n−1)σ². Assim E[s²]=σ² e E[Vₙ]=((n−1)/n)σ². A demonstração usa a variância da média; dependência ou outros desenhos precisam de outra conta.

E[SS]=(n−1)σ²; E[s²]=σ²

## Não viés não implica o menor MSE

No modelo de quatro Bernoullis iid com p=1/2, a variância populacional é 1/4. A regra Vₙ tem esperança 3/16, viés −1/16 e MSE 5/512. A regra s² tem viés zero, mas MSE 1/96. Como 5/512<1/96, a regra viesada tem menor MSE nesse caso. A demonstração calcula todas as contagens possíveis; não generalize essa comparação a todos os modelos ou critérios.

MSE(V₄)=5/512 < 1/96=MSE(s²)

## Um modelo normal explica outra origem do divisor n

Para uma amostra não constante de observações normais iid com μ e σ² desconhecidos, maximizar a verossimilhança fornece μ̂=x̄ e σ̂²=SS/n. Após substituir x̄, a log-verossimilhança em τ=σ² é constante−(n/2)ln(τ)−SS/(2τ); sua derivada zera em τ=SS/n. Isso é um critério de otimização, não uma prova de não viés. Se SS=0, o máximo não ocorre em uma variância estritamente positiva: há um caso de fronteira.

## Consistência e não viés são perguntas diferentes

Consistência trata o comportamento de Tₙ ao aumentar n; não viés trata sua esperança em cada tamanho. Um estimador pode ser viesado para n finito e consistente. Antes de alegar consistência, identifique o limite e as hipóteses. Na Bernoulli finita, a média é consistente pelas contas da lei fraca; isso não autoriza classificar qualquer nova regra sem justificativa.

## Momentos e coleta continuam sendo parte da avaliação

Não viés da variância usa momentos de segunda ordem finitos nas hipóteses acima. Avaliar seu MSE exige momentos adicionais pertinentes; um quarto momento finito é uma condição suficiente usual. O modelo Bernoulli é limitado e não tem esse problema. Mais dados e uma correção de divisor não removem automaticamente seleção enviesada ou dependência.

## A demonstração avalia regras, não uma população real

Aqui p é conhecido para construir um modelo e avaliar o risco das regras. Em dados reais, o parâmetro-alvo geralmente é desconhecido e precisa ser estimado. O gráfico não informa o erro de um resultado da IC ou de um cliente. Para uma aplicação, documente população, coleta, tamanho, unidades, regra e limitações.

## Exemplo resolvido

Nos dados sintéticos 1,2,3, quais são a média e as duas variâncias?

1. n=3 e x̄=2.
2. Desvios: −1,0,1; quadrados: 1,0,1.
3. SS=2.
4. Variância descritiva Vₙ = 2 / 3.
5. Regra com divisor n−1: s² = 2 / 2 = 1.
6. Uma regra não viesada sob um modelo não torna esta estimativa igual à variância populacional desconhecida.

## Exercícios e resoluções

### Nos dados 1,2,3, qual s² com divisor n−1?

2/2=1.

### Não viesado significa resultado exato em toda amostra?

Sim
Não

O estimador ainda tem variabilidade.

### Nos mesmos dados, qual a variância com divisor n?

SS=2 e n=3; resposta 2/3.

### Um estimador tem variância 0,04 e viés 0,1. Qual o MSE?

0,04+(0,1)²=0,05.

### Para n=4 e σ²=1/4, qual o viés de Vₙ=SS/n sob iid?

E[Vₙ]=(3/4)(1/4)=3/16; viés 3/16−1/4=−1/16.

### Sob iid, n=5 e σ²=2. Quanto vale E[SS]?

(n−1)σ²=4×2=8.

### A média 2 calculada na lista 1,2,3 é:

Uma estimativa observada
A prova de que μ=2 na população

É o valor da regra nessa lista; o parâmetro populacional não foi revelado.

### Uma regra não viesada tem sempre o menor MSE?

Sim
Não

O exemplo Bernoulli n=4 fornece uma regra viesada com MSE menor.

### Dividir por n−1 corrige automaticamente qualquer dependência entre observações?

Sim
Não

A demonstração do não viés usa a estrutura iid; covariâncias alteram a conta.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Usa biblioteca padrão: contas racionais de riscos Bernoulli e quantil normal de NormalDist. Não lê dados privados nem escreve resultados externos.

## Proposta didática

Comece separando regra e valor observado; peça uma previsão antes de variar tamanho/nível; confira a conta manual; termine identificando uma hipótese sem a qual o procedimento não se justifica. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Amostragem iid com variância finita para o não viés de s².
- MSE exige momentos pertinentes; o laboratório usa Bernoulli limitada.
- Riscos são expectativas sobre modelos sintéticos, não erros observados de uma amostra.
- Nenhuma comparação de MSE é declarada universal.
