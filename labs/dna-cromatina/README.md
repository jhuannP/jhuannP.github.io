# DNA e cromatina: contagem com fronteiras

Rascunho didático original, 16/10/2026. Execute experiment.py com Python 3.
Na raiz do protótipo, rode python3 -m unittest labs.dna-cromatina.test_experiment.
Não há medições de uma amostra real ou resultados da IC neste modelo.

N cernes de 147 pb, N-1 linkers de comprimento igual, nenhum DNA externo.
B=147N+ℓ(N-1); histonas=8N, duas de cada tipo por cerne.
Aproximação de contorno do DNA B estendido: 0,34B nm. Não é comprimento
espacial da cromatina ou grau de compactação. Fração enrolada não prevê expressão.
N=1 tem zero linkers internos. ℓ=0 é limite de contagem, não prova estabilidade.

Painel: mapa linear, intervalos com início zero e fim exclusivo. Não é imagem
molecular ou simulação dinâmica. N=1..8, ℓ=0..80 pb, cerne selecionado limitado
ao existente. Python também produz reverso-complementar para ACGT maiúsculo
não vazio, representando ambas as sequências na orientação 5′→3′.

Quatro testes: 648 cadeias contra montagem explícita de símbolos, inventários,
extremos e sensibilidade; 5460 sequências ACGT de comprimentos 1..6 verificadas
por pareamento, involução e conservação GC; unidades, seleção e domínio.
Referências de contagem são independentes de somar a fórmula do modelo.
JavaScript tem 32 cadeias contra montagem explícita, sem alegação de comparação
direta JS/Python. A contagem não valida as hipóteses biológicas.

Fonte do acervo: Alberts e colaboradores, Biologia Molecular da Célula, sexta
edição, tradução Artmed 2017. Capítulo 4, trechos pp. 176–177 e 187–189
(PDF 212–213 e 223–225), página 188 inspecionada visualmente. Distinguir pb de
nucleotídeos: uma passagem abrevia imprecisamente 147 nucleotídeos, mas o texto
seguinte e a figura identificam 147 pares. Não transferir paginação para inglês.

Complemento primário: [Ou e colaboradores, ChromEMT, 2017](https://doi.org/10.1126/science.aag0025).
Consulta parcial por busca indexada, 16/10/2026. Acesso direto a PMC/UC encontrou
verificação de navegador, sem contorno. O resultado reportado em células
examinadas limita uma generalização de fibra obrigatória e uniforme de 30 nm.
Não se implementou sua análise de microscopia nem se generalizou a todos os contextos.
Nenhuma figura privada ou micrografia foi reproduzida.

Pendentes: topologia, organização superior, remodelamento, variabilidade
estrutural, dados e métodos, revisão pessoal e demais tópicos da disciplina.
