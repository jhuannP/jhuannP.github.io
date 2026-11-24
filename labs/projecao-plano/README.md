# Projeção ortogonal em um plano de ℝ³

22/10/2026. Rascunho para revisão pessoal. Aprofunda `al-projecao`, preservando o exemplo de reta, seus dois exercícios e o painel `orthogonalProjection`. Painel adicional `planeProjection`, não substituição silenciosa da dimensão ou métrica.

## Fontes e vínculo curricular

- Elon Lages Lima, *Álgebra Linear*, IMPA2014, título/CIP/copyright reconfirmados no acervo. Referência complementar, não promovida à bibliografia oficial de CCM0213. Corpo §10: p.123/PDF134 (reta/norma), pp.125–126/PDF136–137 (base ortogonal, projeção no subespaço e ponto mais próximo), consulta parcial em22/10. Página124/PDF135 foi extraída com o recorte, sem desenvolver aqui o algoritmo de Gram–Schmidt ou seus exercícios. Não se afirma leitura integral. Nenhum PDF, figura ou exercício privado distribuído.
- [Interactive Linear Algebra, Georgia Tech, §6.3 Orthogonal Projection](https://textbooks.math.gatech.edu/ila/projections.html), consulta direta parcial: decomposição, unicidade, equações normais e propriedades da projeção. Exemplos/figuras/código desta unidade são próprios; identidades do plano derivadas e verificadas localmente, não transcrição de exemplo do texto.
- Grupo5 do mapa oficial de MatemáticaIII/CCM0213: operadores em espaços euclidianos, ainda parcial. Notas pessoais não importadas/revisadas. Complemento para mínimos quadrados, sem alegação de cobrir toda a disciplina ou experiência de pesquisa.

## Construção própria

u=(1,0,1), v=(0,1,1), S=span(u,v)={z=x+y}. São independentes, mas u·v=1. n=(−1,−1,1), n·n=3. Projeção pela normal r=(b·n)n/3, p=b−r. Matriz P=(1/3)[[2,−1,1],[−1,2,1],[1,1,2]].

A=(u v) tem Gram AᵀA=[[2,1],[1,2]], determinante3. Equações normais dão α=(2x−y+z)/3, β=(−x+2y+z)/3, p=(α,β,α+β). P=I−nnᵀ/3=A(AᵀA)⁻¹Aᵀ. Fórmula com inversa exige colunas independentes; não é receita para uma matriz de Gram singular.

Para qualquer q∈S, b−q=r+(p−q), termos ortogonais. Portanto ||b−q||²=||r||²+||p−q||², com mínimo apenas emq=p. Existência em dimensão finita segue de uma base ortonormal; projeção no subespaço zero existe e valezero, mesmo que a fórmula da reta não aceite gerador zero.

b=(1,1,1): p=(2/3,2/3,4/3), r=(1/3,1/3,−1/3), ||r||²=1/3. Soma ingênua das duas projeções de reta dá(1,1,2); resíduo tem produtos−1/−1 comu/v. Não é regra geral para bases não ortogonais. No controle, q=p+s u, erro²=1/3+2s². A família é uma ilustração; prova de mínimo foi para todo S.

Com gerador adicional w=u+v, (α−t,β−t,t) representa o mesmo p para qualquer t: vetor projetado único, coeficientes não únicos. P²=P, Pᵀ=P, Pu=u, Pv=v, Pn=0. Idempotência isolada não caracteriza ortogonalidade.

## O que o gráfico representa

Base ortonormal: ê₁=u/√2, ê₂=(−1,2,1)/√6, ê₃=n/√3. b,p,q compartilham a componente emê₂. O gráfico usa somente coordenadas emê₁/ê₃, mas é uma seção afim de componenteê₂ fixa, não projeção arbitrária de toda a cena3D. Distâncias entre os três pontos são preservadas porque suas diferenças têm componenteê₂ zero. Interseção com S é a linha horizontal; o ponto(0,0) do desenho pode representar um vetor não nulo emℝ³.

Escalas iguais e janela quadrada adaptativa, informado pelos eixos. Azul marca b−p; preto tracejado, b−q. Pontos coincidentes recebem rótulo combinado, inclusive b=p=q no zero/s0. A tabela preserva as três coordenadas originais. Mudar s não muda p. Vetores são adimensionais, sem interpretação física escolhida.

## Executar e conferir

```sh
python3 labs/projecao-plano/experiment.py
python3 -m unittest discover -s labs/projecao-plano -t .
```

Quatro testes: matriz obtida independentemente pela inversa2×2 da Gram, idempotência/simetria/imagem/núcleo;625estados de parâmetros com frações e3125candidatos independentes por combinações de geradores; representações redundantes e contraexemplo da soma ingênua; distâncias no corte, zero, vetores no plano/normal e contratos. Trinta referências cruzam JS/Python em vetores, coeficientes, erros e coordenadas da seção.

Fonte dos números é a construção algébrica própria, não medida experimental. Não se analisou estabilidade de equações normais em ponto flutuante, espaços infinitos, pesos ou dados estatísticos. Comparar o desenho não substitui prova. Revisão pessoal permanece pendente; próximas aulas de Gram–Schmidt/mínimos quadrados ainda precisam aprofundamento próprio.
