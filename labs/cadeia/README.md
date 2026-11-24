# Regra da cadeia — notas para revisão e ensino


Aprofundamento original de 13/10/2026. Rascunho preparado com apoio de IA, para revisão de Jhuann. Não são notas importadas do Samsung Notes.


## Antes de começar: função de função

Pré-requisitos: derivada como aproximação linear e regras de soma/produto; conhecer as derivadas de potência, seno, exponencial e logaritmo usadas nos exemplos. Em y=g(f(x)), a função interna f transforma x em u; a externa g transforma esse u em y. Uma mesma expressão pode ser decomposta de mais de uma maneira, mas qualquer decomposição correta precisa reproduzir a função original. Para (1+2x)³, escolha f(x)=1+2x e g(u)=u³.


`x → u=f(x) → y=g(u)`


## Enunciado e ponto de avaliação

Se f é diferenciável em a e g é diferenciável em b=f(a), com a composição definida numa vizinhança de a, então g∘f é diferenciável em a. Multiplique a derivada externa avaliada na saída da função interna pela derivada interna. A condição da vizinhança impede aplicar uma fórmula num ponto sem domínio local adequado. Estas hipóteses são suficientes; a falta de uma delas não decide sozinha se a composição é diferenciável.


`(g∘f)′(a)=g′(f(a))·f′(a)`


## Por que as taxas multiplicam

Diferenciabilidade significa que o incremento da função é sua parte linear mais um resto pequeno em relação ao incremento da entrada. Escreva f(a+h)=b+f′(a)h+r_f(h), com r_f(h)/h→0. Para g, escreva g(b+k)=g(b)+g′(b)k+η(k)k, onde η(k)→0 e podemos definir η(0)=0. Esta escrita evita dividir por k quando k é zero. Como f é diferenciável, é contínua: o incremento k=f(a+h)−b tende a zero.


`k=f′(a)h+r_f(h); g(b+k)−g(b)=g′(b)k+η(k)k`


## Concluir a justificativa sem cancelar uma variação nula

Substitua a expressão de k no incremento de g e divida por h≠0. A parcela principal é g′(b)f′(a). O termo g′(b)r_f(h)/h tende a zero. O último termo é η(k)[f′(a)+r_f(h)/h], produto de algo que tende a zero por algo com limite finito. Assim, o quociente incremental tende a g′(b)f′(a). Nada exigiu f′(a)≠0 nem k≠0. A notação dy/dx=(dy/du)(du/dx) resume essa regra; sua justificativa não é tratar derivadas como frações comuns.


`[g(f(a+h))−g(f(a))]/h = g′(b)[f′(a)+r_f(h)/h] + η(k)[f′(a)+r_f(h)/h]`


## Exemplo 1: potência composta, com conferência independente

Para y=(1+2x)³, u=1+2x e du/dx=2. A taxa externa é 3u². Substituir u de volta dá y′=6(1+2x)². Em x=1, u=3 e a derivada é 3×9×2=54. Uma conferência independente vem de expandir y=1+6x+12x²+8x³, cuja derivada é 6+24x+24x², igual à expressão obtida. Não é necessário expandir toda composição: aqui isso apenas confirma um caso.


`3(1+2x)² × 2 = 6(1+2x)²`


## Exemplo 2: uma composição com três etapas

Para y=exp(sin(x²)), defina u=x², v=sin(u) e y=exp(v). De dentro para fora: du/dx=2x; dv/du=cos(u); dy/dv=exp(v). O produto é 2x·cos(x²)·exp(sin(x²)). Escreva as etapas antes de substituir, para evitar cos(2x), que não é a derivada de sin(x²). Em x=0, o produto é zero por causa do fator interno 2x.


`dy/dx=(dy/dv)(dv/du)(du/dx)=exp(sin(x²))·cos(x²)·2x`


## Exemplo 3: domínio no logaritmo

Para y=ln(1−x²), exigimos 1−x²>0, logo −1<x<1. A função externa ln(u) tem derivada 1/u; a interna tem derivada −2x. Portanto y′=−2x/(1−x²) dentro desse intervalo. Uma expressão algébrica para a derivada não amplia o domínio da função original. Nos pontos x=±1, o logaritmo real sequer está definido.


`y′=−2x/(1−x²), para −1<x<1`


## Taxa interna zero e hipóteses suficientes

Para y=(x²)³=x⁶, a regra vale em zero e dá 3(x²)²·2x=0. Não precisamos excluir esse ponto. Já g(u)=|u| não é diferenciável em u=0, mas g(x²)=x² é diferenciável em x=0: o teorema não se aplica diretamente ali, e o resultado é verificado por outra análise. Por outro lado, sqrt(x²)=|x| não é diferenciável em zero. Estes exemplos mostram por que não devemos tirar conclusões só pela aparência da composição.


`f′(a)=0 é permitido; hipótese suficiente ≠ condição necessária`


## Quando somar e quando multiplicar

Composição corresponde a etapas em sequência e multiplica sensibilidades. Soma de funções corresponde a termos independentes e soma derivadas. Para y=(1+2x)³+sin(x²), derive cada termo e some: 6(1+2x)²+2x cos(x²). Em grafos computacionais maiores, diferentes caminhos podem contribuir para o mesmo resultado; multiplicamos fatores ao longo de cada caminho e somamos contribuições. Backpropagation usa esse princípio, mas a aula trabalha apenas exemplos escalares.


`d(A(x)+B(x))/dx=A′(x)+B′(x)`


## Conferir numericamente sem transformar o teste em prova

Diferença central usa [F(x+h)−F(x−h)]/(2h). Para F(x)=(1+bx)³, a expansão mostra que o valor em aritmética exata é F′(x)+b³h². Se b≠0, reduzir h à metade divide esse erro de truncamento por quatro. Mesmo no ponto em que F′=0, a aproximação com h finito pode ser não nula. Na máquina, passos muito pequenos também sofrem arredondamento/cancelamento; “menor h” não é garantia ilimitada de precisão. A simulação confere esse polinômio, enquanto a justificativa acima sustenta a regra geral.


`D_hF(x)=3b(1+bx)²+b³h²`


## Um roteiro para resolver e explicar

Primeiro declare o domínio; depois identifique cada etapa da composição. Escreva a derivada de cada etapa na sua própria variável, multiplique e substitua as variáveis internas. Só então avalie num ponto. Confira casos constantes, sinais e, se possível, uma expansão independente. Erros frequentes: omitir a taxa interna, avaliar g′ em x em vez de f(x), trocar composição por produto e usar uma conferência numérica como prova. Para ensinar, explique por que cada fator aparece, não apenas a fórmula final.


`domínio → etapas → taxas → produto → substituição → ponto`


## Exercícios e resoluções

Tente sem consultar a resposta; depois explique cada fator, domínio e hipótese.


### 1. Para y=(1+2x)³, qual y′(1)?


Resolução: 6×3²=54.


### 2. Pode omitir a derivada da função interna?

- Sim

- Não


Resolução: Esse fator é parte da regra da cadeia.


### 3. Para y=sin(x²), qual é a derivada?

- cos(x²)

- 2x cos(x²)

- cos(2x)


Resolução: Taxa externa cos(u), interna 2x: y′=2x cos(x²).


### 4. Para y=exp(3x), qual y′(0)?


Resolução: y′=3exp(3x); em zero, 3.


### 5. Para y=ln(1−x²), qual y′(1/2)? O ponto pertence ao domínio.


Resolução: −1/(1−1/4)=−1/(3/4)=−4/3.


### 6. O domínio real de ln(1−x²) é:

- Todos os reais

- −1<x<1

- x≤−1 ou x≥1


Resolução: 1−x²>0 equivale a |x|<1.


### 7. Para y=(x²)³, qual y′(0)?


Resolução: y=x⁶, y′=6x⁵, portanto zero.


### 8. Para F(x)=(1+2x)³ e h=0,1, qual o erro absoluto de truncamento da diferença central em aritmética exata?


Resolução: |2³×0,1²|=8×0,01=0,08.


### 9. Se g não é diferenciável em f(a), podemos concluir que g∘f não é diferenciável em a?

- Sim, sempre

- Não; as hipóteses do teorema são suficientes e é preciso outra análise

- Sim, se f′(a)=0


Resolução: g(u)=|u| não é diferenciável em zero, mas g(x²)=x² é. A ausência da hipótese impede usar diretamente o teorema, sem decidir o resultado.


## Conferência em Python

Salve experiment.py e rode `python3 experiment.py`. Com test_experiment.py ao lado, execute `python3 -m unittest discover -p 'test_*.py'`. Testes usam expansão independente, frações exatas, casos constantes/taxa zero e contratos. Conferência numérica não substitui demonstração.


## Revisão pessoal

Explique o enunciado e o argumento de restos sem ler, resolva três exemplos inéditos e identifique os domínios. Só depois avalie preparo para ensinar. Outras aulas e notas pessoais permanecem em preparação.
