# Bootstrap: reamostrar não corrige qualquer desenho de coleta

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Construir réplicas iid com reposição da distribuição empírica.
- Separar distribuição bootstrap condicional de variabilidade da população.
- Comparar enumeração exata e aproximação Monte Carlo.
- Calcular erro padrão, viés e percentis com suas convenções e limites.

## Comece pela amostra e pela estatística

Os dados observados x₁,…,xₙ são fixados nesta etapa. A estatística T pode ser média, mediana ou outra regra. O bootstrap não repete a coleta original: cria novas amostras a partir de um modelo construído com os dados disponíveis. É preciso decidir se esse modelo representa adequadamente o desenho de coleta.

## A distribuição empírica dá peso às posições

No bootstrap não paramétrico iid, cada uma das n posições observadas recebe peso 1/n. Valores repetidos mantêm sua multiplicidade. Nos dados [0,0,2], a massa de 0 é 2/3 e a de 2 é 1/3; eliminar o zero repetido mudaria a distribuição. A CDF empírica é a média das indicadoras de cada observação ser menor ou igual a x.

F̂ₙ(x)=(1/n)Σᵢ 1{xᵢ≤x}

## Uma réplica usa reposição e tamanho n

Sorteie n posições independentemente com reposição e recalcule T. Uma mesma posição pode aparecer várias vezes e outra pode não aparecer. Para [0,2], as réplicas possíveis são [0,0], [0,2], [2,0], [2,2]. Sem reposição, escolher todos os n elementos só permutaria a lista e a média não variaria.

x*=(x*₁,…,x*ₙ); T*=T(x*)

## Enumere um caso pequeno antes de simular

Há nⁿ sequências de posições, todas com peso 1/nⁿ no modelo iid empírico. Para n=2, as quatro médias são 0,1,1,2; as massas são 1/4,1/2,1/4 nos valores 0,1,2. Isso é a distribuição bootstrap exata condicionada àquela lista. O crescimento nⁿ torna enumeração inviável para amostras grandes; o laboratório limita n a 5.

## A média bootstrap tem uma identidade exata

Use E* e Var* para momentos condicionados aos dados observados. Cada sorteio da distribuição empírica tem média x̄ e variância Vₙ=Σᵢ(xᵢ−x̄)²/n. Pela independência das posições sorteadas, E*[x̄*]=x̄ e Var*(x̄*)=Vₙ/n. Para [0,2], x̄=1, Vₙ=1 e Var*(x̄*)=1/2. Isso não declara que a população original tenha esses parâmetros.

E*[x̄*]=x̄; Var*(x̄*)=Vₙ/n

## Monte Carlo aproxima essa distribuição; não cria dados novos

Em vez de enumerar, gere B réplicas. As frequências e momentos calculados a partir delas aproximam a distribuição bootstrap escolhida. Aumentar B reduz o erro Monte Carlo sob condições adequadas, mas não aumenta n, corrige a coleta ou garante melhora monotônica em cada execução. Mudar a semente muda uma realização do algoritmo, não os dados originais.

## Erro padrão exige declarar qual distribuição e divisor

O desvio padrão exato é √Var*(T*) quando enumeramos toda a distribuição. Com B réplicas Monte Carlo, a estimativa usual do erro padrão usa a soma dos desvios à média das réplicas dividida por B−1 e depois a raiz. Não use B−1 para a variância da distribuição completa enumerada; nesse caso os pesos já definem a esperança.

SE bootstrap exato=√Var*(T*)

## Viés bootstrap é condicional e depende da estatística

A estimativa bootstrap de viés é E*[T*]−T observado, aproximada pela média das réplicas menos o valor observado. Para a média, a identidade acima dá zero na distribuição exata, embora Monte Carlo possa produzir pequeno deslocamento. Para a mediana de [0,0,2], T observado=0; a mediana bootstrap vale 2 com massa 7/27 e 0 com massa 20/27, então o viés bootstrap é 14/27. Não é uma revelação automática do viés verdadeiro na população original.

viés bootstrap=E*[T*]−T observado

## Percentis pedem uma convenção explícita

O método percentil usa os quantis 2,5% e 97,5% da distribuição de T* para um intervalo nominal usual de 95%. Neste laboratório, usamos a inversa da CDF empírica sem interpolação: o menor valor cuja acumulada atinge o nível. Na lista ordenada de B réplicas, isso escolhe o índice de ordem ceil(uB), com índices iniciados em 1. Outras convenções podem dar números distintos em amostras pequenas.

quantil empírico: menor t com F*(t)≥u

## Percentis não garantem cobertura exata de 95%

A enumeração exata elimina erro Monte Carlo no modelo empírico, mas não torna esse modelo igual à população original. Cobertura frequentista do intervalo percentil exige condições de aproximação e depende da estatística e distribuição. Não confundir o nível nominal com cobertura demonstrada, nem com probabilidade posterior. O gráfico mostra os percentis e deixa essa limitação explícita.

## Um extremo expõe um limite do reamostrador

Toda réplica não paramétrica usa valores já observados. Se a estatística é o máximo, o máximo de qualquer réplica não excede o máximo observado. Num problema de estimar a extremidade superior de uma população uniforme, um intervalo percentil do máximo não consegue ultrapassar essa observação e pode falhar para o parâmetro real. Estatísticas não regulares precisam de análise própria; mais B não resolve essa restrição.

## Dependência e seleção pedem outro desenho

Reamostrar linhas individuais pressupõe um modelo iid apropriado. Séries temporais podem requerer reamostragem em blocos; dados agrupados podem exigir preservar os grupos; pesos e estratos podem fazer parte do desenho. Esses métodos não estão implementados aqui. Uma coleta que excluiu parte da população continua excluindo-a na distribuição empírica.

## Dados constantes e a preparação para usar em pesquisa

Com [2,2,2], todas as réplicas são constantes, SE*=0 e os percentis coincidem em 2. Isso é verdadeiro para o mecanismo empírico, não prova variância populacional nula. Antes de aplicar bootstrap, documente unidade de reamostragem, estatística, hipóteses, n, B, semente, convenção de quantis e diagnóstico. Esta aula não estima a incerteza dos resultados da IC.

## Exemplo resolvido

Dados [0,2]: qual a distribuição bootstrap exata da média e seu erro padrão?

1. A distribuição empírica atribui peso 1/2 a cada posição.
2. Reamostre duas posições com reposição: 00,02,20,22.
3. As médias são 0,1,1,2, cada sequência com peso 1/4.
4. E*[média*] = (0+1+1+2) / 4 = 1.
5. Var*(média*) = (1+0+0+1) / 4 = 1/2.
6. SE exato = √(1/2) ≈ 0,707107.
7. Os percentis adotados são [0;2]; isso não comprova cobertura de 95% para a média da população original.

## Exercícios e resoluções

### Para as quatro médias bootstrap de [0,2], qual E*[média*]?

(0+1+1+2)/4=1.

### Bootstrap iid automaticamente corrige viés de seleção na amostra?

Sim
Não

Reamostragem não corrige coleta enviesada por si só.

### Para os dados [0,2], qual Var*(média*) na enumeração exata?

Média das distâncias quadradas à esperança 1: (1+0+0+1)/4=1/2.

### Nos dados [0,0,2], qual a massa empírica do valor zero?

Duas das três posições contêm zero; massa 2/3.

### Para n=3, quantas sequências de posições há na enumeração bootstrap iid?

Há três escolhas em cada uma das três posições; 3³=27.

### Para a mediana de [0,0,2], qual o viés bootstrap exato?

A mediana observada é 0 e a bootstrap vale 2 com massa 7/27; viés 2×7/27=14/27.

### Sem reposição, escolher todos os n elementos e calcular a média permite reproduzir sua variabilidade bootstrap iid?

Sim
Não

As permutações preservam a média; o bootstrap iid usa reposição.

### Aumentar B cria novas observações independentes da população original?

Sim
Não

B controla aproximação Monte Carlo; o tamanho da amostra original continua n.

### SE bootstrap zero em [2,2,2] prova variância populacional zero?

Sim
Não

O mecanismo empírico só enxerga os dados disponíveis; não revela toda a população.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Biblioteca padrão, frações exatas para enumeração e mesmo gerador didático do navegador para Monte Carlo. Sem ler dados privados ou escrever resultados externos. Na interface, dados vêm de quatro listas sintéticas; não há importação de dados reais.

## Roteiro para preparar a aula à mão

1. Definir amostra fixa, distribuição empírica e reposição.
2. Enumerar [0,2] e calcular esperança, variância e SE.
3. Comparar B, semente, média/mediana e valores repetidos.
4. Discutir percentis, dados constantes e um caso em que o reamostrador falha.
5. Resolver exercícios antes de consultar respostas. A condução precisa de revisão de Jhuann.

## Evidência e limites

Cinco testes verificam enumeração, identidades da média, multiplicidade/mediana, quantis, reprodutibilidade/suporte e contratos. As 72 configurações de referência em reference.json foram geradas pelo Python e conferidas contra o JavaScript. Concordância não valida uma população real ou garante cobertura.

## Hipóteses e limites

- Bootstrap não paramétrico iid com reposição, condicionado à amostra observada.
- Enumeração do laboratório limitada a 1≤n≤5; Monte Carlo a 2≤B≤10000.
- Percentis pela inversa da CDF empírica sem interpolação; não garantia de cobertura exata.
- Gerador didático reprodutível; qualidade estatística não é certificada pela reprodutibilidade.
- Modelos sintéticos, sem resultados ou decisão científica da IC.
