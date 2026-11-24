# Eliminação de Gauss e pivotamento parcial

Rascunho original —27/10/2026; revisão de Jhuann pendente.

## O problema é resolver Ax=b, preservando os dados

Pré-requisitos: sistemas lineares, produto matriz-vetor, módulo, frações e laços em Python. A é uma matriz quadrada n×n e b um vetor com n entradas. Procuramos x cujas componentes satisfaçam todas as equações. O caso principal supõe solução única; famílias singulares serão apenas diagnosticadas. Guarde A e b originais para conferir a resposta. As operações são aplicadas a cópias, e os índices do código começam em zero. Os exemplos são próprios e não usam dados da pesquisa ou do trabalho.

## Eliminar é combinar equações

Use uma linha pivô para zerar entradas abaixo dela. Subtraia um múltiplo da equação pivô das seguintes, incluindo o lado direito. No final, resolva o sistema triangular por substituição retroativa. Alterar só os coeficientes sem atualizar b muda o problema.

linha_i ← linha_i−fator×linha_pivô

## Por que a operação não troca a solução?

Substituir a equação i por ela menos m vezes outra equação k é reversível: basta somar m vezes a equação k para recuperar a anterior. A troca de duas equações também é reversível. Portanto essas operações preservam o conjunto de soluções quando aplicadas à equação inteira, incluindo b. A eliminação escolhe m=aᵢₖ/aₖₖ para tornar aᵢₖ−maₖₖ=0; esse passo só é permitido com pivô aₖₖ não nulo.

mᵢₖ=aᵢₖ/aₖₖ

## Escolher o pivô reduz alguns problemas de escala

Na coluna k, escolha p entre as linhas k,…,n−1 que maximize |aₚₖ| na matriz já transformada. Troque as linhas k e p em A e b. Sinal negativo não impede uma entrada de ser o maior módulo. Em empate, o código escolhe o menor índice disponível. Em aritmética exata, os multiplicadores abaixo do pivô satisfazem |mᵢₖ|≤1, pois seu numerador não é maior em módulo que o pivô. Isso limita os multiplicadores desta coluna, não todos os valores intermediários ou o erro final.

troca em A e b; seleção por módulo

## Um exemplo com eliminação não trivial

Preservamos o exemplo original de pivô zero no exemplo resolvido ao final. Para abrir as contas, use A=[[1,2],[3,5]] e b=[5,13]. A primeira coluna contém 1 e 3: troque as linhas para obter 3x+5y=13 e x+2y=5. O multiplicador é 1/3. Subtraindo um terço da primeira equação da segunda, o coeficiente de y fica 2−5/3=1/3 e o lado direito fica 5−13/3=2/3. Alterar só a matriz e manter b antigo falharia aqui.

(1/3)y=2/3

## A matriz aumentada deixa a troca de b visível

A barra separa os coeficientes do lado direito; não é uma coluna de incógnitas. Leia cada linha como uma equação. A segunda etapa troca ambas as partes. A terceira usa o mesmo multiplicador nos coeficientes e em b. Esta é uma sequência didática exata; a implementação float poderá arredondar os terços.

## Substituição retroativa usa o que já foi resolvido

Da última equação, y=(2/3)/(1/3)=2. Na anterior, x=(13−5y)/3=1. Em geral, para uma matriz triangular superior U, resolva da última linha até a primeira: xᵢ=[cᵢ−Σⱼ₌ᵢ₊₁ⁿ⁻¹uᵢⱼxⱼ]/uᵢᵢ. Cada xⱼ necessário já foi calculado e cada divisor diagonal precisa ser não nulo. Não é necessário calcular a matriz inversa para resolver um único sistema.

xᵢ=(cᵢ−Σⱼ>ᵢuᵢⱼxⱼ)/uᵢᵢ

## O laço mantém uma estrutura verificável

Antes de eliminar a coluna k, as colunas anteriores já têm zeros abaixo de sua diagonal. As próximas operações combinam apenas linhas ativas, cujas entradas nessas colunas são zero; assim não desfazem a estrutura construída. O sistema permanece equivalente em aritmética exata. Ao terminar, temos Ux=c triangular. O código escreve zero explicitamente na coluna eliminada; isso registra a estrutura do algoritmo e não torna as demais operações de ponto flutuante exatas.

## O custo explica por que reutilizar uma fatoração

Na eliminação densa, cada coluna atualiza aproximadamente um quadrado de tamanho n−k. A soma desses quadrados cresce como n³; a substituição retroativa cresce como n². Dobrar n tende a multiplicar por cerca de oito o custo dominante para n grande, não necessariamente o tempo de qualquer execução pequena. Para vários vetores b com a mesma A, armazenar uma fatoração com permutação evita repetir toda a eliminação. A implementação desta aula resolve um b por vez; fatoração LU reutilizável está em outra aula.

## Um pivô pequeno pode amplificar o arredondamento

No laboratório, tome ε=2⁻⁶⁰, A=[[ε,1],[1,1]] e b=[1,2]. Esses números de entrada são exatamente representáveis em binário. Sem troca, o primeiro multiplicador é 1/ε=2⁶⁰. Na execução float conferida, a solução ingênua fica(0,1), enquanto a rotina com troca retorna(1,1). A solução racional dos mesmos dados é x=1/(1−ε), y=(1−2ε)/(1−ε). Portanto(1,1) é uma boa aproximação, não a solução racional exata. O resultado de arredondamento descrito é do ambiente testado, não um modelo universal de toda aritmética.

ε=2⁻⁶⁰; x_exato=1/(1−ε)

## Conferir depois da solução

Calcule r=b−Ax usando a matriz original, preservada antes das operações. A implementação cria cópias dos dados e rejeita pivô zero. Um diagnóstico de fatoração não deve ser confundido com uma prova de que toda formulação do problema é impossível.

solução calculada → resíduo na entrada original

## Resíduo calculado zero pode esconder arredondamento

Para a aproximação(1,1) no exemplo ε=2⁻⁶⁰, o resíduo racional b−Ax é(−ε,0). A rotina float soma 1+ε como 1 e devolve resíduo(0,0). Isso não é erro de conversão dos dados: a entrada ε já era binária exata. É arredondamento ao avaliar o produto e a soma. Use uma referência de precisão maior ou uma análise de erro quando precisar avaliar diferenças dessa escala. O laboratório converte as saídas float para suas frações exatas antes da conferência racional.

r=b−Ax

## Resíduo pequeno não garante erro pequeno na solução

Use agora δ=1/1000, A=[[1,1],[1,1+δ]] e b=[2,2+δ]. A solução exata é(1,1). Para a candidata x̂=(2,0), o resíduo é(0,δ), de norma máxima 0,001; o erro x̂−x é(1,−1), de norma máxima 1. As equações são próximas de dependentes e permitem grandes mudanças em x com pequenas mudanças em Ax. Essa candidata é escolhida para ilustrar o diagnóstico; não afirmamos que a rotina com pivotamento a produziu.

## Condicionamento pertence ao problema, não só ao algoritmo

A norma máxima de um vetor é o maior módulo; a norma infinita de uma matriz é a maior soma dos módulos numa linha. Para a matriz com δ, a inversa é δ⁻¹[[1+δ,−1],[−1,1]], então κ∞(A)=||A||∞||A⁻¹||∞=(2+δ)²/δ. Com δ=1/1000, resulta 4004,001. Esse número ajuda a interpretar a sensibilidade do sistema. Trocar linhas organiza a eliminação, mas não torna independentes equações quase dependentes. A análise completa de erro direto e reverso fica na aula de normas e condicionamento.

κ∞(A)=(2+δ)²/δ

## Pivô zero não classifica sozinho as soluções

Em aritmética exata, uma matriz quadrada não singular admite eliminação com pivotamento parcial até o fim. Se a coluna ativa não tem pivô não nulo, não se obtém uma solução única por essa rotina. Duas linhas dependentes com lados direitos compatíveis podem dar infinitas soluções; com lados direitos incompatíveis, nenhuma. Por exemplo, as linhas(1,2) e(2,4) com b=(3,6) são compatíveis, mas com b=(3,7) produzem 0=1. O código para nos dois casos e não classifica a família. Em float, pivô calculado zero também precisa ser interpretado considerando arredondamento e escala, sem anunciar automaticamente um diagnóstico exato da entrada.

## O contrato do código faz parte da resposta

A rotina float original copia a entrada, exige matriz quadrada não vazia e dados reais finitos, e rejeita pivô calculado zero. Não aplica tolerância universal de quase singularidade, nem trata matrizes retangulares, esparsas ou múltiplos lados direitos. A referência racional baixável aceita somente int/Fraction e serve a sistemas pequenos, pois as frações podem crescer muito. Os testes comparam a rotina com Cramer em 2×2 e com soluções conhecidas em matrizes 3×3; testes finitos não substituem a justificativa do algoritmo.

## Duas sessões para demonstrar o raciocínio

Na primeira sessão de vinte minutos, reconstrua o exemplo com linhas(1,2) e(3,5), incluindo b, e explique por que o multiplicador é1/3. Na segunda, compare os exemplos de pivô pequeno e de mau condicionamento: eles ilustram problemas distintos. Registre sua explicação e suas dúvidas; as notas são um rascunho, não prova de domínio pessoal. Próximos recortes: LU com permutação e reutilização, diagnóstico de erro e escolha de rotinas numéricas de produção.

## Exercícios e resoluções

Qual índice de linha, a partir de zero, é escolhido como primeiro pivô no exemplo?

**Resolução:** A coluna ativa contém 0 e 1; escolhemos o módulo maior na linha 1.

No exemplo original [[0,2],[1,3]]x=[4,7], qual é o valor de y?

**Resolução:** 2y=4, portanto y=2.

No novo exemplo A=[[1,2],[3,5]], após a troca, qual é o multiplicador para eliminar a entrada1?

**Resolução:** A entrada a eliminar é1 e o pivô é3: m=1/3.

No novo exemplo, qual é a segunda entrada diagonal após eliminar?

**Resolução:** 2−(1/3)5=1/3.

No novo exemplo com b=[5,13], qual é a segunda entrada transformada de b?

**Resolução:** Depois da troca, b=(13,5); a segunda entrada vira5−13/3=2/3.

Qual é x na solução do novo exemplo A=[[1,2],[3,5]], b=[5,13]?

**Resolução:** A segunda equação dá y=2; x=(13−10)/3=1.

Para A=[[1,2],[3,5]], b=[5,13] e candidata x̂=(1,1), qual é ||b−Ax̂||∞?

**Resolução:** Ax̂=(3,8), resíduo=(2,5), norma máxima5.

No exemplo com δ=1/1000 e candidata(2,0), qual é a norma máxima do resíduo?

**Resolução:** O resíduo é(0,δ), logo1/1000.

No mesmo exemplo, com solução exata(1,1), qual é a norma máxima do erro da candidata(2,0)?

**Resolução:** A diferença é(1,−1); maior módulo1.

Com δ=1/1000, quanto vale κ∞=(2+δ)²/δ?

**Resolução:** (2,001)²/0,001=4004,001.

Se o custo dominante é proporcional a n³, dobrar n multiplica esse termo por quanto?

**Resolução:** (2n)³/n³=8. Não é promessa de tempo para um caso pequeno.

O sistema x+2y=3 e2x+4y=7 tem qual situação?

**Resolução:** Subtrair duas vezes a primeira equação da segunda dá0=1, incompatível.

## Fontes e edições

Burden, Faires e Burden, Análise Numérica: tradução da10ª edição norte-americana,3ª edição brasileira, Cengage2016, confirmada visualmente na ficha PDF4. Sumário PDF12 identifica §6.2, p.412. Inspeção visual parcial das pp.412–413/PDF426–427 em27/10/2026: pivô pequeno, multiplicadores e escolha por maior módulo na coluna. O PDF é de imagens; pdftotext não retornou corpo textual e emitiu avisos de compressão. Não houve OCR, leitura integral do capítulo ou distribuição do PDF/imagens privadas. As páginas do PDF usam contagem a partir de1.

Complementos públicos consultados parcialmente em27/10: [FNC, §2.6 Row pivoting](https://fncbook.com/julia/pivoting/), definição e falha sem trocas; [NIST DLMF, §3.2](https://dlmf.nist.gov/3.2), sistema aumentado, eliminação, retroativa e condicionamento. Exemplos, números, exercícios, figura e código da aula são próprios, não reprodução das listas ou figuras dos autores.

## Verificação e limites

`python3 -m unittest discover -s labs/gauss-pivoteamento -t .` e `python3 labs/gauss-pivoteamento/exact.py`. Cinco testes: sistemas2×2 contra Cramer;40 sistemas3×3 gerados por operações invertíveis com solução conhecida; rastro e empate; pequeno pivô/resíduo racional versus float; contratos e singularidade. A enumeração confere a implementação, não prova estabilidade geral.

No exemplo de arredondamento, ε=2⁻⁶⁰ e b=(1,2) são exatamente representáveis. A referência exata é dos mesmos dados binários. A solução float pivoteada(1,1) tem resíduo racional(−ε,0), embora a avaliação float devolva zero. O exemplo de δ=1/1000 usa candidata(2,0) escolhida, não saída alegada do solver. Não se confundem essas duas demonstrações.

A API racional aceita int/Fraction, rejeita float/bool, dimensões inválidas e pivô exato zero; não classifica famílias singulares. A rotina float é copiada do código já existente, preservado. Não houve modificação do algoritmo da aula. Métodos reutilizáveis, esparsos, estimadores robustos de condição e bibliotecas de produção ficam para próximos recortes.

Próxima revisão: reconstruir as operações em A e b e explicar resíduo versus erro. Próxima elaboração da trilha: LU com permutação; alternar com lacunas de outras disciplinas.
