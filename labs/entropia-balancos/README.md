# Segunda lei: conservar energia não basta

Ciclo com dois reservatórios fixos, TH>TC>0 K. QH recebido da fonte quente e QC rejeitado à fria são módulos em J, com QH>0 e 0≤QC≤QH. W=QH−QC, η=W/QH. A máquina retorna ao estado inicial: ΔSmáquina=0, inclusive se houver irreversibilidade. O total máquina+reservatórios, sem outras trocas de entropia, varia por ΔStot=QC/TC−QH/TH. Exigir ΔStot≥0 equivale a η≤1−TC/TH. Não ser excluído por esse critério não valida engenharia ou construção.

Propostas próprias com TH=600 K, TC=300 K, QH=1200 J:

| QC (J) | W (J) | η | ΔStot (J/K) | Leitura do balanço |
|---|---|---|---|---|
| 600 | 600 | 1/2 | 0 | limite reversível |
| 800 | 400 | 1/3 | 2/3 | compatível com irreversibilidade |
| 400 | 800 | 2/3 | −2/3 | excluída pela segunda lei |

Todas conservam energia; a última viola entropia do total isolado. Não foi fornecida duração do ciclo, então W não é potência. Subsistemas podem perder entropia; não aplicar não diminuição a qualquer sistema fechado sem contar vizinhança.

Entropia é função de estado: ΔS pode ser calculada por integral de δQrev/T em um caminho auxiliar reversível entre os mesmos extremos. Na expansão livre adiabática de gás ideal com razão r, Qreal=Wreal=0 e Tfinal=Tinicial. Escolher uma isoterma reversível auxiliar fornece ΔSgas=nR ln r. Para nR=2 J/K e r=2, vale 2 ln2≈1,386 J/K. No processo livre, a vizinhança não muda de entropia e há produção. Na isoterma reversível auxiliar, o reservatório perde a mesma entropia que o gás ganha e o total é zero. Não confundir Qreal com Qrev.

Na raiz do site:

    python3 -m labs.entropia-balancos.balances
    python3 -m unittest discover -s labs/entropia-balancos -t .

candidate usa int/Fraction sem bool, analisa propostas e retorna not_excluded_by_entropy, sem rejeitar antecipadamente ΔStot negativo. free_entropy usa int/float finitos, nR>0 e r≥1; saídas não representáveis são rejeitadas. Seis testes cobrem referências, equivalência de Carnot em 135 configurações, escala, fronteiras, caminho auxiliar e contratos. Quadratura numérica é do caminho reversível auxiliar, não do processo livre real.

Fontes consultadas parcialmente por texto em 22/10/2026: Nussenzveig, Curso de Física Básica vol.2, 5ª ed., §10.2 p.250/PDF251; §10.7 pp.267–268/PDF268–269; §10.8 pp.273–274/PDF274–275. Cabeçalhos confirmam páginas impressas; sem nova inspeção visual. [OpenStax vol.2 §4.6](https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy) como apoio parcial. Condição de entropia não decrescente aplicada ao total isolado. Contas, propostas, figura e testes próprios; nenhum exemplar privado reproduzido.

Aula f2-segunda-lei ampliada para onze seções/doze exercícios. Exemplo, Python, desafio e painel anteriores preservados. Material assistido por IA para revisão pessoal; não certifica domínio ou resultados de pesquisa. Próxima revisão: reconstruir os três balanços e explicar por que ciclo irreversível tem ΔSmáquina=0 e ΔStot>0. Equivalências formais, ciclos completos, refrigeradores, corpos finitos, geração local e interpretação estatística continuam pendentes. A disciplina mantém dez grupos curriculares parciais, mesmo com os 14 recortes agora desenvolvidos.

Verificação: seis testes novos e 13 de catálogo aprovados; 547 estruturas MathML conferidas. No navegador em 390 px, figura e legenda legíveis; questão da proposta excluída rejeitou +2/3 e aceitou −2/3. Largura igual à tela e nenhum erro de console observado. Prévia: entropia-balancos-mobile.jpg. Não houve revalidação integral da suíte global ou do painel antigo de Carnot, preservado. Catálogo: 501 aulas/3178 exercícios em rascunho. Saldo semanal após bloco: 91%; parada em 65%.


## 27/10/2026 — segunda lei para dois corpos finitos

`f2-segunda-lei` ampliada de11 seções/12 exercícios para16/16. Novo recorte original: dois sólidos rígidos isolados, capacidades totais constantes positivas, sem trabalho, reação ou mudança de fase. Primeira lei determina temperatura final ponderada; caminhos reversíveis auxiliares fornecem C ln(T_f/T_i), sem substituir o processo real. Concavidade de ln prova produção total positiva para temperaturas distintas. Exemplo próprio C_H=C_C=2 J/K,600/300 K: equilíbrio450 K, calor300 J, entropias−0,57536 e+0,81093 J/K, soma2 ln(9/8)≈0,23557 J/K. Explica por que0,5 J/K por temperaturas iniciais constantes falha. Sem modelo temporal de condução ou alegação experimental.

Fonte pública parcialmente consultada: OpenStax University Physics vol.2 §4.6, equação4.10 e exemplo4.5, em27/10/2026, https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy . Sustenta caminho auxiliar e integral C dT/T. Dois corpos, concavidade, números, exercícios e script próprios. Nussenzveig permanece referência curricular já localizada; sem nova leitura nesta continuação. As quinze aulas atuais já têm recortes desenvolvidos; o inventário introdutório no início da auditoria é histórico e não foi usado para afirmar lacuna atual de três seções.

Verificação:14 testes do catálogo aprovados e821 estruturas MathML conferidas. Script `labs/entropia-balancos/finite_bodies.py` executado em três cenários (capacidades iguais, desiguais e temperaturas iguais): energia, sinais, logaritmos por integração de Simpson independente e expressão do exemplo. São exemplos executáveis, não19 novos testes. No navegador390px, exercício13 rejeitou900 e aceitou450 pelo Enter; documento390/390px, console sem erros observados. Fórmulas adicionais renderizadas e texto inspecionado na captura `corpos-finitos-mobile.jpg`. Sem teste no Windows/leitor de tela real. Revisão pessoal pendente.

FísicaII:15 aulas/178 exercícios, dez grupos curriculares parciais. Global51 trilhas,550 aulas/4457 exercícios,191 introduções curtas; contagem não certifica curso completo ou domínio de Jhuann. Próxima revisão20min: reconstruir energia e as duas entropias separadas e justificar por queQ/T inicial não serve. Próxima elaboração global: retomar lacuna introdutória de Álgebra Linear após conferir a cobertura atual, sem prolongar automaticamente termodinâmica. Saldo semanal78%; parada65% mantida.
