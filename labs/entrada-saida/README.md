# Entrada, saída e validação

Rascunho original —27/10/2026; revisão pessoal pendente.

## O dado chega como texto

Uma linha de arquivo ou uma resposta de input não se torna número automaticamente. Converta com float ou int, indicando o formato esperado. Em arquivos científicos, registre unidade e separador decimal; substituir vírgulas sem entender o delimitador pode destruir uma tabela.

## Ler caracteres e converter valores são etapas distintas

input devolve texto; o formato visual de um número não altera isso. float("2.5") cria um valor de ponto flutuante, enquanto a string"2.5" é uma sequência de caracteres. O conversor segue a sintaxe do Python: aceita ponto decimal e notação de expoente, mas não interpreta automaticamente vírgula decimal ou unidade escrita no campo. A função do desafio recebe explicitamente uma string; não deve converterTrue em uma medida só porque bool pode ser tratado numericamente em outros contextos.

## Contagem inteira e medição decimal têm contratos diferentes

int("2") produz 2, mas int("2.5") levanta ValueError. Converter primeiro para float e depois para int produziria2, descartando a parte fracionária: isso não comprova que uma contagem foi informada corretamente. Escolha o tipo de acordo com a pergunta. No exemplo de posições, float é apropriado como representação aproximada; ele não preserva exatamente todo decimal ou toda escala.

## Distinguir problemas de formato e de domínio

"dois" não pode ser convertido por float; "nan" e "inf" podem, mas não são finitos. Já−1 é finito e pode ser uma posição válida no eixo escolhido. O mesmo valor negativo seria inadequado para a massa positiva de outro modelo. Não reúna todos esses casos numa regra de “número errado”: identifique formato, finitude e domínio da grandeza. Os erros devem ser tratados na fronteira da entrada, antes do cálculo.

## Campo vazio não é uma medida zero

O texto vazio não fornece uma medição. O texto"0" pode fornecer uma medição válida, e math.isfinite(0.0) é True. Trocar campo ausente por zero muda os dados e pode alterar uma média ou um ajuste. No laboratório, campos ausentes e colunas extras são rejeitados; linhas inteiramente vazias são ignoradas pelo leitor CSV. Essa é uma escolha explícita do contrato, não prova de que toda linha vazia em qualquer arquivo seja irrelevante.

## Ler uma tabela com nomes de colunas

csv.DictReader lê registros e associa campos aos nomes do cabeçalho. No uso padrão, os campos permanecem textos. O exemplo original em memória usa tempo_s,posicao_m, vírgula entre colunas e ponto decimal; ele não acessa arquivos pessoais. Para abrir um arquivo de texto, use with open(caminho, encoding="utf-8", newline=""). O with fecha o recurso ao sair, inclusive diante de exceções. A codificação e o tratamento de quebras de linha devem ser escolhidos conscientemente.

## Delimitador, decimal e aspas não são a mesma coisa

Em 0,"1,5", as aspas tornam1,5 um único campo CSV, mas float("1,5") continua sem aceitar esse formato decimal. Substituir todas as vírgulas por pontos confundiria separadores de colunas com o conteúdo dos campos. Arquivos com ponto e vírgula entre colunas e vírgula decimal podem ter um contrato legítimo diferente; esta aula não adivinha ou converte esses formatos automaticamente. Use o módulo CSV para interpretar registros, em vez de simplesmente separar cada linha por vírgulas.

## O cabeçalho também precisa ser validado

No projeto integrador já disponível, o cabeçalho exato é time_s,position_m, com esses nomes e nessa ordem. É um contrato diferente dos nomes portugueses usados no pequeno exemplo original. O parser não traduz nomes automaticamente. Rejeitar cabeçalho duplicado, ausente ou inesperado impede atribuir silenciosamente um campo à variável errada. Aspas incompletas no próprio cabeçalho também podem causar erro do leitor, por isso o tratamento precisa começar antes de acessá-lo.

## A validação temporal olha relações entre registros

O integrador pede pelo menos duas amostras, tempos não negativos e estritamente crescentes. Duas linhas com o mesmo tempo violam esse contrato, ainda que cada campo isolado seja numérico e finito. Repetições podem fazer sentido em outro desenho experimental; aqui exigiriam uma decisão de modelagem diferente. Posições negativas continuam permitidas. Os nomes dos campos informam as unidades esperadas, mas não provam que o instrumento ou a pessoa realmente usou essas unidades.

## Finitude não resolve todo problema de precisão

O texto"1e309" pode virar infinito no ambiente float e ser rejeitado pela checagem de finitude. O texto"1e-4000" pode arredondar para zero, que é finito. Se os tempos 0 e1e-4000 se tornam ambos0.0, a verificação de crescimento temporal rejeita a tabela por duplicidade. Validar finitude é necessário neste contrato, porém não assegura que a precisão seja adequada ao problema. A análise de escala numérica tem outro recorte próprio.

## Uma falha deve chegar à pessoa sem fabricar resultado

O programa integrador devolve uma mensagem e um status de erro quando a entrada falha, sem imprimir um ajuste parcial como se tivesse sido aceito. O leitor levanta ValueError para erro de contrato; a interface de linha de comando apresenta a mensagem em stderr e retorna status 2. Não devemos capturar toda exceção e continuar com zero ou simplesmente apagar a linha problemática. Outras aplicações podem reunir vários erros para correção, mas precisam declarar essa política. O diagrama mostra apenas uma rejeição original e sintética.

## Assert ajuda a conferir código, não substitui validar entrada

O pequeno exemplo original usa assert para conferir sua tabela fixa, criada no próprio código. Asserções podem ser desativadas ao executar Python com otimização; por isso não devem ser a única barreira para entradas externas. O laboratório usa if e exceções explícitas para aplicar o contrato. Mantenha os asserts como conferências de desenvolvimento e testes, sem confundi-los com o comportamento obrigatório da interface.

## Apresentar um resultado não muda seu significado

A média das posições 1,3,5 é 3 m. Isso não é uma velocidade: faltaria relacionar variações de posição e de tempo segundo um modelo apropriado. Formatar3.0 como"3.00" escolhe uma apresentação; não cria duas casas de precisão experimental. No integrador, stdout recebe o relatório e stderr as mensagens de falha. O JSON preserva unidades e origem declarada; hashes identificam bytes, sem atestar que os dados sejam verdadeiros ou que um modelo físico esteja validado.

## Use o leitor existente como próximo degrau

O arquivo analyze.py do laboratório de medições já separa parse_csv, validação e ajuste. Esta aula se concentra na fronteira de entrada e não exige estudar o ajuste inteiro. A correção preparada neste bloco inclui o cabeçalho no tratamento de csv.Error e exige que a API receba texto. O pacote para baixar é reconstruído a partir das mesmas fontes testadas. Não são importados arquivos de usuários ou dados privados para a página.

## Uma revisão de vinte minutos com casos concretos

Antes de consultar soluções, classifique: campo vazio, zero, posição negativa, nan, coluna extra e tempo repetido. Depois leia o exemplo de três posições e explique por que sua média é uma posição. Em outra sessão, execute o leitor do integrador com os arquivos sintéticos e confira a mensagem para um cabeçalho com aspas incompletas. Registre sua própria execução antes de apresentar isso como competência demonstrada. Grandes arquivos, contratos de outras fontes e interfaces gráficas ainda precisam de desenvolvimento.

## Exercícios e resoluções

Qual é a média de posições 1,3,5?

**Resolução:** (1+3+5)/3=3.

Uma string "nan" convertida para float é:

**Resolução:** A conversão pode ocorrer, mas isfinite identifica que o valor não é finito.

Quanto vale float("1.5")?

**Resolução:** O texto é convertido no número1.5.

Qual é a média das posições−1,0,1, em metros?

**Resolução:** (−1+0+1)/3=0 m; posições negativas são válidas no exemplo.

No contrato do integrador, qual é o número mínimo de medições?

**Resolução:** São necessárias pelo menos duas amostras.

Que status a interface do integrador devolve quando rejeita uma entrada?

**Resolução:** A convenção da interface deste programa é retornar2 em erro.

Uma chamada input retorna, antes de uma conversão:

**Resolução:** A entrada chega como string.

O que acontece com int("2.5")?

**Resolução:** int não aceita esse texto decimal fracionário.

Campo vazio e texto"0" representam a mesma entrada?

**Resolução:** Ausência de valor não é uma medição zero.

Aspas CSV ao redor de"1,5" fazem float interpretar uma vírgula decimal?

**Resolução:** As aspas organizam o campo CSV; não mudam a sintaxe numérica de float.

O leitor do integrador traduz tempo_s,posicao_m para time_s,position_m automaticamente?

**Resolução:** Ele exige o cabeçalho inglês explícito.

Assert deve ser a única validação de uma entrada externa?

**Resolução:** Asserções podem ser desativadas; use condições e erros explícitos na fronteira.

## Fontes e edições

Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, copyright2017 conforme inventário; nome do arquivo e programa2016. §1.5, pp.126–127/PDF147–148, consulta textual parcial em27/10; p.127/PDF148 visualmente inspecionada. São conceitos de entrada/saída e conversão em Java; não atribuímos aos autores o parser CSV em Python. Sem leitura integral ou distribuição do PDF.

Documentação oficial Python3.14: [csv e DictReader](https://docs.python.org/3.14/library/csv.html), [math.isfinite](https://docs.python.org/3.14/library/math.html#math.isfinite), consultas parciais em27/10. O endereço genérico /3 redirecionou para3.15; a leitura técnica foi fixada em3.14. Página documentação3.14.10 e execução local3.14.5 não são o mesmo patch. O comportamento utilizado foi conferido no ambiente local. Exemplos, contratos, figura e código próprios.

## Continuidade com o projeto existente

Usamos `labs/medicoes/analyze.py`, evitando outro parser paralelo. Cabeçalho do integrador é time_s,position_m; cabeçalho português do pequeno exemplo não é aceito automaticamente. Campo zero e posição negativa são aceitos; tempo negativo, não finitos, menos de duas amostras e tempos não crescentes são rejeitados. Após o cabeçalho, linhas de dados inteiramente vazias são ignoradas pelo DictReader. Relatos de erro numeram a linha física final do registro, que pode ocupar mais de uma linha. A conversão segue a sintaxe de float, não valida perda de precisão ou unidades experimentais.

Correção neste bloco: a leitura de fieldnames foi incluída no try que converte csv.Error em ValueError; a API exige texto. Cabeçalho com aspas incompletas agora chega à CLI como mensagem/status2, sem traceback ou resultado parcial. O cálculo de ajuste não foi alterado. O desafio ler_medida agora rejeita tipos não string.

Executar: `python3 -m unittest discover -s labs/medicoes -t .`. O exemplo em memória da aula é preservado e pode rodar separado. Sete testes do laboratório incluem os quatro anteriores e três novos: cabeçalho/API/CLI; ida e volta pelo csv.writer com LF/CRLF e aspas; vazio/zero, não finitos, precisão temporal e contratos incompatíveis. O ZIP é reconstruído e o relatório sintético de exemplo atualizado com os hashes atuais.

Próxima revisão20min: classificar casos de erro e explicar a diferença entre média de posições e velocidade. Próxima elaboração: usar os contratos para construir um programa próprio, sem declarar que execução ou domínio pessoal já ocorreram.

Complementos oficiais também consultados: [input/float/int](https://docs.python.org/3.14/library/functions.html) e [assert](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement), trechos parciais. O teste de pacote extraiu o ZIP em pasta temporária, conferiu igualdade de todos os arquivos com as fontes e executou os sete testes do laboratório extraído.
