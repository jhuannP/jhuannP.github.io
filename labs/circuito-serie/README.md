# Circuito série: conexões, nós e energia

Notas originais assistidas por IA, em rascunho para revisão pessoal de Jhuann. Não atestam experiência de montagem, medidas ou domínio pessoal. O circuito é um modelo hipotético de fonte CC ideal e resistores ôhmicos constantes positivos em uma única malha, com fios sem resistência.

## Fontes consultadas parcialmente — 26/10/2026

- [OpenStax, University Physics Volume2, §10.2](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel): conexão em série, corrente comum, resistência equivalente e balanço de potência. Consulta dos trechos iniciais de série e comparação da topologia de paralelo; sem declarar leitura de toda a seção de redes mistas.
- [OpenStax, University Physics Volume2, §9.5](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power): definição de potência, formas para resistor e energia com duração/kWh. Não se adotam afirmações de custos ou aparelhos do texto como dados atuais.

A primeira URL tentada para energia/potência usava9.6 e retornou404; a seção efetivamente consultada é9.5 acima. Sem consulta nova aos PDFs privados de NussenzveigIII neste bloco. Números, diagrama, exercícios, deduções didáticas e código são próprios.

## Reconstruir o exemplo

Fonte12V, resistores2Ω e4Ω em série. A conexão sem ramificação permite corrente comum. Pela malha,12−2I−4I=0, logo I=2A e R_eq=6Ω. Quedas4V e8V. Escolhendo o terminal negativo como zero, os potenciais ao longo dos resistores são12,8,0V; adicionar a mesma constante a todos não altera as diferenças.

Corrente é carga por tempo, não energia: em60s passam120C por cada seção, sem consumo de carga. A energia entregue por carga através de uma queda explica Pᵢ=VᵢI=I²Rᵢ. Potências8W e16W; fonte fornece24W. Convenção passiva: resistores absorvem+8,+16W; fonte absorve−24W, com soma zero.

Durante60s em regime constante, energias480,960J, total1440J.1Wh=3600J,1kWh=3,6×10⁶J;24W durante1h correspondem a0,024kWh. Não há duração implícita em um valor em watts.

## Pergunta antes de mover o controle

Em12V,R₁=2Ω,R₂=6Ω, preveja I=1,5A, quedas3 e9V, potências4,5 e13,5W, total18W. O painel existente mantém somente duas resistências positivas em série. Não altera as conexões e não calcula energia acumulada sem tempo. Uma fonte de tensão fixa pode fornecer correntes distintas para cargas distintas.

## Executar

Na raiz do site:

```sh
python3 -m labs.circuito-serie.circuit
python3 -m unittest discover -s labs/circuito-serie -t .
node labs/circuito-serie/test_panel.cjs
```

`series` recebe volts, lista/tupla de resistências em ohms e duração em segundos. Usa int/Fraction, rejeita bool/float, fonte negativa, duração negativa e resistência nula/negativa. Resolve qualquer lista não vazia de resistores em série, não detecta a topologia de uma rede arbitrária. Tensão zero e duração zero são permitidas.

Cinco testes Python: exemplo;468 combinações com0–12V e resistores1–6Ω comparadas à solução independente por equação do nó intermediário; balanços com1–10 resistores racionais; escalas e troca de ordem; contratos. O teste JavaScript confere432 estados dentro dos controles do painel pela equação de nó. Os testes verificam implementação e coerência do modelo, não provam leis físicas ou adequação de um componente real. O painel não foi modificado.

## Exercícios novos: respostas e interpretação

1. R_eq=6Ω.
2. Queda em R₁=4V.
3. Potencial intermediário8V, dada a referência escolhida.
4. P₁=8W.
5. Potência total24W.
6. Energia em60s:1440J.
7. Carga em60s:120C; carga não consumida.
8. Com mais6Ω em série, I=1A.
9. Estado alterado do painel: I=1,5A.
10. Potência absorvida da fonte:−24W, não+24W.

Próxima revisão pessoal de20min: desenhar os nós, resolver o estado alterado do painel e conferir as três somas (quedas, potências e energias). Campos pessoais permanecem sem preenchimento. Redes paralelas/mistas, resistência interna da fonte, instrumentos e transitórios ainda precisam de material próprio.
