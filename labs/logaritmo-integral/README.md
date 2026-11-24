# Logaritmo natural — construção integral

## Uma construção precisa justificar as propriedades que usaremos

A aula escolar de logaritmos parte da relação entre potência e expoente. Aqui construímos o logaritmo natural a partir da integral e depois definimos a exponencial como sua inversa. O percurso usa continuidade, Teorema Fundamental do Cálculo, regra da cadeia e valor médio já estudados nesta trilha. A ordem permite justificar a derivada e a regra do produto sem assumir previamente uma exponencial real com todas essas propriedades.

## Defina ln x por uma integral em domínio positivo

Para x>0, defina ln x=∫ de 1 a x de 1/t dt. O integrando é contínuo em todo intervalo fechado entre 1 e x, pois esse intervalo não atravessa zero. Assim a integral é própria. Quando x=1, vale zero. Para x>1, corresponde à área positiva sob 1/t; para 0<x<1, a orientação inverte os limites e a integral é negativa. Não estendemos esta definição a x≤0.

ln x=∫₁ˣ (1/t) dt, x>0

## O Teorema Fundamental fornece a derivada

Como 1/t é contínua para t>0, o Teorema Fundamental dá (ln x)′=1/x. A derivada é positiva, portanto ln é estritamente crescente; valores diferentes de x têm logaritmos diferentes. Derivando novamente, (ln x)″=−1/x²<0: o gráfico é côncavo para baixo. A inclinação diminui sem que isso implique que a função tenha um teto.

(ln x)′=1/x; (ln x)″=−1/x²

## A regra do produto pode ser provada usando derivadas

Fixe a>0 e considere F(x)=ln(ax)−ln x para x>0. Pela cadeia, F′(x)=a/(ax)−1/x=0. Pelo teorema do valor médio, F é constante em qualquer intervalo positivo. Avaliando em x=1, F(1)=ln a. Logo ln(ax)=ln a+ln x para todo x>0. Esta prova conserva as condições a>0 e x>0; não justifica separar logaritmos de fatores negativos.

ln(ax)=ln a+ln x, a,x>0

## Potências inteiras e recíprocos seguem sem circularidade

Aplicar repetidamente a regra do produto dá ln(aⁿ)=n ln a para n inteiro positivo. Como ln 1=ln(a×1/a)=ln a+ln(1/a), temos ln(1/a)=−ln a. Isso estende a identidade a inteiros negativos e inclui n=0. Ainda não precisamos definir potências reais arbitrárias. Por exemplo, ln 8=3 ln 2 e ln(1/8)=−3 ln 2.

## A função atinge todos os valores reais

A integral que define ln 2 é positiva. Portanto ln(2ⁿ)=n ln 2 cresce sem limite quando n aumenta, enquanto ln(2⁻ⁿ)=−n ln 2 decresce sem limite. Para qualquer y real, podemos escolher dois argumentos positivos com logaritmos abaixo e acima de y. A continuidade e o valor intermediário garantem um argumento com ln x=y; a monotonicidade garante que ele é único. Assim ln é uma bijeção de (0,∞) em ℝ.

## A exponencial é definida como a inversa

Para y real, defina exp(y) como o único x>0 com ln x=y. Então ln(exp y)=y e exp(ln x)=x para x>0. Como ln 1=0, exp(0)=1. Definimos e=exp(1), de modo que ln e=1. A exponencial é crescente e positiva. Esses fatos vêm da inversão de ln, não de uma aproximação decimal para e.

## A derivada da inversa justifica exp′=exp

O logaritmo tem derivada não nula em todo argumento positivo. Pelo teorema da derivada da inversa, exp é diferenciável e exp′(y)=1/[ln′(exp y)]=1/[1/exp y]=exp y. Em particular, exp′(0)=1. Isso justifica por que a exponencial natural aparece em modelos cuja taxa de variação é proporcional ao próprio valor. Resolver um modelo físico ainda exige hipóteses e condições iniciais próprias.

exp′(y)=exp(y)

## A adição dos argumentos vira multiplicação dos valores

Se u=exp a e v=exp b, então ln(uv)=ln u+ln v=a+b. Pela unicidade da inversa, exp(a+b)=uv=exp(a)exp(b). Para base b>0, podemos agora definir bˣ=exp(x ln b). Sua derivada é bˣ ln b. Para construir log_b como inversa exigimos ainda b≠1; então log_b(x)=ln x/ln b. A base 1 produz a exponencial constante 1 e não possui essa inversa.

## Somas de Riemann dão limites antes de escolher uma aproximação

Em [1,2], a função 1/t é decrescente. Com n faixas uniformes de largura 1/n, os retângulos direitos ficam abaixo da curva e os esquerdos acima. Portanto Rₙ≤ln 2≤Lₙ. Para n=4, R₄=1/5+1/6+1/7+1/8=533/840 e L₄=1/4+1/5+1/6+1/7=319/420. A figura mostra as duas construções. São limites exatos racionais, não uma avaliação decimal feita pela função log.

Rₙ≤ln 2≤Lₙ

## A diferença das somas fornece uma garantia de erro

Ao subtrair Lₙ−Rₙ, os termos internos cancelam: sobra (1/n)(1−1/2)=1/(2n). Se usamos o ponto médio dos dois limites como aproximação, o erro absoluto é no máximo metade dessa largura, 1/(4n). Para n=4, o ponto médio é 1171/1680 e o erro é no máximo 1/16. Trata-se do ponto médio dos limites obtidos, não de aplicar a regra do ponto médio a cada faixa da integral.

Lₙ−Rₙ=1/(2n); erro do centro ≤1/(4n)

## A regra da cadeia exige conservar o domínio

Para ln(2x), o domínio é x>0 e a derivada é 2/(2x)=1/x. Para ln(x²−1), precisamos de x²−1>0, isto é, x<−1 ou x>1; a derivada nesse domínio é 2x/(x²−1). Substituir x=0 nessa última fração não avalia a derivada da função original, que nem está definida em zero. Fórmulas simplificadas precisam continuar acompanhadas do domínio.

## O laboratório certifica limites do modelo de integral

O código recebe x racional positivo e n inteiro positivo, usa somas racionais de 1/t e devolve limites inferior/superior, seu ponto médio e um limite para o erro desse ponto médio. Para x<1, calcula no intervalo [x,1] e troca sinais e ordem dos limites; para x=1, ambos são zero. Nenhuma chamada a log é usada no núcleo. Os testes usam log aproximado como conferência externa e também identidades exatas da largura e do refinamento.

## A construção abre um recorte; não encerra as funções especiais

Refaça a prova do produto, explique por que ln alcança todo real e reconstrua os limites para ln 2 antes de usar o código. A leitura foi parcial no Apostol; as provas e os exemplos destas notas de aula são próprios, assistidos por IA para sua revisão. Inversas trigonométricas têm aula separada no catálogo. Este recorte não desenvolve diferenciação logarítmica mais ampla ou aproximações polinomiais. A situação acadêmica no histórico e o domínio pessoal não foram alterados.

## Exercícios e resoluções

- Quanto vale ln 1 pela definição integral? **Resolução:** Os limites coincidem: integral de 1 a 1 vale zero.
- Quanto vale a derivada de ln x em x=2? **Resolução:** ln′(2)=1/2.
- Escreva ln 8=c ln 2. Qual c? **Resolução:** 8=2³ e a propriedade inteira dá c=3.
- Quanto vale exp(0)? **Resolução:** ln 1=0, então a inversa fornece exp(0)=1.
- Quanto vale exp(ln 3)? **Resolução:** 3 é positivo e a composição inversa devolve 3.
- Quanto vale exp′(0)? **Resolução:** exp′(0)=exp(0)=1.
- Quanto vale a derivada de ln(2x) em x=2? **Resolução:** 2/(2x)=1/x, em x=2 vale 1/2.
- Quanto vale a derivada de ln(x²−1) em x=2? **Resolução:** O ponto está no domínio e 2x/(x²−1)=4/3.
- Qual R₄, soma inferior para ln 2 na aula? **Resolução:** 1/5+1/6+1/7+1/8=533/840.
- Qual L₄, soma superior para ln 2 na aula? **Resolução:** 1/4+1/5+1/6+1/7=319/420.
- Quanto vale L₄−R₄? **Resolução:** 1/(2×4)=1/8.
- Qual a garantia de erro absoluto do ponto médio entre L₄ e R₄? **Resolução:** Metade da largura 1/8 é 1/16.

## Laboratório e referência

Na raiz: `python3 -m unittest discover -s labs/logaritmo-integral -t .` e `python3 -m labs.logaritmo-integral.bounds`. Só biblioteca padrão. x int/Fraction positivo e n int positivo, sem bool/float/texto. Para x<1, somas são construídas em [x,1] e negadas com ordem invertida. Para x=1, limites/erro zero. Núcleo sem log/exp de ponto flutuante; retorna frações e garantia por monotonicidade. O teste usa referência externa aproximada e identidades racionais em 30 pares x/n, além de refinamento, orientação e uma faixa.

Fonte: T. M. Apostol, Calculus, volume I, 2ª edição (1967), §§6.3–6.6 pp.229–232 (PDF249–252) e §6.12 pp.242–243 (PDF262–263), consulta textual parcial em 22/10/2026. O extrator emitiu muitos avisos de sintaxe/OCR ao percorrer o PDF; leitura foi limitada aos trechos legíveis e cabeçalhos identificados, sem alegação de transcrição matemática perfeita ou capítulo integral. Prova por valor médio, exemplos, retângulos e exercícios destas notas são próprios. Nenhuma cópia do PDF foi posta no site.

14 seções/12 exercícios em rascunho assistido por IA. Curso passa a 23 aulas/192 exercícios; mapa de CCM0113 tem dez grupos parciais, sem declarar qualquer um completo. Versão da turma segue não recuperada; aprovação histórica não alterada. Inversas trigonométricas e materiais pessoais continuam pendentes. Próxima revisão pessoal: reconstruir as provas e a garantia antes de rodar o código.

Verificação: cinco testes do laboratório aprovados, incluindo 30 pares de x/n com comparação externa, largura telescópica, limites aninhados, orientação e contratos. Treze testes de catálogo e 572 estruturas MathML aprovados. Navegador em 390 px: documento de 375 px, retângulos e limites inspecionados; questão 12 rejeitou 1/8 e aceitou 1/16. Navegação do novo módulo do curso à aula confirmada, aprovação histórica e pendência de inversas trigonométricas preservadas. Console sem erros observados. Prévia logaritmo-integral-mobile.jpg. Catálogo 508 aulas/3303 exercícios, 254 aulas com até três seções; cobertura recalculada. Sem revalidação global dos demais laboratórios, consulta à versão da turma ou revisão pessoal. Saldo semanal confirmado após bloco: 89%; parada em 65%. Próxima revisão pessoal: provar produto/inversa e o erro da aproximação; próximo recorte próprio de funções especiais: inversas trigonométricas, domínio e ramo.
