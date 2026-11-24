# Um corte de regressão auditável

Material original em rascunho,28/10/2026. Referência parcial: scikit-learn, guia1.10.7/1.10.7.2, https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation . Consulta pública em28/10/2026,página exibida1.9.1: partições, ponderação e média/SSE. Não foi instalado ou executado o pacote; algoritmo, dados, deduções, figura e testes próprios,sem equivalência completa com DecisionTreeRegressor.

Da raiz: `python3 -m unittest discover -s labs/stump-regressao -t .`; `python3 labs/stump-regressao/stump.py`.

Um atributo, dados racionais completos, no máximo100linhas; SSE não normalizada, interceptos constantes nas folhas. Candidato constante sempre permitido; cortes somente entre valores distintos, mínimo de linhas por folha. Empates preservam o candidato anterior: constante primeiro,depois limiares crescentes. Sem pesos, ausentes, poda, múltiplos atributos, profundidade ou avaliação externa. Dados sintéticos não pertencem à pesquisa ou a cliente.

Testes:243combinações de alvos/folha mínima contra enumeração independente por previsões,24permutações,escala afim do alvo,fixtures e contratos. Frações exatas não certificam performance ou estabilidade do script flutuante anterior,que permanece como exemplo separado. O limiar médio não identifica fronteira causal entre observações.

Revisão20min: calcule os três custos26/3,5,2 e o custo constante14; depois imponha duas linhas por folha e explique por que muda a escolha. Revisão pessoal, teste externo, árvores completas e custo assimétrico ficam pendentes.
