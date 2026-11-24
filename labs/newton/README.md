# Newton: tangente, hipótese local e falha de derivada

Aprofundamento original de 13/10/2026 com apoio de IA para revisão de Jhuann. Referência temática Burden, Faires e Burden, 10ª edição; exemplos próprios, sem transcrição.

## Da linearização ao próximo candidato

Perto de x_n, a reta tangente é f(x_n)+f′(x_n)(x−x_n). Seu zero é x_n−f(x_n)/f′(x_n), quando a derivada é não nula. Newton usa esse zero como próxima entrada, em vez de calcular uma raiz exata da função inteira a cada passo. O método precisa da função e de sua derivada, com domínios compatíveis. A tangente não garante que o novo ponto permaneça no intervalo anterior.

`x_{n+1}=x_n−f(x_n)/f′(x_n)`

## Exemplo para √2

Para f(x)=x²−2 e x₀=1,5, f=0,25 e f′=3. O próximo valor é 1,5−0,25/3=17/12≈1,4166667. A fórmula pode ser escrita (x+2/x)/2 para x≠0. De uma entrada positiva, os próximos candidatos continuam positivos, mas essa propriedade é deste problema, não regra geral de Newton.

`x₁=17/12`

## A garantia quadrática é local

Se f é duas vezes continuamente diferenciável numa vizinhança de uma raiz simples r, com f′(r)≠0, e o ponto inicial está suficientemente perto, Newton converge a r com erro controlado quadraticamente. A vizinhança precisa permitir avaliar os passos e manter a derivada afastada de zero. A palavra local importa: a mesma função pode ter entradas mais distantes que causam falhas ou convergem a outra raiz.

`|e_{n+1}|≤C|e_n|² perto de uma raiz simples`

## Justificar a relação de erros

Taylor entre x_n e r dá 0=f(x_n)+f′(x_n)(r−x_n)+f″(ξ)(r−x_n)²/2. Substituindo na atualização, e_{n+1}=f″(ξ)e_n²/[2f′(x_n)]. Se |f″|≤M e |f′|≥μ>0 na vizinhança, então |e_{n+1}|≤M|e_n|²/(2μ). Essa cota, junto de um início próximo, mantém os passos controlados. Na máquina, arredondamento limita a faixa em que uma razão de erros observada exibe esse padrão.

`e_{n+1}=f″(ξ)e_n²/[2f′(x_n)]`

## Raiz múltipla muda a ordem

Para f(x)=x² e raiz r=0, a derivada também zera na raiz, portanto ela não é simples. Fora de zero, Newton dá x_n−x_n²/(2x_n)=x_n/2: o erro diminui linearmente por fator 1/2, não quadraticamente. O método pode encontrar a raiz se a entrada já zera f, mas isso não restaura a hipótese da convergência quadrática. Métodos modificados para multiplicidade conhecida exigem análise própria.

`f(x)=x² ⇒ x_{n+1}=x_n/2, para x_n≠0`

## Derivada zero com valor não zero impede o passo

Para x²−2 começando em zero, f(0)=−2 e f′(0)=0. A reta tangente é horizontal e não fornece a atualização por divisão. O código sinaliza ArithmeticError em vez de fabricar um passo. Mesmo uma derivada pequena, embora não exatamente zero, pode produzir salto grande; identificar escala e domínio continua necessário. Se f já é zero na representação, o código trata esse caso antes da divisão.

`f(x_n)≠0 e f′(x_n)=0 ⇒ passo indefinido`

## Um ciclo com derivadas válidas

Para f(x)=x³−2x+2, de x₀=0 obtemos 1; de 1 voltamos a 0. A derivada é −2 em zero e 1 em um, portanto nenhuma dessas divisões usa derivada zero. A sequência alterna sem aproximar uma raiz. Um orçamento evita execução ilimitada, mas não transforma o ciclo em convergência. O arquivo de exemplo confere essa interrupção.

`0 → 1 → 0 → 1 → …`

## Comparar com bisseção e ponto fixo

Bisseção preserva um intervalo com raiz quando suas hipóteses valem e reduz a largura de forma previsível. Newton pode ser muito mais rápido perto de raiz simples, mas não preserva o intervalo automaticamente. Ele também é uma iteração de ponto fixo g=x−f/f′ onde definida; g′(r)=0 numa raiz simples ajuda a entender a rapidez local. Combinar proteção por intervalo com passos de Newton é uma possibilidade de projeto, ainda não implementada nesta aula.

`rapidez local de Newton ≠ garantia global de intervalo`

## Passo e resíduo são critérios distintos

O código usa tolerância xtol para mudança de posição, com escala 1+|novo|, e ftol para resíduo. Ambos precisam cumprir o critério, salvo um zero diretamente avaliado. Isso detecta algumas falhas, mas não prova uma cota universal da distância à raiz. Funções quase planas ou dados imprecisos pedem análise adicional. Uma exceção de orçamento, domínio ou derivada precisa ser relatada como falha/limite, não como resultado bem-sucedido.

`passo + resíduo + hipóteses do problema`

## Roteiro para usar e ensinar

Declare função, derivada e domínio; justifique a escolha inicial e se há raiz simples relevante. Trace o primeiro passo por conta manual, acompanhe candidatos e motivos de término. Compare com uma referência conhecida e teste derivada zero, raiz múltipla e ciclo. Se disser “quadrático”, indique as condições e o regime de erro, em vez de inferir pela aparência de uma sequência curta. Registre quais proteções o código de fato implementa.

`f, f′ e domínio → início → passos → critérios → análise`

## Exercícios e resoluções

Tente antes de consultar; declare domínio, condições e critério de parada.

### 1. Qual é o primeiro passo do exemplo, como número ou fração?

Resolução: 1.5−0.25/3=17/12.

### 2. Newton mantém sempre o novo ponto no intervalo inicial?

- Sim

- Não

Resolução: A atualização por tangente não impõe essa restrição.

### 3. Para f(x)=x² e x₀=2, qual x₁ por Newton?

Resolução: 2−4/4=1.

### 4. Newton para x² perto da raiz zero tem redução de erro:

- Quadrática garantida pelo teorema de raiz simples

- Linear por fator 1/2 neste exemplo

Resolução: A hipótese de raiz simples falha; o padrão aqui é linear.

### 5. Para f(x)=x³−2x+2, começando em zero, qual o primeiro candidato?

Resolução: 0−2/(−2)=1.

### 6. No mesmo ciclo, qual o candidato seguinte a x=1?

Resolução: 1−1/1=0.

### 7. Convergência quadrática perto de raiz simples garante convergência de qualquer início?

- Sim

- Não; a garantia é local

Resolução: Domínio, proximidade inicial e regularidade fazem parte do resultado.

### 8. f′(x_n)=0 e f(x_n)≠0 devem ser tratados como:

- Passo encontrado igual a zero

- Atualização indefinida pelo método padrão

Resolução: É preciso interromper ou usar outra estratégia, sem fabricar um resultado.

### 9. Se uma cota local é |e_{n+1}|≤2|e_n|² e |e_n|=0,1, qual a cota?

Resolução: 2×0,1²=0,02.

## Executar

Salve example.py e rode `python3 example.py`. Só biblioteca padrão, sem leitura interativa ou escrita de arquivos. Contraexemplos são controlados por orçamento; nenhum laço ilimitado é executado.

## Revisão pessoal

Explique a hipótese que sustenta a garantia, faça um passo manual e justifique por que cada contraexemplo não autoriza anunciar sucesso. Os outros temas e a revisão de Computação 3 seguem pendentes.
