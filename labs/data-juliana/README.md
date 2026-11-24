# Calendário e data Juliana — recorte didático

## Calendário, contagem e escala respondem perguntas diferentes

Um calendário organiza rótulos como ano, mês e dia. A data Juliana, JD, organiza uma contagem contínua de dias e suas frações; não é o calendário Juliano. A escala de tempo informa a que leitura física ou convencional o número se refere. Nesta aula, datas do calendário gregoriano e leituras já fornecidas em UT1 serão transformadas em JD(UT1). Não estamos descobrindo UT1 a partir de um relógio civil.

## O calendário gregoriano precisa de uma regra de bissextos

O ano astronômico não contém um número inteiro de dias. No calendário gregoriano, um ano divisível por 4 é bissexto, exceto os divisíveis por 100; entre estes, os divisíveis por 400 continuam bissextos. Assim 2000 tem 29 de fevereiro e 2001 não. O calendário Juliano usa a regra simples de quatro anos. Esta aula não reconstrói datas históricas de transição entre calendários: o laboratório usa apenas o calendário gregoriano no recorte 1901–2099.

## A passagem por um inteiro ocorre ao meio-dia

Na convenção de JD usada aqui, o limite inteiro corresponde ao meio-dia, não à meia-noite. O USNO publica, por exemplo, 1 de janeiro de 1978 às 00h UT1 como JD 2443509,5. Não apague a parte fracionária pensando que ela é um erro de arredondamento. A origem histórica da contagem é anterior à nossa era; não precisamos implementar essa origem ou o calendário antigo para trabalhar com uma referência moderna explicitada.

## Uma referência moderna permite construir o número

Em 1 de janeiro de 2000 às 12h UT1, JD(UT1)=2451545. Às 00h da mesma data, o valor é 2451544,5. Use a meia-noite como referência do algoritmo: conte Δd datas gregorianas desde 01/01/2000, com sinal negativo para datas anteriores, e acrescente a fração t/86400. Aqui t é a leitura UT1 em segundos contados desde 00h, no intervalo [0,86400). É uma representação de leitura de escala, não a medição de uma duração em segundos SI.

JD(UT1)=2451544,5+Δd+t/86400

## Exemplo resolvido: quatro horários da mesma data

Queremos representar 01/01/2000 às 06h UT1. O deslocamento de datas é Δd=0; t=6×3600=21600. A fração é 21600/86400=1/4; somada a 2451544,5 resulta em 2451544,75. Ao meio-dia acrescentamos 1/2 e obtemos 2451545. Às 18h a fração é 3/4 e o resultado é 2451545,25. Na meia-noite seguinte, Δd=1 e t=0: 2451545,5. O número cresce continuamente, sem reiniciar quando muda a data do calendário.

## O bissexto muda a contagem de datas

De 28 de fevereiro a 1 de março de 2000, sempre às 00h UT1, ΔJD é 2: existe 29 de fevereiro entre os rótulos. Em 2001, a diferença é 1. Um algoritmo que assume todos os anos com 365 dias erra depois de um dia bissexto. No laboratório, datetime.date valida o rótulo e calcula o deslocamento em dias; Fraction preserva exatamente as frações racionais fornecidas. Isso elimina arredondamento neste cálculo, sem tornar exatos dados de tempo que foram medidos com incerteza.

## UTC, UT1 e TT precisam continuar identificados

UT1 acompanha a rotação terrestre; UTC é a escala usada como base do tempo civil; TT aparece em cálculos astronômicos com outra definição. Alterar o rótulo UTC para UT1 não converte o valor. O algoritmo sideral da sequência anterior requer escalas declaradas. Nesta etapa, quem chama jd_ut1 deve já possuir a data e a leitura em UT1. O programa não busca correções de orientação da Terra, não resolve segundos intercalares e não converte TT. Uma data Juliana sem identificação da escala deixa incompleta a descrição do instante.

## O que significa subtrair duas datas Julianas

Se as duas entradas pertencem ao mesmo modelo e à mesma escala, ΔJD fornece a diferença na coordenada de tempo expressa em dias. Para duas leituras UT1 da mesma data, 06h e 18h, a diferença é 1/2 dia de coordenada. Multiplicar por 24 dá 12 horas dessa leitura. Não apresente essa conta como cronometração precisa de 43200 segundos SI: a conversão física entre escalas exige informações adicionais. Misturar JD(UT1) e JD(TT) na subtração também muda o problema.

## Um contrato explícito evita conversões silenciosas

A função jd_ut1 recebe ano, mês e dia como int, sem bool, e seconds_ut1 como int ou Fraction. Aceita anos de 1901 a 2099 e exige 0≤t<86400; rejeita datas inválidas, floats e texto. Para representar 00h do dia seguinte, forneça a data seguinte e t=0, em vez de t=86400. O retorno é uma Fraction. A escolha de faixa e tipos torna o exercício auditável; não é uma limitação da definição geral de JD.

## Conferir o algoritmo e manter a próxima lacuna visível

Os testes comparam todas as datas do recorte com a fórmula publicada pelo USNO, além de três exemplos oficiais, bissextos e fronteiras. A implementação usa deslocamento de calendário a partir de uma referência; o oráculo usa uma expressão aritmética distinta. Isso confere o algoritmo no domínio declarado, mas não valida um relógio ou observação real. A continuação deve obter e justificar UT1/TT antes de aplicar um cálculo sideral a uma data civil. AGA0106 permanece em elaboração, com programa da turma e revisão pessoal pendentes.

## Exercícios e resoluções originais

- Que fração de dia corresponde a 06h de uma leitura UT1? **Resolução:** 6/24=1/4.
- Qual JD(UT1) corresponde a 01/01/2000 às 00h? **Resolução:** Doze horas antes de JD 2451545: subtraia 1/2.
- Qual JD(UT1) corresponde a 01/01/2000 às 06h? **Resolução:** 2451544,5+1/4=2451544,75.
- Qual JD(UT1) corresponde a 02/01/2000 às 00h? **Resolução:** 2451544,5+1=2451545,5.
- Qual é ΔJD entre 28/02/2000 e 01/03/2000, ambas às 00h UT1? **Resolução:** 2000 é bissexto: passa também por 29/02.
- Qual é ΔJD entre 28/02/2001 e 01/03/2001, ambas às 00h UT1? **Resolução:** 2001 não é bissexto; são datas consecutivas.
- Qual é ΔJD entre 06h e 18h UT1 da mesma data? **Resolução:** (18−6)/24=1/2 dia de coordenada.
- Quanto vale Δd de 31/12/1999 em relação a 01/01/2000? **Resolução:** A data está um dia antes da referência.

## Código e verificação

Na raiz do site: `python3 -m unittest discover -s labs/data-juliana -t .` e `python3 -m labs.data-juliana.calendar_jd`. Núcleo usa apenas datetime e fractions da biblioteca padrão. Teste enumera todas as datas de 1901–2099 contra a fórmula USNO, válida neste domínio positivo sem ambiguidade entre truncamento e piso. Não há dados externos, consulta de relógio ou dependência instalada. Referência: 01/01/2000 às 12h UT1 corresponde a JD(UT1)=2451545; não se identifica este instante com a época J2000.0 definida em TT.

## Fontes e limites

Consultas parciais em 22/10/2026: [USNO JD](https://aa.usno.navy.mil/faq/JD_formula), definição, três exemplos e fórmula de referência; [USNO Calendars](https://aa.usno.navy.mil/faq/calendars), regras gregorianas; [USNO UT](https://aa.usno.navy.mil/faq/UT), distinção de escalas; [USNO GAST](https://aa.usno.navy.mil/faq/GAST), referência numérica e escala. Página leap_years falhou; não foi lida nem citada como suporte. Não se transportam para este código as precisões do algoritmo sideral USNO. Não se converte UTC ou TT. Código, exemplos e diagrama próprios, sem cópia de código-fonte do USNO.

Rascunho assistido por IA para revisão pessoal. Bibliografia nominal e programa da turma de 2022 pendentes; RN preservado. Aula com dez seções/oito exercícios. Trilha com três aulas/28 exercícios, cinco grupos parciais/cinco lacunas. Próxima revisão pessoal: conferir meio-dia, bissexto e escala; próxima etapa de conteúdo: dados e conversões de escalas antes de prever o céu de uma data real.

Verificação: cinco testes do novo laboratório aprovados, incluindo 72684 datas comparadas à fórmula USNO; 13 testes de catálogo e 551 estruturas MathML aprovados. Figura inspecionada no celular a 390 px, documento com largura 375 px, nenhum erro de console observado. Questão 2 rejeitou 2451545 e aceitou 2451544,5; navegação curso→aula confirmada. RN e limitação curricular visíveis. Prévia data-juliana-mobile.jpg. Catálogo atual: 504 aulas/3211 exercícios; relatório COBERTURA_ATUAL.md recalculado. Sem validação de relógio, observação, UTC/TT ou suíte global de todos os laboratórios. Saldo semanal após o bloco: 91%; parada em 65%.
