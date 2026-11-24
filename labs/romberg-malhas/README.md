# Romberg: malhas aninhadas, hipóteses e falsa convergência

Laboratório original de aritmética racional;preserva a rotina float anterior da aula como recurso separado. `trapezoid_column(f,a,b,levels)` usa malhas n=1,2,4,…,a<b,1…10 níveis. Entradas e retornos do callback int/Fraction;bool,float,texto rejeitados. Função determinística,finita em todos os nós,sem singularidade avaliada;essas hipóteses de avaliação não garantem regularidade do integrando. Integrais prescritas em[0,1],grandezas adimensionais. Para dados dimensionais,trapézio tem unidade do integrando×coordenada.

T_2n=T_n/2+h_novoΣ f(a+(2i−1)h_novo). Reutiliza a soma anterior e avalia só nós novos,não mantém cache genérico de todos os valores. Cinco níveis:17 avaliações distintas em vez de36 quando todas as regras são refeitas. `extrapolate(column)` monta tabela triangular índice0;colunaj usa4^j−1. Não checa se a coluna vem de malha apropriada nem se uma expansão é válida. `romberg` combina as duas funções,não implementa parada automática por tolerância nem retorna erro certificado. O limite10 é operacional didático;rotina anterior tem seu limite12 preservado.

Exemplos:
- x²:preservadoT1=1/2,T2=3/8,R11=1/3.
- x⁴:I1/5,T(h)=I+h²/3−h⁴/30. R11=5/24,R21=77/384,R22=1/5 exato emQ. Primeira extrapolação removeh²;segunda removeh⁴. Expansão genérica de erro deve ser entendida como truncada/assintótica,não série infinita necessariamente convergente.
- |x−1/5|:I17/50. No intervalo que contém a quina,erro do trapézio=h²θ(1−θ),θ=fração de(1/5)/h. Em malhas diádicas θ=1/5,2/5,4/5,3/5,… e o coeficiente alterna4/25,6/25,… . Não há coeficiente único para extrapolarh². R22=149/450,diferente de17/50.
- cos(16πx):I0 analiticamente,n1/2/4/8 amostram apenas1. Toda tabela dos quatro primeiros níveis é1;diferenças diagonais0 enquanto erro1. Emn16,trapézio0;diagonalR44=−325651/722925≈−0,45046305,não0,pois ainda mistura regras grosseiras. Suavidade não assegura que primeiras malhas resolvam as oscilações ou estejam no regime assintótico.

`cosine_coarse_samples` é oráculo parcial de valores exatos cos(16πx) somente nos nós diádicos até n16 no intervalo[0,1]:16x inteiro→(−1)^(16x). Rejeita outros pontos,por exemplo1/32. Não é implementação contínua de cosseno nem método para avaliar malhas posteriores. A figura usa math.cos para traçar a função,pontos do experimento computacional são analíticos. Não se inferem integral ou frequência de dados;ambas foram prescritas.

Roteiro:derive a recorrência,reproduza a tabela de x⁴,compare quina ealias,e separe diagnóstico numérico de cota de erro. O exemplo suave de alias mostra que mesmo estabilidade perfeita e suavidade não certificam uma quadratura finita sem informação quantitativa adicional. Limites rigorosos exigem hipóteses e constantes apropriadas;nenhuma nova regra universal de parada é proposta. Frações eliminam arredondamento destes dados racionais,mas não erro de modelo/integração. Custo de bits de racionais não é constante;sem benchmark de desempenho.

Da raiz:
```
python3 labs/romberg-malhas/nested.py
python3 -B -m unittest discover -s labs/romberg-malhas -t .
```
Seis testes:coluna aninhada versus regra direta em dois intervalos/7 níveis e65 avaliações únicas cada;20 pares coluna/grau comparados a integrais monomiais;expansão quártica e colunas;quina por erro geométrico exato;alias analítico e conferência floatcos nos nós grosseiros;contratos. Não valida pedagogia ou domínio deJhuann.

Fontes consultadas parcialmente29/10/2026:Burden,Faires,Burden,AnáliseNumérica,tradução da10ªedição norte-americana,3ªbrasileira2016,§4.5 pp234–237/PDF248–251,corpo visualmente inspecionado para expansão,fatores,indexação,reuso. Livro começa índices1;esta aula/lab mantêm0,por isso4^j−1 corresponde ao4^(j−1)−1 do livro. Fórmulas gerais são padrão;exemplos,contraexemplos,figura e código deste laboratório próprios. Exemplosin do livro não copiado nem usado como atividade. SumárioPDF12/p.xiv conferido;tentativa de extração textual sem corpo útil por ser digitalização. PDF privado não distribuído.
ProgramaCCM0218 reaberto noportal oficial,ativação01/01/2011,compatível temporalmente mas sem provar versão ministrada2024/2;edição oficialBurden7ª2000 distinta da10ªescolhida porJhuann.
https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0218
ProgramaMAP2220 reaberto,ativação01/01/2027 posterior à aprovação2025/2;referência2016 agora nominalmente coincide com exemplar,sem comprovar programa da turma. Romberg explícito noitem3. Mesma aula compartilhada,sem duplicação.
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=MAP2220

Rascunho assistido porIA para revisão pessoal. Sem integração adaptativa implementada aqui,teorema geral deEuler–Maclaurin provado,erro certificado ou medições físicas.
