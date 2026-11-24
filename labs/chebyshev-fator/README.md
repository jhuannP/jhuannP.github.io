# Chebyshev: raízes, Lobatto e o fator nodal

Laboratório original e racional; mantém o painel de Runge/Lobatto anterior. Reutiliza Lagrange em `labs/lagrange-bases/interpolation.py`. Executar da raiz, não como arquivo autônomo.

`python3 -B -m unittest discover -s labs/chebyshev-fator -t .`
`python3 -B -m labs.chebyshev-fator.factor`

N=4, alvo próprio f=x⁴. Nós uniformes−1,−1/3,1/3,1; Lobatto−1,−1/2,1/2,1. Errof−p é o produto nodal mônico: uniforme x⁴−10x²/9+1/9; Lobatto x⁴−5x²/4+1/4. Normas exatas16/81 e1/4, respectivamente: este contraexemplo não generaliza superioridade dos uniformes.

Raízes deT4,distintas de Lobatto, têm produtoT4/8=x⁴−x²+1/8 e norma1/8. Seus nós são irracionais: o laboratório usa coeficientes racionais exatos do produto, não aproximações racionais dos nós; testes com cos são conferênciafloat separada. `interpolant` é especificamente x⁴menos esse produto, não interpolador genérico. Mesmo com menor norma, raízes têm erro1/8emx1,enquanto as outras duas distribuições interpolam esse extremo exatamente.

`coefficients` calculaTn por recorrência para n0..16, `monic`normaliza o coeficiente líder. `sup_error` prova o máximo deste quartico par por y=x²∈[0,1], candidatos extremos e vértice; não usa malha para certificar. `mapped_error` transforma o produto nodal em intervalo[a,b] com fatorh⁴;fora do intervalo não vale a cota da norma. Int/Fraction no cálculo racional. Não há solver minimax geral, análise global de condicionamento ou nova rotina baricêntrica.

Fontes parcialmente consultadas30/10/2026: Burden/Faires/Burden,10ªedição,tradução/3ªbrasileiraCengage2016,§8.3pp579–583/PDF592–596 visualmente;sumárioPDF13. Offset13neste recorte,distinto de14em páginas anteriores. [NIST DLMF3.3(i)](https://dlmf.nist.gov/3.3#i),E3–E5,produto e resto com regularidade. ProgramaJúpiterCCM0218 reaberto30/10,ativação2011,versão ministrada não comprovada;fonte oficial listaBurden7ªedição,distinta do exemplar10. Não copiadas figuras/exercícios ouPDFprivado; exemplo,figura e implementação locais. Revisão pessoal pendente.
