# Calor e temperatura: balanço com recipiente

22/10/2026. Aula ef-calor ampliada de3 seções/2 exercícios para14/12. Conteúdo, números, diagrama e código originais com apoio de IA, em rascunho para revisão de Jhuann. Percurso de reforço escolar, sem equivalência com disciplina adicional do histórico. Python é opcional, não requisito para resolver os exercícios.

## Pergunta e modelo

Dois corpos em contato térmico chegam a uma temperatura uniforme. O sistema contém ambos e, quando incluído, o recipiente. Capacidades constantes e positivas para os corpos; recipiente pode ter capacidade zero como aproximação que o despreza. Sistema adiabático ideal; sem trabalho, mudança de fase, reação, perdas ao ambiente ou contribuição de energia de mistura. Não se calcula o tempo de equilíbrio.

Calor é transferência por diferença de temperatura, não uma substância armazenada. Capacidade do corpo C=mc é distinta do calor específico por unidade de massa. Com C em kJ/K, temperaturas em °C e Q em kJ, Qi=Ci(Tf−Ti): positivo para quem recebe, negativo para quem cede. Diferença de1 °C tem mesmo valor numérico de1 K; temperaturas absolutas não são iguais nas duas escalas.

Somar Q1+Q2+Qrec=0 produz Tf=(C1T1+C2T2+CrecTrec)/(C1+C2+Crec). Os pesos somam1, permitindo usar qualquer escala afim consistente. O produto C*T em Celsius não é, por si, energia interna absoluta; a derivação vem das diferenças. Tf fica nos extremos dos participantes com capacidade positiva. Só essa verificação não comprova as hipóteses físicas.

## Exemplo original

C1=1,C2=2,Crec=1 kJ/K, temperaturas80,20,20 °C. Tf=140/4=35 °C; transferências−45,+30,+15 kJ, soma zero. Capacidades didáticas, sem identificação de material ou medidas reais. Desprezar o recipiente daria40 °C. Não usar a tabela de calor específico de um material sem verificar suas condições.

O primeiro exemplo antigo de capacidades iguais,20 e60 °C sem recipiente, continua na aula. O painel preserva seu estado inicial:40 °C. Ao incluir recipiente de1 kJ/K a20 °C, mantendo as duas capacidades em1, chega a100/3 °C. Alterar Trec com Crec=0 não altera resultado.

## Executar e conferir

Na raiz do site, biblioteca padrão:
    python3 -m labs.mistura-termica.experiment
    python3 -m unittest discover -s labs/mistura-termica -t .

mix(C1,C2,T1,T2,Ccal=0,Tcal=20) retorna Tf e transferências assinadas. Python aceita int/Fraction, rejeita bool/float, capacidades inválidas e temperaturas Celsius abaixo de−273,15. O modelo não identifica material ou fase; aceitar um número negativo em Celsius não afirma que se trata de água líquida. Temperatura do recipiente é validada mesmo quando sua capacidade é nula.

Cinco testes: exemplo e recipiente desprezado;729 estados por conservação, limites e energia relativa a uma referência de20 °C; deslocamento uniforme da escala e multiplicação das capacidades; permutação dos dois corpos e equilíbrio inicial; contratos. O deslocamento uniforme é invariância algébrica de uma escala afim, não teste físico de constância de c em outro intervalo.

reference.json contém216 estados racionais convertidos a números para comparar com JavaScript. schoolphysics-models.js mantém mix com quatro argumentos e acrescenta os opcionais do recipiente; o retorno inclui Qcal. Entradas JS devem ser números finitos, capacidades válidas e temperaturas acima do zero absoluto. Painel schoolHeatMix ganha controles de capacidade/temperatura do recipiente, comparação com a aproximação sem recipiente e tabela dos três balanços. Estilos móveis restritos a esse painel.

## Fontes

Consulta parcial em22/10/2026:
- OpenStax Physics §11.2, https://openstax.org/books/physics/pages/11-2-heat-specific-heat-and-heat-transfer : definições, calor específico/capacidade e diferenças de temperatura.
- OpenStax College Physics2e §14.2, https://openstax.org/books/college-physics-2e/pages/14-2-temperature-change-and-heat-capacity : hipóteses de Q=mcΔT e balanço de dois corpos.

Extensão algébrica para três participantes, exemplo35 °C, exercícios, código e balanco-calor.svg são próprios. Não foram reproduzidas figuras, atividades, tabelas ou resoluções das fontes; nenhum experimento físico foi realizado. A consulta não prova leitura integral ou domínio pessoal.

## Pendências

Revisão pessoal: explicar sistema e sinais, reconstituir35 °C e comparar com40 °C sem recipiente. Mais tarde: mudanças de fase e outras contribuições energéticas, modelos de transferência temporal e verificação experimental apropriada. A trilha escolar tem sete recortes desenvolvidos e quatro introduções curtas; nenhuma área completa ou capacidade docente certificada.

Verificação do bloco:874 testes Python aprovados;501 estruturas MathML conferidas. Suíte JavaScript aprovada com285 demonstrações/855 cenários básicos, além de216 estados de mistura comparados ao cálculo racional e contratos. No navegador: capacidade do recipiente1 kJ/K altera a previsão40 para100/3 °C no estado inicial; capacidade zero torna sua temperatura irrelevante, inclusive ao alterá-la para80 °C. Resposta100/3 aceita no exercício10. Diagrama e painel inspecionados a390px, sem transbordamento horizontal ou erros de console observados; viewport restaurado. Prévia mistura-termica-mobile.jpg. Catálogo494 aulas/2802 exercícios;287 introduções com até três seções. Revisão pessoal e uso com aluno pendentes. Próxima revisão: justificar sinais e recalcular35 versus40 °C. Próximo preparo global: conferir lacunas de Química II antes de selecionar um recorte. Saldo semanal96%; parada operacional65%.
