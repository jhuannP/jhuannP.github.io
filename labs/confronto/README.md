# Confronto: controlar uma oscilação por uma faixa

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Enunciar e justificar o Confronto por épsilon-delta.
- Construir cotas válidas em todo um entorno.
- Distinguir oscilação sem limite de oscilação com amplitude controlada.
- Separar limite, extensão contínua e propriedades da derivada.

## Duas cotas com o mesmo destino controlam a função

Se g(x)≤f(x)≤h(x) em um entorno perfurado de a e g,h tendem ao mesmo L, então f tende a L. A desigualdade precisa valer para todos os pontos admissíveis suficientemente próximos, não apenas uma tabela. As cotas não precisam ser iguais em cada x.

g≤f≤h e lim g=lim h=L ⇒ lim f=L

## Justifique o teorema com uma única tolerância

Dada ε>0, escolha raios para que g fique acima de L−ε e h abaixo de L+ε. Reduza δ ao menor desses raios e do raio onde a desigualdade é válida. Nesse entorno, L−ε<g(x)≤f(x)≤h(x)<L+ε, portanto |f(x)−L|<ε. Isso demonstra a definição do limite.

L−ε<f(x)<L+ε ⇒ |f(x)−L|<ε

## Uma forma útil controla o módulo do erro

Se |f(x)−L|≤r(x), com r(x)≥0 e r(x)→0, então f(x)→L. As duas cotas são L−r(x) e L+r(x). Separar um erro em sinal de uma cota não negativa costuma facilitar a prova. Uma cota é um limite superior, não necessariamente o valor exato do erro.

|f(x)−L|≤r(x)→0 ⇒ f(x)→L

## A desigualdade trigonométrica é global

Como |sin t|≤1 em radianos, para x≠0 temos |x² sin(1/x)|≤x². Assim −x² e x² prendem a função e tendem a zero. A frequência crescente da oscilação não impede esse limite, porque sua amplitude é dominada.

−x²≤x² sin(1/x)≤x²

## Uma escolha explícita de δ mostra a garantia

Para ε>0, use δ=√ε. Se 0<|x|<δ, então |x² sin(1/x)|≤x²<ε. O fator oscilatório não precisa ser calculado em cada ponto para garantir o erro. Uma escolha menor de δ também funcionaria.

δ=√ε

## Sem amplitude decrescente, duas sequências refutam o limite

Defina xₙ⁺=1/(π/2+2πn) e xₙ⁻=1/(3π/2+2πn). Ambas tendem a zero por valores positivos. Pela identidade trigonométrica, sin(1/xₙ⁺)=1 e sin(1/xₙ⁻)=−1. As saídas têm destinos distintos, então sin(1/x) sozinho não tem limite em zero. Esse argumento usa famílias inteiras, não uma amostra finita.

## A família da demonstração distingue três casos

Considere fₚ(x)=|x|ᵖ sin(1/x), x≠0. Para p=0, as cotas são constantes ±1 e não têm o mesmo limite; as sequências acima mostram a falta de limite. Para p=1 ou p=2, ±|x|ᵖ tendem a zero e o Confronto garante limite zero. Ter limites diferentes nas cotas apenas impede usar o teorema dessa forma; não prova, sozinho, que toda função presa entre elas não tem limite.

## Preencher o ponto é uma etapa posterior

A fórmula com 1/x não define a função em zero. Para o caso p=2, definir f(0)=0 produz uma extensão contínua; outro valor mantém o limite zero e quebra a continuidade. A prova do limite não usa o valor isolado, como nos exemplos de furo estudados antes.

## Uma ponte para derivadas

Na extensão de x² sin(1/x) por zero, o quociente de diferença em zero é h sin(1/h). Seu módulo é no máximo |h|, então tende a zero pelo Confronto: a derivada em zero existe e vale 0. Para |x| sin(1/x) estendida por zero, as sequências positivas produzem quocientes +1 e −1; a função é contínua, mas não tem derivada em zero.

derivada em zero do caso p=2 é 0

## Gráficos finitos não desenham todas as oscilações

A interface amostra a curva fora de |x|<0,002, mostra as cotas e pontos escolhidos nas sequências analíticas. Não mostra um número infinito de oscilações nem fornece a prova por aparência. O argumento é a desigualdade universal e o limite das cotas; o laboratório verifica casos e identidades numéricas.

## Exemplo resolvido

Como garantir |x² sin(1/x)|<0,01 perto de zero?

1. Use |sin(1/x)|≤1 para x≠0.
2. Então o módulo do produto é no máximo x².
3. Escolha δ=√0,01=0,1.
4. Se 0<|x|<0,1, temos x²<0,01.
5. A conclusão vale em todo o entorno perfurado; não precisa prever a fase do seno.

## Exercícios e resoluções

### Qual cota x² para |x² sin(1/x)| em x=0,1?

x²=0,01.

### sin(1/x) sozinho tende a zero?

Sim
Não

A oscilação não tem limite; o fator x² é essencial.

### Pela construção δ=√ε, qual δ para ε=0,04?

√0,04=0,2.

### Qual cota x² para o módulo em x=−0,2?

(−0,2)²=0,04.

### Qual o limite de x² sin(1/x) em zero?

As cotas ±x² tendem a zero.

### Na extensão por f(0)=0 do caso p=2, qual a derivada em zero?

O quociente h sin(1/h) fica em módulo abaixo de |h| e tende a zero.

### Cotas constantes −1 e 1, sozinhas, concluem limite zero?

Sim
Não

As duas cotas não tendem ao mesmo valor; essa forma do Confronto não conclui o limite.

### A cota x² precisa ser o valor exato de |x² sin(1/x)|?

Sim
Não

É um limite superior; o seno pode ter módulo menor que 1.

### Verificar cem pontos substitui a desigualdade em todo o entorno?

Sim
Não

Os testes são finitos; a prova usa a desigualdade universal.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão, intervalos racionais e avaliação trigonométrica em ponto flutuante. Casos computacionais não substituem as provas. Não lê dados privados nem escreve resultados externos.

## Preparação manuscrita

Escreva enunciado e hipóteses; justifique o exemplo; separe existência de cálculo, ou cota de valor exato; desenhe o contraexemplo; resolva exercícios antes da ferramenta. Revisão e notas pessoais de Jhuann continuam pendentes.

## Hipóteses e limites

- Desigualdades válidas em todo o entorno perfurado pertinente.
- As duas cotas tendem ao mesmo valor para aplicar o Confronto.
- Trigonometria em radianos e x≠0 na fórmula original.
- Gráfico amostrado com corte de exibição; não prova por amostragem.
