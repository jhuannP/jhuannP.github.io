# Maturação B: filtro limitado de edição

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Na raiz: python3 -m unittest labs.maturacao-b.test_experiment.

Seis precursores fictícios, quatro elegíveis após checkpoint pesado estipulado.
L0 é inicial; L1/L2 são cadeias leves alternativas supostas funcionais, relativas
a cada precursor. Indicadores binários de reatividade são entradas, não afinidade
calculada, dados humanos ou uma tabela de probabilidades. Duas listas fictícias
de autoantígenos mudam esses indicadores. Nenhum painel é coestimulação.

Busca sequencial até primeiro s=0 no prefixo permitido, com reavaliação após
cada edição. Sem s=0: não resolvido; fora do checkpoint: nenhuma L testada.
Não resolvido não é uma previsão automática de apoptose ou anergia. Não se
calcula rearranjo inicial de DNA, produtividade leve, expansão, maturação
periférica, hipermutação, troca de classe, ativação ou resposta individual.
O limite de duas alternativas não é um limite biológico universal.

Padrão: C2 passa L0, C3 passa L1, C4/C5 não resolvidos; C1/C6 fora.
Passam 2/4 elegíveis (1/2) ou 2/6 iniciais (1/3). Não são eficácia imune ou
sobrevivência biológica. Com duas alternativas, C4 passa em L2; C5 permanece.

Quatro testes: 24 prefixos dos oito vetores binários contra conjuntos de índices
aceitáveis; seis coortes contadas independentemente; conservação da partição,
denominadores exatos, estabilidade ao ampliar orçamento, reavaliação, seleção
apenas visual e contratos. Trinta e seis referências Python/JS e 24 oráculos
de prefixos também no JavaScript. Testes não validam hipóteses como dados reais.

Fonte parcial: Janeway/Imunobiologia, oitava edição, Artmed 2014, original 2012,
seções 8.3/8.5/8.6: pp. impressas 282, 284–288 (PDF 301, 303–307), trechos
consultados em 16/10/2026; página 287 inspecionada visualmente. Não se copiam
figuras, modelos transgênicos, exercícios ou estimativas numéricas do livro.
[Janeway público, quinta edição](https://www.ncbi.nlm.nih.gov/books/NBK27089/)
localizado por busca indexada, sem alegar leitura integral ou paginação idêntica.
[Artigo de 1998](https://pubmed.ncbi.nlm.nih.gov/9763602/) localizado pelo resumo
indexado: edição em camundongos transgênicos. Abertura direta não devolveu corpo
útil; não foi usado para atribuir frequências à coorte ou generalizar a humanos.

Visual: leitura editorial, uma cadeia de três alternativas e tabela auditável,
azul somente para passos visitados/destaque. Conteúdo: sequência biológica,
hipóteses, exemplo, painel, código e prática. Interação: limite muda prefixo;
painel muda hipótese de reatividade; destaque revela um precursor sem mudar coorte.
Sem animação que sugira tempo físico. Teoria de maturação é mais ampla que o modelo;
revisão pessoal e mecanismos periféricos continuam pendentes.
