# Mesmo treino, riscos diferentes

Família original preservada: f_a(x)=x²+a(x³−x). Treino prescrito nos nós−1,0,1, sem ruído; coordenadas abstratas. Não há ajuste de polinômio geral nem dados reais.

`predict`, `mse` e `select`: int/Fraction; MSE1..1000pares, seleção1..1000candidatos, primeiro em empate. A API não garante procedência, independência ou separação de dados.

Com verdade g_b=f_b, qualquer a tem treino0. Em X uniforme[-1,1], risco exato8(a−b)²/105. `uniform_risk` usa integral conhecida de x⁶−2x⁴+x²; não usa teste empírico. Em referência b0: a2 tem previsão−1/2 em1/2, erro quadrático9/16 nesse ponto e risco32/105; a4 tem previsão−5/4 e risco128/105. Se as entradas só puderem ser os três nós, o risco é0para todos: a distribuição importa.

Validação sintética fixada em±1/2 seleciona a0entre0,2,4 para b0, mas a2para b2. Ela orienta escolha, portanto seu erro não é avaliação final independente. Não fornecemos um teste populacional nem garantia de generalização real. Penalizar a² escolheria0no treino plano, o que não é universalmente correto se b mudar.

Da raiz: `python3 -B -m unittest discover -s labs/sobreajuste-risco -t .` e `python3 labs/sobreajuste-risco/family.py`.

Seis testes: referências,ambiguidade do treino,quadratura independente,seleção/empate,material anterior,contratos. O risco é conferido por regra fechada de7nós com pesos(41,216,27,272,27,216,41)/840 na uniforme; momentos0..7 verificados antes, não são novas observações de teste ou hipótese adicional do modelo.

Fontes parcialmente consultadas30/10/2026: BishopPRML2006§1.1,pp4–9/PDF23–28,com recortes textuais e inspeção visualp7/PDF26; [scikit-learn3.1](https://scikit-learn.org/stable/modules/cross_validation.html),introdução sobre treino,validação e teste. Sem copiar a senoide,dados,figuras ou código dessas fontes. Família,integral,figura e laboratório locais. Revisão pessoal pendente.
