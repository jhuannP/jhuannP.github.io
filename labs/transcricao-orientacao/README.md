# Transcrição: fita molde, RNA e orientação

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: nucleotídeos, orientação do DNA e complementaridade; programação é opcional.

## Transcrever é produzir RNA a partir de um molde de DNA

Na transcrição celular considerada aqui, a RNA-polimerase sintetiza uma cadeia de RNA usando uma das fitas de um trecho de DNA como molde. O produto é RNA, não uma segunda dupla-hélice de DNA. Muitos RNAs têm funções que não incluem servir de molde para uma proteína. Nesta aula tratamos princípios de orientação e pareamento, não toda a expressão gênica.



## RNA não é quimicamente DNA com outra letra

RNA contém ribose, enquanto DNA contém desoxirribose. Na representação canônica usada no laboratório, RNA usa A,C,G,U e DNA usa A,C,G,T. O RNA pode formar estruturas por pareamento entre regiões da própria cadeia; desenhá-lo como uma sequência de letras não descreve sua estrutura tridimensional. A substituição T→U é uma comparação entre certas sequências, não uma transformação química do DNA em RNA.



## Síntese e leitura do molde têm sentidos opostos

A cadeia de RNA cresce pela adição de ribonucleotídeos à sua extremidade 3′, portanto a síntese é 5′→3′. A fita molde é percorrida no sentido 3′→5′. Os substratos são ribonucleosídeos trifosfato; RNA-polimerases podem iniciar a cadeia sem o primer exigido pelas DNA-polimerases replicativas. Este modelo não calcula química da catálise, energia ou cinética.

Molde lido 3′→5′; RNA sintetizado 5′→3′

## Fita molde e fita não molde são papéis daquela unidade

Para um mesmo trecho transcrito, a fita molde determina o RNA por complementaridade antiparalela. A outra fita de DNA é chamada não molde ou, frequentemente, codificante: escrita no mesmo sentido 5′→3′ do RNA, coincide com sua sequência no trecho ideal, exceto T no DNA e U no RNA. O nome “codificante” para essa fita não prova que o RNA será traduzido. Superior/inferior são rótulos do desenho; o papel depende da unidade transcrita.



## Declare as pontas antes de comparar letras

Use o duplex sintético com fita superior 5′-ACGTAACC-3′ e inferior alinhada 3′-TGCATTGG-5′. Escolha a inferior como molde. Ao lê-la da esquerda para a direita, de 3′ para 5′, cada T pede A no RNA; G pede C; C pede G; A pede U. O produto é 5′-ACGUAACC-3′. Ele é complementar à inferior e tem a sequência da superior com T trocado por U.

Molde alinhado: 3′-TGCATTGG-5′ → RNA: 5′-ACGUAACC-3′

## Um molde escrito 5′→3′ precisa ser lido ao contrário

Sequências em arquivos e exemplos costumam ser fornecidas 5′→3′. Se o molde inferior do exemplo for reescrito nesse padrão, ele será 5′-GGTTACGT-3′. Para gerar o RNA canônico, percorra essa entrada da direita para a esquerda e aplique as correspondências DNA→RNA: A→U,T→A,C→G,G→C. Apenas trocar T por U no molde produziria outra sequência e estaria errado.

Molde 5′-GGTTACGT-3′ → RNA 5′-ACGUAACC-3′

## Trocar a fita molde muda o produto e a direção no desenho

No mesmo duplex, se a superior 5′-ACGTAACC-3′ for a fita molde, sua leitura3′→5′ acontece da direita para a esquerda. O RNA, escrito canonicamente 5′→3′, será GGUUACGU. Não existe contradição: a síntese continua 5′→3′, mas o sentido em relação à página mudou. O programa exige a escolha da fita; não a infere a partir da sequência.



## O trecho do laboratório é fornecido como um intervalo

A referência computacional é a sequência superior escrita5′→3′. O intervalo [start,stop) inclui start e exclui stop. Com start=2 e stop=6 em ACGTAACC, o trecho superior é GTAA, de quatro bases. Se a inferior for molde, o RNA correspondente é GUAA. Esses índices são uma convenção de representação, não posições de um gene real ou um mecanismo de iniciação.

Comprimento do trecho = stop−start

## As regras dos dois métodos precisam da anotação correta

from_template recebe DNA molde 5′→3′ e devolve RNA 5′→3′ por leitura reversa e complementaridade. from_coding recebe a fita não molde 5′→3′ do mesmo trecho e troca T por U. Usar o método certo com a fita errada ainda dá uma sequência formalmente válida, porém não o produto pedido. Confira os papéis e as pontas antes de confiar nas letras da saída.



## O produto ideal não é automaticamente um RNA maduro

O mapeamento do laboratório conserva todas as bases do trecho indicado. Não executa splicing, adição de cap, poliadenilação, clivagem, edição ou modificação de bases. Em diferentes contextos celulares, transcritos podem passar por processamentos antes de atuar. A relação com a fita não molde é sobre o mesmo trecho copiado no modelo, não uma identidade universal entre DNA genômico e mRNA maduro. Processamento continua em lacuna no percurso.



## A existência de uma sequência não determina sua expressão

Onde iniciar, em qual fita e quando transcrever dependem de sinais, proteínas e contexto. Os mecanismos de iniciação e regulação diferem entre bactérias e eucariotos. Esta unidade não reconhece promotores, terminadores, cromatina acessível ou fatores de transcrição, nem calcula taxas e abundâncias. O usuário fornece essas anotações do problema; obter uma string de RNA não prova expressão biológica.



## Compare com a replicação sem trocar os mecanismos

Na replicação ideal anterior, cada dupla-hélice filha contém uma fita parental e uma nova fita de DNA. Aqui o DNA atua como molde para RNA; a transcrição não divide o duplex em duas moléculas-filhas de DNA. Uma pequena região é aberta e as fitas de DNA voltam a se associar atrás da polimerase. Não aplicamos os papéis de fita contínua/descontínua ou fragmentos de Okazaki ao RNA desta unidade.



## O teste confere representação e orientação

O laboratório reaproveita os contratos de DNA da unidade de replicação. Testes independentes constroem o RNA base a base, verificam todos os trechos do exemplo e invertem a referência do desenho para conferir a mesma molécula reescrita. Erros, ambiguidades, estrutura secundária, processamento e cinética não são simulados. A enumeração de sequências curtas verifica o código, não valida uma predição biológica.



## Um primeiro recorte de expressão gênica

O grupo II.4 do programa passa a ter uma aula inicial de transcrição e orientação. Regulação transcricional geral, processamento, código genético, tradução e regulação pós-transcricional continuam por desenvolver. O material é um rascunho para revisão de Jhuann, sem comprovar experiência de bancada, estudo concluído ou resultado da IC.



## Exemplo resolvido

Para o duplex com superior 5′-ACGTAACC-3′ e inferior 3′-TGCATTGG-5′, qual o RNA 5′→3′ se a inferior é molde?

1. A fita inferior está escrita 3′→5′ da esquerda para a direita.
2. Pareie T,G,C,A,T,T,G,G com A,C,G,U,A,A,C,C.
3. RNA 5′-ACGUAACC-3′; compare com a superior, agora com U no lugar de T.
4. O molde inferior reescrito 5′→3′ é GGTTACGT; essa é a entrada da função de exemplo.
5. Trecho, fita e ausência de processamento são hipóteses fornecidas, não uma predição de expressão.

## Exercícios e resoluções

1. A adição que alonga o RNA ocorre em qual extremidade da cadeia?

   Resolução: O RNA cresce na extremidade 3′, resultando em síntese 5′→3′.

2. Em qual sentido a fita molde é lida para produzir RNA 5′→3′?

   Resolução: Molde e RNA são antiparalelos.

3. No exemplo com molde inferior e RNA ACGUAACC, quantos nucleotídeos tem o produto ideal?

   Resolução: Há oito letras no trecho copiado.

4. Quantas bases U há no RNA ACGUAACC?

   Resolução: Existe uma U, na quarta posição.

5. No intervalo [2,6), quantas bases são incluídas?

   Resolução: 6−2=4; o limite final não é incluído.

6. Se o DNA MOLDE é fornecido 5′-ATGC-3′, qual RNA 5′→3′ corresponde?

   Resolução: Leia o molde da direita para a esquerda: C,G,T,A → G,C,A,U.

7. Se a fita NÃO MOLDE é 5′-ATGC-3′ no trecho idealizado, qual RNA 5′→3′ corresponde?

   Resolução: Compare na mesma orientação: a fita não molde coincide com o RNA exceto T/U.

8. O laboratório reconhece um promotor real só por receber uma sequência de oito bases?

   Resolução: Trecho e fita são fornecidos; nenhum reconhecimento de sinais foi implementado.

9. O RNA maduro precisa ser idêntico ao trecho genômico não molde, apenas com T→U?

   Resolução: Processamento e edição podem mudar a relação com o trecho genômico; não são modelados aqui.

10. Todo RNA celular é necessariamente traduzido em proteína?

   Resolução: Há RNAs com outras funções; o laboratório não determina função.

11. Qual é o produto sintetizado no processo estudado nesta aula?

   Resolução: Transcrição sintetiza RNA usando DNA como molde neste contexto.

12. Com a fita superior 5′→3′ da esquerda para a direita como molde, sua leitura avança para qual lado da página?

   Resolução: O extremo 3′ está à direita; ler 3′→5′ avança para a esquerda.

## Fonte e limites

Alberts e colaboradores, Biologia Molecular da Célula, tradução da sexta edição, Artmed 2017, capítulo 6, pp.302–304 e 306 (PDF338–340 e 342), consulta parcial em 22/10/2026. P.304/PDF340 também inspecionada visualmente para orientação, síntese e distinções com a replicação. A referência oficial inglesa é de 2014; não equiparamos sua paginação à tradução.

[Programa CCM0121 no Júpiter](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121), recuperado pela ferramenta web em 22/10/2026 com rastreamento indicado há quatro semanas. Ativação 01/01/2025; item II.4 inclui transcrição e regulação. A abertura desse grupo é parcial; não prova a versão ministrada nem habilidades experimentais.

Sequência, diagrama, exercícios, representação regional e código próprios. Não foram distribuídos PDF, figura ou questão do livro. O exemplo curto é sintético e serve apenas a pareamento e orientação; não é gene anotado, promotor reconhecido, produto funcional ou protocolo experimental.

## Reprodução

O exemplo da seção Python é autossuficiente e mostra a função sobre uma fita molde fornecida 5′→3′. O laboratório regional é outro arquivo e reutiliza a validação de DNA de labs/replicacao-orientacao/experiment.py. Na raiz do site, execute python3 -m labs.transcricao-orientacao.experiment e python3 -m unittest discover -s labs/transcricao-orientacao -t .

O módulo não funciona como arquivo isolado sem a dependência de replicação. Entradas são DNA canônico maiúsculo não vazio. O intervalo [start,stop) se refere à sequência superior 5′→3′ e deve ser não vazio. A direção retornada é relativa ao eixo do desenho, não mudança da polaridade molecular.

Não há predição de transcrição a partir de sinais, taxa de expressão, reconhecimento de promotores, processamento, tradução ou aplicação experimental. O teste valida representações idealizadas e não funções biológicas.

## Verificação de 22/10/2026

Cinco testes novos aprovados, incluindo 1364 sequências curtas, 36 intervalos nas duas fitas e inversão da referência. Suíte global: 854 testes Python. No navegador, respostas GCAU e AUGC aceitas conforme papel da fita; etapa aberta por teclado e esquema inspecionado em 390 px sem transbordamento horizontal ou erros de console observados. Revisão de Jhuann pendente.
