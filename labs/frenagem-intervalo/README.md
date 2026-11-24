# Aceleração e frenagem: intervalo e mudança de regime

Rascunho didático original de 22/10/2026, para revisão de Jhuann. Aprofunda `ef-aceleracao` sem trocar título, exemplo 10 m/s e 2 m/s², IDs anteriores, desafio position(t,v0,b) ou identificador schoolBraking. Python é opcional. Não há medida ou orientação para trânsito/veículo real.

## Fontes consultadas parcialmente

OpenStax Physics [§3.1](https://openstax.org/books/physics/pages/3-1-acceleration), definições, unidades e sinais; [§3.2](https://openstax.org/books/physics/pages/3-2-representing-acceleration-with-equations-and-graphs), equações de aceleração constante e relações gráficas. Consulta direta parcial em 22/10/2026. Uma tentativa inicial de URL 3.4 não abriu; o título/URL corretos de 3.2 foram encontrados e abertos, sem tratar o endereço falho como fonte lida. Não se copiaram figuras, exemplos resolvidos, exercícios, vídeos ou demonstrações da fonte. Os números, dois modelos e diagramas são próprios. Não houve leitura de PDF privado ou experimento.

## Dois modelos distintos

x₀=t₀=0, v₀>0,b>0. A: aceleração −b até t_s=v₀/b e permanência em repouso depois; x usa τ=min(t,t_s), v=max(v₀−bt,0). B: a=−b continua e a velocidade pode ficar negativa. Em t_s, v de A é contínua com inclinação esquerda −b e direita 0; aceleração instantânea não é definida nessa junção, indicada como None/null. Média em [0,t] é (v_A(t)−v₀)/t somente para t>0; intervalo nulo retorna None/null. Código aceita v₀=0 como repouso desde o início no modelo A, sem inventar uma frenagem anterior.

Caso padrão em t=5 s: 25 m, velocidade zero. Em t=10s: A permanece em 25 m/v=0; B retorna a x=0 com v=−10 m/s e distância 50 m. A média de aceleração de A entre 0 e 10 s é −1 m/s², distinta da aceleração instantânea zero em 10 s.

A função JS SchoolPhysicsModels.brake foi preservada. A nova brakingComparison reaproveita seus campos e adiciona comparação/diagnóstico; o painel mantém o identificador schoolBraking e os mesmos controles. O gráfico de posição de A foi preservado e recebe legenda acessível. Um segundo gráfico v×t compara A azul contínuo e B tracejado escuro, mesma escala adaptativa, marcador azul em A. Tabela separa posição, velocidade e distância, sem confundir posição negativa com distância negativa.

Python usa int/Fraction, sem arredondamento nos testes. JS usa números finitos no domínio do painel (v até 20, b de 1 a 5, t de 0 a 25) e é cruzado com referências racionais. A tela usa v de 1 a 20 m/s, b de 1 a 5 m/s², t de 0 a 25 s. Não há reação, inclinação, aderência, arrasto, força prescrita por contato ou transição suave. É cinemática ideal; parâmetros não são um freio medido.

## Executar e verificar

```sh
python3 labs/frenagem-intervalo/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: área de trapézio independente da expressão de posição; continuidade e inclinações laterais exatas; coincidência até a parada e divergência depois; sinais/escala/repouso inicial/contratos. 45 estados racionais cruzam Python/JS, incluindo parada e pós-parada; a API original brake permanece consistente. Os testes não validam um veículo real nem substituem revisão conceitual.

Próximos recortes: aceleração variável, movimentos por trechos gerais e leitura de dados com referências adequadas. O curso de Física escolar continua parcial e pendente de revisão/planos de aula.


22/10/2026 — Aceleração/frenagem aprofundada: 14 seções/12 exercícios, dois modelos/gráficos/tabela, média e junção. Fontes parciais OpenStax e limites em labs/frenagem-intervalo/README.md. 610 testes Python, 245 demos/735 cenários, 45 referências e 342 MathML aprovados; UI t0/t_s/pós-parada, extremos, exercícios e 390 px conferidos. Física escolar 11 aulas/50 exercícios, três recortes desenvolvidos/oito introduções. Catálogo 466 aulas/2140 exercícios em rascunho. Próxima ação: cobertura/referências de Laboratório I, sem atribuir experimento pessoal. Saldo 88%; parada 65%; revisão pessoal pendente.
