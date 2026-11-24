# Curvatura e mudança de parâmetro

Laboratório original com derivadas analíticas prescritas,sem dados de trajetória ou diferenciação de medições. `curvature_squared(v,a)` retornaκ²=||v×a||²/||v||⁶,com v=r′≠0,a=r″ emR³. Entradas int/Fraction emvetores de3 componentes;bool,float,texto e formatos inválidos rejeitados. Retorno racional evita raízes em testes,não permite chamarκ² deκ. Imprima raiz aproximada somente como tal. `dot`/`cross` são helpers internos sobre vetores já validados.

`normal_acceleration_squared` usa projeção ortogonal e fornece||a_perp||². `reparameterize(v,a,p,q)` aplica(vp,ap²+vq),p=φ′,q=φ″ no ponto;derivadas deφ são entradas,não calculadas nem verificadas como função global. p0 é aceito nessa transformação algébrica,mascurvature_squared rejeita a derivada nula resultante. A invariância é para mudança regular local,p≠0;não classifica cúspides por amostras ou por limite.

Curvaγ(u)=(2u,u²,0),com uadimensional e posição em unidadeL. Derivadas(2,2u,0),(0,2,0). κ²=1/[4(1+u²)³],κ(0)=1/2L^-1. Comφ(s)=2s+s²,regular localmente paras>−1,nozero q′=(4,0,0),q″=(4,8,0);κ² continua1/4,embora rapidez e aceleração mudem. Figura:parábola y=x²/4 e círculo local de centro(0,2),raio2,mesma escala dos eixos. Parte do círculo é recortada na janela,sem sugerir que seja círculo global da parábola. Vetores nas caixas não são desenhados na escala espacial.

Caso padrão adicional de hélice r(t)=(2cos t,2sin t,3t):nozero v=(0,2,3),a=(−2,0,0),κ²=4/169,κ2/13;raio do cilindro2 distinto do raio de curvatura13/2. Apenas o jato analítico nozero é testado,não um integrador de trajetória ou prova numérica para todot. Caso regularκ0:reta ou ponto de inflexão(t,t³)nozero;normal principal indefinida ali,sem cúspide automática. Caso singular de parâmetroγ(s³)temderivadazero nozero e mesma imagem local lisa da parábola;fórmula rejeitada nesse ponto. Limite doκ² é1/4,mas resultado é justificado pela parametrização regularγ,não0/0.

Unidades:quando parâmetro étempo,v emL/T,a emL/T²,κ em1/L. Com parâmetro adimensional,derivadas emL,mesmoκ em1/L. Escala espacialλ>0 divideκ porλ;rotação/reflexão/translação rígida preservamκ;aceleração tangencial pode mudar sem alterarcurvatura. Não se pode obtercurvatura espacial usando a derivada de um gráfico com escala física desigualsemcorreção.

Da raiz:
```
python3 labs/curvatura-parametro/curvature.py
python3 -B -m unittest discover -s labs/curvatura-parametro -t .
```
Seis testes:25 pontos comparados à fórmula cartesiana independente;702 pares inteiros(v,a)contra determinante deGram e projeção normal;108 mudanças locais e uma composição polinomial com derivadas diretas;rotações/reflexão/escalas;regularidade/zeros e aproximação singular;contratos. Testes de cálculo,não inferência física,pedagogia ou domínio pessoal.

Fontes parciais em29/10/2026:Apostol,CalculusI,2ª1967,§14.14,pp536–538/PDF556–558,corpo consultado;extração inclui exercícios anteriores/pósteriores e p539,sem usá-los como atividades. p538/PDF558 inspecionada visualmente;equação14.22 tem glifos corrompidos na própria página,mas14.21 e prova14.23 legíveis corroboram denominadorv³. Usamosν para rapidez na aula,distinguindo vvetor. OpenStaxCalculus3§3.3,definição/Teorema3.6 e prova consultados parcialmente para corroborar fórmula. Curvas padrão não são descobertas originais;valores,comparação de parâmetros,desenho e código preparados para este roteiro. Sem copiar figuras,exercícios ouPDF privado.
https://openstax.org/books/calculus-volume-3/pages/3-3-arc-length-and-curvature
ProgramaJúpiterCCM0123 reaberto29/10,ativação01/01/2025 posterioràturma2024/1;item6 cálculo vetorial é amplo,curvatura é desdobramento editorial apoiado na bibliografia,nãoitemnominalisoladonoJúpiter.
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

Sem torsão,Frenet completo,teoria global ou dados físicos. Rascunho assistido porIA para revisão pessoal deJhuann.
