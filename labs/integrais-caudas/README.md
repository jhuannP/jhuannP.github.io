# Integral imprópria no infinito: limites e caudas

Rascunho didático original · 27/10/2026 · revisão pessoal pendente.

## Infinito não é uma fronteira numérica

Suponha que f seja integrável em todo intervalo finito [1,B], com B≥1. Definimos I(B)=∫₁ᴮ f(x)dx. A integral no infinito converge quando I(B) possui um limite real finito ao fazer B crescer sem limite. Primeiro integramos em uma fronteira finita; depois estudamos o limite. O símbolo ∞ não é um número para substituir em uma primitiva. Um resultado até B=100, sozinho, não determina convergência.

∫₁∞ f(x)dx = lim B→∞ I(B)

## Uma família mostra a fronteira

Para f(x)=x⁻ᵖ, x≥1 e p real, a regra da potência fornece I(B)=(B^(1−p)−1)/(1−p) quando p≠1. Se p>1, o expoente 1−p é negativo e B^(1−p) tende a zero; logo o limite é 1/(p−1). Se p<1, esse expoente é positivo e I(B) cresce sem limite. Resta tratar p=1 separadamente: I(B)=ln B, que também cresce sem limite. Portanto a integral converge exatamente quando p>1.

p > 1 ⇒ ∫₁∞ x⁻ᵖ dx = 1/(p−1)

## O resto ajuda a decidir o corte

Quando p>1, defina R(B)=∫ᴮ∞ x⁻ᵖ dx. Avaliar a integral entre B e uma fronteira finita C e depois tomar C→∞ dá R(B)=B^(1−p)/(p−1). Por aditividade, a integral total é I(B)+R(B). Se usamos apenas a integral parcial exata, o erro absoluto de corte é precisamente R(B), porque o integrando é não negativo. Ainda não há erro de quadratura nesta identidade.

R(B) = B^(1−p)/(p−1)

## Tolerância estrita: o corte 100 ainda não basta

No exemplo p=2, a integral total é 1 e a cauda é 1/B. Para exigir erro estritamente menor que 1/100, resolva 1/B<1/100, obtendo B>100. Se B deve ser inteiro, o menor corte é 101. Em B=100 o erro é exatamente a tolerância: atende a “menor ou igual”, mas não a “menor”. Em B=101, a parte é 100/101 e a cauda 1/101.

## A condição geral para escolher uma fronteira

Com p>1 e ε>0, a desigualdade B^(1−p)/(p−1)<ε equivale a B^(p−1)>1/[(p−1)ε], pois B>0. Portanto B>[1/((p−1)ε)]^(1/(p−1)), além de B≥1. Essa expressão trata p real; o laboratório exato implementa apenas p inteiro a partir de 2. Uma busca por inteiros com comparações racionais evita decidir uma desigualdade estrita com uma raiz arredondada.

B^(p−1) > 1/[(p−1)ε]

## Convergência lenta perto de p igual a um

Para p=11/10, a integral total vale 10. A cauda é 10 B^(−1/10), e a fração do total omitida é B^(−1/10). Mesmo em B=10¹⁰, a cauda ainda vale 1, ou 10% do total. Para erro absoluto estritamente menor que 1/100, precisamos B>10³⁰. Para erro relativo menor que 1/100, basta a condição B>10²⁰. São perguntas diferentes; uma integral convergente pode exigir um corte enorme.

Erro relativo = R(B)/I(∞) = B^(1−p)

## O integrando tende a zero: ainda falta analisar a área

A função 1/x tende a zero, mas sua integral de 1 até B vale ln B e diverge. Alturas pequenas podem acumular área ilimitada quando o intervalo cresce. Em sentido oposto, ver uma curva próxima de seu limite em uma janela do gráfico não fornece por si só uma cota de erro; precisamos de uma estimativa válida para toda a cauda.

## Uma integral parcial limitada pode continuar sem limite

Divergir não significa sempre crescer até infinito. Para f(x)=sin x em [0,∞), a integral parcial é 1−cos B, sempre entre 0 e 2. Nas fronteiras B=2πn ela vale 0; em B=(2n+1)π vale 2. Como duas sequências de fronteiras que vão ao infinito produzem valores distintos, não há limite único. A limitação, sozinha, não é critério para integrandos que mudam de sinal.

## Por que limitação funciona no caso não negativo

Se f≥0, a integral parcial I(B) é não decrescente: aumentar o intervalo só acrescenta massa não negativa. Se também I(B)≤M para todo B≥1, o conjunto de valores tem supremo L finito. Dado ε>0, existe B₀ com I(B₀)>L−ε; para B≥B₀, L−ε<I(B)≤L. Isso prova I(B)→L. A monotonicidade é o elo que faltava no exemplo com seno.

## Comparar com uma cauda conhecida

Considere g(x)=1/(x²+4), x≥1. Temos 0≤g(x)≤1/x², portanto suas integrais parciais crescem e ficam limitadas por 1. Isso prova convergência sem calcular uma primitiva de g. A mesma comparação a partir de B≥1 fornece ∫ᴮ∞ g(x)dx≤1/B. Para garantir cauda estritamente menor que 1/100 por essa cota, podemos escolher B=101. Isso é um corte suficiente; não afirmamos que seja o menor para g.

## Corte e quadratura são erros diferentes

Um programa geralmente aproxima a integral parcial por um número Q(B). A diferença até a integral total satisfaz |I(∞)−Q(B)|≤|I(B)−Q(B)|+R(B). A primeira parcela é erro no intervalo finito; a segunda é erro de corte. Aumentar B pode diminuir a cauda e, ao mesmo tempo, piorar uma quadratura com o mesmo número de pontos. Para uma tolerância global, precisamos controlar as duas parcelas.

Erro total ≤ erro de quadratura + erro de corte

## Um laboratório com limites racionais verificáveis

Para p inteiro ≥2, x⁻ᵖ é positiva e decrescente em [1,B]. Em uma malha uniforme de n partes, retângulos pela direita fornecem limite inferior Lₙ, e pela esquerda limite superior Uₙ. Assim Lₙ≤I(B)≤Uₙ. Somar a cauda exata em ambos os lados enquadra a integral total. O intervalo [Lₙ+R(B),Uₙ+R(B)] ainda tem largura Uₙ−Lₙ: conhecer a cauda não elimina a incerteza da quadratura. O código usa Fraction e recusa p real não inteiro; isso é um limite da implementação, não da teoria.

## Duas direções infinitas exigem dois limites

Para integrar em toda a reta, separe em um ponto finito e exija que as duas integrais laterais convirjam. A função x/(1+x²) não possui singularidade real. Sua integral de 0 até B é (1/2)ln(1+B²), que diverge; a lateral negativa diverge para −∞. No intervalo simétrico [−B,B] a integral vale zero por imparidade, mas isso não define a integral imprópria usual. É um valor principal simétrico, uma construção diferente; não cancelamos duas divergências para provar convergência.

## Não confundir a cauda com uma singularidade finita

O critério p>1 foi obtido para x⁻ᵖ perto de infinito, começando em 1. Perto de zero, a pergunta é outra: ∫₀¹ x⁻ᵖ dx converge quando p<1. A primitiva e o limite no extremo correto mostram a inversão. Se uma integral tiver singularidade finita e cauda infinita, cada trecho problemático precisa de seu próprio limite; conferir apenas a cauda não basta. A aula de singularidades desenvolve esse outro recorte.

## Como usar o painel e revisar em vinte minutos

No painel, escolha p=1 e aumente B: a curva de integrais parciais cresce como ln B, sem limite finito. Depois escolha p=2 e confira parte 9/10 e cauda 1/10 em B=10. A linha pontilhada é uma referência analítica, não uma convergência demonstrada pelo desenho. Sem olhar a solução, derive a cauda, justifique o corte inteiro 101 e explique a diferença entre tolerâncias absoluta e relativa. Revisão pessoal de Jhuann ainda pendente.

## Exercícios e resoluções

1. Quanto vale a integral de 1 até infinito de x⁻² dx?

   Resolução: 1−1/B tende a 1.

2. Integral finita até B=100 prova convergência no infinito?

   Resolução: É necessário analisar o limite.

3. Para p=2 e B=10, quanto vale a integral parcial de 1 até B?

   Resolução: 1−1/10=9/10.

4. Para p=2 e B=10, quanto vale a cauda de B até infinito?

   Resolução: 1/B=1/10.

5. Qual o menor inteiro B≥1 que dá cauda estritamente menor que 1/100 para p=2?

   Resolução: 1/B<1/100 exige B>100; menor inteiro 101.

6. Para p=3 e B=10, qual é a cauda?

   Resolução: 1/(2B²)=1/200.

7. Para p=3, qual o menor inteiro B≥1 que dá cauda estritamente menor que 1/1000?

   Resolução: 1/(2B²)<1/1000 exige B²>500; 22²=484 e 23²=529.

8. Para p=11/10 e B=10¹⁰, quanto vale o erro absoluto de corte?

   Resolução: 10(10¹⁰)^(−1/10)=1.

9. No mesmo caso p=11/10 e B=10¹⁰, qual a fração da integral total omitida?

   Resolução: R/I=1/10; não confunda fração com porcentagem.

10. A condição f(x)→0 é suficiente para a integral de 1 até infinito convergir?

   Resolução: 1/x tende a zero, mas sua integral parcial ln B diverge.

11. As integrais parciais de sin x em [0,B] ficam entre 0 e 2. A integral no infinito converge?

   Resolução: As fronteiras 2πn e (2n+1)π dão limites distintos.

12. A integral de x/(1+x²) em [−B,B] vale zero. Isso prova convergência da integral usual em toda a reta?

   Resolução: As duas laterais divergem; o cancelamento simétrico é valor principal.

## Fontes e alcance da leitura

Programa oficial CCM0123, item 2 (sequências, séries e integrais impróprias), reconferido em 27/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123 . Ativação exibida 01/01/2025; versão da turma de 2024/1 não recuperada. A trilha editorial não é equivalência administrativa da disciplina.

Apostol, Calculus, volume I, 2ª edição, 1967, exemplar privado autorizado: §10.23, pp.416–419/PDF436–439 (PDF contado a partir de 1). Consulta textual parcial; p.417/PDF437 renderizada e inspecionada. A extração perdeu o sublinhado de s≤1; a imagem confirma divergência também em s=1. Definição, família potência, oscilação, comparação e distinção entre extremos constam dos recortes. Não se afirma leitura integral do capítulo. Identificação da edição já conferida nos registros anteriores. O livro não é distribuído.

OpenStax, Calculus Volume 2, §3.7: https://openstax.org/books/calculus-volume-2/pages/3-7-improper-integrals . Consulta parcial em 27/10/2026 das definições de intervalos infinitos, duas laterais e teorema de comparação. O exemplo de acidentes da página contém texto inconsistente e não foi usado como fundamento ou reproduzido. Não se afirma revisão de toda a página. As deduções do corte, tolerâncias, figura, exemplos de comparação e valor principal, exercícios e laboratório são elaboração própria; não são gabarito oficial dos livros.

## Laboratório e verificações

`tails.py`: p inteiro ≥2, B racional ≥1. `tail` calcula a cauda; `partial` a parte em [1,B]; `cutoff` retorna o menor inteiro que satisfaz a tolerância estrita. Dobrar a fronteira encontra um intervalo de busca porque p−1>0 e a cauda tende a zero; bisseção mantém uma fronteira que falha e outra que atende, terminando em inteiros consecutivos. Se B=1 já atende, retorna 1.

`finite_bracket` calcula retângulos inferiores/superiores na parte finita. Malhas diádicas aninhadas apertam os limites porque a função é decrescente; a diferença entre as somas é h(1−B⁻ᵖ), por cancelamento dos pontos internos. Somar a cauda exata dá limites para a integral total. O laboratório não é um integrador geral, não implementa p não inteiro, oscilação, singularidades finitas ou estimativa de erro de ponto flutuante.

```sh
python3 labs/integrais-caudas/tails.py
python3 -m unittest discover -s labs/integrais-caudas -t .
```

Testes: valores conhecidos, lei de escala e monotonicidade; busca de cortes por referência linear independente e igualdade na fronteira; integrais analíticas dentro de limites de retângulos calculados por amostragem; refinamento e largura telescópica; contratos. A prova de convergência está no texto, não no número de testes.

## Registro pessoal — preencher ao revisar

- Data:
- Como provei que p=1 diverge:
- Como escolhi o corte estrito:
- Onde aparece o erro de quadratura:
- Dúvida que restou:

Não certifica aprendizagem pessoal. Outras técnicas de comparação, convergência condicional e problemas de singularidade continuam pendentes.
