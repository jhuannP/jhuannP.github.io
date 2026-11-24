# Resíduos, projeção e erro reservado

Laboratório original de revisão, preparado com IA; não é evidência de domínio pessoal, pesquisa ou desempenho de mercado. Dados sintéticos e adimensionais.

Reutiliza `labs/stump-regressao/stump.py` sem alteração: médias nas folhas, SSE, busca nos pontos médios, candidato constante e melhora estrita. Empates mantêm o primeiro candidato. O novo módulo acrescenta histórico racional e avaliação por rodada; não implementa árvores completas ou outras perdas. Somente inteiros/Fraction, 1–100 linhas, 0–50 rodadas, 0<eta<=1.

Na perda individual (y−F)²/2, o gradiente negativo é y−F. Para uma partição ajustada por médias, r·h=||h||². Portanto SSE_nova−SSE_antiga=−eta(2−eta)||h||². É uma identidade de treino, inclusive com correção zero; não garante melhora estrita ou generalização. O limite matemático 0<eta<2 dessa etapa fixa não amplia a API, que aceita até 1.

Treino x=(0,1,2,3), y=(0,0,2,2), eta=1/2: previsão à esquerda 2^(−M), à direita 2−2^(−M), MSE=4^(−M). O ponto reservado prescrito (x=3/2,y=1) tem erro (1−2^(−M))². É um contraexemplo construído, não amostra representativa: os dados de treino não determinam o valor no meio do intervalo. Se usarmos esse ponto para escolher rodadas, ele vira validação, não teste final independente. Não se implementa seleção automática ou alegação populacional.

Outro alvo y=(0,2,0,2) empata dois cortes; o primeiro 1/2 é mantido. A primeira correção dá previsões (1/2,7/6,7/6,7/6), MSE=3/4. Para x=(0,0), y=(0,2), nenhuma rodada pode separar alvos: MSE permanece 1.

Fonte primária: [scikit-learn 1.9.1, §§1.11.1.2.3–1.11.1.2.5](https://scikit-learn.org/stable/modules/ensemble.html#mathematical-formulation), corpo parcialmente consultado em 30/10/2026 para atualização, perda e passo. Sem instalar/executar scikit-learn ou copiar seus exemplos. Identidades, dados, figura e implementação locais.

Da raiz do protótipo:

```sh
python3 -B -m unittest discover -s labs/boosting-projecao -t .
python3 -B -m labs.boosting-projecao.stages
```

Cinco métodos: referência fechada e ponto reservado; 486 comparações de etapas por identidade e comparação adicional com motor float existente; empate/entrada sem informação; nove derivadas por diferença central exata; snippets/desafio antigos e contratos. Revisão conceitual pessoal pendente. Referências independentes são fórmula fechada e identidade de projeção, não só paridade entre implementações.
