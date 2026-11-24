# Sistemas de duas equações — reforço escolar

27/10/2026. Material original com apoio de IA em rascunho. Revisão pessoal e uso com aluno pendentes. Não é disciplina extra do histórico nem cobertura oficial de exame/BNCC.

## Modelo e contas

Duas compras fictícias, preços adulto a e estudante e em reais por ingresso, fixos por categoria e sem taxas: 3a+2e=94, 2a+3e=86. Substituição: e=(94−3a)/2, então 4a+282−9a=172, a=22, e=14. Eliminação: 3E1−2E2 dá 5a=110. Conferência: 66+28=94 e 44+42=86; preços não negativos. (24,11) satisfaz apenas a primeira: a segunda dá 81, não 86.

A soma das equações fornece a+e=36, condição necessária mas não suficiente: (18,18) satisfaz a soma e falha no sistema. Uma troca reversível mantém uma equação e soma um múltiplo dela à outra. Multiplicar uma equação por zero não é reversível. Gráfico com retas azul contínua/preta tracejada em janela a∈[0,30], e∈[0,50], escalas e unidades explícitas. O ponto (22,14) é confirmado por contas, não precisão do desenho.

Variantes 3a+2e=94 com 6a+4e=188 ou 190: infinitas soluções ou nenhuma. No geral ax+by=r,cx+dy=s, D=ad−bc. Se D≠0, combinar equações dá Dx=dr−bs, Dy=as−cr e um único par. Se D=0, ainda é preciso olhar a compatibilidade. Linhas 0x+0y=r não são retas: são todo o plano se r=0 ou vazio se r≠0.

Domínio contextual: x+y=1,x−y=3 dá (2,−1), incompatível com contagens não negativas. x+y=1,x−y=0 dá (1/2,1/2), incompatível com contagens inteiras. Não arredondar automaticamente.

## Fontes

OpenStax, Elementary Algebra 2e: [§5.1](https://openstax.org/books/elementary-algebra-2e/pages/5-1-solve-systems-of-equations-by-graphing), solução simultânea/conferência/gráfico; [§5.3](https://openstax.org/books/elementary-algebra-2e/pages/5-3-solve-systems-of-equations-by-elimination), propriedades aditivas e eliminação. Consulta parcial em 27/10/2026. Números, contextos, provas escritas, gráfico, código e exercícios próprios; sem reproduzir problemas ou ler integralmente as seções.

## Python opcional e verificação

`systems.py` recebe duas triplas racionais (a,b,r),(c,d,s), somente int/Fraction, sem bool/float. `solve` retorna status unica/nenhuma/infinitas e ponto só no primeiro caso. None não distingue sozinho ausência de infinitude: sempre ler o status. No caso D=0, verifica coeficientes nulos e menores da matriz aumentada para classificar compatibilidade. Não parametriza a família infinita, não estima dados ruidosos e não representa todos os reais no código: exemplos/entradas racionais têm resultados racionais.

`satisfies` confere ambas as equações; `combine` troca a segunda por segunda+m·primeira, mantendo a primeira; `scale_row` exige fator não nulo. Da raiz: `python3 -m unittest discover -s labs/sistemas-duas-equacoes -t .`.

Cinco testes: 729 sistemas de coeficientes/termos −1,0,1 contra RREF independente; exemplos e domínio; operações reversíveis; conversão reais/centavos e gráfico; contratos. Não é validação de um algoritmo de álgebra numérica em float nem de todos os contextos de modelagem.

Respostas dos 12 exercícios: 22;14;81;5;5;1/2; ambas; soma perde informação; infinitas; nenhuma; D=0 exige compatibilidade; domínio também importa. Resoluções na aula.

Revisão proposta em duas sessões: montar/resolver/conferir as compras; depois comparar identidade e contradição. Python não é pré-requisito para estudar a aula. Sistemas maiores, dados aproximados, diagnóstico com aluno e revisão pessoal continuam pendentes.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 749 fórmulas MathML conferidas. A 390 px, exercício adulto rejeitou 24 e aceitou 22 pelo Enter; interpretação da soma aceita. Figura inspecionada, documento sem transbordamento horizontal e console sem erros. Revisão pessoal, uso com aluno, leitor de tela e Windows real pendentes.
