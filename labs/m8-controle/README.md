# Controle observável da M8

Descrição combinacional original de seletores/habilitações para a M8 já existente. O laboratório importa `m8.py` sem alterá-lo; não implementa outro interpretador ou um circuito físico. Rascunho assistido por IA, revisão pessoal pendente.

Da raiz:

```sh
python3 -B -m labs.m8-controle.control
python3 -B -m unittest discover -s labs/m8-controle -t .
```

`controls(instruction,acc)` recebe palavras int0..255 sem bool; opcode0..8, operando nibble0..15. Usa decode/word existentes. Não lê memória, não avança PC, não valida se existe instrução no endereço e não calcula atraso. Devolve uma descrição nova a cada chamada. Fonte ACC: hold, immediate, memory ou alu; operação add/sub quando pertinente; habilitações0/1 para ACC, memória, saída e pedido de parada. PC seleciona target ou sequential, com escrita em todo passo comportamental bem-sucedido, inclusive HALT conforme o contrato antigo.

Para JZ o teste é o ACC antigo igual a zero, não uma flag persistente de outra ALU. STA escreve o ACC antigo e não o altera; OUT acrescenta à lista de saída. HALT e OUT ignoram o nibble baixo. LDI zero-estende o nibble, sem sinal. Soma/subtração retornam byte módulo256, sem estado de carry/overflow na M8. A ALU de quatro bits de outra aula tem contrato diferente e não foi ligada aqui como se tivesse oito bits.

Referência: ADD14,ACC250,M[14]10 → ACC4, memória intacta; o exemplo CLI inicia PC0 e vai a1. No extremo PC15 o próximo sequencial é0, mas run não prossegue depois de HALT. Uma palavra fora do programa continua erro do motor, não uma conclusão do decodificador.

Cinco testes: referência;3024 transições comparando a interpretação das seleções com o motor antigo;256 condições de JZ e wrap em HALT;pureza e nibble ignorado;exemplos/desafio anteriores e contratos. O teste não demonstra equivalência de todo circuito fabricável ou de todas as memórias possíveis. Não simula fetch em vários pulsos, setup/hold, clock ou HDL.

Fonte: Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, copyright2017, §7.5 pp1070–1072/PDF1091–1093 e pp1081–1082/PDF1102–1103, texto parcialmente consultado em30/10/2026. p1081 contém diagrama; OCR não foi usado para reconstruir fiação. TOY-8 tem outro conjunto/formato e sequência de pulsos. A tabela e o recorte M8 são próprios, sem copiar programa ou figura do livro. Website do livro: https://introcs.cs.princeton.edu/java/home/ . Nenhum PDF privado distribuído.
