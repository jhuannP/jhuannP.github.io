# Equilíbrio químico ideal — notas originais

16/10/2026. Rascunho para revisão de Jhuann.

## Equilíbrio não significa reação parada

Em equilíbrio químico macroscópico, a composição permanece constante, embora transformações direta e inversa possam continuar ocorrendo em igual taxa. Isso não implica quantidades iguais de reagentes e produtos. O balanço estequiométrico da aula anterior limita as composições possíveis; ainda precisamos de uma condição de equilíbrio para selecionar uma delas.

## O quociente depende do estado atual

Para uma reação escrita com coeficientes estequiométricos ν_i, Q=∏a_i^{ν_i}, onde a_i são atividades adimensionais. Produtos têm expoentes positivos e reagentes negativos. Em solução ideal diluída, uma aproximação é a_i=c_i/c°, com concentração padrão c°. Não atribua unidades a uma constante termodinâmica definida por atividades sem declarar a convenção.

## K é o valor de Q no equilíbrio

Para a reação e os estados padrão escolhidos, K(T)>0 fixa o quociente no equilíbrio à temperatura declarada. Mudar quantidades iniciais pode alterar Q e a composição final, mas não altera por si só K na mesma temperatura e convenção. Inverter a escrita da reação substitui K por 1/K; multiplicar todos os coeficientes por dois substitui K por K².

## A direção pode ser relacionada à energia livre

Com atividades positivas e temperatura absoluta T>0, Δ_rG=Δ_rG°+RT lnQ e Δ_rG°=−RT lnK. Logo Δ_rG=RT ln(Q/K). No contexto de temperatura e pressão constantes, Δ_rG<0 favorece o avanço direto e Δ_rG>0 o inverso; Q=K dá força motriz nula. Atividade zero exige cuidado com o limite do logaritmo, não calcular ln0 como número finito. O laboratório decide a direção por balanço e comparação exata, sem calcular logaritmos nos extremos.

## Um modelo 1:1 permite uma solução transparente

Considere A⇌B, duas formas hipotéticas de mesma composição atômica, numa fase ideal homogênea, com temperatura fixada. Na aproximação ideal, Q=c_B/c_A=n_B/n_A, pois o volume e o estado padrão se cancelam nessa razão 1:1. A e B não são dados de uma substância real; K é um parâmetro sintético para explorar o raciocínio.

## O balanço permite extensão positiva ou negativa

Com quantidades iniciais a₀,b₀, n_A=a₀−ξ e n_B=b₀+ξ. A condição de não negatividade é −b₀≤ξ≤a₀. Extensão negativa significa avanço no sentido inverso da escrita escolhida; não é quantidade negativa de uma espécie. O total n_A+n_B permanece a₀+b₀ neste modelo, mas essa soma não é conservada para reações de estequiometria arbitrária.

## Resolver Q=K seleciona um estado interior

Impondo (b₀+ξ)/(a₀−ξ)=K, obtemos ξ_eq=(Ka₀−b₀)/(1+K). As quantidades finais são n_A=(a₀+b₀)/(1+K) e n_B=K(a₀+b₀)/(1+K). Para total positivo e K finito positivo, ambas são positivas. No intervalo com n_A>0, Q cresce com ξ, pois dQ/dξ=(a₀+b₀)/(a₀−ξ)²>0; assim há um único estado que satisfaz Q=K.

## O exemplo diferencia estado e sentido de chegada

Com a₀=3 mol, b₀=1 mol e K=1, Q_inicial=1/3<K, ξ_eq=1 mol e o estado final é A=2 mol, B=2 mol. Começando de A=0 e B=4 mol, o mesmo K e total levam ao mesmo estado final, agora com ξ_eq=−2 mol. A ausência inicial de A dá uma razão não finita; o sentido inverso é interpretado pelo limite e pelo balanço, sem divisão por zero no código.

## K grande não significa reação rápida

Para total 1 mol e K=4, a fração final de B é 4/5 e a de A é 1/5. A composição favorece B, mas isso não fornece a velocidade de aproximação ao equilíbrio. Um catalisador pode alterar o caminho e as taxas sem alterar K na mesma temperatura. Parâmetros de cinética e detalhes do mecanismo precisam de outro modelo.

## Deslocamento deve ser analisado no modelo correto

Adicionar espécies muda Q e pode provocar nova evolução. Neste modelo ideal 1:1, mudar o volume multiplicando ambas as concentrações pelo mesmo fator não muda Q, portanto não desloca a razão de equilíbrio. Isso não é regra para toda reação: quando a soma dos coeficientes muda ou a idealidade falha, a análise também muda. Temperatura pode mudar K; a demonstração compara valores de K sem prever sua dependência térmica.

## Uma curva de estados finais não é trajetória no tempo

O gráfico mostra a fração de B no equilíbrio em função de K, e uma linha da fração inicial escolhida. Ele não representa a relaxação temporal nem uma medição de laboratório. Os testes verificam conservação e Q=K em aritmética racional. Reações com outras proporções, gases não ideais, múltiplos equilíbrios e atividades calculadas a partir de modelos reais permanecem pendentes.

## Resoluções

Com a₀=3, b₀=1 e K=1, qual ξ_eq em mol?

(1×3−1)/(1+1)=1 mol.

Nesse exemplo, quantos mol de A há no equilíbrio?

3−1=2 mol.

Nesse exemplo, qual Q inicial? Aceita fração.

b₀/a₀=1/3.

Com total 1 mol e K=4, qual a fração de B no equilíbrio?

K/(1+K)=4/5.

Com a₀=0, b₀=4 e K=1, qual ξ_eq em mol?

(0−4)/2=−2 mol, sentido inverso.

Equilíbrio exige quantidades iguais de A e B para qualquer K?

As quantidades dependem de K e da estequiometria.

Mudar apenas as quantidades iniciais muda K na mesma temperatura e convenção?

Muda Q e pode mudar a composição, não K por si só.

Um K grande determina uma aproximação rápida ao equilíbrio?

K descreve equilíbrio, não tempo ou taxa.

A curva de fração final versus K é uma trajetória temporal?

Cada ponto é um equilíbrio de um modelo com outro K.

## Roteiro de ensino e evidência

Pré-requisitos: quantidade de matéria, extensão e proporções. Fixar a reação e convenção; escrever Q; combinar balanço e K; conferir positividade, conservação e sentido. Pedir um mesmo estado final atingido a partir de dois estados iniciais e explicar por que isso não determina o tempo de chegada. Produto: solução própria com K≠1 e comentário sobre as hipóteses de atividade. Nenhum experimento real foi realizado.

## Fonte e pendências

Escopo: [CCM0114](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114), consulta de 16/10/2026. Referências e diferenças de edição no mapa da disciplina. Modelo, exemplos e código próprios. A ligação termodinâmica foi apresentada sem desenvolver integralmente potenciais químicos e minimização de G; esse aprofundamento permanece pendente. Outros casos: estequiometrias gerais, equilíbrio ácido-base, atividades não ideais e cinética.


Definições conferidas na IUPAC em 16/10/2026: [constante de equilíbrio](https://goldbook.iupac.org/terms/view/E02177) e [constante padrão e Gibbs](https://goldbook.iupac.org/terms/view/S05915). Nesta aula, K é usado para a constante padrão por atividades adimensionais, sem escrever o sobrescrito padrão em cada ocorrência. Não confundir com quocientes baseados em concentrações sem normalização explicitada.
