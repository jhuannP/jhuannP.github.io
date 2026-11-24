# Tempo sideral como relação angular

Aula própria para AGA0106, sem atribuir conteúdo à turma de 2022. Uma hora angular equivale a 15°, e uma volta 24h=360°. GST, TSL e α têm entradas em [0,24), longitude λ em graus positiva a leste, de −180° a 180°. TSL=(GST+λ/15) mod24. H=((TSL−α+12) mod24)−12, ramo [−12,+12). +12h é representado por −12h. H cresce para oeste.

Exemplos próprios: GST22h, λ+30° e α23,5h dão TSL0h, H+0,5h=+7,5°. GST2h, λ−45° e α1h dão TSL23h, H−2h=−30°. Se α0h no primeiro caso, H0° conecta ao exemplo anterior φ−30°, δ0°: altura60°, azimute0°. São ângulos sintéticos; não são o céu de uma data ou localização de Jhuann.

Na raiz do site:

    python3 -m labs.tempo-sideral.angles
    python3 -m unittest discover -s labs/tempo-sideral -t .

Núcleo aceita int/Fraction sem bool/float/texto. wrap24 reduz horas assinadas; hours_to_degrees converte sem normalizar. Os testes de integração dependem do laboratório irmão labs/coordenadas-celestes; baixar só este diretório não inclui essa dependência de teste. O núcleo angles.py não depende dele. Cinco testes cobrem exemplos, unidades, fronteiras, 125 configurações por fases complexas, reconstrução de α, ligação geométrica e contratos.

GMST e GAST referem-se a equinócio médio/verdadeiro e exigem α compatível. As relações angulares não calculam GST a partir de UTC, calendário, longitude ou fuso. USNO usa UT1 e TT e datas Julianas em seu algoritmo aproximado; o algoritmo e sua precisão não foram implementados aqui. Não se aplica precessão, nutação, refração, catálogo ou efeméride. Próxima sequência deve tratar calendários/data Juliana e escalas antes de ligar uma data civil ao céu.

Fontes consultadas parcialmente em 22/10/2026: [Fiona Vincent, notas de St Andrews de 1998, capítulo 6, cópia didática na UFSC](https://minerva.ufsc.br/~kanaan/astro1/aula-posicao/chapter6.htm), relações TSL/GST/H; [USNO — Computing Approximate Sidereal Time](https://aa.usno.navy.mil/faq/GAST), médio/aparente, longitude leste e escalas. A fórmula de longitude oeste da primeira fonte foi convertida explicitamente à convenção leste positiva, consistente com USNO. Código, figura e exercícios próprios, sem transcrição ou redistribuição de fontes.

Doze seções/dez exercícios em rascunho assistido por IA para revisão de Jhuann. Mapa provisório passa a quatro grupos parciais/seis lacunas; não se marcou conteúdo completo nem alterou histórico RN. Revisão pessoal: derivar o sinal de longitude e fechar a volta antes de converter H em graus. Observações e materiais pessoais, bibliografia nominal do acervo e programa da turma de 2022 permanecem pendentes.


## Fechamento de verificação e unidades — 22/10/2026

Revisão conceitual das relações locais nas duas fontes já vinculadas: Fiona Vincent cap.6 usa longitude oeste positiva; USNO usa longitude leste positiva. Reconferência parcial das duas páginas, sem executar o algoritmo USNO. Corrigida a escrita dimensional para λ/(15°/h), e adicionadas duas fórmulas estruturadas MathML (longitude e ramo de H). Não se implementou conversão de datas nem se atribuiu precisão observacional.

Cinco testes do laboratório aprovados, incluindo 125 configurações e integração geométrica; 13 testes de catálogo aprovados; 550 fórmulas MathML e verificações de foco/ajuda/limpeza conferidas. No navegador em 390 px, questão 5 rejeitou −23,5 e aceitou 1/2; figura e fração com unidade inspecionadas visualmente, documento com largura 375 px, nenhum erro de console observado. Prévia: tempo-sideral-mobile.jpg. Suíte global dos demais laboratórios não repetida. Duas aulas/20 exercícios na trilha, quatro grupos parciais/seis lacunas; programa da turma de 2022 ainda pendente. Próxima ação pessoal: justificar o sinal da longitude e resolver os casos de passagem por zero. Para desenvolvimento posterior: calendário, data Juliana e distinção entre escalas de tempo, com fonte e contrato explícitos antes de ligar datas à transformação horizontal. Saldo semanal confirmado ao final: 91%; parada em 65%.
