# Horner com rastro — notas de aula

Rascunho original para revisão de Jhuann, 22/10/2026. Não é resultado da IC.

## A lista precisa de uma convenção

Aqui [c0,c1,...,cn] representa c0+c1x+...+cnxⁿ, do termo constante ao maior grau. Outras bibliotecas usam outra ordem. Confirme a convenção antes de inserir dados ou comparar resultados.

coeficientes em potências crescentes

## Aninhar evita formar todas as potências

A forma de Horner começa no maior coeficiente e repete multiplicar por x e somar o seguinte. Para grau n, são n multiplicações e n adições no modelo simples. A transformação algébrica preserva o polinômio, mas a ordem das operações pode alterar arredondamento. A contagem vale ao iniciar no último coeficiente, sem uma multiplicação inicial por zero. Ela conta operações aritméticas escalares, não tempo de processamento independente do tamanho dos números.

c0+x(c1+x(c2+...))

## Avaliar não é encontrar todas as raízes

Uma avaliação serve de bloco para métodos de raiz, interpolação e aproximação. Ela não resolve, por si só, o problema de localizar todas as raízes. Resultados próximos de zero ainda dependem da escala e do condicionamento do polinômio.

avaliação eficiente + análise do problema

## Um invariante explica a recorrência

Depois de processar os coeficientes cₙ até cₖ, o acumulador b representa cₖ+cₖ₊₁x+⋯+cₙxⁿ⁻ᵏ. Inicialmente, em k=n, isso é apenas cₙ. Para incluir cₖ₋₁, multiplique o acumulador por x e some cₖ₋₁. No final k=0, ele coincide com p(x). Essa descrição mostra por que o algoritmo está correto, não só que os números de um exemplo coincidiram.

bₖ=cₖ+x bₖ₊₁

## O exemplo tem um rastro verificável

Para coeficientes [1,−3,2] e x=2, comece com b=2, o coeficiente de x². O primeiro passo dá b=2×2−3=1. O segundo dá b=2×1+1=3. Compare com a expressão direta: 1−3×2+2×2²=1−6+8=3. O zero em uma posição da lista precisa ser mantido para indicar a potência ausente; apagar um zero intermediário muda o polinômio.



## Os mesmos números dão uma divisão com resto

Use z para a variável do polinômio e x para o argumento fixo em que avaliamos. A recorrência fornece p(z)=(z−x)q(z)+p(x). Para o exemplo x=2, q(z)=1+2z e resto 3. Expandir (z−2)(1+2z)+3 recupera 1−3z+2z² em qualquer z. Isso distingue uma identidade de polinômios de uma igualdade apenas no ponto avaliado. O resto não deve ser descartado quando não é zero.

p(z)=(z−x)q(z)+p(x)

## A derivada aparece ao avaliar o quociente

Derive a identidade anterior em relação a z: p′(z)=q(z)+(z−x)q′(z). Em z=x, o segundo termo é zero, logo p′(x)=q(x). Essa é uma forma de obter a derivada com outro Horner. O laboratório oferece também a atualização simultânea a seguir. Uma avaliação eficiente de p e p′ auxilia Newton, mas não garante convergência nem fornece todas as raízes.

p′(x)=q(x)

## Atualizar valor e derivada juntos

Se o polinômio parcial H tem valor b e derivada d no argumento x, o novo parcial é cₖ+zH(z). A regra do produto dá derivada H(z)+zH′(z). Portanto a nova derivada é o valor antigo de b mais x vezes o valor antigo de d. O novo valor de b é cₖ mais x vezes seu valor anterior. É importante usar b antigo: no código sequencial, atualize d antes de sobrescrever b. Inicialize no maior coeficiente com derivada zero, pois ele é constante naquele estágio.

d ← x·d+b, usando b antigo

## Custo, memória e representação

A avaliação apenas de p, iniciada em cₙ, usa n produtos e n somas para uma lista de n+1 coeficientes. A versão simultânea ingênua repete um produto e uma soma também para d em cada estágio, totalizando 2n de cada operação; otimizações dos primeiros passos podem alterar a contagem. Só valor/derivada cabem em memória auxiliar constante, além da entrada. Guardar o rastro e o quociente, como no laboratório, usa memória proporcional ao tamanho da lista. Em Fraction, os inteiros podem crescer: custo de operação aritmética não é custo fixo em bits.



## Coeficientes finais nulos não definem o grau

A lista [1,−3,2,0] representa o mesmo polinômio quadrático. O laboratório a aceita e executa três estágios, correspondentes ao tamanho da lista; isso não torna seu grau igual a três. A lista [0] representa o polinômio zero, cujo grau usual não é definido. Listas constantes têm derivada zero e quociente vazio, interpretado como zero. Lista vazia é rejeitada para não confundir ausência de dados com um polinômio escolhido.



## Forma equivalente não significa mesmo arredondamento

Em aritmética racional exata, as formas expandida, aninhada e fatorada dão o mesmo número. Em ponto flutuante, cada operação pode arredondar e as ordens mudam. Considere p(z)=1−2z+z²=(z−1)² em z=1,0001. O valor exato é 10⁻⁸, embora os termos da forma expandida tenham magnitude próxima de 1, 2 e 1. O cancelamento deixa uma resposta muito menor que as parcelas. Horner reduz o trabalho, mas não promete erro relativo pequeno perto de uma raiz.



## Sensibilidade a coeficientes pode ser quantificada

Se cada coeficiente recebe perturbação com |δcᵢ|≤ε|cᵢ|, então |δp(x)|≤εΣ|cᵢxⁱ|, pela desigualdade triangular. Quando p(x)≠0, dividir por |p(x)| dá um limite relativo ε κc, com κc=Σ|cᵢxⁱ|/|p(x)|. No exemplo (x−1)² em x=10001/10000, κc=400040001. Esse número descreve perturbações relativas dos coeficientes; não é erro na raiz, nem por si só um limite do erro do algoritmo ou da entrada x. O laboratório confere a identidade com frações exatas.

κc=Σ|cᵢxⁱ|/|p(x)|, p(x)≠0

## Rastro racional e aplicação pessoal

O novo laboratório aceita int e Fraction para coeficientes e argumento e retorna valor, derivada, quociente e rastro. Ele serve como referência exata para pequenos casos; não simula arredondamento binário nem substitui uma análise de estabilidade. O código curto da aula também usa frações. Próximo à raiz, compare a resposta a uma referência apropriada e explicite a escala do resíduo. Para apresentar isto no portfólio, execute o exemplo, explique o invariante e registre sua revisão; a página assistida por IA não certifica domínio.



## Exercícios e resoluções

- Qual é p(2) para p=1−3x+2x²? **Resolução:** 1−6+8=3.
- O código de Horner desta aula recebe: **Resolução:** A convenção é explicitamente crescente em potências.
- Para p(z)=1−3z+2z², quanto é p′(2)? **Resolução:** p′(z)=−3+4z; em 2, resulta 5.
- No Horner de [1,−3,2] em x=2, qual valor vem após processar −3, partindo de b=2? **Resolução:** 2×2−3=1.
- Se p(z)=(z−2)(1+2z)+3, quanto é q(2)? **Resolução:** q(2)=1+2×2=5=p′(2).
- Qual é o resto na divisão de 1−3z+2z² por z−2? **Resolução:** O resto é p(2)=3.
- Ao iniciar no último coeficiente de uma lista de grau 4 sem zeros finais, quantas multiplicações a avaliação apenas do valor exige? **Resolução:** Uma por estágio, quatro estágios.
- Qual é o valor inteiro exato de κc para (x−1)² em x=10001/10000? **Resolução:** κc=(1+x)²/(x−1)²=20001²=400040001.
- Qual é a derivada do polinômio representado pela lista [7]? **Resolução:** É um polinômio constante.
- Na atualização simultânea, dnovo deve usar qual valor de b? **Resolução:** A regra do produto usa o polinômio parcial anterior.
- Horner com poucas operações garante erro relativo pequeno em qualquer ponto perto de uma raiz? **Resolução:** Sensibilidade e cancelamento podem amplificar perturbações; contagem de operações não resolve isso.
- A lista [1,−3,2,0] representa necessariamente grau 3? **Resolução:** O coeficiente de z³ é zero; o grau real é 2.

## Fontes e reprodução

Burden/Faires/Burden, exemplar da tradução da décima edição norte-americana (terceira edição brasileira, Cengage 2016), §2.6, pp.103–104/PDF117–118, conferência visual em 22/10/2026 do método, recorrência, divisão e relação de derivada. Nenhum exemplo, algoritmo diagramado ou figura do livro foi copiado. A bibliografia oficial de CCM0218 indica a sétima edição; sem equivalência de páginas presumida. NIST DLMF §1.11(i), consulta parcial: https://dlmf.nist.gov/1.11#i ; NIST DADS, Horner's rule: https://xlinux.nist.gov/dads/HTML/hornersrule.html . Fontes usadas para identidade e organização do algoritmo; análise de sensibilidade derivada explicitamente na aula. Programa oficial e histórico não reconsultados neste bloco.

Na raiz do site: python3 -m labs.horner-rastro.experiment; python3 -m unittest discover -s labs/horner-rastro -t . . Apenas biblioteca padrão. O rastro racional é um apoio separado à aula existente de zeros; não modifica o solver ou seus diagnósticos. Aceita zeros finais e caso constante, com quociente vazio interpretado como polinômio zero. O tamanho da lista determina a contagem de estágios, não necessariamente o grau real. O código curto embarcado não impõe o limite de 256 da versão de laboratório.

Próxima revisão pessoal: explicar o uso de b antigo, reconstruir p=(z−x)q+resto e distinguir κc de erro na raiz. Arredondamento binário, métodos compensados e análise geral de estabilidade permanecem pendentes.

Conferência no navegador: a questão de κc rejeitou 400040000 e aceitou 400040001. Tabela carregada e inspecionada a 390 px, sem transbordamento horizontal observado; prosa e notação da atualização foram esclarecidas e reconferidas. Prévia horner-rastro-mobile.jpg. Catálogo: 498 aulas/2914 exercícios em rascunho. Saldo semanal 95%; parada operacional 65%.
