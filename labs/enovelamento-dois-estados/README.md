# Enovelamento em dois estados — notas originais

16/10/2026. Rascunho para revisão pessoal.

## Uma proteína tem uma sequência e muitas conformações

Proteínas são cadeias de aminoácidos que podem assumir diferentes conformações em interação com o solvente. Enovelamento envolve a organização estrutural da cadeia. Uma sequência não é uma forma geométrica única e imóvel; estrutura e função dependem do sistema e das condições. Esta aula não calcula a estrutura a partir da sequência.

## Dois estados são uma redução da descrição

F representa o conjunto enovelado, e U, o conjunto desenovelado. U pode conter muitas conformações, não uma cadeia sempre reta. O modelo assume que esses dois conjuntos bastam para representar as populações de equilíbrio nas condições estudadas. Intermediários estáveis, agregação, irreversibilidade ou múltiplos domínios podem exigir outra descrição.

## Fixe o sentido da diferença de Gibbs

Escrevemos F⇌U e definimos ΔG°=G°_U−G°_F como diferença padrão molar de desenovelamento. Se ela é positiva, F é favorecido; se negativa, U é favorecido. Trabalhamos a pressão fixa, solução ideal diluída e espécies de mesma composição, sem associação entre moléculas. Entropia conformacional e solvente já estão incluídos na energia livre efetiva; não acrescente outra degenerescência sem reconstruir o modelo.

## A razão de populações vem do equilíbrio

Para F⇌U ideal 1:1, K=a_U/a_F=p_U/p_F no equilíbrio, com mesma normalização de atividade. A relação termodinâmica é lnK=−ΔG°/(RT). Use R em kJ mol⁻¹ K⁻¹ se ΔG° estiver em kJ/mol; usar 8,314 sem converter kJ para J altera o expoente por fator mil. K é adimensional e T é temperatura absoluta.

## Normalizar a razão produz as duas frações

Como p_F+p_U=1 e p_U=Kp_F, p_U=K/(1+K)=1/[1+exp(ΔG°/(RT))] e p_F=1−p_U. Em ΔG°=0 as frações são 1/2. Essa normalização não atribui metade a qualquer proteína em qualquer temperatura.

## Uma curva térmica precisa de uma hipótese adicional

Adotamos ΔCp=0: as diferenças molares de entalpia e entropia de desenovelamento são constantes na faixa do modelo. Defina T_m pela igualdade de populações, com ΔG°(T_m)=0. Então ΔS°=ΔH_m/T_m e ΔG°(T)=ΔH_m(1−T/T_m). Esta aula exige ΔH_m>0; aquecer favorece U nesse modelo.

## O ponto médio não depende da altura da entalpia

Em T=T_m, ΔG°=0, K=1 e as frações são iguais para qualquer ΔH_m positiva. Mudar ΔH_m mantendo T_m muda a nitidez da transição, pois também muda ΔS°=ΔH_m/T_m. Não é uma alteração isolada da entalpia com entropia mantida. Para ΔH_m=120 kJ/mol e T_m=300 K, ΔS°=0,4 kJ mol⁻¹ K⁻¹, ou 400 J mol⁻¹ K⁻¹.

## A inclinação permite uma verificação independente

Com ΔCp=0, lnK=ΔH_m/R·(1/T_m−1/T), de modo que dlnK/dT=ΔH_m/(RT²)>0. Derivando a fração, dp_U/dT=p_Up_F ΔH_m/(RT²). No ponto médio, isso reduz a ΔH_m/(4RT_m²). Comparar essa inclinação com uma diferença finita testa a curva sem apenas repetir a expressão de p_U.

## O sinal observado precisa de um modelo de leitura

Imagine um sinal sintético com valor 1 para F e 0 para U e resposta média linear. O sinal médio será p_F, não necessariamente p_U. Sinais reais podem ter linhas de base dependentes de T e respostas diferentes por estado. Uma curva sigmoidal sozinha não demonstra que só existem dois estados; observáveis distintos, reversibilidade e controles são evidências adicionais necessárias.

## Equilíbrio não exige ΔG° igual a zero em toda temperatura

A energia livre de reação na composição atual é Δ_rG=ΔG°+RT lnQ. No equilíbrio, Q=K e Δ_rG=0, mesmo quando ΔG° não é zero. Para a mistura ideal, por mol total, G relativo a F pode ser escrito xΔG°+RT[x ln x+(1−x)ln(1−x)], com x=p_U. Sua derivada zera na mesma população calculada; a curvatura é positiva no intervalo interior. T_m é apenas o ponto de populações iguais.

## Uma curva de equilíbrios não é uma trajetória temporal

Cada ponto do gráfico corresponde a outro equilíbrio em outra temperatura, com pressão e parâmetros declarados. Não há relógio, taxas ou tempo de relaxação. Se uma experiência aquecer mais rápido que o sistema relaxa, apresentar histerese ou agregação, este modelo pode falhar. Duas proteínas com a mesma curva de equilíbrio podem ter tempos de enovelamento diferentes.

## A aproximação tem limites físicos e numéricos

ΔCp=0 ignora dependências importantes de entalpia/entropia e não descreve desenovelamento pelo frio. Não há pH, desnaturante, chaperonas, sequência ou interações explícitas. A demonstração usa parâmetros sintéticos e não confirma estabilidade de uma proteína real. O código calcula os dois pesos por ramos com expoentes não positivos para evitar estouro; arredondamento a 0 ou 1 não prova impossibilidade física do outro estado.

## Resoluções

Para ΔH_m=120 kJ/mol e T_m=300 K, qual ΔS° em kJ mol⁻¹ K⁻¹?

120/300=0,4 kJ mol⁻¹ K⁻¹.

Com esses parâmetros, qual ΔG° de desenovelamento a 330 K, em kJ/mol?

120(1−330/300)=−12 kJ/mol.

Com esses parâmetros, qual ΔG° a 270 K, em kJ/mol?

120(1−270/300)=12 kJ/mol.

Em T=T_m, qual fração p_U? Aceita fração.

ΔG°=0 ⇒ K=1 ⇒ p_U=1/2.

Se lnK=ln3, qual p_U?

K=3 ⇒ p_U=3/(1+3)=3/4.

Se p_U=3/4 e o sinal vale 1 em F e 0 em U, qual sinal médio?

S=p_F=1−3/4=1/4.

U representa necessariamente uma conformação única e reta?

O macrostado agrupa configurações; dois macrostados não significam duas geometrias únicas.

No equilíbrio a uma temperatura diferente de T_m, ΔG° precisa ser zero?

A contribuição RT lnQ compensa ΔG° quando Q=K.

A curva de fração versus temperatura informa o tempo de enovelamento?

Ela compara equilíbrios, sem taxas ou escala de tempo.

Este modelo com ΔCp=0 comprova a estabilidade térmica de uma proteína real?

É uma construção sintética; são necessários dados e verificação das hipóteses para uma proteína específica.

## Roteiro e evidência

Derive a razão de populações; normalize; confira o ponto médio; compare as curvas com ΔH_m=40 e 200 kJ/mol no mesmo T_m. Explique quais parâmetros mudam juntos. Escreva por que uma curva de equilíbrio não dá uma taxa. Produto de estudo: uma resolução própria e um gráfico anotado, sem atribuir valores a proteína real.

O laboratório tem quatro testes: normalização/partição independente, mínimo de Gibbs da mistura, monotonicidade/inclinação e contratos. Há 45 combinações físicas nos testes de partição e três curvas verificadas de 260 a 400 K; o arquivo reference.json reúne 45 combinações T/T_m/ΔH para comparação com JavaScript. Rode a suíte na raiz com `python3 -m unittest discover -p 'test_*.py'`. Estados exponencialmente pequenos podem arredondar a zero em precisão finita; não interpretar como impossibilidade física.

## Fontes e limites

[USP CCM0121](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121): item I.3, consulta 16/10/2026, programa ativado em janeiro/2025. [Zwanzig, PNAS 1997](https://pmc.ncbi.nlm.nih.gov/articles/PMC19262/), consultado diretamente em 16/10/2026, sustenta o cuidado com macrostados que agrupam conformações e com a passagem de descrições de equilíbrio a cinéticas. Não foram reproduzidas as equações de taxa ou parâmetros do artigo. A curva aqui é derivada de ΔG°=ΔH°−TΔS° e da hipótese própria ΔCp=0, não apresentada como ajuste de Zwanzig ou resultado da IC.

[MIT OCW, Thermodynamics of Biomolecular Systems](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/) foi consultado como contexto de ensino; a página do curso não é tratada como validação dos parâmetros. Bibliografia privada permanece no mapa, sem cópia dos PDFs. Pendentes: estrutura molecular detalhada, modelos com ΔCp, dados, reversibilidade, intermediários e mecanismos. Execução/revisão pessoal não presumida.
