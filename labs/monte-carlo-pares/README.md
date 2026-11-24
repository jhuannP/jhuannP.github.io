# Monte Carlo e pares antitéticos — notas de aula

Rascunho original para revisão de Jhuann.

## A média amostral estima a esperança

Para valores independentes com mesma distribuição e variância finita, a média tem variância σ²/n. Aqui estimamos ∫_0^1 x² dx gerando X uniforme e observando X². A referência 1/3 é conhecida.

Î=(1/n)Σ X_i²

## Dispersão dos dados não é incerteza da média

O desvio amostral mede variação entre observações. O erro padrão estimado da média é s/√n. A divisão depende de independência; autocorrelação pode tornar essa fórmula inadequada.

SE≈s/√n

## Ganhar uma casa custa amostras

Para reduzir o erro padrão por dois, multiplique n por quatro, mantendo o mesmo modelo. A semente permite repetir a sequência, mas uma realização pode contrariar a expectativa de melhora do erro absoluto. Compare também várias réplicas.

SE escala como n^(−1/2)

## Derivar a variância do exemplo básico

Para U uniforme em [0,1], E(U²)=1/3 e E(U⁴)=1/5, pela integração de potências. Logo Var(U²)=1/5−1/9=4/45. A média de N avaliações independentes tem variância 4/(45N), porque a variância da soma é a soma das variâncias quando as covariâncias são zero. O erro padrão teórico é a raiz dessa variância, não o erro absoluto de uma execução.

Var(Î_ind)=4/(45N)

## Construir um par sem mudar a esperança

Se U é uniforme em [0,1], 1−U tem a mesma distribuição. Assim Y=[f(U)+f(1−U)]/2 tem a mesma esperança de f(U). Para M uniformes independentes, use a média de M valores Y. Há dependência dentro de um par, mas independência entre pares no modelo. A validade da média não exige que os dois membros do par sejam independentes.

Î_anti=(1/M)ΣYᵢ; Yᵢ=[f(Uᵢ)+f(1−Uᵢ)]/2

## A comparação precisa contar avaliações

Cada Y exige duas avaliações de f; portanto M pares têm custo N=2M nesse orçamento. Compare com N avaliações independentes, e não com M. Aqui o custo ignora geração aleatória, reutilização de cálculos, memória e tempo de máquina; ganho estatístico não é automaticamente ganho de desempenho real.

N=2M

## A covariância decide se o par ajuda

Escreva σ²=Var(f(U)) e c=Cov(f(U),f(1−U)). Como os dois termos têm a mesma variância, Var(Y)=(2σ²+2c)/4=(σ²+c)/2. A média de M pares tem variância (σ²+c)/(2M)=(σ²+c)/N. O estimador independente tem σ²/N. Se c<0 há redução; se c>0 há aumento, a custo de avaliações fixo.

Var(Î_anti)=(σ²+c)/N

## Derivar o ganho para f(u)=u²

O par é Y=[u²+(1−u)²]/2=u²−u+1/2. Integre Y e Y² no intervalo unitário: E(Y)=1/3, E(Y²)=7/60, de modo que Var(Y)=7/60−1/9=1/180. Também E[U²(1−U)²]=1/30, e a covariância é 1/30−1/9=−7/90. Com N=2M, a variância antitética é 1/(90N); dividir 4/(45N) por esse valor dá 8. A razão de erros padrão é √8, não 8.

Var(Î_ind)/Var(Î_anti)=8

## Um contraexemplo com a mesma transformação

Agora f(u)=(u−1/2)² é simétrica: f(1−u)=f(u). Cada par repete a mesma saída, não traz cancelamento. A média verdadeira é 1/12 e a variância de f(U) é 1/180. Com M pares, a variância é 1/(180M)=1/(90N), enquanto N avaliações independentes dão 1/(180N). O antitético dobra a variância a custo fixo. A técnica não recebe uma garantia universal pelo nome.

Razão de variâncias independente/antitético=1/2

## O caso linear mostra cancelamento exato

Para f(u)=u, Y=[u+(1−u)]/2=1/2 para todo u. A integral vale 1/2 e o estimador antitético tem variância zero nesse modelo ideal. O painel informa isso sem calcular divisão por zero na razão de ganhos. Esse cancelamento não garante que um problema não linear tenha erro nulo.



## O erro padrão estimado usa os pares

Numa execução, calcule a variância amostral dos M valores Y e use s_Y/√M. Não trate os 2M resultados de f como observações independentes. O laboratório imprime estimativa e SE para cada método, com semente fixa, mantendo a fórmula teórica separada. A semente facilita reproduzir a sequência pseudorrandômica; não prova qualidade do gerador ou validade das hipóteses.

SE_anti estimado=s_Y/√M

## Como ler as curvas de custo

O painel traça erros padrão teóricos contra log₂ N, comparando o mesmo N de avaliações. As três funções são exemplos sintéticos; os pontos só marcam o orçamento selecionado. A linha azul não é uma realização aleatória nem uma cota do erro observado. No caso linear, o traço azul fica em zero. Para o caso simétrico, fica acima do tracejado independente.



## Amostra favorável não valida o método

Uma execução pode dar erro absoluto menor no método de maior variância. Para estudar desempenho empírico, use muitas repetições independentes, referência conhecida, orçamento comparável e registros do gerador. Isso não transforma a raiz do erro quadrático médio em limite absoluto. Para estimadores sem viés deste recorte, o erro quadrático médio coincide com a variância; em outros problemas, o viés também importa.



## Conexão com simulação científica e limites

Pares refletidos podem ser uma hipótese de redução de variância em um cálculo científico, mas é preciso preservar a distribuição marginal e medir custo/precisão na aplicação. Este exemplo não implementa Monte Carlo de cadeias de Markov, importância, eventos raros ou uma pesquisa pessoal. O conteúdo é um complemento didático de Computação IV e não reconstrói a turma a partir do programa padrão.



## Exercícios e resoluções

### Qual erro padrão do exemplo?

2/sqrt(100)=0.2.

### Por qual fator multiplicar n para reduzir SE pela metade?

SE depende de 1/sqrt(n).

### Para f(U)=U², qual é Var(f(U))?

E(U⁴)−E(U²)²=1/5−1/9=4/45.

### Com M=16 pares, quantas avaliações de f compõem o orçamento?

Cada par usa duas avaliações: N=2M=32.

### Para f(U)=U², qual é Var(Y) de um par?

Y=u²−u+1/2 tem variância 7/60−1/9=1/180.

### Para f(U)=U², qual é a razão de variâncias independente/antitético a mesmo custo?

(4/(45N))/(1/(90N))=8.

### No caso simétrico f(U)=(U−1/2)², qual é a razão de variâncias independente/antitético?

A dependência positiva dobra a variância antitética: razão 1/2.

### No caso linear f(U)=U, qual é a variância do estimador antitético?

Cada média de par é exatamente 1/2 no modelo.

### Os dois valores dentro de um par antitético são independentes?

Dependem do mesmo U; a independência vale entre pares distintos no modelo.

### Oito vezes menos variância significa oito vezes menos erro padrão?

O erro padrão é a raiz da variância: o fator é √8.

### Uma execução com menor erro absoluto prova maior eficiência estatística?

A comparação de variâncias se refere à distribuição entre repetições, além de exigir custo comparável.

### Para o SE antitético, podemos tratar os 2M valores de f como IID?

Use as M médias de pares independentes e s_Y/√M.


## Monte Carlo a custo fixo — 22/10/2026

Aula `monte-carlo-incerteza` aprofundada de 3 seções/2 exercícios para 14/12. Preservados exemplo original, Python incorporado, desafio e IDs mc1/mc2. Onze seções/dez exercícios novos desenvolvem variância por integração, dependência dentro de pares, orçamento N=2M, covariância, três casos e SE calculado pelas médias de pares independentes. Dois MathML novos. Nenhum resultado pessoal ou execução de EP1 inferido.

Para f(u)=u²: μ=1/3, σ²=4/45, Y=u²−u+1/2, Var(Y)=1/180 e covariância −7/90. Com mesmo N de avaliações, a razão Var(independente)/Var(antitético)=8, e a razão de SE é √8. Para f(u)=(u−1/2)², f(1−u)=f(u): o antitético dobra a variância a custo fixo. Para f(u)=u, cada par vale 1/2 e a variância antitética é nula. Os exemplos e as contas são desenvolvimentos próprios; não são medidas de desempenho de uma pesquisa.

Fonte complementar primária consultada parcialmente: Art Owen, Monte Carlo theory, methods and examples, capítulo 8/Variance reduction, §§8.1–8.2 pp.4–7/PDF4–7, https://artowen.su.domains/mc/Ch-var-basic.pdf . Fonte disponibilizada pelo autor, cabeçalho copyright 2009–2013,2018. Apoia o método, a covariância e a necessidade de considerar custo; sem reprodução do capítulo, figuras ou exercícios. Apenas link ao PDF original, sem cópia no site. Os fundamentos temáticos dos Magalhães permanecem referências anteriores, sem nova consulta aos seus corpos neste bloco. A bibliografia do programa padrão não foi substituída por este complemento. Fonte oficial da disciplina não reaberta: limitações anteriores de acesso e versão da turma preservadas.

Laboratório em `labs/monte-carlo-pares/`: polinômios por coeficientes int/Fraction, integração e momentos exatos; experimento separado com gerador Random e semente. O SE da média antitética usa M valores Y, não 2M resultados tratados como independentes. `python3 labs/monte-carlo-pares/experiment.py`; testes `python3 -m unittest discover -s labs/monte-carlo-pares -t .`. O orçamento conta chamadas de f, sem cronometrar gerador, máquina ou reaproveitamento. A semente não prova independência matemática ou qualidade do gerador.

Novo `antithetic-cost-models.js`, namespace exclusivo AntitheticCostModels, painel antitheticCost: três funções, M=2^k com k 2..10, N 8..2048, curvas teóricas contra log₂N. Azul antitético, preto tracejado independente, pontos no orçamento selecionado. Não há erro observado ou simulação de réplicas no painel; as saídas aleatórias só estão no laboratório. Variância zero é exibida sem razão infinita. Texto e notas explicam as hipóteses e o caso de piora.

Quatro testes novos: momentos racionais e mesmo custo em 27 estados; 27 polinômios quadráticos contra quadratura independente e identidade por covariância; escala e reprodução do experimento; contratos. Vinte e sete referências exatas conferidas no JavaScript. Suíte completa: 797 testes Python, 284 demonstrações/852 cenários JS mais referências adicionais e 470 estruturas MathML aprovados. JS repetido após ajustar formatação portuguesa do SE. Navegador: teclado mudou família 0→1 (razão 0,5)→2 (variância nula), resposta 0 aceita no exercício 8. Gráfico/relatório inspecionados em 390 px, sem transbordamento horizontal e console sem erros observados. Prévia monte-carlo-pares-mobile.jpg; viewport restaurado.

Percurso de Computação IV reconciliado: 30 aulas próprias/177 exercícios, 19 introduções curtas e 11 recortes mais desenvolvidos. As 30 aparecem uma vez cada nas etapas; apoios PECE/MAP2220 e calor implícito/MAP2320 preservam suas origens. Dez grupos do programa padrão continuam parciais. Complementos probabilísticos não acrescentam itens oficiais e não certificam a turma ou domínio pessoal. Catálogo global: 488 aulas/2631 exercícios, rascunhos para revisão.

Próxima ação pessoal: derivar Var(Y), justificar o fator 8 a custo fixo e explicar o contraexemplo simétrico. Próxima ampliação local: réplicas independentes e estudo de erro observado versus SE, com custo explícito. Próxima alternância global: sequência e cobertura de Biologia IV. Samsung Notes, evidência pessoal e objetivo integral permanecem pendentes. Saldo semanal após bloco: 99%; parada operacional: 65%.
