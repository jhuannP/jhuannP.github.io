# Reações consecutivas: intermediário e aproximações

27/10/2026. Notas de aula originais com apoio de IA,14 seções/12 exercícios em rascunho. Revisão pessoal de Jhuann pendente. Modelo e dados sintéticos, sem reação experimental identificada, ajuste ou experiência laboratorial comprovada.

## Hipóteses e solução

A→I→P, duas etapas irreversíveis de primeira ordem, constantes positivas k1,k2 em min⁻¹. Volume/temperatura constantes, bem misturado, fechado, sem outras reações. A0>0,I0=P0=0 em uma unidade comum de concentração (mmol/L nos exemplos). Estequiometria1:1. Não se infere lei cinética automaticamente da equação global.

A′=−k1A, I′=k1A−k2I, P′=k2I. Somar dá A+I+P=A0. Esse inventário de unidades de espécie não é conservação universal do número de moléculas de qualquer reação. A eP sozinhos não somam A0 enquanto I acumula.

A=A0exp(−k1t). Multiplicar I′+k2I=k1A0exp(−k1t) por exp(k2t), integrar e aplicar I0=0 dá

I=A0k1[exp(−k1t)−exp(−k2t)]/(k2−k1), se k1≠k2.

P=A0−A−I. Para taxas iguais k, derivar diretamente dá I=A0kt exp(−kt) e P=A0[1−(1+kt)exp(−kt)]. A divisão0/0 da fórmula não descreve singularidade física. Diferença de exponenciais próximas em float também exige cuidado; no comparador dos testes usa-se expm1 para a diferença relativa, em escalas moderadas. Não se oferece uma biblioteca analítica de precisão arbitrária para tempos extremos.

Máximo do intermediário: tmax=ln(k2/k1)/(k2−k1) para taxas distintas; nas iguais tmax=1/k,Imax=A0/e. Derivada nula no pico não torna o intermediário constante. Em A0=1,k=1,t=1, concentrações A=I=1/e eP=1−2/e≈0,264241 mmol/L. No início,I′=1 eP′=0 nas unidades dadas.

## Quase estacionário e transiente

Se k2≫k1, aproximar formação/remoção de I fornece Iqs=(k1/k2)A eP′≈k1A após o transiente. Não é equilíbrio termodinâmico nem uma afirmação de I exatamente constante. Iqs(0)>0 entra em conflito com I0=0: aproximação não válida uniformemente desde o início.

Para r=k2/k1>1:

I/Iqs=[r/(r−1)]·[1−exp(−(r−1)k1t)].

No regime tardio, a razão tende a r/(r−1), e o erro relativo tardio de Iqs em relação ao exato é1/r. Em r=10,razão10/9 e erro10%; em k1t=1,razão≈1,11097. A comparação é analítica do modelo, sem chamar esses números de limites universais para qualquer mecanismo.

Conhecer A(t) exponencial não prova mecanismo único ou existência de I. Molecularidade pertence a etapa elementar; ordem pertence à lei assumida/observada. Reações reversíveis/paralelas, etapas bimoleculares, teorias de colisão/estado de transição e inferência experimental permanecem pendentes.

## Laboratório e contratos

`chain.py` integra as três EDOs por RK4 com h·max(k1,k2)≤max_step, padrão0,05 e máximo0,25. Parâmetros int/float finitos, sem bool; k1,k2,A0 positivos, tempo não negativo. Mais de100000 passos são rejeitados antes de executar. Instantes não são medidas experimentais. Resultado imutável inclui concentrações, passos e erro de inventário. Estados não finitos ou negativos provocam diagnóstico em vez de truncamento silencioso. Escalas extremas podem perder precisão ou falhar; não é solver de produção/rigidez geral.

Esse controle de passo é operacional, não certificado de erro. Volumes e temperaturas não são inferidos; mudar min para s requer dividir as constantes por60 e multiplicar o tempo por60. Quantidades requerem volume; taxas têm unidade concentração/tempo.

Da raiz: `python3 -m unittest discover -s labs/reacoes-consecutivas -t .`.

Cinco testes:60 estados comparados à solução exata (taxas iguais/distintas/quase iguais e escalas moderadas), não negatividade e inventário; pico; transiente e razão exata da aproximação; refinamento de quarta ordem e mudança de unidades/escala; contratos e orçamento de passos. Referência analítica é independente do RK4; comparações e refinamento não provam erro certificado para todo parâmetro ou validação química do mecanismo.

## Fontes e edição

Ira N. Levine,Physical Chemistry,6th ed.,McGraw-Hill2009. Exemplar privado identificado anteriormente; o nome do arquivo diz2008, mas páginas editoriais confirmam2009. Consulta parcial em27/10/2026: §16.3 pp.524–525/PDF542–543 e §16.6 p.534/PDF552 para consecutivas/quase estacionário. p.525/PDF543 inspecionada visualmente para equações; gráficos embutidos ficaram escuros nessa renderização e não foram usados como evidência visual. Não houve leitura integral. Redação, caso de taxas iguais, parâmetros, gráfico e comparações adicionais próprios; não se reproduzem exemplos, problemas ou figuras do livro.

CCM0124: mapa existente com ativação2025 posterior à turma2024/1; versão ministrada não recuperada. Item9 inclui mecanismos e catálise, agora com recorte próprio, mantendo apoios enzimáticos de BiologiaI. Programa e histórico não reabertos neste bloco. Quinze grupos ainda parciais. Livro e capturas privadas não distribuídos.

## Exercícios e revisão

Respostas dos12 itens:1;1;0;1;1/e;1−2/e;0,1;10/9; aproximação de fluxos não é equilíbrio; equação global não determina ordem; um pico não implica quase estacionário; uma curva exponencial não prova mecanismo único. Dicas e resoluções completas na aula.

Duas sessões de20min propostas: derivar balanços e taxas iguais; depois comparar pico, transiente e aproximação. Dúvidas e avaliação pessoal permanecem em branco. Conteúdo preparado não certifica domínio, autoria independente ou experiência de pesquisa de Jhuann.

Conferência da entrega: cinco testes locais e14 de catálogo aprovados;730 estruturas MathML verificadas. Em390px, exercício11 rejeitou justificar quase estacionário por um único máximo e aceitou a distinção pelo Enter. Gráfico inspecionado; sem transbordamento ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes. Saldo semanal85%, parada65%.
