# Ligante livre, total e ocupação

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Na raiz: python3 -m unittest labs.ligante-receptor.test_experiment.

Equilíbrio 1:1 fechado, ideal, sítios independentes: Kd*C=(Rtotal-C)(Ltotal-C).
A raiz física está entre 0 e min(Rtotal,Ltotal); usa forma racionalizada.
Unidades nM sintéticas e volume fixo; Rtotal é sítio por volume, não por área.
Nada calcula resposta celular, tempo, internalização ou ativação do receptor.

Ocupação f=C/Rtotal=Llivre/(Kd+Llivre).
Em meia ocupação, Llivre=Kd, mas Ltotal=Kd+Rtotal/2.
Usar total na hipérbole superestima f neste modelo fechado e só aproxima
o exato quando a retirada de ligante livre é desprezível.
Em Ltotal=0, f=0, mas C/Ltotal é indefinida e depletion=None.

Quatro testes: 45 raízes por bisseção Decimal independente (70 dígitos),
inventários e equação de equilíbrio; dezesseis casos de meia ocupação;
303 estados com monotonicidade/inventários, dependências e limite de
receptor diluído; sinais da cinética em torno da raiz e contratos.
45 referências Decimal também verificadas pelo JavaScript.
O painel não integra a equação cinética usada no teste de sinais.

Fontes parciais, consulta em 16/10/2026:
- Alberts e colaboradores, Biologia Molecular da Célula, sexta edição,
  tradução Artmed 2017: pp. 458 e 813–815 (PDF 494 e 849–851).
  Página 814 inspecionada visualmente. O texto relaciona taxas a afinidade;
  aqui explicita-se que meia ocupação usa concentração livre, não
  automaticamente concentração total. Paginação não transferida ao inglês.
- [Hulme e Trevethick, 2010](https://doi.org/10.1111/j.1476-5381.2009.00604.x),
  Ligand binding assays at equilibrium: validation and interpretation.
  Busca indexada parcial: retirada de ligante pode distorcer interpretação.
  Acesso direto PMC encontrou verificação de navegador, sem contorno.
  Não se reproduzem protocolo, dados ou exercício do artigo.

Exemplos e gráficos próprios, sem experiência de bancada atribuída a Jhuann.
Pendente: classes/vias de sinalização, resposta dinâmica, amplificação,
realimentação, competição, cooperatividade, dados e revisão pessoal.
