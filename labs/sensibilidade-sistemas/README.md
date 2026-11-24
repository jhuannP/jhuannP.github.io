# Sensibilidade de sistemas: resíduo não é erro direto

22/10/2026. Rascunho original preparado com apoio deIA, pendente de revisão pessoal. Não são dados físicos ou evidência de atuação em pesquisa/cliente.

## Família e hipóteses

A=c[[1,1],[1,1+δ]], b=c[2,2+δ], referência x*=(1,1). δ=10⁻ᵉ, e1..6; c=10ᵠ, q−3..3. Matriz inversível. Proposta manual, sem solver: direção0 x̂=(1+s,1−s); direção1 x̂=(1+s,1+s), s−1..1. Norma infinito vetorial e matricial induzida. Dados adimensionais.

O exemplo antigo c1/δ0,001/x̂(2,0), funções de norma/resíduo, dois IDs antigos e desafio foram preservados. Novo painel é conditionSensitivity, global ConditionSensitivityModels, sem sobrescrever o painel conditioning anterior usado no catálogo.

κ=(2+δ)²/δ. Na direção0: r=(0,cδs), ρ=δ|s|/(2+δ), ε=|s| e κρ=(2+δ)|s|. Na1: r=−cs(2,2+δ), ρ=ε=|s|, mesma matriz/κ e outra amplificação. Escala comum muda r absoluto e não as medidas relativas matemáticas. Cota não é erro realizado ou confiança estatística.

A curva compara valores analíticos em log10. Zero é informado sem logaritmo. A tabela separa resíduo analítico e avaliação direta emfloat. Diferenças pequenas podem resultar de arredondamento de dados/produtos/somas. Essa separação evita usar o cálculo do diagnóstico como verdade exata. Não há singularidade no domínio escolhido, SVD, estimador automático de condição, perturbação simultânea deA/b ou garantia de precisão.

No padrão: erro relativo1, r∞0,001, ρ1/2001, κ4004,001 e cota2,001. Um resíduo pequeno não exclui erro grande. Proposta satisfaz exatamente o lado direito b−r no modelo matemático; a leitura retroativa fixaA e não prova estabilidade de procedimento.

## Fonte consultada parcialmente

Burden, Faires e Burden, *Análise Numérica*, tradução da10ª edição norte-americana, terceira brasileira/Cengage2016. Exemplar privado da pasta Livros daIC, anteriormente identificado por folha/ficha. Neste bloco foram lidos visualmente trechos§7.1/pp.480–481(PDF493–494) e§7.5/pp.523–524(PDF536–537). Cabeçalhos impressos confirmados; não presumida a paginação por título de PDF homônimo. A leitura termina no começo da definição de condicionamento, sem completar as seções ou refinamento iterativo.

As páginas motivam definições e limites. Família, direções, curvas, redação, exercícios e código são próprios; não copiadas figuras, tabelas ou enunciados. PDF/imagens privadas não distribuídos. A sétima edição indicada pelo programa não é presumida equivalente à décima escolhida por Jhuann.

## Testes

Na raiz:

```sh
python3 labs/sensibilidade-sistemas/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:108estados contra frações exatas, inversa por produto identidade e solução do RHS perturbado; escala/direção; exemplo/avaliaçãofloat por outra ordem; domínio.54estados Python/JS cruzam métricas e resíduo avaliado. A comparação usa tolerância proporcional à escala e não exige igualdade de somas float com ordens diferentes. Provas da aula complementam testes, que não demonstram domínio pessoal.

## Composição e interação

Tese visual: uma figura de medidas relativas, com tabela numérica, torna comparáveis grandezas que diferem por ordens de magnitude. Plano: norma→cota→família→direções/escala→limites→prática. Quatro controles mudam sensibilidade, desvio, direção e escala. Curvas atualizam sem sugerir execução de solver ou aquisição de dados. Estilos de linha e legenda diferenciam séries além da cor; zero explícito.

## Pendências

Revisão, normas componente a componente, escalas não uniformes, estimadores sem inversa explícita, estabilidade e Gauss/pivotamento, refinamento e matrizes gerais. Nenhum grupo curricular concluído.
