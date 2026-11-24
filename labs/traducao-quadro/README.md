# Tradução: ler um quadro não demonstra expressão

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão de Jhuann.

## Da sequência de RNA à cadeia de resíduos

A tradução utiliza a sequência de um RNA mensageiro para orientar a síntese de uma cadeia polipeptídica. A sequência escrita é apenas uma representação: na célula, o processo depende de ribossomos, tRNAs, aminoácidos carregados e fatores. Aqui começamos com um trecho de RNA hipotético já escrito de 5′ para 3′ e um quadro de leitura fornecido. Não inferimos processamento, início de tradução ou expressão a partir de um texto de letras.

## Três bases formam um códon

Um códon é um grupo de três nucleotídeos consecutivos na leitura estabelecida. Com quatro bases possíveis por posição, existem 4³=64 trincas. Na tabela padrão adotada nesta aula, 61 correspondem a aminoácidos e três a parada. O fato de haver mais códons que aminoácidos permite que diferentes códons tenham a mesma atribuição; isso não torna a leitura de um códon ambígua dentro da tabela especificada.

4³=64 códons

## O quadro decide onde separar as trincas

Para uma sequência escrita em uma orientação fixa, podemos começar o agrupamento no primeiro, no segundo ou no terceiro nucleotídeo. O laboratório chama essas escolhas de quadros 0, 1 e 2, com índices iniciados em zero. Alterar o quadro muda quais bases são agrupadas e pode mudar a sequência de resíduos e a posição de parada. Os três agrupamentos possíveis de um fragmento não identificam qual deles é utilizado por uma célula.

RNA é lido de 5′ para 3′

## Exemplo resolvido: um trecho com parada explícita

Use 5′-AUGGCUUUUUAAGG-3′. No quadro zero, separe AUG | GCU | UUU | UAA | GG. Na tabela padrão, AUG corresponde a metionina (Met, M), GCU a alanina (Ala, A) e UUU a fenilalanina (Phe, F). UAA sinaliza parada e não adiciona um resíduo. A cadeia representada é MAF, escrita de N-terminal para C-terminal. As duas bases GG depois da parada não entram nessa leitura. O exemplo é sintético e não representa uma proteína funcional identificada.

Quadro 0: AUG | GCU | UUU | UAA

## Comparar os outros agrupamentos

Com a mesma sequência, o quadro um separa UGG | CUU | UUU | AAG e sobra G. A leitura hipotética dá WLFK: triptofano, leucina, fenilalanina e lisina, sem parada nas trincas completas fornecidas. O quadro dois separa GGC | UUU | UUA | AGG e dá GFLR: glicina, fenilalanina, leucina e arginina. Esses resultados são comparações de agrupamento. O código não exige AUG nem procura um início; portanto não apresenta esses produtos como cadeias realmente sintetizadas.

Quadros distintos → agrupamentos distintos

## Códon e anticódon têm orientações opostas

Um tRNA atua como adaptador: apresenta um anticódon que interage com o códon e uma extremidade ligada ao aminoácido correspondente. No pareamento ideal do exemplo, o códon 5′-GCU-3′ pode ser alinhado com o anticódon 3′-CGA-5′. Escrever esse anticódon de 5′ para 3′ dá AGC, não CGA. A correspondência do aminoácido ao tRNA também depende de enzimas de carregamento. A regra simples de complementaridade não descreve sozinha modificações de bases ou o pareamento flexível em células reais.

5′-GCU-3′ / 3′-CGA-5′

## A cadeia cresce na extremidade C-terminal

Durante o alongamento, a cadeia ligada a um tRNA é transferida para o aminoácido ligado a outro tRNA, formando uma nova ligação peptídica. A adição ocorre na extremidade C-terminal; a ordem dos resíduos é apresentada de N para C. Uma cadeia linear de três resíduos possui duas ligações peptídicas entre eles. A tabela computacional apenas fornece rótulos de resíduos: ela não calcula carregamento de tRNAs, gasto energético, velocidades ou o mecanismo catalítico do ribossomo.

3 resíduos → 2 ligações peptídicas

## Parada não é um quarto aminoácido

Na tabela padrão, UAA, UAG e UGA sinalizam terminação. O símbolo * usado em tabelas e no código marca essa instrução; ele não é um resíduo da cadeia. Na terminação usual descrita aqui, fatores de liberação permitem liberar a cadeia do tRNA. O laboratório interrompe a leitura no primeiro códon de parada encontrado no quadro fornecido e registra a posição. Ele não modela o reconhecimento molecular nem situações de recodificação.

UAA, UAG, UGA: parada no código padrão

## Código degenerado não significa sequência equivalente

GCU, GCC, GCA e GCG têm a mesma atribuição alanina na tabela padrão. Trocar uma dessas trincas por outra pode preservar o resíduo nesse ponto, mas não garante que todos os aspectos da expressão sejam iguais. Além disso, nem toda troca na terceira posição preserva a atribuição: UGG codifica triptofano e UGA é parada nesta tabela. O laboratório aplica apenas o código padrão; variantes mitocondriais e outras tabelas precisam ser escolhidas explicitamente em outra análise.

GCU, GCC, GCA, GCG → Ala

## Início e fim exigem contexto biológico

AUG pode atuar como início em contextos apropriados e também pode codificar metionina no interior de uma região traduzida. Sua presença isolada não comprova que a tradução começa ali. Um trecho sem parada fornecida também não demonstra que uma cadeia seja ilimitada: podemos estar vendo apenas parte do RNA ou o quadro inadequado. A escolha do início e os sinais de término dependem do sistema e do contexto, que não foram inferidos neste exercício.

## Sequência prevista não comprova proteína madura

Mesmo uma leitura correta segundo uma tabela não demonstra quantidade de RNA, tradução efetiva, estabilidade da cadeia, enovelamento, modificações, localização ou função. Processamento de RNA e regulação pós-transcricional continuam tópicos próprios por desenvolver. Uma análise de sequência tem de declarar o que recebeu, qual tabela usou, qual quadro adotou e onde terminou. Dados ou resultados experimentais exigiriam evidência adicional, separada do exercício sintético.

## Contrato do laboratório e revisão

O programa aceita letras A,C,G,U maiúsculas e um quadro 0,1 ou 2. Valida a entrada inteira, lê somente trincas completas e para no primeiro stop do código padrão. Retorna a sequência de resíduos, os códons lidos, o índice de início da parada em base zero e o sufixo não lido. Se não encontra parada, retorna None nessa posição e preserva bases incompletas no sufixo. Isso é um decodificador de quadro informado, não um preditor de genes ou um simulador completo da tradução.

## Exercícios e resoluções

- Quantas trincas diferentes existem com quatro bases e três posições? **Resolução:** 4×4×4=64.
- Quantos códons do código padrão correspondem a aminoácidos, descontando os três de parada? **Resolução:** 64−3=61.
- No quadro zero do trecho AUGGCUUUUUAAGG, quantos resíduos aparecem antes da parada? **Resolução:** AUG, GCU e UUU dão M, A e F: três resíduos.
- No mesmo quadro, quantos códons completos são lidos incluindo a parada UAA? **Resolução:** AUG, GCU, UUU e UAA: quatro.
- Quantas bases do trecho ficam depois da parada no quadro zero? **Resolução:** Depois de UAA restam GG: duas bases.
- Uma cadeia linear de três resíduos tem quantas ligações peptídicas entre eles? **Resolução:** Há uma ligação entre o primeiro e o segundo e outra entre o segundo e o terceiro.
- No laboratório com índices começando em zero, em qual posição começa UAA no quadro zero do exemplo? **Resolução:** Os três primeiros códons ocupam os índices 0–8; UAA começa em 9.
- Quantos quadros de leitura por agrupamento em trincas há numa orientação fixa de RNA? **Resolução:** É possível começar na primeira, segunda ou terceira base.
- Qual sequência de resíduos corresponde ao quadro zero do trecho AUGGCUUUUUAAGG até a primeira parada? **Resolução:** A parada não adiciona resíduo; o produto representado é MAF.
- O anticódon alinhado como 3′-CGA-5′ fica como quando escrito de 5′ para 3′? **Resolução:** Inverta a ordem para reescrever a mesma fita na direção oposta: 5′-AGC-3′.
- Encontrar AUG sozinho demonstra que uma célula inicia a tradução nesse ponto? **Resolução:** A escolha real do início depende do contexto e da maquinaria; o programa não a infere.
- Uma sequência decodificada por uma tabela basta para demonstrar uma proteína funcional? **Resolução:** Ainda faltam evidências de síntese, processamento, estabilidade, estrutura e função.

## Fontes e execução

Alberts e colaboradores, Biologia Molecular da Célula, 6ª ed. em português, Artmed 2017, capítulo 6, pp.334–335,339,348 (PDF370–371,375,384), consulta textual parcial em 22/10/2026. [NCBI, código padrão tabela 1](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1), tabela factual conferida; T do registro convertido em U para RNA. [OpenStax Biology 2e §15.5](https://openstax.org/books/biology-2e/pages/15-5-ribosomes-and-protein-synthesis), visão geral consultada parcialmente. Não foram reproduzidos exercícios ou figuras. O trecho e o exemplo computacional são sintéticos.

Na raiz: python3 -m labs.traducao-quadro.experiment; testes: python3 -m unittest discover -s labs/traducao-quadro -t .

O decodificador não exige AUG, não escolhe início e não encontra genes. Uma saída em outro quadro é uma leitura hipotética, sem comprovação biológica. O campo stop_offset é o índice de início da parada em base zero; suffix é o trecho após a parada ou, se ela não aparece, as bases restantes sem formar trinca.


## Código genético e tradução — 22/10/2026

Nova aula b2-traducao-quadro, 12 seções/12 exercícios: códon, código padrão, quadros 0/1/2, leitura do RNA 5′→3′, anticódon antiparalelo, tRNA, cadeia N→C, parada e limites de inferência. Trecho sintético AUGGCUUUUUAAGG: quadro zero representa MAF e para em UAA (índice 9, base zero), deixando GG após a parada. Quadro um dá WLFK e sobra G; quadro dois dá GFLR e não sobra base. As duas leituras alternativas não demonstram início ou síntese real.

Fontes primárias consultadas parcialmente em 22/10/2026: Alberts e colaboradores, Biologia Molecular da Célula, sexta edição em português/Artmed2017, capítulo 6, pp.334–335,339,348 (PDF370–371,375,384), leitura textual para trincas/tRNA, sentido da cadeia e parada; [NCBI, código padrão tabela 1](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1), tabela factual e introdução; [OpenStax Biology 2e §15.5](https://openstax.org/books/biology-2e/pages/15-5-ribosomes-and-protein-synthesis), visão geral. Sem leitura integral ou reprodução de páginas, exercícios e figuras. A tabela NCBI é apresentada com T; o código local usa U em RNA. Início real, variantes do código e recodificação não são inferidos.

Laboratório labs/traducao-quadro/: decodificador específico do quadro fornecido, com validação da sequência inteira, parada no primeiro stop e registro de sufixo. Não exige AUG nem procura genes. Cinco testes novos aprovados: 64 trincas, degenerescência/atribuições e três stops; três quadros do exemplo; parada não contada como resíduo e sufixo não lido; janelas curtas/incompletas; contratos. Doze testes de catálogo e 535 estruturas MathML aprovados; catálogo revalidado após legenda móvel. Suíte global não repetida; nenhum modelo JavaScript alterado.

Navegador: figura legível em 390 px; legenda longa foi encurtada e reinspecionada. Largura da página igual à tela e nenhum erro de console observado. Contagem quatro de resíduos rejeitada, três aceita: UAA é parada. Prévia: traducao-quadro-mobile.jpg. Conteúdo em rascunho assistido por IA, sem resultado experimental ou habilidade pessoal inferidos.

Biologia II passa a seis aulas próprias/70 exercícios. O grupo II.6 muda de lacuna para parcial; total nove grupos parciais e nove lacunas, nenhum completo. Etapa cinco do percurso liga transcrição à nova aula, mantendo processamento e regulação como pendências. Situação acadêmica, programa oficial e histórico pessoal preservados. Catálogo: 501 aulas/3034 exercícios em rascunho.

Próxima revisão pessoal: separar os três quadros, explicar por que a parada não entra na cadeia e distinguir leitura de sequência de expressão. Próximo bloco global: aprofundar cinemática ou vetores em Física I, após conferir fonte e material existente, mantendo alternância entre disciplinas. Saldo semanal após bloco: 93%; parada operacional em 65%.
