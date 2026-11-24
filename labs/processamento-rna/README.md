# Processamento de RNA: do precursor às isoformas

Rascunho didático original · 27/10/2026 · revisão pessoal pendente.

## Transcrever não encerra a produção de um RNA funcional

A transcrição produz uma molécula de RNA, mas muitos transcritos ainda precisam de modificações, clivagens e montagem em complexos para exercer sua função. O processamento atua no RNA; não é uma remoção de íntrons do DNA do gene. Esta aula começa pelos pré-mRNAs nucleares de eucariotos e depois distingue outros RNAs. O esquema é uma orientação de processos, não uma regra de que tudo acontece somente depois de terminar a transcrição.

## O cap modifica a extremidade 5′

Em muitos mRNAs nucleares eucarióticos, uma guanosina modificada, a 7-metilguanosina, é ligada à extremidade 5′ por uma ponte incomum de 5′ para 5′. O cap participa da proteção e do reconhecimento por proteínas relacionadas ao processamento, exportação e tradução. Não é o códon AUG, não é uma base que substitui todo o primeiro éxon e não pode ser representado fielmente por uma letra G comum numa string de A, C, G e U.

## Clivagem e poliadenilação formam a extremidade 3′

No processamento típico de muitos pré-mRNAs de polimerase II, o RNA é clivado em um sítio reconhecido por complexos proteicos; a poli-A-polimerase acrescenta adenilatos à nova extremidade 3′. A cauda não é simplesmente a transcrição de um longo trecho de T no DNA. Sinais como AAUAAA fazem parte do reconhecimento, mas motivo isolado não determina sozinho todo sítio ou eficiência. Comprimentos e efeitos dependem do contexto; não adotamos um número universal de adenilatos para todo RNA.

## Éxon não é sinônimo de sequência traduzida

Éxons são segmentos retidos no RNA processado da isoforma em questão; íntrons são removidos na montagem correspondente. Um éxon pode conter região não traduzida, UTR, além de parte da sequência codificadora. Portanto juntar éxons não equivale a definir automaticamente uma proteína. A classificação depende da isoforma e da anotação: uma região retida em uma montagem pode ser omitida em outra. Regiões não traduzidas também podem participar de regulação.

## Splicing une segmentos do mesmo precursor

No splicing típico de pré-mRNA pelo spliceossomo, o complexo de RNAs e proteínas reconhece regiões do precursor, aproxima os pontos relevantes e promove a remoção do íntron e a ligação dos éxons. No mecanismo usual, forma-se um intermediário em laço envolvendo uma adenosina de ramificação, e a extremidade 3′-OH do primeiro éxon participa da união ao seguinte. Não se trata apenas de procurar duas letras no RNA: sinais adicionais, montagem do complexo e contexto importam.

## Transcrição e processamento podem estar acoplados

O cap pode ser acrescentado enquanto o RNA ainda é sintetizado. Componentes de processamento interagem com a maquinaria de transcrição e agem sobre o RNA emergente; eventos de splicing e de formação da extremidade 3′ também podem ser coordenados com a transcrição. Um fluxograma linear é útil para distinguir funções, mas não prova uma ordem temporal rígida para todo gene. Tampouco o cap, isoladamente, certifica que o RNA já esteja completamente processado.

## Uma miniatura para ler uma anotação fornecida

Use o segmento sintético 5′-AUGGUAGGAAGUAGUAG-3′, com 17 nucleotídeos. A atividade fornece três blocos: E1 ocupa posições [0,3), E2 [7,10) e E3 [14,17). Os intervalos [3,7) e [10,14) são omitidos na montagem A. Esta convenção começa em zero e exclui a posição final: [7,10) inclui 7, 8 e 9. É uma miniatura de coordenadas, muito curta para representar a maquinaria real de um gene; não é proposta de um precursor biologicamente viável.

## A primeira montagem conserva três blocos

Retenha E1, E2 e E3 na ordem em que aparecem: AUG, GAA e UAG. O resultado é 5′-AUGGAAUAG-3′, com 9 nucleotídeos; 8 dos 17 foram omitidos. A primeira junção fica entre o terceiro e o quarto nucleotídeo da montagem, e a segunda entre o sexto e o sétimo. A origem de cada base continua rastreável ao segmento fornecido. Cap e cauda poli-A não estão na string nem entram nessa contagem.

## Uma segunda montagem omite o bloco central

Na montagem B fornecida, retenha apenas [0,3) e [14,17). O resultado é 5′-AUGUAG-3′, com 6 nucleotídeos; 11 do precursor foram omitidos e há uma junção entre os blocos. Na biologia, escolhas alternativas de processamento podem gerar isoformas de RNA; isso não significa que toda combinação imaginada seja produzida, estável ou funcional. Aqui as duas anotações são entradas do exercício, não uma previsão do programa.

## Uma isoforma de RNA não garante uma nova proteína

Diferentes RNAs podem ter a mesma região codificadora e UTRs diferentes. Outros podem mudar o quadro, introduzir uma parada ou ser degradados. Saber que a string começa com AUG e contém UAG não demonstra iniciação, tradução ou atividade proteica. Para uma interpretação funcional, precisaríamos de contexto, anotações e evidências adequadas. A aula de tradução trata de quadro de leitura em trecho fornecido, não validação de uma proteína expressa.

## Exportação e controle de qualidade acrescentam outras etapas

RNAs associam-se a proteínas durante e após a síntese; processamento, empacotamento e reconhecimento influenciam exportação e destino. RNAs inadequadamente processados podem ser retidos e degradados. Isso não deve ser convertido em uma regra de que todo RNA exportado funciona ou de que todo erro é sempre detectado. Quantidade de RNA, estabilidade, localização, tradução e função são perguntas relacionadas, mas distintas.

## Outros RNAs têm processamento próprio

rRNAs e tRNAs também são produzidos como precursores e passam por clivagens e modificações. Eles não se tornam funcionais por serem traduzidos em proteínas: são componentes funcionais da maquinaria. O percurso de cap, splicing e poli-A de muitos mRNAs nucleares não é uma receita universal para todos os RNAs, organismos ou organelas. Mecanismos e destinos específicos permanecem para aprofundamento.

## O código seleciona intervalos; não descobre éxons

A função da atividade valida letras de RNA e intervalos fornecidos, concatena os trechos na ordem e devolve o mapa de posições de origem. Não reconhece promotores, sítios de splicing, ramificação, cap, clivagem ou cauda; não mede taxas nem prevê isoformas. Rejeitar sobreposição e coordenadas fora da string evita erros de anotação computacional, mas aceitar uma anotação não a torna biologicamente correta. Os testes verificam essa operação limitada.

## Sua revisão de vinte minutos

Explique separadamente o que faz o cap, o que é acrescentado na poliadenilação e o que é unido no splicing. Depois reconstrua as duas strings e conte as bases sem o código, declarando o que ficou fora da contagem. Dê um motivo para éxon não ser sinônimo de sequência codificadora e outro para isoforma não provar função. Registre suas dúvidas; o material e os testes não certificam aprendizagem ou prática experimental pessoal.

## Exercícios e resoluções

1. Na convenção [7,10), quantas posições são incluídas?

   Resolução: 7,8,9: 10−7=3.

2. Quantos nucleotídeos há no segmento fornecido AUGGUAGGAAGUAGUAG?

   Resolução: Os blocos têm 3+4+3+4+3=17 bases.

3. Quantos nucleotídeos há na montagem A, retendo [0,3), [7,10) e [14,17)?

   Resolução: 3+3+3=9.

4. Quantos nucleotídeos do segmento foram omitidos na montagem A?

   Resolução: 17−9=8.

5. Quantos nucleotídeos há na montagem B, retendo [0,3) e [14,17)?

   Resolução: 3+3=6.

6. Quantos nucleotídeos do segmento foram omitidos na montagem B?

   Resolução: 17−6=11.

7. Qual é a string da montagem A?

   Resolução: A montagem une AUG, GAA e UAG, sem as sequências omitidas.

8. Um éxon precisa conter somente sequência traduzida?

   Resolução: Éxons também podem conter UTRs.

9. No splicing do pré-mRNA, o íntron é removido do DNA do gene?

   Resolução: A reação atua no RNA precursor.

10. A cauda poli-A típica é acrescentada por uma enzima após clivagem do RNA?

   Resolução: A poli-A-polimerase acrescenta adenilatos à nova extremidade 3′.

11. O cap é o mesmo que o códon AUG?

   Resolução: Cap é uma modificação da extremidade 5′; AUG é uma trinca na sequência.

12. Aceitar duas anotações no programa prova que ambas as isoformas existem e funcionam na célula?

   Resolução: O programa aplica intervalos fornecidos e não fornece evidência biológica de existência ou função.

## Fontes e alcance da leitura

CCM0121, item II.5, programa público reaberto em 27/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121 . Ativação exibida 01/01/2025; versão ministrada não comprovada.

Alberts e colaboradores, Biologia Molecular da Célula, tradução da sexta edição, Artmed2017: cap.6, recortes pp.315–320/325–326/328, PDF351–356/361–362/364, consulta textual parcial em 27/10. PDF contado a partir de 1. P.316/PDF352 renderizada e inspecionada visualmente: estrutura do cap, ligação 5′–5′ e acoplamento com transcrição. Pp.318/320: recortes de legendas e mecanismos de splicing; p.325: clivagem/poliadenilação; pp.326/328: exportação e outros RNAs. Não se afirma leitura integral das páginas ou capítulo; arquivo privado não distribuído. Referência oficial inglesa de 2014 não tem paginação presumida igual à tradução.

OpenStax Biology2e §15.4, consulta parcial em 27/10: https://openstax.org/books/biology-2e/pages/15-4-rna-processing-in-eukaryotes . Apoio delimitado à identificação dos processos e legenda de UTRs. Não se adotaram generalizações de éxon como apenas sequência codificadora, de processamento como obrigatoriamente posterior à transcrição, nem números universais de meia-vida ou cauda. A aula usa texto e figura originais; não reproduz figuras da fonte.

O segmento de 17 nt e seus intervalos são uma miniatura computacional deliberada. A atividade não modela comprimentos reais de íntrons, reconhecimento, montagem do spliceossomo, taxas, cap, poliadenilação ou função. Não é um protocolo experimental nem uma sequência natural proposta.

## Laboratório e contratos

`annotation.py` seleciona posições fornecidas e retorna (sequência, mapa de origem). Entrada: string não vazia de ACGU em maiúsculas; lista/tupla não vazia de intervalos inteiros, em ordem e sem sobreposição. Final excluído. Não ordena silenciosamente, não aceita DNA com T e não acrescenta cauda. Não confere se o intervalo é um éxon biológico.

```sh
python3 labs/processamento-rna/annotation.py
python3 -m unittest discover -s labs/processamento-rna -t .
```

Testes verificam duas montagens e suas junções, todos os pares de intervalos ordenados em string curta por seleção independente de posições, limites semiabertos, rastreabilidade, preservação das entradas e rejeição de coordenadas inválidas. Não validam biologia ou experiência pessoal.

## Registro pessoal — preencher ao estudar

- Data:
- Como diferenciei cap, splicing e cauda:
- Onde aparece uma UTR em um éxon:
- O que a string não permite concluir:
- Dúvida que permaneceu:
