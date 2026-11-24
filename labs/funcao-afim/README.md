# Função afim — exploração opcional

Rascunho original, 16/10/2026. Teoria e exercícios escolares não exigem Python.
Execute experiment.py com Python 3. Na raiz do protótipo:
python3 -m unittest labs.funcao-afim.test_experiment.

f(x)=ax+b, a real incluindo zero; contradomínio R. Domínio R ou [0,+∞).
O painel preserva o identificador linear, os controles a/b e o ponto (0,b).
O render antigo foi substituído. P/Q têm valores só se pertencerem ao domínio.
Pontos coincidentes têm taxa indefinida. Zero algébrico fora do domínio não é
zero da função restrita. Constante zero: todos; constante não nula: nenhum.

Azul: gráfico válido e P/Q. Círculo preto: intercepto. Tracejado: variações.
Janela x de -3 a 3, y de -12 a 16, sem interpretação do ângulo visual;
o limite da janela não termina a função. Nenhum dado real foi ajustado.
affine calcula a expressão algébrica; model respeita o domínio selecionado.
preco preserva o exemplo de entrega, hipotético, 6 reais + 2 reais/km.

Quatro testes: 375 pares avaliados por diferença racional (300 recuperam
coeficientes, 75 coincidentes rejeitados); 324 avaliações comparadas com
interpolação baricêntrica independente; domínio, zeros, monotonicidade,
conversão de unidades e mudança de origem. 72 configurações JS/Python,
com verificações de taxa e zeros. Não é validação didática com alunos.

Fonte parcial: [OpenStax Algebra and Trigonometry 2e, 4.1](https://openstax.org/books/algebra-and-trigonometry-2e/pages/4-1-linear-functions),
trechos de representações, taxa/intercepto e crescimento, 16/10/2026.
O texto inglês chama ax+b de linear function; aqui usamos convenção afim,
com a=0 permitido e primeiro grau apenas se a≠0. Nenhum exemplo ou exercício
do livro foi reproduzido. Busca nominal por Iezzi/Fundamentos no acervo não
identificou candidato; não prova ausência e não é inventário bibliográfico
completo. O apoio usado está publicamente acessível no OpenStax.

Pendentes: problemas integradores adicionais, planos de aula, funções por
partes, composição/inversa em sequência própria e revisão pessoal de Jhuann.
