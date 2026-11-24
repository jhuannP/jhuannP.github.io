# Mínimos quadrados: previsão, resíduo e identificabilidade

22/10/2026. Aula al-minimos-quadrados ampliada de3 seções/2 exercícios para14/12. Material original com apoio de IA, em rascunho para revisão de Jhuann. O primeiro exemplo constante com dados(1,2,6) permanece disponível; o novo exemplo afim é distinto.

## Critério e prova

A tem n linhas/p colunas; y em R^n contém observações e θ em R^p os coeficientes. A melhor previsão permitida está em Im(A). O critério é J(θ)=||Aθ−y||² com pesos iguais. Resíduo adotado: r=previsão−observado, conservando a convenção do primeiro exemplo. Trocar o sinal não muda norma ou ortogonalidade.

A projeção única de y no espaço de colunas caracteriza o mínimo. Resíduo ortogonal a cada coluna equivale a A^Tr=0 e A^TAθ=A^Ty. Para uma perturbação δ:
J(θ+δ)=||r+Aδ||²=||r||²+2δ^TA^Tr+||Aδ||².
No ajuste normal, o termo cruzado é zero; sobra um acréscimo não negativo. Necessidade: uma componente não nula de A^Tr permitiria reduzir o objetivo com pequena perturbação de sinal oposto.

A previsão ótima é única. Os coeficientes são únicos se e somente se ker(A)={0}, isto é, as colunas são independentes. Posto deficiente não impede a melhor previsão; impede identificar todos os coeficientes. Não inverter automaticamente A^TA.

## Exemplo original reconstruível

Dados adimensionais x=(0,1,2), y=(1,2,2); modelo a+b*x. Linhas de A:(1,0),(1,1),(1,2).
A^TA tem linhas(3,3),(3,5); A^Ty=(5,6).
Equações3a+3b=5 e3a+5b=6 dão b=1/2 e a=7/6.
Previsões(7/6,5/3,13/6); resíduos(1/6,−1/3,1/6).
Soma r=0 e soma x*r=0; SSE=1/6.
Perturbar a por h e b por k aumenta SSE em3h²+6hk+5k². As colunas entre si não são ortogonais; o resíduo é ortogonal a ambas.

Se x=(1,1,1), a previsão ótima para o mesmo y é5/3 em cada linha e SSE=2/3. Qualquer par a+b=5/3 é minimizador. O laboratório escolhe a=5/3,b=0, não uma solução de menor norma dos coeficientes. O vetor(-1,1) está no núcleo. O esquema dados-previsao-residuo.svg é original; não reproduz figura dos livros ou gráfico experimental.

## Laboratório e testes

Na raiz do site, biblioteca padrão:
    python3 -m labs.minimos-quadrados-afim.experiment
    python3 -m unittest discover -s labs/minimos-quadrados-afim -t .

fit(xs,ys) aceita listas/tuplas racionais não vazias de mesmo comprimento; int/Fraction, sem bool/float. Não modifica entradas. Calcula reta por somas centralizadas, sem inversão de matriz. Se todas as abscissas coincidem, declara posto1 e escolhe o representante de inclinação zero. Retorna coeficientes, posto, direção de núcleo quando aplicável, previsões, resíduos, SSE e duas somas normais. Não é solver genérico de matrizes ou inferência estatística.

Cinco testes: exemplo racional;819 conjuntos de1..3 pontos e7371 perturbações, com coeficientes por forma independente das somas brutas, normalidade e identidade de mínimo; posto deficiente e família de parâmetros; transformação afim da abscissa, deslocamento de y e preservação; contratos e ajuste exato. Somar5 a todos os y muda o intercepto, não a SSE. Mudar a escala/origem de x conserva previsões e muda os coeficientes de forma correspondente.

Fraction torna exatas essas contas racionais, sem demonstrar estabilidade de ponto flutuante. QR/SVD, condicionamento, pesos e matrizes gerais continuam pendentes. Resíduo pequeno e ortogonal não garante lei física, independência do ruído, causalidade, intervalo de confiança ou generalização.

## Fontes e limites

Programa CCM0213: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213, aberto em22/10/2026; retorno com captura de seis dias antes. Ativação15/07/2024 compatível com período2024/2, sem comprovar a versão da turma. Aprovação permanece a do panorama, sem nova inspeção do histórico. Mínimos quadrados é um desenvolvimento editorial conectado a espaços euclidianos/projeção, não item nominal adicional ou prova do que foi ministrado.

Apostol, Cálculo volumeII, tradução Reverté1996/reimpressão2004 da segunda edição: consulta textual parcial §§1.15–1.16 pp.30–32/PDF48–50, decomposição ortogonal e melhor aproximação. Fonte complementar em Matemática III, distinta da bibliografia oficial; sem nova renderização, leitura integral ou distribuição do PDF.

Georgia Tech, Interactive Linear Algebra §6.5:
https://textbooks.math.gatech.edu/ila/least-squares.html
Consulta parcial em22/10/2026: interpretação, condições normais e unicidade. Extração textual omite várias fórmulas; não foi usada como transcrição literal delas. A prova e as contas acima são próprias, apoiadas também no teorema local de aproximação do Apostol. Sem copiar exemplos, tabelas ou figuras.

## Continuidade

Revisão pessoal: reconstruir as duas equações, o resíduo e a identidade de mínimo; explicar por que a+b pode ser identificável sem identificar cada parcela. Próximo currículo: matrizes gerais, QR/SVD e condições numéricas com fontes específicas. Álgebra linear tem18 aulas/111 exercícios, nove introduções curtas e nove recortes desenvolvidos; os nove grupos de Matemática III seguem parciais, sem domínio pessoal certificado.

Verificação do bloco: 889 testes Python aprovados, incluindo cinco testes novos de ajuste afim; 509 estruturas MathML conferidas. No navegador, resposta 1/6 aceita na questão 7; esquema inspecionado a 390 px, sem transbordamento horizontal ou erros de console observados; viewport restaurado. Prévia minimos-quadrados-afim-mobile.jpg. Nenhum modelo JavaScript alterado. Catálogo: 496 aulas/2836 exercícios em rascunho, 286 introduções com até três seções. Próxima revisão pessoal: reconstruir as equações normais, os resíduos e a família de coeficientes no posto deficiente. Próximo preparo global: conferir lacunas e fontes de Física III. Saldo semanal: 96%; parada operacional: 65%.
