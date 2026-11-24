# Arredondamento e cancelamento — notas de aula

## Representar já é aproximar

Um formato de ponto flutuante tem um conjunto finito de números. Muitas frações decimais, como 1/10, não têm expansão binária finita. No ambiente verificado, float tem base 2 e precisão de 53 bits significativos. Isso não torna toda operação errada: números e resultados representáveis podem ser exatos. Antes de interpretar o erro, separe o valor pretendido, o valor de entrada efetivamente armazenado e o resultado do procedimento. Esta aula usa exemplos numéricos próprios, sem dados de pesquisa.

## Mostrar 0,1 não significa armazenar exatamente 1/10

A representação textual curta de um float pode esconder seus dígitos completos. Fraction.from_float(0.1) recupera exatamente o racional armazenado: 3602879701896397/36028797018963968, diferente de 1/10. Já Fraction(1,10) representa exatamente a fração decimal pretendida. Converter um float para Fraction depois do fato conserva o float recebido; não adivinha a intenção original do usuário.

## O espaçamento muda com a escala

No formato verificado, o próximo float acima de1 fica a 2⁻⁵². math.ulp(1.0) permite consultar esse espaçamento. Um incremento x=2⁻⁵⁴ é apenas um quarto desse intervalo; ao somá-lo a 1, o valor arredonda para1 neste ambiente. O epsilon de sys.float_info é o espaçamento 2⁻⁵² na escala de 1; não o confunda com a convenção de erro unitário 2⁻⁵³ para arredondamento ao mais próximo. Limites relativos usuais exigem cuidados com resultados subnormais, overflow e underflow.

ulp(1)=2⁻⁵²; fl(1+2⁻⁵⁴)=1

## Subtrair pode expor o erro que já ocorreu

No laço ingênuo para [1e16,1.0,−1e16], somar1 ao acumulador1e16 perde essa contribuição; subtrair1e16 depois retorna 0. O erro surgiu antes da subtração final. Cancelamento entre quantidades próximas pode expor erros de representação ou de operações anteriores: não é correto atribuir sempre toda a perda à instrução de subtrair, que pode até ser exata para os operandos já recebidos.

## A ordem da soma faz parte do procedimento

A soma matemática das três parcelas é 1. O laço explícito total+=valor devolve 0 para [1e16,1.0,−1e16] e1 para [1e16,−1e16,1.0]. Os arredondamentos acontecem em etapas diferentes. Isso mostra que a associatividade dos números reais não se transporta automaticamente à execução em float. Não usamos o sum nativo como sinônimo desse laço: versões recentes do Python podem usar uma acumulação melhor.

## fsum melhora a acumulação dentro de seu alcance

math.fsum acompanha somas parciais e devolve 1 nas duas ordens do exemplo. A documentação registra hipóteses e possíveis efeitos de arredondamento duplo; isso não é garantia universal de resultado exato, de ausência de overflow ou de recuperação de informação perdida na entrada. Se você calcula primeiro u=1e16+1.0 e só então passa [u,−1e16], os dados recebidos já têm soma exata 0; fsum também retorna 0.

## Erro absoluto e relativo precisam de uma referência declarada

Para referência r e aproximação r̂, erro absoluto é |r̂−r|. Se r≠0, o erro relativo é |r̂−r|/|r|. Um número pequeno em valor absoluto pode ter erro relativo enorme se a referência também for pequena. Se r=0, esta definição de erro relativo não existe; o laboratório retorna None, preservando o erro absoluto. Para decidir se uma diferença é aceitável, o problema precisa fornecer escala e tolerância.

erro relativo=|r̂−r|/|r|, r≠0

## Reescrever a expressão pode evitar a combinação ruim de escalas

Considere f(x)=(1+x)²−1 para 0≤x≤1/4. Pela distributividade nos reais, f(x)=1+2x+x²−1=x(2+x). A primeira forma soma um incremento a 1, eleva o resultado ao quadrado e subtrai1. A segunda trabalha diretamente com o incremento. São funções matematicamente iguais, mas sequências distintas de operações arredondadas.

(1+x)²−1=x(2+x)

## Um incremento representável pode desaparecer em uma operação

Escolha x=2⁻⁵⁴, que é representável exatamente. A referência racional é r=2x+x²>0. Na forma ingênua, fl(1+x)=1 e a saída é 0; o erro relativo é1, ou 100%. Na forma reformulada, o ambiente verificado retorna 2x=2⁻⁵³. Ela ainda omite o termo x², mas o erro relativo é x²/(2x+x²)=x/(2+x), aproximadamente 2⁻⁵⁵. A boa resposta não é exatamente a referência: é uma aproximação com erro muito menor.

r=2x+x²; ingênua=0; reformulada=2x

## A referência exata não pode repetir o mesmo arredondamento

Para avaliar o procedimento com a entrada recebida, o código primeiro cria q=Fraction.from_float(x), e só então calcula 2q+q² em aritmética racional. Usar Fraction((1.0+x)**2−1.0) converteria em fração uma saída já arredondada, não a referência real desejada. O experimento mede o erro de cálculo sobre o float recebido; a diferença entre esse float e um dado decimal originalmente pretendido é outra camada de erro.

## Condicionamento do problema e estabilidade do procedimento diferem

Para x>0 neste recorte, f′(x)=2+2x. A sensibilidade relativa local é κ(x)=|xf′(x)/f(x)|=(2+2x)/(2+x), próxima de 1 quando x é pequeno. Pequenas perturbações relativas da entrada não são enormemente amplificadas pela função. Apesar disso, a forma ingênua pode devolver zero. O exemplo separa um problema localmente bem condicionado de um procedimento ruim nesse regime; a sensibilidade local não descreve perturbações arbitrariamente grandes nem define erro relativo em x=0.

κ(x)=(2+2x)/(2+x), x>0

## A reformulação tem domínio e limites

O laboratório limita a comparação a 0≤x≤1/4 e aceita somente floats finitos explicitamente fornecidos. Não afirma que x(2+x) é a melhor forma para todo x. Perto de−2, essa forma também pode envolver combinação de valores próximos; em escalas enormes, produtos podem exceder o formato. Overflow, subnormais e a plataforma precisam ser tratados conforme a aplicação. Os testes incluem valores pequenos, inclusive o menor float positivo do ambiente, mas não provam estabilidade universal.

## A mesma álgebra aparece em diferenças de energia

Se uma velocidade muda de v para v+δ, a diferença dos quadrados é (v+δ)²−v²=δ(2v+δ). Quando δ é pequeno em relação a v, calcular dois quadrados grandes e depois subtrair pode expor perda de precisão. Para energia cinética com massa constante, multiplique essa expressão por m/2 e confira as unidades. A identidade não determina se δ foi medido com precisão nem quais forças produziram a mudança; ela melhora a organização do cálculo no regime apropriado.

## Diagnosticar exige seguir o caminho dos dados

Registre formato e versão do ambiente, construa uma referência independente, compare erros absoluto/relativo e teste escalas relevantes. Só depois escolha ordem de soma, reformulação, maior precisão ou outro método. O laboratório confere casos finitos, não calibra dados físicos e não garante que aumentar precisão resolva um modelo errado. Bibliografia e exemplos servem de notas originais assistidas por IA para revisão de Jhuann; domínio pessoal e uso em pesquisa ainda exigem demonstração própria.

## Exercícios originais e resoluções

Qual é a soma matemática exata de 10¹⁶+1−10¹⁶? **Resolução:** As parcelas grandes se cancelam e resta 1.

Uma soma mais estável recupera qualquer dado já perdido antes da entrada? **Resolução:** O algoritmo só pode trabalhar com os valores que recebeu.

No formato verificado, qual o resultado em float de 1.0+2⁻⁵⁴? **Resolução:** O incremento é um quarto do espaçamento para o próximo float acima de1, e a soma arredonda para 1.

Com x=2⁻⁵⁴, qual a saída da forma ingênua (1.0+x)*(1.0+x)−1.0? **Resolução:** A soma intermediária vira 1. Então1×1−1=0.

Se a referência r>0 e a aproximação é0, qual o erro relativo |0−r|/|r|? **Resolução:** r/r=1, equivalente a100%.

No exemplo x=2⁻⁵⁴, a forma reformulada retorna 2x. Quanto é saída/x? **Resolução:** A saída é o dobro de x. A referência ainda inclui x².

Qual o valor matemático de (1+x)²−1 para x=1/4? **Resolução:** 2(1/4)+(1/4)²=1/2+1/16=9/16.

Qual o valor matemático para x=1/8? **Resolução:** 1/4+1/64=17/64.

Qual a saída do laço ingênuo para [1e16,−1e16,1.0] neste exemplo? **Resolução:** As parcelas grandes se cancelam primeiro e depois entra 1.

Se u=1e16+1.0 já arredondou para1e16, qual fsum([u,−1e16])? **Resolução:** As entradas recebidas somam exatamente0; a contribuição perdida antes não reaparece.

Se a referência é zero, |aproximação−referência|/|referência| define um erro relativo finito? **Resolução:** O denominador é zero. O laboratório retorna None e mantém o erro absoluto.

Neste exemplo, κ(x) próximo de1 garante que a forma ingênua será precisa para x pequeno? **Resolução:** κ mede sensibilidade do problema; a sequência de operações ingênua pode perder a contribuição em1+x.

## Fontes e limites

Burden, Faires e Burden — Análise Numérica, tradução da10ª edição, edição brasileira2016 do acervo autorizado; documentação oficial Python3.14.

Burden §1.2: p.16 (PDF30) e pp.20–21 (PDF34–35), leitura visual parcial em26/10/2026 sobre representação, erros e aritmética finita. Sumário PDF11 reconferido; não se leu toda a seção. Tutorial oficial Python3.14 de ponto flutuante e math.fsum consultados na mesma data. Exemplo polinomial, derivação, figura e testes originais.

[Python: representação de floats](https://docs.python.org/3.14/tutorial/floatingpoint.html) e [math.fsum](https://docs.python.org/3.14/library/math.html#math.fsum). A versão exibida da documentação é3.14.10; não se presume identidade com o patch do Python local.

`compare_expression(x)` exige float finito em[0,1/4]; retorna a referência exata sobre a entrada recebida, saídas e erros racionais. Erro relativo é None quando referência zero. `compare_sum(values)` recebe lista/tupla de floats finitos e soma em laço, fsum e frações. Não recupera intenções decimais e não trata somas com overflow.

Executar: `python3 -m unittest discover -s labs/arredondamento-cancelamento -t .`. Os testes registram base 2/53bits do ambiente e conferem uma grade de potências, valores extremos, seis ordens da soma, erros de entrada e contratos; não constituem prova de estabilidade geral. Rascunho assistido por IA, sem dados reais, com revisão de Jhuann pendente. PDFs e páginas dos livros não distribuídos.
