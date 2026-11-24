# Jacobi e Gauss–Seidel: informação antiga, informação nova

Notas de aula originais, em rascunho para revisão de Jhuann. Apoio parcial a sistemas lineares iterativos de ComputaçãoIII. Pré-requisitos: sistemas, norma infinito, resíduo e contração. Os números são sintéticos; não são resultados da IC nem demonstração de experiência profissional.

## Um sistema, duas varreduras

Para A=[[4,1],[1,3]], b=(1,2), x⁽⁰⁾=(0,0), a solução é x*=(1/11,7/11). Isolar cada coordenada fornece x₁=(1−x₂)/4 e x₂=(2−x₁)/3.

| Método | Primeiro vetor | Segundo vetor |
|---|---|---|
| Jacobi, todo o vetor anterior | (1/4,2/3) | (1/12,7/12) |
| Gauss–Seidel, novos valores nas coordenadas anteriores | (1/4,7/12) | (5/48,91/144) |

Não substitua a lista antiga enquanto calcula Jacobi. Em Gauss–Seidel, a ordem da varredura faz parte do método; alterações de ordenação devem ser explícitas.

## Derivar uma prova de convergência

Se x novo=T x antigo+c e x*=Tx*+c, subtrair dá e novo=T e antigo. Para este sistema:

- T_J=[[0,−1/4],[−1/3,0]], c_J=(1/4,2/3).
- T_G=[[0,−1/4],[0,1/12]], c_G=(1/4,7/12).

A norma matricial infinito é a maior soma absoluta de uma linha: limitar cada componente de Tv por Σ|t_ij| max|v_j| prova ||Tv||∞≤||T||∞||v||∞. Aqui ||T_J||∞=1/3 e ||T_G||∞=1/4. Iterar a desigualdade fornece ||e⁽ᵏ⁾||∞≤qᵏ||e⁽⁰⁾||∞→0 para qualquer início. Isso é prova no exemplo, não uma inferência a partir de poucas iterações.

Com Δ_k=||x⁽ᵏ⁾−x⁽ᵏ⁻¹⁾||∞, as diferenças futuras têm normas no máximo qΔ_k,q²Δ_k,…; a soma da cauda limita ||x*−x⁽ᵏ⁾||∞ por qΔ_k/(1−q). Para o primeiro Gauss–Seidel, Δ₁=7/12 e o limite é7/36. O erro real é max(7/44,7/132)=7/44.

O resíduo r=b−Ax é outro vetor. Como x*−x=A⁻¹r e A⁻¹=(1/11)[[3,−1],[−1,4]], sua norma∞ é5/11. O primeiro resíduo de Gauss–Seidel é(−7/12,0), fornecendo outro limite: (5/11)(7/12)=35/132. Não precisamos nem recomendamos formar uma inversa densa somente para parar um programa; este é um exemplo pequeno com inversa analítica.

## Suficiente não é necessário

Dominância diagonal estrita por linhas significa |a_ii|>Σ_(j≠i)|a_ij| para toda linha. Para Jacobi, isso garante ||T_J||∞<1. É também condição suficiente usual para Gauss–Seidel; sua prova geral não é desenvolvida aqui. Nossa matriz satisfaz4>1 e3>1.

No segundo exemplo, A=[[1,2],[1/10,1]], b=(3,11/10), x*=(1,1), a primeira linha não é dominante e ||T_J||∞=2. Porém T_J²=(1/5)I. Os erros dos índices pares tendem a zero como(1/5)^m; os ímpares também tendem a zero, pois são T_J vezes os pares. Assim Jacobi converge. Uma norma de um passo maior que1 apenas impede aquela prova, sem provar divergência.

No terceiro exemplo, A=[[1,2],[2,1]], b=(1,1), x⁽⁰⁾=(0,0), a solução é(1/3,1/3), mas cada componente de Jacobi obedece y_(k+1)=1−2y_k. Logo y_k−1/3=(−2)^k(−1/3), divergindo em módulo. A matriz é inversível, o que não basta para a iteração convergir.

## Implementação e limites

Execute `python3 labs/jacobi-reutilizacao/iterations.py`. O laboratório usa int/Fraction, matrizes densas pequenas e diagonal não nula. Uma varredura exige O(n²) coeficientes e O(n) memória de vetores além da matriz. Não há implementação esparsa, escolha automática de ordenação ou alegação de desempenho de produção.

O programa racional retorna vetor, traço, número de passos e motivo de parada. Exige passo e resíduo escalados pequenos; orçamento esgotado permanece separado de convergência. No exemplo principal, com tolerância10⁻⁸, Jacobi para em16 e Gauss–Seidel em9 varreduras. Isso não é benchmark ou prova de que Gauss–Seidel seja sempre mais rápido. A solução exata inicial pode parar sem varreduras. O código float anterior da aula foi preservado e lança RuntimeError ao esgotar o orçamento.

Seis testes verificam: primeiros dois vetores; 784 estados com identidade de erro, contração, limite de cauda e limite de resíduo, a partir de49 inícios em dois métodos e oito passos; 245 identidades de dois passos no caso não dominante; recorrência divergente e orçamento; critérios de parada e preservação das entradas; contratos. Verificações finitas não demonstram um teorema para matrizes arbitrárias. Frações evitam arredondamento destes números, sem certificar dados de origem ou adequação física. Em float, passo/resíduo calculados não equivalem automaticamente a limites rigorosos de erro real.

## Referências consultadas

- Burden, Faires e Burden, *Análise Numérica*,10ª ed., §7.3: pp.501–502/PDF514–515 e p.505/PDF518, inspeção visual parcial em27/10/2026 do acervo privado autorizado. Sumário p.xiv/PDF12 também conferido: seção começa na p.500, mas esse início não foi lido neste bloco. Numeração impressa conferida em cada imagem; não se presumiu o mesmo deslocamento no livro inteiro. Jacobi, forma afim e aproveitamento das novas coordenadas. Sem leitura integral, transcrição dos exemplos4D ou distribuição do PDF/imagens privadas.
- [Netlib — Templates for the Solution of Linear Systems](https://netlib.org/templates/templates.html), consulta parcial em27/10/2026, §§2.2.1–2.2.2 e quadro de aplicabilidade em §2.3: significado das varreduras, armazenamento auxiliar e condições de uso. Complemento público; não foi instalado código externo.
- [USP — CCM0218 ComputaçãoIII](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0218): mapa curricular previamente registrado no curso. Nova abertura direta em27/10/2026 falhou por timeout; não se apresenta como nova leitura bem-sucedida nem confirmação da versão ministrada. Cobertura e exemplo não dependem de uma equivalência administrativa inventada.

Exemplos2D, demonstrações específicas, figura, exercícios e laboratório próprios. Revisão conceitual/didática pessoal pendente.

## Revisão em vinte minutos

Escreva os dois primeiros vetores de cada método; destaque qual x₁ foi usado na segunda equação. Derive os dois T e o limite7/36. Termine explicando a diferença entre ausência de uma garantia, orçamento esgotado e divergência demonstrada.
