# Certificados, busca e tamanho codificado

27/10/2026. Notas de aula originais com apoio de IA. Aula `complexidade-certificados`, em rascunho; revisão pessoal de Jhuann pendente. Percurso complementar de teoria e arquitetura baseado em *Computer Science*, distinto da disciplina formal CCM0128. Não certifica experiência profissional ou domínio pessoal.

## Fontes e alcance

Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar com copyright 2017, arquivo nomeado como 2016. Consulta parcial em 27/10/2026 ao §5.5: pp.822–827 (PDF843–848) para custo, pior caso, inteiros e subconjuntos; pp.834–837 (PDF855–858) para conferência, busca e classes. Página impressa827/PDF848 renderizada e inspecionada visualmente. A paginação é específica do exemplar; sem leitura integral do capítulo ou distribuição do PDF privado.

O livro usa também uma formulação por busca e apresenta subconjunto não vazio com soma zero. Estas notas adotam explicitamente um problema de decisão com alvo arbitrário e vazio permitido. Não copiar essa diferença de convenção sem percebê-la. Exemplo [2,5,9], figura, provas específicas, contratos, DP e testes são próprios; não se atribui a DP à leitura desses trechos.

[Clay Mathematics Institute: P versus NP](https://www.claymath.org/millennium/p-vs-np/) reconferido em27/10/2026, listado como problema em aberto. O portal de apoio de Princeton retornou403 nas páginas5.4/5.5; não foi tratado como leitura. Os trechos do exemplar autorizado sustentam a preparação. Não se executou programaJava da fonte.

## Modelo e exemplo

Inteiros a₀,…,aₙ₋₁ e alvo T. Pergunta: há um conjunto de índices distintos cuja soma é T? O vazio é permitido e soma zero. Inteiros com sinal são permitidos no enunciado geral.

Busca devolve um certificado ou conclui inexistência quando termina todos os candidatos. Decisão responde sim/não. Verificação avalia uma candidata, não todas. No exemplo [2,5,9], alvo11, [0,2] é certificado positivo:2+9=11. [0] não é; sua rejeição não elimina [0,2]. [2], alvo4, [0,0] é inválido por repetir posição. Em [5,5], [0,1] é válido para alvo10: valores iguais podem ocupar posições distintas.

Cada posição entra ou fica fora:2ⁿ máscaras. A figura usa b₂b₁b₀; bᵢ indica a posição i. Na ordem das máscaras000,…,111, as somas do exemplo são0,2,5,7,9,11,14,16. A busca para na primeira solução, que é a máscara101, índices[0,2]. Só um candidato é necessário para conferir uma resposta positiva já fornecida.

## Correção e custo do verificador

Se aceita, os índices são inteiros na faixa, sem repetição, e a soma é T; portanto a candidata descreve um subconjunto válido. Se existe tal subconjunto, listar suas posições distintas faz o verificador aceitar. São as duas direções da correção para este enunciado.

Uma máscara tem n bits; uma lista de até n índices ocupa O(n log(n+1)) bits. L é o tamanho da codificação completa da instância. Validar o certificado e fazer até n adições de inteiros de tamanho controlado tem custo polinomial em L, incluindo a representação dos inteiros. Não tratar arbitrariamente uma adição de números enormes como uma operação de custo constante. A quantidade de candidatos e o tempo medido em segundos são objetos diferentes.

Nesta formulação por decisão, a existência de certificado positivo polinomialmente verificável estabelece pertinência a NP. P está contida em NP: o verificador pode ignorar certificado vazio e executar o decisor polinomial. Não demonstra P≠NP, NP-completude ou uma cota inferior para todo algoritmo. Confundir NP com “não polinomial” ou com indecidibilidade seria incorreto.

## Tabela para o domínio não negativo

Inicialmente R₀={0}. Após processar aᵢ, as somas atingíveis vêm de manter uma soma anterior ou somar aᵢ a ela. Como todos os valores são não negativos, para decidir um alvo T não negativo basta guardar somas0,…,T. Não se faz esse descarte automaticamente no domínio com negativos.

A tabela booleana começa com reachable[0]=True. Para cada item, percorre s de T para baixo e atualiza reachable[s] com reachable[s−aᵢ]. O sentido decrescente evita usar o mesmo item duas vezes. Com [2], alvo4, uma varredura ascendente incorreta tornaria2 atingível e reutilizaria o mesmo2 para marcar4. O resultado correto éFalse; [2,2] é outra entrada e admite4.

A versão simples usa O(n(T+1)) atualizações e O(T+1) posições. Essas são contagens no modelo de operações da tabela; aritmética e índices têm custos adicionais no modelo de bits. Se T=2ᵏ, sua escrita tem k+1 bits, mas a tabela teria2ᵏ+1 posições. Por isso o algoritmo é pseudopolinomial, não uma prova de tempo polinomial no comprimento binário. [2¹⁰⁰⁰] com esse mesmo alvo é fácil para uma enumeração de dois candidatos e inviável para essa tabela direta: um método ruim numa entrada não estabelece dificuldade intrínseca.

## Laboratório e contratos

`subsets.py` usa apenas Python padrão, sem dependências. Inteiros de precisão arbitrária não têm overflow de largura fixa, mas tamanho em bits ainda custa tempo e memória. Não há promessa de eficiência prática geral.

```sh
python3 -m labs.certificados.subsets
python3 -m unittest discover -s labs/certificados -t .
```

Instância: lista/tupla de int e alvo int, sem bool ou float; entrada malformada geraTypeError. Certificado deve ser lista/tupla de índices inteiros distintos na faixa, sembool, nemfloat; caso contrário retornaFalse. O verificador checa tipos antes de usar índices: [[]] é rejeitado, em vez de ser passado prematuramente a um conjunto e causar erro de hash. Nenhuma função modifica os dados.

`search` percorre máscaras em ordem crescente e retorna uma lista, incluindo[] quando pertinente; None só após terminar todos os candidatos sem solução. Ao chegar ao orçamento `max_candidates`, geraBudgetExceeded se ainda não terminou. Uma solução encontrada antes do limite continua válida. O orçamento deve ser inteiro positivo, sembool. Um limite de candidatos não constitui limite absoluto de tempo/memória para inteiros de qualquer tamanho.

`dp_decide` só aceita valores e alvo não negativos e devolvebool. Antes de alocar, compara (T+1)max(1,n) com `max_work`; se exceder, geraBudgetExceeded sem concluir não. O max(1,n) protege a alocação mesmo com lista vazia. É regra conservadora do laboratório, não contagem exata de passos. Não reconstrói certificado; busca e verificador são funções separadas.

Cinco testes confrontam busca em todas as364 listas de comprimento0–5 sobre{-1,0,2} e vários alvos com somas de combinações enumeradas independentemente; DP em todas as364 listas sobre{0,1,3} e alvos até a soma+1; certificados inválidos, igualdade de valores, zeros/negativos; orçamento versus conclusão, inteiros de1001bits e ausência de mutação. Não são ensaios de desempenho nem prova das classes gerais.

## Resoluções e revisão pessoal

1. Quatro itens:16 subconjuntos.
2. NP usa certificados positivos de tamanho e verificação polinomiais.
3. [0,2] seleciona2+9=11.
4. [0,0] repete posição e é inválido.
5. [5,5] permite[0,1], pois são posições distintas.
6. Rejeitar[0] não elimina[0,2].
7. 2¹⁰ exige11bits em binário.
8. Alvo8 pede9posições, incluindo zero.
9. [2] não admite4 sem reutilização indevida.
10. Orçamento excedido não decide inexistência.
11. Estar emNP não prova estar fora deP.
12. O(nT) não é necessariamente polinomial no comprimento binário deT.

Revisão20min proposta: enumerar as máscaras, justificar o verificador, explicar o sentido da tabela e distinguir negativa comprovada de execução limitada. Dúvidas e avaliação pessoal ainda não preenchidas. Pendentes reduções, NP-completude, outros algoritmos e análise experimental documentada; a aula não encerra §5.5 nem o percurso.
