# Regra da alavanca em base molar

Rascunho original22/10/2026, revisão pessoal pendente. Aula `q2-regra-alavanca`:14seções/12exercícios, duas fórmulas MathML e painel próprio. Primeiro recorte de fases/diagramas binários, não conclusão do tema.

## Fonte e limites

Levine, *Physical Chemistry*, sexta edição/McGraw-Hill2009, §12.6 pp.364–366 (PDF382–384): consulta parcial a linha de coexistência, distinção composição global/fases e derivação da regra da alavanca. Extração exploratória PDF379–385incluiu trechos vizinhos, sem declarar leitura integral. Extrator emitiu avisos de fontes; o texto conceitual e balanços usados ficaram legíveis. Não reproduzimos figura, dados, exemplo ou solução da referência. Nenhum PDF privado distribuído.

## Modelo

Binário A/B, sem reação, fechado a T/P fixados. Extremos sintéticos x_Bα=1/5 e x_Bβ=4/5 fornecidos, sem função de Gibbs ou estabilidade calculada. z=n_B/n. n=nα+nβ e nz=nαx_Bα+nβx_Bβ. fα=(x_Bβ−z)/(x_Bβ−x_Bα); fβ=1−fα. Válido com quantidades não negativas só para z em[1/5,4/5]; ambas positivas apenas no interior. Fora da faixa, quantidades retornam None/null; não se escolhe outro estado estável por extrapolação. Composição da fase ausente é apenas extremo limite fornecido.

Base molar: a barra usa nα/n e nβ/n, não volumes ou massas. Em z=1/2,n=5mol, nα=nβ=2,5mol; n_Bα=0,5mol,n_Bβ=2mol. Quantidade da fase não é quantidade de B nela. Hipótese ilustrativa M_A=10/M_B=30g/mol dá massas médias14/26g/mol; quantidades molares iguais têm fração mássica de α=0,35.

Tese visual: linha de composição e barra de quantidades em linhas separadas, com tabela exata e unidades. Conteúdo: z,total,esquema,balanços. Interação: variar z altera pesos sem mover extremos; variar total escala mols sem alterar frações. Fora da faixa, não desenhar barra negativa. Sem animação ou aparência de diagrama T–x.

## Verificação

Quatro testes: contagem independente de pacotes com4A+1B e1A+4B; balanços de A/B/total e escala em305estados; extremos/40composições fora da faixa; contratos.63referências por solução racional dos balanços2×2via determinantes cruzadas com JS. Biblioteca padrão apenas.

Execute `python3 -m unittest discover -s labs/regra-alavanca -t .`, `node test_simulations.cjs` e `node test_math.cjs` na raiz.

Próxima revisão pessoal: reconstruir n_B sem confundir com nβ e explicar base molar/massa. Construção de diagramas, regra de fases completa, dados reais e previsão de estabilidade permanecem pendentes.

Verificação final:728testes Python,271demos/813cenários básicos e comparações adicionais,420MathML e12testes de catálogo aprovados. Browser conferiu escala, extremo, composição externa e resposta7/20;390px sem overflow horizontal e console sem erros observados. Prévia `regra-alavanca-mobile.jpg` na raiz; viewport restaurado. Rascunho para revisão pessoal; saldo76%, parada65%.
