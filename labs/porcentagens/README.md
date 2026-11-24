# Porcentagens sucessivas e inversas

Execute `python3 experiment.py`. Na raiz do protótipo, `python3 -m unittest discover -p 'test_*.py'` inclui quatro testes novos. `sequence` e `rate_back` usam Fraction para aritmética exata, sem arredondar as etapas. Taxas em unidades percentuais: 20 significa 20%, não 0,2.

Base inicial positiva e taxas a partir de −100%. Uma taxa de −100% zera o valor e não tem inversa multiplicativa finita. `summary` devolve `None` para a taxa de recuperação nesse caso. A soma simples das taxas coincide com o total em alguns casos (por exemplo, uma taxa zero), mas não é regra geral.

Testes independentes de identidade polinomial, escala, ordem dos fatores, inversas e domínio. Exemplo Decimal de arredondamento “meio para cima” em cada etapa: 0,02 com +20%/+50% resulta em 0,03, e ordem inversa em 0,04; sem arredondar, ambos dão 0,036. Isso é outro modelo, não o que o gráfico aplica. Os 75 casos de `reference.json` foram comparados ao JavaScript.

A aula foi ampliada preservando seu ID e os dois exercícios anteriores. A solução do desafio agora declara taxas em unidades percentuais, de acordo com as novas instruções. Não representa preços, aplicações, contratos ou condições de uma operação financeira real.

Fonte consultada em 16/10/2026: [IMPA/OBMEP, Porcentagem e Juros](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=26&tipo=1), página de apresentação e descrição dos fatores/mudanças sucessivas. Vídeos, caderno e material teórico não foram declarados integralmente estudados. Exemplos, explicações, código e exercícios originais; revisão de Jhuann pendente.
