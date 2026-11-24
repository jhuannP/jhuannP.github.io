# Microestados, macroestados e pesos

22/10/2026. Notas de aula originais com apoio de IA, em rascunho para revisão de Jhuann.

## O que sabemos sobre cada sítio?

Imagine N posições identificadas, cada uma com um estado 0 ou 1. Um microestado é a lista completa desses valores. Para N=4, 1001 e 0110 são configurações diferentes: os rótulos das posições têm significado. Aqui não estamos distribuindo partículas quânticas indistinguíveis entre orbitais; estamos descrevendo sítios distinguíveis. Se o estado 1 tem energia ε acima de 0 e desprezamos interações, a energia de uma configuração é ε vezes seu número de uns.

s=(s₁,…,sₙ), sᵢ∈{0,1}; E=εm

## Contar todas as configurações

Em cada posição há duas escolhas. Para a primeira e a segunda, são 2×2 pares; acrescentar outra posição duplica o total. Repetir o argumento N vezes dá 2 elevado a N. Isso é uma contagem de possibilidades, não uma hipótese sobre suas chances. Para N=0 há uma lista vazia, não zero listas: a convenção 2⁰=1 mantém as identidades de contagem. O laboratório inclui esse caso de borda.

Número total=2ᴺ

## O macroestado esquece quais posições estão excitadas

Defina M(s)=s₁+⋯+sₙ. Quando observamos apenas m, esquecemos a posição dos uns. Para N=4 e m=2, o grupo contém 1100, 1010, 1001, 0110, 0101 e 0011. São seis microestados para um único valor de M. O mesmo conjunto de configurações pode ser agrupado por outras grandezas; a descrição macroscópica utilizada precisa ser declarada.

M(s)=m

## Por que aparece o coeficiente binomial?

Para marcar m posições distintas, uma escolha ordenada tem N(N−1)⋯(N−m+1) possibilidades. Mas trocar a ordem das mesmas m posições não cria uma nova configuração. Cada subconjunto foi contado m! vezes; dividir corrige a repetição. Logo Ω(N,m)=N!/[m!(N−m)!]. Nas extremidades m=0 ou m=N há apenas uma configuração. Valores fora de 0,…,N não são macroestados possíveis neste modelo.

Ω(N,m)=N!/[m!(N−m)!]

## Uma partição confere a contagem

Cada configuração tem exatamente um número de excitações. Portanto os grupos m=0,…,N são disjuntos e cobrem o conjunto inteiro. Para N=4, as multiplicidades são 1, 4, 6, 4 e 1: sua soma é 16. A simetria Ω(N,m)=Ω(N,N−m) também tem uma prova concreta: troque cada 0 por 1 e cada 1 por 0; essa operação é reversível e emparelha os dois grupos.

Σₘ Ω(N,m)=2ᴺ

## Para obter probabilidades, declare a distribuição

Suponha agora, como escolha de distribuição, que todas as 2ᴺ configurações tenham a mesma probabilidade. A chance de um grupo é a soma das chances de seus integrantes: Ω(N,m)/2ᴺ. Os N+1 valores de m não ficam equiprováveis. Em N=4, o grupo m=2 tem chance 6/16=3/8, enquanto m=0 tem 1/16. Uma configuração particular, como 1100, continua tendo apenas 1/16.

P(M=m)=Ω(N,m)/2ᴺ

## Exemplo resolvido: um pico não contém tudo

Para N=8 existem 256 configurações. As multiplicidades são 1, 8, 28, 56, 70, 56, 28, 8 e 1. O maior grupo é m=4, com probabilidade 70/256=35/128, menor que 1/2. Já o evento 3≤M≤5 reúne três grupos e tem probabilidade (56+70+56)/256=91/128, maior que 1/2. Ser o valor mais provável não significa concentrar a maioria dos resultados. Uma faixa e um valor exato são eventos diferentes.

P(M=4)=35/128

## Os pesos podem mudar sem alterar as multiplicidades

Outra distribuição possível atribui a cada sítio, de forma independente, probabilidade p de estar em 1. Uma configuração com m uns recebe peso pᵐ(1−p)ᴺ⁻ᵐ. Há Ω(N,m) configurações desse tipo; somar seus pesos produz a distribuição binomial. A independência e o mesmo p para todos os sítios são hipóteses desta distribuição, não consequências da ausência de interação na fórmula da energia.

P(M=m)=Ω(N,m)pᵐ(1−p)ᴺ⁻ᵐ

## Mesma contagem, outra resposta

Com N=4 e p=1/4, as seis configurações com m=2 continuam existindo. Cada uma recebe peso (1/4)²(3/4)²=9/256; o grupo pesa 54/256=27/128, diferente dos 3/8 do caso uniforme. Dentro desse grupo os seis pesos são iguais, mas configurações de grupos diferentes já não têm necessariamente a mesma chance. Não atribuímos aqui temperatura ao parâmetro p; uma interpretação térmica requer outro desenvolvimento.

P(M=2)=6×9/256=27/128

## Média, flutuação e grandeza física

Como M é a soma dos indicadores sᵢ, a linearidade da esperança dá E[M]=Np. Com independência, as covariâncias entre sítios distintos são zero; somar as variâncias p(1−p) dá Var(M)=Np(1−p). Em N=8,p=1/2, a média é 4 e a variância é 2. M é uma contagem adimensional. Se E=εM, sua média é εNp e sua variância é ε²Np(1−p), com unidades de energia ao quadrado. Nenhum resultado fornece, por si só, uma trajetória temporal.

E[M]=Np; Var(M)=Np(1−p)

## Fixar energia muda o conjunto acessível

Se ε>0 é fixo e impomos E=εm₀, apenas o grupo M=m₀ permanece acessível. Uma distribuição microcanônica uniforme nesse grupo atribui 1/Ω(N,m₀) a cada configuração permitida, e probabilidade 1 ao macroevento M=m₀. O denominador 2ᴺ pertence à distribuição uniforme sem essa restrição. A aula seguinte, “Microcanônico: declarar o conjunto acessível de energia”, desenvolve o caso de um todo fixo com subsistemas que flutuam.

P(M=m₀ | M=m₀)=1

## O que o laboratório verifica e o que fica pendente

O código compara duas construções independentes: uma fórmula combinatória e a enumeração de listas binárias com produto dos pesos locais. Usa frações exatas, verifica a normalização e calcula momentos a partir da distribuição. A enumeração é limitada a N≤16 para conter o custo exponencial. Os extremos p=0 e p=1 são distribuições determinísticas válidas. Esses testes verificam um modelo finito; não demonstram ergodicidade, equilíbrio experimental, comportamento quântico indistinguível ou o limite termodinâmico. A trilha é complementar e permanece em rascunho para revisão pessoal.

## Exercícios e resoluções

- Qual multiplicidade do exemplo? **Resolução:** C(4,2)=6.
- Quantas configurações binárias existem para N=4? **Resolução:** 2^4=16.
- No modelo de N=4 sítios identificados, quantas configurações pertencem ao grupo m=1? **Resolução:** Escolha a posição do único 1: quatro possibilidades.
- Quanto somam as multiplicidades 1,4,6,4,1 de N=4? **Resolução:** 1+4+6+4+1=16=2⁴.
- Sob distribuição uniforme em todas as configurações de N=4, qual a probabilidade da configuração específica 1100? **Resolução:** Uma entre 16 configurações: 1/16.
- Na mesma distribuição uniforme com N=4, quanto é P(M=2)? **Resolução:** Seis configurações favoráveis entre 16: 6/16=3/8.
- Para N=8 uniforme, qual a probabilidade do grupo M=4? **Resolução:** C(8,4)/256=70/256=35/128.
- Para N=8 uniforme, quanto é P(3≤M≤5)? **Resolução:** (56+70+56)/256=182/256=91/128.
- Para quatro sítios independentes com p=1/4, quanto é P(M=2)? **Resolução:** 6(1/4)²(3/4)²=54/256=27/128.
- Para N=8,p=1/2 independentes, quanto é E[M]? **Resolução:** Np=8/2=4.
- Para N=8,p=1/2 independentes, quanto é Var(M)? **Resolução:** Np(1−p)=8(1/2)(1/2)=2.
- Fixando M=2 e usando distribuição uniforme apenas nas seis configurações permitidas de N=4, qual a chance da configuração 1100? **Resolução:** Agora o conjunto acessível tem seis configurações; cada uma tem chance 1/6.

## Fonte e reprodução

[David Tong, Statistical Physics, §1.2 e início do §1.2.3](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), consulta parcial em 22/10/2026: definição do conjunto acessível e contagem do sistema de dois estados. Não foram transcritos exercícios, figuras ou parágrafos. Os casos N=4 e N=8, comparação de distribuições, contas e código foram construídos localmente. Temperatura, aproximação de Stirling e limite termodinâmico não são desenvolvidos nesta aula.

## Executar

Na raiz do site: python3 -m labs.micro-macro-binario.experiment e python3 -m unittest discover -s labs/micro-macro-binario -t .

As funções de distribuição validam N e p; moments recebe uma distribuição normalizada válida, como as geradas por elas. Enumeração exata limitada a N≤16; não há simulação temporal nem ajuste a dados reais.


## Microestados, macroestados e pesos — 22/10/2026

Aula micro-macroestados ampliada de três seções/dois exercícios para 12 seções/12 exercícios. Os dois exercícios antigos, exemplo resolvido, desafio e painel existente foram preservados. Definição de configuração, agrupamento por número de excitações, coeficiente binomial e soma das multiplicidades; distinção entre contagem e probabilidades, distribuição uniforme irrestrita, Bernoulli independente e restrição de energia. Média e variância derivadas pelos indicadores. Nenhuma temperatura, preparação experimental, termalização ou ergodicidade foi inferida.

Exemplos originais: N=4 tem 16 configurações e seis no grupo m=2; uma configuração pesa 1/16, o grupo 3/8. Após restringir ao grupo e assumir uniformidade nele, uma configuração permitida pesa 1/6. Em N=8 uniforme, o pico m=4 pesa 35/128, mas a faixa de três a cinco pesa 91/128. Para N=4 e p=1/4 independente, P(M=2)=27/128, com a mesma multiplicidade seis. A contagem não foi convertida automaticamente em distribuição física.

Fonte primária: [David Tong, Statistical Physics](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), §1.2 e início do §1.2.3, consulta parcial em 22/10/2026. Sistema de dois estados e multiplicidade conferidos; exemplos, figura, enumeração e exercícios próprios. Notas com referências e resoluções em labs/micro-macro-binario/README.md. Não se afirma leitura integral da fonte nem estudo pessoal concluído.

Verificação: cinco testes novos aprovados, comparando fórmula com enumeração independente para N de zero a nove e cinco pesos racionais; normalização, momentos, reflexão, extremos, contratos e valores da aula. Doze testes de catálogo e 531 estruturas MathML aprovados. Navegador: 1/16 aceito para uma configuração irrestrita; na pergunta restrita, 1/16 rejeitado e 1/6 aceito. Figura e texto conferidos a 390 px, largura da página igual à tela e nenhum erro de console observado. Prévia micro-macro-binario-mobile.jpg. Modelos JavaScript preservados; suíte global não repetida.

Catálogo: 500 aulas/2972 exercícios em rascunho. Mecânica estatística permanece uma trilha própria com dois recortes desenvolvidos e 23 introduções; sem equivalência automática com disciplina cursada ou certificação pessoal. Próxima revisão: explicar as três chances 1/16, 3/8 e 1/6 antes de seguir ao microcanônico. Próxima preparação global: aprofundar assunto de Computação II ou Física Matemática, conferindo fonte e pré-requisitos. Saldo semanal após o bloco: 94%; parada operacional em 65%.
