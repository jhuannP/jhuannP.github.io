# Oscilador livre: condições iniciais e energia

Rascunho original para revisão de Jhuann, 22/10/2026. Não é resultado de pesquisa ou certificação de domínio.

## Força e equilíbrio

Uma mola ideal exerce F=−kx em relação à posição de equilíbrio. O sinal negativo indica uma força restauradora. Pela segunda lei, mx″=−kx. Aqui x é medido a partir do equilíbrio, em metros; m está em kg e k em N/m. Para uma mola vertical, o peso desloca o equilíbrio: −kx é a força resultante escrita nessa coordenada, não a força elástica isolada com x medido do comprimento natural.

x″+ω²x=0; ω=√(k/m)

## Uma solução com condições iniciais

Com x(0)=A e v(0)=0, a solução é x(t)=A cos(ωt). A velocidade é −Aω sin(ωt). O período é 2π/ω. A forma cosseno com esse início descreve apenas o caso de soltura do repouso.

T=2π√(m/k)

## Conservação da energia

A energia potencial elástica aumenta com x²; a energia cinética aumenta com v². Sem atrito e sem força externa, a soma é constante. O zero da energia potencial é escolhido no equilíbrio. No estado imóvel x=v=0, a energia é zero; esse caso não executa ciclos, embora a equação continue tendo a escala natural ω.

E=½mv²+½kx²=½kA²

## Por que aparecem duas condições iniciais

A equação contém uma segunda derivada. Fixar apenas x(0)=x₀ não diz se a massa está parada ou atravessando aquela posição. As duas soluções cos(ωt) e sen(ωt) são independentes. Escrevendo x=c cos(ωt)+d sen(ωt), obtemos x(0)=c e v(0)=ωd. Logo c=x₀ e d=v₀/ω. Isso permite preparar qualquer posição e velocidade iniciais dentro do modelo.

x(t)=x₀ cos(ωt)+(v₀/ω) sen(ωt)

## Conferir a solução por derivação

Derivar o cosseno produz −ω sen(ωt); derivar o seno produz ω cos(ωt). Portanto v=−ωx₀ sen(ωt)+v₀ cos(ωt). Derivando novamente, a=−ω²x. Substituindo em ma+kx, o resultado é zero porque mω²=k. Em t=0, cosseno vale 1 e seno vale 0: recuperamos separadamente x₀ e v₀. Conferir a equação sem conferir o início não identifica o movimento solicitado.

v(t)=−ωx₀ sen(ωt)+v₀ cos(ωt)

## Amplitude não é a posição inicial

Na forma x=A cos(ωt+φ), expandimos o cosseno da soma. Os coeficientes exigem A cosφ=x₀ e −A senφ=v₀/ω. Elevando ao quadrado e somando, A=√[x₀²+(v₀/ω)²], sempre não negativa. A fase pode ser obtida por atan2(−v₀/ω,x₀), que escolhe o quadrante; fases que diferem por 2π representam o mesmo movimento. Se A=0, a fase é indeterminada e o código retorna None.

A²=x₀²+(v₀/ω)²

## Exemplo: começar já em movimento

Prepare m=2 kg, k=8 N/m, x₀=0,6 m e v₀=1,6 m/s. Então ω=2 rad/s, v₀/ω=0,8 m e A=√(0,36+0,64)=1 m. A posição inicial não é o ponto de retorno. A energia é (1/2)(2)(1,6)²+(1/2)(8)(0,6)²=2,56+1,44=4 J. O período é π s. Em T/4=π/4 s, temos x=0,8 m e v=−1,2 m/s; as energias passam a 2,56 J potencial e 1,44 J cinética.

x(t)=0,6 cos(2t)+0,8 sen(2t)

## A conservação pode ser demonstrada

Derive E=mv²/2+kx²/2 usando v=x′. A regra da cadeia dá dE/dt=mv v′+kx x′=v(ma+kx)=0. A energia total é constante em cada instante, embora suas parcelas mudem. Nos retornos x=±A, v=0. No cruzamento x=0, a força e a aceleração se anulam naquele instante, mas a rapidez é máxima: |v|=ωA. Força nula não significa velocidade nula.

dE/dt=v(ma+kx)=0

## Ler a órbita no espaço de estados

Da conservação segue x²+(v/ω)²=A². No plano com eixos x e v/ω, ambos em metros, a órbita não trivial é um círculo. No plano x por v, com unidades distintas, é uma elipse nas escalas usuais. Não é a trajetória espacial da massa: ela se move em uma linha. O ponto do diagrama reúne posição e velocidade no mesmo instante. O sentido horário na figura resulta de x′=v e v′=−ω²x.

x²+(v/ω)²=A²

## O que o painel desta aula permite mudar

O painel preservado usa x₀=A e v₀=0. Seus controles de massa, constante elástica e amplitude não representam todas as preparações da solução geral. Aumentar a amplitude nesse caso aumenta a energia como A² e não altera o período. Quadruplicar a massa mantendo k duplica o período; quadruplicar k mantendo m o divide por dois. Para investigar v₀≠0, use o exemplo e o laboratório Python desta aula.



## Erro numérico não é uma fonte física

Ao usar Euler explícito, xₙ₊₁=xₙ+h vₙ e vₙ₊₁=vₙ−hω²xₙ. Ao expandir a energia seguinte, os termos cruzados se cancelam e sobra Eₙ₊₁=(1+h²ω²)Eₙ. Para h>0 e movimento não trivial, a energia cresce artificialmente. Isso não contradiz dE/dt=0: o algoritmo discretiza a dinâmica e não preserva esse invariante. O laboratório compara a solução fechada com RK4 independente e refinamento; nem essa comparação nem um gráfico bonito provam conservação exata por qualquer integrador.

Eₙ₊₁=(1+h²ω²)Eₙ

## O alcance desta aproximação

O modelo pressupõe m e k positivos e constantes, força linear, um grau de liberdade e ausência de amortecimento ou excitação após a preparação. Perto de um mínimo não degenerado de um potencial suave, U≈U(eq)+kx²/2 com k=U″(eq)>0 fornece uma aproximação local. Um mínimo com curvatura zero exige análise diferente. A independência do período em relação à amplitude vale aqui; uma mola real fora do regime linear ou um pêndulo de grande amplitude podem fugir dela. Siga para as aulas de pêndulos, amortecimento e forçamento depois de revisar esta base.



## Exercícios e resoluções

- Qual é ω para k=9 N/m e m=1 kg? **Resolução:** ω=√(9/1)=3 rad/s.
- No equilíbrio x=0, a energia potencial elástica é: **Resolução:** U=0.5kx²=0 no equilíbrio; a energia cinética é máxima.
- No exemplo com m=2 kg, k=8 N/m, x₀=0,6 m e v₀=1,6 m/s, qual é ω em rad/s? **Resolução:** √(8/2)=2 rad/s.
- Qual é a amplitude em metros no mesmo exemplo? **Resolução:** √[0,6²+(1,6/2)²]=√1=1 m.
- Qual é o coeficiente do seno, em metros, no mesmo exemplo? **Resolução:** v₀/ω=1,6/2=0,8 m.
- Em t=T/4, qual é x em metros no mesmo exemplo? **Resolução:** cos(π/2)=0 e sen(π/2)=1, logo x=0,8 m.
- Em t=T/4, qual é v em m/s no mesmo exemplo? **Resolução:** v=−2×0,6=−1,2 m/s.
- Qual é a energia total em joules no mesmo exemplo? **Resolução:** K₀=2,56 J e U₀=1,44 J, soma 4 J.
- Qual é a rapidez máxima em m/s no mesmo exemplo? **Resolução:** ωA=2×1=2 m/s.
- Quadruplicando m com k constante, por qual fator o período se multiplica? **Resolução:** T é proporcional a √m; √4=2.
- No estado x₀=v₀=0, a fase é determinada? **Resolução:** A=0: o produto A cos(ωt+φ) é zero para qualquer φ.
- Crescimento de energia no Euler explícito deste sistema demonstra uma força externa real? **Resolução:** O crescimento pertence à discretização; a equação física do modelo conserva energia.

## Fontes e reprodução

Nussenzveig, Curso de Física Básica 2, quinta edição Blucher 2014, §§3.1–3.2, pp.60–66 (PDF61–67), consulta textual parcial do exemplar privado. Feynman I, §21–2: https://www.feynmanlectures.caltech.edu/I_21.html, consulta pública parcial em 22/10/2026. O programa CCM0122 já mapeado tem ativação posterior à turma de 2024; não foi reconsultado neste bloco nem se declara equivalência de versões. Nenhum livro ou figura do livro redistribuído.

Na raiz do site: python3 -m labs.oscilador-livre.experiment e python3 -m unittest discover -s labs/oscilador-livre -t . . O laboratório usa apenas a biblioteca padrão e números finitos int/float, recusando bool. É cálculo em ponto flutuante; resultados podem conter arredondamento. Tempos negativos representam reversibilidade matemática, não recomendação de retroceder uma medição.

A solução fechada verifica o PVI; testes adicionais comparam diferenças centrais, composição temporal e periodicidade. RK4 independente testa refinamento para um PVI de exemplo; não prova convergência universal. Euler explícito é usado para demonstrar o fator artificial de crescimento de energia. O painel existente permanece o caso v₀=0. Não foi acrescentado novo simulador ou alterado o algoritmo RK4 de outra trilha.

Próxima revisão pessoal: obter A e as energias a partir de x₀ e v₀ sem consultar a solução, e explicar por que o diagrama não é a trajetória no espaço físico.

Conferência no navegador: resposta −1,2 m/s aceita com vírgula decimal; diagrama carregado e inspecionado a 390 px, sem transbordamento horizontal. Prévia oscilador-livre-mobile.jpg. Os exemplos de soltura do repouso e início com velocidade foram explicitamente separados. Modelos JS não alterados; suíte global não repetida. Saldo semanal após o bloco: 95%, parada operacional em 65%.
