# Carbonilas — convenção e contrato de contagem

Material original em rascunho. Um metal, CO terminais neutros, sem ponte ou ligação metal–metal. g=número de grupo, q=carga total com sinal, n=número de ligantes. Método iônico: d formal=g−q; total=d+2n. Neutro: g+2n−q. Não contar a carga duas vezes. O número d formal do complexo não é a configuração do átomo gasoso, nem medida de carga real.

Miessler/Fischer/Tarr, Química Inorgânica5, edição brasileira Pearson2014: §13.3.1 pp.472–474/PDF487–489, métodos e carga; §13.3.2 pp.475–476/PDF490–491, justificativa por orbitais e exceções. Recortes textuais parciais conferidos em27/10/2026 pelos cabeçalhos impressos; sem leitura integral, nova inspeção visual ou reprodução de tabelas/exercícios/figuras. Cr(CO)6, Fe(CO)5, Ni(CO)4 são exemplos clássicos; candidato carregado e variação de fragmento são exercícios formais próprios. Exemplar privado não distribuído.

Na raiz: `python3 labs/carbonilas-contagem/counting.py`. Biblioteca padrão; grupo3..10, CO0..8, carga inteira com0≤g−q≤10; sem bool/float. Domínio didático restrito, não critério de existência. Script confere exemplos,792 inventários formais, concordância de convenções, perda de uma doação e contratos. Verificação aritmética não demonstra estabilidade, geometria ou mecanismo; os792 inventários não são792 espécies conhecidas.

Próxima revisão20min: explicar a contribuição de cada parcela, comparar coordenações e apontar o limite de retirar CO sem medir uma reação. Outros ligantes, NO, hapticidade, pontes, ligações metal–metal, clusters e catálise continuam pendentes. Revisão pessoal não realizada.


## 27/10/2026 — carbonilas e contagem eletrônica

Nova `q3-carbonilas-contagem`,11 seções/12 exercícios, primeiro recorte do grupo organometálicos/clusters/ligação metal–metal, que passou de Lacuna a Parcial. Contrato: um metal com CO terminais neutros. Convenções iônica e neutra: d formal=g−q, N_e=d+2n=g+2n−q; carga usada uma única vez. Cr(CO)6/Fe(CO)5/Ni(CO)4 ilustram mesma contagem18 com coordenações6/5/4. Candidato de grupo9 com5CO/carga+1 explicitamente formal, sem alegar espécie observada. Limites18/16, retrodoação, contagem versus carga física e perda de ligante versus mecanismo. Outros ligantes, pontes, hapticidade, clusters, metal–metal e catálise pendentes.

Miessler/Fischer/Tarr, Química Inorgânica5, edição brasileira Pearson2014: §13.3.1 pp.472–474/PDF487–489;§13.3.2 pp.475–476/PDF490–491. Consulta textual parcial em27/10/2026, cabeçalhos de extração paginada conferidos. P.466/PDF481 não forneceu corpo legível e não foi tratada como fonte lida. Sem nova inspeção visual, reprodução de tabela13.1, exercícios ou figura13.8. Exemplos clássicos são contextualizados, comparação, figura, candidato e atividades adicionais próprios. Livro privado não distribuído. Histórico/programa oficial não reabertos nesta extensão; versão ministrada continua incerta.

Verificação:14 testes de catálogo aprovados;821 estruturas MathML do catálogo conferidas. Script executado com exemplos e792 inventários formais no domínio didático (grupos3..10,d0..10,n0..8); concordância de convenções, efeito de retirada de CO e rejeição de entradas inválidas. Não são792 espécies observadas nem testes de estabilidade/energia. No navegador390px, exercício5 rejeitou17 e aceitou18 pelo Enter; figura inspecionada em `carbonilas-contagem-mobile.jpg`, documento390/390px e console sem erros observados. Sem teste real de Windows/leitor de tela. Revisão pessoal pendente.

QuímicaIII:12 aulas/142 exercícios;10 grupos parciais/8 lacunas em18 grupos. Global51 trilhas,552 aulas/4499 exercícios,189 introduções curtas. Nenhum curso completo ou domínio pessoal certificado. Próxima revisão20min: reconstruir as três contagens, justificar carga única e apontar o limite de inferir estrutura/reatividade. Próxima elaboração global: conferir introduções curtas de deep learning e escolher uma lacuna com relação clara entre matemática e código. Saldo semanal78%; parada65% mantida.
