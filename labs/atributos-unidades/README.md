# Atributos, unidades e disponibilidade

Representação original de energia cinética clássica em movimento1D, massa positiva e velocidade com sinal. Dados prescritos da lei K=m v²/2, sem ruído, não são medições ou descoberta de pesquisa. Rascunho assistido por IA, revisão pessoal pendente.

Da raiz:

```sh
python3 -B -m labs.atributos-unidades.features
python3 -B -m unittest discover -s labs/atributos-unidades -t .
```

Reutiliza o ajuste afim racional de `labs/regressao-afim/ols.py` sem alteração. `feature` converte massa kg/g e velocidade m/s,cm/s,km/h para SI e retorna m v² em joules dimensionais, antes do fator1/2. A entrada speed é uma componente com sinal em1D; não aceita vetor3D. Todas grandezas numéricas usam int/Fraction, sem bool/float/texto. O código não identifica a unidade real de um número rotulado incorretamente.

Treino sintético(m,v,K):(1,2,2),(2,2,4),(1,4,8). Com φ=m v²:(4,2),(8,4),(16,8), ajuste K=wφ+b dáw1/2,b0,MSE0. Com v² apenas, a entrada4 tem alvos2 e4. A melhor reta nesses três pontos dáw5/12,b4/3,MSE2/3; nenhum preditor determinístico só de v² consegue duas saídas distintas na mesma entrada. Isso demonstra perda de informação neste desenho, não superioridade universal de engenharia manual. O novo estado m2,v3 dá9J no modelo compatível e61/12J na reta que omite massa; é teste algébrico, não validação de generalização em amostra real.

A conversão1000g,200cm/s dáφ4kg m²/s², mesmo que1kg,2m/s. Usar os números crus dáφ40000000, fator10^7; a transformação deve acompanhar treino e uso. A normalização por escalas físicas externas m0>0,v0>0 define π=(m/m0)(v/v0)² e E0=m0v0²; K/E0=π/2. Não é StandardScaler nem média aprendida no teste. Se escalas/atributos forem selecionados a partir de dados, sua escolha pertence ao treino/validação.

`feature_at` apenas verifica timestamps declarados, na mesma coordenada temporal, e pressupõe entradas já em SI. Inclui igualdade com instante de previsão; não verifica procedência, causalidade, atraso de sensores ou metadados falsos. Uma velocidade fornecida depois do evento é inválida para uma previsão anterior; a mesma velocidade pode ser válida em uma tarefa posterior de estimar energia no estado já observado. Um atributo derivado do alvo futuro não se torna disponível ao mudar seu nome.

Cinco testes incluem coeficientes/resíduos contra equações normais,54 equivalências de unidades,48 comparações adimensionais/sinal,tempos declarados e exemplos/contratos anteriores. Sem instalação/execução de scikit-learn ou novo motor de regressão. Limites relativísticos,ruído e inversão de velocidade não tratados;quadrado apaga sinal e não serve sozinho para prever velocidade assinada.

Fontes efetivamente consultadas30/10/2026:Bishop,PRML2006,§3.1pp138–139/PDF157–158,recorte textual sobre bases e linearidade nos parâmetros;sem nova inspeção visual ou leitura integral. scikit-learn1.9.1,Common pitfalls§§12.1–12.2.2,corpo parcial sobre consistência/disponibilidade/seleção no treino, https://scikit-learn.org/stable/common_pitfalls.html . Referência da lei cinética já presente nas aulas de mecânica,sem afirmar nova verificação experimental. Exemplos,figura e código locais;PDFprivado não distribuído.
