# Energia e momento em 1+1 dimensões

Material original em rascunho para revisão; não é dado experimental ou resultado da IC. Uma partícula de massa m₀, ou duas iguais com velocidades opostas ±βc em S. Partículas livres, sem campos ou energia de interação. S′ move-se a +w em relação a S; mudar w troca o observador, sem acelerar o sistema.

Normalização: E*=E/(m₀c²), p*=p/(m₀c), M*=M/m₀. Código usa c=m₀=1. Para partícula, E=γ e p=γβ; K=p²/(E+1) evita o cancelamento de E−1 quando β é muito pequeno. Não recupera precisão perdida nos dados. Boost: E′=γw(E−wp), p′=γw(p−wE). A inversa usa −w; a norma E²−p² é invariante.

Para o par, some os quadrimomentos antes de calcular a massa. Em S, Ptotal=0, Etotal=M=2γ. A soma das massas individuais é 2, mas M inclui a energia cinética interna no referencial de momento zero. Kbulk=Etotal−M e soma Ki=Etotal−2 são distintos. Em β=0,6 e w=0, M=2,5, Kbulk=0 e soma Ki=0,5. A fusão completa sem perda preservaria o mesmo quadrimomento, com massa final M; mecanismo ou possibilidade material dessa fusão não são calculados.

Gráfico de E versus p do objeto selecionado, com hipérbole de massa e referência E=|p|. Os dois eixos têm mesma escala por unidade e a janela se ajusta. Compare números, não pixels entre janelas. Fótons não entram na fórmula material com γ(1); dois fótons opostos, no teste, mostram que massa nula individual não obriga massa nula do conjunto.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/energia-momento/experiment.py
python3 labs/energia-momento/verify_decimal.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes novos: quarenta estados de partícula conferidos por parametrização independente de rapidez (cosh/sinh) e boost inverso; sete referências Decimal 70 dígitos de K=γ−1 (incluindo β=10⁻⁹); quarenta estados de sistema com invariantes e balanço de fusão; composição de velocidades, fótons e domínios. A cinética estável em β=10⁻⁹ é positiva, enquanto γ−1 em binary64 zera. As tolerâncias são locais aos cenários e não prova universal de precisão. Vinte e quatro configurações JS/Python e comparação JS direta com as referências Decimal.

A coluna Ki da tabela é individual. A linha total deixa essa coluna vazia e o texto informa Kbulk e soma Ki separadamente. Pequenos valores usam notação científica; erro relativo da aproximação clássica fica indefinido quando K=0.

## Fontes consultadas parcialmente — 16/10/2026

- Nussenzveig, *Curso de Física Básica*, vol. IV, segunda edição, 2014, exemplar privado do acervo: trechos de 6.9–6.11, pp. 176–180 (PDF 177–181). Extração dos cinco trechos e inspeção visual de pp. 176 e 179. A notação m(v)=γm₀ do texto é distinguida da massa invariante m₀ usada aqui. Sem reprodução de páginas ou figuras.
- [OpenStax III 5.8](https://openstax.org/books/university-physics-volume-3/pages/5-8-relativistic-momentum): momento, tempo próprio e convenção de massa.
- [OpenStax III 5.9](https://openstax.org/books/university-physics-volume-3/pages/5-9-relativistic-energy): trechos de trabalho/cinética, limite clássico e relação energia–momento.
- [Feynman I 16–4](https://www.feynmanlectures.caltech.edu/I_16.html): trecho da colisão inelástica e energia interna, com notação histórica explicitada.
- [Feynman I 17–4/17–5](https://www.feynmanlectures.caltech.edu/I_17.html): transformação, soma e norma do quadrimomento.

Exemplos, exercícios, gráficos e código próprios; não se declarou leitura integral dos capítulos ou validação experimental. Pendentes: colisões gerais, vetores não colineares, Compton, forças/acelerações e revisão pessoal.
