# Definir tarefa,perda e referência

30/10/2026. Material original em rascunho para revisão.

Regressão,constantes ajustadas em treino. Média minimizaMSE pela identidadeMSE(c)=MSE(média)+(c−média)². Mediana minimizaMAE por pareamento dos extremos;em npar a implementação escolhe a inferior. Métricas emU²/U se alvos emU. Não é alegação de melhor regra em população futura.

Treino sintético[2,2,8]:média4,MSE8,MAE8/3;mediana2,MSE12,MAE2. Teste[5,7]:média do treino4 congelada dáMSE5. Ajustar6 aos próprios alvos de teste dáMSE1,mas é avaliação contaminada. Mediana do treino temMAEteste4,enquanto média4temMAEteste2;minimizador empírico não garante vitória fora do treino.

A API separa ajuste e avaliação,mas não detecta origem/instante de dados. Cliente pode fazer uso indevido;registro de procedência é parte do protocolo. Entradas int/Fraction,1..1000alvos,sem bibliotecaML. Nenhuma validação real de produto,pesquisa ou pessoa.

Fontes:Bishop2006,PRML§1.5.5pp46–48/PDF65–67,consulta textual parcial30/10/2026;p46/PDF65ep48/PDF67visuais. Offset19aqui,distinto de trechos posteriores. PDF61era42,não46. Sem cópia de figura/atividade/PDFprivado. [scikit-learn12.2](https://scikit-learn.org/stable/common_pitfalls.html)consultado parcialmente,vazamento;sem usar exemplos da documentação. Derivações finitas,dados e figura locais.

```sh
python3 labs/baseline-tarefa/baseline.py
python3 -B -m unittest discover -s labs/baseline-tarefa -t .
```

Cinco testes: referência/heldout;125amostras×7constantes para identidadeMSE/MAE;intervalo de medianas pares;escala/unidade/deslocamento e material anterior;contratos. Revisão pessoal20min: justificar objetivo e explicar melhoria aparente5→1sem chamá-la de generalização.
