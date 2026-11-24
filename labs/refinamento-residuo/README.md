# Refinamento e qualidade do resíduo

Laboratório original, racional, 2×2. Execute `python3 -m unittest discover -s labs/refinamento-residuo -t .` e `python3 labs/refinamento-residuo/refine.py` na raiz do protótipo. Sem dependências externas.

A=[[4,1],[1,3]], b=[1,2], x*=[1/11,7/11]. `step` aplica x+B(b−Ax+η). B=A⁻¹ dá solução em um passo com resíduo exato. B=I/4 dá T=I−BA=[[0,−1/4],[−1/4,1/4]], norma infinito 1/2; B=I pode aumentar o erro. Não há fatoração reutilizada ou implementação LAPACK aqui. A inversa 2×2 por adjugada é apenas um oráculo didático; sistemas grandes pedem resolução por fatores, não inversa explícita.

`quantize` é uma grade racional com empate para par: não modela arredondamento relativo IEEE, produtos ou armazenamento de um solver real. η prescrito é perturbação artificial do resíduo; não uma distribuição ou medição de erro de máquina. Int/Fraction, módulos de entrada/resultado validados até1000, inversas rejeitadas se ultrapassarem esse limite; dimensão fixa2. Fraction não sofre arredondamento float, mas o tamanho dos inteiros pode crescer; não é solver de produção.

Fonte complementar: Demmel et al., *Error Bounds from Extra Precise Iterative Refinement*, LAPACK Working Note165, 8/2/2005, https://www.netlib.org/lapack/lawnspdf/lawn165.pdf. Leitura parcial da introdução p.3/PDF3 em29/10/2026, algoritmo1 e distinção de precisão do resíduo. Fonte usa r=Ax−b e subtrai a correção; notas usam r=b−Ax e somam. Não foi reproduzida a análise de erro, resultados experimentais ou rotina do artigo. Burden10ª permanece referência temática; nenhuma nova leitura do exemplar privado neste bloco. Programa oficial e histórico mantidos, sem nova consulta à versão de turma.

Verificações: exemplo racional, 289 direções de erro e cota, aumento e piso por resíduo perturbado, sistemas não singulares/escala por oráculo independente, contratos. Testes não certificam estabilidade geral nem domínio pessoal. Rascunho para revisão de Jhuann.
