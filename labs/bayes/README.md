# Bayes: combinar base e informação do detector


13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.


## Objetivos

- Derivar Bayes a partir de duas fatorações da mesma conjunta.
- Montar uma tabela de probabilidades ou contagens esperadas.
- Distinguir sensibilidade, falso positivo e probabilidade posterior.
- Investigar efeito da base e tratar explicitamente denominador zero.


## Duas fatorações da mesma conjunta

Denote por D o evento defeito e por + o sinal positivo. A mesma conjunta é P(D∩+)=P(+|D)P(D)=P(D|+)P(+). Divida por P(+)>0 para obter Bayes. Nenhuma causalidade é necessária para essa identidade; ela reorganiza probabilidades condicionais.

P(D|+)=P(+|D)P(D)/P(+)


## Defina cada parâmetro antes de calcular

p=P(D) é a proporção de defeitos, s=P(+|D) é a sensibilidade e f=P(+|não D) é a taxa de falso positivo entre peças sem defeito. A probabilidade de uma peça sem defeito entre as sinalizadas é outra condicional: P(não D|+). Ela não é f.

p=P(D); s=P(+|D); f=P(+|não D)


## O denominador reúne dois caminhos

D e não D formam uma partição. Um sinal pode vir de uma peça defeituosa ou de uma peça sem defeito. A probabilidade total de sinal é sp+f(1−p). O numerador sp conta apenas defeituosas sinalizadas; o denominador reúne todas as sinalizadas.

P(D|+)=sp/[sp+f(1−p)]


## Uma tabela torna a base visível

No modelo p=0,1, s=0,8, f=0,2, entre 1000 peças esperamos 100 defeituosas e 900 sem defeito. Os grupos esperados são: 80 defeituosas sinalizadas, 20 defeituosas sem sinal, 180 sem defeito sinalizadas e 720 sem defeito sem sinal. Esses são valores esperados sintéticos; uma amostra real não precisa ter exatamente essas contagens.

Defeito: [80,20]; sem defeito: [180,720]


## A posterior não é a sensibilidade

Entre as 260 sinalizadas esperadas, 80 são defeituosas. A posterior é 80/260=4/13≈0,30769. A sensibilidade 80/100=0,8 responde a outra pergunta, com outra população de referência. Aqui a maioria das sinalizadas é sem defeito, embora a sensibilidade seja 80%.

P(D|+)=4/13; P(+|D)=4/5


## A base pode mudar a interpretação

Mantendo s=0,8 e f=0,2, trocar p de 0,1 para 0,5 dá posterior 0,4/(0,4+0,1)=0,8. Em uma população com defeitos raros, a massa das peças sem defeito pode gerar muitos sinais falsos. Transportar uma posterior de uma fábrica para outra requer justificar a base e as taxas relevantes.

p=1/2 → P(D|+)=4/5


## A ausência de sinal também informa

No exemplo, esperamos 20 defeituosas e 720 sem defeito no grupo sem sinal. Assim P(D|−)=20/740=1/37. Não é simplesmente 1−s: esse último é P(−|D). A posterior negativa requer seu próprio denominador, P(−).

P(D|−)=p(1−s)/[p(1−s)+(1−p)(1−f)]


## Casos limites conferem a interpretação

Se s=f e P(+)>0, o sinal tem a mesma probabilidade nos dois estados e a posterior permanece p. Se s=1, f=0 e p>0, todo sinal indica defeito no modelo. Se P(+)=0, a posterior positiva é indefinida pela fórmula; isso inclui situações com p=0 e f=0. O código retorna None para esse caso.




## O código confere contas, não calibra um detector

Fraction mantém probabilidades racionais exatas neste pequeno modelo. A tabela fecha seus totais e as posteriores usam as colunas apropriadas. Isso testa a implementação da conta. Não demonstra que as taxas sintéticas representam um equipamento real, nem que o detector tem boa utilidade na prática.




## Para sair do modelo e trabalhar com dados

Uma aplicação real exige esclarecer como as peças foram escolhidas, como o estado verdadeiro foi medido, se as taxas mudam entre lotes e qual a incerteza das estimativas. Custos de falso positivo e falso negativo também influenciam decisões. Bayes sozinho não resolve o desenho de coleta, não prova causa e não elimina incerteza.




## Exemplo resolvido

Qual a chance de defeito entre peças sinalizadas e entre peças sem sinal?

1. Fixe o modelo sintético p=1/10, s=4/5 e f=1/5.
2. Em 1000 peças, a tabela esperada tem linhas [80,20] e [180,720].
3. Na coluna sinal: 80/(80+180)=4/13.
4. Na coluna sem sinal: 20/(20+720)=1/37.
5. 80/100=4/5 é a sensibilidade, com denominador distinto.
6. São expectativas do modelo, não uma coleta de 1000 peças observada.


## Exercícios e resoluções


### No modelo p=0,1, s=0,8, f=0,2, qual é P(D|+)?



4/13≈0,30769.


### P(defeito|sinal) é sempre igual a P(sinal|defeito)?

Sim
Não

As condições são diferentes.


### No mesmo modelo, quanto é P(+)?



0,1×0,8+0,9×0,2=0,26.


### Qual é P(D|−) no mesmo modelo?



20/(20+720)=1/37.


### Mantendo s=0,8 e f=0,2, use p=0,5. Qual é P(D|+)?



0,4/(0,4+0,1)=0,8.


### A taxa f=0,2 mede qual probabilidade?

P(não D|+)
P(+|não D)

A condição são as peças sem defeito.


### Se P(+)=0, qual o tratamento desta fórmula elementar?

Posterior automaticamente zero
Condicional indefinida pela divisão

Uma divisão por zero não define a posterior.


### Se s=f e P(+)>0, a posterior positiva é:

A própria base p
Sempre 1/2

A taxa comum cancela no numerador e denominador.


### A tabela esperada de 1000 peças demonstra uma coleta real?

Sim, são observações
Não, são expectativas sintéticas

As contagens derivam dos parâmetros do modelo e não de arquivos observados.


## Python

Execute com Python 3, somente biblioteca padrão: `python3 experiment.py`. Sem leitura de dados privados ou escrita de resultados externos.


## Hipóteses e limites

- Modelo sintético com estados D/não D formando uma partição.
- p, s e f são probabilidades hipotéticas; contagens são expectativas.
- Posterior positiva exige P(+)>0; a negativa exige P(−)>0.
- Não é validação de detector, estimativa empírica ou resultado da IC.


## Continuação — razões de chances e taxa-base, 22/10/2026

A aula `pe-bayes` passa de 10 para 15 seções e de 9 para 14 exercícios, preservando os anteriores. Acrescentadas definições de odds O=p/(1−p), conversão p=O/(1+O), derivação da atualização O(D|+)=O(D)×s/f, distinção entre favorecer e tornar majoritário e limiar de base p*=f/(s+f) para posterior 1/2. A conta não escolhe uma política de aceitação: custos e consequências permanecem fora do modelo.

Exemplo original mantido: p=1/10,s=4/5,f=1/5; odds anterior1/9, fator4, odds posterior4/9, probabilidade4/13. Com p=1/5, posterior1/2; o painel existente confirma o resultado. Sem nova hipótese de independência entre sinais ou dados reais.

Fontes privadas consultadas parcialmente: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.58–59 (PDF73–74); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, p.30 (PDF20, página dupla; página vizinha31 não é referência deste bloco). Partição e Bayes conferidos por extração local. O extrator de Noções emitiu avisos de compressão, mas o texto relevante da definição, teorema e demonstração foi recuperado legível. A forma em odds e seu limiar são derivações próprias a partir de Bayes; não se afirma que esses tópicos foram lidos nesses recortes. Nenhum exercício, figura ou PDF privado foi reproduzido.

`odds.py` aceita somente int/Fraction estritamente entre 0 e 1 para os três parâmetros. A restrição permite razões finitas sem dividir por zero; extremos continuam disponíveis no `experiment.py` anterior. Não é estimativa, calibração de detector ou resultado da IC.

Na raiz do protótipo:

```sh
python3 labs/bayes/odds.py
python3 -m unittest labs.bayes.test_odds
```

Quatro testes novos: 729 combinações confrontadas com enumeração independente de 1000 átomos equiprováveis por combinação; empate exato e posições abaixo/acima do limiar para nove pares de taxas; fator neutro/favorável/desfavorável e contraexemplo à maioria; contratos inválidos. Suíte completa com 751 testes Python aprovada; 438 estruturas MathML conferidas. Navegador: resposta decimal 0,2 aceita; controle por teclado em p=0,20 produz posterior0,5 e sinal0,32. Layout390px sem transbordamento horizontal, sem erros de console observados, viewport restaurado. Prévia na raiz: `bayes-razoes-mobile.jpg`.

Catálogo atual: 485 aulas/2507 exercícios. Percurso complementar de probabilidade e estatística: 15 aulas/145 exercícios. Não implica conclusão curricular, domínio de Jhuann ou validação com alunos. Próxima revisão neste tema: explicar os denominadores e comparar detector informativo com decisão por custo. Próxima alternância global: auditar a sequência de Física II e suas lacunas antes de acrescentar outro tópico. Saldo após o bloco75%; parada65%.


## 27/10/2026 — primeira ocorrência e informação resumida

Extensão original de `pe-bayes`: cinco seções e cinco exercícios. Hipóteses fixas equiprováveis, taxas 3/4 e 1/4, tentativas condicionalmente independentes, até três. Registro T=3 equivale a 001, evidência 3/32 e posterior 1/4. Registro T≤3 tem evidência 25/32 e posterior 63/100. Registro 000 tem posterior 1/28. No protocolo de duas tentativas fixas, observar 01 e parar com T=2 revelam o mesmo prefixo: evidência 3/16 e posterior 1/2. Contar exatamente um sucesso reúne 01 e 10: evidência 3/8, mas a mesma posterior pelo fator comum. Essa equivalência depende do protocolo especificado; não é um resultado geral sobre testes com parada.

Fontes: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2 pp.54–55 e 59 (PDF69–70 e 74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3 pp.28–30 (PDF19–20, páginas duplas). Reconferência textual parcial em 27/10/2026, com limitações de OCR; sem leitura integral ou nova inspeção visual. Definição, produto e Bayes fundamentam a dedução original. Não se atribui o experimento aos autores nem se distribuem os livros privados.

Execute `python3 labs/bayes/stopping.py`. Oito sequências potenciais são enumeradas; os registros 1, 01, 001 e 000 particionam o espaço. Frações exatas, casos de evidência zero e normalização; verificações finitas não substituem as deduções. Python opcional. Taxas desconhecidas, seleção não especificada e inferência frequentista com parada continuam pendentes. Revisão de Jhuann pendente.


## 27/10/2026 — resumir registros: média com os pesos corretos

`pe-bayes` recebeu quatro seções e quatro exercícios: agora 24 seções/23 exercícios. Dado sucesso até a terceira tentativa, os registros 1, 01 e 001 têm pesos 16/25, 6/25 e 3/25. Suas posteriores 3/4, 1/2 e 1/4 dão média ponderada 63/100, em vez da média simples 1/2. Demonstração pela probabilidade total; massa zero não exige definir posterior. Antes de qualquer registro, a média das quatro posteriores recupera a prévia 1/2. Isso não garante calibração em dados ou que cada informação favoreça a mesma hipótese. Modelo e figura originais.

Referências reconferidas textualmente em 27/10/2026: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2 pp.54–55 e 59/PDF69–70 e 74; Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3 pp.28–30/PDF19–20 (páginas duplas). Consulta parcial, OCR imperfeito, sem nova inspeção dos PDFs nem leitura integral. Definição, produto, probabilidade total e Bayes sustentam a dedução própria; o protocolo não é atribuído aos livros. Não houve nova auditoria curricular.

`labs/bayes/coarsening.py`: três testes aprovados, incluindo 125 modelos × 16 subconjuntos de registros, fórmulas de prefixo independentes da enumeração, pesos/posteriores, casos de massa zero e contrato de partição. Grade finita verifica implementação, não substitui a demonstração. 14 testes do catálogo e 862 estruturas MathML aprovados. Navegador móvel de 390px rejeitou 1/2 e aceitou 63/100; largura do documento 390px, sem erros observados no console. Figura inspecionada em `condicional-media-mobile.jpg`. Windows real, leitor de tela e revisão pessoal pendentes.

Probabilidade/estatística: 25 aulas/342 exercícios, complemento em elaboração. Global: 51 trilhas, 573 aulas/5214 exercícios, 145 introduções curtas. Contagens não comprovam domínio ou cobertura integral. Durante os testes, recursos ausentes de `c2-comparacao`, preparados anteriormente, foram completados em `labs/comparacao-caudas/`: figura, notas e certificado racional, três testes aprovados. Cálculo 2 tem 21 aulas/217 exercícios e duas introduções curtas; revisão de interface desse recorte ainda pendente.

Próxima ação de estudo (20 minutos): reconstruir as quatro massas, renormalizar os três registros de sucesso e explicar por que 1/2 não responde à pergunta do resumo. Próxima elaboração: revisar o percurso de condicionamento para reduzir repetição e tornar os pré-requisitos visíveis antes de acrescentar mais extensões. Saldo semanal antes/depois: 68%; parada operacional em 65% mantida.
