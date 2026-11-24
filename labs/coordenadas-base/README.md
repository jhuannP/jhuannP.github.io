# Mudança de base — notas de aula

Rascunho original para revisão de Jhuann, 22/10/2026.

## Colunas da base formam uma matriz

Escolha uma base ordenada (b₁,b₂) do plano e forme B colocando esses vetores nas colunas, escritos na base cartesiana. Todo vetor v se escreve de uma única forma v=z₁b₁+z₂b₂. A coluna z=[v]B contém esses coeficientes e satisfaz v=Bz. B precisa ser invertível para que a representação exista e seja única para todo vetor do plano. Os números e vetores do exemplo são adimensionais.

[v]_B=B⁻¹v

## Exemplo de uma base oblíqua

Com b₁=(1,0), b₂=(1,1) e v=(3,2), escreva z₁(1,0)+z₂(1,1)=(z₁+z₂,z₂). A segunda equação dá z₂=2; a primeira dá z₁=1. Assim as coordenadas na base oblíqua são (1,2), embora as coordenadas cartesianas sejam (3,2). Reconstruir B(1,2) devolve (3,2). O par de coeficientes precisa sempre vir acompanhado da indicação da base.

B=[[1,1],[0,1]]

## Operadores também mudam de representação

Se A é a matriz do operador na base cartesiana, sua matriz na base B é B⁻¹AB. A mudança é de coordenadas; não foi aplicada uma nova transformação física ao vetor.

A_B=B⁻¹AB

## A ordem dos vetores também faz parte da base

Se trocarmos b₁ e b₂, a matriz passa a ter as colunas trocadas. O mesmo v do exemplo terá coeficientes (2,1) nessa nova base ordenada. Manter os números (1,2) depois da troca reconstruiria outro vetor. O vetor geométrico não mudou quando mudamos sua descrição; a ordem da lista é uma parte indispensável da convenção.



## De uma base B para outra base C

Se v=Bz e também v=Cw, igualar as duas expressões dá Cw=Bz. Multiplicando por C⁻¹, obtemos w=C⁻¹Bz. Portanto a matriz de transição de coordenadas B para coordenadas C é P(C←B)=C⁻¹B. A seta registra origem e destino para evitar inverter a ordem. As colunas dessa matriz são as coordenadas dos vetores de B expressos em C.

P(C←B)=C⁻¹B

## Exemplo com uma segunda base

Escolha c₁=(2,0) e c₂=(0,1), formando C diagonal com entradas 2 e 1. Para v=(3,2), as coordenadas em C são (3/2,2), pois (3/2)c₁+2c₂=(3,2). A matriz P(C←B) tem primeira linha (1/2,1/2) e segunda linha (0,1). Aplicada a z=(1,2), ela produz (3/2,2). Reconstruir por C ou por B dá o mesmo vetor.

C(3/2,2)=B(1,2)=(3,2)

## Compor transições exige acompanhar a direção

Se houver uma terceira base D, primeiro converta B para C e depois C para D. O produto é (D⁻¹C)(C⁻¹B)=D⁻¹B, pois os fatores centrais se cancelam. A inversa da transição B para C é a transição C para B, não a transposta em geral. Esse cancelamento fornece uma verificação algébrica antes de calcular números.

P(D←C)P(C←B)=P(D←B)

## Por que a transposta não basta na base oblíqua

No exemplo, B⁻¹ tem linhas (1,−1) e (0,1). Já Bᵀ tem linhas (1,0) e (1,1). Aplicar Bᵀ a v=(3,2) produz (3,5), que não são as coordenadas corretas (1,2). Produtos escalares com vetores da base dão coordenadas diretamente quando a base é ortonormal. Uma base apenas invertível, ou apenas com vetores normalizados individualmente, não permite essa substituição.

B⁻¹≠Bᵀ em geral

## As linhas da inversa extraem os coeficientes

As linhas de B⁻¹ definem duas funções lineares: a primeira retorna x−y e a segunda retorna y. A primeira vale 1 em b₁ e 0 em b₂; a segunda vale 0 em b₁ e 1 em b₂. Elas formam a base dual, no sentido de extrair cada coeficiente da combinação. Isso explica por que tomar produto com b₂=(1,1) não extrai sozinho o segundo coeficiente numa base oblíqua.

z₁=x−y; z₂=y

## O comprimento usa a métrica da representação

Para z=[v]B, temos v=Bz. O comprimento euclidiano ao quadrado é vᵀv=zᵀBᵀBz. Defina G=BᵀB, a matriz de Gram da base. Aqui G tem linhas (1,1) e (1,2). Para z=(1,2), zᵀGz=1+4+8=13, igual a 3²+2². Somar apenas 1²+2² daria 5 e corresponderia a usar indevidamente a matriz identidade nessas coordenadas.

‖v‖²=zᵀGz; G=BᵀB

## Derivar a representação do mesmo operador

Se A representa uma transformação linear nas coordenadas cartesianas, T(v)=Av. Como v=Bz, a imagem cartesiana é ABz. Para escrever a imagem em coordenadas B, aplicamos B⁻¹ e obtemos znovo=B⁻¹ABz. Assim A_B=B⁻¹AB. A ordem expressa o caminho: sair das coordenadas B, aplicar o operador e voltar às coordenadas B. Essa semelhança exige usar a mesma base na entrada e na saída; bases diferentes dariam outra fórmula.

A_B=B⁻¹AB

## Exemplo de operador e reconstrução

Considere A diagonal com entradas 2 e 3: T(x,y)=(2x,3y). A matriz na base oblíqua B tem linhas (2,−1) e (0,3). Aplicada às coordenadas z=(1,2), produz (0,6). Reconstruindo, B(0,6)=(6,6), que coincide com A(3,2). O termo fora da diagonal −1 não revela uma nova ação física: surge da descrição na base escolhida.

A_B(1,2)=(0,6); B(0,6)=(6,6)

## A escolha da base e o limite do laboratório

O laboratório usa matrizes 2×2 e frações racionais para conferir reconstrução, transição, representação e Gram. Rejeita bases singulares. A fórmula com inversa é uma descrição matemática; em problemas numéricos grandes costuma-se resolver sistemas, sem formar a inversa explicitamente. Bases quase dependentes podem amplificar perturbações, mesmo quando a inversa existe. O código exato não analisa estabilidade em ponto flutuante nem bases de dimensão geral. Revisão pessoal, espaços funcionais e uso em aplicações ainda precisam de desenvolvimento.



## Exercícios e resoluções

- Para v=(3,2), b₁=(1,0), b₂=(1,1), qual é a primeira coordenada em B? **Resolução:** 3−2=1.
- Mudar coordenadas significa necessariamente mover o vetor físico? **Resolução:** O vetor permanece; muda a representação.
- No mesmo exemplo v=(3,2), qual é a segunda coordenada na base B? **Resolução:** A segunda componente cartesiana é z₂=2.
- Na base C com c₁=(2,0), c₂=(0,1), qual é a primeira coordenada de v=(3,2)? **Resolução:** 2w₁=3, portanto w₁=3/2.
- Qual é a entrada da primeira linha e segunda coluna de P(C←B) no exemplo? **Resolução:** C⁻¹B tem primeira linha (1/2,1/2).
- Qual é a entrada G₂₂ de G=BᵀB para b₂=(1,1)? **Resolução:** G₂₂=b₂·b₂=1²+1²=2.
- Qual é ‖v‖² para o vetor cartesiano v=(3,2)? **Resolução:** 3²+2²=13, também zᵀGz nas coordenadas B.
- Quanto dá a soma ingênua dos quadrados das coordenadas z=(1,2), que não é ‖v‖² nessa base? **Resolução:** 1²+2²=5; a métrica da base oblíqua não é a identidade.
- Para A diagonal (2,3), qual é a entrada da primeira linha e segunda coluna de A_B=B⁻¹AB no exemplo? **Resolução:** A_B tem linhas (2,−1) e (0,3).
- Qual é a primeira coordenada da imagem A_B(1,2) no exemplo? **Resolução:** 2×1−1×2=0; a segunda é 6.
- Para toda base invertível, podemos trocar B⁻¹ por Bᵀ? **Resolução:** A igualdade vale para matrizes ortogonais, não para toda base.
- Duas colunas proporcionais representam uma base do plano? **Resolução:** São dependentes; falta representar o plano de forma única.

## Fontes e reprodução

Apostol, Cálculo II, exemplar português do acervo, §2.10 pp.51–54/PDF69–72, consulta textual parcial em 22/10/2026 para componentes, ordem da base e representação matricial. Fonte complementar, sem alegar bibliografia oficial de CCM0213. Paginação conferida no trecho, sem inferir deslocamento único de páginas para todo o PDF. MIT OCW18.06SC, resumo da aula31, seção Change of basis, p.3/PDF3: https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/7ce6815ffe9ec37129e581485494acde_MIT18_06SCF11_Ses3.7sum.pdf . Consulta parcial por extração, sem assistir aula ou desenvolver compressão de imagens. Derivações da transição/Gram, exemplos, diagrama e exercícios próprios. Programa e histórico não reconsultados neste bloco.

Na raiz do site: python3 -m labs.coordenadas-base.experiment; python3 -m unittest discover -s labs/coordenadas-base -t . . Só biblioteca padrão; listas/tuplas 2×2 e vetores de comprimento2, int/Fraction. A matriz do operador pode ser singular; apenas as bases devem ser invertíveis. A inversa explícita 2×2 serve à conferência racional, não recomenda esse procedimento como solver numérico geral.

Próxima revisão pessoal: reconstruir v em B e C, explicar por que Bᵀv falha e conferir a norma com G. Condicionamento quantitativo, dimensões gerais e espaços de funções permanecem pendentes.

Conferência no navegador: exercício da segunda base aceitou 3/2; diagrama carregado e inspecionado a 390 px, sem transbordamento horizontal observado. Prévia coordenadas-base-mobile.jpg. Limitação do mapa reconciliada para 18 aulas/121 exercícios e oito introduções curtas; Apostol continua explicitamente complementar, sem exemplar oficial confirmado. Catálogo global: 499 aulas/2946 exercícios em rascunho. Saldo semanal 94%; parada operacional 65%.
