# Texto, bytes e frações representadas

Rascunho original de ComputaçãoII. Execute `python3 representation.py`. Sem dependências adicionais ou arquivos externos. CPython3.14.5 neste Mac,radix2 e mant_dig53 explicitamente verificados;se outro formato aparecer,o teste numérico sinaliza a diferença em vez de presumir equivalência.

## Dois contratos de representação

UTF-8 estrito transforma valores escalares Unicode em bytes e permite voltar ao texto original. O domínio exclui surrogates isolados U+D800..U+DFFF,embora str Python possa contê-los. A função scalar_utf8 monta bytes por máscaras/deslocamentos,sem chamar encode. Os testes confrontam o resultado com encode/decode da biblioteca padrão para todos os1.112.064 valores escalares,sem generalizar para outra codificação ou para segmentação visual.

é precomposto:U+00E9,um ponto e bytes C3 A9. e+U+0301:dois pontos e bytes65 CC 81. NFC pode unificar as formas antes de codificar,mas não decodifica bytes de origem desconhecida nem remove acentos. Latin-1 interpreta E9 como é;UTF-8 o rejeita isolado. Decode com replace pode perder informação:FF vira U+FFFD e não volta ao byte original. O exemplo original de á foi preservado.

Um racional reduzido com expansão binária finita tem denominador potência de2,pois um número com q casas binárias é inteiro/2ᵠ. A recíproca também vale,mas não garante caber numa precisão fixa ou faixa limitada de expoentes. Em particular1/8 cabe exatamente neste float;1/10 não. A razão de0.1 é3602879701896397/2⁵⁵ e seu excesso sobre1/10 é1/(5×2⁵⁵). Fraction do texto decimal e Fraction do float são exatos para entradas diferentes.

Exibir0.1 não altera o valor armazenado.0.1+0.2 e0.3 são floats distintos neste ambiente. A tolerância do exemplo só declara uma comparação,não apaga erros ou corrige hipóteses. Em torno de2⁵³,o próximo float maior dista2:2⁵³+1 perde distinção na conversão,e2⁵³+2 continua representável. Inteiros Python não foram limitados a53 bits. Não implementamos IEEE754 completo,Decimal irrestrito,transmissão ou formatos de arquivo.

## Fontes parciais —27/10/2026

- Sedgewick/Wayne,Computer Science,exemplar copyright2017 (arquivo2016),§6.1 p.874/PDF895,introdução de representação/contexto;e apenas o parágrafo final de p.890/PDF911,sobre aproximação numérica. Não usamos os exemplos,código Java ou figuras dessa página para descrever float Python. Sem nova inspeção visual ou leitura integral;PDF privado não distribuído.
- [Python3.14,Unicode HOWTO](https://docs.python.org/3.14/howto/unicode.html),definições,codificação e UTF-8,recortes.
- [Python3.14,tutorial de ponto flutuante](https://docs.python.org/3.14/tutorial/floatingpoint.html),recortes de frações binárias,representação,exibição e comparação.

Online3.14.10 distinguido de execução3.14.5. Figuras,provas,casos,código e exercícios próprios;sem copiar um programa de codificação dos autores. Fonte curricular de ComputaçãoII não reaberta neste bloco;versão ministrada continua conforme limite do registro existente.

## Verificações e próxima ação

Cinco testes locais:todos os valores escalares UTF-8 contra biblioteca padrão;256bytes isolados e políticas de erro;normalização/tamanhos/surrogate;672racionais pequenos versus igualdade exata após conversão,a razão de0.1 e espaçamento em2⁵³;contratos. A enumeração cobre exatamente o domínio escalar especificado,mas não todas as sequências de bytes,formatos ou operações numéricas. Sem dados reais,medição física ou desempenho de produção certificados.

Em duas sessões de20min,reconstrua os bytes e a ida/volta estrita;depois prove o critério do denominador e compare valor pretendido/representado/exibido. Leitor de tela,Windows real e revisão pessoal pendentes.
