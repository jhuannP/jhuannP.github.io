# Linguagens: definir um conjunto e reconhecer uma palavra

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão pessoal de Jhuann.

## Do símbolo à palavra

Fixe o alfabeto Σ={a,b}. Uma palavra é uma sequência finita de símbolos desse alfabeto; sua ordem importa: ab e ba são diferentes. O comprimento |w| conta quantos símbolos há em w. A palavra vazia, escrita ε na notação matemática, tem comprimento zero. No código Python, ela é a string vazia "", não a string contendo o caractere grego ε.

|ab|=2; |ε|=0

## Um conjunto pode conter a palavra vazia

Σ* reúne todas as palavras finitas sobre o alfabeto, incluindo ε. Uma linguagem L é qualquer subconjunto de Σ*. O conjunto vazio ∅ não contém palavra alguma; o conjunto {ε} contém exatamente uma palavra. Nenhum deles é igual a Σ*. Uma linguagem pode ser infinita mesmo quando há apenas dois símbolos disponíveis.

∅ ≠ {ε}

## Concatenar preserva a ordem

Concatenar u e v significa colocar os símbolos de v depois dos de u. Para u=aa e v=bb, uv=aabb, enquanto vu=bbaa. A palavra vazia funciona como identidade: anexá-la não muda a sequência. A operação é associativa, mas geralmente não comutativa. Escrever aᵐ significa concatenar m cópias de a; para m=0, o resultado é ε.

uε=εu=u

## Uma regra precisa dizer exatamente o que aceita

A linguagem deste exemplo contém aᵐbⁿ para todos os inteiros m,n≥0. Portanto todos os a vêm antes de todos os b, permitindo que uma das partes seja vazia. Ela aceita ε, aaa, bb e aabb; rejeita aba e ba. A descrição a*b* usa duas repetições independentes. Não exige quantidades iguais de a e b.

L={aᵐbⁿ : m,n≥0}

## O alcance da repetição muda o conjunto

O símbolo * permite zero ou mais repetições da expressão imediatamente anterior. Em a*b*, cada letra repete por conta própria. Em (ab)*, o bloco ab inteiro é repetido. A palavra aabb pertence à primeira linguagem e não à segunda; abab pertence à segunda e não à primeira. A palavra ab pertence às duas, assim como ε. Uma palavra compartilhada não prova igualdade de linguagens.

a*b* ≠ (ab)*

## Especificar e reconhecer são tarefas distintas

A regra matemática especifica o conjunto inteiro. Um reconhecedor recebe uma palavra finita e responde se ela pertence ao conjunto. Para esta regra, basta lembrar se já entramos na parte dos b e se depois dela apareceu um a. Encontrar um trecho aceito dentro da entrada responde a outra pergunta: mesmo ba contém trechos aceitos, mas não pertence a L. No exemplo Python, re.fullmatch confere a string completa; re.search pode aceitar um trecho vazio e não serve como substituto.

Reconhecer: dada w, decidir se w∈L

## Três estados resumem o prefixo lido

Use A para o prefixo composto somente de a, incluindo ε. Use B quando o prefixo ainda está na ordem permitida e já contém pelo menos um b. Use X para um prefixo que já apresentou algum a depois de um b. O estado inicial é A; A e B aceitam quando a entrada acaba. Em A: ler a mantém A e ler b vai para B. Em B: b mantém B e a vai para X. Em X, a e b mantêm X. Essas seis transições definem uma máquina determinística completa sobre {a,b}.

A: a→A, b→B; B: a→X, b→B; X: a,b→X

## Rastro resolvido: o erro fica no prefixo

Para aabb, o rastro é A,A,A,B,B: a palavra termina em B e é aceita. Para aba, o rastro é A,A,B,X: o último a surge depois de um b e provoca rejeição. Não basta inspecionar apenas a última letra; a memória do prefixo está no estado. Uma continuação como abaaa permanece em X porque acrescentar símbolos não remove a violação que já ocorreu.

aba: A → A → B → X

## Por que o reconhecedor funciona para qualquer comprimento?

O invariante classifica o prefixo exatamente pelas três descrições anteriores. Antes de ler símbolos, ε pertence à classe A. Suponha a classificação correta após k símbolos. De A, a mantém um prefixo só de a e b inaugura a parte B; de B, b conserva a ordem e a cria a violação X; de X, qualquer continuação conserva a violação. Isso cobre todos os casos e prova o passo de indução. Ao final, A ou B equivale precisamente a pertencer a a*b*. Testes finitos ajudam a achar erros no código, mas é esse argumento que cobre comprimentos não testados.

## Contar palavras aceitas de um comprimento fixo

Para comprimento k, uma palavra aceita tem a forma aʲbᵏ⁻ʲ, com j de zero a k. Cada valor de j dá uma palavra distinta, e toda palavra aceita aparece assim. Portanto há k+1 palavras aceitas de comprimento k, entre 2ᵏ palavras binárias possíveis. Para k=3, elas são bbb, abb, aab e aaa: quatro entre oito. A linguagem completa continua infinita, pois k não tem um limite fixo na definição. Contar palavras não fornece uma probabilidade sem declarar uma distribuição sobre elas.

Quantidade aceita no comprimento k: k+1

## Por que três estados são necessários neste modelo?

Considere os prefixos ε, b e ba, que alcançam A, B e X. A continuação a distingue os dois primeiros: a é aceita e ba é rejeitada. A continuação vazia distingue cada um deles de ba, pois ε e b são aceitos e ba é rejeitado. Se dois desses prefixos terminassem no mesmo estado de uma máquina determinística, toda continuação produziria a mesma decisão, contrariando os exemplos. Logo qualquer autômato determinístico completo que reconheça esta linguagem precisa de pelo menos três estados; a construção usa exatamente três. A afirmação é sobre esse modelo, não sobre o número de variáveis de qualquer programa.

## Contrato do código e próximos limites

O reconhecedor aceita strings e rejeita símbolos fora de {a,b}. O rastro exige uma palavra do alfabeto e sinaliza erro para entradas inválidas; isso separa a tabela formal de uma política de validação externa. O reconhecimento usa uma passagem e memória auxiliar constante; guardar todos os estados do rastro usa memória proporcional ao comprimento. Não foi construído um compilador geral de expressões regulares, nem provada aqui a equivalência de todas as linguagens regulares com autômatos. Recursos como retroreferências de bibliotecas de regex também exigem outra análise.

## Exercícios e resoluções

- a*b* aceita a palavra vazia? **Resolução:** As duas repetições podem ter zero ocorrências.
- Qual palavra viola a ordem de a*b*? **Resolução:** aba contém um a depois de um b.
- Qual conjunto contém exatamente uma palavra de comprimento zero? **Resolução:** {ε} contém a palavra vazia; ∅ não contém palavra alguma.
- Para u=aa e v=bb, qual é vu? **Resolução:** vu coloca v antes de u: bb seguido de aa produz bbaa.
- A linguagem a*b* exige o mesmo número de a e b? **Resolução:** As repetições são independentes; abb e aaa também são aceitas.
- Qual palavra pertence a (ab)*, mas não a a*b*? **Resolução:** abab repete o bloco ab, mas volta de b para a e viola a*b*.
- Encontrar um trecho aceito com re.search garante que toda a entrada pertença a a*b*? **Resolução:** A busca pode encontrar até um trecho vazio. O pertencimento da palavra inteira exige verificação completa.
- Em que estado termina o rastro A,A,B,X da entrada aba? **Resolução:** O último a aparece depois de um b; X guarda essa violação.
- Qual argumento cobre palavras de qualquer comprimento neste reconhecedor? **Resolução:** A base e o passo de indução cobrem todo prefixo finito, além dos casos testados.
- Quantas palavras de comprimento três pertencem a a*b*? **Resolução:** bbb, abb, aab e aaa: quatro, conforme k+1=4.
- Quantas palavras de comprimento oito pertencem a a*b*? **Resolução:** Há uma palavra para cada número de a de zero a oito: nove possibilidades.
- Qual é o número mínimo de estados de um autômato determinístico completo para a*b* sobre {a,b}, conforme a prova apresentada? **Resolução:** Os prefixos ε, b e ba são distinguíveis por continuações e exigem três estados.

## Fontes e limites

Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, exemplar do acervo com copyright 2017 (nome do arquivo 2016), §5.1, pp.718–722 e 728–729, PDF739–743 e 749–750. Leitura textual parcial em 22/10/2026: definições, especificação e reconhecimento. A página complementar https://introcs.cs.princeton.edu/java/51language/ retornou 403 e não foi consultada com sucesso neste bloco. Prova por prefixos, máquina, contagens e exercícios locais são originais; não se afirma leitura integral ou domínio pessoal.

## Executar

Na raiz: python3 -m labs.linguagem-ordem.experiment; testes: python3 -m unittest discover -s labs/linguagem-ordem -t .

accepts usa memória auxiliar constante; trace guarda um estado por prefixo e requer memória linear. O código é um reconhecedor específico e não interpreta qualquer expressão regular. A palavra vazia é a string vazia; o caractere ε é um símbolo externo ao alfabeto do programa.


## Linguagens e reconhecedor por prefixos — 22/10/2026

Aula linguagens-formais ampliada de três seções/dois exercícios para 12 seções/12 exercícios, preservando o exemplo resolvido, o código inicial e o desafio. Definições de símbolo, palavra, linguagem e concatenação; distinção entre ∅ e {ε}, a*b* e (ab)*, busca de trecho e pertencimento da entrada inteira. Reconhecedor completo de três estados com invariante por prefixo, contagem k+1 por comprimento e argumento de necessidade dos três estados por continuações distinguíveis. Os argumentos matemáticos são próprios e não dependem de um teste finito para cobrir todos os comprimentos.

Fonte primária local: Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, exemplar com copyright 2017 e nome de arquivo 2016. §5.1, pp.718–722 e 728–729 (PDF739–743 e 749–750), consulta textual parcial em 22/10/2026. Definições, especificação e reconhecimento conferidos. A página https://introcs.cs.princeton.edu/java/51language/ retornou 403 neste bloco; não foi consultada com sucesso. Não há reprodução de páginas ou programas do livro. A máquina e a prova deste exemplo são próprias; não foi demonstrada a equivalência geral entre regex e autômatos nem implementado um compilador geral.

Laboratório: labs/linguagem-ordem/, com reconhecedor, rastro, notas, tabela vetorial original e cinco testes. Conferência exaustiva de palavras binárias até comprimento dez contra propriedade por pares de posições e fullmatch; invariante de todos os prefixos até comprimento oito; palavras aceitas até comprimento 12 contra construção por ponto de separação; alcance dos estados e sufixos distinguíveis; validação de entradas e símbolo ε fora do alfabeto. Cinco testes novos e doze testes de catálogo aprovados. 531 estruturas MathML conferidas antes da adição da figura, sem alteração posterior de fórmulas MathML; catálogo revalidado após a figura. Suíte global não repetida, nenhum modelo JavaScript alterado.

Navegador: tabela e texto legíveis a 390 px, largura da página igual à tela. Exercício sobre {ε} e resposta nove para comprimento oito aceitos; nenhum erro de console observado. Prévia: linguagens-ordem-mobile.jpg. Tudo permanece em rascunho para revisão de Jhuann. Computação II agora tem 20 aulas/70 exercícios, três recortes desenvolvidos e 17 introduções curtas. É percurso complementar próprio, sem equivalência automática com a disciplina cursada CCM0128. Catálogo: 500 aulas/2982 exercícios.

Próxima revisão pessoal: traçar aabb e aba, explicar o invariante e justificar k+1 palavras de comprimento k. Próxima preparação global: aprofundar um tópico de Física Matemática, preservando a alternância entre percursos. Saldo semanal depois do bloco: 93%; parada operacional em 65%.
