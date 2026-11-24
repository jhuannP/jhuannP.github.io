# Refinamento do mesmo PVI

Material original,28/10/2026, com apoio de IA; revisão pessoal pendente. Preserva o exemplo anterior de erros0,008/0,002 e o código genérico Euler/Heun/RK4 na aula. Novo laboratório em `refine.py`: y′=−y,y(0)=1,T=1,variáveis adimensionais. Euler racional dá q_N=(1−1/N)^N. A referência exp(−1) é aproximada com Decimal,28–100dígitos; logaritmos usam float.

Expansão própria: log(q_N)=−1−h/2+O(h²),h=1/N. Logo erro assinado q_N−exp(−1)=−exp(−1)h/2+O(h²). O termo linear não nulo estabelece primeira ordem para esse problema. Erro é no instante final, não norma máxima na trajetória.

Assumindo q(h)=y+C h^p+o(h^p),C≠0, diferenças D(h)=q(h/2)−q(h) têm razão de módulos tendendo a2^p. A estimativa do erro fino é |D(h)|/(2^p−1); não é uma cota geral. Para p=1 e expansão com resto O(h²), R=2q(h/2)−q(h) cancela o termo linear. Não transforma toda a trajetória do integrador em segunda ordem.

N=1,2,4: q=0,1/4,81/256, diferenças1/4 e17/256, razão64/17,p_obs≈1,9125. N=16,32,64: p_obs≈1,028916. Para N16/32: erro fino≈0,0058241519, estimativa≈0,0059811588, erro extrapolado≈0,0001570069. Três execuções independentes N16/32/64 usam112avaliações. As linhas da tabela mostram n coarse e o erro da solução com2n; custo7n inclui também4n para diagnóstico.

`differences` recebe três aproximações int/Fraction e deixa a ordem ausente se diferenças forem nulas ou trocarem sinal. A estimativa order1 continua sendo um número condicional ao modelo de primeira ordem, não garantia. Caso constante y′=0 produz diferenças zero e razão0/0, não ordem infinita comprovada. Sem referência, coincidência pode vir de cancelamento ou arredondamento.

## Fonte

Driscoll e Braun, Fundamentals of Numerical Computation, [§6.2 Euler](https://fncbook.com/euler/), recortes de§§6.2.1–6.2.2 consultados em28/10/2026: definições de truncatura unitária e erro global, Teorema6.2.1 e sua hipótese de controle da derivada em relação ao estado. A truncatura é dividida pelo passo; o defeito de um passo de Euler é O(h²), sua truncatura unitária O(h). Com as hipóteses do teorema em intervalo fixo, a ordem global é O(h). Sem cópia de scripts, exemplos ou exercícios. Referência temática anterior Burden10 cap.5 não relida neste bloco; não se declara leitura integral de nenhum capítulo. PVI, números, expansão e diagrama próprios.

## Executar e verificar

```sh
python3 labs/convergencia-malhas/refine.py
python3 -m unittest discover -s labs/convergencia-malhas -t .
```

Quatro testes:64contagens com recorrência independente contra expressão fechada; erros em28/60dígitos e razões em quatro refinamentos; famílias sintéticas de ordens1–4 e cancelamento; contratos. Limite4096passos por referência racional, triplas exigem4n≤4096. Sem medição de custo real; contagem de avaliações teórica.

Revisão20min: reconstruir q_N, refutar a interpretação da tripla grosseira, separar erro/estimativa/extrapolação. Sistemas/normas físicas, eventos, malha adaptativa, rigidez e validação pessoal continuam pendentes. Testes não certificam domínio de Jhuann ou resultado de pesquisa.
