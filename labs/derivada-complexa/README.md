# Derivada complexa — caminhos, regularidade e contraexemplos

Laboratório original de quocientes incrementais, com complexos representados por pares (real, imaginária) de int/Fraction. Não usa amostragem para afirmar existência de limites. Nenhuma dependência externa.

- `square`: f(z)=z², quociente 2z+h, erro com módulo |h|.
- `conjugate`: conj(z), quocientes 1 no eixo real e−1 no imaginário em qualquer ponto.
- `trap`: g(0)=0, g(z)=conj(z)²/z fora da origem. Contínua em0 por |g(z)|=|z|; parciais satisfazem Cauchy–Riemann em0; quocientes1 nos dois eixos e−1 na diagonal. Não há derivada complexa em0.
- `radial`: |z|², derivada complexa0 somente na origem; não holomorfa perto dela.

## Referência

[NIST DLMF §1.9(ii)](https://dlmf.nist.gov/1.9#ii), subtítulos Differentiation, Cauchy–Riemann Equations (1.9.25), Analyticity e Harmonic Functions (1.9.26). Consulta pública parcial em27/10/2026. As provas didáticas, exemplos, figura e código são próprios; não se atribuem os contraexemplos a um exercício da fonte. Não foi coberta a teoria integral ou equivalência com séries de potências.

## Uso e verificação

Na raiz: `python3 -m unittest discover -s labs/derivada-complexa -t .`.

As operações racionais são comparadas com complex em exemplos pequenos; o quociente polinomial é confrontado com identidade algébrica para diferentes pontos, direções e escalas. O contraexemplo é verificado também em forma cartesiana independente. Controle de norma, parciais nos eixos e contratos completam os casos. Isso verifica implementação e identidades selecionadas, não substitui as provas nem a revisão pessoal.

`quotient` rejeita h=0; a extensão g(0)=0 é parte da definição. Valores decimais/bool são rejeitados: use Fraction. Retorna pares racionais. Desafio original do conjugado e exemplo de z² com complex foram preservados na aula.

Próximo passo de20min: derivar as duas expressões axiais, identificar a hipótese de suficiência e refazer os três quocientes de g. Revisão pessoal, leitor de tela e aplicações físicas pendentes.

Conferência em 27/10/2026: cinco testes locais e 14 de catálogo aprovados; 803 fórmulas estruturais. No navegador em 390 px, rejeição de 1 e aceite de −1 pelo Enter no exercício da diagonal, mais critério de regularidade aceito. Figura final inspecionada, sem rolagem horizontal; console sem erros. Captura na raiz: `derivada-complexa-mobile.jpg`.
