# Exponencial por etapas — notas de aula

Rascunho original para revisão de Jhuann, 22/10/2026. Python é opcional; a aula matemática é independente de programação.

## A taxa relativa produz multiplicação

Se a quantidade dobra em cada etapa, a regra é Qₙ₊₁=2Qₙ. De Q₀ passamos a 2Q₀, depois 4Q₀ e então 8Q₀. Após n etapas inteiras, Qₙ=Q₀·2ⁿ. O expoente conta quantas multiplicações foram feitas; no instante inicial, n=0 e 2⁰=1. Nesta aula usamos quantidade inicial não negativa e etapas de mesma duração.

Qₙ=Q₀·2ⁿ

## Crescimento e decaimento usam fatores distintos

Com quantidade inicial positiva, fator r>1 gera crescimento; fator entre 0 e 1 gera redução. Em Qₙ=80·(1/2)ⁿ, cada passo retém metade: 80, 40, 20, 10. O fator é o que permanece, não o que foi removido. r=1 dá quantidade constante, um caso degenerado separado da função exponencial não constante. Q₀=0 permanece zero na regra multiplicativa.

0<a<1: decrescente

## O contexto limita a extrapolação

O modelo exponencial pode valer apenas por um intervalo ou sob recursos e taxas estáveis. Fazer a conta para qualquer n não prova que um fenômeno real manterá essa regra.

hipótese de fator constante

## Da porcentagem ao fator

Crescer 50% significa manter o valor anterior e acrescentar metade dele: Qnovo=Qanterior+0,5Qanterior=1,5Qanterior. Diminuir 25% significa reter 75%: fator 0,75, não 0,25. A taxa percentual por etapa e o fator são objetos relacionados, mas diferentes. Se a taxa relativa é p, em forma decimal, o fator é r=1+p; para redução de fração d, r=1−d.

r=1+p; redução de d: r=1−d

## Exemplo resolvido: três aumentos de metade

Um modelo hipotético começa com 80 mg e multiplica a quantidade por 1,5 em cada etapa. A primeira etapa dá 80×1,5=120 mg. A segunda usa 120 como base: 120×1,5=180 mg. A terceira usa 180: 180×1,5=270 mg. Juntando as multiplicações, Q₃=80·(3/2)³=80·27/8=270 mg. Não há uma substância ou experimento real identificado; são dados sintéticos para estudar a regra.

Q₃=80·(3/2)³=270 mg

## Somar quarenta produz outra sequência

Na primeira etapa, aumentar 80 mg em 50% acrescenta 40 mg. Mas repetir sempre +40 mg dá 80,120,160,200. Repetir ×1,5 dá 80,120,180,270. As duas regras coincidem no início e após uma etapa; isso não as torna equivalentes. Compare diferenças consecutivas: no modelo afim elas são 40 mg; no multiplicativo são 40,60,90 mg. Compare razões consecutivas: no multiplicativo elas são sempre 3/2.

Regra afim: Qₙ=80+40n. Regra multiplicativa: Qₙ=80·(3/2)ⁿ.

## A variação absoluta também pode ser calculada

Se Qₙ₊₁=rQₙ, subtrair Qₙ dos dois lados dá Qₙ₊₁−Qₙ=(r−1)Qₙ. Com r=1,5, o aumento é sempre metade do valor atual. Por isso ele passa de 40 para 60 e depois 90 mg. A expressão confirma fator constante e aumento variável sem precisar inferir o padrão apenas de um desenho.

Qₙ₊₁−Qₙ=(r−1)Qₙ

## Mudar a duração muda o fator

Se cada etapa representa uma hora, três horas contêm três aplicações da regra. O fator de três horas é r³. Para r=1,5 por hora, esse fator é 27/8=3,375: o aumento acumulado é 237,5%, não 150%. Em geral, agrupar k etapas produz rᵏ. O expoente deve contar intervalos na unidade escolhida; trocar horas por minutos sem converter o fator altera o modelo.

Fator de k etapas = rᵏ

## O que ocorre entre duas etapas?

O laboratório calcula apenas etapas inteiras n≥0. Para desenhar uma evolução contínua, uma escolha usual é Q(t)=Q₀r^(t/Δt), com Δt>0 igual à duração da etapa e r>0. Assim t/Δt é adimensional. Essa extensão faz as razões dependerem apenas do tempo decorrido, mas não é a única curva que atravessa os pontos da tabela. Conhecer valores a cada hora não determina automaticamente o comportamento entre as horas.

Q(t)=Q₀r^(t/Δt)

## Redução repetida não zera em uma etapa finita

Na sequência 80·(1/2)ⁿ, cada valor de n finito dá uma quantidade positiva, embora ela possa ficar muito pequena. O limite zero não significa atingir zero após uma etapa finita. Um visor pode arredondar a quantidade para 0,00; isso descreve a resolução da apresentação. O Python racional do laboratório conserva valores exatos para as frações e etapas aceitas, sem arredondá-los a zero.



## Não misturar aumento e retorno

Depois de crescer 50%, reduzir 50% usa uma base maior. Partindo de 80 mg: 80×1,5=120 mg, depois 120×0,5=60 mg. O produto dos fatores é 3/4, portanto houve redução total de 25%. Para desfazer um aumento por r, precisamos do fator 1/r; após ×1,5, o retorno é ×2/3, uma redução de um terço. Esse caso conecta a aula a porcentagens sucessivas; ele não é uma sequência com o mesmo fator em ambas as etapas.

1,5×0,5=0,75; 1/1,5=2/3

## Base, expoente e domínio

Em 2ⁿ, a base 2 é fixa e o expoente varia. Em n², a base varia e o expoente é fixo: são funções diferentes. A base positiva permite a extensão real usual; uma base negativa não fornece uma função real para todos os expoentes reais, pois (−1)^(1/2) não é real. Para uma exponencial não constante com Q₀>0, exigimos r>0 e r≠1. Neste laboratório, r=1 e Q₀=0 são aceitos e identificados como casos constantes.



## Da tabela a uma hipótese de modelo

Com quantidades positivas em instantes igualmente espaçados, razões consecutivas iguais são compatíveis com uma regra multiplicativa nos pontos observados. Um número finito de pontos não prova a regra para todos os tempos. Medidas podem conter ruído, limites de detecção e mudanças de regime. Ajustar um fator e testar previsões com dados novos é diferente de reconhecer uma sequência construída para obedecer à fórmula. Não extrapole o exemplo sintético para crescimento ilimitado em um sistema real.



## Exercícios e resoluções

- Na regra Qₙ=5·2ⁿ, quanto vale Q₃? **Resolução:** 5×8=40.
- Dobrar em cada passo significa somar sempre 5? **Resolução:** É multiplicar o valor atual por 2.
- Qual fator corresponde a crescer 50% em uma etapa? **Resolução:** 1+0,5=1,5.
- Qual fator corresponde a reduzir 25% em uma etapa? **Resolução:** Retém 100%−25%=75%, fator 0,75.
- No modelo 80 mg multiplicados por 1,5 por etapa, qual é Q₂ em mg? **Resolução:** 80×(3/2)²=80×9/4=180 mg.
- Qual é Q₃ em mg no mesmo modelo? **Resolução:** 80×(3/2)³=270 mg.
- Quanto aumenta, em mg, da etapa 2 para a 3 no mesmo modelo? **Resolução:** 270−180=90 mg, metade de 180.
- Qual fator corresponde a três etapas com fator 1,5 em cada uma? **Resolução:** (3/2)³=27/8=3,375.
- Partindo de 80 mg e retendo metade em cada etapa, quanto sobra após três etapas, em mg? **Resolução:** 80×(1/2)³=10 mg.
- Partindo de 80, aumentar 50% e depois reduzir 50% deixa qual quantidade? **Resolução:** 80×1,5×0,5=60.
- Uma tabela de valores a cada hora determina sozinha a curva entre as horas? **Resolução:** Há várias curvas possíveis entre os pontos; a extensão exponencial acrescenta uma hipótese.
- Na regra exata 80·(1/2)ⁿ, existe etapa inteira finita em que a quantidade é zero? **Resolução:** Uma potência finita de 1/2 é positiva; arredondar a exibição não muda esse fato.

## Fontes e reprodução

OpenStax Algebra and Trigonometry 2e, §6.1, consulta parcial em 22/10/2026: definição, base positiva, crescimento/decrescimento e distinção entre taxa relativa e incremento. https://openstax.org/books/algebra-and-trigonometry-2e/pages/6-1-exponential-functions . Não foram reutilizados exemplos, dados populacionais/financeiros, exercícios ou figuras da fonte. A tabela e as quantidades em mg são sintéticas e originais. Este é um percurso próprio de reforço, sem atribuição a disciplina específica do histórico ou matriz de vestibular.

Na raiz do site: python3 -m labs.exponencial-etapas.experiment; python3 -m unittest discover -s labs/exponencial-etapas -t . . O módulo usa a biblioteca padrão e int/Fraction; não aceita bool, float, fator zero/negativo ou etapas não inteiras. Etapas limitadas a 0..256 para uso didático. Retorna valores e diferenças exatos. O intervalo inicial tem delta=None, pois não há etapa anterior na tabela. Não calcula expoentes reais; a extensão contínua é apenas explicada no texto.

Próxima revisão pessoal: explicar as duas sequências da tabela, recalcular o fator de três etapas e justificar a diferença entre limite zero e etapa finita. Equações/logaritmos e ajuste de modelos a dados continuam por desenvolver.

Navegador: questão de agrupamento aceitou 27/8. Tabela carregada e inspecionada a 390 px; expressão longa foi separada entre prosa e fórmula, com nova conferência visual. Sem transbordamento horizontal da página observado. Prévia exponencial-etapas-mobile.jpg. Catálogo: 498 aulas/2904 exercícios em rascunho. Saldo semanal: 95%; parada operacional: 65%.
