# Trocar uma coluna de uma base

Experimento original racional em R²: colunas ordenadas b1,b2, vetor v=α1b1+α2b2. Trocar a coluna j por v mantém uma base se e somente se αj≠0. A identidade det(nova)=αj det(antiga) fornece diagnóstico independente e reconstrói as colunas antigas. Não se calcula det de família abstrata de funções; a prova geral do princípio de troca está na aula.

Execute `python3 labs/troca-base/exchange.py` e `python3 -m unittest discover -s labs/troca-base -t .`. Sem dependências. Componentes int/Fraction de módulo até100,duas colunas,índice0 ou1,base original não singular. Testes finitos não provam teorema geral nem estabilidade em float.

Fonte complementar pública: Interactive Linear Algebra,GeorgiaTech,§2.7 Basis and Dimension,https://textbooks.math.gatech.edu/ila/dimension.html,consulta parcial29/10/2026 a definições,cardinalidade e Basis Theorem. Extração omite alguns símbolos matemáticos; não foi usada para conferir equações invisíveis. Dedução por troca,exemplo,colunas e código próprios; não copiadas figuras ou exercícios. Lima/IMPA2014 permanece referência temática do acervo já identificado,sem nova leitura de corpo neste bloco. ProgramaCCM0213 e status histórico mantidos conforme consulta28/10; versão ministrada não comprovada.

Quatro testes: fixture e troca proibida;1920 trocas válidas em48 bases inteiras com coordenadas prescritas/determinante/reconstrução e rejeições dos coeficientes zero;exemplo fracionário;contratos. Revisão pessoal pendente.
