# Gauss–Legendre2: exatidão e falha de amostragem

Material original em rascunho,29/10/2026. Fonte pública NIST DLMF §3.5(v),Eqs.3.5.18–3.5.20_1, https://dlmf.nist.gov/3.5#v ,consulta parcial: nós por polinômio ortogonal,pesos positivos,resto e exatidão. Derivação de dois pontos,contraexemplo,figura e código próprios. ProgramaCCM0218 reaberto29/10 pelo portal oficial:ativação01/01/2011;versão ministrada em2024 não comprovada. Bibliografia oficial Burden7ª,diferente da10ª escolhida por Jhuann. Exemplar10ª previamente identificado no acervo;corpo de Gauss não relido nesta rodada,paginação não presumida. Sem distribuir PDF privado ou copiar tabela da fonte.

O novo laboratório recebe apenas polinômios com coeficientes racionais em ordem crescente,grau≤8 e1–32painéis. Ao expandir f(c±h/√3),as potências ímpares cancelam e as pares usam1/3^j;isso permite resultado racional exato sem aproximar√3. Não é algoritmo geral para função arbitrária,gerador de nós ou quadratura adaptativa. O script flutuante anterior da aula foi preservado/executado;estes testes não certificam todos os seus arredondamentos.

Da raiz: `python3 -m unittest discover -s labs/gauss2-momentos -t .`; `python3 labs/gauss2-momentos/polynomial.py`.

Quatro testes:1875cúbicos/intervalos com integral por antiderivada,quarticos/refinamento,linearidade/mapeamento,contratos. Para f=(x²−1/3)² em[−1,1],Q1=0 mas I=8/45;Q2=1/6. Em quartico monico,I−Qn=(b−a)^5/(180n^4). Para funçãoC⁴ geral,uma cota exige conhecer M≥max|f⁽⁴⁾|;não a inferimos de duas amostras. Revisão pessoal20min:derivew1,r²1/3 e o fator da transformação,depois explique o contraexemplo. Fonte singular,dimensão maior,erro de avaliação e adaptação pendentes.
