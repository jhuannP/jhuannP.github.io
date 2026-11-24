# Roteiro de estudo — probabilidade condicional

Preparado em 26/10/2026. Material original assistido por IA, em rascunho para revisão pessoal. Aulas, código e roteiro preparados não comprovam domínio de Jhuann. Esta é uma sequência de revisão, não o programa completo de probabilidade e estatística.

No site, abra **Biblioteca → Probabilidade e estatística → Abrir percurso de estudo**. Cada etapa é expansível, com leituras, entrega e links às aulas. Dentro das aulas, o sumário leva aos títulos citados. Não é necessário ler todas as seções de uma vez.

## Escolha um caminho depois dos fundamentos

Comece nas etapas **1–4**. Elas constroem eventos, massas, atualização em etapas e Bayes. Não é necessário concluir as 19 etapas para usar a primeira aplicação.

| Interesse | Depois das etapas 1–4 | O que precisa acrescentar |
|---|---|---|
| Primeiro sucesso e informação resumida | 18 → 19 | Apenas frações e probabilidade total; sem cálculo |
| Urnas e observações imperfeitas | 5 → 6 | Contagem sem reposição; separar resultado de relato |
| Taxas e mecanismos de registro | 7 → 8 → 9 | Tabelas conjuntas e hipóteses sobre a coleta |
| Informação contínua e previsão | 10 → 11 → 12 → 13 → 14 → 15 | Densidades, integral definida e, para previsão, momentos/variância |
| Tempos de espera | Aula de exponencial → 16 → 17 | Exponencial e integral; etapa 17 também compara uma versão por densidade |

Os números continuam estáveis para preservar os links do site. A ordem da lista não cria dependências entre caminhos: o bloco finito 18–19 pode vir antes do contínuo. Cada entrega é uma proposta de estudo, não um registro de domínio. Dentro de uma aula longa, use o sumário para ir aos títulos indicados.

## Como usar cada sessão

1. Escolha uma entrega e escreva os eventos e o protocolo.
2. Tente a conta antes de ler a resolução; registre onde travou.
3. Compare o denominador, a normalização e as hipóteses, não só o número final.
4. Execute o código depois de reconstruir o raciocínio. Um resultado aprovado no exercício é evidência local, não certificação de aprendizagem.

O tempo é uma sugestão de sessão, não um prazo. Se o raciocínio não estiver claro, retome a mesma entrega. Python não é pré-requisito para as contas finitas.

## 1. Escolher o denominador — 20 minutos

Noções, 7ª ed., §2.2, pp.54–55 (PDF69–70), e PVA, 2ª ed., §1.3, pp.26–29 (PDF18–19, páginas duplas): recortes parcialmente consultados. Comece nas seções “A informação define o denominador” e “A pergunta inversa muda a referência”. Para este bloco bastam frações e conjuntos; o cálculo será necessário em aulas posteriores de densidade.

**Entrega:** No dado justo com A={2,4,6} e B={4,5}, desenhar a interseção e calcular P(A|B)=1/2 e P(B|A)=1/3. Explicar em uma frase por que os denominadores mudam antes de abrir a resolução.

**Aulas:** `pe-eventos` — Eventos: conjuntos e regra da união, `pe-condicional` — Condicionamento: mudar a informação disponível.

## 2. Trocar contagem por massa — 20 minutos

Os mesmos fundamentos de restrição e renormalização; na aula de condicionamento, seguir de “Quatro rótulos, quatro pesos diferentes” até “Um evento não vazio pode ter massa zero”. O exemplo de pesos é próprio. Não supor que nomes sobreviventes se tornam equiprováveis.

**Entrega:** Usar pesos a=1,b=2,c=3,d=4 e B={b,c}. Escrever a distribuição condicionada (0,2/5,3/5,0), conferir a soma e explicar por que contar rótulos daria uma resposta errada. Distinguir conjunto vazio de conjunto não vazio com massa zero.

**Aulas:** `pe-condicional` — Condicionamento: mudar a informação disponível.

## 3. Receber duas informações — dois blocos de 20 minutos

Noções §2.2, pp.54–58 (PDF69–73); PVA §1.3, pp.26–29 e35 (PDF18–19/22), consulta parcial. Na aula de condicionamento, estudar a atualização em etapas e depois “Quando uma condição pode ser retirada?”. São duas sessões, não uma leitura de todas as 41 seções.

**Entrega:** Primeiro: reconstruir as massas 10,5,3 do exemplo de cinco resultados e obter P(A|B∩C)=3/5. Depois: enumerar os quatro pares de moedas e mostrar por que independência antes da seleção não implica independência dado que as moedas são iguais. Só retirar uma condição após justificar a fatoração.

**Aulas:** `pe-condicional` — Condicionamento: mudar a informação disponível, `pe-independencia` — Independência: uma hipótese de fatoração.

## 4. Misturar e inverter dentro da informação disponível — 20 minutos

Noções §2.2, p.59 (PDF74); PVA §1.3, Teorema1.4, p.30 (PDF20), consulta parcial. Na aula de condicionamento, retomar “Probabilidade total depois de receber uma informação” e “Bayes sem apagar a informação anterior”. Aplicação dentro de C deduzida nas notas.

**Entrega:** Com C={2,3,4,5,6}, O={1,3,5} e A={2,3,5}, obter P(O|C)=2/5, P(A|C)=3/5 e P(O|A∩C)=2/3. Explicar por que a taxa P(A|O∩C)=1 não pode ser substituída por P(A|O)=2/3 durante a mistura.

**Aulas:** `pe-condicional` — Condicionamento: mudar a informação disponível, `pe-bayes` — Bayes: combinar base e informação do detector.

## 5. Declarar como os dados chegam — 20 minutos

Definição, produto e Bayes nos recortes anteriores. Aulas e protocolos originais: “A informação depende de como observamos” e “Sem reposição: o espaço contém objetos identificados”. O mecanismo do experimento faz parte do modelo.

**Entrega:** Escolher um dos dois casos: enumerar os oito átomos do protocolo de indicadores; ou enumerar os 20 pares de bolas de uma urna com três vermelhas e duas azuis. No segundo caso, justificar P(VV)=3/10 e comparar com 9/25 sob reposição e sorteios independentes.

**Aulas:** `pe-condicional` — Condicionamento: mudar a informação disponível, `pe-sem-reposicao` — Sem reposição: condicionais, contagem e distribuição hipergeométrica.

## 6. Separar hipótese, cor e relato — três blocos de 20 minutos

Na aula de composição desconhecida: primeiro as duas hipóteses de urna; depois sequência e contagem; por último as seis seções do sensor. Bayes nos recortes anteriores; hipergeométrica em Noções §3.3, p.94 (PDF109), e PVA §2.3, p.87 (PDF48), consulta parcial. A extensão do sensor é própria.

**Entrega:** Sessão1: após uma vermelha conhecida, obter posterior2/3 e previsão1/3. Sessão2: em N=6, distinguir evidência2/5 da contagem e2/15 de VVA, com posterior3/4 em ambos. Sessão3: após o relato do sensor com erro, reconstruir os quatro estados e obter posterior3/5 e previsão2/5; explicar por que retirar automaticamente uma vermelha daria3/10.

**Aulas:** `pe-bayes-urna` — Composição desconhecida: atualizar hipóteses e prever a próxima retirada.

## 7. Comparar taxas com a mesma composição — 20 minutos

Condicional e probabilidade total: Noções §2.2, pp.54–55 e59 (PDF69–70/74); PVA §1.3, definição1.3 e Teorema1.3, pp.28–29 (PDF19), consulta textual parcial em 27/10. Exemplo de inversão e padronização original.

**Entrega:** Reconstruir as taxas brutas 27/40 e29/40, os pesos diferentes e as taxas de referência 3/4 e13/20. Explicar por que a inversão não é contradição e não prova causalidade.

**Aula:** `pe-taxas-condicionais` — Taxas condicionais: quando agregar inverte a comparação.

## 8. Conferir se o segundo relato traz informação nova — 20 minutos

Noções §2.2, pp.54–55 e59 (PDF69–70/74); PVA §1.3, pp.28–30 e35 (PDF19–20/22), consulta textual parcial em 27/10. Os três mecanismos de relatos são exemplos originais.

**Entrega:** Reconstruir uma tabela de oito células e explicar as posteriores 9/10, 3/4 e 21/26. Conferir a evidência zero de +− na cópia e os pesos atualizados dos modos na mistura.

**Aula:** `pe-relatos-repetidos`.

## 9. Incluir o registro na informação — 20 minutos

Noções §2.2, pp.54–55 e59 (PDF69–70/74); PVA §1.3, pp.28–30 e35 (PDF19–20/22), reconferência textual parcial em 27/10. Protocolos e exercícios originais, com taxas conhecidas por hipótese.

**Entrega:** Na aula `pe-selecao-relatos`, reconstruir as oito massas do protocolo B e obter P(H|S)=2/5, P(H|+∩S)=2/3 e P(H|Sᶜ)=2/3. Comparar com A e explicar a condição de cancelamento do filtro. Não inferir essas taxas de um conjunto real de registros.

## Registro pessoal — preencher ao estudar

| Etapa | Data | O que consegui reconstruir sem consultar | Dúvida ou erro a retomar |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 — atualização | | | |
| 3 — independência | | | |
| 4 | | | |
| 5 | | | |
| 6 — composição | | | |
| 6 — contagem | | | |
| 6 — sensor | | | |
| 7 — taxas e composição | | | |
| 8 — relatos repetidos | | | |
| 9 — seleção de registros | | | |
| 10 | | | |
| 11 | | | |
| 12 | | | |
| 13 | | | |
| 14 | | | |
| 15 | | | |
| 16 | | | |
| 17 | | | |
| 18 | | | |
| 19 | | | |

## Fontes e limites

As páginas impressas e as páginas do PDF são identificações distintas; PDF usa contagem a partir de1. Noções:7ª edição; PVA:2ª edição, duas páginas impressas por página do PDF nos recortes citados. Correspondências vêm dos registros e leituras locais já documentados em PROBABILIDADE_ESTATISTICA.md e nos READMEs dos laboratórios. Este roteiro não representa uma nova leitura integral das seções ou livros. A extração de PVA intercala colunas em alguns trechos. Exemplos, perguntas, código e sensor são elaborações próprias, não transcrições dos exercícios dos autores. Livros privados não são disponibilizados no site.

O tratamento elementar usado nos laboratórios retorna None para condição de massa zero. Noções p.54 menciona extensão arbitrária; essa convenção não torna a divisão por zero definida. Condicionamento contínuo exige outro tratamento, além destas razões finitas.

Ainda não são cobertos por este roteiro: inferência das taxas de erro, dados empíricos, causalidade, séries de relatos com erros correlacionados e o restante de densidades/inferência.

A etapa 8 cobre apenas dois relatos sob três mecanismos conhecidos; séries gerais com dependência desconhecida continuam pendentes.


## 10. Passar de eventos para densidades condicionais — dois blocos de 20 minutos

Preparado em 27/10/2026. Esta etapa exige densidades e integral definida. Retome `pe-densidade` antes de iniciar se necessário. Noções §2.2, pp.54–55/PDF69–70, para condicionamento por eventos; PVA §3.2, pp.128–133/PDF69–71, definição 3.6, razão por densidades, faixas e mistura. Reconferência textual parcial; sem leitura integral ou nova inspeção visual dos exemplares.

**Entrega:** primeiro normalizar f(x,y)=(6/5)(x²+y) no quadrado e reconstruir as marginais e 13/20. Depois comparar a cauda condicional em X=1/2, na versão contínua, com a faixa [1/4,3/4]: 2/3 versus 49/74. Deduzir o limite das faixas e explicar por que P(X=1/2)=0 não permite dividir 0/0, embora uma versão por densidades esteja definida. Exemplo original e sintético, sem ruído de instrumento.

**Aulas:** `pe-densidade` e `pe-condicional-continua` — Condicionamento contínuo: da faixa à densidade condicional. As nove etapas anteriores não exigem que você domine este recorte para começar a revisão.

## Continuação opcional: Bayes com uma observação por evento — 20min

Após a etapa contínua, revisar as cinco seções finais de `pe-condicional-continua`: A={Y>1/2}, B={X≤1/2}; reconstruir P(A|B)=5/7 e P(B|A)=5/13, normalizar a posterior e explicar3/5→15/26. Usar os mesmos fundamentos parcialmente consultados de Noções §2.2/PVA §3.2; atividade proposta, revisão pessoal pendente.

## 18. Primeira ocorrência ou ocorrência até um limite — 20 minutos

Após as etapas 1–4 e a apresentação inicial de Bayes, em `pe-bayes`, estudar de “Parar na primeira ocorrência: descreva o experimento” até “Atualize em etapas e confira o que não ocorreu”. Não depende da aula de exponencial ou das etapas contínuas. Fundamentos e referências parciais nos dois Magalhães registrados nas notas de Bayes. Reconstruir os quatro registros 1, 01, 001 e 000, conferir que suas evidências somam 1 e explicar a diferença entre as posteriores 1/4 e 63/100. Depois comparar sequência 01 com contagem de um sucesso em duas tentativas. Registro pessoal desta entrega ainda em branco; atividade preparada não comprova aprendizagem.

## 19. Combinar registros — 20 minutos

Após a etapa 18, em `pe-bayes`, seguir de “Resumir os registros exige novos pesos” até “Uma conferência global não prevê o resultado individual”. Reconstruir as quatro evidências, obter 16/25, 6/25 e 3/25 dentro do resumo e explicar 63/100 versus 1/2. Conferir com `labs/bayes/coarsening.py`; leitura pessoal ainda pendente.
