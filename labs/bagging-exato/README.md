# Bagging exato: reamostras, médias e OOB

Laboratório próprio de regressão sobre treino sintético x=(0,1,2), y=(0,2,0). Enumera3³=27 sequências de índices, cada uma com peso1/27 no bootstrap empírico. Não são27 novos conjuntos de dados independentes de uma população real. O conjunto completo de possibilidades calcula a esperança condicional exatamente; não equivale a sortear27 reamostras independentes, que poderiam repetir possibilidades e omitir outras.

`ensemble.py` importa, sem alterar, `../stump-regressao/stump.py`, da aula de um corte. Requer manter essa disposição de pastas no protótipo. O algoritmo ajusta stumps de regressão com perda quadrática, folhas pela média, constante como candidato e primeiro corte que melhora estritamente em caso de empate. Código de classificação por votos da aula anterior preservado como demonstração separada. Nenhuma floresta completa, diversidade de atributos ou biblioteca externa instalada.

`bootstrap_models` aceita1…4 pares int/Fraction, exclui bool/float e enumera n^n ajustes. O limite é operacional para conter custo exponencial. Dados sem unidades físicas neste exemplo. `distribution` conta previsões em uma consulta; `mean_variance` calcula momentos populacionais dessa distribuição empírica, divisor27, não estimativa amostral com divisor26. `oob_predictions` recebe os modelos e o vetor original x, na mesma ordem, e usa somente reamostras que omitem cada índice original. Retorna(None,0) quando não há modelo elegível. Não é API de produção com rastreamento automático da procedência de argumentos.

Em x=1: valor0 ocorre8 vezes,1 ocorre6 e2 ocorre13. Média32/27; variância condicional542/729. Duas reamostras sorteadas independentemente, dado esse treino, têm média com variância271/729. Isso descreve variação do sorteio, não erro de generalização ou intervalo de confiança da previsão. A fonte de aleatoriedade é declarada antes de cada fórmula.

OOB: cada índice é omitido em8 modelos; médias em x=0,1,2 são7/4,0,7/4. O MSE com alvos0,2,0 é27/8=3,375. É uma conta exata desse exemplo pequeno, não uma estimativa universalmente não viesada de desempenho futuro. Os testes mudam o alvo da linha omitida e verificam que sua previsão OOB não muda. Nenhum pré-processamento aprendido globalmente é usado. Em aplicações, grupos, tempo, seleção repetida e transformações podem comprometer a interpretação; protocolo externo pode continuar necessário.

Para previsores de variância comumσ² e correlação comumρ, Var(média)=σ²[ρ+(1−ρ)/B]. A função `variance_factor` ilustra somente0≤ρ≤1 e B inteiro positivo. O toy independente de árvores usa Z_b=A+ε_b com sinais±1 independentes: variância individual2, covariância1, variância média1+1/B. Não é uma medida deρ das árvores do exemplo. Para sorteios independentes dado D, variância total=Var_D(μ_D)+E_D[v_D]/B; enumerar um único treino não estima a primeira parcela.

Da raiz do protótipo:
```
python3 labs/bagging-exato/ensemble.py
python3 -B -m unittest discover -s labs/bagging-exato -t .
```
Seis testes: fixture exata e stump original; dez vetores de contagem com pesos multinomiais comparados às27 sequências em sete consultas;729 pares de duas reamostras para média/variância; exclusão OOB e três mudanças de alvo; componentes compartilhados em B=1…4 por enumeração de sinais; contratos. Cálculo e integração verificados, sem validação pedagógica ou experiência pessoal certificada.

Fontes consultadas parcialmente em29/10/2026: Bishop, PRML,2006, §14.2, p655 início e pp656–657/PDF670–672. Cabeçalhos individuais confirmados, p656/PDF671 visualmente inspecionada para média e hipóteses. Primeira renderização tentouPDF674 e mostroup659/boosting; faixa corrigida após inspeção, sem usar conteúdo deboosting como fonte deste bloco. Não transplantar offset18 de outro registro: neste exemplar a paginação confirmada é+15. PDF privado não distribuído; exemplos/figura/código próprios, fórmulas padrão não reivindicadas como descobertas.

Breiman/Cutler, Random Forests, trechos de Overview e mecanismo OOB, consulta online parcial. Usados para procedimento de amostragem/atributos/exclusão, não para promessas universais de desempenho da página histórica. Artigo bagging.pdf não recuperado, portanto não lido nem usado como fonte.
https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm

Percurso complementar de machine learning, sem nova disciplina ou equivalência curricular formal. Sem dados de cliente, benchmark real, importância causal, probabilidade calibrada ou garantia de emprego/desempenho. Rascunho assistido por IA para revisão pessoal de Jhuann.
