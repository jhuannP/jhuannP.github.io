# Bootstrap: duas distribuições e cobertura

29/10/2026. Modelo original para revisão de Jhuann. Nenhum dado real ou conclusão de pesquisa.

## Pergunta

A enumeração exata do bootstrap torna um intervalo percentil nominal de 95% um procedimento com cobertura de 95%?

Três observações iid Bernoulli(p). O alvo é p=E[X]. Fixada a contagem k, a média bootstrap tem distribuição K*/3 com K*~Binomial(3,k/3). Percentis são os menores valores cuja CDF atinge 1/40 e 39/40, sem interpolação; intervalo fechado. Não há correção básica, studentização ou BCa. A distribuição bootstrap e o intervalo não usam o p verdadeiro.

Para k=0,1,2,3, os intervalos são [0,0],[0,1],[0,1],[1,1]. Nos grupos mistos, as massas nas duas extremidades são pelo menos 1/27>1/40, e a acumulada antes de 1 é no máximo 26/27<39/40. Para 0<p<1, a cobertura é P(1<=K<=2)=1-(1-p)^3-p^3=3p(1-p). Em p=1/4, as massas externas são 27,27,9,1 sobre64 e a cobertura é36/64=9/16=56,25%. Em p=1/2, cobertura75%, ainda abaixo do nominal95%. Nos parâmetros de fronteira p=0 ou1, cobertura1; não estender a fórmula interior por continuidade.

B não aparece: eliminamos a aproximação Monte Carlo. Isso não resolve a diferença entre a distribuição empírica e a população. O intervalo realizado não recebe uma probabilidade frequentista posterior de conter p. O painel antigo da aula reamostra listas fixas, não exibe esta cobertura.

## Outro limite, demonstrado sem simulação

Para n finito de observações iid Uniforme[0,theta], theta>0, o máximo M é estritamente menor que theta quase certamente. Qualquer máximo bootstrap não paramétrico é <=M. Logo a extremidade superior de um intervalo percentil bruto do máximo também é <=M<theta: cobertura de theta é zero. Isso trata do extremo populacional, não de estimar a média, e não se estende a todos os intervalos bootstrap. A prova analítica usa continuidade e suporte; o script não simula nem valida modelos uniformes.

## Código e verificação

`python3 labs/bootstrap-cobertura/risk.py`

`python3 -B -m unittest discover -s labs/bootstrap-cobertura -t .`

Biblioteca padrão, int/Fraction, 1<=n<=5, 0<=p<=1 e0<alpha<1; bool/float rejeitados. Cobertura exata por mistura de contagens. Cinco testes: exemplo;20 pares(n,k) e três níveis comparados com enumeração de posições;105 leis de coleta comparadas com sequências;99 parâmetros interiores e fronteiras/simetria;contratos. A fórmula do caso n3 é demonstrada, não inferida da grade finita.

## Fontes parciais

Magalhães e Lima, Noções de Probabilidade e Estatística,7ªedição2010/reimpressão2011,§7.4 pp244–246/PDF259–261: consulta textual parcial29/10/2026 sobre intervalo aleatório e interpretação por repetições, sem nova inspeção visual ou leitura integral. Fórmulas OCR da normal não usadas neste laboratório. Exemplo de bootstrap e contraexemplo do máximo próprios, não atribuídos ao livro.

NIST, Confidence Limits for the Mean, seção Purpose, consultada29/10/2026: https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm . Apoia interpretação de cobertura por repetição, não esta dedução binomial nem garantia de bootstrap. Fontes privadas não distribuídas. PVA não reconsultado como fonte deste recorte.

## Próximo estudo

Reconstruir os quatro intervalos, obter36/64 sem código e explicar por que enumeração exata não garante95%. Métodos corrigidos, aproximação assintótica, outras populações, dados dependentes e revisão pessoal pendentes.
