# Leis de Newton: forças e vínculo unilateral

Rascunho original, 16/10/2026. Execute experiment.py com Python 3.
Na raiz: python3 -m unittest labs.leis-newton.test_experiment.

Partícula de massa constante, referencial inercial, chão horizontal rígido
liso sem adesão. Inicialmente y=0, vy=0; vx é escolhido. g=10 m/s² didático.
F é força prescrita de um agente, não precisa representar uma corda.
No contato, N=mg-Fy e ay=0. Se isso exigir N<0, a resposta inicial é N=0
e ay=(Fy-mg)/m>0. Em Fy=mg, N=ay=0: limite, não subida automática.

O diagrama contém forças em N; velocidade/aceleração estão no relatório.
As origens das setas são ligeiramente separadas para leitura, sem significado
de torque. A escala de comprimentos é comum às forças e se reajusta.
O painel não integra trajetórias, colisões ou mudança posterior de forças.
A potência inicial é Fx*vx porque vy=0; energia/potência dependem do referencial.
Exemplo anterior de duas forças +10/-4 N foi preservado separadamente.

Quatro testes: enumeração independente dos dois candidatos admissíveis ao
vínculo, 63 combinações exatas Fraction; trabalho/energia por deslocamento
finito e derivada simétrica exata; direções e independência da aceleração
em relação à velocidade inicial; continuidade na fronteira e domínio.
90 referências JS/Python conferem também equações e N*ay=0.
A condição de complementaridade é da resposta inicial adotada, não uma lei
geral para qualquer ponto de uma trajetória com impacto.

Fontes parciais consultadas em 16/10/2026:
- Nussenzveig, Curso de Física Básica I, exemplar autorizado do acervo,
  pp. 104–105 (PDF 105–106), terceira lei, e p. 119 (PDF 120), isolamento
  e normal sob força inclinada. Página 119 inspecionada visualmente.
  O exemplo da fonte inclui atrito; nosso modelo é próprio e liso.
  Não se reproduziu figura, enunciado ou solução do livro.
- [OpenStax University Physics I, 5.3](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law)
  e [6.1](https://openstax.org/books/university-physics-volume-1/pages/6-1-solving-problems-with-newtons-laws):
  trechos sobre sistema, lei vetorial e solução por componentes.

Pendentes: restrições acopladas, polias, planos inclinados, atrito,
rotação/torque, contato com impacto e revisão pessoal.
