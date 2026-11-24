# Frações parciais: identidade e domínio

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão de Jhuann.

## Primeiro observe graus, fatores e domínio

Uma função racional é apresentada como quociente de polinômios. Registre primeiro os zeros do denominador: esses pontos não pertencem ao domínio da expressão original. Se o grau do numerador é pelo menos o do denominador, faça divisão polinomial antes. Na parcela própria restante, a fatoração real do denominador orienta a forma das frações parciais. A decomposição reorganiza a expressão onde ela existe; não autoriza apagar suas restrições de domínio.

1/[x(x+1)]=A/x+B/(x+1)

## O exemplo simples por coeficientes

Procure A e B para 1/[x(x+1)]=A/x+B/(x+1), com x≠0,−1. Ao reunir os termos, o numerador é A(x+1)+Bx=(A+B)x+A. Para ser identicamente igual a um, precisamos de A=1 e A+B=0. Logo B=−1. Recombinar as frações devolve o numerador um e o denominador x(x+1), uma verificação algébrica para todo ponto permitido.

1/[x(x+1)]=1/x−1/(x+1)

## Primitivas vivem em intervalos do domínio

Uma primitiva é F(x)=ln|x|−ln|x+1|. Sua derivada é 1/x−1/(x+1), em qualquer um dos intervalos (−∞,−1), (−1,0) e (0,∞). O valor absoluto permite escrever uma mesma fórmula real nos três intervalos, mas não torna os polos válidos. Cada componente pode receber sua própria constante aditiva: a derivada não impõe uma relação entre constantes de intervalos desconectados.

F(x)=ln|x|−ln|x+1|

## Quando é preciso dividir antes

Considere (x²+1)/(x²+x). Os graus são iguais, então divida: x²+1=(x²+x)+(1−x). A parcela própria é (1−x)/[x(x+1)]. Comparando coeficientes em A(x+1)+Bx=1−x, obtemos A=1 e B=−2. Portanto a expressão é 1+1/x−2/(x+1), para x≠0,−1. Uma primitiva é x+ln|x|−2ln|x+1| em cada intervalo do domínio. O termo polinomial um não pode desaparecer.

(x²+1)/(x²+x)=1+1/x−2/(x+1)

## Um fator repetido exige todas as potências

Agora use f(x)=(2x+3)/[x(x+1)²], com x≠0,−1. A forma a testar é A/x+B/(x+1)+C/(x+1)². O fator repetido (x+1)² pede espaço para os termos com potência um e dois. Reunindo denominadores, o numerador fica A(x+1)²+Bx(x+1)+Cx. Omitir um desses termos pode tornar impossível a identidade. A existência geral da decomposição é um resultado algébrico; aqui verificaremos esta família diretamente.

f(x)=A/x+B/(x+1)+C/(x+1)²

## Determinar os três coeficientes sem saltos

Expanda o numerador proposto: (A+B)x²+(2A+B+C)x+A. Para coincidir com 2x+3, compare os coeficientes: A+B=0, 2A+B+C=2 e A=3. Da primeira igualdade, B=−3. Na segunda, 6−3+C=2, portanto C=−1. O numerador reconstruído é 0x²+2x+3, exatamente o desejado. Assim a verificação não depende apenas de testar alguns valores de x.

A=3; B=−3; C=−1

## Substituir um polo na identidade não avalia a função nele

Depois de escolher coeficientes, podemos verificar a igualdade polinomial 2x+3=A(x+1)²+Bx(x+1)+Cx em qualquer x. Nessa identidade, x=0 dá A=3 e x=−1 dá −C=1. Isso é diferente de calcular a função racional nesses pontos: suas frações continuam indefinidas ali. A igualdade polinomial é uma ferramenta para achar ou conferir coeficientes, não uma extensão automática do domínio.

2x+3=3(x+1)²−3x(x+1)−x

## Integrar e conferir o sinal do termo repetido

A decomposição é 3/x−3/(x+1)−1/(x+1)². Os dois primeiros termos integram em 3ln|x| e −3ln|x+1|. Como a derivada de 1/(x+1) é −1/(x+1)², o terceiro termo integra em +1/(x+1). Portanto F=3ln|x|−3ln|x+1|+1/(x+1) é uma primitiva em cada intervalo permitido. Derivar cada parcela e recombinar confirma f. O sinal positivo do último termo da primitiva é essencial.

F=3ln|x|−3ln|x+1|+1/(x+1)

## Um fator quadrático real pede numerador linear

Se um fator quadrático não tem raízes reais, não o substitua por fatores lineares reais inexistentes. Para x²+1, uma parcela de decomposição pode ter numerador Ax+B. Por exemplo, (2x+3)/(x²+1) se separa em 2x/(x²+1)+3/(x²+1). Uma primitiva é ln(x²+1)+3arctan(x), pois x²+1 é positivo e sua derivada é 2x. Esse exemplo mostra duas formas básicas, sem desenvolver todos os casos de quadráticos repetidos.

F=ln(x²+1)+3arctan(x)

## Integral definida sem atravessar singularidades

Retome g(x)=1/[x(x+1)]. O intervalo [1,2] está dentro de (0,∞), onde g é contínua. Podemos aplicar o teorema fundamental: F(2)−F(1)=[ln2−ln3]−[ln1−ln2]=ln4−ln3=ln(4/3). O resultado é positivo, coerente com g positiva nesse intervalo. Antes de substituir extremos, confira sempre o intervalo inteiro, não só a existência da função nos extremos.

Integral de g em [1,2]=ln(4/3)

## Extremos válidos não garantem uma integral própria

O intervalo [−1/2,1/2] contém o polo zero de g. A função existe nos dois extremos, mas não é contínua no intervalo. Uma integral imprópria precisa ser separada em limites laterais, e ambos precisam convergir para que a integral usual exista. Perto de zero, a primitiva ln|x|−ln|x+1| diverge: as integrais laterais não convergem a valores finitos. Não se cancelam infinitos e não se usa diretamente F(1/2)−F(−1/2). Um valor principal, quando definido, é outro conceito.

## O que a verificação exata cobre

O laboratório trata a família (ax+b)/[x(x+1)²]. A fórmula A=b, B=−b, C=a−b é conferida pela expansão dos três coeficientes polinomiais e por avaliações com frações exatas. O código preserva os pontos excluídos da expressão original, mesmo em parâmetros que permitam simplificação. Um verificador de intervalo detecta se o caminho entre os extremos inclui −1 ou zero. Isso não é um integrador geral nem uma prova de convergência de toda integral imprópria. Fatoração geral, casos quadráticos repetidos e algoritmos simbólicos completos permanecem pendentes.

## Exercícios e resoluções

- Qual B? **Resolução:** A+B=0 com A=1.
- Decompor a fração permite incluir x=0 no domínio? **Resolução:** O polo não foi removido.
- Na decomposição de (2x+3)/[x(x+1)²], qual é A, coeficiente de 1/x? **Resolução:** A constante do numerador reconstruído é A=3.
- Na mesma decomposição, qual é B, coeficiente de 1/(x+1)? **Resolução:** A+B=0 e A=3, logo B=−3.
- Na mesma decomposição, qual é C, coeficiente de 1/(x+1)²? **Resolução:** 2A+B+C=2: 6−3+C=2, então C=−1.
- Quanto vale (2x+3)/[x(x+1)²] em x=1? **Resolução:** (2+3)/(1×4)=5/4. A decomposição dá 3−3/2−1/4=5/4.
- Qual é o quociente polinomial na divisão de x²+1 por x²+x? **Resolução:** x²+1=1×(x²+x)+(1−x).
- Na primitiva ln(x²+1)+3arctan(x), qual é o coeficiente de arctan(x)? **Resolução:** O termo 3/(x²+1) integra em 3arctan(x).
- Para o fator repetido (x+1)², quais termos devem ser permitidos na forma da decomposição? **Resolução:** Permitem-se todas as potências até a multiplicidade do fator.
- Substituir x=0 na identidade polinomial dos numeradores torna f(0) definida? **Resolução:** A identidade polinomial pode ser avaliada em zero; a função racional original continua excluindo esse ponto.
- Qual termo integra −1/(x+1)²? **Resolução:** A derivada de +1/(x+1) é −1/(x+1)².
- Podemos calcular a integral usual de 1/[x(x+1)] em [−1/2,1/2] apenas substituindo os extremos numa primitiva? **Resolução:** O intervalo atravessa o polo zero; os limites laterais precisam ser analisados e neste caso divergem.

## Fontes e execução

Apostol, Calculus I, exemplar do acervo, §6.23, p.258 e pp.260–263 (PDF278 e 280–283), leitura textual parcial; [OpenStax, Calculus Volume 2, §3.4](https://openstax.org/books/calculus-volume-2/pages/3-4-partial-fractions), início e fatores simples, consulta parcial em 22/10/2026. Sem reprodução de exercícios ou páginas. Exemplo racional, figura, domínio e código locais originais.

Na raiz: python3 -m labs.fracoes-polos.experiment; testes: python3 -m unittest discover -s labs/fracoes-polos -t .

O código usa int ou Fraction. proper_interval apenas verifica os pontos excluídos da expressão especificada; não calcula integrais nem decide convergência em qualquer problema.


## Frações parciais, identidade e domínio — 22/10/2026

Aula c2-fracoes-parciais ampliada de três seções/dois exercícios para 12 seções/12 exercícios. Exemplo inicial 1/[x(x+1)], código, desafio e IDs antigos preservados. Novos recortes: divisão antes de decompor, todas as potências de fator repetido, identidade polinomial, coeficientes, primitiva verificada por derivação, numerador linear em quadrático e intervalo de integração. A técnica continua apoio editorial complementar ao programa recuperado; os seis grupos oficiais permanecem parciais.

Fontes primárias: Apostol I, exemplar do acervo, §6.23, p.258 e pp.260–263 (PDF278 e 280–283), leitura textual parcial em 22/10/2026. [OpenStax, Calculus Volume 2, §3.4](https://openstax.org/books/calculus-volume-2/pages/3-4-partial-fractions), início e fatores simples, consulta parcial na mesma data. Não se afirma leitura integral. Exemplos, decomposição da família, figura e código locais são originais; sem reprodução de páginas ou exercícios.

Família (ax+b)/[x(x+1)²]: A=b, B=−b, C=a−b. Para a=2,b=3: A=3,B=−3,C=−1. Recombinar produz os coeficientes (3,2,0), em ordem crescente, do numerador 2x+3. Primitiva 3ln|x|−3ln|x+1|+1/(x+1), em cada componente de domínio; constantes podem diferir entre componentes. Para g=1/[x(x+1)], integral em [1,2] é ln(4/3); cruzar o polo zero não permite aplicar diretamente a avaliação por primitiva. Não foi adotado valor principal.

Laboratório em labs/fracoes-polos/: cinco testes novos aprovados. Identidade polinomial para 121 pares de coeficientes, avaliações racionais para 49 pares, termo repetido indispensável, pontos excluídos e orientação dos intervalos, contratos de entrada. Doze testes de catálogo e 534 estruturas MathML aprovados após figura e integração no percurso. Nenhum modelo JavaScript alterado; suíte global não repetida.

Navegador: diagrama e texto legíveis a 390 px, largura da página igual à tela e nenhum erro de console observado. Coeficiente −1 e valor 5/4 aceitos nas novas atividades. Prévia fracoes-polos-mobile.jpg. O percurso recebeu uma sétima etapa explicitamente opcional, de apoio às técnicas de integração. Nenhuma atividade pessoal ou aprovação acadêmica foi inferida.

Estado: 21 aulas/127 exercícios em Cálculo II, 11 introduções curtas; seis grupos oficiais parciais. Catálogo global 500 aulas/3012 exercícios em rascunho. Próxima revisão pessoal: reconstruir os coeficientes 3,−3,−1, derivar a primitiva e explicar por que a avaliação nos extremos não basta ao atravessar zero. Próximo bloco global: aprofundar um primeiro assunto de deep learning, como neurônio e regra da cadeia, após conferir fonte e material existente. Notas pessoais e domínio demonstrado continuam pendentes. Saldo semanal após o bloco: 93%; parada operacional em 65%.
