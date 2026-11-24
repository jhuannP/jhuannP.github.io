# Unidades e MRU — roteiro original

Estado: rascunho, pendente da revisão pessoal. Não registra uma experiência realizada.

## Modelo e reprodução

`motion(x0, velocity, t, t0)` usa metros, segundos e velocidade com sinal em m/s. Exige valores finitos e t>=t0. Frações preservam os casos decimais exatos. `kmh_to_ms` usa 5/18. Rode `python3 -m unittest labs.mru.test_experiment` na raiz do protótipo. As 36 referências cruzam três posições, três velocidades e quatro intervalos; o navegador usa os mesmos controles e t0=4 s. Python e JS são implementações independentes; os testes Python também acumulam passos de 1/4 s.

## Sequência

1. Preveja 30 m às 4 s, -2 m/s e leitura às 9 s: x=20 m, deslocamento=-10 m, distância=10 m.
2. Zere v e explique a reta horizontal. Inverta o sinal e compare inclinações.
3. Desloque x0 em 10 m: quais quantidades mudam?
4. Opcionalmente registre um movimento aproximadamente retilíneo e compare resíduos de uma reta. Registre resolução e método; dois pontos não bastam para testar constância. Não há dados medidos neste laboratório.

## Fontes e limites

Consultados em 16/10/2026: [OpenStax Physics 2.2](https://openstax.org/books/physics/pages/2-2-speed-and-velocity) para rapidez/velocidade e [2.3](https://openstax.org/books/physics/pages/2-3-position-vs-time-graphs) para gráficos. Exemplos, exercícios, simulação e código originais. Não há reprodução de figuras ou exercícios da fonte. Esta aula não é uma ementa universitária nem prova de domínio de Jhuann. Não inclui ajuste estatístico, incerteza, aceleração ou dinâmica.
