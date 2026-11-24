# Dois resíduos no método de tiro

Experimento original para u''=-c*x em[0,1],u(0)=u(1)=0. c6 no exemplo,solução exata u=x−x³ e inclinação1. Integração Euler explícita racional,com duas inclinações e uma secante do mapa numérico. Sem dependências,sem rotina FNC copiada. n2..200,c int/Fraction em(0,12],s int/Fraction de módulo≤100.

N10 dá s18/25,u_E(1)=0 mas u_exato(s;1)=s−1=−7/25;u_E(1/2)=3/10 e a solução do contorno tem3/8,erro3/40. N20 reduz o erro médio para3/80. Fraction elimina arredondamento no experimento,mas não o erro de discretização. Este exemplo usa Euler para expor o erro; não altera o RK4 da aula antiga.

Fórmulas próprias por soma: v_k=s−c*k*(k−1)/(2N²),u_k=s*k/N−c*k*(k−1)*(k−2)/(6N³). O mapa final é afim e tem derivada1. s_N=c*(N−1)*(N−2)/(6N²);nos nós,u_N−u*=−(c/2)h*x*(1−x). O problema cúbico e todas as contas são sintéticos,adimensionais.

Fonte complementar Driscoll/Braun,Fundamentals of Numerical Computation,§10.2 Shooting,https://fncbook.com/shooting/,consulta parcial29/10/2026 à formulação de primeira ordem e resíduo,Eqs10.2.1–2 e texto de implementação sobre precisão do PVI. Não se leu integralmente o capítulo,não se reproduziu código,dados,exemplos ou figuras. Burden10ª permanece referência temática,sem nova leitura privada. EmentaCCM0226 preservada conforme consulta22/10,ativação2011 e versão2025 não comprovada. A discussão de ressonância no texto é analítica,não usa sin(pi) de máquina para provar singularidade.

Quatro testes:fixture;174 combinações(c,N)×3 inclinações e todos os nós contra somas fechadas,além do ajuste;25 refinamentos e mapas afins;contratos. Não garantem métodos gerais,contornos não lineares ou estabilidade em float. Revisão pessoal pendente.
