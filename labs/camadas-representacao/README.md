# Composição e representação

Material original, rascunho para revisão de Jhuann. Convenção de vetores-coluna: W1 é Hxd, W2 é oxH. Colapsar afins produz W2W1 e W2b1+b2, nunca omitir o bias propagado. O código recebe int/Fraction e matrizes retangulares não vazias até4x4; rejeita bool/float e incompatibilidades, sem truncamento por zip. Aritmética racional, sem framework ou treinamento; dimensões limitadas por didática, não suporte a batch, tensores gerais ou diferenciação automática.

Exemplo afim próprio: W1=((1,2),(-1,1)),b1=(1,-2),W2=(3,-2),b2=4; mapa final5x1+4x2+11. Em x=(2,-1),h=(1,-5),z=17.

Construção ReLU independente da MLP tanh existente: h=(ReLU(x1-x2),ReLU(x2-x1)),z=2(h1+h2)-1. Nos vértices binários os scores são−1,+1,+1,−1. Em todo[0,1]^2,z=2|x1-x2|−1, mas só os quatro vértices têm rótulo XOR especificado. Limiar positivo classifica os quatro; sigmoide dos scores finitos não produz probabilidades exatas0/1. Pesos escolhidos analiticamente; não alegar convergência de treinamento, cobertura de domínio físico ou generalização.

Fonte primária: Dive into Deep Learning1.0.3,§5.1.1.3,Eqs.5.1.1–5.1.3 e definição ReLU§5.1.2.1, consulta textual parcial29/10/2026, https://d2l.ai/chapter_multilayer-perceptrons/mlp.html . Fonte usa minibatch em linhas; aqui usamos um exemplo em coluna, com produtos na ordem correspondente. Não copiamos código, figura, exercício ou experimento da fonte; prova da impossibilidade afim para os quatro rótulos e exemplos locais próprios. Não foram consultados teoremas de aproximação universal em detalhe.

Execute da raiz: `python3 -m unittest discover -s labs/camadas-representacao -t .`; `python3 labs/camadas-representacao/layers.py`.

Quatro testes: exemplo afim e25 entradas com oráculo escalar;64 combinações de formas e associatividade de três mapas;441 pontos comparados com fórmula absoluta independente, quatro vértices, teste de ponto médio e cancelamentos; contratos. A malha confere implementação, não substitui prova. Não linearidade pode cancelar e não garante por si só função final não afim.
