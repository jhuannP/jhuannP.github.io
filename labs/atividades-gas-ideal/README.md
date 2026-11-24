# Atividades: pressão e estado padrão em um gás ideal

22/10/2026. Aula q2-atividades-gas-ideal,14 seções/12 exercícios, em rascunho para revisão de Jhuann. Conteúdo, reação hipotética, números e diagrama originais com apoio de IA. Sem resultados experimentais ou identificação de uma substância.

## Escopo e sequência

Potencial químico e referência → atividade adimensional → pressões parciais → Q/K → inventário A⇌2B → equilíbrio com pressão controlada → mudança de unidade versus mudança de estado padrão. Requer estequiometria, fração molar, termodinâmica introdutória e logaritmos. Não substitui soluções não ideais ou Debye–Hückel.

Em gás ideal, μ_i=μ_i°+RT ln a_i e a_i=p_i/p°=y_i P/p°. T é absoluta; p°=1 bar é a convenção de referência adotada. Um número com unidade de pressão não entra sozinho no logaritmo. Mudar bar para Pa em ambos os termos não muda a atividade. Mudar fisicamente o valor de p° altera a convenção e exige alterar μ° e K consistentemente.

Para A(g)⇌2B(g), Q=a_B²/a_A e Δ_rG=Δ_rG°+RT ln Q. Com K=exp(−Δ_rG°/RT), Δ_rG=RT ln(Q/K) nos estados interiores. Pressão fixa no estado padrão e gás ideal implicam K dependente apenas de T; composição e pressão mudam Q. Nenhuma velocidade é calculada.

## Controles e inventário

Sistema fechado para matéria e isotérmico; pressão total P prescrita por fronteira móvel idealizada. Não é um recipiente de volume constante nem sistema energeticamente isolado. Interação mecânica externa mantém a pressão. Um mol de A inicialmente, nenhum B, reação única e sem inerte.

x é fração dissociada: n_A=(1−x) mol, n_B=2x mol, total=(1+x) mol. O total de mols não se conserva, mas2n_A+n_B=2 mol de unidades constituintes. Para0≤x<1 e r=P/p°>0:
y_A=(1−x)/(1+x), y_B=2x/(1+x);
a_A=r y_A, a_B=r y_B;
Q=4r x²/(1−x²).
Igualar a K>0 dá x²=K/(K+4r); a raiz positiva está no intervalo permitido.

## Exemplo original e três comparações

K=4/3,r=1: x²=1/4, x=1/2. n_A=1/2 mol, n_B=1 mol; atividades1/3 e2/3; Q=4/3. Não são dados de uma reação real.

Compressão na comparação de equilíbrios: r novo=4, K mantido em4/3. x²=1/13, x≈0,27735. Avaliar a composição antiga sob a nova pressão dá Q=16/3 e Q/K=4, indicando retorno termodinâmico. O volume do novo equilíbrio é n_total RT/P; não foi mantido fixo. Para um recipiente rígido, substituir P=n_total RT/V antes de resolver altera o problema.

Trocar unidade de pressão: converter numerador e pressão padrão para Pa preserva r, Q e K.

Trocar estado padrão: p° novo=2p° antigo, no mesmo estado físico. As atividades se dividem por2 e, para esta reação de diferença estequiométrica+1, Q e K se dividem por2. Q/K e x não mudam. Não confundir essa operação com compressão.

## Laboratório

Na raiz do site, biblioteca padrão:
    python3 -m labs.atividades-gas-ideal.experiment
    python3 -m unittest discover -s labs/atividades-gas-ideal -t .

state(x,r) usa int/Fraction, sem bool/float. Retorna quantidades em mol para a base inicial de1 mol, frações, atividades e Q. Em x=0 retorna Q=0; não calcula ln(0). Rejeita x=1 ou fora do balanço e r≤0. equilibrium_square(K,r) retorna x² exato, exigindo K e r positivos. Não é solver para reações gerais ou mistura de reações.

Cinco testes: exemplo e compressão;100 estados por inventário/pressões parciais;57 reconstruções de equilíbrios racionais e monotonicidade; conversão de unidades e nove trocas consistentes de padrão; extremos e contratos. A raiz aproximada aparece só na explicação, não é um resultado racional exato. O diagrama estado-atividade.svg é próprio.

## Fontes

Programa oficial CCM0124: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124, aberto em22/10/2026, retorno da ferramenta com captura de quatro semanas antes. Ativação01/01/2025 posterior à turma2024/1; versão ministrada não recuperada. Itens5 e7 incluem atividades e equilíbrio. A aprovação permanece a do panorama consolidado, sem nova inspeção do histórico neste bloco.

Levine, Physical Chemistry, sexta edição2009, exemplar privado: consulta textual parcial em22/10/2026 a §§6.1–6.2 pp.175–179/PDF193–197 e §10.1 pp.294–295/PDF312–313. A extração emite avisos de fonte; identidade dos símbolos/sinais foi conferida pela derivação e coerência dimensional, sem nova inspeção visual do PDF neste bloco. Não foi lido o capítulo integral, copiado o exemplo numérico do livro ou distribuído o PDF.

A referência da turma e a existência do livro não provam que Jhuann domina esses assuntos. Esta aula não desenvolve propriedades de eletrólitos; termos de atividade em soluções líquidas apenas delimitam o que ainda falta.

## Continuidade e lacunas

Revisão pessoal: reconstruir o inventário, Q, x² e as diferenças entre pressão controlada, conversão de unidade e referência. Atividades/soluções iônicas passa a cobertura Parcial pelo primeiro recorte de atividade; soluções não ideais, íons e Debye–Hückel ainda pendentes. Terceira lei e eletroquímica permanecem Lacuna. Química II tem7 aulas/82 exercícios,13 grupos parciais e duas lacunas; nenhum completo.

Verificação do bloco:879 testes Python aprovados;506 estruturas MathML conferidas. Após ajustes apenas de clareza nos enunciados,12 testes do catálogo/correção repetidos e aprovados. No navegador,1/13 aceito na questão6; figura inspecionada a390px, sem transbordamento horizontal ou erros de console observados; viewport restaurado. Prévia atividades-gas-ideal-mobile.jpg. Nenhum modelo JavaScript alterado, suíte de simulações não repetida. Catálogo495 aulas/2814 exercícios em rascunho; nenhuma disciplina completa. Próxima revisão pessoal: distinguir r, Q e K e reconstruir o efeito da pressão. Próximo preparo global: conferir lacunas e referências de Computação II. Saldo semanal96%, parada operacional65%.
