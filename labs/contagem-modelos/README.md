# Contagem — ordem, repetição e protocolo

## Defina quando dois resultados são diferentes

Antes de contar, descreva um resultado completo. A dupla formada por Ana e Bia é a mesma se os nomes forem escritos em ordem trocada? Se há cargos de presidente e vice, trocar as pessoas muda o resultado. Se estamos apenas escolhendo uma dupla, não muda. Também precisamos dizer se uma opção pode aparecer mais de uma vez e se há restrições entre as escolhas. A fórmula depende dessas decisões.

## Etapas com o mesmo número de continuações permitem multiplicar

Com três camisetas e duas calças, todas as combinações permitidas produzem 3×2=6 conjuntos de roupa. Para cada escolha da primeira etapa há duas continuações. Se uma combinação específica é proibida, ficam cinco conjuntos, e não seis. O princípio multiplicativo de contagem não exige declarar independência probabilística; ele exige contar corretamente as possibilidades de cada etapa. Somar serve para alternativas disjuntas, sem contar o mesmo resultado duas vezes.

## Ordem conta e repetição é proibida: as opções diminuem

Escolha três pessoas entre cinco para três cargos distintos, sem acumular cargos. Há cinco escolhas para o primeiro cargo, quatro para o segundo e três para o terceiro. O total é 5×4×3=60. Cada resultado é uma sequência de três pessoas diferentes. Se a ordem fosse ignorada, esses 60 registros contariam o mesmo grupo várias vezes. O enunciado precisa dizer qual desses objetos interessa.

A(5,3)=5×4×3=60

## O fatorial resume produtos de inteiros consecutivos

O símbolo k! significa k(k−1)…2×1 para k≥1. Por exemplo, 3!=6 e 5!=120. Para n opções e k posições distintas sem repetição, com 0≤k≤n, A(n,k)=n!/(n−k)!. O quociente cancela os fatores que não entram nas k escolhas. A convenção 0!=1 é compatível com o único arranjo vazio: não escolher nada. No caso k=n, ordenar todos os n objetos dá n!.

A(n,k)=n!/(n−k)!

## Sem ordem e sem repetição: cada grupo apareceu k! vezes

Um grupo de três pessoas distintas pode ocupar os três cargos em 3!=6 ordens. Todos os grupos têm essa mesma multiplicidade; por isso 60/6=10 grupos. Em geral, C(n,k)=n!/[k!(n−k)!]. Para a dupla entre quatro pessoas do exemplo inicial, os 12 pares ordenados se agrupam de dois em dois e produzem seis duplas. A divisão precisa ser justificada por uma multiplicidade igual para cada resultado final.

C(n,k)=n!/[k!(n−k)!]

## Com ordem e repetição: cada posição conserva as opções

Agora use cinco símbolos para formar sequências de três posições, permitindo repetir símbolos. Cada posição tem cinco opções; o total é 5³=125. A sequência AAB difere de ABA, pois a ordem importa, e AAA também é permitida. Para n tipos e k posições livres, o total é nᵏ. A possibilidade de repetir é parte do protocolo, não algo que podemos acrescentar depois de aplicar a fórmula sem repetição.

## Compare os quatro modelos com os mesmos números

Mantendo n=5 e k=3, temos 60 sequências sem repetição, 10 grupos sem repetição e 125 sequências com repetição. Se também ignorarmos a ordem, mas permitirmos repetir tipos, há 35 escolhas, como a extensão abaixo justificará. Os quatro números respondem a quatro perguntas. Nenhum deles é a resposta universal para “escolher três entre cinco”. A figura organiza as hipóteses antes de mostrar as contas.

## Dividir por k! falha quando as multiplicidades não são iguais

Use apenas A e B em três posições. Há oito sequências. Ignorando a ordem, elas formam quatro grupos: AAA, AAB, ABB e BBB. AAA aparece uma vez; AAB aparece em três sequências, AAB, ABA e BAA. Os grupos não têm a mesma multiplicidade. Portanto dividir 8 por 3!=6 não conta esses grupos corretamente. A razão usada para pessoas distintas não se transporta automaticamente para escolhas com repetição.

## Extensão: escolhas com repetição podem ser organizadas sem ordem

Represente os tipos por 0,…,n−1 e escreva uma escolha sem ordem como sequência não decrescente x₀≤…≤xₖ₋₁. Transforme cada posição em yᵢ=xᵢ+i. Os yᵢ passam a ser distintos e estritamente crescentes, escolhidos entre 0 e n+k−2. A transformação inversa subtrai i, então não perdemos nem duplicamos escolhas. Logo, para n≥1, há C(n+k−1,k) possibilidades. Com n=5 e k=3, C(7,3)=35. É uma dedução própria por correspondência, não uma aplicação de dividir todas as sequências pelo mesmo fatorial.

Sem ordem, com repetição: C(n+k−1,k)

## Restrições mudam a contagem de cada etapa

Considere sequências de três símbolos usando 0,1,2,3,4, com repetição permitida, mas com primeiro símbolo diferente de zero. A primeira posição tem quatro opções; as outras duas têm cinco. O total é 4×5×5=100. Não precisamos proibir o zero em todas as posições. Se uma restrição depender do símbolo já escolhido, talvez seja necessário separar casos ou enumerar as sequências, em vez de usar um único produto sem justificativa.

## A escolha vazia e os casos impossíveis também têm significado

Há uma forma de escolher zero posições: a sequência vazia ou o grupo vazio, inclusive se não há opções disponíveis. Se k>n e a repetição é proibida, não existe resultado e a contagem é zero. O laboratório trata esses casos explicitamente, recebe n e k como inteiros não negativos e exige declarar ordem e repetição. Retorna um inteiro exato. Os testes geram sequências pequenas e, quando necessário, agrupam versões ordenadas para conferir a contagem.

## Contar possibilidades ainda não atribui probabilidades

Para converter uma contagem em probabilidade por razão entre casos favoráveis e possíveis, os resultados contados precisam ser equiprováveis no modelo. Ignorar a ordem pode formar grupos com pesos diferentes: no exemplo das oito sequências equiprováveis, AAA tem peso 1/8 e AAB tem peso 3/8. Os quatro grupos não são equiprováveis. Ao ligar esta aula à probabilidade, preserve o protocolo e os pesos. Os exemplos são didáticos originais, não registros de uma coleta ou comprovação de domínio pessoal.

## Exercícios e resoluções originais

- Quantas duplas sem cargos podem ser formadas entre quatro pessoas, sem repetição? **Resolução:** Há 4×3=12 pares ordenados e cada dupla aparece duas vezes: 12/2=6.
- Presidente e vice formam um resultado sem ordem? **Resolução:** Os cargos distinguem a ordem.
- Cinco pessoas disputam três cargos distintos, sem acumular cargos. Quantos resultados? **Resolução:** 5×4×3=60.
- Quantas sequências de três posições usam cinco símbolos com repetição permitida? **Resolução:** 5³=125.
- Quantos grupos de três pessoas entre cinco, sem cargos e sem repetição? **Resolução:** 60/3!=60/6=10.
- Cinco tipos, três escolhas, repetição permitida e ordem ignorada. Quantas possibilidades? **Resolução:** C(5+3−1,3)=C(7,3)=35.
- De quantas maneiras cinco pessoas distintas podem ocupar uma fila de cinco posições? **Resolução:** 5!=120.
- Quantas escolhas de zero posições existem no modelo, mesmo com zero opções disponíveis? **Resolução:** Há um único resultado vazio.
- Três cargos precisam de pessoas distintas, mas só duas estão disponíveis. Quantos resultados? **Resolução:** Não é possível preencher três cargos sem repetir uma das duas pessoas.
- Com A e B em três escolhas, permitindo repetir e ignorando a ordem, quantos grupos existem? **Resolução:** AAA, AAB, ABB e BBB: quatro grupos.
- Com símbolos 0–4 em três posições e repetição permitida, quantas sequências têm primeiro símbolo não nulo? **Resolução:** 4×5×5=100.
- Há três camisetas e duas calças. Se só uma das seis combinações é proibida, quantos conjuntos permitidos restam? **Resolução:** 3×2−1=5.

## Código e referências

Na raiz: `python3 -m unittest discover -s labs/contagem-modelos -t .` e `python3 -m labs.contagem-modelos.counting`. Somente biblioteca padrão. n/k int não negativos sem bool; ordered/repetition devem ser bool. Convenção k=0 dá um resultado vazio; n=0 com k>0 ou k>n sem repetição dá zero. O núcleo usa contagens inteiras exatas; o oráculo gera sequências e agrupa chaves ordenadas, em 120 configurações. Bijeção de multiconjuntos verificada separadamente e multiplicidades comparadas. Não gera todas as combinações para entradas arbitrariamente grandes na interface; o teste é pequeno e determinístico.

Referências: Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.2, pp.8–9 (PDF9, página dupla), consulta textual parcial do acervo autorizado em 22/10/2026, sem cópia do arquivo para o site; [OpenStax Algebra and Trigonometry 2e §13.5](https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-5-counting-principles), consulta HTML parcial na mesma data. Correspondência de multiconjuntos, exemplos, figura e exercícios próprios. Noções não foi consultado como apoio desta ampliação.

Aula escolar existente ampliada de três para 12 seções e de dois para 12 exercícios, mantendo IDs antigos e esclarecendo pergunta sem contexto. Rascunho assistido por IA para revisão pessoal, sem equivalência com curso completo. Próxima revisão: justificar por que k! divide as escolhas de pessoas distintas, mas não as sequências repetidas; conectar a diferença de multiplicidades aos pesos em probabilidade. Restrições complexas, inclusão-exclusão e permutações circulares permanecem pendentes.

Verificação: cinco testes do laboratório aprovados, incluindo 120 configurações contra enumeração, grupos com multiplicidades diferentes, correspondência de multiconjuntos e contratos/casos vazios. Treze testes de catálogo e 567 estruturas MathML aprovados. No navegador a 390 px, documento com 375 px, quadro inspecionado; questão 6 rejeitou 125/6 e aceitou 35. Console sem erros observados. Prévia contagem-modelos-mobile.jpg. Catálogo 507 aulas/3281 exercícios, 255 aulas com até três seções; cobertura recalculada. Sem repetição da suíte global ou revisão pessoal de domínio. Saldo semanal confirmado após bloco: 90%; parada em 65%. Próxima revisão pessoal: justificar as multiplicidades antes de dividir. Próximo recorte escolar: probabilidade, preservando a distinção entre grupos e resultados equiprováveis; depois redistribuir o avanço pelas disciplinas básicas/complementares.
