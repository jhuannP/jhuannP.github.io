# LU — construção e reutilização

27/10/2026. Ampliação de uma aula existente de Computação III. Notas, figura e laboratório originais com apoio de IA, em rascunho. Revisão pessoal pendente; não certificam domínio de Jhuann. Mantidos o exemplo original, código float, desafio e IDs lu1/lu2.

## Modelo e construção

Matriz quadrada não vazia, fixa entre resoluções. Em Doolittle sem troca, A=LU, L inferior unitária e U superior. Pela multiplicação Aij=Σk Lik Ukj, calculamos, na ordem de linhas i:

- Uij=Aij−Σk<i Lik Ukj, para j≥i;
- Lji=(Aji−Σk<i Ljk Uki)/Uii, para j>i;
- Lii=1.

Índices começam em zero, como Python; soma vazia é zero. Pivôs Uii precisam ser não nulos. A rotina não usa a inversa de A explicitamente.

A=[[4,3],[6,3]] dá L=[[1,0],[3/2,1]] e U=[[4,3],[0,−3/2]]. Reconstrução: segunda linha [(3/2)4,(3/2)3−3/2]=[6,3]. O pivô negativo é válido; não se impôs positividade definida.

## Duas resoluções, uma fatoração

Progressiva: yi=bi−Σk<i Lik yk, para L unitária. Retroativa: xi=(yi−Σk>i Uik xk)/Uii.

| Lado direito | Intermediário y | Solução x | Verificação |
|---|---|---|---|
| (7,9) | (7,−3/2) | (1,1) | A(1,1)=(7,9) |
| (5,9) | (5,3/2) | (2,−1) | A(2,−1)=(5,9) |

Os fatores permanecem idênticos nas duas chamadas de `solve`. Refatorar a cada b desperdiça trabalho; se A mudar, esse reuso deixa de ser justificado em geral.

Para matrizes densas, custo aritmético fixo: uma fatoração O(n³), cada resolução O(n²), total O(n³+r n²). Não é benchmark. Frações exatas podem crescer e o custo de suas operações não é constante. Matrizes esparsas e implementações otimizadas exigem análise própria.

## Permutação também se aplica a b

Se PA=LU e Ax=b, então LUx=Pb. Resolver Ly=Pb e Ux=y. Sempre conferir a convenção da biblioteca: outra identidade pode representar outra convenção para P.

B=[[0,1],[1,1]] é inversível, det(B)=−1, mas falha na ordem sem troca. Troque as duas linhas: PB=[[1,1],[0,1]], L=I,U=PB. Para b=(1,2), Pb=(2,1), a solução correta é(1,1). Usar b sem trocar dá(−1,2), que não resolve o problema original. É uma permutação declarada antes da fatoração, não uma implementação geral de pivotamento.

Pivô zero informa falha do contrato desta rotina, não singularidade em todo caso. Matrizes singulares também podem ter representações LU, mas não são aceitas por este solver, que exige todos os pivôs não nulos.

## Código e verificações

`exact_lu.py` usa apenas Python padrão e Fraction. `factor(A)` copia os dados, retorna tuplas imutáveis L,U e não faz trocas. `solve(L,U,b)` confere dimensões, triangulação, diagonal unitária de L e pivôs de U; aplica progressiva/retroativa. Aceita `int` ou `Fraction`, sem `bool` ou `float`. Não altera A,b ou os fatores. `ZeroPivot` é uma exceção própria, sem classificar automaticamente a matriz como singular.

O Python float anterior da página foi preservado como outro recurso. Não é um solver geral robusto: comparação exata a zero não trata todos os pivôs numericamente ruins. A referência racional verifica identidades sem arredondamento, sem provar estabilidade do código float. Reconstrução LU=A, solução triangular e resíduo Ax−b são diagnósticos distintos; precisão também depende do condicionamento.

Rodar da raiz do protótipo:

```sh
python3 -m unittest discover -s labs/fatoracao-lu -t .
```

Cinco testes: exemplo e reuso imutável;81 matrizes 3×3 construídas de fatores conhecidos e três lados direitos cada; referência independente de Cramer em matrizes2×2 elegíveis; permutação correta/incorreta de b; contratos e pivô zero tardio. Construção e Cramer evitam usar apenas reconstrução pelo mesmo algoritmo como oráculo. Testes finitos não substituem demonstração algébrica ou análise geral de estabilidade.

## Resoluções dos exercícios

1. L[1][0]=3/2, divisão6/4 (ID lu1 preservado).
2. U[1][1]=−3/2, atualização3−(3/2)3 (ID lu2 preservado).
3. Para b₁, y0=7.
4. Para b₁, y1=9−(3/2)7=−3/2.
5. Para b₁, x1=1.
6. Para b₂, y1=9−(3/2)5=3/2.
7. Para b₂, x0=(5−3(−1))/4=2.
8. det(A)=det(L)det(U)=1×4×(−3/2)=−6.
9. Com PA=LU, usar Ly=Pb.
10. Primeiro pivô zero na matriz de determinante−1 prova falha da ordem, não singularidade.
11. Reuso denso: O(n³+r n²), sob custo aritmético fixo.
12. Reconstrução exata não prova estabilidade em float para qualquer matriz.

## Fontes e limites da consulta

[CCM0218 — programa oficial](https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0218), reaberto em27/10/2026: métodos diretos incluem eliminação, LU e Cholesky. Ativação01/01/2011; captura indicada de um mês antes. Versão efetivamente ministrada em2024/2 não comprovada.

Burden, Faires e Burden, *Análise Numérica*, tradução da10ª edição norte-americana, terceira edição brasileira, Cengage2016: §6.5, páginas impressas445–447/PDF459–461, inspecionadas visualmente em27/10 para reuso, custo, resolução triangular e eliminação. O arquivo não ofereceu extração textual útil nessas páginas. Sem leitura integral da seção; não se reproduziram exemplo, tabela ou figura. O programa oficial cita Burden7, enquanto o exemplar escolhido é10; paginação e exercícios não foram transferidos entre edições. A identidade PA=LU já introduzida na aula de Gauss é deduzida algebricamente aqui para o exemplo de troca. Fonte privada não distribuída.

## Próxima revisão e lacunas

Em20min: fatorar o exemplo, resolver os dois b e explicar o lado direito permutado. Campo de compreensão pessoal permanece em branco. LU com pivotamento geral, análise de crescimento/estabilidade, dados mal condicionados, famílias esparsas e desempenho medido continuam pendentes. Cholesky permanece uma unidade própria.
