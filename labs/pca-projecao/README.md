# PCA: variação, reconstrução e estado aprendido

27/10/2026. Aula existente ampliada para16 seções/12 exercícios, em rascunho com apoio de IA; revisão pessoal de Jhuann pendente. Três seções, dois exercícios, exemplo diagonal, rotina2D, desafio e painel anteriores preservados. Novos dados, figura, contas e testes próprios. Percurso complementar, sem crédito formal ou domínio profissional certificado.

## Modelo e derivação

Dados xn em R², métrica euclidiana, mesma escala no exemplo sintético. Média de treino μ, centrados zn=xn−μ e S=(1/N)Σznznᵀ. Sem centralizar, segundo momento=S+μμᵀ. Para direção unitária u, escores tn=uᵀzn têm variância uᵀSu. S é simétrica semidefinida positiva por ser média de produtos quadráticos. Maximizar uᵀSu na esfera leva ao maior autovalor e sua direção própria. Escalonar colunas muda a métrica; não é feito automaticamente pela PCA.

Reconstrução xhat=μ+u(uᵀz); resíduo perpendicular. Pitágoras dá perda média=tr(S)−uᵀSu. Com dois autovalores λ1≥λ2, mínimo de reconstrução em uma dimensão éλ2. Essa perda de representação não é erro supervisionado de um alvo nem evidência causal.

Exemplo anterior(-1,-1),(0,0),(1,1) permanece com autovalores4/3 e0, reconstrução exata em uma direção, até sinal. Se as coordenadas forem diferentes unidades físicas, antes é preciso decidir métrica e escalas apropriadas.

## Exemplo novo original

Pontos(12,22),(8,18),(11,19),(9,21), média(10,20); centrados(2,2),(−2,−2),(1,−1),(−1,1). Somas quadráticas10 por coluna e cruzada6, divididas porN=4:

S=[[5/2,3/2],[3/2,5/2]].

Autovalores4 e1, direções(1,1)/√2 e(1,−1)/√2. Total5, fração retida4/5. Escores2√2,−2√2,0,0. Reconstruções dos dois últimos pontos(10,20); cada erro quadrático2, média total1. O escore zero não significa ponto original zero. Inverse de uma projeção reduzida não desfaz a perda de informação.

Novo ponto(14,20): subtrair média do treino produz(4,0), escore2√2, reconstrução(12,22). Recentrar só esse ponto produziria zero e mudaria o procedimento. Ajuste de média, escala e PCA deve ficar dentro de cada treino da avaliação, sem usar teste reservado.

Trocar u por−u inverte escores e preserva uuᵀ. S=cI dá direção não única; dados todos idênticos dão variância total zero e proporção0/0 indefinida(None no laboratório). Código anterior usa limiar absoluto1e−12 de degenerescência; depende da escala, sem certificação de multiplicidade matemática.

DivisorN−1 paraN>1 multiplica autovalores porN/(N−1), sem mudar eixos ou proporções. Já y→10y dá Snovo=[[5/2,15],[15,250]], mudando a direção. Padronizar é outra escolha. Relação com SVD em dados centrados nas linhas: S=XcᵀXc/N, direções nas colunas de V e λj=σj²/N. Não implementamos SVD geral/whitening.

## Contraexemplo supervisionado

Pontos(10,1),(10,−1),(−10,1),(−10,−1), alvo=sinal(y). S=diag(100,1); primeira componente retém100/101≈99,01%, mas pares de mesmo x e y oposto colapsam no mesmo escore. Um preditor determinístico que só vê esse escore não pode distingui-los. Exemplo de perda de informação do alvo, sem concluir que PCA sempre prejudique previsão.

## Código e painel

`pca.py` mantém a função PCA2D e auxiliar finite da aula, extraídas sem alteração. Ajuste continua float, com covariância divisorN e fórmula analítica de2×2. Função fit acrescenta verificação de estatísticas finitas e estado congelado Model, com tuplas para média, direção e autovalores. Transform e inverse usam o mesmo estado. Entradas do ajuste são convertíveis para float real finito; bool, nan/inf e dimensões inválidas são rejeitados. Escalas extremas podem falhar ou perder precisão; não é solver numérico robusto geral. Autovalores pequenos podem sofrer arredondamento e o limiar de degenerescência permanece absoluto.

Referência exact_covariance aceita apenas int/Fraction sem bool; suas médias e matriz são racionais. Não substitui o ajuste por eigendecomposição exata. Explained_ratio retorna None se o total não é positivo; isso não inventa uma fração para variância zero. Métodos não alteram o estado e a validação verifica imutabilidade/reuso.

O painel preservado usa cinco pontos diferentes e média(0;0,08),com controle do ângulo de projeção; não representa o exemplo novo de quatro pontos. Conferir seus números segundo a própria nuvem. A figura estática é do exemplo novo e não usa dados de cliente/pesquisa.

Da raiz: `python3 -m unittest discover -s labs/pca-projecao -t .`.

Cinco testes: referência racional e reconstrução;361 direções comparando variância projetada com forma quadrática; sinal/translação/mudança de unidade; estado fixo, novo ponto, degenerescência e contraexemplo supervisionado; contratos/overflow. Testes finitos não certificam generalização, causalidade ou precisão para dados arbitrários.

## Fontes e paginação

Bishop,Pattern Recognition and Machine Learning,2006. §§12.1.1–12.1.2 pp.562–565/PDF578–581 parcialmente consultados em27/10/2026; p.562/PDF578 visualmente conferida. Correspondência conferida diretamente para este trecho, sem aplicar offsets de outros capítulos. Sem leitura integral do capítulo, reprodução de figuras, exercícios ou dados do livro. Arquivo privado não distribuído.

[scikit-learn — §2.5.1.1 PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca),consulta parcial27/10/2026: aprendizagem de componentes e centralização sem escalonamento automático; página exibe1.9.1. Pacote não instalado/executado, sem afirmar identidade entre nosso código e a biblioteca. Fonte principal para derivações foi o livro, com exemplos novos originais.

## Respostas e revisão

Respostas dos12 itens:0; não;10;3/2;4;4/5;1;2√2; sinais dos escores com projeção igual; proporção indefinida; estado do treino; variância alta não preserva o alvo. Dicas e resoluções completas na aula.

Duas sessões propostas de20min: μ,S,projeções e erro; depois estado no teste, escalas e contraexemplo. Dúvidas e avaliação pessoal em branco. Pendentes: PCA/SVD robusta em dimensão maior, outliers, dados ausentes, seleção de componentes, avaliação real e revisão pessoal.

Conferência da entrega: cinco testes locais e14 de catálogo aprovados;736 estruturas MathML verificadas. Em390px, exercício11 rejeitou recentrar teste e aceitou estado do treino pelo Enter. Painel preservado alterou o erro de0,02829 em30° para0,7336 em0° via Home; sua nuvem de cinco pontos é distinta do exemplo novo. Figura inspecionada, sem transbordamento ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
