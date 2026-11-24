# Trajetória e ensemble: manter os dois índices visíveis

Modelo fictício adimensional Xₙ=Z, com um sorteio de Z em {−1,+1}, ambos de peso 1/2, por realização. A esperança em cada instante é zero, a variância é 1 e a média temporal é Z para todo N positivo. Portanto a média temporal é não enviesada, mas seu erro quadrático é 1 e P(|erro|>1/2)=1. A distribuição de todo vetor finito é invariante a translações do tempo: o modelo é estritamente estacionário e não é ergódico na média.

A figura enumera as duas trajetórias possíveis com pesos exatos. Não é uma amostra aleatória obrigada a conter ambos os sinais. Quatro realizações independentes dão variância da média igual a 1/4; quatro cópias compartilhando Z dão variância 1. Dispersão temporal nula não prova variância de ensemble nula.

No contraste Yₙ=(−1)ⁿZ, a média temporal dos N primeiros instantes é zero se N é par e Z/N se N é ímpar. A variância é zero ou 1/N². O cálculo não supõe independência. Para qualquer vetor com momentos de segunda ordem, Var(soma Xₙ/N)=soma dupla das covariâncias/N². A rotina recebe a matriz, valida forma/simetria e calcula a expressão; não valida semidefinição positiva ou ajusta uma matriz a dados reais.

Na raiz do site:

    python3 -m labs.trajetoria-ensemble.exact
    python3 -m unittest discover -s labs/trajetoria-ensemble -t .

Cinco testes verificam os eixos de médias, o desafio original, enumeração das duas trajetórias constantes para N até 40, todas as 2^M combinações independentes para M até 9, alternância para N até 30 e entradas inválidas. Nenhum simulador ou resultado científico da IC foi alterado.

Aula ampliada de três para doze seções e de dois para doze exercícios. Exemplo e desafio anteriores preservados. Preparação assistida por IA para revisão de Jhuann. Próxima revisão: desenhar a tabela e explicar por que repetir instantes da mesma trajetória não cria realizações independentes. Estimação de covariância, erro de dados reais, Browniano e teoria geral de ergodicidade continuam pendentes.

Fontes de fundamentos consultadas parcialmente em 22/10/2026: [MIT 6.432, Willsky/Wornell/Shapiro, capítulo 4](https://sia.mit.edu/wp-content/uploads/2015/04/chapter4.pdf), §4.1 (PDF4) e discussão de médias e ergodicidade (PDF74–78); [MIT 16.322, Vander Velde, Lecture 10](https://ocw.mit.edu/courses/16-322-stochastic-estimation-and-control-fall-2004/119c1f1c042eccaa717f6c9c2e9eb540_lecture10.pdf), PDF7–8. Índices de PDF contados a partir de 1, sem alegação de nova verificação das páginas impressas. A consulta foi textual e parcial; nenhum gráfico ou exercício dos materiais foi copiado. O exemplo binário, a tabela e o código foram elaborados aqui. Chorin–Hald/Pavliotis permanecem referências temáticas, não relidos neste bloco.

Verificação: cinco testes novos e 13 de catálogo aprovados; 540 estruturas MathML conferidas. Em 390 px, figura e fórmula revisadas; linha de texto matemático encurtada após detectar corte visual. Exercício da variância temporal rejeitou 1/100 e aceitou 1; nenhum erro de console observado. Prévia: trajetoria-ensemble-mobile.jpg. Não houve revalidação global dos simuladores. Catálogo: 501 aulas/3088 exercícios em rascunho; nenhuma disciplina concluída. Saldo semanal após bloco: 92%; parada em 65%. Próximo bloco editorial: desenvolver covariância temporal e separar essa base da hipótese de previsão linear; revisão pessoal desta aula segue pendente.
