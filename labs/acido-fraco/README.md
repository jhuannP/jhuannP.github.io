# Ácido HA ideal com a contribuição da água

Rascunho original para revisão de Jhuann. Ácido hipotético, sem dados experimentais, identificação de substância real ou experiência pessoal presumida.

## Referências efetivamente consultadas em 16/10/2026

- Atkins/Jones/Laverman, Princípios de Química, 7ª edição, Bookman 2018: sumário e texto de 6D.1, páginas impressas 472–473 (PDF 604–605). Aproximações de ácido fraco e alerta sobre água; não foi lido integralmente o capítulo nem copiado exercício/figura. É edição diferente da terceira citada no programa CCM0114. PDF privado identificado e mantido no acervo, sem cópia ao site.
- [OpenStax Chemistry 2e, 14.3](https://openstax.org/books/chemistry-2e/pages/14-3-relative-strengths-of-acids-and-bases): equilíbrio, constantes e ionização. A igualdade aproximada entre hidrônio e base conjugada não foi estendida ao regime com água relevante.
- [IUPAC Gold Book, pH](https://goldbook.iupac.org/terms/view/P04524): definição por atividade consultada no conteúdo indexado; abertura direta retornou 403. A definição explicita atividade em escala molal. A aula usa concentrações normalizadas como aproximação ideal e não afirma equivalência de estados padrão ou realização metrológica de pH.

Texto, derivação do experimento, exemplos, dados, código e gráficos próprios.

## Convenção e hipóteses

HA neutro monoprótico em água sem sal ou outros íons, CO₂, outros equilíbrios ou reações laterais. c°=1 mol/L; h=[H3O+]/c°, a=[A-]/c°, u=[HA]/c° e o=[OH-]/c°. C é concentração analítica dividida por c°. pH≈-log10 h é a aproximação ideal à definição por atividade. As constantes escolhidas são compatíveis com essa convenção de modelagem; não são parâmetros medidos de uma substância.

Balanços: C=a+u e h=a+o. Constantes adotadas: Ka=ha/u, Kw=ho. Solvente e coeficientes de atividade aproximados por 1. Kw=10^-14 é o valor arredondado do cenário a 25 °C. Neutralidade pH 7 só vale neste cenário. A faixa até 0,1 mol/L permite explorar o modelo, sem garantir idealidade de uma solução real.

## Solução e referências independentes

a=C Ka/(Ka+h), u=C h/(Ka+h), o=Kw/h. Resolver g(h)=h-Kw/h-C Ka/(Ka+h)=0. g é estritamente crescente para h>0; uma raiz única está em [sqrt(Kw), C+sqrt(Kw)]. Bisseção em log h evita h negativo. Em C=0 há água pura e fração dissociada não definida.

A verificação independente resolve com Decimal de 80 dígitos e Newton a cúbica h³+Ka h²-(Kw+KaC)h-KaKw=0. Começa no limite superior; a derivada da cúbica é positiva acima da raiz e sua convexidade mantém a sequência de referência por cima. Não usa a bisseção como referência de si mesma.

Na raiz: `python3 -m unittest discover -s labs/acido-fraco -t .`. Quatro testes verificam balanços/constantes, doze configurações de referência Decimal, regimes de aproximação, diluição, água pura, alteração matemática de Kw e entradas inválidas. `reference.json` tem 28 configurações cruzadas Python/JS, incluindo C=0.

## Duas aproximações diferentes

1. Omitir água: h≈a leva à quadrática. Calcule a raiz positiva pela forma estável 2KaC/[Ka+sqrt(Ka²+4KaC)].
2. Omitir também depleção: u≈C leva a sqrt(KaC).

O critério de 5% trata depleção nas condições apropriadas, não certifica omissão da água ou coeficientes de atividade. A fração dissociada correta é a/C; h/C pode superar 1 porque a água também contribui com hidrônio. O modelo com água não prevê solução básica ao dissolver apenas HA neste cenário.

## Exploração proposta e limites

Compare C=0,01 mol/L e C=10^-10 mol/L mantendo Ka=10^-5. No primeiro, pH≈3,50687 e alpha≈3,11267%. No segundo, pH≈6,99979 e alpha≈99,0094%, enquanto a quadrática sem água prevê pH≈10. Esses são resultados do modelo ideal, não medições.

Tampões, bases fracas, titulação, polipróticos, íons espectadores, força iônica e atividades não ideais ainda precisam de aulas próprias. O grupo curricular continua parcial; não há curso completo nem domínio pessoal certificado.
