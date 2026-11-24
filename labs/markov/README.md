# Laboratório: trajetórias e distribuição de uma cadeia finita

Projeto original em Python 3 e português, com biblioteca padrão. A matriz sintética em `transition.json` tem linhas como origens e colunas como destinos. O vetor linha de probabilidades evolui por `p_novo=pP`. Uma trajetória ocupa um estado por vez; a distribuição descreve chances, não uma trajetória individual.

## Executar

Abra terminal na pasta extraída, com Python 3 disponível:

```sh
python3 experiment.py --matrix transition.json --steps 10 --samples 1000 --seed 42
python3 experiment.py --matrix transition.json --steps 10 --samples 1000 --seed 42 --output meu-resultado.json
python3 -m unittest discover -p 'test_*.py'
```

No Windows, use o comando Python 3 configurado, como `python` ou `py -3`, se disponíveis. A saída precisa ser um arquivo novo; não substitui um existente.

Contrato: matriz quadrada de 1–10 estados, entradas finitas entre 0 e 1 e linhas somando 1 com tolerância absoluta 10⁻¹². Após essa verificação, cada linha é normalizada para corrigir apenas discrepância de arredondamento; a matriz usada e esse procedimento aparecem no relatório. Etapas 0–50, trajetórias 1–10000, estado inicial válido e semente uint32.

## Roteiro de implementação

1. Leia a matriz e explique a convenção. Confira linhas, domínio, soma e estado inicial.
2. Implemente a atualização do vetor distribuição. Teste massa total, não negatividade e referências abaixo.
3. Implemente um sorteio pela soma acumulada das probabilidades de uma linha. Teste matrizes determinísticas antes das aleatórias.
4. Gere várias trajetórias com estado local do gerador; conte os estados em cada instante. Aqui a ordem de sorteios é por tempo e depois por trajetória.
5. Compare frequência e probabilidade calculada. A diferença é erro Monte Carlo neste modelo discreto, não erro de um integrador de EDO.
6. Acrescente intervalos Wilson marginais nominais de 95% no instante final, quando houver sorteios. Tempos dentro da mesma trajetória são dependentes; o intervalo marginal não é uma banda simultânea para toda a curva.
7. Troque a matriz em uma cópia por alternância determinística e por identidade. Explique por que distribuição estacionária, convergência e unicidade são conceitos distintos.
8. Produza relatório de configuração, gerador, versão/hash e interpretação. Preserve os arquivos de entrada e saída existentes.

## Referências independentes

Para `P=[[0,8;0,2],[0,4;0,6]]`, começando em A:

`a(t+1)=0,4+0,4a(t)` e `a(t)=2/3+(1/3)0,4^t`.

Logo a(0)=1, a(1)=0,8, a(2)=0,72 e o limite é 2/3. As referências são contas do modelo, não dados experimentais.

Em `P=[[0,1],[1,0]]`, (1/2,1/2) é estacionária, mas começar em A alterna entre (1,0) e (0,1), sem convergência. Na identidade, toda distribuição é estacionária e o estado inicial permanece.

## Sementes e incerteza

Python usa `random.Random`; navegador usa LCG. Mesma semente não promete mesmas trajetórias entre esses geradores. Compare o modelo e registre a implementação.

Intervalos Wilson são nominais aproximados. Referência de estudo: [NIST — Confidence intervals for proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm). Os intervalos por estado não são uma região conjunta de confiança para o vetor todo. Em t=0 a distribuição inicial é conhecida e o relatório usa os valores fixos, sem atribuir incerteza amostral a eles.

## Entrega e limites

Sua versão deve tratar matrizes inválidas, conservar massa na evolução, recuperar casos determinísticos e fórmula de dois estados, reproduzir a sequência dentro do protocolo, e gerar relatório com frequências e interpretação. Testes e referência prontos não comprovam implementação ou domínio pessoal de Jhuann.

Não há modelo de dados da IC, tempo contínuo, cadeia de Markov geral infinita, estimação da matriz a partir de dados, ou validação de mecanismo físico neste laboratório.
