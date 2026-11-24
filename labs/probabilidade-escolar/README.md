# Probabilidade escolar — resultados, pesos e agrupamento

## Um resultado e um evento não são a mesma coisa

Descreva primeiro o procedimento e o espaço amostral Ω, conjunto dos resultados possíveis. No modelo de um dado de seis faces, Ω={1,2,3,4,5,6}. Uma jogada produz um resultado, como 4. O evento “sair par” reúne os resultados {2,4,6}. Ele ocorre se o resultado pertence a esse conjunto. A probabilidade é um número atribuído ao evento pelo modelo; não é uma face adicional do dado.

## A razão de contagens exige resultados equiprováveis

Se cada face tem probabilidade 1/6, a chance de sair par é 1/6+1/6+1/6=3/6=1/2. A forma “favoráveis divididos por possíveis” funciona porque as parcelas têm o mesmo peso. O dado justo é uma hipótese do exemplo; a simetria descrita no modelo não é uma inspeção de um dado real. Ser imprevisível não obriga que todos os resultados sejam igualmente prováveis.

P(A)=|A|/|Ω| no modelo finito uniforme

## Quando os pesos diferem, some os pesos relevantes

Considere dois rótulos de resultado, vermelho e azul, com pesos sintéticos 3 e 1. Após normalizar pela massa total 4, P(vermelho)=3/4 e P(azul)=1/4. Contar um rótulo favorável entre dois daria 1/2 para ambos, contrariando o modelo. Uma distribuição precisa de probabilidades não negativas que somem 1; um evento pode ter probabilidade zero. Esses pesos foram escolhidos para o exemplo, não medidos em uma experiência.

## Dois dados devem ser representados por pares ordenados

Adote dois dados ideais de seis faces, distinguíveis entre si e independentes. O espaço tem 6×6=36 pares (a,b), todos com probabilidade (1/6)(1/6)=1/36. Os pares (2,5) e (5,2) são resultados diferentes, pois identificamos qual dado mostra cada face. “Ambos pares” contém 3×3=9 resultados; sua probabilidade é 9/36=1/4. A equiprobabilidade desses pares usa as hipóteses de uniformidade e independência.

## Agrupar pela soma preserva os pesos, não a equiprobabilidade

A soma pode valer de 2 a 12, mas esses 11 valores não têm o mesmo peso. A soma 2 aparece somente em (1,1). A soma 7 aparece em (1,6),(2,5),(3,4),(4,3),(5,2),(6,1). Portanto P(soma 2)=1/36 e P(soma 7)=6/36=1/6. Usar 1/11 para cada soma esqueceria quantos pares foram reunidos em cada grupo. A altura das barras da figura conta pares; para obter a probabilidade, dividimos por 36.

## “Ao menos um seis” usa uma união com sobreposição

Seja A o evento de o primeiro dado mostrar 6, e B o de o segundo mostrar 6. Cada evento contém seis pares. Ao somar as contagens, (6,6) aparece duas vezes; por isso a união contém 6+6−1=11 pares. Logo P(A∪B)=11/36. Em geral, P(A∪B)=P(A)+P(B)−P(A∩B). O “ou” desta união inclui a possibilidade de ambos ocorrerem.

P(A∪B)=P(A)+P(B)−P(A∩B)

## O complemento oferece outro caminho para a mesma conta

O complemento de “ao menos um seis” é “nenhum dado mostra seis”. Cada dado pode mostrar uma entre cinco faces, produzindo 5×5=25 pares. A chance é 25/36, então o evento inicial tem probabilidade 1−25/36=11/36. Complementos não se sobrepõem e cobrem todo o espaço; suas probabilidades somam 1. Distinguir “nenhum”, “ao menos um” e “exatamente um” evita trocar a pergunta.

## “Exatamente um seis” exclui o caso de dois seis

Há cinco pares em que só o primeiro dado mostra 6 e cinco em que só o segundo mostra 6. São conjuntos disjuntos, totalizando dez pares e probabilidade 10/36=5/18. A união de “ao menos um” também inclui (6,6), portanto tem 11 pares. Duas frases próximas podem definir eventos diferentes; escrever os pares ou as restrições ajuda a conferir a interpretação.

## Independência é uma hipótese de fatoração

Dois eventos são independentes se P(A∩B)=P(A)P(B). No modelo dos dois dados, A: primeiro mostra 6 e B: segundo mostra 6 têm conjunta 1/36=(1/6)(1/6). A palavra “e” indica interseção, mas só permite multiplicar probabilidades marginais quando a independência for válida. Para dados reais, o procedimento e o mecanismo precisam sustentar o modelo; o código não verifica isso.

Independência: P(A∩B)=P(A)P(B)

## Eventos disjuntos de probabilidades positivas não são independentes

Em um único dado justo, A: sair 1 e B: sair 2 são disjuntos: não ocorrem na mesma jogada. A conjunta é zero, mas o produto das marginais é (1/6)(1/6)=1/36. Portanto não são independentes. A impossibilidade de ocorrerem juntos é diferente de não alterar probabilidades. Não use “independentes” como sinônimo de “diferentes” ou de “sem resultados em comum”.

## Frequência observada e probabilidade do modelo precisam ser distinguidas

Ao observar dez lançamentos, uma face pode aparecer três vezes. A frequência relativa dessa face nessa amostra é 3/10. Isso não altera automaticamente a probabilidade 1/6 do modelo de dado justo, nem prova que a face tem chance real 3/10. Avaliar o modelo com dados exige considerar tamanho da amostra, coleta e variação aleatória. Um resultado não observado também não está, por isso só, provado impossível.

## O laboratório confere a distribuição, mas não certifica um dado real

O código enumera pares de dados ideais e soma pesos para cada evento. Aceita pesos racionais não negativos com massa total positiva; não supõe que todo rótulo tem a mesma chance. Os testes conferem normalização, complementos, união e multiplicidades das somas. A enumeração exata verifica o modelo finito escolhido, não o mecanismo de um instrumento real ou sua aprendizagem. Probabilidade condicional e inferência com dados observados seguem em outras aulas e precisam de revisão própria.

## Exercícios e resoluções originais

- Em duas jogadas independentes de um dado justo, qual a probabilidade de ambos os resultados serem pares? **Resolução:** Cada jogada tem três faces pares em seis: (1/2)(1/2)=1/4. Equivale a nove pares favoráveis entre 36.
- Contar casos favoráveis/possíveis vale sem verificar equiprobabilidade? **Resolução:** Casos podem ter probabilidades diferentes.
- Em um dado justo de seis faces, qual a probabilidade de sair par? **Resolução:** Há três faces pares entre seis: 3/6=1/2.
- Nos dois dados ideais e independentes, qual a probabilidade de soma 7? **Resolução:** Seis pares geram 7: 6/36=1/6.
- Nos mesmos dados, qual a probabilidade de soma 2? **Resolução:** Apenas (1,1): 1/36.
- Qual a probabilidade de soma 11 nos dois dados? **Resolução:** Os pares (5,6) e (6,5): 2/36=1/18.
- Qual a probabilidade de ao menos um dado mostrar 6? **Resolução:** 6+6−1=11 pares favoráveis entre 36.
- Qual a probabilidade de nenhum dos dois dados mostrar 6? **Resolução:** Cinco opções em cada dado: 25/36.
- Qual a probabilidade de ambos os dados mostrarem 6? **Resolução:** Somente (6,6), com probabilidade 1/36.
- Qual a probabilidade de exatamente um dado mostrar 6? **Resolução:** São 5+5=10 pares: 10/36=5/18.
- Rótulos vermelho/azul têm pesos 3 e 1. Qual P(azul)? **Resolução:** Peso azul dividido pelo total: 1/(3+1)=1/4.
- Uma face apareceu 3 vezes em 10 lançamentos. Isso prova que sua probabilidade é 0,3? **Resolução:** Uma amostra apresenta variação; avaliar a probabilidade requer modelo e análise da coleta.

## Código e fonte

Na raiz: `python3 -m unittest discover -s labs/probabilidade-escolar -t .` e `python3 -m labs.probabilidade-escolar.finite`. Só biblioteca padrão. dice_weights recebe faces int positivas sem bool e produz pares ordenados com pesos iguais. probability aceita dict não vazio de pesos int/Fraction não negativos e evento contido no espaço; massa total deve ser positiva. sum_distribution agrega pesos por soma. Nenhuma função testa uniformidade ou independência de dados reais.

Testes comparam a distribuição enumerada à contagem triangular e aos momentos conhecidos para 1–12 faces; conferem simetria, normalização, união, complemento, peso nulo e contratos. Os cálculos são exatos em Fraction. O gráfico mostra contagens dos 36 pares, não frequências medidas.

Fonte: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.1, pp.49–51 (PDF64–66), e §2.2, p.56 (PDF71), consulta textual parcial do acervo autorizado em 22/10/2026. Não se disponibilizou cópia do livro nem se reproduziram suas figuras, exercícios ou dados. Material, gráfico e exemplos próprios assistidos por IA para revisão.

Aula existente aprofundada de três para 12 seções e de dois para 12 exercícios, IDs antigos preservados e pergunta numérica sem contexto corrigida. Próxima revisão pessoal: explicar por que as somas não têm peso 1/11 e reconstruir 11/36 por dois caminhos. Condicionamento mais amplo e inferência continuam em outros percursos, sem equivalência com domínio do material preparado.

Verificação: cinco testes do laboratório aprovados, incluindo distribuição triangular/momentos para 1–12 faces, normalização, agrupamento, união, complemento, peso zero e contratos. Treze testes de catálogo e 568 estruturas MathML aprovados. Figura com rótulos ampliados inspecionada no navegador a 390 px; documento de 375 px, sem transbordamento horizontal; questão 4 rejeitou 1/11 e aceitou 1/6. Console sem erros observados. Prévia probabilidade-somas-mobile.jpg. Catálogo 507 aulas/3291 exercícios, 254 aulas com até três seções; cobertura recalculada. Não se revalidou toda a suíte dos demais laboratórios nem se testou um dado real. Saldo semanal confirmado após bloco: 89%; parada em 65%. Próxima revisão pessoal: reconstruir as somas e os dois caminhos para 11/36. Após estes recortes escolares, retomar uma lacuna de disciplina básica/complementar; estatística e gráficos escolares ainda curtos.
