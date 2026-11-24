# Taxas condicionais e composição dos grupos

Rascunho didático original — 27/10/2026. Revisão de Jhuann pendente.

## Tabela sintética

| Método | Fácil | Difícil | Total |
|---|---|---|---|
| A |9/10|18/30|27/40|
| B |24/30|5/10|29/40|

Cada célula indica sucessos/total. Não são dados reais.

## A mesma pergunta precisa da mesma população

Pré-requisitos: frações, eventos, partições e a aula de condicionamento. Vamos comparar dois métodos A e B em tarefas classificadas previamente como fáceis ou difíceis. Os números são inventados: não são dados de empregadores, de uma pesquisa ou de um aluno. “Sucesso” significa cumprir o critério da tarefa, definido antes da comparação. Uma observação é uma tarefa registrada; sorteá-la uniformemente da tabela transforma as contagens em probabilidades empíricas. Não estamos estimando automaticamente a chance de sucesso em novas tarefas.

## Declare a tabela antes da taxa

O método A tem 9 sucessos em 10 tarefas fáceis e 18 em 30 difíceis; B tem 24 em 30 fáceis e 5 em 10 difíceis. Cada método possui 40 registros, totalizando 80. S é o evento sucesso, M_A é usar A, e F e D são os dois estratos de dificuldade, disjuntos e exaustivos. Usaremos r_AF para P(S|M_A∩F), e assim por diante. Cada célula tem total positivo: a razão está definida.

## Dentro de cada grupo, A tem maior taxa

Entre as fáceis: r_AF=9/10=90% e r_BF=24/30=80%. Entre as difíceis: r_AD=18/30=60% e r_BD=5/10=50%. A diferença é de 10 pontos percentuais nos dois estratos. Isso é uma diferença entre taxas, não um aumento relativo de 10%: entre as fáceis o aumento relativo é (0,9−0,8)/0,8=12,5%. As comparações ainda são descritivas.

## No total observado, a ordem se inverte

A soma dos sucessos de A é 9+18=27: taxa bruta 27/40=67,5%. B soma 24+5=29: 29/40=72,5%. Logo A fica 5 pontos percentuais abaixo de B no agregado, apesar de superar B nos dois grupos. Essa inversão por agregação é uma forma do paradoxo de Simpson. Nenhuma conta está em contradição: os denominadores descrevem composições diferentes.

## O denominador também decide o peso

Entre as tarefas de A, apenas 10/40=1/4 são fáceis; em B, 30/40=3/4 são fáceis. A recebe mais tarefas do estrato de menor taxa. São pesos condicionados ao método: P(F|M_A) e P(F|M_B). Substituí-los por P(F)=40/80=1/2 mudaria a pergunta. Esse 1/2 pode ser escolhido como peso comum para outra comparação, mas não reconstrói a taxa bruta de cada método.

## Probabilidade total dentro de um método

Fixe M_A como informação disponível. Os eventos S∩F e S∩D são disjuntos e cobrem S. Divida suas massas por P(M_A) e aplique a regra do produto dentro dessa condição. Assim a taxa de A é a soma das taxas nos grupos multiplicadas pelas proporções desses grupos entre as tarefas de A. A mesma derivação vale para B; não exige independência entre método e dificuldade.

P(S|M_A) = r_AF P(F|M_A) + r_AD P(D|M_A)

## Reconstruir as duas misturas confere a tabela

A: (9/10)(1/4)+(3/5)(3/4)=9/40+18/40=27/40. B: (4/5)(3/4)+(1/2)(1/4)=24/40+5/40=29/40. As parcelas são contribuições para o total do método, não probabilidades isoladas de sucesso dado o estrato. A média simples 75% das duas taxas de A não é sua taxa bruta, porque os estratos têm tamanhos diferentes.

## Leia a figura com os denominadores

As barras começam em zero e usam a mesma escala. Os dois primeiros pares comparam estratos; o terceiro usa as composições observadas diferentes; o último usa pesos comuns iguais. Leia junto as contagens da tabela: o gráfico de taxas sozinho não informa quantos registros existem nem a incerteza de cada taxa.

## Padronizar significa declarar outra mistura

Escolha uma população de referência com metade de tarefas fáceis e metade difíceis. A taxa padronizada é 1/2 vezes cada taxa de estrato: A dá 3/4=75%; B, 13/20=65%. Essa mistura sintética responde como as taxas se comparam usando a mesma composição de referência. Não observamos novas execuções nem provamos que a taxa se transferirá a uma população futura. Outra referência pode ser mais pertinente; a escolha deve ser justificada.

## Por que pesos comuns preservam a ordem?

Se w_F e w_D são não negativos, somam 1 e são os mesmos para A e B, a diferença padronizada é a soma ponderada das diferenças por estrato. Quando cada diferença é não negativa, a soma também é. Se há diferença estritamente positiva em algum estrato de peso positivo, a soma é positiva. Aqui ambas são 1/10, então qualquer mistura comum vale 1/10, inclusive pesos 0 e 1. A inversão bruta usa pesos diferentes e não satisfaz essa hipótese.

Δ = w_F(r_AF − r_BF) + w_D(r_AD − r_BD)

## Estrato ausente não tem taxa zero

Se um método não tiver nenhuma tarefa difícil, sua taxa nesse estrato será 0/0. Não preencha com zero, mesmo que o programa aceite uma tabela vazia em outro contexto. O laboratório exige total positivo em cada estrato para tornar a comparação identificada pela tabela. Seria preciso obter dados, restringir a referência ou acrescentar um modelo e suas hipóteses.

## Associação não determina qual método escolher

O exemplo não informa por que as tarefas foram distribuídas, como a dificuldade foi definida ou se existem diferenças adicionais. Pode haver seleção por dificuldade ou por características não registradas. Condicionar em uma variável arbitrária não garante remover vieses; a variável e o desenho precisam de justificativa. Não concluímos superioridade causal nem recomendamos um método real. Para uma avaliação, definir previamente tarefa, sucesso, distribuição-alvo e mecanismo de atribuição é parte do trabalho.

## O código verifica contas; não valida o desenho

O laboratório usa Fraction para manter as razões exatas. Confere as taxas brutas também por registros individuais, preservação da ordem com pesos comuns, extremos e mudança da composição. A prova da preservação da ordem está na soma anterior; uma enumeração finita não a substitui. Não há intervalos de confiança, teste estatístico, custos, dependência entre tarefas ou calibração neste recorte.

## Uma sessão de revisão de vinte minutos

Sem consultar a solução, reconstrua 27/40 e 29/40, escreva os pesos 1/4 e 3/4, e depois obtenha 3/4 e 13/20 usando pesos iguais. Explique qual pergunta cada comparação responde. Este material é rascunho para sua revisão e não comprova domínio pessoal. Próximo aprofundamento: escolher uma distribuição-alvo e discutir incerteza e dependência em avaliações de modelos, sem tratar tarefas correlacionadas como ensaios independentes por conveniência.

## Exercícios e resoluções

Na tabela da aula, qual é a taxa de sucesso de A entre as tarefas fáceis?

**Resolução:** 9/10=0,9. O denominador inclui apenas as dez tarefas fáceis de A.

Qual é a taxa de B entre as tarefas difíceis?

**Resolução:** 5/10=1/2.

Que fração das tarefas de A é fácil?

**Resolução:** 10/(10+30)=1/4.

Que fração das tarefas de B é fácil?

**Resolução:** 30/(30+10)=3/4.

Qual é a taxa bruta de A, como fração ou decimal?

**Resolução:** (9+18)/(10+30)=27/40.

Qual é a taxa bruta de B?

**Resolução:** (24+5)/(30+10)=29/40.

Com pesos 1/2 para cada dificuldade, qual é a taxa padronizada de A?

**Resolução:** (1/2)(9/10)+(1/2)(3/5)=3/4.

Com os mesmos pesos iguais, qual é a taxa padronizada de B?

**Resolução:** (1/2)(4/5)+(1/2)(1/2)=13/20.

Em pontos percentuais, quanto A supera B na mistura de pesos iguais?

**Resolução:** 100(3/4−13/20)=10 pontos percentuais.

Se a referência tiver 3/4 de tarefas fáceis e 1/4 difíceis, qual a taxa padronizada de A?

**Resolução:** (3/4)(9/10)+(1/4)(3/5)=33/40.

A tabela prova que usar A causa mais sucessos?

**Resolução:** A tabela é descritiva; atribuição de tarefas e diferenças adicionais não foram controladas.

Se não houver tarefas difíceis de A, podemos atribuir taxa zero nesse estrato?

**Resolução:** A razão é 0/0; ausência de registros não é evidência de taxa zero.

## Fontes e limites

Consulta textual parcial em 27/10/2026: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.54–55 e59 (PDF69–70/74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, definição1.3 e Teorema1.3, pp.28–29 (PDF19, página dupla). Fundamentos de condicional, produto e probabilidade total. Extração PVA com colunas intercaladas. Comparação de métodos, números, padronização, deduções e exercícios próprios; não atribuídos aos exemplos dos livros. Sem leitura integral ou distribuição dos exemplares privados.

O exemplar de Noções gerou avisos de extração de imagens; os recortes textuais citados estavam legíveis. Não se afirma nova inspeção visual ou leitura integral. A convenção de extensão da condicional em evento nulo dos livros não torna 0/0 uma razão definida; o laboratório rejeita estrato sem registros.

Executar: `python3 -m unittest discover -s labs/taxas-condicionais -t .` e `python3 labs/taxas-condicionais/rates.py`. API limitada a contagens inteiras, totais positivos e pesos racionais não negativos cuja soma é1. Nenhuma estimação estatística ou avaliação causal é implementada.

Próxima revisão: reconstruir as duas misturas sem consultar. Próxima elaboração: desenho de avaliação e incerteza, sem atribuir independência a tarefas correlacionadas.
