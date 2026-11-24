# Programar a M8: guarda antes da saída

29/10/2026. Programa e provas originais para revisão de Jhuann. Usa `m8.py` existente da raiz; não é outro interpretador. Requer o projeto local completo, não funciona como script isolado baixado sem a dependência. Nenhuma alteração da ISA, JavaScript ou painel.

## Programa de sete palavras

| PC | Assembly | Hex |
|---|---|---|
|0|LDA14|2E|
|1|JZ6|76|
|2|OUT|80|
|3|SUB15|5F|
|4|STA14|3E|
|5|JMP0|60|
|6|HALT|00|

Dados14=n, dados15=1,0≤n≤255. InícioPC0/ACC0. Outras posições preservadas. Programa e dados separados: endereço14 não precisa existir como instrução. `LDI20` não cabe, mas M[14]=20 é byte válido e LDA14 o lê.

Pergunta: emitir n,n−1,...,1, sem emitir0, e parar; n0 deve emitir lista vazia. Depois de k passagens completas e antes da próxima LDA14 na posição0, contador n−k e saída n,...,n−k+1, para0≤k≤n. A LDA lê esse contador e JZ testa o ACC atual. Se positivo, emite, subtrai1,guarda e volta. A subtração nunca passa de0 porque só ocorre com contador positivo. O contador natural é variante estritamente decrescente; em0,o salto evita o corpo e alcançaHALT.

São6 instruções por saída, mais LDA/JZ/HALT na verificação final:6n+3. n3 dá21;n0 dá3;n255 dá1533. Essas são instruções do modelo, não ciclos de hardware, tempo físico ou uma família de memória ilimitada. Não inferir complexidade assintótica geral de uma máquina fixa de8 bits.

## Testar depois muda a precondição

O programa CONTAGEM anterior prepara contador3 e decremento1, emite antes de testar. Preservado. Só trocar a carga inicial por0 dá saída0,255,254,...,1, pois0−1 módulo256=255; termina depois de256 saídas e1540 instruções. Isso não é contagem de naturais negativa e não é laço infinito. A entrada zero precisa de tratamento explícito para a especificação nova.

## Alterar o decremento não preserva a prova

Se trocar dados15 por2, contador inicial3 permanece ímpar módulo256 e nunca fica0. Se decremento0, permanece3. O timeout apenas limita observação; a demonstração modular é que estabelece não término desses casos. Contador4 com decremento2,por outro lado,emite4,2 e termina em15 instruções. A prova n−k e custo6n+3 exigem decremento1. Não se alegou repetição do estado inteiro: saída/traço são listas que podem crescer, embora o controle interno seja finito.

## Executar na raiz

`python3 -m labs.m8-contagem.countdown`

`python3 -B -m unittest discover -s labs/m8-contagem -t .`

Sete testes:tradução/cenário;todas256 entradas com invariante,custo e preservação;orçamento/retomada;zero no programa antigo;decrementos0/2;cinco traçados Python/JavaScript com interpretadores existentes;contratos. Testes de exemplos complementam a prova. Dados sintéticos,sem hardware ou aplicação profissional alegados.

## Fontes

Contrato local primário:m8.py e computer-models.js;opcodes e efeitos existentes. Sedgewick/Wayne,Computer Science: An Interdisciplinary Approach,exemplar copyrightPearson2017,§6.2 pp918–919/PDF939–940,consulta textual parcial29/10/2026 de controle por desvios e condição antes do corpo;§6.3 início p930/PDF951,sobre programação/recursos. Sem nova inspeção visual ou leitura integral. TOY é distinta; não copiamos código,programaEuclides,figura ou tabela do livro. Primeira busca retornou recorte de bits p892–893, não usado como fonte de controle. Prova e programa de contagem próprios;PDF privado não distribuído.

Percurso complementar de teoria/arquitetura, distinto da disciplina cursadaCCM0128. Júpiter não reconsultado, pois não se altera o mapa formal dessa disciplina. Painel antigo continua mostrando soma e contagem3,2,1; não oferece entrada n nem novo programa.

Próxima revisão20min:reconstruir sete palavras,traçar n0/n3 e provar6n+3. Contratos de outros programas,interpretador geral,caminho de dados e revisão pessoal pendentes.
