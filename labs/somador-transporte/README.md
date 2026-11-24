# Somador completo — notas de aula

Aula existente aprofundada; IDs sc1/sc2, exemplo15+1, Python e desafio de quatro bits preservados. Rascunho; revisão pessoal pendente. Portas ideais, sem medir circuito físico.

Fonte: Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, exemplar©2017,§7.3 pp.1028–1029/PDF1049–1050, consulta textual parcial em27/10/2026. Arquivo nomeado2016 diverge do copyright; não apagada a diferença. Fonte descreve módulos MAJ/ODD e ripple-carry; dois meios somadores, invariante, figura, exemplos e testes produzidos nas notas. Não copiados diagrama/exercícios; sem leitura integral ou nova inspeção visual. PDF privado não distribuído.

Identidade local A+B+Cin=S+2Cout. Posição i usa peso2^i; prefixo j satisfaz A<j+B<j+c0=R<j+2^j c_j. Conclusão A+B+c0=baixo+2^w carry. Carry final não é overflow com sinal:7+1 tem baixo8,carry0,overflow1 em quatro bits;−1+1 tem baixo0,carry1,overflow0. Overflow de adição é XOR entre carry que entra/sai do bit de sinal, comparado a faixa decodificada nos testes.

Rodar na raiz:`python3 -m unittest discover -s labs/somador-transporte -t .`. Biblioteca padrão, largura1..16, palavras inteiras sem sinal e carry0/1. Rejeita bool/float e operandos fora da faixa. Sem alteração no emulador M8 ou integração automática de flags. Quantidade de módulos/caminho de dependência é contagem lógica, não atraso em nanossegundos, potência, carga ou transistor.


## 27/10/2026 — verificação do somador e prova de overflow

Consolidada a elaboração previamente existente de `somador-completo`:14 seções/12 exercícios, identidade local, dois meios somadores, invariante por prefixos, reconstrução da soma e distinção entre carry sem sinal/overflow em complemento de dois. Acrescentada nesta continuação a prova algébrica: se u,v,s são bits de sinal e c,d os transportes nessa posição, u+v+c=s+2d; soma decodificada menos resultado decodificado =2^w(c−d). Portanto c XOR d detecta overflow. Revisada a legibilidade de enunciados. Exemplo15+1, código e desafio anteriores preservados; M8 não alterada. Portas ideais, sem medir circuitos, atrasos ou potência.

Proveniência: Sedgewick/Wayne, Computer Science, exemplar©2017,§7.3 pp.1028–1029/PDF1049–1050, leitura textual parcial registrada no bloco de elaboração anterior. Fonte com MAJ/ODD e ripple-carry; decomposição por meios somadores, provas, figura, exercícios e laboratório próprios. Nesta continuação conferidos os registros e o material, sem nova leitura do livro ou inspeção visual do PDF; exemplar privado não distribuído. Nome2016 do arquivo e copyright2017 não confundidos.

Verificação desta continuação:14 testes de catálogo e5 do laboratório aprovados. Oito linhas da tabela-verdade confrontadas com divisão inteira;10.920 configurações em larguras1..6 verificam soma e invariante dos prefixos;512 combinações de quatro bits/carry verificam overflow por faixa decodificada; casos em8,12,16 bits e contratos. Conferidas819 estruturas MathML. No navegador390px, exercício de carry em0111+0001 rejeitou1 e aceitou0 pelo Enter; documento390/390px, console sem erros observados. Figura inspecionada em `somador-transporte-mobile.jpg`. Windows real, leitor de tela e revisão pessoal pendentes. A prova complementa os testes, sem alegação de hardware validado.

ComputaçãoII:20 aulas/130 exercícios e11 introduções curtas; percurso editorial de teoria/arquitetura, sem equivalência administrativa automática comCCM0128. Global51 trilhas,550 aulas/4453 exercícios e191 introduções curtas; nenhuma disciplina concluída ou domínio pessoal certificado. Próxima revisão20min: traçar15+1 e explicar por que7+1 tem carry0/overflow1, enquanto−1+1 tem carry1/overflow0. Próxima elaboração global: retomar uma lacuna curta de FísicaII, consultando seu programa e referências. Saldo semanal78%; parada operacional65% mantida.
