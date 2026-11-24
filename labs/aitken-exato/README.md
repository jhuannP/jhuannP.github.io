# Aitken: erro modelado, erro observado e sensibilidade

Rascunho original para revisão de Jhuann,28/10/2026. Não é experimento real nem prova de domínio pessoal.

## Referências e limites

Referência temática: Burden,Faires e Burden,Análise Numérica,10ª edição. A paginação de Aitken não foi reconferida neste bloco.
Complemento efetivamente consultado parcialmente: [NIST DLMF §3.9(i),(iii)](https://dlmf.nist.gov/3.9),28/10/2026: definição de aceleração por razão dos erros e fórmulaΔ². Não foi lida a seção inteira. Deduções e exemplos abaixo são próprios.

## Executar

Na raiz do protótipo:

```sh
python3 labs/aitken-exato/sequence.py
python3 -m unittest discover -s labs/aitken-exato -t .
```

A função recebe inteiros/Fraction; rejeita float e bool. Segunda diferença zero gera ArithmeticError mesmo numa sequência constante já convergida. O gerador de dois modos aceita índices0–100 como limite operacional didático. Não é solver robusto de produção.

## Reconstruir as contas

Para x_n=L+Cqⁿ: Δx_n=Cqⁿ(q−1), Δ²x_n=Cqⁿ(q−1)². Com C≠0 e0<|q|<1 a correção é Cqⁿ e sobra L.
Para a=Aqⁿ,b=Brⁿ, expandir o numerador da diferença transformada produz ab(q−r)². Assim o erro é ab(q−r)²/[a(q−1)²+b(r−1)²], onde o denominador não é zero.
L2,A=B1,q1/2,r1/4 dá entradas4,11/4,37/16: Δ−5/4,Δ²13/16,estimativa27/13,erro1/13.

A harmônica1/(n+1) transforma-se em1/[2(n+2)]; a razão de erros tende a1/2, não0. Melhorar cada termo não basta para a definição assintótica de aceleração.

A sequência2−(99/100)ⁿ começa1,101/100,10199/10000 e é transformada em2. Mudar só o terceiro para20399/20000 (acréscimo1/20000) muda a estimativa para3. O denominador passa de−1/10000 para−1/20000. Não se estabelece tolerância universal para dados reais.

## Revisão pessoal de20min

1. Derive as duas diferenças e o cancelamento sem consultar a solução.
2. Refaça27/13 e a perturbação2→3 em frações.
3. Explique por que a harmônica não é acelerada nesta definição.
4. Diferencie transformação deslizante de reinício de Steffensen.

Testes exatos não analisam estabilidade geral, desempenho, dados reais, formas vetoriais ou condições suficientes para ordem quadrática de Steffensen. Essas extensões e revisão pessoal permanecem pendentes.
