# Logística: probabilidade, perda e decisão

Rascunho original para revisão pessoal, 21/10/2026. Cinco pares sintéticos: x=(-2,-1,0,1,2), y=(0,1,0,1,1). O painel usa pesos manuais; não treina, calibra ou mede generalização. A consulta x destacada não modifica a coorte.

## Experimento

Na raiz do protótipo:

```sh
python3 labs/logistica-decisao/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

O teste local tem quatro métodos: probabilidades/perdas contra Decimal de 90 dígitos; gradiente contra diferença central independente; contagens manuais e invariantes do limiar; regra de custos e contratos. `reference.json` registra 135 combinações para confronto Python/JavaScript.

Com w=1,b=0, limiar 0,5: TN=1,FP=1,FN=1,TP=2. Com limiar 0,8: TN=2,FP=0,FN=2,TP=1. A acurácia permanece 3/5; precisão e revocação mudam. Probabilidades, log-loss média e gradiente não mudam. Empate recebe 1 nesta demonstração; não se afirma que todas as bibliotecas adotem essa convenção.

Para logits finitos, limiar zero prevê sempre 1 e limiar um sempre 0. A comparação ocorre nos logits, evitando decisões por probabilidade arredondada. Com w=0 a probabilidade é constante, sem fronteira única. Precisão é indefinida quando não há positivos previstos.

A perda é calculada por ramo do rótulo com log1p e sem cancelamento de termos grandes. O resíduo de y=1 usa −sigmoid(−z). Isso preserva valores pequenos em z=40, mas não elimina underflow em magnitudes arbitrárias. Rotinas antigas e exemplos da aula mantêm suas APIs. A perda usa média sem penalização, e não a soma da referência nem os padrões regularizados de bibliotecas.

O limiar por custos C_FP/(C_FP+C_FN) pressupõe probabilidades condicionais adequadas à população, erros com custos constantes positivos e acertos com custo zero. Não é um resultado empírico obtido destes cinco casos.

## Fontes e escopo da consulta

- Bishop, *Pattern Recognition and Machine Learning* (2006), §4.3.2, páginas impressas 205–206 (PDF 223–224 do exemplar privado). Consulta parcial; página 206 inspecionada visualmente. Apoio para Bernoulli, verossimilhança e gradiente. Normalização por média explicitamente adaptada. O livro não é distribuído neste site.
- [scikit-learn: limiar de decisão](https://scikit-learn.org/stable/modules/classification_threshold.html): distinção entre estimar probabilidades e decidir; seleção de limiar e risco de usar os mesmos dados de ajuste.
- [scikit-learn: calibração](https://scikit-learn.org/stable/modules/calibration.html): significado de frequência e limites de interpretar perdas como calibração isolada.
- [scikit-learn: regressão logística](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression): modelo binário e contexto de regularização. Não se reproduzem os padrões ou o solver do pacote.

Fontes públicas consultadas em 21/10/2026. Dados, sequência, código, exercícios e verificações são próprios. Ainda faltam ajuste regularizado, multiclasses, diagnóstico de calibração com amostra adequada, curvas de ranking e avaliação com divisão independente. Nada neste laboratório comprova competência profissional ou conclusão do percurso de ML.
