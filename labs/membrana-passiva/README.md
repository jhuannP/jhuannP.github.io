# Membrana passiva: balanço elétrico e correntes iônicas

22/10/2026. Aula b4-membrana-passiva,14 seções/12 exercícios. Texto, parâmetros e esquema originais com apoio de IA, em rascunho para revisão de Jhuann. Não é medida pessoal, experimento ou simulação de potencial de ação.

## Do equilíbrio de Nernst ao circuito efetivo

V=V_interno−V_externo em mV. Correntes iônicas convencionais positivas para fora; corrente aplicada I positiva para dentro. Para K+ e Na+ isso corresponde ao sentido dos próprios cátions. Icap=C dV/dt é saldo capacitivo, não transporte de íons pelo isolante.

Ramos efetivos: I_K=g_K(V−E_K), I_Na=g_Na(V−E_Na), com g em nS, E e V em mV e correntes em pA. São condutâncias ôhmicas constantes, não permeabilidades de Goldman. Potenciais de reversão mantidos fixos representam reservatórios; não se calcula a concentração ou sua evolução. Uma espécie sem ramo condutor pode ter corrente zero sem V ser seu equilíbrio.

Conservação de carga: I=I_K+I_Na+C dV/dt. G=g_K+g_Na>0; C total em pF, não por área. V∞=(g_KE_K+g_NaE_Na+I)/G, τ=C/G em ms. A solução para parâmetros constantes é V(t)=V∞+(V0−V∞)exp(−t/τ).

Com I=0 o valor estacionário é média dos E pelas condutâncias. Isso não é Goldman; com I não nulo a soma iônica estacionária é I e V∞ pode ficar fora dos dois E.

## Exemplo original

E_K=−90mV,E_Na=+60mV,g_K=4nS,g_Na=1nS,C=100pF,V0=−80mV,I=0.
G=5nS,V∞=−60mV,τ=20ms.
No estado estacionário: I_K=+120pA,I_Na=−120pA, soma0. A membrana não acumula carga líquida, mas as espécies transportam matéria/carga em sentidos opostos. Em célula real, manter gradientes requer processos energéticos; bombas podem também fornecer corrente direta. Nenhum desses processos ou gastos é calculado. O esquema correntes-opostas.svg é próprio.

Inicialmente: I_K=40pA,I_Na=−140pA, soma−100pA. Icap=+100pA e dV/dt=+1mV/ms. Em20ms, V=−60−20/e≈−67,35759mV, ainda longe do limite exato. I=25pA, com demais parâmetros fixos, desloca V∞ em5mV; não gera disparo neste modelo.

Unidades: nS*mV=pA; pF/nS=ms; pF*(mV/ms)=pA. Não se misturam condutâncias totais com capacitância por área.

## Laboratório

Na raiz do site, biblioteca padrão:
    python3 -m labs.membrana-passiva.experiment
    python3 -m unittest discover -s labs/membrana-passiva -t .

stationary usa int/Fraction não negativos para condutâncias, soma positiva, C positivo, corrente aplicada com sinal. Retorna estado estacionário racional. transient exige tempo não negativo e condição inicial racional; avalia exponencial em ponto flutuante. Rejeita bool/float na interface Python. Não é integrador numérico ou solver de canais ativos.

Cinco testes: estado e derivada inicial, comparando V(τ) também com Decimal de50 dígitos;135 estados estacionários por balanço, limites e ramos individuais;144 estados transientes por resíduo, derivada central e composição temporal; escalas e capacitância; contratos. A composição usa conversão explícita da tensão arredondada para Fraction como condição inicial; não afirma exatidão da exponencial.

reference.json registra81 trios/tempos com resultados analíticos numéricos para comparar JavaScript. O painel usa C,V0,E fixos acima e quatro controles(g_K,g_Na,I,t). A curva é analítica, com eixo t em ms e V em mV, escala vertical adaptativa, valor estacionário tracejado e marcador. Não usa Euler, limiar/reset, Goldman ou Hodgkin–Huxley. Normaliza zero para evitar−0 nas correntes de ramos fechados.

## Fontes e seleção curricular

Bear e colaboradores, Neurociências: Desvendando o Sistema Nervoso, quarta edição Artmed2017: consulta textual parcial ao capítulo3 pp.72–73/PDF114–115 sobre repouso multi-iônico/permeabilidades e Goldman. Essa leitura dá contexto e diferenças; os valores da aula não são copiados do livro e seu quadro não foi reproduzido. Não houve nova renderização ou leitura integral do capítulo.

Gerstner e colaboradores, Neuronal Dynamics, edição online:
https://neuronaldynamics.epfl.ch/online/Ch1.S3.html
Consulta parcial em22/10/2026 a §1.3.1, circuito passivo, conservação de corrente e escala RC. Não incorporamos o mecanismo de disparo/limiar/reset da parte seguinte. A extensão em dois ramos ôhmicos é uma escolha efetiva própria, com limites declarados.

CCM0221:
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221
Programa aberto em22/10/2026, retorno da ferramenta com captura de dois meses antes. Ativação01/01/2025; seleção de sistemas efetivamente ministrada não confirmada. Aprovação2026/1 mantém a fonte pessoal já registrada, sem nova inspeção do PDF. A fonte lista sistemas possíveis; esta aula não comprova que o recorte foi ministrado ou dominado por Jhuann.

## Continuidade

Revisão pessoal: explicar sinais, correntes opostas, limite e tempo; separar ramo fechado de equilíbrio. Próximo conteúdo curricular: Goldman, canais ativos e comunicação sináptica mediante fontes específicas. Estoques finitos, bombas, glia e organização sistêmica seguem sem modelo integrado. BiologiaIV: seis aulas/70 exercícios, quatro grupos parciais/dezoito lacunas; nenhum completo ou competência pessoal certificada.
