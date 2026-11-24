# Corda fixa: modos e superposição

Exemplo e material originais, rascunho para revisão de Jhuann. Corda uniforme ideal, pequena inclinação, extremidades y(0,t)=y(L,t)=0, tensão e rapidez constantes, regime linear não dispersivo. Não modela rigidez, perdas, tensão variável, dedilhado geral ou resposta forçada. Um modo livre não requer uma força externa periódica permanente no modelo sem perdas.

Exemplo próprio L=1,2m,v=48m/s,n=3: f=60Hz,lambda=0,8m; nós0;0,4;0,8;1,2m e ventres0,2;0,6;1m. Cada componente progressiva tem amplitude A=1mm; o máximo de deslocamento em cada ventre é2mm, não1mm. No instante T/4 toda a corda cruza o equilíbrio, sem tornar todos os pontos nós. Não ocorre desaparecimento de energia: nesse instante o modo tem velocidade transversal e energia cinética.

Fontes primárias consultadas parcialmente29/10/2026:
- OpenStax Physics §13.3, recortes superposição, nós/ventres e reflexão fixa: https://openstax.org/books/physics/pages/13-3-wave-interaction-superposition-and-interference . Não usados problemas, soluções ou figuras da fonte.
- OpenStax University PhysicsI §16.6, equações16.14–16.16 e limites fixos: https://openstax.org/books/university-physics-volume-1/pages/16-6-standing-waves-and-resonance . Há frases locais com ±A contrastando com a própria expressão2A sin(kx)cos(wt); adotamos explicitamente A por componente e máximo2A na resultante, conferido algebricamente. Não copiamos desenho ou exemplo da fonte.
Sem nova consulta a livro privado ou currículo oficial brasileiro; percurso próprio de reforço.

Python padrão sem dependências. spectrum aceita int/Fraction, uma unidade SI consistente assumida, 0,01<=L<=10m,0,01<=v<=1000m/s,n inteiro1..20. Posições e espectro racionais; profile usa trigonometria float após reduzir ciclos exatamente. 0<=t<=10s e0<A<=L/(100n); esse limite é didático e mantém inclinação máxima2A*n*pi/L<=2pi/100, não um limiar físico universal. Nenhuma unidade detectada automaticamente, nenhuma física quântica ou medição real inferida.

Execute da raiz: `python3 -m unittest discover -s labs/corda-modos -t .`; `python3 labs/corda-modos/modes.py`.

Quatro testes: exemplo/contagens; nós em diferentes fases, amplitudes dos ventres, inversão e periodicidade para12 modos;900 pontos comparados com soma independente de ondas progressivas, mais escala; contratos. Resíduos trigonométricos próximos de zero são arredondamento. A prova das frequências vem da condição de borda, não da malha. Roteiro de estudo: prever o desenho em0,T/4,T/2 antes de comparar a figura. Não é experimento realizado.
