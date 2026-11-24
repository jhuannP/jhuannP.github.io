# Propagação não linear — energia quadrática

## Uma derivada descreve a resposta local do modelo

Na aula anterior, a diferença de posições era linear e sua propagação de variância era exata. Agora considere K=mV²/2 para movimento clássico em uma dimensão, com massa tratada como exata no modelo. A velocidade V é assinada, enquanto K é não negativa. Sua incerteza será representada por uma distribuição atribuída a V; não estamos descrevendo a variação temporal da energia de um objeto real. O exemplo é sintético.

## Escolha uma distribuição de entrada antes de calcular

Adotamos V=v₀+δ, com δ uniforme entre −a e +a. A semilargura a é não negativa; não é o desvio padrão. Para a>0, a densidade de δ é 1/(2a). Simetria dá E[δ]=E[δ³]=0. A integração de δ² e δ⁴ fornece E[δ²]=a²/3 e E[δ⁴]=a⁴/5. Por exemplo, E[δ²]=(1/(2a))×[δ³/3] de −a a +a=a²/3. Se a=0, a entrada é constante. A distribuição uniforme é uma hipótese deste exercício, não consequência automática da resolução de um instrumento.

u²(V)=a²/3; E[δ⁴]=a⁴/5

## A aproximação de primeira ordem mantém somente a inclinação

No ponto v₀, a derivada é dK/dV=mv₀. Escrever K(V)≈K(v₀)+mv₀δ substitui a curva por sua tangente. A contribuição de primeira ordem para a variância é u_lin²(K)=(mv₀)²u²(V)=m²v₀²a²/3. Essa é uma aproximação: o termo quadrático em δ foi descartado. Sua unidade é J², pois mv₀ tem unidade J/(m/s), que ao quadrado multiplica uma variância em (m/s)².

u_lin²(K)=m²v₀²a²/3

## Expandir a energia mostra o termo que ficou de fora

Neste modelo quadrático, a expansão termina exatamente: K=mv₀²/2+mv₀δ+mδ²/2. Ao tomar a média, o termo linear some e o quadrático permanece. Logo E[K]=K(v₀)+ma²/6. Calcular a energia na velocidade central e calcular a média da energia atribuída pela distribuição são operações diferentes. Não alteramos automaticamente o estimador de uma experiência real: primeiro é preciso decidir qual quantidade se quer relatar e justificar a distribuição de entrada.

E[K]=mv₀²/2+ma²/6

## A variância exata inclui a contribuição da curvatura

Subtraindo a média, K−E[K]=mv₀δ+(m/2)(δ²−a²/3). Ao elevar ao quadrado e tomar a média, o termo cruzado é zero pela simetria: depende de E[δ³] e E[δ]. A variância de δ² é a⁴/5−a⁴/9=4a⁴/45. Portanto Var(K)=m²v₀²a²/3+m²a⁴/45. O primeiro termo é o da tangente; o segundo é não negativo e permanece mesmo se a inclinação for zero.

Var(K)=m²v₀²a²/3+m²a⁴/45

## Exemplo: compare os dois cálculos sem confundir média e variância

Use m=2 kg, v₀=2 m/s e a=0,2 m/s. A energia no centro é K(v₀)=4 J. Como a²=1/25 (m/s)², a variância de entrada é 1/75 (m/s)² e a média da energia é 301/75 J≈4,01333 J. A variância linear vale 16/75 J²≈0,213333 J². A contribuição adicional vale 4/28125 J²≈0,000142222 J²; a soma exata é 6004/28125 J²≈0,213476 J². Não some números de média em J com variâncias em J².

## Um critério de comparação precisa declarar o que está comparando

Se v₀≠0 e a>0, a razão entre a variância adicional e a variância linear é a²/(15v₀²). No exemplo, ela é 1/1500, cerca de 0,067%. Essa porcentagem compara variâncias, não incertezas padrão, nem o deslocamento da média. Se esse desvio é aceitável depende da precisão exigida e das outras componentes do orçamento. Não transformamos uma razão pequena em validação universal da tangente para qualquer modelo.

[Var(K)−u_lin²(K)]/u_lin²(K)=a²/(15v₀²)

## No centro zero, a tangente fornece uma conclusão incompleta

Mantenha m=2 kg e a=0,2 m/s, mas use v₀=0. A derivada é zero; a fórmula linear produz variância zero. Entretanto V pode assumir velocidades não nulas, e a parábola atribui energia positiva a elas. O modelo exato tem E[K]=1/75 J e Var(K)=4/28125 J². A razão relativa ao termo linear fica indefinida, pois seu denominador é zero. O código retorna None nessa razão, preservando separadamente a variância positiva.

## Diminuir a largura afeta os termos com potências diferentes

Se dividimos a por dois mantendo m e v₀, a variância linear divide por quatro e a contribuição de curvatura divide por dezesseis. Esse comportamento explica por que a tangente melhora em muitos regimes estreitos fora do centro zero. Também mostra por que olhar somente o tamanho absoluto da incerteza de entrada não basta: a curvatura e o ponto de operação importam. Trocar v₀ pelo seu negativo preserva todos os momentos da energia neste modelo simétrico.

## Massa conhecida e modelo clássico são hipóteses do exercício

Não propagamos incerteza da massa, correlação entre massa e velocidade, calibração, resolução adicional ou efeitos relativísticos. Na prática, o modelo de medição deve incluir as componentes relevantes e dados que sustentem a distribuição de entrada. A expressão exata desta aula vale para a distribuição uniforme especificada e a função quadrática; outras distribuições podem ter momentos de terceira e quarta ordem diferentes. Não use a⁴/5 sem verificar a distribuição.

## O laboratório confere os momentos por um segundo caminho

O núcleo retorna frações racionais para energia no centro, média, variância de entrada, variância linear e variância exata. O teste independente integra V² e V⁴ diretamente entre v₀−a e v₀+a e compara E[K²]−E[K]², sem usar a expansão centrada. Aceita massa positiva, centro assinado e semilargura não negativa como int/Fraction. Entradas float, bool ou texto são rejeitadas. O programa calcula o modelo, sem escolher automaticamente um procedimento de medição.

## Como transformar a aula em uma demonstração pessoal

Refaça a expansão e a conta do centro zero; depois execute o laboratório e explique quais termos foram mantidos ou descartados. Ao escrever um futuro relatório, declare a grandeza, a distribuição, as unidades e o critério para aceitar a aproximação. Os exemplos preparados aqui não são dados de sua graduação nem prova de que você executou uma experiência. Física Experimental I continua com várias lacunas, materiais pessoais e revisão conceitual pendentes.

## Exercícios e resoluções

- Com m=2 kg e v₀=2 m/s, quanto é K(v₀), em J? **Resolução:** 2×2²/2=4 J.
- Para a=0,2 m/s e distribuição uniforme simétrica, qual u²(V), em (m/s)²? **Resolução:** a²/3=(1/25)/3=1/75.
- Com m=2 kg e v₀=2 m/s, qual a derivada dK/dV, em J/(m/s)? **Resolução:** mv₀=2×2=4.
- No exemplo completo m=2, v₀=2 e a=0,2, qual E[K], em J? **Resolução:** 4+ma²/6=4+1/75=301/75 J.
- Qual a variância linear da energia nesse exemplo, em J²? **Resolução:** (mv₀)²u²(V)=16/75 J².
- Qual a variância adicional de curvatura, em J²? **Resolução:** m²a⁴/45=4/(625×45)=4/28125 J².
- Qual a variância exata total no mesmo exemplo, em J²? **Resolução:** 16/75+4/28125=6004/28125 J².
- Quanto vale a razão variância adicional/variância linear no exemplo v₀=2 e a=0,2? **Resolução:** a²/(15v₀²)=0,04/60=1/1500.
- Para m=2 kg, v₀=0 e a=0,2 m/s, qual a variância exata da energia, em J²? **Resolução:** O termo linear zera, mas m²a⁴/45=4/28125 J² continua positivo.
- Ao dividir a por dois, por quanto se divide a contribuição de curvatura à variância? **Resolução:** Ela é proporcional a a⁴: 2⁴=16.

## Código e fontes

Na raiz: `python3 -m unittest discover -s labs/propagacao-nao-linear -t .` e `python3 -m labs.propagacao-nao-linear.kinetic`. Somente biblioteca padrão. Entradas em SI como int/Fraction; massa positiva, centro assinado e semilargura não negativa. Para a=0, o modelo é degenerado e os momentos são tratados sem dividir por a. A razão extra_over_linear retorna None quando a variância linear é zero. A função não infere a distribuição, não propaga massa incerta e não calcula fatores de abrangência.

Oráculo independente: integra V² e V⁴ no suporte uniforme em 60 combinações de massa, centro e largura, incluindo suporte atravessando zero e entrada degenerada. Compara E[K] e E[K²]−E[K]² com a fórmula centrada. Código não depende do laboratório anterior.

Fonte primária: [NIST TN1297 Apêndice A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty), A.1–A.3 e A.5 reconferidos parcialmente em 22/10/2026. O cálculo exato da energia, os números e os exercícios são próprios; não são resultados ou experiências pessoais. Livros da bibliografia nominal e programa efetivo da turma não foram reconsultados. Rascunho assistido por IA; próxima revisão pessoal: reconstruir a variância a partir de δ e explicar o caso v₀=0. Próximo desenvolvimento desta trilha: gráficos e medidas com dados pessoais quando disponíveis.

Verificação do bloco não linear: cinco testes de laboratório aprovados, incluindo 60 combinações comparadas por integração racional direta de V² e V⁴, entrada degenerada, sinal e escalas de massa/largura. Treze testes de catálogo e 559 estruturas MathML aprovados. Navegador a 390 px: documento de 375 px, figura inspecionada; questão 9 rejeitou zero e aceitou 4/28125 J². Console sem erros observados. Prévia propagacao-nao-linear-mobile.jpg. Catálogo: 507 aulas/3241 exercícios; cobertura recalculada. Não houve revalidação global de todos os laboratórios ou comprovação de medição real. Saldo semanal confirmado após bloco: 90%; parada em 65%. Próxima revisão pessoal: reconstruir E[K] e Var(K) sem tratar o valor central como média da função. Após estes três recortes de metrologia, distribuir o próximo bloco entre as outras lacunas do catálogo; gráficos experimentais permanecem pendentes.
