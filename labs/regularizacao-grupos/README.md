# Regularização por grupos e regra de atualização

Laboratório original para acompanhar a aula existente; não é treinamento de produção, implementação de Adam ou evidência de generalização.

## Contratos

`penalty.py` usa inteiros e `Fraction`, sem floats/booleanos nas coordenadas. A máscara é uma sequência booleana de mesmo tamanho. λ e η são não negativos. A diagonal P deve ser positiva. As funções retornam valores novos, sem alterar entradas.

A penalidade é λ/2 vezes a soma dos quadrados das coordenadas incluídas. O exemplo usa dois pesos e um bias, máscara `(True,True,False)`. O bias pode mudar pelo gradiente dos dados; não recebe termo direto de regularização.

O passo acoplado é w−ηP(g+λm⊙w). O separado é w−ηPg−ηλm⊙w. Ambos usam w antigo; multiplicar o resultado já atualizado por um fator de decaimento é outra ordem de operações. A convenção do coeficiente deve ser explicitada ao comparar implementações.

Exemplo prescrito: w=(2,−1,3),g=(1,2,−4),η=1/10,λ=1/5,P=diag(1,1/4,2). Acoplado=(93/50,−209/200,19/5); separado=(93/50,−103/100,19/5). Com P identidade, as duas expressões coincidem. P fixo ilustra a álgebra e não simula o histórico adaptativo de Adam.

`quadratic` usa curvaturas positivas e objetivo separado do classificador: metade da soma a_j(w_j−t_j)² mais a penalidade. Curvaturas=(1,4,2), alvos=(2,−1,3),λ=1/2 e a máscara acima dão mínimo(4/3,−8/9,3), valor8/9. Não extrapolar convexidade para toda rede tanh.

## Executar

Da raiz do protótipo:

```sh
python3 labs/regularizacao-grupos/penalty.py
python3 -B -m unittest discover -s labs/regularizacao-grupos -t .
```

Cinco métodos de teste cobrem:

- 36 diferenças centrais racionais exatas da função quadrática e quatro pontos estacionários;
- 27 igualdades entre passos SGD simples, além do contraexemplo diagonal com valores literais;
- sete passos sem gradiente de dados, exclusão do bias e exemplos de oscilação/crescimento;
- gradiente completo da BCE média com L2 do snippet já existente:18 coordenadas em redes H=1 e H=3, comparadas a diferenças centrais com passo1e−5; diferenças entre gradientes λ=0 e1/8 conferidas em pesos/biases;
- contratos de tipos, dimensões, máscara e sinal.

Essas verificações auditam contas e código. Não selecionam λ nem medem desempenho em novos dados. O painel XOR, o código da rede e o desafio anterior foram preservados; a demonstração nova não altera seu treino.

## Fontes — 29/10/2026

- Bishop, Pattern Recognition and Machine Learning,2006,§5.5 pp256–258/PDF274–276: trechos de regularização/escala; Eq5.112 em p257/PDF275 inspecionada visualmente. Não há cópia de páginas ou figuras no servidor.
- [D2L1.0.3,§3.7.1](https://d2l.ai/chapter_linear-regression/weight-decay.html): leitura parcial de Eqs3.7.2–3.7.3 e convenções; sem exemplos/código copiados. A tentativa inicial do endereço antigo em chapter_multilayer-perceptrons falhou; a página atual abriu.
- [Loshchilov/Hutter,ICLR2019,arXiv1711.05101v3](https://arxiv.org/abs/1711.05101): PDF §2 pp2–3 consultado parcialmente em texto para comparação de atualizações. Abertura HTML falhou; não houve replicação de benchmarks ou certificação do comportamento de um framework instalado.

O percurso é complementar próprio, sem créditos ou disciplina Júpiter atribuídos. Estudo sistemático, revisão pessoal e validação pedagógica pendentes.
