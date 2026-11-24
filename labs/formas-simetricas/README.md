# Matrizes simétricas e formas quadráticas

27/10/2026. Notas de aula originais com apoio de IA, em rascunho. Revisão pessoal de Jhuann pendente. Ampliação da aula existente: 16 seções e 12 exercícios, preservando as três seções, os dois exercícios, o exemplo, o Python e o desafio anteriores. Uma preparação didática não certifica domínio nem autoria independente de Jhuann.

## Hipóteses e fundamentos

Matrizes reais simétricas em bases ortonormais do espaço euclidiano de dimensão finita. Simetria implica ⟨Az,w⟩=⟨z,Aw⟩. Para autovetores p,r de autovalores distintos λ,μ, segue (λ−μ)⟨p,r⟩=0, portanto são ortogonais. Autovetores de um mesmo autovalor não precisam ser ortogonais; pode-se escolher uma base ortonormal no autoespaço. Uma base não ortonormal pode esconder a simetria da representação de um operador auto-adjunto.

Em 2×2, A=[[a,b],[b,c]] tem polinômio λ²−(a+c)λ+ac−b² e discriminante (a−c)²+4b²≥0. No caso zero, b=0 e a=c, logo A=aI; caso positivo dá dois autovalores reais distintos e uma base ortonormal própria.

A aula contém esboço do teorema espectral real em dimensão finita: máximo da forma na esfera compacta dá um autovetor pelo teste da derivada em direções tangentes; seu complemento ortogonal é invariante; indução completa a base. Não é uma prova para dimensão infinita. O livro usa uma rota por subespaço invariante de dimensão1 ou2; a aula explicita uma rota alternativa com compacidade e cálculo diferencial.

## Exemplo preservado e coordenadas próprias

A=[[2,1],[1,2]], q(x,y)=2x²+2xy+2y²=(x+y)²+x²+y². A decomposição prova positividade para todo vetor não nulo; q(1,−1)=2 isoladamente não a provaria.

Os autovetores unitários e₊=(1,1)/√2 e e₋=(1,−1)/√2 formam as colunas de Q. QᵀQ=I, QᵀAQ=diag(3,1). Com u=(x+y)/√2 e v=(x−y)/√2, a forma vira3u²+v². A norma se conserva; ‖z‖²≤q(z)≤3‖z‖². Similaridade da representação do operador e congruência da forma têm a mesma expressão nesta base ortogonal, pois Q⁻¹=Qᵀ; não generalizar essa coincidência a matrizes de base arbitrárias.

Em geral, q=Σλᵢwᵢ² explica positividade/semidefinição/indefinição pelos sinais. Para a simétrica 2×2 e a>0, completar quadrados dá

q=a(x+by/a)²+[(ac−b²)/a]y².

Isso prova a suficiência de a>0 e det A>0. Necessidade: testar (1,0) dá a>0; testar (−b/a,1) dá det A/a>0. A divisão não é usada quando a=0. Diagonal positiva não basta: [[1,2],[2,1]] dá q(1,−1)=−2. Determinante positivo também não basta: −I é negativa definida. Para semidefinição, apenas os menores iniciais não negativos não bastam: diag(0,−1) é um contraexemplo. Estes são argumentos universais/contraexemplos, sem substituir prova por uma malha finita de vetores.

## Família e figura originais

Aₜ=[[2,t],[t,2]] tem os mesmos autovetores normalizados, com λ₊=2+t e λ₋=2−t. É positiva definida para |t|<2, positiva semidefinida singular para |t|=2 e indefinida para |t|>2. Na figura, o corte (x,y)=v(1,−1)/√2 tem q=(2−t)v²; t=1 sobe, t=2 é plano e t=3 desce, enquanto o outro eixo permanece positivo nesses três casos. Um corte negativo refuta positividade; um corte positivo não prova a forma toda.

O código evita aproximar √2: usa r=x+y e s=x−y, e verifica qₜ=(2+t)r²/2+(2−t)s²/2. São coordenadas não normalizadas, distintas de u,v. Em t=2, há direção nula; em t=3, q(1,−1)=−2 e q(1,1)=10.

## Energia e mínimo

Modelo adimensional sintético E(z)=q(z)/2−fᵀz, com A positiva definida e f fixo. Gradiente Az−f, equilíbrio Az*=f. Para A=[[2,1],[1,2]], f=(1,0), z*=(2/3,−1/3), E(z*)=−1/3. Energia negativa não contradiz positividade da forma: existe o termo linear.

Expandindo z=z*+h e usando Az*=f, os termos lineares se cancelam:

E(z*+h)−E(z*)=q(h)/2>0 para h≠0.

Logo o mínimo é global único. No exemplo, a diferença é ao menos ‖h‖²/2. A semidefinição não garante esse resultado com qualquer f: A₂ e f=0 têm uma linha de mínimos. A rotina exige positividade definida e rejeita demais casos; rejeição do algoritmo não afirma que todos os outros problemas sejam insolúveis. Não se atribuem unidades mecânicas ou resultados experimentais a este exemplo.

## Referência, páginas e alcance

Elon Lages Lima, *Álgebra Linear*, IMPA2014: §13 pp.156–161/PDF167–172 consultadas parcialmente em27/10/2026, incluindo auto-adjunção, Teoremas13.1–13.7, ortogonalidade, espectro e positividade. p.160/PDF171 conferida visualmente. Página do PDF contada desde1; não é o número impresso. Não houve leitura integral do livro. Livro complementar localizado no acervo privado, fora da bibliografia oficial consultada de CCM0213; não substitui a busca das referências oficiais ainda não identificadas. Exemplares privados e imagens de suas páginas não distribuídos.

O mapa existente de CCM0213 registra ativação pública15/07/2024, reabertura27/10/2026 e aprovação2024/2 pelo panorama dos históricos. Isso não comprova o programa efetivamente ministrado ou domínio individual. As nove áreas oficiais continuam parciais. Redação, família, figura, exercícios e aplicação de energia são preparados com deduções próprias; a rota de prova geral é explicitamente distinta da usada no livro.

## Laboratório e testes

Da raiz: `python3 -m unittest discover -s labs/formas-simetricas -t .`.

`Symmetric2(a,b,c)` representa [[a,b],[b,c]] e aceita int/Fraction, sem bool/float. `classify` usa o critério 2×2 e trata os seis casos (positivo/negativo definido, positivo/negativo semidefinido não nulo, nulo, indefinido). `completed_square` exige pivô a≠0, sem inferir positividade por essa restrição isolada. `minimizer` só atende o caso positivo definido, com solução exata por inversão2×2. Métodos recebem vetores de duas componentes racionais; instâncias são imutáveis.

Cinco testes selecionados: expansão contra produto matriz-vetor e quadrados completados em125 matrizes×25 vetores; classificação de343 matrizes contra sinais das raízes via traço/determinante; identidade e autovetores da família; mínimo/resíduo de energia sob deslocamentos e forças diferentes; contraexemplos e contratos. Testes finitos detectam erros de implementação; não substituem as provas de positividade ou garantem estabilidade em ponto flutuante. Não é biblioteca de álgebra linear geral.

## Exercícios e revisão pessoal

Respostas dos12 itens:2; não;3;0;4;3; matriz escalar; positiva semidefinida singular;−2;2/3;−1/3; a>0 e det A>0. Dicas e resoluções completas estão na aula.

Dois blocos de20min propostos: primeiro reconstruir a base e as coordenadas próprias; depois classificar a família, justificar os contraexemplos e provar o cancelamento da diferença de energia. Dúvidas e avaliação pessoal permanecem em branco. Pendentes: inversa e diagonalização gerais, SVD, estabilidade, outros produtos internos, caso complexo e operadores em dimensão infinita.

Conferência de entrega: cinco testes locais e14 do catálogo aprovados;717 estruturas MathML conferidas. Em390px, exercício12 rejeitou determinante isolado e aceitou o critério completo pelo Enter. Figura legível, documento sem transbordamento e console sem erros. Leitor de tela, Windows real e revisão pessoal pendentes.
