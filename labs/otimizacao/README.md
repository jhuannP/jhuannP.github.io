# Otimização com domínio e candidatos

Material original em rascunho — 13/10/2026. Revisão pessoal pendente.

## Comece pela pergunta e pelas variáveis

Otimizar exige dizer qual quantidade deve ser maior ou menor e quais escolhas são permitidas. Para um retângulo de lados x,y e perímetro P>0, a restrição é 2x+2y=P. A área é xy. Elimine y=P/2−x e registre o domínio antes de derivar. Se x,y forem medidos em metros, P tem unidade metro e a área metro quadrado.



## O domínio depende de admitir figuras degeneradas

Retângulos com lados estritamente positivos dão 0<x<P/2. Incluir x=0 ou y=0 cria uma extensão de domínio para [0;P/2] com figuras degeneradas e área zero. O máximo encontrado no interior vale nos dois problemas. O mínimo zero só é atingido na extensão fechada; no aberto, há ínfimo zero, mas nenhum mínimo.



## Local e global respondem a perguntas diferentes

Um máximo local domina escolhas suficientemente próximas do ponto; um máximo global domina todas as escolhas admissíveis. O mínimo é análogo. Pontos diferentes podem ser máximos locais com valores diferentes. A afirmação global exige conferir o domínio inteiro, seja por um teorema e comparação de candidatos, seja por uma desigualdade válida em todo ele.



## O intervalo fechado fornece existência sob continuidade

O Teorema do Valor Extremo garante que uma função contínua num intervalo fechado e limitado atinge máximo e mínimo. Ele não localiza os pontos. Em um intervalo aberto, ilimitado ou numa função descontínua, essa garantia não se aplica; isso não prova que extremos sejam impossíveis, apenas que é necessário outro argumento.



## Derivada zero é uma condição necessária limitada

Se f tem extremo local num ponto interior e é diferenciável ali, então f′=0. Para um máximo, os quocientes com h>0 são não positivos e com h<0 são não negativos; se o limite bilateral existe, ele só pode ser zero. O argumento para mínimo inverte os sinais. Fronteiras e pontos não diferenciáveis não estão cobertos por essa conclusão.



## Faça uma lista completa de candidatos

No problema fechado, compare as extremidades, pontos interiores onde f′=0 e pontos interiores onde f′ não existe. Para |x| em [−1;1], o mínimo é zero num canto; para f(x)=x em [0;1], o máximo ocorre na fronteira, sem derivada zero. Quando existem infinitos pontos críticos ou estrutura irregular, uma lista finita pode não resolver e é necessário outro método.



## Uma derivada zero pode não indicar extremo

Em x³, a derivada é zero em zero, mas há valores negativos à esquerda e positivos à direita: nenhum extremo local. Já x⁴ tem mínimo em zero apesar de f″(0)=0. O teste da segunda derivada zero é inconclusivo. Uma mudança de sinal de f′ de positiva para negativa indica máximo; negativa para positiva indica mínimo, sob as hipóteses de derivabilidade nos lados.



## Resolva o retângulo com cálculo e comparação

A(x)=Px/2−x² tem A′=P/2−2x, logo x=P/4 é candidato interior e y=P/4. A′ é positiva antes e negativa depois; A″=−2 confirma máximo local estrito. Na extensão fechada, as áreas das fronteiras são zero e a do candidato é P²/16, o máximo global. Para P=20 m, os lados são 5 m e a área 25 m².

A′(x)=P/2−2x; x*=P/4; Amax=P²/16

## Completar o quadrado certifica o resultado global

A identidade A(x)=P²/16−(x−P/4)² vale para todo x admissível. O quadrado subtraído é não negativo, então A≤P²/16 com igualdade somente em x=P/4. Ela prova o máximo sem depender de uma grade ou apenas do teste local. Também mede a perda exata de área ao se afastar da melhor escolha.

Amax−A(x)=(x−P/4)²

## Uma restrição adicional pode levar o melhor ponto à fronteira

Se P=20 e só permitimos 0≤x≤3, o candidato x=5 não é admissível. Como A′=10−2x>0 em [0;3], a área cresce e o máximo é A(3)=21, na fronteira. O outro lado é 7. Nunca use um candidato fora do domínio como resposta a um problema restrito.



## Uma busca computacional precisa de uma justificativa

Amostras de uma grade podem aproximar o melhor valor, mas podem perder um pico entre seus pontos. O laboratório compara candidatos exatos no modelo quadrático e fornece a identidade do quadrado como certificado. Os testes conferem contas racionais; a prova global está na identidade e nas hipóteses declaradas. Finalize uma solução com valores, unidades e interpretação dos limites do modelo.



## Exemplo resolvido

Um retângulo tem perímetro 20 m. Qual é a maior área quando seu lado x deve satisfazer 0≤x≤3 m?

A restrição do perímetro dá y=10−x e A=x(10−x) em m².

O domínio adicional é [0;3], e não [0;10].

A′=10−2x só zera em x=5, fora desse domínio.

Em todo [0;3], A′>0; portanto A cresce e o máximo é na fronteira x=3.

O outro lado é y=7 m e a área é 21 m²; compare com A(0)=0.

O máximo irrestrito de 25 m² continua válido para o problema mais amplo, mas não é uma escolha permitida aqui.

## Exercícios e resoluções

### Sem a restrição adicional x≤3, qual a área máxima com perímetro 20 m?

Quadrado de lado 5.

### Derivada zero sozinha garante máximo global em qualquer problema?

É preciso considerar domínio e outros candidatos.

### Qual o lado do quadrado ótimo quando P=12 m?

P/4=3 m.

### Qual a área máxima para P=12 m?

P²/16=144/16=9 m².

### Para P=20 m e 0≤x≤3 m, qual a área máxima?

A(3)=3×7=21 m².

### Para P=20 m e x=3 m, quanto de área se perde em relação ao máximo irrestrito?

(3−5)²=4 m².

### Um extremo local precisa sempre ter derivada existente e igual a zero?

Um canto como |x| em zero pode ser mínimo, sem derivada.

### No domínio de lados estritamente positivos, a área mínima zero é atingida?

A área é positiva; aproxima zero, mas não atinge. Zero é ínfimo.

### f″(a)=0 permite concluir que não existe extremo em a?

O teste é inconclusivo; x⁴ tem mínimo em zero.

## Preparação manuscrita

Desenhe o retângulo; declare unidades e restrições; diferencie local de global; monte a lista de candidatos; compare o problema irrestrito com x≤3; complete o quadrado para certificar; explique máximo, mínimo e ínfimo no domínio aberto. Peça ao aluno que encontre a falha numa resposta que escolhe um ponto fora do domínio.
