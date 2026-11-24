# Processo de Poisson — notas de aula

Aula existente aprofundada. Exemploλ=2,horizonte3, média6; sampler exponencial, desafio e IDs pp1/pp2 preservados. Rascunho original; revisão pessoal pendente.

Fonte: Pavliotis, Stochastic Processes and Applications,2014,§2.1 p.30/PDF43 eq.2.3 e definição no exercício18 de§1.7 p.25/PDF39. Consulta textual parcial em27/10/2026, cabeçalhos conferidos por extração direta. Não foi reproduzida/resolvida a questão de continuidade, nem feita nova inspeção visual ou leitura integral. Exemplar privado não distribuído. Momentos, previsão, binomial condicionada ao total e exemplos foram deduzidos nas notas; figura própria.

Incrementos disjuntos independentes, mas Cov(N(s),N(t))=λmin(s,t). Comλ=2, E[N(3)|N(1)=4]=8 e variância4. Dado N(3)=6, N(1) é Binomial(6,1/3); os blocos separados passam a ter covariância−4/3. Contagem não é estacionária; incrementos de igual duração têm a mesma lei. Tempos de evento fixados na figura são apenas ilustrativos.

Rodar na raiz: `python3 -m unittest discover -s labs/poisson-incrementos -t .`. Biblioteca padrão. Probabilidades Poisson em float por recorrência limitada aλh≤100 e k≤1000, sem garantia de erro relativo em caudas muito pequenas. Momentos/binomial condicionada usam int/Fraction. Não estima taxa, não valida dados reais ou a IC e não substitui revisão pessoal. O limite de100000 iterações do sampler antigo é orçamento, não propriedade da distribuição.

## 27/10/2026 — Poisson, incrementos e condicionamento

Aula `processo-poisson` aprofundada de3 para14 seções e2 para12 exercícios. IDs pp1/pp2, exemploλ2/horizonte3, sampler exponencial e desafio anteriores preservados. Contagem/espera, sobrevivência, convolução de incrementos, Cov(N(s),N(t))=λmin(s,t), previsão após contagem observada, binomial condicionada ao total e covariância negativa entre blocos selecionados. N(t) não estacionário separado de incrementos estacionários; pequena expansão temporal conecta saltos e equação de probabilidades. Sem estimação deλ ou validação de dados reais/IC.

Fonte: Pavliotis, Stochastic Processes and Applications,2014, §2.1 p.30/PDF43 eq.2.3 e definição no exercício18 de§1.7 p.25/PDF39, consulta textual parcial em27/10/2026. Cabeçalhos conferidos por extração direta; não transferir offset global. Questão de continuidade não reproduzida nem resolvida. Sem nova inspeção visual, leitura integral ou distribuição do livro. Figura, números, deduções, código e exercícios próprios.

Verificação:14 testes do catálogo e cinco locais aprovados;790 estruturas MathML conferidas. Probabilidades/momentos por soma truncada até700 para cinco parâmetros até100; convolução em21 totais; condicional por razão de conjuntas, distribuição binomial exata, covariância entre blocos e contratos. Domínio float explicitamente limitadoλh≤100,k≤1000, com possível arredondamento de caudas pequenas; não é pacote robusto geral. No navegador390px, covariância após fixar o total rejeitou0 e aceitou−1,333333333333 pelo Enter; N(t) não estacionário aceito. Figura inspecionada em`poisson-incrementos-mobile.jpg`, documento390px e console sem erros. Leitor de tela, Windows real e revisão pessoal pendentes.

Processos Estocásticos:25 aulas/110 exercícios,19 introduções curtas. Catálogo51 trilhas,544 aulas/4279 exercícios e201 introduções curtas. Nada declarado completo ou como domínio demonstrado. Próxima ação: reconstruir previsão8 e binomial após total6 em20min, explicando por que as informações diferem. Próximo bloco global: inspecionar lacuna de QuímicaIV e referência do acervo, preservando equilíbrio curricular. Saldo semanal81%; parada operacional65% mantida.
