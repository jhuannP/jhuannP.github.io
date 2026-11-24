# Batches, denominadores e estado dos parâmetros

27/10/2026. Aula original em rascunho,12 seções/12 exercícios; revisão pessoal de Jhuann pendente. Pré-requisitos: média ponderada, derivada e atualização por gradiente.

## Dois blocos de revisão

1. Reconstrua a soma para batches4,4,2 com médias1,2,3. Compare1,8 com a média sem pesos2 e com1,5 após descartar os dois itens finais.
2. No exemplo separado y=(1,1,3),w=0,ℓ=(w−y)², derive gradientes−2 e−6. Ponderados em2/3 e1/3, dão−10/3 e passo1/3 comη1/10. Atualizar a cada microbatch produz19/25; inverter a ordem produz17/25. Explique o papel do estado, além dos pesos.

## Código e alcance

Execute `python3 labs/batches-denominadores/batches.py` na pasta do protótipo. Usa Fraction,sem dependências externas. Enumera partições contíguas não vazias e confronta média ponderada com média direta e gradiente acumulado com gradiente completo no mesmo estado. Verifica descarte do resto, denominadores vazios e o contraexemplo de passos intermediários.

A mesma função de combinação é usada só quando a contagem corresponde ao objetivo declarado. No exemplo de tokens, média por token e média por sequência são objetivos diferentes. Máscaras, padding, múltiplas saídas e pesos de uma API precisam de contrato próprio; não há implementação de tokenização ou de redução de framework.

A figura mostra perdas fixas, não um registro de treino com parâmetros mudando. Não há autodiff,rede real,distributed training ou buffers de gradiente de framework. A equivalência demonstrada pressupõe perdas por exemplo idênticas nas duas avaliações,mesmo θ e estado. BatchNorm/dropout e alterações de composição/estado podem quebrá-la; não são implementados neste bloco. Arredondamento também pode causar diferenças numéricas mesmo quando a identidade algébrica vale.

## Fontes e limites

- [D2L1.0.3 §12.5.2](https://d2l.ai/chapter_optimization/minibatch-sgd.html),consulta textual parcial em27/10/2026: gradiente da média de minibatch. Dados, deduções de ponderação, exemplos escalares, figura e código próprios; sem copiar treinamento do livro ou seu conjunto de dados.
- [PyTorch2.14 DataLoader](https://docs.pytorch.org/docs/2.14/data.html),consulta textual parcial de batch_size/drop_last e aviso sobre iteráveis multiprocessados em27/10/2026. O endereço stable redirecionou para2.14. Não se afirma que essa versão esteja instalada nem se executa PyTorch. O script só particiona uma lista local em ordem, sem simular workers,samplers ou regras de distribuição.

As verificações não certificam desempenho, generalização, equivalência para qualquer rede ou domínio pessoal. Avaliação de rede,amostragem dependente,otimizadores com estado,acumulação distribuída e revisão pessoal permanecem pendentes.
