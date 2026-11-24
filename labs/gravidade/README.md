# Laboratório de gravitação e erro de integração

Material original em rascunho, para revisão de Jhuann. Referência temática: Computer Science, eixo 3.4. Não utiliza dados da IC nem modela buracos negros.

## Objetivo e modelo

Implementar interações de 2–20 massas pontuais em duas dimensões; G=1, unidades adimensionais, sem suavização nem colisões. O algoritmo direto tem custo O(N²) por passo. A distância zero é rejeitada nos estados avaliados, mas isso **não detecta colisões entre instantes**. Aproximações muito próximas exigem rever o passo/modelo; este laboratório não resolve esse problema.

Euler–Cromer atualiza velocidades e depois posições a partir de forças simultâneas. Velocity Verlet usa r'=r+hv+h²a/2, recalcula a' em r' e usa v'=v+h(a+a')/2. [Documentação primária de integração velocity Verlet no LAMMPS](https://docs.lammps.org/latest/Developer_flow.html). Código deste laboratório é próprio, sem uso do LAMMPS.

Referência: massas 1 e 1 em x=±1/2, velocidades tangenciais ±1/√2. Pela aceleração centrípeta, ω²(1/2)=1 e ω=√2. Período 2π/√2. Energia −1/2, momento total e centro de massa zero; momento angular 1/√2. Só essa configuração tem a referência analítica implementada.

## Execução

Baixe `experiment.py` e execute `python3 experiment.py`. Apenas biblioteca padrão; imprime comparação em t=0,7 com 20, 40, 80 e 160 passos. Não grava arquivos nem altera entradas. Para testes, salve também `test_experiment.py` ao lado e execute `python3 -m unittest discover -p 'test_*.py'`.

A função `integrate(masses,positions,velocities,time,steps,method)` retorna estados e diagnósticos sem modificar os argumentos. Métodos: `cromer` e `verlet`. Não aplicar `position_error` a outro estado: essa função usa exclusivamente a referência de `binary()`.

## Roteiro de estudo

1. Derive o período e os invariantes da configuração inicial no papel.
2. Explique por que a força de cada par deve usar um único estado de posições.
3. Execute os dois métodos em t=0,7; compare h e h/2. Use um instante não periódico para evitar cancelamentos acidentais.
4. Calcule erro de posição e máxima diferença absoluta de energia; explique por que são diagnósticos diferentes. Não deduza a ordem geral do método pela energia deste caso especial.
5. No site, observe a órbita, selecione instantes e compare os métodos/passos.
6. Experimente três massas no Python. Confira momento e movimento uniforme do centro de massa; não reutilize a solução exata binária.
7. Escreva uma análise curta com configuração, método, passo, referência, resultado e limites.

Cinco testes conferem invariantes analíticos, força como negativo do gradiente do potencial por diferença central, convergência de posição, momento/centro de massa/momento angular de três massas e contratos. Esses testes não validam modelos astrofísicos nem demonstram aprendizagem de Jhuann.

Pendentes: revisão conceitual e didática de Jhuann, desafios graduais, condições iniciais importadas, relatórios com proveniência e visualização geral de N corpos. O site apresenta somente a configuração binária conhecida.
