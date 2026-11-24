# Autovalores e autoespaços em duas dimensões

Rascunho original · 27/10/2026 · revisão pessoal pendente.

## Uma reta especial, não necessariamente o mesmo sentido

Para uma matriz quadrada A, um vetor v≠0 é autovetor se Av=λv para algum escalar λ, chamado autovalor. O vetor e sua imagem ficam na mesma reta pela origem; λ negativo inverte o sentido, e λ=0 leva o vetor a zero. Assim o título “direções que não giram” se refere à reta preservada, não a uma seta que sempre mantém sentido ou comprimento. O corpo de escalares, real ou complexo, faz parte da pergunta.

Av=λv, v≠0

## Por que o vetor zero é excluído

A0=λ0 vale para qualquer λ. Se zero fosse autovetor, a igualdade não identificaria uma escala associada à transformação de uma direção não nula. Excluímos v=0, mas não excluímos λ=0: qualquer vetor não nulo do núcleo de A é autovetor de autovalor zero. Uma matriz pode ser singular e ainda ter autovetores perfeitamente válidos.

## Exemplo simétrico com duas direções

A=[[2,1],[1,2]] envia (1,1) para (3,3), portanto esse vetor tem autovalor 3. Também envia (1,−1) para (1,−1), com autovalor 1. Todo múltiplo não nulo de cada um continua sendo autovetor do mesmo autovalor. Não existem apenas “dois autovetores”: existem duas retas próprias e infinitos vetores em cada reta.

## Verificar um candidato exige todas as componentes

Para testar um v fornecido, calcule Av e compare com um único λ multiplicando todo v. Em v=(1,0), a imagem pela matriz do exemplo é (2,1), que não é múltiplo de (1,0): esse candidato não é autovetor. Dividir componente a componente sem conferir os zeros falha. Podemos obter λ a partir de uma componente não nula e depois verificar a igualdade completa; se v=0, a função do laboratório rejeita a pergunta.

## O autoespaço é um núcleo

Reorganizar Av=λv dá (A−λI)v=0. Para um λ fornecido, o conjunto Eλ=ker(A−λI) contém todos os autovetores desse autovalor e também o vetor zero. Ele é um subespaço; seus elementos não nulos são os autovetores. Sua dimensão é chamada multiplicidade geométrica. Se o núcleo só tem zero, λ não é autovalor. A diferença entre conjunto de autovetores e autoespaço evita excluir incorretamente zero de um subespaço.

Eλ=ker(A−λI)

## Do sistema homogêneo ao polinômio característico

Para uma matriz quadrada em dimensão finita, existir solução não nula de (A−λI)v=0 equivale a A−λI ser singular. No caso 2×2, isso equivale a det(A−λI)=0. Se A=[[a,b],[c,d]], expandir o determinante produz λ²−(a+d)λ+ad−bc. Na convenção det(λI−A), a expressão é a mesma em dimensão dois; em dimensão ímpar o sinal global das duas convenções difere, sem alterar as raízes.

p(λ)=λ²−tr(A)λ+det(A)

## Encontrar os números não encerra os vetores

Para a matriz do exemplo, p(λ)=(2−λ)²−1=λ²−4λ+3=(λ−3)(λ−1). Com λ=3, o sistema reduz a −x+y=0: o autoespaço é span{(1,1)}. Com λ=1, reduz a x+y=0: é span{(1,−1)}. As raízes fornecem candidatos a escala; os sistemas homogêneos fornecem as direções. Confira ainda soma 3+1=tr(A)=4 e produto 3×1=det(A)=3.

## Autovalores distintos dão independência, não ortogonalidade geral

No caso de dois autopares com λ₁≠λ₂, suponha c₁v₁+c₂v₂=0. Aplicar A−λ₂I dá c₁(λ₁−λ₂)v₁=0; como v₁≠0, c₁=0 e depois c₂=0. Logo os vetores são independentes. No exemplo simétrico, também são ortogonais, mas isso não vale para qualquer matriz: [[2,1],[0,3]] tem autopares ((1,0),2) e ((1,1),3), cujo produto escalar é 1. A ortogonalidade exige hipóteses adicionais.

## Uma base própria simplifica iterações

As duas direções próprias do exemplo formam uma base de R². Escreva (x,y)=c₊(1,1)+c₋(1,−1), com c₊=(x+y)/2 e c₋=(x−y)/2. Aplicar Aⁿ multiplica as parcelas por 3ⁿ e 1ⁿ. Para (2,0), temos c₊=c₋=1 e Aⁿ(2,0)=(3ⁿ+1,3ⁿ−1); em n=2 resulta (10,8). Essa decomposição antecipa diagonalização, mas só pode ser usada como base se houver vetores próprios independentes suficientes.

## Autovalor repetido pode oferecer apenas uma reta

Considere J=[[2,1],[0,2]]. Seu polinômio é (λ−2)²: a raiz 2 tem multiplicidade algébrica dois. Porém J−2I=[[0,1],[0,0]], cujo núcleo é apenas o eixo x, de dimensão um. Não há base de R² formada por autovetores de J. Compare com 2I: mesmo polinômio, mas o núcleo de 2I−2I é R² inteiro, com dimensão dois. Polinômios iguais não determinam sozinhos a estrutura dos autoespaços.

## O corpo real ou complexo muda a resposta

A rotação R=[[0,−1],[1,0]] tem p(λ)=λ²+1. Não há raiz real e, portanto, não há autovetor real não nulo. Sobre os complexos, as raízes são i e −i; por exemplo, R(1,−i)=(i,1)=i(1,−i). Isso não cria uma reta própria real no desenho do plano: estamos trabalhando em outro espaço de escalares. O laboratório racional desta aula não implementa números complexos nem busca raízes irracionais.

## Um autovalor negativo ou zero também tem interpretação

Na matriz D=diag(−2,0), (1,0) tem autovalor −2 e muda de sentido com módulo dobrado; (0,1) tem autovalor zero e é levado a zero. O segundo vetor continua sendo não nulo e satisfaz a definição. Se repetirmos a transformação, a componente de autovalor −2 alterna e cresce em módulo, enquanto a de autovalor zero desaparece após uma aplicação. Isso descreve a iteração discreta de D, não automaticamente uma EDO contínua.

## Um resíduo pequeno precisa de escala e contexto

Em cálculo numérico, conferir Av≈λv exige tolerâncias e normalização apropriadas. Multiplicar v por um número muito pequeno também reduz um resíduo absoluto, sem melhorar a direção relativa. No caso exato, a igualdade e v≠0 são suficientes; no caso aproximado, erro do autopar e sensibilidade da matriz são outras questões. O laboratório usa Fraction para entradas racionais e autopares fornecidos, sem alegar ser um algoritmo geral para calcular espectros.

## O laboratório separa cálculo, candidato e autoespaço

Uma função verifica se o candidato não nulo é realmente multiplicado por uma única escala. Outra calcula uma base de ker(A−λI) em matrizes 2×2 para λ racional fornecido. Se A−λI é invertível, devolve base vazia; se é zero, devolve a base canônica; se tem posto um, usa um vetor perpendicular a uma linha não nula. A justificativa é o sistema homogêneo, e os testes conferem os vetores devolvidos e o efeito de iterações. Não resolve automaticamente todo problema de autovalores.

## Uma revisão de vinte minutos

Reconstrua o polinômio, os dois autoespaços e a decomposição de (2,0) no exemplo. Depois compare J com 2I e explique as duas multiplicidades, sem usar apenas o número de raízes. Dê um exemplo de autovalor zero e explique por que a rotação precisa de complexos. Diagonalização geral, teorema espectral, algoritmos numéricos e demonstrações em dimensão geral ainda precisam de estudo; revisão pessoal de Jhuann pendente.

## Exercícios e resoluções

1. Qual autovalor corresponde a v=(1,1) para A=[[2,1],[1,2]]?

   Resolução: A multiplica essa direção por 3.

2. O vetor zero é autovetor?

   Resolução: A definição exige vetor não nulo.

3. Qual autovalor corresponde a (1,−1) na matriz A do exemplo?

   Resolução: A(1,−1)=(1,−1).

4. Qual é o traço de A=[[2,1],[1,2]]?

   Resolução: 2+2=4.

5. Qual o determinante de A=[[2,1],[1,2]]?

   Resolução: 2×2−1×1=3.

6. Qual a primeira componente de A²(2,0), para a matriz A do exemplo?

   Resolução: 3²+1=10; a outra componente é 8.

7. Qual a dimensão de ker(J−2I) para J=[[2,1],[0,2]]?

   Resolução: O sistema impõe y=0; há uma direção independente.

8. Qual a dimensão do autoespaço de autovalor 2 para a matriz 2I em R²?

   Resolução: A−2I=0; todo R² está no núcleo.

9. Qual autovalor corresponde a (0,1) na matriz diag(−2,0)?

   Resolução: A(0,1)=0=0(0,1).

10. Para A=[[2,1],[1,2]], o vetor (1,0) é autovetor?

   Resolução: A(1,0)=(2,1), fora da reta do eixo x.

11. Uma raiz de multiplicidade algébrica dois garante duas direções próprias independentes?

   Resolução: J tem raiz dupla e autoespaço de dimensão um.

12. A rotação real de 90 graus tem autovetores reais não nulos?

   Resolução: λ²+1 não tem raiz real; complexos mudam o espaço de escalares.

## Fontes e limites

Programa CCM0213, item4, reaberto em27/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213 . Ativação15/07/2024, compatível com aprovação2024/2, sem comprovar versão ministrada. A trilha Álgebra Linear é organização editorial que cobre parte de Matemática III; os demais itens têm apoios em outras trilhas.

Elon Lages Lima, Álgebra Linear, IMPA2014, exemplar do acervo identificado previamente por folha de rosto/CIP. Referência complementar, não bibliografia oficial de CCM0213. §12, pp.147–151/PDF158–162 consultados textualmente de forma parcial em27/10; p.150/PDF161 renderizada e inspecionada visualmente para matriz, polinômio e distinção de coordenadas. PDF contado a partir de1; offset confirmado nesses recortes. Pp.148–149 incluem independência e base de autovetores com autovalores distintos. Sem leitura integral do capítulo e sem distribuição do exemplar. Matrizes, exercícios, figura e código da aula são próprios, não gabaritos transcritos.

Margalit/Rabinoff, Interactive Linear Algebra, Georgia Tech, §5.1: https://textbooks.math.gatech.edu/ila/eigenvectors.html . Consulta pública parcial em27/10: definições, zero, colinearidade e independência. A extração web perde símbolos em várias fórmulas; a derivação matemática foi conferida no exemplar local legível, não inferida de lacunas da extração. Teoremas, exemplos e métodos não foram atribuídos a uma leitura integral.

Os livros oficiais continuam não identificados pelas buscas nominais já registradas. Não se afirma nova busca completa neste bloco ou equivalência entre Lima e uma edição oficial.

## Laboratório

`analyze.py` aceita somente matrizes2×2, vetores2 e escalares int/Fraction, rejeitando bool/float. `candidate` retorna λ racional se o candidato não nulo for autovetor, None caso contrário, e rejeita zero. `eigenspace` fornece uma base do núcleo para λ fornecido; não procura todas as raízes e não aceita complexos. Matriz2×2 com determinante nulo e uma linha não nula tem linhas dependentes; o vetor perpendicular à linha selecionada anula ambas. Se todas as linhas são zero, o núcleo é todo R². Isso justifica os ramos do cálculo de base.

```sh
python3 -m labs.autopares-exatos.analyze
python3 -m unittest discover -s labs/autopares-exatos -t .
```

Testes conferem pares conhecidos, candidatos com componente nula, bases devolvidas em405 combinações de matriz/autovalor, contraexemplos de multiplicidade, iterações contra decomposição independente e contratos. Casos finitos não substituem as provas e não certificam um algoritmo geral de autovalores.

## Registro pessoal — preencher ao estudar

- Data:
- Como encontrei os autoespaços:
- Como distingui as duas multiplicidades:
- O que mudou ao considerar complexos:
- Dúvida que restou:
