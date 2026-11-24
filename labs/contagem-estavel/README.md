# Contagem estável — rascunho

Aula `ccm0128-contagem`,14seções/12exercícios/3MathML. CCM0128 é a disciplina de algoritmos/estruturas;rota `computacao-2` é outro percurso complementar de teoria/arquitetura.

## Fontes

[Programa USP](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0128) reconferido22/10/2026,ativação01/01/2025 posterior à turma2024. Versão ministrada não recuperada;aprovação histórica preservada da conferência anterior.

Sedgewick/Wayne,Algorithms4ªedição:identificação,copyright2011/primeira impressão março2011 reconfirmados no acervo autorizado. Consulta textual parcial §5.1,pp.703–705(PDF716–718),contagem indexada,prefixos e distribuição. Cache integral extraído para localizar páginas não equivale a leitura integral. [Site dos autores](https://algs4.cs.princeton.edu/51radix/) retornou403,não foi usado como leitura. Nenhum PDF,figura,tabela ou solução copiado ao site.

O algoritmo é adaptação própria em Python com frequências,start e cursor separados,retorno de nova lista e validação explícita;não transcrição linha por linha da implementação Java. Exemplo rotulado A–F,dados,exercícios,tabelas e testes próprios.

## Contrato e prova

Tuplas(chave,valor),chave int não bool em[0,K),K int positivo. Valores não são comparados;referências são preservadas e entrada não muda. Regiões[start[k],start[k]+freq[k]) disjuntas. Após i registros,cursor[k]=start[k]+vistos_i[k];a região preenchida mantém ordem original. Isso justifica ausência de sobrescrita,permutação,ordenação e estabilidade. A enumeração testa a implementação,não substitui prova geral.

Núcleo counting:Θ(n+K)tempo e espaço,incluindo saída,sob operações unitárias e alocação viável. O traçado copia n+K referências por estado e custa O((n+1)(n+K))tempo/espaço. Não confundir os dois. Chaves arbitrárias/grandes e domínio esparso não ganham gratuidade;K é custo real. Não há radix ou compressão de coordenadas implementados.

Painel:cinco conjuntos pequenos, K3..8;passo controla só distribuição,após contagens/prefixos prontos. Passo é limitado ao tamanho atual,inclusive zero na entrada vazia. Frequências e inícios permanecem fixos;cursores mudam. O estado inicial de chave ausente pode ser n,sem representar slot para escrita. Dados sintéticos,sem clientes ou evidência pessoal de trabalho.

## Verificar e explorar

`python3 -m unittest discover -s labs/contagem-estavel -t .`

Quatro testes:todos os vetores de comprimento0..6 e domínios1..4 contra sorted estável usando objetos como valores;invariante em364entradas de comprimento0..5/domínio3 e seus prefixos;vazio/domínio esparso/referências/entrada imutável;contratos.105estados Python/JS,com adaptação do controle de passo.

Tese visual:entrada com rótulos,uma tabela de contadores e posições de saída explícitas;sem barras que escondam estabilidade. Contraste e indicação textual de vazio;controles em coluna no celular. Exploração manual por passo,sem animação automática.

Próxima revisão pessoal:prever o destino do próximo registro e provar por que A,C,F permanecem nessa ordem. Radix,grafos ponderados,construção linear de heap,projeto próprio e revisão do curso inteiro permanecem pendentes.
