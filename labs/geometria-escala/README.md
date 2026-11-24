# Geometria e escala — perímetro, área e volume

## Primeiro escolha a grandeza que responde à pergunta

Contornar um terreno pede perímetro, cobrir uma superfície pede área e preencher um espaço pede volume. Essas grandezas têm dimensões distintas: comprimento, comprimento ao quadrado e comprimento ao cubo. Antes de escolher uma fórmula, descreva a região ou o sólido e o que será contado. Somar as arestas de uma caixa não calcula quanto espaço ela ocupa.

## A área do retângulo conta unidades quadradas

Um retângulo de lados 2 e 3 unidades contém duas colunas e três linhas de quadrados unitários: 2×3=6 unidades². Em geral, A=ab. Seu perímetro é 2(a+b), que no exemplo vale 10 unidades. Um retângulo de lados 1 e 4 também tem perímetro 10, mas área 4: mesmo perímetro não determina a mesma área. As unidades ajudam a distinguir as duas perguntas.

A=ab; P=2(a+b)

## A altura do triângulo deve ser perpendicular à base

Para um triângulo de base b e altura perpendicular h, a área é bh/2. Podemos justificar a metade juntando duas cópias congruentes em um paralelogramo de base b e altura h. A altura não é necessariamente um lado do triângulo. Se a base mede 6 cm e a altura 4 cm, a área é 12 cm², mesmo que o lado inclinado tenha outra medida. Em um triângulo obtusângulo, a perpendicular pode encontrar o prolongamento da base.

A_triângulo=bh/2

## O volume da caixa acrescenta uma terceira dimensão

Na caixa retangular ideal de lados a,b,c, cada camada tem área ab e a altura c determina quanto espaço é empilhado. Assim V=abc. Para a=2 m, b=3 m e c=4 m, a base tem 6 m² e V=6 m²×4 m=24 m³. Trocar a escolha da face chamada base muda a área da base, mas não o volume do sólido. O modelo usa dimensões perpendiculares e consistentes.

V=abc

## A área total da superfície soma as seis faces

Uma caixa retangular fechada tem dois pares de faces de áreas ab e ac, além de duas faces de área bc. Portanto S=2(ab+ac+bc). Para lados 2,3,4 m, as áreas diferentes são 6,8,12 m²; o total é 2(6+8+12)=52 m². Esses 52 m² descrevem a superfície, e não o volume de 24 m³. Uma caixa sem tampa possui outra área de material; é preciso dizer quais faces entram na conta.

S=2(ab+ac+bc)

## Dimensões externas e capacidade interna precisam ser distinguidas

O volume calculado a partir de dimensões externas inclui o espaço ocupado pelas paredes de uma caixa real. Para capacidade útil, precisaríamos das dimensões internas e das condições de preenchimento. Já a área a pintar depende de quais faces são acessíveis e se o interior também será pintado. Os exemplos desta aula são sólidos geométricos ideais, sem espessura de parede ou perdas de material.

## Semelhança multiplica todos os comprimentos pelo mesmo fator

Se a,b,c passam a ka,kb,kc, com k>0, a nova área de base é (ka)(kb)=k²ab e o novo volume é (ka)(kb)(kc)=k³abc. A área total também multiplica por k², porque cada face recebe dois fatores k. Para k=2, a caixa 2×3×4 passa a 4×6×8: a superfície passa de 52 para 208 m² e o volume de 24 para 192 m³. O fator de comprimento 2 não é o fator de área nem o de volume.

comprimento ×k; área ×k²; volume ×k³

## Dobrar apenas uma dimensão não produz um sólido semelhante

Mude somente a primeira dimensão da caixa 2×3×4 para obter 4×3×4. O volume é 48 m³: dobrou, porque o produto recebeu apenas um fator 2. A área total é 2(12+16+12)=80 m². Ela não dobrou nem quadruplicou. A regra k²/k³ exige escala uniforme; não serve quando cada direção muda de maneira diferente. Leia exatamente quais medidas o problema altera.

## Converter a unidade exige elevar também o fator

Como 1 m=100 cm, um quadrado de lado 1 m tem área (100 cm)²=10000 cm². Um cubo de aresta 1 m tem volume (100 cm)³=1000000 cm³. Portanto 1 m² não corresponde a 100 cm², e 1 m³ não corresponde a 100 cm³. O expoente acompanha a dimensão da grandeza. Converter a unidade da descrição não aumenta fisicamente o objeto.

1 m²=10000 cm²; 1 m³=1000000 cm³

## Exemplo com unidades misturadas: converta antes do produto

Um retângulo de lados 20 cm e 0,3 m tem um lado em centímetros e outro em metros. Em centímetros, os lados são 20 e 30, então A=600 cm². Em metros, são 0,2 e 0,3, logo A=0,06 m². A conversão 0,06×10000=600 confirma que são a mesma área. Multiplicar 20×0,3 e escrever 6 cm² omitiria a unidade diferente do segundo lado.

## O laboratório usa frações para conferir a geometria

A função box recebe três dimensões positivas na mesma unidade como int ou Fraction. Retorna área de base, área total e volume. A função scale permite fatores positivos diferentes nas três direções, para comparar escala uniforme e mudança em um único lado. O código não reconhece unidades: a preparação dos dados deve convertê-las antes. Os testes contam cubos unitários e faces externas de caixas inteiras, verificando os resultados por uma construção diferente da fórmula.

## Uma conferência deve combinar fórmula, unidade e hipótese

Ao terminar, confirme se procurava contorno, superfície ou volume, se a altura usada é perpendicular e se todas as medidas estão na mesma unidade. Verifique também se a escala foi aplicada a todas as dimensões e se o modelo é um sólido fechado, aberto ou com espessura. Círculos, cilindros, cones, esferas e problemas de decomposição mais complexos ainda precisam de outros recortes. O material é rascunho assistido por IA para sua revisão, sem certificar domínio pessoal.

## Exercícios e resoluções originais

- Qual o volume de uma caixa retangular de lados 2 m, 3 m e 4 m, em m³? **Resolução:** A área de base é 2×3=6 m²; multiplicar por 4 m dá 24 m³.
- Dobrar todas as três dimensões de uma caixa multiplica o volume apenas por 2? **Resolução:** Não. Cada dimensão recebe um fator 2, então o volume multiplica por 2³=8.
- Qual a área total de uma caixa fechada 2×3×4 m, em m²? **Resolução:** 2(6+8+12)=52 m².
- Se todas as dimensões dessa caixa dobram, qual a nova área total, em m²? **Resolução:** 52×2²=208 m².
- Se todas as dimensões da caixa 2×3×4 m dobram, qual o novo volume, em m³? **Resolução:** 24×2³=192 m³.
- Se somente o lado 2 m passa para 4 m, qual o novo volume, em m³? **Resolução:** 4×3×4=48 m³.
- Qual a área total da caixa 4×3×4 m, em m²? **Resolução:** 2(12+16+12)=80 m².
- Um triângulo tem base 6 cm e altura perpendicular 4 cm. Qual a área, em cm²? **Resolução:** 6×4/2=12 cm².
- Quantos cm² correspondem a 1 m²? **Resolução:** (100 cm)²=10000 cm².
- Quantos cm³ correspondem a 1 m³? **Resolução:** (100 cm)³=1000000 cm³.
- Qual a área de um retângulo de lados 20 cm e 0,3 m, em cm²? **Resolução:** 0,3 m=30 cm; área 20×30=600 cm².
- Qual o perímetro de um retângulo 2×3 m, em m? **Resolução:** 2(2+3)=10 m.

## Código, fontes e limites

Na raiz: `python3 -m unittest discover -s labs/geometria-escala -t .` e `python3 -m labs.geometria-escala.box`. Apenas biblioteca padrão. Entradas int/Fraction positivas na mesma unidade, sem bool/float/texto. box retorna área de base, superfície total da caixa fechada e volume. scale aceita fatores positivos por eixo. Não reconhece unidades ou dimensões internas/externas automaticamente. Teste independente conta cubos unitários e faces expostas de 64 caixas com arestas inteiras; verifica também semelhança racional, permutação de eixos e mudança de unidade.

Fontes consultadas parcialmente em 22/10/2026: [OpenStax Prealgebra 2e §9.4](https://openstax.org/books/prealgebra-2e/pages/9-4-use-properties-of-rectangles-triangles-and-trapezoids), medidas e áreas; [§9.6](https://openstax.org/books/prealgebra-2e/pages/9-6-solve-geometry-applications-volume-and-surface-area), volume/superfície da caixa. Consulta HTML, sem paginação impressa conferida. Fórmulas usadas como referência para explicação, figura e exemplos próprios; nenhuma figura ou solução do livro reproduzida.

Aula aprofundada de três para 12 seções e de dois para 12 exercícios, IDs antigos preservados e pergunta genérica corrigida. Rascunho assistido por IA para revisão pessoal. Próxima revisão: distinguir 52 m² de 24 m³ e comparar escala uniforme com apenas uma direção alterada. Outros sólidos e decomposições complexas continuam pendentes.

Verificação: cinco testes do laboratório aprovados, incluindo contagem independente de cubos/faces expostas para 64 caixas, fatores racionais, permutação e mudança de unidade; 13 testes de catálogo e 565 estruturas MathML aprovados. Navegador a 390 px: documento de 375 px, figura inspecionada, questão 4 rejeitou 104 e aceitou 208 m²; console sem erros observados. Prévia geometria-escala-mobile.jpg. Catálogo 507 aulas/3271 exercícios, 256 aulas com até três seções; cobertura recalculada. Sem revisão pessoal, validação de medição real ou repetição da suíte global dos demais laboratórios. Saldo semanal confirmado após bloco: 90%; parada em 65%. Próxima revisão pessoal: explicar escala uniforme e conversão m²/cm² e m³/cm³. Próximo recorte escolar: contagem com ordem e repetição; demais sólidos permanecem pendentes.
