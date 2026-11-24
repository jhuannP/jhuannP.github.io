# Newton: diferenças divididas e atualização

Laboratório original com `Fraction`, 1 a12 nós distintos, reais racionais, sem NumPy. A rotina copia os dados, preserva a associação entre nós e coeficientes e rejeita floats/bool. A avaliação isolada não certifica que os coeficientes correspondam a dados externos. Não aceita nós repetidos: Hermite exige outra construção.

```sh
python3 labs/newton-divididas/newton.py
python3 -m unittest discover -s labs/newton-divididas -t .
```

Exemplo próprio: nós−1,1,2 com valores2,0,2. Diferenças de primeira ordem−1,2 e segunda1. Coeficientes2,−1,1: p=x²−x e p(3/2)=3/4. Inclua(3,8): o produto nodal em3 é8; a discrepância8−6 é2; novo coeficiente1/4. O novo polinômio passa pelos quatro pontos e vale1/2 em0. A correção não afeta os três nós antigos.

Construção: n(n−1)/2 diferenças para n dados, O(n²) operações racionais; avaliação aninhada O(n), atualização de um nó O(n). A contagem ignora crescimento do tamanho em bits das frações. Em cada ordem da tabela in-place, atualizar de trás para frente preserva os dois elementos da ordem anterior. No exemplo quadrático, uma varredura crescente indevida muda o coeficiente de ordem2 de1 para4/3. Essa falha é algoritmo, não efeito de arredondamento.

O exemplo de nós0 e10⁻⁹ com valores0 e10⁻⁶ tem inclinação1000. Frações exatas eliminam arredondamento nesse cálculo, mas não a sensibilidade dos dados ou erros de modelagem. A extrapolação não recebe garantia pelo simples fato de interpolar.

Fontes consultadas parcialmente em29/10/2026:
- Burden/Faires/Burden, Análise Numérica10ª, Cengage2016, §3.3 pp.137–138/PDF151–152: notação, recorrência e forma de Newton, inspeção visual. Tentativa textual PDF140–150 retornou páginas vazias e avisos Flate; não foi contada como leitura. PDF142/p.128 apenas localizou seção3.2; não é fonte da recorrência. Sem leitura integral, cópia de tabela/algoritmo/exercício ou distribuição do exemplar.
- [NIST DLMF3.3(iii–iv)](https://dlmf.nist.gov/3.3), Eq.3.3.34–3.3.38: diferenças e representação; leitura parcial, sem implementação de nós confluentes.

O programa CCM0218 registra Burden7ª; o acervo10ª é referência separada. Versão ministrada em2024 não comprovada. Exemplos, deduções redigidas, código e testes próprios. Quatro testes com Lagrange independente, seis permutações,27 conjuntos de valores e sete pontos, atualização versus reconstrução, sensibilidade, constante, nó único e contratos. Não provam estabilidade geral em float. Revisão pessoal pendente.
