# Proporções: qual relação permanece?

Rascunho original22/10/2026, revisão pessoal pendente. Aula existente `em-proporcoes` de3/2para14seções/12exercícios, quatro MathML; preserva IDs, exemplo dos cadernos e desafio de trabalho ideal. Reforço escolar, sem equivalência de disciplina ou matriz de exame; Python opcional.

## Fonte e autoria

[OpenStax, Elementary Algebra2e §8.9](https://openstax.org/books/elementary-algebra-2e/pages/8-9-use-direct-and-inverse-variation), consulta parcial em22/10/2026 às definições, constante e método de variações direta/inversa. Definições orientam a aula; exemplos, valores, contraste afim, exercícios, código e gráfico próprios. Nenhuma figura, questão ou solução da fonte reproduzida.

## Modelo e visual

Três funções adimensionais:4x,24/x,6+4x. No painel x=1..6em passos de1/2; tabela avalia x e2x, com valores até12fora da janela. Azul contínuo:direta; preto tracejado:inversa; pontilhado:taxa fixa. Gráfico x0..6,y0..32; inversa desenhada de0,75a6porque abaixo de0,75fica acima da janela vertical. x0é indefinido na inversa, não concentração ou valor zero. Pontos marcam entrada escolhida, não dados.

Tese visual: três formas em um eixo comum, distinguíveis por traço e tabela. Conteúdo: um controle, gráfico, tabela de duplicação e razão/produto. Interação: teclado muda x e permite testar invariantes; domínios da fórmula não são confundidos com a janela. Sem animação decorativa.

Direta mantém y/x=4 e duplica saída ao duplicar entrada; inversa mantém xy=24 e reduz à metade. Taxa fixa tem diferença constante por unidade, mas razão variável e y(2x)−2y(x)=−6. Modelos de preço/trabalho exigem hipóteses e unidades próprias; não são ofertas ou previsões profissionais.

## Verificação e continuação

Quatro testes: invariantes/duplicação em11entradas; contagem independente de itens/tarefas em6entradas inteiras;55pares que distinguem razão constante, produto e taxa; contratos.11referências racionais com três modelos e cinco grandezas cruzadas com JavaScript. Python aceita int,float ou Fraction compatíveis com a grade, sem bool/NaN/infinito.

Execute `python3 -m unittest discover -s labs/proporcoes-modelos -t .`, `node test_simulations.cjs`, `node test_math.cjs` na raiz.

Próxima revisão pessoal: justificar o modelo antes do produto cruzado e dar um contraexemplo com taxa fixa. Proporção composta, dados reais e teste com aluno continuam pendentes.

Verificação final:732testes Python,272demos/816cenários básicos e comparações adicionais,424MathML e12testes de catálogo aprovados. Browser verificou duplicação na janela e fora dela, respostas1/2e1440,390px sem overflow horizontal e console sem erros observados. Prévia `proporcoes-modelos-mobile.jpg` na raiz; viewport restaurado. Rascunho para revisão pessoal; saldo76%, parada65%.
