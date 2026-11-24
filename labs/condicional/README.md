# Condicionamento: mudar a informação disponível


13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.


## Objetivos

- Construir uma condicional pela restrição a um evento de probabilidade positiva.
- Distinguir condicionais inversas e reconhecer quando contagens são adequadas.
- Usar a regra do produto e uma partição para calcular probabilidade total.
- Separar probabilidades de um modelo, frequências observadas e causalidade.


## A informação define o denominador

Ao saber que B ocorreu, mantemos apenas a massa de probabilidade dentro de B e a renormalizamos para somar 1. A chance de A passa a ser a fração dessa massa que também pertence a A. A definição elementar exige P(B)>0. Não basta escolher um conjunto com muitos elementos: os pesos de seus resultados também importam.

P(A|B)=P(A∩B)/P(B)


## Quando podemos contar resultados

No dado justo, os seis resultados têm peso 1/6. Ao condicionar em B={4,5,6}, os três resultados remanescentes continuam igualmente prováveis. Para A={2,4,6}, A∩B={4,6}, logo P(A|B)=2/3. Em um dado enviesado, a mesma razão de contagens pode estar errada; precisamos somar os pesos dos resultados.

P(A|B)=|A∩B|/|B|, somente no modelo finito uniforme


## A pergunta inversa muda a referência

Agora use B={4,5}, mantendo A={2,4,6}. A interseção tem um resultado, mas B tem dois e A tem três. Portanto P(A|B)=1/2 e P(B|A)=1/3. Na primeira pergunta sabemos B; na segunda sabemos A. Igualdade em algum exemplo não prova uma identidade geral.

P(A|B)=1/2; P(B|A)=1/3


## A regra do produto vem da definição

Multiplique a definição por P(B). A probabilidade conjunta pode ser calculada como a chance de B vezes a chance de A dentro de B. Se também P(A)>0, inverter a ordem da fatoração fornece a mesma conjunta. Essa igualdade será a base de Bayes.

P(A∩B)=P(A|B)P(B)


## Uma partição evita dupla contagem

Suponha B₁,…,Bₖ disjuntos, cobrindo todo o espaço, com probabilidades positivas. Os eventos A∩Bᵢ também são disjuntos e sua união é A. Somar suas probabilidades e aplicar a regra do produto dá a lei da probabilidade total. Se uma parte tem probabilidade zero, sua conjunta é zero; não atribuímos uma condicional pela divisão por zero.

P(A)=Σᵢ P(A|Bᵢ)P(Bᵢ)


## Taxas de defeito precisam de pesos

Uma fábrica hipotética recebe 60% das peças da máquina M₁ e 40% de M₂. As taxas de defeito são respectivamente 2% e 5%. A taxa global é 0,6×0,02+0,4×0,05=0,032. A média simples 3,5% responde a uma mistura com pesos iguais e não a esta produção. Todos os valores são parâmetros sintéticos, não medições.

P(defeito)=4/125=0,032


## Independência é uma hipótese verificável no modelo

Eventos A e B são independentes se P(A∩B)=P(A)P(B). Quando P(B)>0, isso equivale a P(A|B)=P(A). Eventos disjuntos de probabilidades positivas não são independentes: sabendo B, A fica impossível. A dependência estatística por si só não identifica uma relação causal.

Independência: P(A∩B)=P(A)P(B)


## Probabilidade e frequência são objetos diferentes

A fórmula define uma propriedade do modelo. Em dados, a razão de contagens entre os casos observados em B é uma estimativa, sujeita ao desenho da coleta e à variação amostral. Zero casos observados em B não prova P(B)=0; apenas impede formar aquela razão empírica. Uma coleta seletiva pode mudar as frequências condicionais.




## Condicionamento zero e revisão

Na definição usada nesta aula, P(B)=0 deixa a divisão indefinida. Retornar None torna isso explícito no código; retornar zero inventaria uma probabilidade. Tratamentos mais avançados de condicionamento contínuo exigem outras construções e não são implementados aqui. Antes de usar um resultado, escreva o espaço amostral, os pesos e a informação conhecida.




## Exemplo resolvido

Duas máquinas produzem peças: qual a probabilidade total de defeito?

1. M₁ e M₂ formam uma partição; os pesos são 3/5 e 2/5.
2. As condicionais de defeito são 1/50 e 1/20.
3. Conjuntas: (3/5)(1/50)=3/250 e (2/5)(1/20)=1/50.
4. Somando: 3/250+5/250=8/250=4/125=0,032.
5. A conta descreve o modelo hipotético; estimar esses parâmetros exigiria dados.


## Exercícios e resoluções


### No dado justo, A={2,4,6} e B={4,5,6}. Quanto é P(A|B)?



2 favoráveis entre 3.


### Pode usar essa fórmula sem cuidado quando P(B)=0?

Sim
Não

O denominador zero exige outro tratamento.


### No dado justo, A={2,4,6}, B={4,5}. Quanto é P(B|A)?



A é a condição: apenas 4 entre três pares, portanto 1/3.


### P(B)=0,4 e P(A|B)=0,75. Quanto é P(A∩B)?



0,4×0,75=0,3.


### Máquinas com pesos 0,6 e 0,4 têm taxas de defeito 0,02 e 0,05. Qual a taxa global?



0,6×0,02+0,4×0,05=0,032.


### Podemos usar a razão de contagens em qualquer dado enviesado?

Sim, os nomes dos resultados bastam
Não, os pesos precisam ser considerados

A fórmula por contagens exige equiprobabilidade.


### Que condições justificam somar P(A|Bᵢ)P(Bᵢ) neste roteiro?

Bᵢ disjuntos e cobrindo todo o espaço, com probabilidades positivas
Bᵢ apenas diferentes, ainda que se sobreponham

Disjunção evita dupla contagem; cobertura evita omissão.


### P(A|B) diferente de P(A) prova que B causa A?

Sim
Não

A associação é compatível com explicações causais distintas e seleção de dados.


### Nenhum caso observado em B prova P(B)=0?

Sim
Não

Ausência na amostra não prova probabilidade nula no modelo.


## Python

Execute com Python 3, somente biblioteca padrão: `python3 example.py`. Sem leitura de dados privados ou escrita de resultados externos.


## Hipóteses e limites

- Contagens por razão apenas no espaço finito uniforme.
- Condicionais elementares exigem evento condicionante de probabilidade positiva.
- Lei total usa partição, com taxas e pesos hipotéticos.
- Exemplos não são dados da pesquisa ou comprovação de causalidade.


## Continuação — pesos não uniformes, 22/10/2026

Aula `pe-condicional`: 14 seções e 14 exercícios, preservando o conteúdo anterior. Cinco seções e cinco exercícios novos. Modelo original Ω={a,b,c,d}, pesos (1,2,3,4), A={a,c}, B={b,c}: P(A|B)=3/5, P(B|A)=3/4, conjunta=3/10. Os rótulos não são equiprováveis. No painel existente, representar as quatro regiões pelas contagens (3,1,2,4), compostas por átomos equiprováveis.

`weighted.py` aceita mapa não vazio de pesos int/Fraction não negativos, total positivo e eventos contidos no espaço. Não aceita float nem bool. Pesos podem não estar normalizados. Evento condicionante de massa zero retorna None, incluindo evento não vazio com peso nulo. Não é inferência empírica nem análise de dados da IC.

Fontes privadas reconferidas por extração parcial: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.54–55 (PDF69–70); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, pp.26–29 (PDF18–19, páginas duplas). Definição, restrição e renormalização fundamentam o texto; exemplos, exercícios e código são originais. A convenção dos livros para massa zero difere do retorno explícito None do laboratório. Não houve leitura integral ou distribuição dos PDFs. A extração integral preliminar de Noções emitiu avisos em outros trechos; o recorte citado foi extraído e lido separadamente sem esses avisos.

Execute na raiz do protótipo:

```sh
python3 labs/condicional/weighted.py
python3 -m unittest labs.condicional.test_weighted
```

Três testes novos: 80 vetores de pesos com entradas 0–2 cruzados com todos os pares de 16 eventos, conferidos por expansão independente em objetos distintos; invariância por escala racional e complemento; massa zero e contratos inválidos. Suíte completa: 747 testes Python aprovados; 435 estruturas MathML conferidas. No navegador, resposta 3/5 aceita; largura 390px sem transbordamento horizontal e sem erros de console observados. Prévia: `condicional-pesos-introducao-mobile.jpg` na raiz do protótipo.

Catálogo atual: 485 aulas/2502 exercícios. Percurso complementar de probabilidade e estatística: 15 aulas/140 exercícios. Esses totais incluem conteúdo de outros blocos; não representam cobertura completa. Revisão pessoal de Jhuann pendente. Próxima ação: revisar esta aula e o encadeamento para Bayes, diferenciando taxa do detector, taxa-base e probabilidade posterior. Saldo consultado após o bloco: 75%; parada em 65% preservada.


## Atualização em etapas — 22/10/2026

Aula `pe-condicional`: 19 seções/20 exercícios. Cinco seções e seis exercícios novos preservam as 14 seções/14 questões anteriores e o painel existente. Derivação original: se P(B∩C)>0, condicionar primeiro em B e depois em C equivale a condicionar diretamente na interseção. Não supõe independência. Ordem das restrições não muda o resultado final; os intermediários podem mudar. Repetir uma informação não cria evidência independente. Interseção nula retorna None.

Exemplo próprio com pesos (1,2,3,4,5), A={c,e}, B={a,b,c,d}, C={b,c,e}: P(A|B)=3/10, P(C|B)=1/2, P(A|B∩C)=3/5, P(A|C)=4/5. A conjunta tripla é 1/5; trocar a última condicional por P(A|C) produz 4/15 incorretamente. Valores sintéticos; nenhuma aplicação empírica ou causal inferida.

Referências privadas parcialmente reconferidas por extração: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2 pp.54–55 (PDF69–70), definição e regra do produto; Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3 pp.26–29 (PDF18–19, páginas duplas), restrição da medida e produto de múltiplos eventos. A derivação em etapas, os números, exercícios e código são próprios; não se atribui o exemplo aos autores. PDFs não distribuídos; convenção dos livros em eventos nulos permanece distinguida da razão elementar usada aqui.

Laboratório: `python3 -m labs.condicional.sequential` na raiz. O import relativo exige execução como módulo. `sequential.py` reaproveita a validação racional de `weighted.py`. Três testes novos: 26 vetores de pesos × 512 trios de eventos, verificados por enumeração independente de objetos; igualdade entre etapas/direto, inversão da ordem e repetição; exemplo e produto; massa nula e entradas inválidas. Não implementa condicionamento contínuo nem inferência amostral.

Verificação: 780 testes Python aprovados, incluindo catálogo e todos os laboratórios; 458 estruturas MathML aprovadas. Navegador aceitou 3/5 na questão 16; largura de 390 px sem transbordamento horizontal observado, sem erros de console. Prévia `condicional-atualizacao-mobile.jpg`. Nenhuma simulação JS alterada; suíte JS de simulações não repetida neste bloco. Rascunho aguardando revisão de Jhuann.

Próxima ação de estudo: reconstruir as massas 10, 5 e 3, explicar por que não se pode apagar B da última condição e resolver as questões 15–20. Próximo aprofundamento possível: ponte entre essa regra e independência condicional em sinais sucessivos; há apoio anterior na aula `probabilidade-condicional`, ainda não revisado pessoalmente. Catálogo: 487 aulas/2583 exercícios; percurso complementar de probabilidade e estatística: 15 aulas/151 exercícios. Nenhum curso completo. Saldo semanal após o bloco: 99%; parada operacional em 65% preservada.

### Receber outra informação restringe novamente

Depois de saber B, a medida é P_B(D)=P(D∩B)/P(B). Ao saber também C, só restam resultados em B∩C. Se P(B∩C)>0, podemos condicionar em uma etapa ou em duas. A condição é a interseção, não a união: ambas as informações devem valer.

P_B(A|C)=P_B(A∩C)/P_B(C)=P(A∩B∩C)/P(B∩C)

### Por que a atualização em etapas funciona

No numerador, P_B(A∩C)=P(A∩B∩C)/P(B); no denominador, P_B(C)=P(B∩C)/P(B). Dividir as duas razões cancela o mesmo fator P(B). Isso prova a identidade sem supor independência. O cálculo usa a informação conjunta, e não apenas as probabilidades marginais de A, B e C.

P_B(A|C)=P(A|B∩C)

### Exemplo: cinco resultados, duas restrições

Use pesos a=1, b=2, c=3, d=4, e=5, massa total 15. Tome A={c,e}, B={a,b,c,d}, C={b,c,e}. Primeiro, B tem massa 10 e A∩B={c}, de massa 3: P(A|B)=3/10. Dentro de B, C retém {b,c}, massa 5: P(C|B)=5/10. A∩C dentro de B tem massa 3. Logo (3/10)/(5/10)=3/5. Diretamente, A∩B∩C={c} e B∩C={b,c}, dando 3/5.

P(A|B∩C)=3/5; P(A|C)=8/10

### Três fatores, três denominadores

A regra do produto para três eventos é P(A∩B∩C)=P(B)P(C|B)P(A|B∩C), quando a última condição tem massa positiva. No exemplo, (10/15)(5/10)(3/5)=3/15=1/5. Trocar o último fator por P(A|C)=4/5 daria 4/15: uma resposta errada. Apagar B da condição exige uma hipótese adicional, como independência condicional apropriada.

P(A∩B∩C)=(2/3)(1/2)(3/5)=1/5

### Ordem, informação repetida e incompatibilidade

A ordem de chegada muda as probabilidades intermediárias, mas não o resultado final após conhecer B e C: B∩C=C∩B. Repetir B também não altera a resposta, pois B∩B=B; uma cópia de uma informação não é uma nova observação independente. Se B e C têm massa positiva separadamente, mas sua interseção tem massa zero, a última razão ainda fica indefinida. O laboratório retorna None. A comutatividade da interseção não afirma causalidade nem independência temporal.

### No exemplo de cinco pesos, quanto é P(C|B)?

Dentro de B a massa de C é 2+3=5, entre 10: 1/2.

### No mesmo exemplo, quanto é P(A|B∩C)?

A interseção final tem massa 3 e B∩C massa 5: 3/5.

### No mesmo exemplo, quanto é P(A∩B∩C) antes de condicionar?

Apenas c, com peso 3 em 15: 1/5.

### Saber B duas vezes deve mudar P(A|B)?

Uma informação idêntica repetida não restringe novamente o espaço.

### Com P(B∩C)>0, inverter a ordem das duas restrições muda a probabilidade final?

Ambas terminam em B∩C; os valores intermediários podem diferir.

### P(B)>0 e P(C)>0 garantem P(B∩C)>0?

Dois eventos disjuntos podem ter massas positivas. Nesse caso a interseção é nula.


## Continuação: independência dentro de uma condição — 22/10/2026

### Quando uma condição pode ser retirada?

Escreva primeiro qual informação será mantida. Dentro de C, com P(C)>0, A e B são condicionalmente independentes quando a conjunta condicional é o produto das duas marginais condicionais. É a definição de independência aplicada à medida P_C. Essa afirmação vale para o evento C indicado; independência dada uma variável aleatória exigiria verificar seus estratos relevantes, um tema posterior.

P(A∩B|C)=P(A|C)P(B|C)

### A divisão que permite eliminar B

Se também P(B∩C)>0, divida a fatoração anterior por P(B|C). A definição fornece P(A|B∩C)=P(A∩B|C)/P(B|C)=P(A|C). A condição C permanece: só B foi retirada. Para eventos, a igualdade implica de volta a fatoração quando esse denominador é positivo. Independência de A e B sem C não autoriza esta simplificação.

A e B independentes dado C ⇒ P(A|B∩C)=P(A|C)

### Duas moedas antes e depois de uma informação

Retome o espaço da aula de independência: Ω={00,01,10,11}, com quatro resultados equiprováveis. Os dígitos representam os resultados de duas moedas justas e independentes. A significa primeiro dígito 1; B significa segundo dígito 1. Sem restrição, P(A)=P(B)=1/2 e P(A∩B)=1/4. Agora C significa dígitos iguais: restam 00 e 11, ainda equiprováveis. Dentro de C, A e B têm probabilidade 1/2, mas ocorrem juntas em 11, também com probabilidade 1/2. O produto das marginais seria 1/4. Portanto deixam de ser independentes sob essa informação.

P(A∩B|C)=1/2 ≠ (1/2)(1/2)

### Conhecer a segunda moeda agora revela a primeira

Sabendo que os dígitos são iguais e que o segundo é 1, só resta 11. Logo P(A|B∩C)=1, enquanto P(A|C)=1/2. Não há alteração física das moedas: estamos selecionando resultados da mesma distribuição. O exemplo também mostra que independência aos pares entre A, B e C não equivale a independência mútua, como discutido na aula “Independência: uma hipótese de fatoração”. Aqui o foco é o denominador depois da seleção.

P(A|B∩C)=1; P(A|C)=1/2

### Como conferir sem inventar independência

O novo laboratório calcula as três condicionais com frações exatas e compara a conjunta ao produto. Para C de massa zero, devolve valores None, incluindo o diagnóstico de independência, em vez de escolher a convenção de extensão dos livros. A igualdade é uma propriedade da distribuição fornecida, não um teste estatístico sobre dados. Ela não demonstra causalidade nem que diferenças empíricas sejam significativas. Para o efeito de misturar grupos com pesos distintos, consulte as aulas de comparação de condicionais e agregados e de mistura e independência; esse problema tem material próprio.



### Exercícios adicionais e resoluções

- Nas duas moedas, sabendo que os dígitos são iguais (C), quanto é P(A∩B|C)? **Resolução:** Só 11 entre 00 e 11: 1/2.
- No mesmo exemplo, quanto vale P(A|C)P(B|C)? **Resolução:** Cada marginal vale 1/2; o produto é 1/4.
- Sabendo C e que o segundo dígito é 1 (B), quanto é P(A|B∩C)? **Resolução:** B∩C={11}; o primeiro dígito é 1 nesse único resultado.
- A e B independentes sem restrição permitem retirar B de P(A|B∩C), para qualquer C de massa positiva? **Resolução:** Não. Independência marginal não garante independência dado C; além disso, a razão exige P(B∩C)>0.
- Se P(A|C)=0,3, P(B|C)=0,4 e A e B são independentes dado C, quanto é P(A∩B|C)? **Resolução:** A hipótese autoriza 0,3×0,4=0,12.
- Se P(B∩C)=0, podemos dividir por P(B|C) para retirar B? **Resolução:** Não. Com P(C)>0, esse denominador é zero. A equivalência por divisão não está disponível.

### Fontes, reprodução e limites

Consulta parcial dos exemplares privados autorizados: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.54–58 (PDF69–73); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, pp. 26–29 e 35 (PDF18–19 e 22, duas páginas impressas por página do PDF). A p.35 foi conferida também visualmente. Noções fundamenta a primeira leitura; PVA apresenta explicitamente independência condicional e independência de vários eventos. Não se atribui aos livros a autoria desta explicação, do código ou dos exercícios. Nenhum PDF ou figura do livro foi copiado para o site.

Na raiz do site:

```sh
python3 -m labs.condicional.independence
python3 -m unittest labs.condicional.test_independence
```

O módulo usa weighted.py deste laboratório; baixar apenas independence.py não basta. Casos exatos de modelos finitos não substituem inferência com dados. Condicionamento por variáveis contínuas e uma teoria geral de independência condicional ainda não foram desenvolvidos. Rascunho para revisão de Jhuann.


## Continuação visual — 22/10/2026

A aula pe-condicional passa a 26 seções/29 exercícios. Diagrama original moedas-informacao.svg compara a distribuição original e as restrições a C={00,11} e D={01,10}, com legenda textual acessível. Novas explicações e três questões desenvolvem o complemento e a reconstrução da conjunta por probabilidade total. As marginais continuam 1/2 em todos os casos, mas as conjuntas são 1/4, 1/2 e zero, respectivamente. A mistura simétrica recupera independência; isso não vale para misturas arbitrárias. Nenhum exemplo ou figura do livro foi copiado.

Reconferência parcial dos exemplares privados: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.56–58 (PDF71–73), independência e partições; Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, p.35 (PDF22, página dupla), definição de independência condicional. Extração textual; sem nova conferência visual das páginas nesta continuação. Notação A/B/C/D e diagrama são próprios. Rascunho para revisão pessoal.

Próxima revisão: reconstruir as três distribuições, responder às questões 27–29 e explicar por que marginais preservadas não garantem independência. Condicionamento contínuo e independência dada uma variável continuam fora deste recorte.

Verificação desta continuação: 21 testes direcionados aprovados (catálogo e três laboratórios de condicionamento), mais conferência racional das três conjuntas, dos produtos e da mistura. No navegador, 1/4 aceito na questão 29; diagrama legível a 390 px, sem transbordamento horizontal ou erros de console observados. Prévia: condicional-moedas-mobile.jpg. Nenhum modelo JS ou código de laboratório alterado; suíte completa não repetida. Catálogo: 493 aulas/2760 exercícios em rascunho. Saldo semanal conferido: 96%; parada em 65%.


## Probabilidade total dentro de uma condição — 22/10/2026

### Probabilidade total depois de receber uma informação

Suponha que já sabemos C, com P(C)>0. Uma partição B₁,…,Bₖ continua separando os resultados possíveis, mas seus pesos agora são P(Bᵢ|C). Dentro de cada grupo que ainda tem massa, a taxa relevante é P(A|Bᵢ∩C). Multiplicar taxa e peso fornece P(A∩Bᵢ|C); somar essas conjuntas disjuntas reconstrói P(A|C). Grupos com P(Bᵢ∩C)=0 não entram na soma: não calculamos uma razão indefinida para depois multiplicá-la por zero.

P(A|C)=Σᵢ:P(Bᵢ∩C)>0 P(A|Bᵢ∩C)P(Bᵢ|C)

### Exemplo resolvido: os grupos mudam de peso

Lance um dado justo. A é obter um número primo: {2,3,5}. C informa que o resultado é pelo menos 2: {2,3,4,5,6}. Separe os resultados por paridade, E={2,4,6} e O={1,3,5}. Dentro de C há três pares e dois ímpares, portanto P(E|C)=3/5 e P(O|C)=2/5. Nos pares sobreviventes, só 2 é primo: P(A|E∩C)=1/3. Nos ímpares sobreviventes, 3 e 5 são primos: P(A|O∩C)=1. Assim (1/3)(3/5)+(1)(2/5)=3/5. A contagem direta confirma: três primos entre os cinco resultados de C.

P(A|C)=1/5+2/5=3/5

### Por que não conservar as taxas anteriores?

Antes de saber C, a taxa de primos entre os ímpares é P(A|O)=2/3, porque 1 ainda está no grupo. Usá-la junto dos pesos atualizados daria (1/3)(3/5)+(2/3)(2/5)=7/15, diferente de 3/5. Usar também os pesos antigos, 1/2 e 1/2, recuperaria P(A)=1/2, outra pergunta. Toda taxa e todo peso precisam se referir à informação indicada. O exemplo é uma dedução original da definição e da probabilidade total dos livros; não é um exercício transcrito. O laboratório enumera resultados e confere a identidade com frações exatas.



### Exercícios originais e resoluções

- No exemplo do dado justo, C={2,3,4,5,6} e O={1,3,5}. Quanto é P(O|C)? **Resolução:** O∩C={3,5}: dois entre os cinco resultados de C.
- Com A={2,3,5}, quanto é P(A|O∩C) no mesmo exemplo? **Resolução:** O∩C={3,5}, e ambos são primos: 2/2=1.
- Quanto é P(A|C) ao combinar os grupos de paridade do exemplo? **Resolução:** (1/3)(3/5)+(1)(2/5)=3/5; diretamente são três primos entre cinco.
- Que valor incorreto resulta de usar a taxa antiga P(A|O)=2/3 com os pesos atualizados 3/5 e 2/5? **Resolução:** (1/3)(3/5)+(2/3)(2/5)=1/5+4/15=7/15. A conta mistura informações distintas.

Fontes reconferidas parcialmente: Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.54–55 (PDF69–70); Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, pp.26–29 (PDF18–19, páginas duplas). PVA fundamenta a medida restrita e a lei total; a aplicação dentro de C é uma dedução original. Não houve reprodução de páginas ou exercícios. Leitura textual nesta continuação. Rascunho para revisão de Jhuann.

A aula passa a 29 seções/33 exercícios. Execute na raiz: python3 -m unittest labs.condicional.test_conditioned_total. Não há alteração dos modelos interativos ou condicionamento contínuo. Próxima revisão pessoal: resolver o dado sem consultar a conta e explicar por que 7/15 responde a uma combinação inconsistente.

Verificação deste bloco: 24 testes direcionados aprovados e 515 estruturas MathML conferidas; resposta 3/5 aceita na questão 32, leitura a 390 px sem transbordamento horizontal observado. Prévia: condicional-total-mobile.jpg. Suíte global não repetida; modelos interativos preservados.


## Bayes mantendo a informação anterior — 22/10/2026

### Bayes sem apagar a informação anterior

Já sabemos C, com P(C)>0, e recebemos A, com P(A∩C)>0. Queremos atualizar a chance de um grupo B. Na medida condicionada em C, a definição dá P(B|A∩C)=P(A∩B|C)/P(A|C). Se P(B∩C)>0, a regra do produto escreve o numerador como P(A|B∩C)P(B|C). Assim a probabilidade anterior ao novo dado é P(B|C), e a taxa de A no grupo também conserva C. Nenhuma independência foi suposta.

P(B|A∩C)=P(A|B∩C)P(B|C)/P(A|C)

### Exemplo resolvido: de qual grupo veio o primo?

No mesmo dado justo, C={2,3,4,5,6}, A={2,3,5} e O={1,3,5}. Antes de saber que saiu primo, P(O|C)=2/5. A taxa de primos nos ímpares que sobreviveram é P(A|O∩C)=1. Já calculamos P(A|C)=3/5 somando as contribuições par e ímpar. O numerador de Bayes é (1)(2/5)=2/5; dividindo por 3/5 obtemos 2/3. Confira sem fórmula: A∩C={2,3,5}, e dois desses três resultados são ímpares. A informação de primalidade aumenta a chance do grupo ímpar de 2/5 para 2/3.

P(O|A∩C)=(2/5)/(3/5)=2/3

### Uma igualdade numérica pode esconder um passo errado

Neste exemplo, A está contido em C; portanto P(O|A∩C)=P(O|A). Essa coincidência no resultado final não autoriza misturar condicionais. Usar a taxa antiga P(A|O)=2/3, o peso atualizado P(O|C)=2/5 e o denominador correto P(A|C)=3/5 daria 4/9. Se também calcular o denominador com as duas taxas antigas, obteria (4/15)/(7/15)=4/7: outra resposta errada. A fórmula exige que todos os fatores pertençam à mesma medida. C pode ser redundante na pergunta final e continuar indispensável na justificativa dos fatores usados.

### Células nulas e o limite da atualização

Se P(B∩C)=0, a chance posterior do grupo B é zero quando P(A∩C)>0: a interseção A∩B∩C também tem massa zero. Calcule pela conjunta, sem formar a taxa indefinida P(A|B∩C). Se P(A∩C)=0, a própria informação nova tem massa zero dentro de C e a razão elementar de Bayes não está definida; o laboratório retorna None. Isso não significa que dados possam refutar qualquer modelo sem uma análise da coleta. Os exemplos são distribuições hipotéticas, não frequências medidas, testes estatísticos ou prova de causalidade.

### Exercícios originais e resoluções

- No dado justo com C={2,3,4,5,6}, qual é a chance de resultado ímpar antes de receber a informação de primalidade? **Resolução:** Dois resultados de C são ímpares: P(O|C)=2/5.
- No mesmo dado, sabendo também A={2,3,5}, quanto é P(O|A∩C)? **Resolução:** (1)(2/5)/(3/5)=2/3. Direto: 3 e 5 são ímpares entre 2, 3 e 5.
- Que valor incorreto resulta de (2/3)(2/5)/(3/5), misturando a taxa antiga com o peso e o denominador atualizados? **Resolução:** (2/3)(2/5)/(3/5)=(4/15)(5/3)=4/9, diferente de 2/3.
- Suponha P(C)>0, P(A∩C)>0 e P(B∩C)=0. Quanto é P(B|A∩C)? **Resolução:** A∩B∩C tem massa zero; dividindo pela massa positiva de A∩C, obtemos zero. Não é preciso definir P(A|B∩C).

Fontes: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, p.59 (PDF74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, Teorema 1.4, p.30 (PDF20, página dupla). Consulta textual parcial. A aplicação de Bayes dentro de C e os exercícios são deduções originais; não são transcrições dos livros. Material preparado com apoio de IA, em rascunho para revisão de Jhuann.

Aula: 33 seções/37 exercícios. Execute python3 -m unittest labs.condicional.test_bayes_conditioned na raiz do site. Próxima revisão pessoal: justificar 2/3 por contagem e por Bayes, explicar por que 4/9 está errado e tratar um grupo de massa zero.


## Bayes dentro de uma condição — 22/10/2026

A aula pe-condicional passa a 33 seções/37 exercícios. Continuação original: Bayes na medida condicionada em C, atualização da chance de um grupo, comparação com fatores inconsistentes e distinção entre grupo de massa zero e informação nova de massa zero. No dado justo, P(O|C)=2/5 e P(O|A∩C)=2/3; usar a taxa antiga no numerador daria 4/9. Não se supõe independência.

Referências consultadas parcialmente por extração textual: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, p.59 (PDF74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, Teorema 1.4, p.30 (PDF20, página dupla). A aplicação dentro de C é uma dedução didática própria; não há transcrição de exercícios ou reprodução das páginas.

Verificação: 18 testes direcionados aprovados (12 de catálogo e seis de total/Bayes condicionados), incluindo enumeração independente, células nulas e um contraexemplo à retirada de C; 529 estruturas MathML conferidas. No navegador, questão 35 aceitou 2/3; fórmula legível a 390 px, largura da página igual à tela e nenhum erro de console observado. Prévia: condicional-bayes-c-mobile.jpg. Suíte global e modelos interativos não foram alterados nem revalidados integralmente. Catálogo: 500 aulas/2962 exercícios; trilha de Probabilidade: 16 aulas/180 exercícios. Rascunho assistido por IA, sujeito à revisão pessoal. Próxima ação: resolver as questões 34–37 explicando cada denominador, antes de ampliar o conteúdo. Saldo semanal: 94%; parada operacional em 65%.


## O protocolo de observação — 22/10/2026

Continuação original de pe-condicional: dois indicadores ordenados equiprováveis. Saber que pelo menos um está ligado dá P(ambos|E)=1/3. Escolher uma posição uniformemente, independentemente do par, e observar que ela está ligada dá P(ambos|R)=1/2. Espaço ampliado com oito átomos, verossimilhanças e posterior dos quatro pares explicitados. Não são dados de equipamentos reais. Quatro seções e quatro exercícios novos: a aula tem 37 seções/41 exercícios, ainda em rascunho assistido por IA para revisão pessoal.

Referências de fundamentos reconferidas parcialmente por extração textual: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.54 e 59 (PDF69 e 74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, pp.26–27 e 30 (PDF18 e 20, páginas duplas). Exemplo, números e exercícios próprios; não há reprodução do livro nem alegação de leitura integral. A razão elementar exige condição de massa positiva; o retorno None do laboratório é uma convenção explícita, distinta da extensão arbitrária mencionada em Noções p.54.

Teste: python3 -m unittest labs.condicional.test_observation. Enumeração independente dos oito átomos, comparação com Bayes para 80 configurações não nulas de pesos e conferência de observar sempre a primeira posição. Próxima revisão pessoal: explicar por que 11 tem peso posterior duplo de 01 no protocolo aleatório, sem invocar equiprobabilidade dos pares sobreviventes. Condicionamento contínuo permanece pendente.

Verificação deste bloco: 22 testes direcionados aprovados (13 de catálogo, três do protocolo e seis de probabilidade total/Bayes condicionados); 538 estruturas MathML conferidas. No navegador, questão 39 rejeitou 1/3 e aceitou 1/2; largura 390 px sem transbordamento horizontal e nenhum erro de console observado. Prévia: condicional-protocolo-mobile.jpg. Suíte global e modelos interativos não foram revalidados integralmente. Catálogo: 501 aulas/3068 exercícios; Probabilidade: 16 aulas/184 exercícios. Saldo semanal após o bloco: 92%; parada em 65%.


## Retiradas sem reposição — 22/10/2026

### Sem reposição: o espaço contém objetos identificados

Uma urna hipotética contém três bolas vermelhas V₁,V₂,V₃ e duas azuis Z₁,Z₂. Retiramos duas, em ordem, sem reposição. O protocolo escolhe cada bola restante com a mesma chance. Os 5×4=20 pares ordenados de bolas distintas são equiprováveis. Os quatro pares de cores VV, VZ, ZV e ZZ não são equiprováveis: representam respectivamente 6, 6, 6 e 2 pares de objetos. Defina A: a primeira é vermelha; B: a segunda é vermelha. Identificar os objetos evita atribuir pesos iguais apenas porque há quatro nomes de cores.

### O primeiro resultado muda o segundo denominador

Sem informação, P(A)=3/5. Sabendo A, restam duas vermelhas entre quatro bolas, portanto P(B|A)=2/4=1/2. Pela regra do produto, P(A∩B)=(3/5)(1/2)=3/10. Se a primeira foi azul, continuam três vermelhas entre quatro: P(B|Aᶜ)=3/4. A chance condicional depende do resultado anterior porque a composição restante mudou. Todos os valores vêm deste modelo de sorteio uniforme, sem dados experimentais.

P(A∩B)=P(A)P(B|A)=(3/5)(2/4)=3/10

### Mesma marginal, dependência preservada

Antes de observar a primeira bola, a probabilidade total fornece P(B)=(1/2)(3/5)+(3/4)(2/5)=3/5. Assim P(A)=P(B), mas P(B|A)=1/2 difere de 3/5 e P(A∩B)=3/10 difere de 9/25. A simetria entre as duas posições recupera as marginais; ela não torna os resultados independentes. Saber que a segunda foi vermelha também dá P(A|B)=(3/10)/(3/5)=1/2. Essa igualdade entre condicionais inversas vale neste exemplo, não em geral.

P(B)=3/10+3/10=3/5; P(A|B)=1/2

### Reposição é outra hipótese de amostragem

Se devolvemos a primeira bola e o segundo sorteio é uniforme independentemente do primeiro, o espaço tem 5×5=25 pares equiprováveis, incluindo repetir a mesma bola. Agora P(B|A)=3/5 e P(A∩B)=9/25. Reposição sozinha não declara independência de qualquer mecanismo: precisamos explicitar como os sorteios são realizados. O teste Python enumera objetos, confere as duas marginais, a regra do produto e a probabilidade total, e contrasta os dois protocolos. Para uma urna com r vermelhas em n bolas, 1≤r≤n e n≥2, a expressão sem reposição é (r/n)((r−1)/(n−1)).

Sem reposição: P(VV)=r(r−1)/[n(n−1)]

### Exercícios originais

- Sem reposição, três vermelhas e duas azuis: quanto é P(B|A), com A: primeira vermelha e B: segunda vermelha? **Resolução:** Restam duas vermelhas entre quatro bolas: 2/4=1/2.
- Na mesma urna sem reposição, quanto é P(A∩B)? **Resolução:** (3/5)(2/4)=3/10. O segundo denominador é quatro.
- Antes de observar a primeira bola, quanto é P(B) sem reposição? **Resolução:** (1/2)(3/5)+(3/4)(2/5)=3/5. Marginal igual não implica independência.
- Sabendo que a segunda bola foi vermelha, quanto é P(A|B) sem reposição? **Resolução:** P(A∩B)/P(B)=(3/10)/(3/5)=1/2.
- Com reposição e sorteios uniformes independentes, quanto é P(A∩B)? **Resolução:** (3/5)(3/5)=9/25, diferente de 3/10.

Fontes de fundamentos: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.54–55 (PDF69–70); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, pp.28–29 (PDF19, página dupla). Consulta textual parcial aos recortes locais. Exemplo e exercícios originais; rascunho assistido por IA para revisão pessoal. Não atesta domínio de Jhuann. Próxima ação: resolver as cinco questões e explicar por que P(A)=P(B) não permite multiplicar as marginais.

Verificação do bloco de retiradas: 16 testes aprovados (13 do catálogo e três por enumeração de urnas, incluindo 88 composições com 2–12 bolas); 548 estruturas MathML e verificações de foco/ajuda de equações aprovadas. No navegador a 390 px, a questão 43 rejeitou 9/25 e aceitou 3/10; largura do documento 375 px, sem transbordamento da página, e nenhum erro de console observado. Prévia: condicional-urna-mobile.jpg. Aula atual: 41 seções/46 exercícios; trilha: 16 aulas/189 exercícios. Cobertura recalculada a partir do catálogo; nenhum mapa declarado completo. Não se repetiu a suíte global dos demais laboratórios. Saldo semanal conferido após o bloco: 91%; parada em 65%. Para aprofundar contagem e número de vermelhas, seguir a aula existente “Sem reposição: condicionais, contagem e distribuição hipergeométrica”, sem duplicar esse percurso.
