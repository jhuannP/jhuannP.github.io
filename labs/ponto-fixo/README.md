# Ponto fixo: uma equação pode ter várias iterações

Aprofundamento original de 13/10/2026 com apoio de IA para revisão de Jhuann. Referência temática Burden, Faires e Burden, 10ª edição; exemplos próprios, sem transcrição.

## Resolver uma equação não escolhe um algoritmo único

Uma solução desejada pode satisfazer x=g(x). A iteração escolhe x₀ e aplica x_{n+1}=g(x_n). Diferentes g podem ter o mesmo ponto fixo e comportamentos distintos. Para solução 2, g₁(x)=x/2+1 aproxima de modo estável, enquanto g₂(x)=2x−2 afasta a maioria das entradas. Além da equivalência algébrica, declare o domínio em que as expressões estão definidas; uma reformulação pode introduzir restrições.

`x*=g(x*); x_{n+1}=g(x_n)`

## Duas hipóteses da garantia

Se g leva um intervalo fechado [a,b] nele mesmo e é uma contração nele, com |g(x)−g(y)|≤q|x−y| e 0≤q<1, há um único ponto fixo nesse intervalo e as iterações de qualquer x₀ nele convergem a esse ponto. A autoaplicação mantém a sequência no domínio. Uma condição suficiente para a contração é continuidade no fechado, diferenciabilidade no aberto e |g′|≤q<1; o Valor Médio dá a desigualdade. Conferir a derivada em poucos pontos não prova a cota no intervalo.

`g([a,b])⊆[a,b]; |g(x)−g(y)|≤q|x−y|`

## Por que as diferenças formam uma sequência controlada

A contração implica |x_{n+1}−x_n|≤q|x_n−x_{n−1}|. Repetindo, a diferença do passo n para n+1 é no máximo q^n|x₁−x₀|. Para comparar x_n com um termo posterior, some as diferenças intermediárias; a soma geométrica tem cauda que tende a zero. A sequência é de Cauchy, converge num intervalo fechado e, pela continuidade de g, seu limite r satisfaz r=g(r).

`|x_{n+1}−x_n|≤q^n|x₁−x₀|`

## Uniquidade e uma cota a posteriori

Se r e s fossem pontos fixos distintos, |r−s|=|g(r)−g(s)|≤q|r−s|, impossível com q<1. Para limitar o erro de x_n usando o último passo, some as diferenças futuras: |x_n−r|≤q|x_n−x_{n−1}|/(1−q), para n≥1. Essa cota exige um q válido e domínio invariável; observar só uma diferença pequena não fornece o mesmo certificado. Quanto mais q se aproxima de 1, maior pode ser o fator de amplificação do último passo.

`|x_n−r|≤q|x_n−x_{n−1}|/(1−q)`

## Exemplo linear com garantia completa

Para g(x)=x/2+1 em [0,2], a imagem está em [1,2] e |g′|=1/2. O ponto fixo é 2. De x₀=0, obtemos 1; 1,5; 1,75; 1,875; …, sempre dentro do intervalo. Em x₃=1,75, o último passo vale 0,25; q/(1−q)=1, então a cota é 0,25, igual ao erro exato nesse exemplo. A linearidade torna a razão de erros exatamente 1/2.

`x₃=1,75; erro e cota=0,25`

## Oscilar pode ser convergir

Para g(x)=−x/2+3, o ponto fixo também é 2. De zero, a sequência 3; 1,5; 2,25; 1,875; … alterna ao redor de 2 e o módulo do erro cai pela metade. O sinal da derivada controla a alternância, enquanto seu módulo fornece o fator de contração. Na demonstração, o controle q é um coeficiente assinado da família linear; a constante de contração correspondente é |q|, quando menor que 1. No intervalo [0,4], g leva os valores a [1,3], mantendo o domínio com constante de contração 1/2.

`coeficiente negativo pode alternar; |coeficiente|<1 controla o erro`

## Sem as hipóteses, analisar o caso

Para g(x)=2x−2, partindo de 1, a sequência é 1,0,−2,−6,… e se afasta de 2. Partindo exatamente de 2, permanece em 2: uma iteração desfavorável não faz toda entrada divergir. Para g(x)=x, todo ponto é fixo e não há unicidade; q=1 não é contração estrita. A ausência das hipóteses impede usar o teorema, mas não decide automaticamente cada sequência.

`não contração ≠ todas as entradas necessariamente divergem`

## Um passo minúsculo com erro grande

Escolha g(x)=s x+2(1−s), com s=1−10⁻¹², e comece em zero. O primeiro passo é cerca de 2×10⁻¹², mas o ponto fixo está em 2. O critério padrão do código pode aceitar esse passo sem estar perto de 2. A função é uma contração, porém q/(1−q) é enorme: a cota a posteriori não é pequena. Isso distingue convergência eventual do método e precisão garantida pelo critério de término escolhido.

`passo pequeno pode ser amplificado por q/(1−q)`

## Critério de código, orçamento e representação

A função de apoio para quando |novo−x|≤tol(1+|novo|). Essa é uma regra de passo com escala; não calcula automaticamente o erro verdadeiro. Se o orçamento termina antes, sinaliza RuntimeError; avaliações não finitas são rejeitadas. Na precisão finita pode ocorrer estagnação por arredondamento. Declare se a aproximação retornada por essa regra será tratada apenas como candidato ou se há uma cota adicional para qualificá-la.

`passo aceito ≠ erro certificado sem hipóteses adicionais`

## Roteiro para usar e ensinar

Verifique equivalência e domínio; escolha intervalo e início; justifique autoaplicação e uma constante de contração. Trace passos, compare diferenças e aplique a cota somente quando suas hipóteses estiverem disponíveis. Teste uma sequência oscilante, uma divergente e um critério enganoso. Para uma aplicação científica, reporte condição inicial, orçamento, motivo de término e qual erro foi efetivamente controlado.

`equação → g → domínio → início → garantia → parada`

## Exercícios e resoluções

Tente antes de consultar; declare domínio, condições e critério de parada.

### 1. Qual é o terceiro valor depois de x0=0: x1=1, x2=1.5, x3=?

Resolução: 1.5/2+1=1.75.

### 2. A condição |g′|<1 em apenas um ponto basta para garantir convergência em todo intervalo?

- Sim

- Não

Resolução: A hipótese deve valer no domínio usado e a iteração deve permanecer nele.

### 3. Para g(x)=x/2+1 e x₀=0, qual x₄?

Resolução: 1,75/2+1=1,875.

### 4. Com q=0,5 e último passo 0,1, qual cota q·passo/(1−q)?

Resolução: 0,5×0,1/0,5=0,1.

### 5. Para g(x)=−x/2+3, partindo de x₀=0, qual x₁?

Resolução: −0/2+3=3.

### 6. Oscilar ao redor do ponto fixo significa sempre divergência?

- Sim

- Não; o módulo do erro pode diminuir

Resolução: A sequência pode alternar e convergir.

### 7. A autoaplicação do intervalo é dispensável na garantia apresentada?

- Sim

- Não

Resolução: g([a,b])⊆[a,b] faz parte da garantia usada.

### 8. g(x)=x tem um único ponto fixo?

- Sim

- Não; todos os pontos são fixos

Resolução: q=1 não é contração estrita e não há unicidade.

### 9. Com q=0,99 e último passo 0,001, qual a cota q·passo/(1−q)?

Resolução: 0,99×0,001/0,01=0,099.

## Executar

Salve example.py e rode `python3 example.py`. Só biblioteca padrão, sem leitura interativa ou escrita de arquivos. Contraexemplos são controlados por orçamento; nenhum laço ilimitado é executado.

## Revisão pessoal

Explique a hipótese que sustenta a garantia, faça um passo manual e justifique por que cada contraexemplo não autoriza anunciar sucesso. Os outros temas e a revisão de Computação 3 seguem pendentes.
