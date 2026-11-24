# Seleção e endereçamento

Rascunho original da aula `multiplexador-decodificador`:10 seções/10 exercícios. Mantém o painel anterior, IDs, exemplo e desafio. Trilha complementar, sem equivalência com CCM0128 ou afirmação de domínio pessoal.

## Fundamento e convenção

Mux2 seleciona A para S0 e B para S1. A expressão (¬S∧A)∨(S∧B) reduz à especificação nos dois casos. Endereço s₁s₀ significa índice2s₁+s₀. O decodificador enumera mintermos e produz uma lista por índice, sem interpretar a lista como outro endereço. EN0 desliga tudo; exatamente uma linha ativa exige EN1. Uma árvore de três muxes e a composição decoder/AND/OR implementam a mesma escolha de quatro dados.

Palavras têm quatro bits selecionados pelo mesmo S. O inteiro1 como máscara não é1111: usamos máscara de0 ou15. Circuitos são combinacionais ideais, sem estado, atraso, glitches ou medições elétricas.

## Fonte e limites

Sedgewick/Wayne, *Computer Science*, ©2017, §7.3 pp.1019–1022/PDF1040–1043, seleção e decoder: consulta textual parcial em27/10/2026. OCR/legendas contêm inconsistências de índices/zero versus um, não adotadas; lógica reconstruída pelas definições. Sem nova inspeção visual ou leitura integral, cópia de figura ou exercício. Página complementar de Princeton não abriu: não registrada como consulta do corpo. Nenhum programa oficial foi reaberto.

## Executar

```sh
python3 labs/selecao-endereco/selection.py
```

Cinco testes enumeram as8 linhas do mux2,8 combinações de endereço/habilitação,64 seleções de quatro dados e512 seleções de palavras de quatro bits, além dos contratos. Compare com escolha por índice, independente da construção por portas. Para esses domínios finitos, a enumeração é completa; não prova implementação física ou largura arbitrária. Entradas apenas int nativos, sem bool/float.

Revisão de20min: escrever códigos/linhas, prever a árvore e explicar leitura versus seleção de escrita. Memória sequencial, barramentos reais, otimização e projeto físico pendentes. Revisão pessoal e uso com aluno ainda não feitos.


## 27/10/2026 — multiplexador e decodificador: controle, linhas e dados

`multiplexador-decodificador` ampliada de3 seções/2 exercícios para10/10, preservando IDs, exemplo, desafio e painel. Mux2 justificado pelos dois valores de S; ordem s₁s₀ e mintermos do decoder2:4; EN0 permite zero linhas, EN1 exatamente uma; árvore de três muxes e construção por decoder/AND/OR; seleção de palavras e máscara correta. Código/desafio anteriores aceitavam bool/float por comparação numérica e podiam falhar depois; contrato agora exige int nativo. Sem equivalência com CCM0128, armazenamento ou inferência de atrasos físicos.

Fonte: Sedgewick/Wayne ComputerScience ©2017 §7.3 pp.1019–1022/PDF1040–1043, consulta textual parcial em27/10/2026. OCR/legendas inconsistentes não adotados; lógica reconstruída pela especificação. Sem nova inspeção visual/leitura integral, cópia de figuras ou exercícios. Página complementar de Princeton inacessível; não marcada como leitura do corpo. Programa oficial não reaberto. Figura, exemplos e enumerações próprios.

Cinco testes em `labs/selecao-endereco/selection.py` aprovados:8 linhas mux2,8 combinações decoder/EN,64 seleções com quatro dados e512 escolhas de palavras, mais contratos. Tabelas completas nesses domínios ideais; não prova de hardware físico ou largura geral.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou1 e aceitou0 para linhas ativas com EN0; documento390/390px, console sem erros observados. Figura inspecionada em `selecao-endereco-mobile.jpg`; viewport restaurada. Windows real, leitor de tela e revisão pessoal pendentes.

ComputaçãoIIcomplementar20 aulas/158 exercícios, oito introduções curtas, distinta da disciplina oficial. Global51 trilhas/576 aulas/5276 exercícios,142 introduções curtas; sem certificação de cobertura ou domínio. Próxima ação20min:traduzir endereço10 em linha2, explicar EN0 e reconstruir mux4 pelas duas implementações. Próxima elaboração global:conferir uma lacuna de Física escolar, alternando as áreas após consultar referência. Saldo semanal antes/depois66%; parada operacional65% preservada.
