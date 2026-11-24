# Separação e vazamento por imputação

Rascunho original22/10/2026, revisão pessoal pendente. Aula `ml-separacao-vazamento` de3/2para14seções/12exercícios, três MathML; mantém IDs sv1/sv2, exemplo de IDs e desafio anteriores. Não altera APIs de escalonamento/pipeline nem treina estimador.

## Protocolo e dados

Imputação indutiva com teste reservado. Treino x=[0,2]; teste tem q observado e um atributo ausente. Regra de decisão fornecida antes:classe1 se x≥2. O rótulo do observado é int(q≥2); o do ausente é escolhido0/1. Dados inventados para isolar o efeito, não um conjunto de validação real. Rótulos são usados apenas no score.

Estado só treino:μ=1, prevê0 para o ausente. Estado com teste:μ=(2+q)/3; prevê1 se q≥4. Em q8, rótulo ausente1 melhora acurácia de1/2para1; rótulo0piora de1para1/2. Para outras entradas pode empatar. Em q1, até os estados numéricos coincidem, mas o fluxo de informação continua diferente. Não prometer que todo vazamento sempre aumenta toda métrica. Acurácia de dois registros não estima generalização.

Classificador não treinado, ausência não descartada, sem seleção de modelo ou CV implementada. Reajuste planejado em treino+validação pode fazer parte de um protocolo com teste final separado; isso não autoriza fit no teste. Outros protocolos exigem hipóteses próprias e não são simulados.

## Fontes

- [Práticas e vazamento scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html), consulta parcial22/10/2026: aprendizado de transformações e dados reservados.
- [Validação cruzada scikit-learn](https://scikit-learn.org/stable/modules/cross_validation.html), consulta parcial22/10/2026: seleção e avaliação.
- Bishop PRML2006§1.3pp.32–33/PDF51–52, leitura parcial registrada no bloco anterior; sem nova leitura integral ou reprodução.

Experimento, números, código, exercícios e gráfico próprios. Nenhuma figura/dado da fonte copiado; nenhuma biblioteca instalada. Não confundir exemplos de biblioteca padrão com a implementação scikit-learn ou versão web com runtime local. Sem dados privados.

Tese visual: estado constante só treino e estado dependente do teste compartilham eixos; limiar pontilhado separa cálculo e decisão. Conteúdo: dois controles, curva, dados, tabela e limite. Interação: q altera só o estado contaminado; rótulo altera pontuação sem alterar imputação. Não há trajetória temporal ou animação de treinamento.

## Verificação e continuação

Quatro testes:22cenários por materialização dos dois registros e contagem; rótulo sem influência em estados e inclinação de1/3em q; score melhor/pior/igual e empate no limiar; contratos.22referências racionais cruzadas com JS.

Execute `python3 -m unittest discover -s labs/vazamento-imputacao -t .`, `node test_simulations.cjs`, `node test_math.cjs` na raiz.

Próxima revisão pessoal: prever quais valores mudam quando q muda e quando muda só o rótulo. Próximo aprofundamento local: estados reais de escalonamento/pipeline e validação por divisão; grupos/tempo, validação aninhada e generalização científica permanecem pendentes.

Verificação final:740testes Python,274demos/822cenários básicos e comparações adicionais,431MathML e12testes de catálogo aprovados. Browser confirmou rótulo sem mudar curvas, score invertido, q0/tieq4, respostas10/3e1/2;390px sem overflow horizontal e console sem erros observados. Prévia `vazamento-imputacao-mobile.jpg` na raiz; viewport restaurado. Rascunho para revisão pessoal; saldo75%, parada65%.
