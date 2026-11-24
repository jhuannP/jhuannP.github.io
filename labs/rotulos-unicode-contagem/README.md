# Rótulos, Unicode e contagem

Rascunho original. Execute `python3 labels.py`,sem dependências adicionais. Dados sintéticos;sem dados de clientes,pessoas ou da pesquisa. Exemplo e desafio antigos da aula foram preservados.

## Contrato novo,explicitamente separado

Entrada:lista ou tupla de strings. Cada item é um rótulo completo,sem tokenização interna. Canonização:strip,casefold,NFC. Vazios são descartados e contabilizados;acentos,pontuação e espaços internos ficam. Não é correção linguística,remoção de diacríticos,identificação de pessoas ou fusão aproximada de registros. Não trocar NFC por NFKC sem especificar outra política.

Duas representações de í,U+00ED e i+U+0301,se unem neste exemplo. A forma física com vírgula e fisica sem acento permanecem distintas. Os seis registros produzem quatro chaves,física com frequência2 e outras três com1;cinco aceitos e um descarte. O desafio original strip/casefold podia manter vazios como chave;ele não foi silenciosamente substituído.

A função não altera a entrada e cria um novo dicionário. get consulta com padrão0 e não insere por si só. O invariante por prefixos prova que cada frequência é exatamente a quantidade aceita correspondente. A soma de frequências é o número aceito;aceitos+descartes é o tamanho da entrada.

Ordem de inserção não é alfabética ou de frequência. Atualizar chave existente preserva sua posição;permutar a entrada pode alterar a ordem das primeiras aparições. Para saída canônica,ordenamos por frequência decrescente e string Unicode em empates,sem colação linguística portuguesa. Comparações textuais têm custo dos caracteres;operações hash não têm garantia universal de tempo constante.

## Fontes consultadas parcialmente em27/10/2026

- Sedgewick e Wayne,Computer Science:An Interdisciplinary Approach,exemplar do acervo com copyright2017 (nome do arquivo2016),§4.4 pp.624–626/PDF645–647. Extração textual parcial de associação chave–valor,API,atualização,consulta e chaves,principalmente inícios das páginas. Sem nova inspeção visual,leitura integral ou reprodução do PDF privado. A API Java da obra tem escolhas próprias,como null,não transplantadas para dict Python. Exemplos e código em português/Python são originais.
- [Python3.14,dict e strings](https://docs.python.org/3.14/builtins/stdtypes.html),recortes de get,ordem de inserção e str.casefold.
- [Python3.14,unicodedata.normalize](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize),recorte de NFC/NFKC e equivalência canônica/compatibilidade.

A documentação online identificada é3.14.10;execução local CPython3.14.5. Sem atualização do ambiente ou instalação. Júpiter não reaberto neste bloco;versão efetiva da turma2023 de ComputaçãoI continua pendente conforme mapa existente. O recorte por Sedgewick é organização editorial,não prova de linguagem ou sequência ministrada.

## Verificações e alcance

Cinco testes locais:casos Unicode conhecidos e políticas,idempotência nos rótulos do exemplo,contagens/ordens/entrada preservada;2801 entradas de comprimentos0..4 confrontadas com contagem por lista,conservação e permutação;combinação de lotes;contratos. Casos finitos não certificam todas as strings Unicode,qualidade linguística ou desempenho. Não implementamos tabela hash,árvore,tokenizador geral ou correção de dados.

Em20min,reconstrua os seis registros,prove o invariante,explique consulta versus inserção e preveja a mudança de ordem após permutar. Depois indique uma alteração de política que exigiria outro significado para as contagens. Revisão pessoal pendente;Windows real e leitor de tela não testados.
