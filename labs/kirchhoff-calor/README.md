# Capacidades caloríficas e Kirchhoff

22/10/2026. Rascunho didático original, preparado com apoio de IA e pendente de revisão pessoal. Não há substância real, experimento de bancada ou dado de pesquisa de Jhuann.

## Modelo

Duas formas isoméricas hipotéticas A/B, mesma composição, reação 1:1 A→B, mesma fase no intervalo250–650K, pressão padrão1bar. Referência300K: hA=0 e hB=2kJ/mol. Cp,A=40+0,02(T−300); Cp,B=b constante20..60, em J/(molK). Ambas positivas no intervalo. Os números são estipulados, sem ajuste a dados reais ou alegação de plausibilidade para molécula identificada.

O código integra capacidades separadamente para obter hA/hB e compara a diferença com um caminho que retorna A à referência e aquece B. Conversão J→kJ explícita. O modelo menos a aproximação de ΔrCp congelado na referência é−0,01(T−300)²/1000kJ/mol. Diferença nula em300K não valida a aproximação em outro estado.

O painel tem controles de T, b e vista Cp/entalpia. Alterar b troca a hipótese de substância, sem representar uma transformação temporal. Curvas não são mecanismo, perfil de ativação ou calor medido. ΔrCp pode ser negativo sem nenhuma capacidade individual negativa. Entalpia não determina rapidez ou espontaneidade. Fases, Cp/Cv geral, mistura, pressão variável, incerteza e dados reais permanecem fora do recorte.

No padrão T500K/b30: hA8,4; hB8; ΔrH−0,4kJ/mol. Cp,A44, Cp,B30 e ΔrCp−14J/(molK). Aproximação constante dá0. Caminho de estados:−8,4+2+6=−0,4. Para extensão2mol da reação escrita, ΔH−0,8kJ; só identificar com calor sob condições de balanço declaradas na aula.

## Fonte consultada parcialmente

Levine, *Physical Chemistry*, sexta edição, McGraw-Hill2009, exemplar privado autorizado. Trechos do §2.6: pp.53–54/PDF71–72, leitura por extração. §5.5: p.151/PDF169, lida e visualmente inspecionada. A correspondência foi conferida no corpo, sem presumir a partir do sumário. P.152/PDF170 foi lida exploratoriamente, sem usar tabelas, exemplos, exercícios ou coeficientes. Páginas vizinhas52/55 foram extraídas, mas não sustentam cobertura de outros tópicos. Metadados da edição já reconferidos no bloco anterior; nome do arquivo2008 diverge do copyright2009.

A referência motivou os conceitos; dados, redação, desenho e exercícios são próprios. PDF privado e imagem da página não estão na raiz pública ou nos downloads. O programa CCM0124 disponível é de ativação2025, posterior à turma2024: não comprova o conteúdo efetivamente ministrado.

## Verificação

Na raiz do protótipo:

```sh
python3 labs/kirchhoff-calor/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:153 estados contra trapézio independente em frações exatas; composição/reversão de integrais e derivada numérica local; referência/unidades/exemplo; domínio. Trapézio é exato apenas porque Cp é linear neste modelo.81estados Python/JS cruzam capacidades, entalpias, aproximação, erro e caminho. O contrato recusa extrapolação, valores não finitos e intervalos com Cp não positivo.

Testes verificam consistência do modelo e não uma propriedade de um composto real, adequação de um ajuste ou competência pessoal. Integrar um polinômio fora do domínio não fornece validade científica.

## Composição e interação

Tese visual: uma curva central com eixos legíveis, acompanhada de tabela de unidades. Sequência: conceito → integral → balanço de reação → contraste de aproximações → código/prática. Interações: temperatura move o ponto; capacidade de B modifica as curvas; vista alterna observável e unidade, sem animar um tempo inexistente. Mantida a composição editorial da biblioteca.

## Pendências

Revisão de Jhuann, capacidades reais e seus intervalos, Cp/Cv geral, transições e entalpias latentes, condições de pressão, análise de incerteza. Não declarar o item2 ou a disciplina completos.
