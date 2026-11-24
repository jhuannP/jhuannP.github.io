# Poisson iterativo — erro algébrico e discretização

16/10/2026. Rascunho para revisão de Jhuann.

## Fixe a equação, o sinal e a fronteira

No quadrado [0,1]², considere −Δu=g e u=0 na borda, com variáveis adimensionais. Escolhemos u(x,y)=sin(πx)sin(πy); derivar duas vezes em cada direção dá g=2π²u. A solução conhecida é uma referência fabricada para verificar o código, não resultado de medição.

## O stencil define outro problema, agora finito

Divida cada direção em n subintervalos, h=1/n. Há (n−1)² incógnitas interiores. A equação em cada nó é (4u_ij−u_(i−1,j)−u_(i+1,j)−u_(i,j−1)−u_(i,j+1))/h²=g_ij. A malha aproxima as derivadas; resolver esse sistema não equivale a resolver exatamente a EDP contínua. Na fórmula compacta, a soma em v percorre somente os quatro vizinhos desse nó.

## Jacobi usa apenas a varredura anterior

Isolar u_ij fornece a média dos quatro vizinhos mais h²g_ij/4. Em Jacobi, todos os vizinhos vêm do estado anterior: a nova malha precisa ser separada. Sobrescrever os valores enquanto ainda são usados muda o algoritmo.

## Gauss–Seidel reutiliza valores na ordem escolhida

Neste laboratório, percorremos i de 1 a n−1 e, dentro dele, j de 1 a n−1. A atualização usa imediatamente os valores já recalculados; os demais ainda são antigos. As bordas permanecem zero. Uma varredura é uma iteração do sistema linear, não evolução física no tempo.

## O resíduo deve usar a mesma escala da equação

Medimos ||r||∞ com r=g−A_hu, usando o operador com divisão por h². O resíduo do stencil sem essa divisão é h²r: comparar esses dois números como se fossem iguais confunde escalas. O resíduo informa satisfação do sistema discreto; não é diretamente o erro da solução contínua.

## Uma referência discreta permite separar os erros

Para o modo sin(πi/n)sin(πj/n), a identidade sen(t+α)+sen(t−α)=2sen(t)cosα mostra que A_h multiplica o modo por λ_h=8n²sin²(π/(2n)). Assim a solução exata do sistema discreto é u_h=C_h u nos nós, com C_h=2π²/λ_h. Essa referência é própria deste modo e desta malha.

## Erro algébrico e erro de malha têm destinos distintos

Defina E_alg=||u^(k)−u_h||∞ e E_malha=||u_h−u||∞ nos nós. O erro total é ||u^(k)−u||∞≤E_alg+E_malha, pela desigualdade triangular. Mais varreduras podem reduzir E_alg, mas não alteram u_h na mesma malha. O erro total pode ter cancelamento temporário e não precisa diminuir monotonamente.

## Refinar a malha muda a referência discreta

Como sin z=z−z³/6+O(z⁵), C_h=(z/sin z)²=1+z²/3+O(z⁴), z=π/(2n). Para n par, o nó central tem u=1, portanto E_malha=C_h−1=π²/(12n²)+O(n⁻⁴). Dobrar n reduz aproximadamente por quatro esse erro, após controlar o erro algébrico.

## O modo também verifica a iteração de Jacobi

A média dos vizinhos de um modo senoidal multiplica sua amplitude por ρ=cos(π/n). Partindo de zero, u^(k)=(1−ρ^k)u_h. Logo E_alg=C_hρ^k e ||r||∞=2π²ρ^k para n par. Quando n cresce, ρ se aproxima de 1: o mesmo número de varreduras pode resolver pior o sistema de uma malha mais fina.

## Um orçamento fixo é uma comparação, não critério de sucesso

A interface executa o número de varreduras escolhido e informa o resíduo; não declara convergência só porque o orçamento terminou. A comparação Jacobi/GS usa a mesma malha, fonte e início zero. Número de varreduras não mede sozinho tempo de execução, custo paralelo ou precisão final.

## O exemplo anterior continua útil, mas testa outra coisa

O teste quadrático u=x(1−x)y(1−y), usado na aula introdutória de Poisson, tem diferença central exata em cada variável. Ele ajuda a conferir montagem e sinal, mas pode esconder erro de truncamento. O modo senoidal deste laboratório torna a separação de erros observável.

## A figura é uma seção da solução bidimensional

Mostramos y=1/2: aproximação iterada, referência contínua e referência discreta nos mesmos nós. Os erros e o resíduo são máximos sobre toda a malha interior, não apenas essa seção. O Python também compara a referência discreta com solução densa em malha pequena. Outros domínios, fontes e condições de contorno exigem novas verificações.

## Resoluções

Para n=8 subintervalos por direção, quantas incógnitas interiores há?

(n−1)²=7²=49.

Para n=8, qual h? Aceita fração.

h=1/n=1/8.

Qual o fator do resíduo sem divisão por h² em relação a r=g−A_hu, para n=8?

O stencil sem escala tem resíduo h²r=r/64.

Em ordem dominante, por qual fator divide-se E_malha ao dobrar n?

O termo dominante é proporcional a n⁻².

Antes de qualquer varredura, com início zero, qual erro total máximo nodal para n par?

O modo contínuo atinge 1 no nó central.

Jacobi deve usar valores recém-atualizados na mesma varredura?

Jacobi usa o estado anterior; reutilização imediata caracteriza o GS desta rotina.

Mais varreduras na mesma malha eliminam necessariamente o erro de discretização?

Elas resolvem melhor o sistema discreto, sem mudar a discretização.

O número de varreduras é tempo físico da EDP de Poisson?

É uma iteração do solver de um problema estacionário.

O erro total deve diminuir monotonamente se o erro algébrico diminui?

Erros algébrico e de malha podem se cancelar temporariamente.

## Fontes e roteiro

Escopo: CCM0226, programa indexado consultado em 16/10. Apoio sobre Poisson discreto e iteração: [James Demmel, Berkeley CS267](https://people.eecs.berkeley.edu/~demmel/cs267/lecture24/lecture24.html), consultado diretamente em 16/10/2026. A fonte usa outra convenção de contagem dos pontos: aqui n é número de subintervalos, h=1/n. O sinal também foi fixado como −Δ. Modo fabricado, comparação de erros, exercícios e código são próprios.

Pré-requisitos: derivadas parciais, sistemas lineares, normas, diferenças e seno. Roteiro: derivar fonte; montar stencil; executar uma varredura manual; comparar Jacobi/GS; conferir resíduo; separar erros com referência discreta; refinar malha após reduzir erro algébrico. Produto: tabela de resíduo/erros com malha, método e orçamento explícitos. Sem dados experimentais ou resultados da IC.

Pendentes: domínios/fontes/contornos gerais, parada por tolerância e estimadores sem solução conhecida, métodos acelerados, estruturas esparsas e custo real. GS não é declarado universalmente mais rápido; o teste apenas compara esta implementação e este problema.

## Conferência numérica do exemplo

Para n=8 e vinte varreduras Jacobi, C_h≈1,01295075 e E_malha≈0,01295075; E_alg≈0,20791951, E_total≈0,19496877 e ||r||∞≈4,05169420. Valores computacionais para conferência, sem incerteza experimental associada.
