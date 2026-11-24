# Raiz e majorante geométrica

Material original, rascunho para revisão de Jhuann. Índices n>=1; a_n=2^(−n) se n par,3^(−n) se n ímpar. As raízes são exatamente1/2 e1/3; a sequência de raízes não tem limite, mas a_n<=2^(−n) para todo n. Não atribuímos ao teste na forma de limite uma hipótese que o exemplo não satisfaz: usamos a majorante direta que sustenta a prova. Uma apresentação geral por limsup permanece para aprofundamento futuro.

Separar índices pares/ímpares dá S=1/3+3/8=17/24. Após somar atéN,a cauda começa emN+1. Majorante R_N<=2^(−N). Para tolerância1/100,primeiro índice garantido por essa cota é7;isso não é o primeiro índice do erro verdadeiro,pois R_6=1/192+1/1944<1/100 enquanto cota_6=1/64>1/100. Código calcula a cauda por duas geométricas exatas e compara com soma total menos soma parcial nos testes.

Fontes: OpenStax Calculus2§5.6, Teorema5.17 e contexto do teste da raiz, consulta textual parcial29/10/2026, https://openstax.org/books/calculus-volume-2/pages/5-6-ratio-and-root-tests . Usamos o enunciado do teorema com L>1 para divergência e L=1 inconclusivo; frase heurística anterior que sugere divergência em>=1 não foi transportada. Prova por q intermediário, família por paridade, figura, código e exercícios próprios. Sem copiar problemas, soluções ou figuras da fonte.

Programa CCM0123, https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123 , reconferido diretamente29/10/2026: seis grupos e bibliografia mantidos,ativação01/01/2025 posterior à turma2024/1. Teste da raiz é escolha didática dentro de séries infinitas,não item literal separado do programa. Aprovação histórica não prova domínio atual. Acervo e correspondências de Apostol/Stewart/Simmons mantidos conforme auditorias anteriores; nenhum novo trecho privado lido neste bloco.

Biblioteca padrão. term/root_value: n inteiro1..128,sem bool/float;partial/tail/bound permitemN0. first_bound aceita int/Fraction com0<tol<1 e buscaN<=128,senão informa limite do contrato. Frações exatas,sem estimar raízes com float ou inferir limites de128 amostras. Não inclui solver geral de convergência ou séries com unidades; parâmetros são adimensionais.

Execute da raiz: `python3 -m unittest discover -s labs/raiz-majorante -t .`; `python3 labs/raiz-majorante/root.py`.

Quatro testes: exemplo/soma/cota;129 caudas contra subtração independente e recorrência;128 identidades de raiz,razões por paridade e80 tolerâncias com minimalidade da cota;contratos. Verificações finitas não substituem a prova de comparação.
