# Normal: padronizar não torna todo dado gaussiano

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Interpretar μ, σ e σ² na família normal.
- Derivar a padronização e calcular probabilidades pela CDF.
- Distinguir padronização de uma hipótese de distribuição.
- Reconhecer precisão numérica e caudas fora de uma janela gráfica.

## Localização, escala e a convenção da notação

Na convenção X~N(μ,σ²), μ é a média e σ² é a variância. O desvio padrão σ é positivo nesta família com densidade. Alterar μ desloca a curva; alterar σ muda sua largura e altura. Informar N(10,4) significa aqui média 10 e variância 4, portanto desvio padrão 2. Declare a convenção ao comparar softwares e referências.

X~N(μ,σ²); σ>0

## A densidade inclui um fator de normalização

A densidade é f(x)=exp(−(x−μ)²/(2σ²))/(σ√(2π)). Ela é positiva em todo x real e tem área total 1. A integral gaussiana pode ser obtida elevando a integral ao quadrado e usando coordenadas polares no plano; o resultado fornece √(2π) para o fator padrão. Probabilidades são integrais, não valores isolados de f.

f(x)=exp(−(x−μ)²/(2σ²))/(σ√(2π))

## A mudança de variável demonstra a padronização

Defina Z=(X−μ)/σ, então x=μ+σz e dx=σdz. Substituindo na densidade e incluindo o fator σ do diferencial, obtemos φ(z)=exp(−z²/2)/√(2π). Portanto, quando X já é normal, Z é normal padrão. Dividir pela variância σ² não é a mesma transformação.

Z=(X−μ)/σ

## Média zero e variância um não bastam

A transformação afim padroniza os dois primeiros momentos de qualquer variável com média e variância finitas e variância positiva. Ela não força a forma normal. Se X vale −1 e 1 com pesos iguais, já tem média zero e variância um, mas continua discreta nesses dois pontos, não uma curva gaussiana.

## Os momentos da normal padrão também podem ser justificados

A simetria de φ torna E[Z]=0. Como φ′(z)=−zφ(z), uma integração por partes dá E[Z²]=−∫ zφ′(z) dz=1: o termo de fronteira zφ(z) tende a zero e a integral de φ é 1. Assim Var(Z)=1. Pela transformação inversa, E[X]=μ e Var(X)=σ².

E[Z]=0; Var(Z)=1

## CDF e simetria fornecem probabilidades

Escreva Φ(z)=P(Z≤z)=∫₋∞ᶻ φ(t)dt. Simetria dá Φ(−z)=1−Φ(z) e Φ(0)=1/2. No modelo normal, P(a≤X≤b)=Φ((b−μ)/σ)−Φ((a−μ)/σ) para a≤b; pontos isolados não têm massa. A sobrevivência é 1−Φ(z) na matemática.

Φ(z)=∫₋∞ᶻ φ(t)dt

## Intervalos de um, dois e três desvios

P(|Z|≤c)=2Φ(c)−1. Para c=1,2,3, as probabilidades são aproximadamente 0,682689; 0,954500; 0,997300. Dois desvios não correspondem exatamente a 95%; para 95% bilateral, o quantil é aproximadamente 1,959964. Essas probabilidades dependem da hipótese normal, não são regras universais sobre dados.

P(|Z|≤c)=2Φ(c)−1, c≥0

## Transformações afins preservam a família, com ressalva

Se X é normal e Y=aX+b com a≠0, então Y é normal de média aμ+b e variância a²σ². Para a<0, a distribuição padronizada é espelhada, mas a normal padrão é simétrica. Se a=0, Y é constante e não tem densidade normal com σ>0. A variância usa a²; o desvio padrão usa |a|.

## Janela gráfica não é o suporte inteiro

A demonstração mostra de μ−4σ a μ+4σ. A normal tem caudas fora dessa janela. A área preenchida visível até o ponto escolhido omite cerca de 0,00003167 na cauda esquerda, enquanto a CDF no relatório integra desde −∞. Isso é um corte de exibição, não truncamento da distribuição. A altura muda com σ e a área total teórica permanece 1.

## Cuidados numéricos em caudas pequenas

Calcular 1−CDF(x) com CDF arredondada perto de 1 pode perder uma cauda pequena. O Python usa erfc para obter diretamente acumulada ou sobrevivência e a compara com NormalDist em pontos de referência. Na interface, a CDF padrão usa Simpson composto com 512 subintervalos e z entre −3 e 3. É uma aproximação numérica conferida, não uma fórmula elementar exata.

## Uma hipótese de distribuição precisa de contexto

Ter uma curva com aparência de sino, ou padronizar observações, não comprova normalidade. O desenho da coleta, outliers, dependência e a pergunta da análise importam. Os parâmetros desta aula são escolhidos em modelos sintéticos; não foram estimados de dados pessoais, de clientes ou da IC.

## Exemplo resolvido

X~N(10,4): qual P(X≤14) e qual a probabilidade entre 8 e 12?

1. A variância é 4, portanto σ=2.
2. Para x=14, z = (14−10) / 2 = 2.
3. P(X≤14) = Φ(2) ≈ 0,977250.
4. Os limites 8 e 12 correspondem a z=−1 e z=1.
5. P(8≤X≤12) = Φ(1) − Φ(−1) ≈ 0,682689.
6. São probabilidades do modelo normal declarado; padronizar outros dados não prova essa hipótese.

## Exercícios e resoluções

### Com μ=10, σ=2 e x=14, qual z?

4/2=2.

### Padronizar qualquer dado garante distribuição normal?

Sim
Não

A forma da distribuição continua outra questão.

### Na convenção N(10,4), qual o desvio padrão?

O segundo parâmetro é variância; σ=√4=2.

### Qual Φ(0) na normal padrão?

Simetria e ausência de massa no ponto dão 1/2.

### Qual P(−1≤Z≤1) na normal padrão?

2Φ(1)−1≈0,682689.

### Se Var(X)=4, qual Var(−3X+2)?

(−3)²×4=36; a constante não muda a variância.

### Dois desvios padrão cobrem exatamente 95% na normal?

Sim
Não

Cobrem aproximadamente 95,45%; 95% bilateral usa cerca de 1,959964 desvios.

### O corte gráfico em quatro desvios elimina as caudas do modelo?

Sim
Não

O modelo tem suporte real inteiro; o corte é apenas de exibição.

### A variável equiprovável em {−1,1} é normal por ter média 0 e variância 1?

Sim
Não

Ela é discreta; os momentos não determinam por si só a forma da distribuição.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Apenas biblioteca padrão; distribuição binomial racional e referência normal por erfc. Não lê dados privados nem escreve resultados externos. O caso iid e o caso de cópias são modelos distintos.

## Proposta didática

Peça uma previsão antes de mudar n ou σ; separe distribuição do dado da distribuição da média; contraste exatidão com aproximação; termine com uma hipótese que impede aplicar a fórmula. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Família normal declarada com σ>0 quando as probabilidades normais são usadas.
- Convenção N(μ,σ²): segundo parâmetro é variância.
- CDF da interface é aproximação por Simpson na faixa declarada.
- Modelos sintéticos, sem diagnóstico ou ajuste de dados reais.
