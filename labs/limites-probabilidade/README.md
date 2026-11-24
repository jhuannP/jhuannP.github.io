# LLN e CLT: média consistente e distribuição do erro

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Derivar média e variância da média amostral no caso iid.
- Provar uma versão da Lei Fraca dos Grandes Números por Chebyshev.
- Distinguir convergência da média de convergência em distribuição do erro padronizado.
- Reconhecer limites da aproximação normal e efeitos de dependência ou seleção.

## Defina o experimento amostral

Considere X₁,…,Xₙ independentes e identicamente distribuídas, com E[Xᵢ]=μ e Var(Xᵢ)=σ² finita. A média amostral é X̄ₙ=(X₁+…+Xₙ)/n. Antes de observar os valores, ela é uma variável aleatória; depois da coleta, uma realização dessa regra é a média calculada. Para o TCL desta aula exigimos ainda σ²>0.

X̄ₙ=(1/n)Σᵢ Xᵢ

## A média da média vem da linearidade

E[X̄ₙ]=(1/n)Σᵢ E[Xᵢ]=μ. Esse cálculo não exige independência se as marginais têm a mesma média e os momentos existem. Isso não diz que uma realização de X̄ₙ seja exatamente μ. Também não corrige uma coleta que seleciona outra população.

E[X̄ₙ]=μ

## A dispersão da média depende da conjunta

Expandir a variância da soma produz n⁻²[Σᵢ Var(Xᵢ)+2Σᵢ<ⱼ Cov(Xᵢ,Xⱼ)]. No caso iid, as covariâncias são zero e as n variâncias iguais, portanto Var(X̄ₙ)=σ²/n. O erro padrão é o desvio padrão da média: σ/√n. Ele não é o desvio padrão de uma observação individual.

Var(X̄ₙ)=σ²/n

## Uma prova da lei fraca por Chebyshev

Para qualquer ε>0, Chebyshev aplicado à média dá P(|X̄ₙ−μ|≥ε)≤Var(X̄ₙ)/ε²=σ²/(nε²). Com ε fixo, a cota tende a zero quando n cresce. Isso prova convergência em probabilidade para μ sob as hipóteses de variância finita usadas aqui. Cotas maiores que 1 podem ser substituídas por 1 e são pouco informativas.

P(|X̄ₙ−μ|≥ε)≤σ²/(nε²)

## O sentido da convergência importa

A lei fraca diz que a probabilidade de um desvio fixo diminui para zero no limite. Não diz que o erro de uma sequência observada diminui monotonamente a cada novo dado. Convergência quase certa é outro sentido; há versões mais amplas da lei dos grandes números, mas esta aula prova apenas a versão fraca com variância finita. Mais observações não garantem erro zero em uma amostra finita.

## O TCL descreve o erro em outra escala

Para iid com variância finita positiva, Zₙ=√n(X̄ₙ−μ)/σ converge em distribuição para N(0,1). A média sem reescalar se concentra em μ; o fator √n mantém visível a distribuição do erro nessa escala. Lei dos Grandes Números e TCL fazem afirmações distintas. Aqui apresentamos o enunciado do TCL e uma ilustração, sem uma prova geral.

Zₙ=√n(X̄ₙ−μ)/σ ⇒ N(0,1)

## Não há um n mágico que garanta boa aproximação

No TCL, o limite é n→∞. A qualidade em n finito depende da distribuição, de assimetria, caudas e da região de probabilidade considerada. Um limiar como n=30 não garante uma aproximação universal. No modelo Bernoulli com p próximo de zero, uma contagem pequena pode continuar concentrada em poucos resultados e muito assimétrica.

## A normal oferece um caso exato distinto

Se os Xᵢ já são normais iid, a média tem distribuição N(μ,σ²/n) para todo n≥1. Isso vem do fechamento da normal sob combinações lineares independentes, não de esperar n grande. No TCL geral, usamos uma aproximação assintótica. Trocar σ por uma estimativa amostral envolve outra regra e outras justificativas.

## A demonstração usa a binomial exata

Para Bernoullis iid de parâmetro p, K=Σᵢ Xᵢ é binomial e X̄ₙ=K/n. Calculamos todas as massas, sem sortear uma trajetória. As barras padronizadas têm área igual à massa e são comparadas com a densidade normal padrão. Zₙ continua discreto em n finito. A comparação visual não constitui prova do TCL.

## Dados repetidos fornecem um contraexemplo de dependência

Se X₁=…=Xₙ=Y para uma mesma Bernoulli de parâmetro 1/2, a média é Y e sua variância é 1/4 para todo n. Não fica 1/(4n). Para ε=0,2, a probabilidade de desvio em relação a 1/2 é 1 para qualquer n. Acrescentar cópias não fornece informação independente, embora as marginais sejam iguais.

Var(X̄ₙ)=1/4 no modelo de cópias

## Seleção e momentos podem invalidar a aplicação

Uma coleta que muda a média da população-alvo pode convergir para uma média diferente: estabilidade não elimina viés de seleção. Distribuições sem os momentos usados também ficam fora dos enunciados desta aula. Em séries dependentes, a variância da média precisa considerar covariâncias; não substitua a análise por σ/√n automaticamente.

## O que levar para pesquisa e ensino

Declare a variável, a população, o desenho de coleta, os momentos e a hipótese de dependência antes de citar uma lei de limite. O erro padrão quantifica uma dispersão do procedimento, não todo erro sistemático. O laboratório compara modelos sintéticos e não estabelece incerteza dos resultados da IC. A interpretação e o desenho das aplicações reais precisam de revisão própria.

## Exemplo resolvido

Bernoullis iid com p=1/2: o que muda de n=16 para n=64?

1. Cada observação tem média 1/2 e variância 1/4.
2. Com n=16, Var(média)=1/64 e erro padrão 1/8.
3. Com n=64, Var(média)=1/256 e erro padrão 1/16.
4. Quadruplicar n divide a variância por 4 e o erro padrão por 2.
5. A distribuição da média continua discreta para n finito; a curva normal é referência aproximada.
6. Se todos os dados fossem cópias da mesma Bernoulli, Var(média) seria 1/4 nos dois tamanhos.

## Exercícios e resoluções

### Com σ=4 e n=16 iid, qual o erro padrão da média?

4/4=1.

### σ/√n é automaticamente correto para toda série autocorrelacionada?

Sim
Não

A dependência altera a variância da média.

### Bernoullis iid com p=1/2 e n=25: qual a variância da média?

p(1−p)/n=(1/4)/25=0,01.

### Com σ=4 e n=64 iid, qual o erro padrão?

4/√64=4/8=0,5.

### Com σ²=1/4, n=100 e ε=0,1, qual a cota σ²/(nε²)?

(1/4)/(100×0,01)=1/4.

### Se todos os dados repetem a mesma Bernoulli de p=1/2, qual Var(média), mesmo com n=100?

A média é a própria Bernoulli; sua variância é 1/4.

### A lei fraca promete que o erro observado diminui a cada nova observação?

Sim
Não

A convergência em probabilidade não exige monotonicidade de uma realização.

### n=30 garante a mesma qualidade de aproximação normal para qualquer distribuição?

Sim
Não

A aproximação depende da distribuição e da região considerada, além de n.

### Para observações normais iid, a média é normal:

Somente quando n é grande
Para todo n≥1

O fechamento por combinações lineares independentes fornece o resultado exato.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Apenas biblioteca padrão; distribuição binomial racional e referência normal por erfc. Não lê dados privados nem escreve resultados externos. O caso iid e o caso de cópias são modelos distintos.

## Proposta didática

Peça uma previsão antes de mudar n ou σ; separe distribuição do dado da distribuição da média; contraste exatidão com aproximação; termine com uma hipótese que impede aplicar a fórmula. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Versão da lei fraca provada aqui usa iid e variância finita.
- TCL apresentado usa iid e variância finita positiva.
- A aproximação normal em n finito não tem qualidade universal garantida.
- Distribuições sintéticas, sem inferência ou decisão científica sobre dados da IC.
