# Memória 4×8: seleção e preservação

Material original preparado com IA, revisão de Jhuann pendente. Percurso complementar de arquitetura, distinto de CCM0128. Não experimento físico ou pesquisa executada.

## Interface

Estado: tupla de quatro bytes `int` 0..255. Endereço `int` 0..3. Dados `int` 0..255. `we` e `event`: int 0/1, sem bool ou float. Todos os argumentos são validados mesmo quando a escrita está desabilitada. Não há acesso a arquivo, rede ou hardware.

`read` usa decodificação exclusiva e seleção bit a bit; não altera estado. `transition` usa habilitação local seleção AND we AND event e seleção entre bit antigo/novo. Retorna nova tupla. O exemplo inicial da aula com lista continua preservado e sua chamada habilitada representa o evento implicitamente. No laboratório cada chamada com event=1 representa um evento discreto separado; não detecta borda nem simula um sinal mantido alto.

Leitura antes da transição consulta S; depois consulta S′. Uma única porta/endereço é usada. Não descreve RAM comercial síncrona, política de leitura durante escrita, múltiplos escritores, cache, latência, setup/hold, metastabilidade ou circuito elétrico. A capacidade de dados é 4×8=32 bits; controle e fiação não entram nessa contagem.

## Roteiro e verificação

Da raiz do protótipo:

    python3 -B labs/memoria-selecao/memory.py
    python3 -B -m unittest discover -s labs/memoria-selecao -t .

Preveja seis eventos a partir de (3,85,170,240). Primeiro não há evento; depois endereço2 recebe9; uma tentativa desabilitada não o muda; endereço1 recebe200; endereço2 recebe13 duas vezes. Snapshots anteriores permanecem tuplas imutáveis. A escrita repetida é habilitada mas não muda bits. Posições não selecionadas preservam cada bit porque sua habilitação local é zero.

Cinco métodos verificam 4096 combinações (4 endereços×256 dados×2 we×2 event) para um estado inicial não uniforme; 1024 leituras sobre 256 estados prescritos; decoder; traçado literal de seis etapas; 16 pares de destinos em duas ordens; contratos. Referência de transição por cópia/indexação independente da implementação por bit. Isso não enumera os 2³² estados possíveis. Prova geral de não interferência na aula; testes finitos de implementação, sem certificação de eletrônica ou pedagogia.

## Fonte

Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar copyright2017 (arquivo nomeado2016), §7.4 p.1054/PDF1075, pp.1056–1057/PDF1077–1078 e síntese p.1062/PDF1083: consulta textual parcial em29/10/2026. Interface, seleção e escrita por pulso; diagramas/legendas OCR não adotados como fiação. A figura, valores e transição por evento são próprios. Página pública bibliográfica: https://introcs.cs.princeton.edu/java/home/ (corpo não consultado neste bloco). Sem transcrição de exercícios ou figura da fonte; sem leitura integral.
