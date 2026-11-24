# Teoria neutra: origem, destino e taxa

27/10/2026. Notas de aula originais assistidas por IA, em rascunho para revisão pessoal. Primeiro recorte de uma lacuna do programa, sem análise de dados, identificação de seleção ou pesquisa pessoal executada.

Retomar `b3-wright-fisher`. População ideal diploide com M=2N cópias, reprodução neutra, tamanho constante, sem migração; destino de uma variante sem novas mutações durante a trajetória. A chance eventual de fixar é i/M. Para origem única,1/(2N); chance não é a mesma de fixar já na geração seguinte. M4,i1:1/4 eventual versus1/256 na próxima geração.

Com taxa neutra μ₀ por cópia/sítio/geração, entrada esperada2Nμ₀ e chance eventual1/(2N) dão produtoμ₀. O código chama isso de origens destinadas à fixação. Interpretar como taxa de substituição de longo prazo exige o regime ideal neutro com mutações raras e sem problemas de recorrência/sobreposição no sítio. Não diz que uma origem já se fixa no instante da introdução. A função de produto não verifica biologicamente esse regime; apenas confere sua aritmética e unidades.

Exemplo sintético N50,μ₀10⁻⁵: entrada0,001,chance0,01,produto10⁻⁵. N100:0,002×0,005,mesmo produto. Independência da taxa em relação a N não elimina efeitos populacionais sobre chance individual, tempos ou diversidade. Neutralidade seletiva não é ausência de função nem negação de adaptação.

## Fontes e limites

Charles F. Aquadro, “Molecular Evolution”, cap.V.1 em The Princeton Guide to Evolution, PUPcopyright2014; o programa/arquivo citam2013, divergência editorial já registrada. Consulta textual parcial em27/10/2026 de pp.367–370/PDF389–392: glossário, teoria e trecho§3 em p.370 sobre chance de fixação/taxa. PDF contado a partir de1; colunas e figura de relógio não foram reproduzidas. Sem leitura integral, nova inspeção visual ou distribuição do PDF privado.

[Kimura1968, DOI10.1038/217624a0](https://www.nature.com/articles/217624a0) é referência histórica identificada por metadados e resumo indexado, não uma leitura integral feita nesta aula. A abertura direta falhou no acesso da editora. Foi localizado um PDF de três páginas na coleção de textos clássicos da Blackwell, mas sem texto extraível pelo navegador; não foi usado como se todo o artigo tivesse sido lido. O fundamento explicativo veio do capítulo do acervo e das deduções próprias. Não foi identificada a seleção de artigos efetivamente lidos por Jhuann na disciplina.

## Conferências reproduzíveis

Execute `python3 labs/teoria-neutra/fixation.py`. Quatro testes: resolução racional do sistema de absorção para M2..10 versus i/M; normalização, média e equação harmônica de cada linha binomial; comparação de horizonte finito e eventual em M2..6; produto de taxa para12 combinações de população/μ₀ e exemplo; contratos. O código limita a matriz a2..12 cópias por custo didático. O sistema linear é resolvido separadamente, sem inserir i/M como resposta na rotina. Fronteiras h₀0/h_M1 são impostas por definição do evento; absorção e unicidade fundamentam sua interpretação.

A teoria não é demonstrada empiricamente pelos testes. Quase neutralidade, seleção ligada, demografia real, mutações recorrentes, relógios calibrados, evolução do genoma e testes estatísticos de neutralidade continuam pendentes. Próxima ação de20min: distinguir mutação/polimorfismo/fixação e reconstruir o cancelamento2N sem confundir tempo de fixação com taxa média. Revisão pessoal pendente.
