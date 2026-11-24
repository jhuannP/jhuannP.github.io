# Unidade da avaliação: grupos e disponibilidade temporal

Material e exemplos originais, rascunho para revisão de Jhuann. Não são dados da IC, cliente ou pessoa real. Memorizador didático usa média por grupo visto e média global do treino para grupo desconhecido, ambos reajustados em cada fold. IDs de grupo fazem parte desta construção para evidenciar dependência; não é recomendação automática de atributo.

Exemplo g=A,A,B,B,C,C,y=0,2,8,10,16,18. Divisão primeira medida de cada grupo para treino/segunda para avaliação: previsões0,8,16 e MSE4. Leave-one-group-out: médias de fallback13,9,5; MSEs145,1,145 e MSE OOF reunido97. As perguntas de uso são diferentes; esse contraste não prova que qualquer split de linhas será otimista ou que97 estima qualquer população. Com tamanhos desiguais, média por linha e média por grupo não coincidem necessariamente.

Temporal: origens inteiras unitárias, rótulo da linha t disponível em t+h; ajuste em c após chegada dos dados carimbados c. Treino exige t<c e t+h<=c. Para n=10,c=8,h=2,size=2: treino0..6,purgo7,teste8..9. As previsões são emitidas em cada origem8 e9, com estado ajustado em8; não são duas previsões feitas ambas em8, pois a entrada de9 só chega em9. Disponibilidade real pode ter atrasos, revisões e janelas adicionais. Função própria, não réplica de TimeSeriesSplit/gap. Purgo por disponibilidade não comprova independência nem elimina toda autocorrelação.

Fonte primária: scikit-learn1.9.1, guia§3.1.2.4.1,§3.1.2.4.3 e§3.1.2.6.1, consulta textual parcial29/10/2026: grupos inteiros, leave-one-group-out e treinos temporais crescentes; https://scikit-learn.org/stable/modules/cross_validation.html . Equações/horários de disponibilidade, dados, resultados e código locais próprios. Nenhum código, figura ou exemplo copiado, sem instalar/executar scikit-learn. Versão do documento não afirma versão instalada.

Biblioteca padrão. Grupos textuais não vazios,1..100 linhas, valores int/Fraction. Índices únicos e treino/avaliação não vazios sem linhas compartilhadas. Tempo n2..100,h1..20,teste contíguo dentro do domínio e treino com ao menos um alvo disponível. Unidades de tempo são intervalos unitários assumidos; não há timestamps irregulares, ajuste de timezone, calendário, imputação ou construção real de atributos. Não existem validação aninhada, teste externo ou intervalos populacionais implementados.

Execute da raiz: `python3 -m unittest discover -s labs/tempo-grupos -t .`; `python3 labs/tempo-grupos/split.py`.

Testes: exemplo calculado independentemente;120 permutações de cinco linhas com invariância, partição e grupos disjuntos;270 cortes com disponibilidade, purgo e expansão; contratos. Conferir a média OOF por soma dos erros/n, não médias de folds sem seus tamanhos. Um split operacionalmente correto ainda precisa da pergunta científica e de hipótese sobre representatividade.
