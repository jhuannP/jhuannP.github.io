# Lógica booleana e transporte

27/10/2026. Notas originais assistidas por IA, em rascunho para revisão pessoal. A trilha Computação2 mantém seu estado de percurso complementar; o material não é evidência de aprovação ou competência demonstrada de Jhuann.

Bits são inteiros0/1 no contrato do laboratório. AND,OR inclusivo,NOT eXOR são funções distintas. XOR de três bits é paridade ímpar, não “exatamente um”. Quatro linhas provam a equivalência de funções de duas entradas nesse domínio completo; algumas amostras não bastam.

Meio somador: S=A XOR B,C=A AND B,A+B=S+2C. Retorno(S,C) não é a ordem da palavra bináriaCS. Somador completo: dois meios somadores, transporte finalOR dos transportes parciais; A+B+C_in=S+2C_out. A entrada111 produz resultado3,saídasS1/C1. Modelo ripple sem sinal usa bits menos significativos primeiro e preserva transporte final.

O exemplo original foi preservado, com correção da validação: pertencer a(0,1) aceita1.0,que não suporta^ inteiro. Agora exige int exato0/1, rejeitando bool/float. O operador~ não é NOT restrito a um bit em Python;~0=−1. O painel existente continua só meio somador,sem C_in ou relógio; não foi modificado.

## Fontes e alcance

Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach,©2017: §7.1 pp.987–988/PDF1008–1009,operações e tabelas;§7.3 pp.1028–1029/PDF1049–1050,soma por posições e transporte. Consulta textual parcial em27/10/2026,sem nova inspeção visual ou leitura integral. OCR e ordem de legendas de diagramas têm imperfeições; nenhuma conexão foi transferida automaticamente deles. Exemplos,figura e código próprios,não transcrições. A tentativa de abrir Princeton71logic não foi acessível e não serve como leitura confirmada. Júpiter não reaberto; estado complementar da trilha preservado.

## Laboratório

Execute `python3 labs/booleano-somador/logic.py`. Quatro testes:quatro linhas do meio somador/XOR/DeMorgan; oito linhas do somador completo comparadas a total%2/total//2;512 combinações de dois inteiros de4 bits e transporte inicial;contratos. Caso vazio é declarado: somar duas listas vazias devolve apenas transporte inicial. A referência aritmética não usa as portas para calcular a soma esperada.

A propriedade geral por encadeamento decorre do invariante: após k posições, soma dos k bits de saída mais2^k vezes o transporte equivale à soma dos k bits inferiores das duas entradas com o transporte inicial. A identidade local preserva essa igualdade ao adicionar a posição seguinte. Ao final, o transporte extra mantém o resultado inteiro; removê-lo conserva apenas módulo2^n. Os testes de4 bits conferem esse caso finito, sem provar atributos físicos.

Próxima ação de20min: reconstruir quatro linhas,compor111 e explicar peso/ordem de saídas. Atraso,ruído,glitches,clock,registradores e overflow com sinal permanecem pendentes. Não houve montagem de hardware ou benchmark. Revisão pessoal pendente.
