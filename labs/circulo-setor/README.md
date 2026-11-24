# Círculo, setor e coroa — região não é contorno

Sequência escolar própria para preparar aulas particulares; não é disciplina cursada ou prova de revisão pessoal. Antes de calcular, identifique grandeza, medida do raio/diâmetro, unidade e parte da figura.

Circunferência é o contorno; disco inclui a região interior. Raio r,diâmetro2r,comprimento2πr e áreaπr². π não é igual a3,14 ou22/7; conservarπ até o fim permite indicar resultado exato.

## Por que aparece r²

Semelhança multiplica comprimentos por k e áreas por k². Isso explica a escala, mas não determina sozinha o coeficienteπ. Um polígono regular inscrito tem área P_n a_n/2,perímetroP_n e apótemaa_n. Com mais lados,a_n→r eP_n→2πr; o polígono externo fornece a outra aproximação. A passagem ao limite dá A=πr². Essa justificativa usa a aproximação de contorno por polígonos e o limite de áreas; o programa ilustra essas hipóteses, sem provar teoria completa de medida ou convergência.

No laboratório, inscrito usa circunraior e externo apótemar: A_in=(n/2)r²sin(2π/n), A_out=nr²tan(π/n). Não são dois polígonos com o mesmo circunraio. Suas áreas cercamπr².

## Dois blocos de20 minutos

Um setor de ângulo centralα em graus ocupa fração f=α/360 da volta. Arco s=f2πr e área fπr². Em radianosθ=2πf, dão s=rθ e A=r²θ/2. Substituir120 diretamente no lugar deθ misturaria unidades angulares.

Exemplo próprio r6cm eα120°: f1/3,θ2π/3,arco4πcm e área12πcm². O perímetro do setor parcial é o arco mais os dois raios:12+4πcm. Arco não é corda. Em360° a região é o disco completo e os raios coincidentes não são bordas externas: perímetro12πcm, não12+12πcm. Zero é caso degenerado rejeitado pelo contrato.

Coroa de raio externo5cm e interno3cm tem áreaπ(25−9)=16πcm². A diferença dos raios2cm é espessura,não raio de um disco de área equivalente. Região com um furo exige subtrair área removida; se fosse solicitado todo o contorno, incluiria bordas interna e externa.

Dobrar raio multiplica arco por2 e área por4,se o ângulo é mantido. Um centímetro quadrado equivale a100mm²; mudar a unidade exige quadrar o fator. Ao dividir um disco em setores, as áreas e arcos somam os totais,mas os perímetros de todas as peças também contam os cortes internos em duplicidade.

## Código

Python3,biblioteca padrão. Coeficientes racionais deπ são separados: `sector(6,Fraction(1,3))` retorna área12π,arco4π e parte racional12 do perímetro. A fração de volta é entrada explícita,não um número de graus. Polígonos usam sin/tan float para conferência numérica. Limites didáticos: raio1/1000..1000,3..256lados,setor em(0,1]volta. Unidades lineares devem ser consistentes; o programa não detecta misturas de cm/m.

Execute `python3 labs/circulo-setor/circle.py`;testes `python3 -m unittest discover -s labs/circulo-setor -t .`. Quatro testes:exemplos/caso completo,partições/escala/coroas,contenção/refinamento de polígonos e contratos. Não igualar coeficientes racionais a uma avaliação racional deπ ou testes finitos a demonstração universal.

Fontes públicas consultadas parcialmente em29/10/2026: [OpenStax Prealgebra2e§9.5](https://openstax.org/books/prealgebra-2e/pages/9-5-solve-geometry-applications-circles-and-irregular-figures),raio/diâmetro,comprimento e área;[Precalculus2e§5.1](https://openstax.org/books/precalculus-2e/pages/5-1-angles),radianos,arcos e área de setor. Convenções deπ aproximado da primeira fonte não são tomadas como igualdade. Sem livro escolar privado consultado,nova ementa oficial,figura ou exercício copiado. Redação,dados,figura,código e exercícios originais assistidos por IA. Pendente:segmento circular,geometria espacial geral,sequência escolar integral e revisão pessoal.
