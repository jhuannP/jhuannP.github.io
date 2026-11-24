# Partição, grupos e microestados

Novo laboratório original, mantendo o código float/painel/desafio anteriores da aula. Modelo finito com E/ε inteiro e q=exp(−βε) racional em(0,1); β=1/(kB T_física). O código anterior adota kB=1 e usa T como escala térmica de energia; não inserir joules/kelvin sem conversão.

Tong, Statistical Physics§1.3.1 equações1.20–22;§1.3.2 equações1.25–26 e§1.3.3 agrupamento por degenerescência: https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html . Consulta textual parcial em27/10/2026. Modelo de grupos1/3 com q1/3, números, figura e derivações adicionais próprios; sem copiar exercícios ou notas integralmente. Não é evidência de domínio pessoal ou validação da IC.

Na raiz: `python3 labs/particao-grupos/groups.py`. Biblioteca padrão;1..20 grupos, níveis inteiros−100..100, multiplicidades1..100 e q int/Fraction em(0,1), sem bool/float. Probabilidades/momentos são racionais exatos; logaritmos de entropia usam float e não têm faixa ilimitada. Não é rotina geral de ensemble ou de energia contínua. Para escalas extremas do racional, conversão em float pode falhar; os exemplos verificados estão longe desse regime.

Conferência por expansão explícita de microestados, em12 cenários: probabilidades, normalização, média, variância, identidade de entropia e deslocamento de origem. Emq1/3,g=(1,3),as probabilidades microscópicas são(1/2,1/6,1/6,1/6); probabilidades agrupadas(1/2,1/2). Entropia de rótulos difere da de microestados por(1/2)ln3. São exemplos executáveis, não prova de limite termodinâmico ou dados experimentais.

Próxima revisão20min: reconstruir a distribuição e explicar por que agrupar níveis não elimina a multiplicidade. Revisão pessoal, dinâmica térmica, sistemas infinitos, faixa numérica geral e efeitos de interação pendentes.


## 27/10/2026 — partição, degenerescência e entropia interna

`particao-degenerescencia` ampliada de3 seções/2 exercícios para12/12. Preservados código float, painel, desafio e IDs anteriores. Exemplo de mesma energia esclarecido como dois grupos, não dois níveis energéticos distintos. Definidos β=1/(kB T_física) e T térmico do código comkB=1. Novo modelo com energias0/ε,g1/3,qexp(−βε): paraq1/3, probabilidades dos grupos1/2,1/2 e microestados1/2,1/6,1/6,1/6. Derivados U/ε1/2,Var/ε²1/4 e parcela interna de entropia(1/2)ln3. Provas por agrupamento, derivadas de lnZ, origem de energia e limites de temperatura finitos; sem dinâmica de térmicas ou limite termodinâmico comprovado.

Fonte pública parcialmente consultada em27/10/2026: Tong,StatisticalPhysics§1.3.1 eq1.20–22,§1.3.2 eq1.25–26,§1.3.3 agrupamento por degenerescência, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html . Modelo, figura, números e derivações adicionais próprios. Sem reprodução integral/exercícios, sem resultado experimental ou da IC.

Verificação:14 testes de catálogo aprovados;822 estruturas MathML conferidas. Laboratório racional executado em12 cenários de agrupamento/expansão explícita: normalização, médias/variância, entropia e mudança de origem, além de caso de referência e contratos. Entropias usam logaritmo float com faixa limitada; demais probabilidades/momentos são racionais. Não é rotina canônica geral ou teste de todas as escalas. No navegador390px, exercício5 rejeitou1/2 e aceitou1/6 pelo Enter; figura inspecionada em `particao-grupos-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados. Revisão pessoal pendente.

MecânicaEstatística:25 aulas/100 exercícios, cinco recortes desenvolvidos e20 introduções curtas. Global51 trilhas,552 aulas/4529 exercícios,186 introduções curtas. Contagens não certificam curso completo ou domínio individual. Próxima revisão20min: expandir os quatro microestados e justificar a diferença de entropia após agrupamento. Próxima elaboração global: conferir uma introdução de ProcessosEstocásticos e suas referências, preservando alternância. Saldo semanal78%; parada65% mantida.
