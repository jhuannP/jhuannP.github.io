# Gases reais: equação reduzida e limites

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Na raiz: python3 -m unittest labs.gases-reais.test_experiment.

Definições: x=b/Vm, Θ=RTb/a e P*=pb²/a, com a,b>0.
P*=Θx/(1-x)-x²; Z=1/(1-x)-x/Θ.
O painel limita Θ a 0,4..2 e x a 0..0,6. Θc=8/27 é menor
que toda a faixa de temperatura. dP*/dx é positivo; não há laço subcrítico.
Não se ajustou gás real ou reproduziu dados de pressão.

eos permite avaliar a expressão fora da faixa do painel, mas não classifica
equilíbrio global. Se a derivada não é positiva, pkappa retorna None.
Isso não implementa coexistência ou construção de Maxwell.

pκT=P*/[x(dP*/dx)]. No ideal vale 1; não confundir com fator Z.
Em x=0, a expressão usa limites Z=1, P*=0, pκT=1; volume_ratio=None.
κT isolada não é finita nesse limite. Em Θ=3/5,x=2/5: Z=1 e pκT=9/13.
Na temperatura de Boyle Θ=1, Z-1=x²/(1-x), não zero em densidade finita.

Quatro testes: 64 estados contra equação dimensional independente com
Fraction; resto virial/Boyle e cancelamento; diferenças finitas nas
coordenadas de densidade e volume; fatoração exata do limite mecânico,
derivadas críticas e contratos. Quarenta referências JS/Python conferem
também a identidade p/(RT/Vm)=Z, o resto e a derivada positiva.
Curvas do painel são estados na mesma temperatura, não trajetória.

Fontes parciais, consulta em 16/10/2026:
- Atkins/de Paula, Físico-Química I, nona edição, tradução LTC 2012,
  seções 1.3/1.4, pp. impressas 25–28 (PDF 49–52), todas inspecionadas
  visualmente porque o exemplar é digitalização sem texto útil.
  Esta edição difere da oitava de 2008 indicada no programa. Metadados
  reconfirmados no copyright, sem equiparar os dois volumes do acervo.
- [OpenStax Chemistry 2e 9.6](https://openstax.org/books/chemistry-2e/pages/9-6-non-ideal-gas-behavior):
  trechos de Z, correções e equação textual. Não se copiou tabela ou exemplo.
  Forma correta: (p+a/Vm²)(Vm-b)=RT, ou p=RT/(Vm-b)-a/Vm².

Gráficos, exemplos e exercícios próprios. Pendente: dados experimentais,
coexistência, outras equações, propriedades caloríficas e revisão pessoal.
