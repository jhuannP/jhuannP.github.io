# Potência: direção e resíduo

Modelo original, matrizes2×2 e vetores racionais prescritos; não são dados de pesquisa. Normalização em norma infinita, até100 passos. Não encerra cedo nem certifica dominância; devolve história incluindo k=0.

Da raiz: `python3 -B -m unittest discover -s labs/potencia-residuo -t .` e `python3 labs/potencia-residuo/power.py`.

Para A=diag(3,1),x0=(1,1),xk=(1,3^−k). Em k1: Rayleigh14/5, resíduo absoluto∞3/5, indicador escalado3/29; em k2: Rayleigh122/41. O código antigo normaliza em norma2: vetores com escalas diferentes representam a mesma direção, mas resíduos absolutos podem ter valores diferentes.

η=||Ax−ρx||∞/[(||A||∞+|ρ|)||x||∞], com norma matricial por soma de linha. Invariante a escala não nula da matriz e do vetor. Não é cota de erro do autovetor. Caso A=0,rho=0 tem denom0/resíduo0 eη0 por convenção; tentar iterar um produto nulo falha.

Teste independente: fórmula de potências diagonais para quatro espectros×nove instantes; ausência da componente dominante e ciclo±1; escalas; material float anterior; contratos. Sem bibliotecas adicionais.

Fonte temática parcial30/10/2026: [Netlib, Power Method](https://netlib.org/utk/people/JackDongarra/etemplates/node95.html), contexto hermitiano, condição inicial e razão espectral. Algoritmo em imagem não foi transcrito; Burden10cap9 permanece referência da aula, não capítulo relido neste bloco. Derivações, figura e implementação locais. Revisão pessoal pendente.
