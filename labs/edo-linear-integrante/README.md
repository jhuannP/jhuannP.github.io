# EDO linear: fator integrante, PVI e domínio

22/10/2026. Material original preparado com apoio de IA; rascunho para revisão pessoal. Aula c2-linear-edo preserva as três seções e duas questões iniciais e passa a14 seções/12 exercícios. O exemplo de relaxação y′+2y=4, y(0)=1 continua disponível; a família singular abaixo é um segundo exemplo.

## Da equação à fórmula

Para y′+p(t)y=q(t), p e q contínuas em um intervalo aberto I com t₀ em I, defina A(t)=integral de t₀ até t de p(s), μ=exp(A). O teorema fundamental e a regra da cadeia dão μ′=pμ, μ>0 e μ(t₀)=1. Multiplicar a equação transforma o lado esquerdo em (μy)′. Integrar no mesmo intervalo e usar a condição inicial resulta em:

y(t) = [y₀ + integral de t₀ até t de μ(s)q(s)] / μ(t).

A fórmula constrói uma solução e sua diferenciação verifica a EDO. Para unicidade, a diferença z de duas soluções do mesmo PVI satisfaz (μz)′=0 e z(t₀)=0, logo z=0 em I. Não é um teorema geral para qualquer EDO. Não é preciso dividir por y ou excluir soluções que cruzam zero.

Se o fator for multiplicado por uma constante K não nula, o termo inicial é Kμ(t₀)y₀. Manter y₀ sozinho sem normalizar μ em t₀ seria um erro.

## Exemplo original e singularidade

y′+(2/t)y=3, y(1)=2, t>0. Variáveis adimensionais. μ=t²; (t²y)′=3t²; t²y−2=t³−1; y=t+1/t². Verificar: y′=1−2/t³ e (2/t)y=2+2/t³, soma3. Em t=2: y=9/4, y′=3/4.

Se y(1)=1, a fórmula simplifica para y=t, mas a EDO original segue indefinida em zero. Multiplicar por t altera o problema no ponto singular; uma extensão da fórmula não é automaticamente solução da mesma equação através de zero. A semirreta negativa suporta outro PVI; um valor inicial positivo não determina uma travessia do ponto singular.

## Laboratório e limites

Na raiz do site, apenas biblioteca padrão:
    python3 -m labs.edo-linear-integrante.experiment
    python3 -m unittest discover -s labs/edo-linear-integrante -t .

solve(m,q,t0,y0) trata somente y′+(m/t)y=q(t), m inteiro positivo, q lista/tupla de coeficientes racionais em ordem crescente. Para q(t)=sum q_j t^j, particular=sum q_j t^(j+1)/(m+j+1), e y=particular+C t^(−m). C é fixada pela condição inicial. O fator t^m é proporcional ao positivo normalizado em cada semirreta, mesmo se for negativo para m ímpar e t<0.

As entradas escalares aceitam int/Fraction, sem bool ou float. Rejeita t0=0 e consultas fora da semirreta inicial; isso explicita o intervalo do PVI. O estado é imutável, criado por solve. Não é API para validar estados construídos arbitrariamente à mão. Não é solver de EDO geral ou numérico, não calcula eventos e não atravessa singularidades.

Cinco testes: referência e fórmula removível;972 PVIs em grade e3888 verificações de resíduos em ambas as semirretas; derivadas conferidas por diferença central independente com passo1/1000000 e tolerância1/1000000 (apoio numérico, não prova); diferença homogênea entre soluções e preservação de entradas; contratos. A prova da família está na integração dos monômios, não na quantidade de testes.

## Fontes e correspondência

Programa CCM0123: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123, aberto em22/10/2026; retorno da ferramenta com captura de seis dias antes. Item1 introdução a EDOs; Apostol I2 na bibliografia. Ativação01/01/2025 posterior à turma2024/1: versão efetivamente ministrada não recuperada. Aprovação em2024/1 é registro do panorama já consolidado, não nova inspeção do histórico.

Apostol, Calculus, vol.I, segunda edição1967: corpo§8.4 pp.308–310 (PDF328–330), consulta parcial textual em22/10/2026. Forma linear, hipóteses de intervalo e teoremas8.2–8.3 de existência/unicidade. A leitura atual substitui o estado anterior de seção apenas localizada no sumário. Não houve nova renderização de páginas, leitura integral do capítulo ou distribuição do PDF. A notação, prova em prosa, exemplo, código e esquema fator-e-dominio.svg foram produzidos para estas notas, sem copiar o exercício da fonte.

## Continuidade

Revisão pessoal: reconstruir a regra do produto e a fórmula definida; conferir o PVI e justificar por que y=t não remove 2/t da equação. Preparação curricular seguinte: critérios de séries e mais problemas. Cálculo II mantém seis grupos parciais; não é curso completo. Próximo bloco global: revisar física escolar e uma introdução ainda curta, alternando as áreas.

Verificação do bloco:869 testes Python aprovados, incluindo cinco testes novos do laboratório;499 estruturas MathML conferidas. Após esclarecer apenas os enunciados dos exemplos,12 testes de catálogo/correção repetidos e aprovados. Navegador aceitou9/4 na questão5; diagrama legível a390px, sem transbordamento horizontal ou erros de console observados. Prévia edo-linear-integrante-mobile.jpg; viewport restaurado. Nenhum modelo JavaScript alterado. Catálogo494 aulas/2792 exercícios;288 aulas com até três seções, indicador de extensão e não de domínio. Todos os recortes seguem em rascunho. Próxima revisão pessoal: derivar o fator, conferir y=t+1/t² e justificar o intervalo. Próximo preparo global: física escolar, escolhendo uma introdução curta após conferir lacunas. Saldo semanal96%, parada operacional65%.
