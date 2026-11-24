# Fotossíntese: estoques, carbono e energia

Rascunho original para revisão de Jhuann, sem evidência de experimento ou domínio pessoal. Recorte de fotossíntese oxigênica vegetal e assimilação pelo ciclo de Calvin. Não inclui C4/CAM, fotorrespiração, transporte detalhado ou regulação completa.

## Fronteira e cálculo

Entrada: estoques disponíveis em mol de CO2, NADPH e ATP; RuBP inicialmente disponível e regenerada. Saída: equivalentes líquidos de triose-fosfato, com custo 3 CO2, 6 NADPH e 9 ATP por mol. Isso é um orçamento reduzido, não uma equação química completa nem uma simulação temporal. Água, H+, Pi, ADP, NADP+ e intermediários não são estados do código.

O maior q viável satisfaz 3q≤C, 6q≤N e 9q≤A. Logo q=min(C/3,N/6,A/9): o mínimo é viável e qualquer valor maior viola ao menos uma restrição. Usam-se quantidades molares contínuas; não arredondar como se contássemos moléculas individuais. Atingibilidade pressupõe ausência de perdas e limitações não representadas. Para uma folha real o valor é apenas um teto condicionado.

Exemplo próprio: (C,N,A)=(9,18,18) mol → q=2 mol, consumo (6,12,18), sobras (3,6,0). Mais CO2 sozinho não resolve falta de ATP. Com ATP=27, q=3. A taxa de regeneração de ATP/NADPH e a luz não são calculadas.

## Execução e verificação

`python3 labs/fotossintese-estoques/budget.py`

`python3 -m unittest discover -s labs/fotossintese-estoques -t .`

Quatro testes: exemplo e empates; 343 estoques inteiros comparados com busca independente de candidatos em passos de 1/18 mol; escala e recurso não limitante; contratos. Frações verificam o modelo contábil, não fisiologia real. A grade de candidatos é exata nesse conjunto de estoques, não em entradas racionais arbitrárias.

## Fontes e autoria

Lehninger, Nelson e Cox, 6ª edição em português, Artmed 2014: consulta textual parcial em 29/10/2026 a p.780/PDF810 (fotossistemas), p.783/PDF813 (fluxo cíclico), trecho final p.784/PDF814 (água como doador) e pp.808–809/PDF838–839 (custo e regeneração). Sem nova inspeção visual ou leitura integral. OpenStax Biology 2e §8.3 consultado parcialmente na mesma data como apoio. Programa USP CCM0111: referência já conferida em 28/10; reabertura em 29/10 indisponível, sem atualizar versão ministrada.

Redação, exemplo de estoques, figura SVG, prova do teto, código e exercícios próprios com apoio de IA. Nenhum PDF privado é distribuído; não reproduzimos figuras, tabelas ou exercícios das fontes.

[OpenStax §8.3](https://openstax.org/books/biology-2e/pages/8-3-using-light-energy-to-make-organic-molecules)

## Próxima revisão

Reconstruir o trajeto dos elétrons e justificar o carbono da regeneração sem consultar a resposta. Depois aprofundar fotofísica, acoplamento e fotorrespiração, antes de tentar prever uma planta real. Esta aula não demonstra experiência experimental.
