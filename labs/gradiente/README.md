# Derivadas direcionais, gradiente e diferenciabilidade

Material original em rascunho para revisão. A parte diferencial desta trilha apoia CCM0213 (Matemática III); não amplia a cobertura dos cinco grupos integrais/especiais de CCM0223 (Matemática IV).

Função 0: f=x²+2y², g=(2x,4y), diferenciável em R². Em deslocamento hu com ||u||=1, o resto exato é h²(uₓ²+2uᵧ²), limitado por 2h² uniformemente nas direções. Função 1: F=x³/(x²+y²) fora da origem, F(0)=0. É contínua porque |F|≤||(x,y)||, suave fora da origem, com todas as derivadas direcionais na origem DᵤF=uₓ³. As parciais ali são (1,0), mas o mapa direcional não é linear. Na direção u=(3/5,4/5), o resto/h do candidato linear é −48/125 para todo h>0, provando a falha.

O campo de parciais não representa o diferencial onde este não existe. O azul do painel representa g normalizado (comprimento 1), com traço descontínuo na origem singular; não representa ||g||. Preto contínuo: nível do ponto; preto tracejado: deslocamento h·u; cinza: níveis de referência. Nas direções com resto zero o contraexemplo ainda não se torna diferenciável. O programa conhece a classificação analítica apenas desses exemplos; não faz diagnóstico geral por amostras.

Na quadrática, g=0 na origem, mas o nível zero é um ponto. No contraexemplo, g=0 em (0,1), com nível zero x=0: não se deve aplicar o critério regular de gradiente não nulo. Derivada direcional nula não prova constância, extremo ou regularidade do nível.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/gradiente/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes: 144 incrementos quadráticos exatos com Fraction e diferenças centradas; homogeneidade do contraexemplo, continuidade limitada e resto não nulo em direções racionais; parciais por diferenças numéricas e normalidade em elipses parametrizadas independentemente; refinamento, pontos críticos e domínios. Na comparação de restos em binary64, a tolerância considera unidades do último dígito divididas pelo passo, pois a subtração de valores próximos amplifica arredondamento. A prova racional não depende dessa tolerância.

Quarenta e oito configurações JS/Python. O teste JavaScript também verifica que os pontos desenhados nas curvas satisfazem os níveis, incluindo curvas racionais e nível zero. A demonstração existente `gradient` foi ampliada mantendo seu identificador, e o exemplo Python anterior `gradiente(x,y)` foi preservado como função para a quadrática.

## Fontes consultadas parcialmente — 16/10/2026

- Apostol, *Cálculo*, vol. II, tradução identificada no acervo (Reverté 1996, reimpressão 2004, original segunda edição): trechos 8.11–8.13, pp. 290–293 (PDF 305–308), e trecho 8.16, p. 299 (PDF 314). Inspeção visual de pp. 291 e 293; sem presumir paginação da edição inglesa ou reproduzir páginas, figuras/exercícios.
- [OpenStax Calculus III 4.4](https://openstax.org/books/calculus-volume-3/pages/4-4-tangent-planes-and-linear-approximations): resto relativo, diferenciabilidade e condição suficiente de parciais contínuas.
- [OpenStax Calculus III 4.6](https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient): definição direcional, enunciado com diferenciabilidade, máxima taxa e níveis. A hipótese de diferenciabilidade foi mantida; existência de parciais isoladas não foi usada como prova.

Exemplos, contraexemplo selecionado, desenvolvimento, exercícios, código e gráficos próprios, sem alegar leitura integral dos capítulos. Não são resultados experimentais nem certificação de domínio. Pendentes: Jacobiana/diferencial geral, plano tangente/cadeia aprofundados, mais provas e revisão pessoal.
