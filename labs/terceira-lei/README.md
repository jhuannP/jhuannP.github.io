# Terceira lei e calorimetria

Rascunho original —27/10/2026; revisão de Jhuann pendente.

## Por que uma diferença de entropia não fixa uma referência?

Pré-requisitos: entropia como função de estado, aquecimento reversível, capacidade calorífica molar e integrais. A segunda lei permite calcular diferenças de entropia, mas uma diferença não determina sozinha o valor de referência. A terceira lei acrescenta uma condição de limite para substâncias em equilíbrio interno. O programa público de QuímicaII inclui esse tema; sua versão de 2025 é posterior ao período cursado e não comprova o conteúdo exato da sua turma ou seu domínio pessoal.

## O cristal ideal é uma hipótese, não qualquer amostra

No enunciado usual para substância pura em cristal perfeito, a entropia tende a zero quando a temperatura absoluta tende a zero. A interpretação exige o estado de equilíbrio e a organização apropriada; não se aplica automaticamente a uma amostra congelada fora do equilíbrio. Levine apresenta também o enunciado de Nernst–Simon para variações isotérmicas em equilíbrio interno. Aqui usamos o cristal de referência para construir um primeiro cálculo, sem provar a equivalência entre todas as formulações da terceira lei.

lim T→0 S_m(T)=0 (cristal ideal de referência)

## Zero de entropia não é zero de entalpia de formação

Uma entropia molar padrão S°m(T) é uma propriedade de uma substância em estado padrão e temperatura especificados. O sobrescrito padrão não fixa sozinho a temperatura em 298,15 K; informe T. A convenção de entalpia de formação padrão nula para certos elementos de referência não implica S°m=0 desses elementos em temperatura ambiente. A referência de entropia está ligada ao limite de baixa temperatura, não a zerar uma tabela inteira em qualquer T. Tampouco S→0 implica que todas as outras propriedades tenham valor zero.

## A calorimetria acumula Cp dividido por T

Numa fase de composição fixa a pressão constante, o aquecimento reversível tem δq_rev,m=Cp,m dT. Pela definição diferencial dS_m=δq_rev,m/T, segue dS_m=(Cp,m/T)dT. Portanto S_m(T₂)−S_m(T₁)=∫T₁ᵀ²(Cp,m/T)dT, sem atravessar uma transição que não tenha sido incluída. A capacidade molar tem unidade J/(mol K); dividir por T e integrar dT deixa J/(mol K).

ΔS_m=∫T₁ᵀ²(Cp,m/T)dT

## Começar em zero exige um limite

Para usar a referência S_m(0)=0, a notação ∫₀ᵀCp,m/T dT é uma integral imprópria: primeiro integre de uma temperatura positiva τ até T e depois tome τ→0⁺. É preciso conferir a convergência. Não substitua T=0 numa divisão0/0 nem suponha que uma capacidade medida em temperatura alta continue válida até zero. A referência é um limite termodinâmico, não um relato de medição realizada exatamente em 0 K.

## Um modelo sintético com capacidade cúbica

Para fazer contas verificáveis, definimos Cp,m=αT³ com α=1/500 J/(mol K⁴), no intervalo numérico0≤T≤20 K, sem transições inicialmente. É uma ilustração de um comportamento de baixa temperatura, não um ajuste de dados nem um material identificado. Levine discute capacidades cúbicas em certos sólidos não metálicos em temperaturas suficientemente baixas; isso não valida nosso coeficiente ou intervalo para uma amostra real. No modelo, Cp,m/T=αT² para T>0, com extensão contínua zero em T=0.

Cp,m/T=αT²

## Calcular a entropia também confere a convergência

A integral de αT² entre τ e T é α(T³−τ³)/3. Como τ³→0, o limite existe e S_m(T)=αT³/3 para a referência zero. Em10 K, Cp,m=2 J/(mol K), mas S_m=2/3 J/(mol K): essas propriedades têm a mesma unidade e valores distintos. Em20 K, S_m=16/3 J/(mol K), oito vezes o valor em 10 K. A potência cúbica vem da integração de Cp,m/T, não de integrar diretamente Cp,m.

S_m(T)=αT³/3

## A área da figura tem unidade de entropia

O eixo vertical mostra Cp,m/T, não Cp,m. A região sombreada vai de 0 a 10 K e tem área2/3 J/(mol K) pelo cálculo anterior. A altura final é0,2 J/(mol K²), que não pode ser confundida com a área. A curva é desenhada com valores sintéticos; não se mediu essa área em pixels ou se inferiu uma propriedade de uma substância real.

## Entropia molar e entropia total precisam de unidades distintas

Para n mols do mesmo material nas mesmas condições, S=nS_m. Em10 K, dois mols deste modelo têm entropia total4/3 J/K, enquanto a propriedade molar permanece2/3 J/(mol K). Não multiplique Cp,m por uma massa em quilogramas sem converter pela massa molar. O laboratório trabalha com grandezas molares; o exemplo de dois mols é uma conversão explícita, não um parâmetro oculto.

## Por que uma capacidade constante não serve até zero?

Se usássemos Cp,m=C>0 até temperaturas arbitrariamente próximas de zero, a integral desde τ seria C ln(T/τ). Ela cresce sem limite quando τ→0⁺, contrariando a referência finita pretendida. Uma aproximação constante pode funcionar num intervalo com T₁>0, mas não ganha validade até 0 K por extrapolação. Mesmo saber que Cp,m tende a zero não dispensa analisar a integrabilidade de Cp,m/T para a função escolhida.

## Mudanças de fase acrescentam outro tipo de contribuição

Numa transição reversível de primeira ordem em temperatura T_tr>0, a entropia molar muda em ΔH_tr,m/T_tr. Esse termo não é a área de um aquecimento contínuo que pula a mudança de fase. Para construir S de um estado final, some as integrais das fases percorridas e as contribuições das transições fornecidas. É necessário conhecer as temperaturas e entalpias adequadas à pressão do caminho; a terceira lei não fornece esses dados sozinha.

ΔS_tr,m=ΔH_tr,m/T_tr

## Uma transição hipotética mostra o termo que faltaria

Como segundo cenário sintético, forneça uma transição a 10 K com ΔH_tr,m=30 J/mol e mantenha Cp,m=αT³ nos dois ramos puros. O salto é3 J/(mol K). Imediatamente antes, S_m=2/3; imediatamente depois,11/3. Em20 K na fase de alta temperatura, a soma é16/3+3=25/3 J/(mol K). O cenário sem transição e o cenário com transição são modelos diferentes; não acrescente o salto sem declará-lo. Em10 K, informe a fase ou a fração transformada: T sozinha não escolhe entre esses estados.

## Resfriar diminui a entropia do sistema sem violar a segunda lei

No modelo sem transição, de 20 para10 K a variação molar é2/3−16/3=−14/3 J/(mol K). Essa diminuição não é, por si só, uma violação: a segunda lei exige considerar também a vizinhança e as condições do processo. A terceira lei tampouco demonstra que uma reação arbitrária é espontânea em qualquer temperatura. Entropia de reação exige composição, fases e estequiometria; espontaneidade envolve o sistema e as restrições apropriadas.

## O laboratório verifica uma integral, não certifica uma amostra

O código racional mantém Cp,m, sua razão estendida e a integral exatas no intervalo declarado. A função de transição apenas divide uma entalpia fornecida por uma temperatura positiva; não prevê fases ou latentes. O parâmetro de referência S₀ permite mostrar que diferenças não dependem de uma constante aditiva; ele não determina experimentalmente entropia residual. Equilíbrio fora do ideal, desordem congelada, graus de liberdade eletrônicos e técnicas de refrigeração precisam de tratamento específico.

## Uma sessão de vinte minutos para reconstruir a conta

Explique por que o integrando é Cp,m/T, obtenha2/3 em 10 K e converta para a entropia total de dois mols. Depois refaça o caso da transição e diga por que ele dá25/3 em 20 K. Registre sua própria justificativa e dúvidas antes de apresentar essa capacidade no portfólio. A aula é rascunho assistido por IA; não comprova domínio pessoal nem encerra a terceira lei ou a disciplina.

## Exercícios e resoluções

No modelo α=1/500 J/(mol K⁴), qual é Cp,m em 10 K, em J/(mol K)?

**Resolução:** (1/500)10³=2.

Qual é Cp,m/T em 10 K, em J/(mol K²)?

**Resolução:** 2/10=1/5.

Com referência zero e sem transição, qual é S_m(10 K), em J/(mol K)?

**Resolução:** (1/500)10³/3=2/3.

No mesmo modelo sem transição, qual é S_m(20 K), em J/(mol K)?

**Resolução:** (1/500)20³/3=16/3.

Qual é S_m(20 K)/S_m(10 K), para referência zero e sem transição?

**Resolução:** O valor varia com T³:2³=8.

Quanto vale S de dois mols em 10 K, sem transição, em J/K?

**Resolução:** 2×(2/3)=4/3 J/K.

Para a transição fornecida de 30 J/mol em 10 K, qual é ΔS_tr,m em J/(mol K)?

**Resolução:** 30/10=3.

Qual é S_m imediatamente após essa transição em 10 K, em J/(mol K)?

**Resolução:** 2/3+3=11/3.

No cenário com essa transição, qual é S_m em 20 K, em J/(mol K)?

**Resolução:** 16/3+3=25/3.

Sem transição, qual é ΔS_m ao resfriar de 20 para10 K, em J/(mol K)?

**Resolução:** S_final−S_inicial=2/3−16/3=−14/3.

Entalpia de formação padrão zero de um elemento implica entropia molar padrão zero em qualquer T?

**Resolução:** São propriedades e referências diferentes; a condição de entropia é de baixa temperatura.

Cp,m constante e positiva pode ser extrapolada até0K mantendo finita ∫₀ᵀCp,m/T dT?

**Resolução:** A integral desdeτ é C ln(T/τ), que diverge quandoτ→0⁺.

## Fontes e limites

Levine, Physical Chemistry,6ª ed., §5.7, pp.156–158/PDF174–176, consulta textual parcial em27/10. P.157/PDF175 também inspecionada visualmente: referência, integrais e transição. Os metadados da edição vêm do inventário anterior; o programa indica2009 e o arquivo/inventário2008, diferença mantida. P.158 apresenta comportamento cúbico não metálico de baixaT e limites; coeficiente1/500, intervalo e cenário de transição são inventados aqui. Extração do PDF gera avisos de fontes, com trechos usados legíveis. Sem leitura integral ou distribuição do PDF privado.

[OpenStax Chemistry2e §16.3](https://openstax.org/books/chemistry-2e/pages/16-3-the-second-and-third-laws-of-thermodynamics), consulta parcial: cristal de referência, terceira lei e propriedades padrão. Não usamos a simplificação de ausência de todo movimento como definição física de zeroK; o foco é o limite de entropia sob hipóteses. [USP CCM0124](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124) reaberto em27/10: ativação01/01/2025, item3 contém terceira lei, bibliografia Levine6/Atkins8. Versão da turma não recuperada. Fontes não certificam domínio pessoal. Exemplos, deduções, exercícios, figura e código próprios.

## Laboratório e continuidade

`python3 -m unittest discover -s labs/terceira-lei -t .` e `python3 labs/terceira-lei/calorimetry.py`. Cp e S usam grandezas molares, T em kelvin e0..20. Funções recebem int/Fraction, rejeitam bool/float. cp_over_t(0) é a extensão contínua, não divisão0/0. phase_change recebe ΔH eT>0, sem prever uma transição. Não há integrador de curva medida, modelo de refrigeração ou cálculo de entropia residual.

Cinco testes:231 intervalos contra Simpson racional exato para integrando quadrático; limite e fator8 em temperaturas divididas por2; referência e aditividade; salto fornecido e reverso; contratos. As provas da integral e de convergência estão nas notas, não se inferem de enumeração finita. Próxima revisão20min: integral, unidades e salto. Próximo recorte: diagnóstico das condições de equilíbrio/residual e eletroquímica, com fontes próprias.
