# M8: campos e significado da palavra

Material original assistido por IA, revisão pessoal pendente. Complemento de teoria/arquitetura,distinto da disciplinaCCM0128. A ISA e os interpretadores existentes não foram alterados.

Fonte local do contrato:`m8.py` e `computer-models.js` na raiz,com testes prévios `test_m8.py`. Palavras8 bits,programa1…16 posições,dados16 bytes,PC4 bits,ACC8 bits,nove opcodes. Decoder preserva operando até quando a operação o ignora. Alguns bytes representam opcodes indefinidos. Endereço codificável não garante palavra carregada.

`word_contract.inspect` importa decode/encode daM8 existente. Retorna campos binários,hexadecimal,operação,operando e seu papel,além de uma palavra canônica que zera campos ignorados emHALT/OUT. Não executa instrução,altera programa,dados,ISA,simulador ou API.144 palavras reconhecidas/112 indefinidas;114 formas canônicas para apresentação,não equivalência entre todos os estados completos:IR e traçado guardam a palavraoriginal.

Exemplos originais:0x3E=62dec,opcodeSTA,operando14;ACC203 escreve dados14 sem mudar programa. Com dados3=203,LDI3→3 eLDA3→203. Operando16 não cabe;unir campos sem validar pode transformarADD16 emSUB0. PC15 passa a0 num programa completo;programa curto não reduz PC pelo seu comprimento. HALT em0 deixa PC1 porémencerra,sem nova busca. Um passoé uma instrução comportamental,sem temporização elétrica.

## Executar da raiz
```sh
python3 -m labs.m8-palavra.word_contract
python3 -B -m unittest discover -s labs/m8-palavra -t .
python3 -B -m unittest test_m8.MachineSpecification
```
Seis métodos novos:todos256 bytes comparados com divisão posicional(divmod) e reconstrução por pesos;160 casos de campos ignorados (2 operações×5 acumuladores×16 operandos),efeito igual/IR distinto;32 cargas imediato/endereço e rejeição de operando fora do campo;48 escritas preservando programa/outras posições e entrada do chamador;PC/saltos/endereços não carregados/HALT;contratos. As seis verificações existentes deMachineSpecification também aprovadas,incluindo concordância de traçadosPython/JavaScript. Não provar equivalência de hardware ou de todo programa.

## Referência consultada parcialmente em29/10/2026
Sedgewick eWayne,ComputerScience:AnInterdisciplinaryApproach,exemplar privado comcopyrightPearson2017/ISBN978-0-13-407642-3 previamente identificado. Cache textual autorizado relido em§6.2pp906–908 e910–911/PDF927–929 e931–932:objetivo da máquina didática,componentes e formatosTOY. Sem nova inspeção visual,leitura integral ou reprodução de figura/tabela/programa. TOY tem palavras16 bits e outra organização;os números e efeitosM8 vêm do código local próprio,não de um transplante da tabelaTOY. Ano2016 no nome do arquivo não certifica publicação. PDF privado não distribuído.

O websitePrinceton não foi reaberto nesta rodada. M8não é ISA comercial,chip físico,emulador deTOY ou resultado pessoal deJhuann. Programação,interpretador e caminho de dados têm aulas próprias ainda introdutórias;um aprofundamento não encerra o percurso.
