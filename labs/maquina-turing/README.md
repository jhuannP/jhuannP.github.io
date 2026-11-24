# Máquina de Turing — traço, parada e orçamento

## Estados finitos e fita sem limite fixado são objetos diferentes

Uma máquina determinística tem um conjunto finito de estados de controle e uma tabela finita de regras. A fita oferece células indexadas por inteiros, sem um maior índice fixado de antemão; a cabeça lê uma célula por vez. Num número finito de passos, apenas uma região finita pode ser visitada. Isso é um modelo abstrato: um computador que simula a fita tem memória e tempo finitos. A fita não fica inteiramente codificada em um único estado de controle.

## Uma configuração precisa registrar onde e como a máquina está

Usaremos configuração (q,h,T): estado q, posição inteira da cabeça h e conteúdo T da fita. O branco é escrito como _. Só guardamos células não brancas num dicionário; uma posição ausente é lida como branco. Duas configurações com o mesmo estado podem produzir futuros diferentes se a cabeça ou a fita diferirem. O contador de passos e o histórico são instrumentos do simulador, adicionais à configuração lógica.

Configuração=(estado,cabeça,fita)

## Declare a convenção da transição antes de traçar

Nesta aula δ(q,a)=(q′,b,D): ler a na cabeça, escrever b nessa célula, mover D posições e passar a q′. D pode ser −1,0 ou1: esquerda, imóvel ou direita. Depois verificamos se q′ é final. Assim uma transição que termina também pode mover a cabeça. A referência do Sedgewick associa movimento ao novo estado e não move ao entrar em estado final; usamos uma variante explícita, não copiamos silenciosamente o traço dela.

δ(q,a)=(q′,b,D)

## Uma regra pode escrever e recuar para uma célula nova

Se a cabeça está em 0 sobre 1 e δ(buscar,1)=(voltar,0,−1), a próxima configuração tem 0 na célula 0, cabeça em−1 e estado voltar. A célula −1 é branca se nunca recebeu escrita. A leitura e a escrita se referem à posição anterior ao movimento. Escrever branco remove a entrada do dicionário, mas não remove a célula do modelo; ela continua existindo como branca.

## Incrementar unário exige especificar a entrada admitida

Represente n≥0 por n símbolos 1 consecutivos nas posições 0 até n−1; as outras posições são brancas e a cabeça começa em 0. n=0 é a entrada vazia. As regras são δ(buscar,1)=(buscar,1,+1) e δ(buscar,_)=(aceita,1,+1). O primeiro caso conserva o símbolo e avança; o segundo acrescenta um1 e termina. O estado chamado aceita indica término bem-sucedido desta transformação, não uma prova de qualquer linguagem arbitrária.

1ⁿ → 1ⁿ⁺¹

## O traço de 111 inclui a escrita final

Partimos de buscar, cabeça 0, fita 111. Após três transições de leitura, a cabeça está em 3, sobre branco, e a fita ainda contém 111. A quarta escreve 1 na posição 3, move a cabeça para 4 e entra em aceita. A saída é 1111, mas a cabeça final está na primeira célula branca à direita da saída. Contamos transições efetivamente executadas, não apenas deslocamentos sobre a entrada nem linhas do histórico.

## Um invariante justifica o resultado para qualquer n admitido

Antes de k transições, para 0≤k≤n, o estado é buscar, a cabeça está em k e as n células iniciais ainda guardam1. Se k<n, a regra sobre 1 conserva esse fato e avança para k+1. Em k=n, a leitura é branco e a transição final escreve o novo 1. Portanto a saída tem n+1 símbolos e a execução usa n+1 transições, inclusive quando n=0. A prova por esse invariante e pela travessia finita vale para o domínio declarado; testar alguns n não a substitui.

T(n)=n+1 transições

## O tamanho da representação faz parte do custo

Em unário, a entrada que representa n tem comprimento n. Dizer que o incremento usa n+1 transições é linear no tamanho dessa entrada; não significa custo logarítmico em n. Uma representação binária seria outro protocolo. Além disso, o interpretador Python armazena cópias da fita no histórico: seu tempo e sua memória podem ser maiores do que simplesmente contar transições do modelo. Não medimos desempenho de hardware com esse contador.

## Aceitar e rejeitar podem reconhecer uma propriedade

Um segundo programa lê uma palavra binária e guarda no controle a paridade do número de 1 já vistos. Começa no estado par; ler 0 conserva o estado, ler 1 alterna par/impar. Ao ler o branco final, par vai para aceita e impar para rejeita. O invariante é a paridade do prefixo já percorrido. Por exemplo,101 tem dois 1 e é aceita;111 tem três e é rejeitada. A palavra vazia tem zero 1 e é aceita. Comprimento par e quantidade par de1 são propriedades diferentes.

## Um limite de simulação não é um estado de rejeição

Para entrada unária 111, orçamento de três transições termina antes da escrita: o simulador retorna limite, com buscar e cabeça3. Com orçamento quatro, a mesma máquina aceita. Outro programa que sempre avança sobre brancos sem mudar para estado final também atinge limite. Só esse resultado finito não distingue os casos. Para esse programa específico sobre fita vazia podemos provar por indução que o estado nunca é final; isso não fornece um decisor para todas as tabelas e entradas.

## Uma tabela incompleta também não é rejeição automática

O interpretador retorna sem_regra quando não existe uma transição para o par estado/símbolo e ainda há orçamento. Reservamos rejeita para entrada explícita no estado final de rejeição. Essa é uma escolha da API; outras definições podem tratar transição ausente de outra maneira. Ao atingir exatamente o orçamento, checamos primeiro se a última transição entrou em estado final. Se não entrou, limite não promete que a próxima regra existe nem que a execução futura para.

## Uma simulação finita não prova universalidade

O programa baixável interpreta tabelas determinísticas de um formato declarado, permite ler/escrever e mover nos dois sentidos, e registra um traço finito. Não apresenta uma construção demonstrada de máquina universal nem uma decisão geral sobre parada. A distinção entre reconhecer e decidir uma linguagem também exige analisar término em todas as entradas do domínio. Nosso reconhecedor de paridade termina em m+1 transições para toda palavra binária de comprimento m; isso decorre da travessia até o primeiro branco.

## O laboratório ajuda a revisar regras e contratos

run recebe tabela, fita, configuração inicial e orçamento inteiro não negativo, e devolve estado, cabeça, células não brancas, passos e histórico. Não executa comandos presentes nos símbolos. As tabelas e a entrada são preservadas; movimentos e símbolos inválidos são recusados. Os testes conferem incremento, paridade, escrita, recuo, branco, orçamento e estados finais. Programas universais, provas gerais de computabilidade e ligação completa com arquitetura permanecem pendentes. Percurso complementar próprio, separado de CCM0128 e sem certificação de domínio pessoal.

## Exercícios originais e resoluções

Quantos passos a regra usa para uma entrada com quatro 1? **Resolução:** Quatro passos para atravessar os 1 e um para escrever no branco.

A fita do modelo teórico tem um tamanho máximo fixo como a memória M8? **Resolução:** A definição teórica não fixa um limite a priori para as posições usadas.

No incremento de 111, onde está a cabeça após três transições, antes de escrever o novo 1? **Resolução:** A cabeça atravessa as posições 0,1,2 e chega à posição 3, branca.

Após as quatro transições do incremento de 111, qual a posição final da cabeça nesta convenção? **Resolução:** A quarta escreve na posição 3 e move para 4 antes de conferir o estado final.

Quantas transições incrementam a entrada unária vazia? **Resolução:** A primeira leitura já é branca: escreve 1, move e aceita em uma transição.

Quantos símbolos 1 há na saída do incremento unário da entrada11? **Resolução:** A entrada representa2 e a saída111 representa3.

Cabeça em 0, símbolo 1 e regra (voltar,0,−1): qual a nova posição da cabeça? **Resolução:** A escrita ocorre em 0 e o movimento−1 leva à célula −1.

Quantas transições o programa de paridade usa para a palavra 101, incluindo a leitura do branco final? **Resolução:** Três leituras da palavra e uma do branco:4.

O programa de paridade aceita ou rejeita101? **Resolução:** A palavra tem dois símbolos 1, quantidade par.

Incrementar111 com orçamento de três transições produz qual status? **Resolução:** A cabeça chega ao branco, mas falta executar a quarta transição.

Tabela vazia, estado buscar, fita vazia e orçamento positivo: qual status definido nesta API? **Resolução:** Não existe instrução para buscar/branco; não houve entrada no estado final de rejeição.

Atingir o limite em uma execução prova que a máquina nunca vai parar? **Resolução:** A mesma situação ocorre antes do término de um incremento unário finito.

## Referência e execução

Sedgewick e Wayne — Computer Science: An Interdisciplinary Approach, exemplar autorizado com copyright Pearson2017; nome de arquivo2016 não estabelece o ano editorial.

§5.2, pp.766–768 (PDF787–789), consulta textual parcial em26/10/2026 sobre modelo, configurações operacionais e ausência de limite prévio de fita/passos. A convenção de movimentos foi adaptada e explicitada. Sem leitura integral da seção; tabelas, incremento unário, figura e interpretador originais. Website oficial retornou403; a leitura veio do exemplar local.

Executar: `python3 -m unittest discover -s labs/maquina-turing -t .`. `run(program,tape,state=...,head=0,accept="aceita",reject="rejeita",max_steps=100)` retorna status, configuração, passos e histórico, sem mudar a entrada. Movimento é inteiro−1/0/+1 e símbolos são caracteres únicos; `_` é branco. Regras ausentes não são rejeição implícita. O histórico copia células e tem custo real maior que uma transição abstrata.

Os testes finitos não provam universalidade; o término dos dois programas particulares é justificado no texto. Sem páginas do livro distribuídas, sem execução de código vindo das tabelas, sem máquina física ou resultado de pesquisa reivindicado. Rascunho assistido por IA para revisão pessoal.

O exemplo Python anterior da aula usa o rótulo final parada; o interpretador baixável usa aceita. As duas versões contam a mesma escrita e o movimento finais.
