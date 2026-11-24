# Quiralidade e sobreposição tetraédrica

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Na raiz: python3 -m unittest labs.quiralidade.test_experiment.

Modelo de tetraedro regular centrado, vértices (1,1,1), (1,-1,-1),
(-1,1,-1), (-1,-1,1). Grupos abstratos ABCD ou AACD.
Reflexão espacial, troca formal e rotação são operações geométricas;
a troca não representa mecanismo químico. Não há atribuição CIP/R/S,
rotação óptica, energia ou detector geral de quiralidade molecular.

χ é o determinante dos três vetores medidos a partir do quarto vértice.
Seu valor inicial é 16; reflexão ou troca invertem seu sinal, rotação
própria conserva. O sinal depende da ordem dos marcadores e não é R/S.
Com grupos iguais, a permutação de marcadores equivalentes pode mudar χ
sem representar outra configuração química.

A busca enumera as 24 correspondências e conserva só as que respeitam
as identidades dos grupos. Para cada uma constrói Q=Σ alvo*referênciaᵀ/4,
verifica ortogonalidade, determinante +1 e todos os vértices.
A classificação não é uma tentativa em alguns ângulos do controle.
O encaixe visual aplica Qᵀ ao alvo; não altera as operações nem χ bruto.
A figura é uma projeção 3D com ligações posteriores tracejadas.

Quatro testes: 24 permutações com produto misto independente e translação;
104 combinações de grupos, reflexão, troca e ângulo, com matriz própria;
rotação por quaternion racional independente; distâncias, simetria de AACD
no plano y+z=0 e contratos. As 104 referências também são conferidas em JS,
incluindo correspondência de grupos e encaixe dos quatro vértices.

Fontes parcialmente consultadas em 16/10/2026:
- Brown/Poon, Introduction to Organic Chemistry, sexta edição, Wiley 2016,
  seções 6.1/6.2, páginas impressas 161–163 (PDF 181–183).
  Página impressa 162 inspecionada visualmente. Paginação do exemplar inglês.
- [OpenStax 5.1](https://openstax.org/books/organic-chemistry/pages/5-1-enantiomers-and-the-tetrahedral-carbon).
- [OpenStax 5.2](https://openstax.org/books/organic-chemistry/pages/5-2-the-reason-for-handedness-in-molecules-chirality).

Desenho, exemplos e exercícios próprios. Pendentes: regras CIP, vários
centros, meso, conformações e análise de moléculas completas; revisão pessoal.
Uma aprovação curricular não comprova domínio deste material por Jhuann.
