# Mutação, seleção e amostragem: ciclo declarado

Rascunho original de `b3-mutacao-selecao`,11 seções/10 exercícios. População haploide, um locus e alelos A/a; contribuição relativa1+s para A e1 para a; seleção seguida de mutação A→a com probabilidade μ, sem reversão ou migração. Amostragem binomial opcional da próxima geração. As taxas grandes do exemplo são sintéticas, não estimativas de organismo.

## Fontes e interpretação

Charles F. Baer, IV.2 “Mutation”, *The Princeton Guide to Evolution*, p.317/PDF331: consulta textual parcial em27/10/2026. Autoria localizada no início do capítulo/PDF329; copyright2014 difere do ano2013 da referência curricular. Conceitos de mutação/seleção e população finita; não leitura integral, nova inspeção visual ou cópia de exemplos. A parametrização e ordem do ciclo foram especificadas e derivadas separadamente. A seleção contra a pode usar uma escala diferente de s: dividir todos os pesos por1+s dá peso1 para A e1/(1+s) para a; a desvantagem nessa escala é s/(1+s).

[Notas UC Berkeley — Mutation](https://ib.berkeley.edu/courses/ib162/Mutation.htm), trecho inicial sobre fluxos mutacionais parcialmente consultado; as fórmulas diploides em imagens e o estudo empírico posterior não foram analisados nem transferidos ao nosso modelo. Programa curricular não reaberto; o recorte atende parcialmente à interação entre processos, sem fechar o item11b.

## Derivação e laboratório

F(p)=(1−μ)(1+s)p/(1+sp). F(p)−p=p[s−μ(1+s)−sp]/(1+sp). Para s>0, o ponto positivo é1−μ(1+s)/s quando μ<s/(1+s). p=0 continua fixo. Para s=0, usar F(p)=(1−μ)p. Esses pontos não são uma promessa sobre trajetórias finitas.

```sh
python3 labs/mutacao-selecao/cycle.py
```

Cinco testes: exemplo e ordem, equilíbrios/diferença, contribuições ponderadas de contagens explícitas, binomial versus enumeração de todas as sequências em60 parâmetros e M1–6 (360 distribuições), normalização/média/variância e contratos. Usa frações exatas, sem semente. A grade verifica implementação e não substitui a álgebra. M≤20 é limite do laboratório, não biológico; M conta cópias haploides.

Exemplo p1/4,s1,μ1/4: p_sel2/5,F3/10,p*1/2. Em M4: média de K6/5, variância da frequência21/400 e perda em uma geração2401/10000. Na ordem inversa, frequência6/19. Exercício de interpretação propõe réplicas e fontes independentes, sem coleta real ou protocolo experimental. Evolução do genoma, diploidia, fluxo gênico e inferência empírica pendentes. Revisão pessoal ainda não feita.


## 27/10/2026 — interação: seleção, mutação e deriva num ciclo explícito

Nova `b3-mutacao-selecao`,11 seções/10 exercícios. Modelo haploide de um locus: pesos1+s/1, seleção seguida de mutação A→a sem reversão e amostragem binomial opcional. Deriva F(p), ponto positivo com domínio e contraste p=0 absorvente; s=0 tratado sem divisão. Não confunde equilíbrio determinístico com permanência de alelo em réplica finita. Exemplo p1/4,s1,μ1/4 dá2/5→3/10; ordem inversa6/19. M4: E[K]6/5, perda2401/10000 e variância da frequência21/400. Parâmetros sintéticos, sem ajuste ou dados reais.

Fontes textuais parciais em27/10/2026: PrincetonGuide, Baer IV.2 “Mutation”, p.317/PDF331; autoria localizada emPDF329, copyright2014 versus referência curricular2013 preservado. Sem nova inspeção visual/leitura integral. UC Berkeley https://ib.berkeley.edu/courses/ib162/Mutation.htm , início de fluxos mutacionais; fórmulas em imagens e estudo empírico posteriores não analisados. Ciclo, parametrização, deduções, figura e questões próprios; não se transporta o símbolo s de outra escala de aptidão sem reparametrizar. Programa curricular não reaberto.

Cinco testes em `labs/mutacao-selecao/cycle.py` aprovados: exemplo/ordem, equilíbrios/diferença, normalização de contribuições de contagens explícitas, enumeração de360 distribuições de um passo em60 parâmetros e M1–6, momentos e contratos. Frações exatas, sem semente ou trajetória aleatória inventada; testes finitos não provam dinâmica geral.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou0 e aceitou2401/10000 para perda em uma geração; documento390/390px, console sem erros observados. Figura inspecionada em `mutacao-selecao-mobile.jpg`; viewport restaurada. Windows real, leitor de tela, revisão pessoal e dados empíricos pendentes.

BiologiaIII11 aulas/130 exercícios,13 grupos parciais/três lacunas, nenhum completo. Grupo interação passou de lacuna a parcial; evolução do genoma, discussão pessoal de artigos e comunicação continuam pendentes. Global51 trilhas/575 aulas/5256 exercícios,143 introduções curtas; sem certificação de cobertura ou domínio. Próxima ação:duas sessões de20min para reconstruir a ordem do ciclo/equilíbrio e a distribuição de uma geração. Próxima elaboração global:auditar uma lacuna do percurso escolar de matemática e desenvolver o recorte após verificar referências, mantendo alternância. Saldo semanal antes/depois67%; parada operacional65% preservada.
