# C₂v: operações, matrizes e permutações

Execute `python3 experiment.py`. Na raiz do protótipo, `python3 -m unittest discover -p 'test_*.py'` inclui quatro testes deste laboratório. Sem rede, dependências ou cálculo eletrônico.

AB₂ ideal: A=(0,0,0), B₁=(1,0,1), B₂=(−1,0,1), coordenadas adimensionais. Plano molecular xz e eixo principal z. Geometria inspirada em moléculas angulares como água, sem representar seu ângulo de ligação medido. A/B são tipos genéricos e B₁/B₂ são etiquetas de núcleos equivalentes.

Índices: 0 E, 1 C₂(z), 2 σ(xz), 3 σ(yz). Vetores coluna. `compose(a,b)` aplica b primeiro, depois a. Tabela com A nas linhas e B nas colunas:

| A após B | E | C₂ | σxz | σyz |
|---|---|---|---|---|
| E | E | C₂ | σxz | σyz |
| C₂ | C₂ | E | σyz | σxz |
| σxz | σxz | σyz | E | C₂ |
| σyz | σyz | σxz | C₂ | E |

Testes: 16 pares, 64 trios associativos, identidade/inversos, produtos por matrizes completas independentes e preservação das distâncias. A permutação dos núcleos é não fiel: E e σxz têm a mesma ação nos lugares dos três núcleos, mas matrizes e ação no vetor (1,2,3) diferentes. `reference.json` contém 16 casos comparados ao JavaScript.

Fontes e acervo conferidos em 16/10/2026:

- [Júpiter CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214): consulta direta; simetria/grupos no início do programa, ativação 15/07/2024. Não reconstitui execução da turma.
- [Newcastle, exemplo da água](https://www.staff.ncl.ac.uk/j.p.goss/symmetry/Water/water0.html): consulta direta, operações C₂v e ambiguidade dos nomes xz/yz sem convenção explícita.
- Miessler, Fischer e Tarr, Química Inorgânica, quinta edição brasileira de 2014: exemplar identificado anteriormente no acervo; sumário conferido neste bloco inclui elementos/operações de simetria. Não foi declarado capítulo integralmente lido.

IUPAC Gold Book e USC apareceram nas buscas, mas não abriram diretamente; não foram apresentados como leitura integral. Texto, exemplos, desenho e código originais com auxílio de IA, ainda sem revisão pessoal. Não usa imagens ou exercícios copiados. Não implementa grupos gerais, representações irredutíveis, modos, orbitais ou espectros.
