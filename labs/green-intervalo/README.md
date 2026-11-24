# Green no intervalo — aprofundamento

29/10/2026. Percurso complementar, rascunho assistido por IA; revisão pessoal pendente. Operador −d²/dx² em [0,L], L>0, Dirichlet zero. Não representa disciplina formal adicional ou experiência de pesquisa.

## Reconstruir antes de programar

1. Faça duas retas que zerem nas bordas. Continuidade e salto direita−esquerda=−1 fornecem G=min(x,s)[L−max(x,s)]/L. O sinal é determinado por −G″=δ.
2. Separe a integral em [0,x] e [x,L]. Defina I1=∫s f(s) e I2=∫(L−s)f(s). Mostre u=[(L−x)I1+xI2]/L, u′=(I2−I1)/L e u″=−f para f contínua. Unicidade: a diferença de soluções é uma reta com bordas zero.
3. Exemplo original: f=6x,L=1, u=x−x³, u(1/2)=3/8. Bordas2 e−1: some a reta2−3x, obtendo2−2x−x³.
4. Fonte estreita simétrica: altura Q/(2ε), suporte [a−ε,a+ε] interior. Área Q preservada. Demonstre |u_ε−QG|≤|Q|ε/2 usando que G é1-Lipschitz em s. No centro a=1/2,Q=1,L=1, a diferença é ε/4; para ε=1/8, a altura da resposta é7/32, não a altura4 da fonte.
5. Diferencie solução C² com f contínua, solução C¹ por partes da faixa e solução contínua com quina da fonte ideal. Convergência uniforme de funções não dá automaticamente convergência uniforme das derivadas.

Se x tem unidade de comprimento e u de U, G tem unidade comprimento, f de U/comprimento² e Q de U/comprimento. Em uma corda estática de tensão T constante, −Tu″=carga por comprimento exige fator1/T na resposta. Exemplos computacionais adimensionais; sem experimento ou dinâmica.

## Executar e conferir

Na raiz do protótipo:

```sh
python3 labs/green-intervalo/green.py
python3 -B -m unittest discover -s labs/green-intervalo -t .
```

`solution` integra polinômios de coeficientes crescentes e grau até8. `uniform_patch` integra a faixa uniforme; `green` avalia o kernel, incluindo bordas zero. Entradas somente int/Fraction; fonte pontual física pressupõe s interior, e a faixa deve estar estritamente no interior. Valores em bordas no helper são extensões de avaliação, não deltas de fronteira. Python antigo/desafio e painel `greenSource` preservados; o painel continua uma fonte pontual em [0,1], não a faixa.

Cinco métodos de teste: 243 pares x,s por simetria/bordas/positividade e21 saltos; 729 avaliações de27 fontes polinomiais em três comprimentos/nove pontos por integração independente da EDO; 150 avaliações de faixas por potências truncadas e limite de erro; linearidade/bordas; contratos. Frações verificam identidades desses casos; não validam toda teoria ou um experimento.

## Fontes realmente consultadas

- [S.G.Johnson, Notes on the 1d-Laplacian Green’s function](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/e1dc3f76e50d80b7f00a8040a25c0ddf_MIT18_303F14_Green_explicit.pdf), datado12/10/2011, no cursoMIT18.303/2014. pp.1–2, consulta textual parcial29/10/2026. Tentativa de screenshotp.2 falhou. A passagem da p.2 toma limites x′→x na variável da fonte, enquanto G′ deriva na variável de observação. Isso explica o sinal que inicialmente pareceu inconsistente; não foi identificado erro. Nesta aula, o salto direita−esquerda é tomado em x, com s fixo, e vale−1.
- [S.G.Johnson, Introduction to Green’s functions and operator inverses](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/e2ac5c8e1b07eb8d9bed4aca68e4cf09_MIT18_303F14_green.pdf), datado9/10/2011, mesmo curso. Recortes textuais pp.3–7: representação, fonte de largura finita e salto. Consulta parcial29/10/2026; sem afirmar inspeção visual ou leitura integral. A construção assimétrica da fonte não foi reproduzida; usamos exemplo simétrico e contas próprias.

Fontes públicas complementares, sem nova busca/identificação de livro privado nesta unidade. Deduções, exercícios, figura e limite uniforme aqui organizados são material original de estudo, sem transcrever exercício das notas. Não comprovam domínio, matrícula no MIT ou resultado científico.
