# Dinâmica harmônica de AB₂ em nove coordenadas

22/10/2026. Rascunho original, pendente de revisão pessoal. Continua classificação e seleção vibracional sem substituir esses laboratórios. Não é potencial de água, campo de força validado, cálculo eletrônico, saída ORCA ou evidência experimental.

## Fontes e alcance

Miessler/Fischer/Tarr, *Química Inorgânica*, quinta edição brasileira, Pearson 2014: §4.4 e recortes de classificação previamente consultados em pp.101–103, além dos canais IR/Raman anteriormente registrados. Contexto de contagem/classificação; não se atribuem ao livro a energia, o bloco analítico ou os parâmetros desta aula. Não houve nova leitura integral do capítulo.

[ORCA 6.1 Manual, Vibrational Spectroscopy, §5.18.8](https://www.faccts.de/docs/orca/6.1/manual/contents/spectroscopyproperties/vibrations.html), consulta direta parcial em 22/10/2026: Hessiana de uma energia fixa, mudança de massas e distinção entre modos/frequências e propriedades ópticas. Sem instalação, execução ou cópia de resultados. A aproximação de energia fixa ao mudar massas é declarada neste modelo, não afirmada como descrição de todo efeito isotópico real.

Construção algébrica, formas lineares, energia e testes são próprios. Os arquivos privados dos livros permanecem fora do site. Nenhum espectro, espécie ou dado real foi gerado ou inferido.

## Geometria e energia adimensionais

A=(0,0,0), Bₐ=(1,0,1), Bᵦ=(−1,0,1), dois B equivalentes, plano xz. Tudo é adimensionalizado; mB=1 e mA=1..8. κ é selecionado em quartos de zero a dois. Não há unidades cm⁻¹, u atômica ou constantes de força reais.

Defina b₁=(1,0,1), b₂=(−1,0,1); d₁=uBₐ−uA e d₂=uBᵦ−uA. Formas lineares:

- q₁=b₁·d₁;
- q₂=b₂·d₂;
- q₃=(b₂·d₁+b₁·d₂)/2.

q₁ e q₂ são deformações de ligação escaladas. Como b₁·b₂=0 e os dois comprimentos de referência são √2, q₃ é a derivada de cos(θ) nesta referência. São primeiras ordens, não geometria exata de uma grande deformação.

q=Ju; a matriz 3×9 consta no código. V=(q₁²+q₂²+κq₃²)/2 e H=JᵀKJ, K=diag(1,1,κ). H é simétrica e semidefinida positiva para κ≥0. J anula as três translações e três rotações infinitesimais. Para κ>0, posto H=3; para κ=0, posto H=2. A invariância infinitesimal não autoriza tratar uma rotação finita como deslocamento dentro da aproximação linear.

## Massas, redução e modos

M é diagonal, repetindo cada massa três vezes. Hv=λMv, D=M^(−1/2)HM^(−1/2), λ=ω². Vetores cartesianos têm vᵀMv=1 e ortogonalidade por massa. Fase fixada pelas combinações internas, não por escolher a maior componente a cada massa, para evitar inversões visuais arbitrárias.

O espectro não nulo pode ser obtido de C=K^(1/2)GK^(1/2), G=JM^(−1)Jᵀ, com

G=((a,0,b),(0,a,b),(b,b,c)), a=2+2/mA, b=1/mA, c=1+1/mA.

A combinação antissimétrica das ligações tem classe B₁ e λ=a. O bloco A₁ simétrico/ângulo é ((a,√(2κ)b),(√(2κ)b,κc)), fornecendo λ±=[a+κc ± √((a−κc)²+8κb²)]/2. O cálculo não usa uma frequência atribuída previamente a uma classe. Os dois A₁ podem misturar deformações.

Vetores não nulos são levantados por v=M^(−1)JᵀK^(1/2)e/√λ, onde e é autovetor unitário do bloco reduzido. Para κ=0 o modo nulo exige construção separada, sem dividir por √λ: use g=G^(−1)(0,0,1), v proporcional a M^(−1)Jᵀg, normalizado e com fase compatível com o limite. Ele é ortogonal por massa ao espaço rígido e tem deformação angular não nula. Os seis zeros rígidos continuam existindo; esse sétimo zero é interno. Não é oscilador de frequência positiva nem torna a geometria linear.

Exemplo mA=2, κ=1: λA₁=(9−√17)/4≈1,2192236; λB₁=3; λA₁=(9+√17)/4≈3,2807764. Frequências angulares: 1,1041846; 1,7320508; 1,8112914 em unidades abstratas. Em κ=0 surgem degenerescências particulares da energia escolhida; não são uma degenerescência obrigatória de C₂v.

## Verificação e visual

Quatro testes Python: diagonalização Jacobi independente da matriz D9×9 em 72 pares massa/κ, com resíduos e ortogonalidade; simetria dos vetores e ortogonalidade rígida ligada ao construtor geométrico existente; Hessiana por diferenças finitas racionais da energia em 324 componentes; limite sem rigidez, deslocamento visual e contratos. A diagonalização de referência não recebe os três autovalores analíticos como entrada.

`reference.json`: 144 estados (quatro massas, quatro rigidezes incluindo zero, três modos e três fatores visuais). JavaScript compara autovalores, frequências, classes, norma/resíduo, vetores e posições. Não valida força molecular real ou espectro.

Tese visual: projeção xz com referência cinza e deformação azul, seguida de tabela de λ/ω. O cálculo mantém nove componentes; neste modelo os três vetores internos têm y=0. O maior deslocamento é escalado a 0,25×|fator visual|, sem sentido de amplitude/energia física. Fator não é tempo; zero restaura a referência e sinal negativo inverte a direção representada. Massas e rigidez alteram a dinâmica; modo e fator mudam a inspeção. Sem animação que sugira aquisição ou frequência experimental.

Pendências: revisão pessoal, potenciais/geometrias gerais, unidades físicas, propriedades ópticas e validação. Próximo eixo: abrir coordenação por geometria e isomeria ideais, após consultar fonte pertinente, sem confundir equivalência geométrica e isômero real. Os 15 grupos em lacuna de Química III permanecem.
