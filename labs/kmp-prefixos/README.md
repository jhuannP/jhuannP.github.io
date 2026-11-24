# KMP: padrões, bordas e sobreposição

Algoritmo original por função de prefixos em Python3, biblioteca padrão. Padrão não vazio, busca literal sensível a maiúsculas; retorna todas as posições de início, inclusive sobrepostas, com índices começando em0. Strings Python são tratadas por pontos de código, não bytes ou grafemas. Sem normalização Unicode automática: é e e+acento combinante não são a mesma sequência. Limites do laboratório: padrão1..64 e texto0..512 pontos de código, não limites do algoritmo geral.

## Reconstruir antes de executar — duas sessões de20 minutos

Uma borda é prefixo próprio que também é sufixo. Para cada i, π[i] é o maior comprimento dessa borda em p[0:i+1]. Para ababa, a tabela é0,0,1,2,3. Em aba, borda a; em abab, ab; em ababa, aba. Comprimento é diferente do índice do último caractere:π[4]=3 descreve aba, cujos índices são0..2.

Para calcular π[i], comece com j=π[i−1]. Se p[i]=p[j], a borda cresce em um. Se falha e j>0, a próxima possibilidade é a maior borda da própria borda, j=π[j−1]. Ela conserva o sufixo já conhecido, e comprimentos intermediários descartados não satisfazem o requisito de borda. Repita até casar ou chegar a zero. A tabela já preenchida refere-se a prefixos menores, então o cálculo não é circular.

Na busca, j guarda o comprimento do prefixo compatível com o sufixo do texto processado, após retirar o estado de aceitação para sua maior borda. No próximo caractere, tente prolongar; falhas percorrem a mesma cadeia de bordas sem recuar o índice do texto. Se j=m, registre i−m+1 e retome π[m−1]. Reiniciar emzero perderia ocorrências sobrepostas: ababa em ababababa começa em0,2,4. Depois do primeiro acerto, a borda aba de comprimento3 já está presente.

## Prova e custo

Todo candidato viável após falha é borda do prefixo conhecido; a cadeia de π enumera esses candidatos em ordem decrescente. Quando um prolonga, é o maior compatível; quando chega a zero e falha, não há sufixo não vazio possível. Indução sobre os caracteres dá o invariante e a correção dos inícios reportados. No estado de aceitação, reportar antes do recuo conserva o acerto completo, e a maior borda conserva a possibilidade de sobreposição.

Nesta implementação há uma comparação final por caractere visitado. Cada falha com j>0 reduz j estritamente; o total dessas reduções não ultrapassa o total de incrementos, de no máximo n. Retornar pela borda após um acerto completo também reduz j e não aumenta esse total. Assim a busca tem até2n comparações; a construção, até2(m−1). Custo O(n+m), memória auxiliar O(m), além da lista O(k) de k resultados. O modelo conta comparação/acesso de pontos de código como constante e não mede tempo de parede, I/O ou alocações do ambiente.

Não construímos uma tabela DFA de tamanho alfabeto×padrão. O livro de referência apresenta essa organização; o algoritmo de prefixos aqui tem outra representação, retorna todos os acertos e possui análise própria. Limite assintótico não garante que Python próprio supere uma biblioteca otimizada.

## Verificação

Execute `python3 labs/kmp-prefixos/search.py`; testes `python3 -m unittest discover -s labs/kmp-prefixos -t .`. Quatro testes: bordas por comparação independente de prefixos/sufixos;15810 pares de textos/padrões binários contra oráculo por fatias, contadores lineares;repetição/Unicode/sobreposição;contratos. Testes finitos apoiam o programa, não demonstram universalidade ou desempenho real. Padrão vazio é rejeitado por contrato; outras APIs podem defini-lo de modo diferente.

Fontes consultadas parcialmente em29/10/2026: Sedgewick/Wayne, Algorithms4ªed2011, §5.3 p.758/PDF771 e pp.762–763/PDF775–776, problema de substring e reaproveitamento do padrão; p.768/PDF781 consultada para contraste com implementação DFA. Sem nova inspeção visual ou leitura integral. [Site dos autores §5.3](https://algs4.cs.princeton.edu/53substring/) retornou403 no acesso direto; recorte indexado consultado nesta data, com distinção KMP/KMPplus. Não descrito como leitura direta da página. Exemplos, prova, figura, código e exercícios próprios; sem copiar o autômato, Java, figuras ou exercícios da fonte. PDF privado não disponibilizado.

Programa CCM0128 não reaberto neste bloco: registro22/10/ativação01/01/2025 posterior àturma2024 preservado, versão histórica desconhecida. Algorithms4 e Computer Science são obras diferentes; não transferir paginação. Pendentes: Boyer–Moore/Rabin–Karp, indexação, texto normalizado, múltiplos padrões, fluxos incrementais e revisão pessoal. Página preparada não comprova domínio ou autoria pessoal.
