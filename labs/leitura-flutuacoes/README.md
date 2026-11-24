# Oficina de leitura e flutuações

Aula original em rascunho, revisão pessoal pendente. Recorte complementar para BiologiaIII; não identifica a lista de artigos da turma nem comprova atividade pessoal.

## Fonte

Luria,S.E.; Delbrück,M. Mutations of Bacteria from Virus Sensitivity to Virus Resistance. Genetics28(6),491–511,1943. [DOI](https://doi.org/10.1093/genetics/28.6.491). [Cópia acadêmica consultada](https://www.bx.psu.edu/~anton/bioinf1-2014/delbruck-luria-1943.pdf). Consulta textual parcial29/10/2026 à introdução/formulação pp.491–494/PDF1–4 e início da discussão/resumo pp.509–510/PDF19–20. Metadados conferidos no índice público PubMed17247100. Tentativa de PDFNLM retornou timeout; não registrada como leitura. Sem transcrição de tabelas, dados, figura ou protocolo; não houve leitura integral nem nova validação visual do PDF.

A fonte contrapõe hipóteses sobre a origem da resistência e usa distribuições para distingui-las. Nossa oficina acrescenta dois modelos finitos originais para raciocinar sobre média, variância e alternativas. Não reproduz a distribuição histórica de Luria–Delbrück, não estima taxa de mutação nem reanalisa dados.

## Modelos próprios e execução

Na raiz: `python3 labs/leitura-flutuacoes/models.py`; testes: `python3 -m unittest discover -s labs/leitura-flutuacoes -t .`.

A: Binomial(15,1/8). B: soma de quatro Bernoulli independentes, pesos1,2,4,8, mesma probabilidade. Médias15/8; variâncias105/64 e595/64. P(B≥8)=1/8, P(B=0)=2401/4096. A lei B é convolução exata; teste independente enumera moedas. Fraction, limites pequenos declarados no código; sem MonteCarlo, ajuste, tecido ou dinâmica de população.

Contraexemplo próprio: P=0 ou1/4 com chances iguais e X|P~Binomial(15,P). Média15/8, variância315/64. Dispersão extra também pode nascer de heterogeneidade. Médias e variâncias teóricas não são estimativas de uma amostra nem teste de significância.

## Revisão

Preencher `ficha.md` com páginas, separar hipótese/observável/previsão/limite. Ler o artigo integral, conferir tabelas e incertezas, confirmar lista da turma e registrar discussão pessoal continuam pendentes. A explicação acessível do exemplo não equivale ao vídeo previsto no programa. Nenhuma publicação ou atividade de laboratório foi executada.
