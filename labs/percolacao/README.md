# Laboratório: ensemble de percolação

Projeto original em Python 3 e português brasileiro, com biblioteca padrão. Cada sítio de uma grade quadrada abre independentemente com probabilidade `p`. A travessia liga a borda superior à inferior usando quatro vizinhos; diagonais não conectam.

`p` é probabilidade de ocupação de um sítio. A frequência de grades que atravessam estima outra quantidade: a probabilidade de travessia da grade finita escolhida. Ela não é um limiar crítico ou resultado da IC.

## Executar localmente

No terminal da pasta extraída, com Python 3 disponível:

```sh
python3 experiment.py --size 8 --samples 100 --p 0.6 --seed 42
python3 experiment.py --size 8 --samples 100 --p 0.6 --seed 42 --output meu-ensemble.json
python3 -m unittest discover -p 'test_*.py'
```

No Windows, use o comando do Python 3 configurado no seu ambiente, por exemplo `python` ou `py -3`, se disponíveis. Não há dependência externa. A saída em arquivo é nova e não substitui existente.

Contrato didático: tamanho 1–40, realizações 1–5000, p real finito em [0,1], semente inteira entre 0 e 2³²−1. O gerador é `random.Random`, local à execução. O relatório inclui configuração, algoritmo, versão de Python e hash do código.

## Etapas para sua implementação

1. Teste a travessia em grades fechadas, abertas, uma linha, um caminho com curvas e um par apenas diagonal. Explique a fronteira e a regra dos vizinhos.
2. Implemente uma busca com fila e conjunto de visitados; evite visitar o mesmo sítio indefinidamente. Valide grade retangular não vazia e valores booleanos ou inteiros 0/1.
3. Gere uma grade com o gerador local. Reproduza a execução com a mesma semente e ordem de chamadas.
4. Repita por M realizações independentes no modelo. Registre sucessos e proporção `sucessos/M`.
5. Acrescente intervalo Wilson bilateral nominal de 95%. É uma aproximação de cobertura; não prometa exatamente 95% em toda combinação de M e probabilidade.
6. Compare o caso 2×2 com a referência exata abaixo. Aumente M e observe variabilidade, sem exigir que o erro diminua monotonicamente em cada realização.
7. Compare diferentes tamanhos de grade, mantendo p. Registre cada configuração; não concluir limiar crítico a partir de uma grade ou de poucos tamanhos finitos.
8. Escreva o relatório e uma interpretação curta. Diferencie incerteza Monte Carlo, modelo de ocupação e conclusões físicas não examinadas.

## Referência exata 2×2

A grade atravessa se ao menos uma das duas colunas tem os dois sítios abertos. As colunas são independentes. Logo:

`θ₂(p)=1−(1−p²)²=2p²−p⁴`.

Em p=1/2, θ=7/16=0,4375. O teste também enumera todas as 16 grades com seus pesos, independentemente da simulação.

## Intervalo e interpretação

Para estimativa q=k/M e quantil z≈1,9599639845, Wilson usa centro `(q+z²/(2M))/(1+z²/M)` e meia largura `z sqrt(q(1−q)/M+z²/(4M²))/(1+z²/M)`.

Nos extremos k=0 ou k=M, os limites matemáticos exatos 0 ou 1 são preservados. Estimativa zero em M realizações não prova probabilidade verdadeira zero para um p interior.

Referência de estudo do intervalo: [NIST — Confidence intervals for proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm). Implementação e exemplos são próprios.

O navegador usa outro gerador pseudoaleatório; mesma semente não promete as mesmas grades de Python. Compare modelo, propriedades e distribuições, e registre o gerador usado.

## Critério de conclusão

Sua implementação deve passar em grades conhecidas e na enumeração pequena, preservar o protocolo de geração, produzir contagem/frequência/intervalo válidos, recusar entradas fora do contrato, e registrar configuração/versão e limites da interpretação. A referência pronta não comprova que Jhuann já implementou ou estudou este laboratório.
