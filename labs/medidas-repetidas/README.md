# Medidas repetidas — primeiro recorte próprio

## Primeiro declare o que está sendo medido

Queremos estimar o comprimento de um objeto em condições declaradas de medição. As leituras 9,8; 10,0; 10,2 cm são um conjunto sintético para estudar o cálculo, sem instrumento ou bancada reais. Em uma experiência, o registro precisa identificar objeto, unidade, instrumento, procedimento e condições. Uma lista de números não informa sozinha se houve reposicionamento independente, deriva de temperatura ou leitura repetida da mesma imagem.

## A média estima o centro, e o desvio descreve a dispersão

Há n=3 leituras. A soma é 30,0 cm; dividindo por 3, a média é 10,0 cm. Os desvios em relação a ela são −0,2; 0; +0,2 cm. Seus quadrados somam 0,08 cm². A variância amostral usa n−1=2, resultando em s²=0,04 cm² e s=0,2 cm. Esse desvio descreve o espalhamento das leituras; não é automaticamente a incerteza completa do comprimento.

s²=Σᵢ(xᵢ−x̄)²/(n−1)

## A incerteza da média exige uma hipótese sobre as leituras

Se as observações forem independentes, do mesmo processo estável e com variância comum finita, a contribuição estimada para a variância da média é s²/n. No exemplo, u_A²=0,04/3=1/75 cm² e u_A≈0,1155 cm. A avaliação estatística é chamada tipo A. Não concluímos que n=3 comprova normalidade ou estabilidade. Dependência entre leituras pode invalidar esta redução por n.

u_A²=s²/n; u_A=s/√n

## Copiar leituras não produz novas observações independentes

Duplicar as três linhas no arquivo faria o programa contar seis valores, mas não criaria seis medições. Uma redução numérica da incerteza calculada não justificaria ganho físico de informação. O laboratório conhece somente os valores e não verifica o protocolo. Em contraste, novas leituras independentes sob condições estáveis podem reduzir a contribuição estatística; por isso a unidade de repetição deve ser registrada antes do cálculo.

## Uma correção aditiva muda a estimativa sem diminuir o espalhamento

Suponha, apenas neste exemplo, que uma calibração externa estima que o instrumento indica b=+0,3 cm a mais. O modelo corrigido é y=x̄−b: 10,0−0,3=9,7 cm. Subtrair a mesma constante de todas as leituras deixa seus desvios em torno da nova média iguais aos anteriores. Logo s continua 0,2 cm. Não estamos afirmando conhecer o comprimento verdadeiro: b é uma estimativa da correção necessária.

y=x̄−b=9,7 cm

## A incerteza da calibração não se divide pelo número de leituras

Ainda suponha que a incerteza padrão da estimativa b seja u_b=0,1 cm, independente da média das leituras. Como y=x̄−b, os coeficientes de sensibilidade são +1 e −1; sem covariância, as variâncias somam: u_c²=s²/n+u_b². A correção é comum a todas as leituras, portanto seu termo 0,01 cm² não se divide por n. No exemplo, u_c²=1/75+1/100=7/300 cm² e u_c≈0,1528 cm. Se houver covariância entre a média e b, esta soma simples deixa de bastar.

u_c²=1/75+1/100=7/300 cm²

## Tipo A e tipo B classificam como a incerteza foi avaliada

Uma componente avaliada pela análise estatística de observações é tipo A; avaliações por outras informações, como um relatório de calibração e suas hipóteses declaradas, são tipo B. Essa classificação não equivale à oposição entre efeito aleatório e efeito sistemático. No modelo sintético, recebemos u_b já como incerteza padrão de uma fonte externa; não deduzimos seu valor do espalhamento das três leituras.

## Resolução exige uma distribuição justificada, não uma regra automática

Como exemplo separado, imagine um mostrador que arredonda em passos de d=0,1 cm e uma hipótese de erro de arredondamento uniforme entre −d/2 e +d/2. A semilargura é a=0,05 cm; a variância dessa distribuição é a²/3=d²/12=1/1200 cm², e a incerteza padrão é aproximadamente 0,02887 cm. A hipótese uniforme precisa ser defensável. Este termo não foi somado ao exemplo de calibração: antes de combinar, precisamos verificar se o efeito já aparece na dispersão ou em outra componente, evitando contagem dupla.

u_res²=a²/3=d²/12

## Zero dispersão não encerra o orçamento de incerteza

Se um instrumento fornece doze vezes 10,0 cm, o desvio calculado é zero. Ainda podem existir resolução limitada, correção incerta ou condições não exploradas. No nosso modelo, manter u_b=0,1 cm deixa u_c=0,1 cm mesmo com s=0. O programa não detecta efeitos omitidos: a qualidade do modelo depende da investigação experimental e das informações registradas.

## Uma incerteza padrão não é, por si só, um intervalo de 95%

O exemplo poderia ser relatado, com arredondamento declarado, como estimativa corrigida 9,70 cm e incerteza padrão combinada 0,15 cm, dentro das hipóteses do modelo. Isso não atribui automaticamente uma probabilidade de 95% ao intervalo correspondente. Incerteza expandida, fator de abrangência, distribuição e graus de liberdade exigem uma análise adicional, ainda não implementada. É preciso informar quais componentes foram consideradas e quais permanecem ausentes.

## Do cálculo ao experimento: um roteiro de registro

Para uma futura prática, prepare antes uma tabela com identificador da leitura, valor, unidade, instrumento e condição. Registre a regra de repetição e preserve os dados originais; crie uma coluna separada para valores corrigidos. Documente a origem e a unidade de b e u_b e justifique a independência usada. Este é um roteiro de estudo, não um relatório de experimento já executado nem um protocolo validado de uso de instrumentos.

## O laboratório mantém as variâncias exatas e as hipóteses explícitas

O núcleo Python aceita int e Fraction, rejeita bool, float, texto e amostras com menos de duas leituras. Retorna média, variância amostral, variância da média e, no modelo corrigido, variância combinada. Variâncias conservam a unidade ao quadrado; as raízes apresentadas no texto são aproximações. Testes usam uma identidade por diferenças entre pares e mudanças de unidade. Eles conferem as contas; não verificam independência, validade da calibração ou competência pessoal em bancada.

## Exercícios e resoluções

- Nas leituras sintéticas 9,8; 10,0; 10,2 cm, qual a média, em cm? **Resolução:** 30/3=10 cm.
- Qual é a variância amostral s² desse conjunto, em cm²? **Resolução:** (0,04+0+0,04)/(3−1)=0,04 cm².
- Qual o desvio amostral s, em cm? **Resolução:** A raiz de 0,04 cm² é 0,2 cm.
- Sob as hipóteses da aula, qual u_A², em cm²? **Resolução:** s²/n=0,04/3=1/75 cm².
- Com b=+0,3 cm, qual é y=x̄−b, em cm? **Resolução:** 10−0,3=9,7 cm.
- Com u_b=0,1 cm, qual sua contribuição à variância combinada, em cm²? **Resolução:** u_b²=0,01 cm²; não se divide por n.
- Para as três leituras e calibração independentes, qual u_c², em cm²? **Resolução:** 1/75+1/100=7/300 cm².
- No exemplo separado de resolução d=0,1 cm com arredondamento uniforme, qual a variância, em cm²? **Resolução:** d²/12=0,01/12=1/1200 cm².
- Se s=0 e u_b=0,1 cm, qual u_c neste modelo, em cm? **Resolução:** u_c=√(0+0,01)=0,1 cm.
- Converta s²=0,04 cm² para mm². **Resolução:** Como 1 cm=10 mm, a variância multiplica por 100: 4 mm².

## Código e fontes

Na raiz do site: `python3 -m unittest discover -s labs/medidas-repetidas -t .` e `python3 -m labs.medidas-repetidas.measurement`. Só biblioteca padrão. Entradas list/tuple com pelo menos duas leituras int/Fraction; viés estimado pode ser assinado e incerteza padrão deve ser não negativa. Variâncias racionais, sem inferência automática de independência, unidades ou suficiência do orçamento. Não se escolhe correção a partir da média dos dados sem uma referência externa.

Consulta parcial em 22/10/2026: NIST TN1297 (edição de 1994 em HTML), §§2–5 e Apêndice A.
- [NIST TN1297 — Classificação](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty)
- [NIST TN1297 — Tipo A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-3-type-evaluation-standard-uncertainty)
- [NIST TN1297 — Tipo B](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty)
- [NIST TN1297 — Composição](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty)
- [NIST TN1297 — Apêndice A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)

Júpiter e livros da turma: mantidos os registros de 16/10/2026, sem nova confirmação da versão de 2023 ou nova busca no acervo. Vuolo e Helene/Vanin não foram consultados; materiais pessoais de laboratório não foram recuperados. Preparação assistida por IA não demonstra prática ou competência pessoal. Primeira aula própria da trilha, 12 seções/10 exercícios, mapa 12 parciais/oito lacunas. Próxima etapa: propagação para grandezas indiretas e covariância; revisão pessoal deste modelo antes de atribuí-lo ao currículo demonstrável.

Verificação em 22/10/2026: cinco testes de laboratório aprovados (775 amostras de duas a quatro leituras por identidade entre pares, invariância a permutação, correção, mudança de unidade e contratos); 13 testes de catálogo e 554 estruturas MathML aprovados. Navegador a 390 px: figura legível, documento de 375 px, questão 6 rejeitou 1/300 e aceitou 0,01 cm². Navegação curso→aula e aprovação histórica visíveis; console sem erros observados. Prévia medidas-repetidas-mobile.jpg. Catálogo: 505 aulas/3221 exercícios. Suíte global dos outros laboratórios e experiência real não verificadas. Saldo semanal ao final: 90%; parada em 65%.
