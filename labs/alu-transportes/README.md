# ALU: transporte, seleção e duas leituras

Rascunho original preparado com IA, revisão de Jhuann pendente. Percurso complementar de arquitetura; não aprovação em disciplina ou competência demonstrada.

## Contrato

Duas palavras `int` 0..15, sem bool, e operação ADD/AND/OR/XOR. Quatro bits, ADD sem carry de entrada. Retorna resultado sem sinal R, zero Z e flags C/V. Em ADD, C é carry final; V é XOR dos carries de entrada e saída do bit de sinal. Nas operações lógicas C=V=0. O vetor `carries` sempre descreve o candidato ADD interno, em ordem c0..c4, e não flags adicionais publicados. Sem clock, estado, SUB, saturação ou validação de hardware. Nenhuma unidade física é atribuída aos bits.

O laço usa soma completa por XOR/maioria, sem usar a soma inteira como implementação da ADD. O teste usa soma inteira modular e faixa assinada −8..7 como referência independente. Para os lógicos, tabelas booleanas literais independentes. O invariante de cada prefixo usa os operandos truncados, não os operandos inteiros quando i<4.

## Reconstruir

Da raiz do protótipo:

    python3 -B labs/alu-transportes/alu.py
    python3 -B -m unittest discover -s labs/alu-transportes -t .

Preveja as quatro somas da figura. Confira c0..c4=(0,1,1,1,0) para 7+1. Explique por que 15+1 não tem overflow assinado, mas 8+8 tem carry e overflow. Compare XOR/AND/OR de 10 e 6; se o resultado da operação é zero, Z=1.

Cinco métodos de teste percorrem 1024 combinações de operação/palavras, 256 pares em cinco prefixos, quatro marcos explícitos, decodificação assinada e contratos. Cobertura exaustiva da função finita não comprova atraso, consumo, fiação, arquitetura comercial ou ausência de falha eletrônica. Entradas prescritas e diagrama próprio; não medição experimental.

## Fonte e diferenças

Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar copyright 2017 (arquivo nomeado 2016), §7.3 pp.1028–1032, PDF1049–1053, consulta textual parcial em 29/10/2026. A fonte discute ripple carry, blocos lógicos e multiplexação; seleciona operações com linhas de controle próprias e não fornece este contrato de flags. Nosso OR, seleção binária possível e flags são extensões didáticas, sem alegar reproduzir TOY-8. Diagramas e legendas OCR não usados como fiação automática; nenhuma figura ou exercício transcrito. Página pública de referência: https://introcs.cs.princeton.edu/java/home/ (referência bibliográfica; corpo não consultado neste bloco).

O snippet/painel original da aula continuam preservados. Este laboratório separado permite traçar a composição. Aprovação de testes não substitui revisão conceitual/pessoal.
