# Gradiente linear: a curvatura limita o passo

27/10/2026. Aula em rascunho,12 seções/12 exercícios. Exemplos, prova, figura e verificações originais. Revisão pessoal de Jhuann pendente. Pré-requisitos: derivada, média, reta, MSE e sequência geométrica.

## Reconstruir antes de executar

Com x=(−1,0,1),y=(−1,1,3), abra a MSE média, sem fator1/2. Obtenha L=(2/3)(w−2)²+(b−1)². A centragem elimina o termo cruzado. Os fatores dos erros são1−4η/3 e1−2η. A condição de convergência para qualquer início é0<η<1. Para η=1, o erro do intercepto oscila sem diminuir; para1,1 cresce a partir do início zero. Isso não é prova para todos os modelos de ML.

No segundo bloco de20min, troque x por10x e declare w′=w/10. A curvatura da inclinação cresce cem vezes e o limite do passo comum cai para3/200. A transformação foi especificada, sem estimar médias ou desvios nem construir pipeline. Para reproduzir a mesma trajetória, só o passo da inclinação deve cair cem vezes; diminuir ambos os passos muda também o ritmo do intercepto.

## Laboratório

Execute `python3 labs/gradiente-curvatura/gradient.py` na pasta do protótipo. Usa Fraction e diferenças centrais exatas para quadráticas, não aproximações de precisão arbitrária ou autodiff. Compara iterações com formas fechadas e verifica a reparametrização com passos por coordenada. A atualização simultânea é contrastada com uma atualização sequencial no exemplo de um ponto. Um ponto não identifica dois parâmetros: w+b=2 tem infinitas soluções.

A figura mostra o erro do intercepto em seis iterações, preservando seu sinal. O painel interativo já existente mostra log10(MSE),com piso visual10^-12. Grandezas e pisos são distintos; o limite visual não certifica erro nulo ou precisão de parâmetros. Os dados são sintéticos, sem validação populacional.

## Fonte e limites

[Dive into Deep Learning1.0.3 §12.3](https://d2l.ai/chapter_optimization/gd.html), consulta textual parcial em27/10/2026 aos trechos12.3.1.1 e12.3.2, passo e gradiente multivariado. A prova exata usa os dados próprios do painel, sem copiar gráficos, código ou exercícios do livro e sem instalar/executar seus frameworks. Nenhum novo trecho de Bishop foi lido nesta rodada.

Batch completo, taxa constante e MSE linear sem ruído ou regularização. Queda de perda de treino não comprova generalização. Análise com minibatches, otimizadores adaptativos, redes não convexas, ruído e avaliação fora do treino permanece pendente. Material preparado não comprova domínio pessoal ou resultado em pesquisa/cliente.
