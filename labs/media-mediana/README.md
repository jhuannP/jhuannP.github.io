# Média, mediana e extremos — notas de aula

## Antes do resumo, identifique o que foi observado

Considere cinco tempos hipotéticos em minutos:1,2,3,4,10. Cada número é uma observação da mesma variável e o tamanho do conjunto é n=5. Registre unidade, método de coleta e valores faltantes antes de interpretar um resumo. Não faz sentido calcular a média aritmética de categorias como nomes de cores atribuindo-lhes números arbitrários. Nossos dados são exemplos didáticos; não descrevem alunos reais ou resultados da pesquisa.

## Média reparte a soma igualmente

A média aritmética soma as observações e divide pela quantidade. Nos cinco tempos, a soma é20min e a média é20/5=4min. Isso preserva o total: cinco parcelas iguais a4 também somam20. A média não precisa ser um valor observado: nos dados2 e8, ela é5. Se m é a média, Σ(xᵢ−m)=Σxᵢ−nm=0; desvios com sinal se equilibram.

média=Σxᵢ/n

## Mediana depende da ordem e da convenção para quantidade par

Ordene os dados crescentemente antes de localizar o centro. Para n ímpar, a mediana é a observação da posição(n+1)/2, contando posições desde1. Para n par, adotamos a convenção usual: média dos valores nas posições n/2 e n/2+1. Nos dados2 e8, a mediana é5, embora5 não seja uma observação. A média dos dois centrais é uma convenção numérica; não é a média de todos os dados em geral.

## O exemplo original tem média4 e mediana3

Os dados1,2,3,4,10 já estão ordenados. Como n=5, a terceira observação é3min: essa é a mediana. A média usa a soma20 e vale4min. As duas respostas são corretas e resumem aspectos diferentes do conjunto. Se os valores viessem na ordem10,1,4,2,3, a mediana continuaria3 após ordenar; pegar apenas a terceira posição recebida daria4 e estaria errado.

## Uma troca isolada altera a média por Δ dividido por n

Troque10 por100, conservando as outras quatro observações. A soma aumenta90 e a média aumenta90/5=18: passa de4 para22min. A mediana permanece3 neste caso. Em geral, com o mesmo número n de observações e apenas uma mudança de tamanho Δ, a nova média é a antiga mais Δ/n. Essa identidade explica a sensibilidade da média à magnitude dos valores.

nova média−média antiga=Δ/n

## Menor sensibilidade a um extremo não significa imutabilidade

Se trocarmos a observação3 por12 no conjunto original, a ordem se torna1,2,4,10,12 e a mediana passa a4. Alterações que atravessam a região central podem mudar a mediana. O contraste com a troca10→100 mostra uma característica útil, não uma regra de que valores discrepantes jamais a afetam. Um valor muito alto também não deve ser apagado automaticamente: pode ser erro de registro ou uma ocorrência importante, e isso exige conferir a fonte.

## Mesmo centro pode esconder dispersões diferentes

Os conjuntos4,4,4,4 e1,3,5,7 têm média e mediana iguais a4. Mas a amplitude, máximo menos mínimo, é0 no primeiro e6 no segundo. Um centro sozinho não descreve a forma da distribuição, valores repetidos ou extensão da amostra. A amplitude também depende dos extremos e não substitui uma medida completa de dispersão. Variância, desvio padrão e quartis serão desenvolvidos em outros recortes.

amplitude=máximo−mínimo

## Frequências contam observações, não apenas linhas da tabela

Na tabela valor2 com frequência3, valor5 com frequência1 e valor8 com frequência2, há seis observações:2,2,2,5,8,8. A soma é3×2+1×5+2×8=27 e a média é27/6=4,5. As posições centrais3 e4 têm valores2 e5; a mediana é3,5. Fazer a média simples dos três valores distintos daria5, esquecendo as frequências. A tabela aqui contém valores exatos, não intervalos de classe; um histograma agrupado pode perder a informação necessária para recuperar a mediana exata.

média=Σ fⱼvⱼ/Σ fⱼ

## Combinar médias de grupos exige usar seus tamanhos

O grupoA contém2 e4, com tamanho2 e média3. O grupoB contém seis valores10, com média10. Se os grupos são disjuntos e medem a mesma variável na mesma unidade, a soma total é2×3+6×10=66, em oito observações. A média conjunta é66/8=8,25. A média simples das duas médias,6,5, dá pesos iguais a grupos de tamanhos diferentes. Cada tamanho deve acompanhar o resumo fornecido.

média conjunta=(n₁m₁+n₂m₂)/(n₁+n₂)

## A regra das médias de grupos não vale para medianas

Considere grupos numéricosA=(0,0,100) e B=(1,1,1). Suas medianas são0 e1. A média dessas medianas, mesmo ponderada pelos tamanhos iguais, é1/2. Juntando as seis observações e ordenando, obtemos0,0,1,1,1,100; a mediana conjunta é1. Para recuperar medianas a partir de grupos precisamos de informação suficiente sobre as posições da distribuição, não apenas das medianas e tamanhos.

## Por que a média minimiza desvios ao quadrado?

Se m é a média, escreva xᵢ−c=(xᵢ−m)+(m−c), eleve ao quadrado e some. O termo cruzado é2(m−c)Σ(xᵢ−m)=0. Resta Σ(xᵢ−c)²=Σ(xᵢ−m)²+n(c−m)². A última parcela é não negativa e só zera em c=m: a média é o único centro que minimiza essa soma. Para1,2,3,4,10, a soma dos quadrados é50 em c=4 e55 em c=3. Esse critério dá peso quadrático a desvios grandes; sua unidade é o quadrado da unidade dos dados.

Σ(xᵢ−c)²=Σ(xᵢ−m)²+n(c−m)²

## A mediana minimiza outra soma de desvios

Emparelhe o menor com o maior valor ordenado, o segundo menor com o segundo maior, e assim por diante. Para um par a≤b, |a−c|+|b−c|≥b−a, com igualdade quando c está entre a e b. Se n é ímpar, sobra o valor central: escolher c igual a ele minimiza todos os pares e o termo restante. Se n é par, qualquer c entre os dois centrais minimiza a soma absoluta; a convenção de sua média escolhe um desses centros. Para2 e8, todo c entre2 e8 dá soma absoluta6. Isso explica por que minimizar desvios absolutos e quadráticos pode produzir respostas diferentes.

## Unidades e dados ausentes precisam de tratamento explícito

Se cada valor muda por y=ax+b com a>0, média e mediana mudam pela mesma transformação; a amplitude é multiplicada por a. Converter minutos em segundos multiplica esses resumos por60. Uma observação ausente não é automaticamente zero. Excluir ausências ou substituí-las muda o conjunto e pode introduzir viés; registre o que foi feito. O código recusa None, não faz limpeza automática e exige frequências inteiras não negativas com total positivo.

## O laboratório descreve os dados recebidos

O código usa inteiros e Fraction para obter média, mediana, total e amplitude. Pode trabalhar com frequências sem expandir cada observação; uma contagem grande não exige criar uma lista igualmente grande. combine_means pressupõe grupos não vazios, disjuntos e da mesma variável/unidade. Os testes conferem cálculos e propriedades; não provam amostragem representativa, causalidade ou incerteza de uma estimativa populacional. Notas assistidas por IA, com revisão pessoal e uso com aluno pendentes.

## Exercícios originais e resoluções

Qual a mediana dos dados1,2,3,4,10? **Resolução:** Depois de ordenar, o terceiro dos cinco valores é3.

Média e mediana são sempre iguais? **Resolução:** O exemplo fornece 4 e 3.

Qual a média de1,2,3,4,100? **Resolução:** A soma é110;110/5=22.

Ao trocar10 por100 em um conjunto de cinco observações, quanto a média aumenta? **Resolução:** A soma aumenta90, então a média aumenta90/5=18.

Pela convenção desta aula, qual a mediana de2 e8? **Resolução:** Média dos dois centrais:(2+8)/2=5.

Valores2,5,8 têm frequências3,1,2. Quantas observações há? **Resolução:** 3+1+2=6, não três.

Qual a média da tabela anterior? **Resolução:** (3×2+1×5+2×8)/6=27/6=4,5.

Qual a mediana dessa tabela de frequências? **Resolução:** Dados2,2,2,5,8,8; centrais2 e5 dão3,5.

GrupoA:n=2,média3. GrupoB:n=6,média10. Qual a média conjunta de grupos disjuntos na mesma unidade? **Resolução:** (2×3+6×10)/(2+6)=66/8=8,25.

Qual a amplitude dos dados1,3,5,7? **Resolução:** 7−1=6. O centro4 é igual ao de4,4,4,4, mas a amplitude difere.

Para1,2,3,4,10, qual centro c minimiza a soma de desvios ao quadrado? **Resolução:** A identidade com a média deixa n(c−m)², mínima apenas em c=m=4.

A mediana é sempre imutável quando uma observação muda? **Resolução:** No original, trocar3 por12 dá1,2,4,10,12 e mediana4. A troca10→100 preservava a mediana apenas naquele caso.

## Fonte e laboratório

Magalhães e Lima — Noções de Probabilidade e Estatística,7ª edição, exemplar autorizado.

§4.2, definição4.1 e recortes de pp.106–108/PDF121–123, consulta textual parcial em26/10/2026: média, mediana, frequências e transformação de escala. Sem leitura integral do capítulo. Dados, provas de minimização, figura, código e exercícios originais; exposição adaptada ao reforço escolar.

`summarize(values)` exige lista/tupla não vazia de int/Fraction, sem bool/float/None. `frequency_summary(frequencies)` recebe mapa valor→contagem inteira não negativa com total positivo; frequências zero são ignoradas na ordem, extremos e total. A mediana usa frequências acumuladas e não expande os dados. `combine_means(groups)` exige grupos de contagem positiva e média racional; unidades/ausência de sobreposição cabem ao chamador. `losses(values,center)` compara somas absolutas e quadráticas, não uma incerteza estatística.

Executar: `python3 -m unittest discover -s labs/media-mediana -t .`. Testes com3905 conjuntos curtos, frequências, mudança de escala, grupos e funções de perda conferem implementação; provas gerais estão no texto. Sem limpeza automática, inferência populacional ou distribuição de páginas dos livros. Rascunho assistido por IA para revisão de Jhuann.

Se as médias dos grupos já foram arredondadas, a combinação também carrega essa aproximação; o código não recupera os dados originais.
