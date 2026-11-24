# Roteiro próprio: força, previsão e explicação

Primeiro recorte de Ensino de Física4300356. Rascunho de preparação docente, ainda não aplicado. Não é material de estágio realizado, coleta com alunos, certificação de competência ou protocolo de eficácia comprovada.

## Objetivo observável

Ao final, explicar por que resultante horizontal nula permite velocidade constante num referencial inercial e distinguir esse caso de resultante constante não nula. Não basta acertar um número: pedir desenho de forças, previsão e justificativa das hipóteses.

## Enunciado para a primeira previsão

Um carrinho passa a mover-se a3m/s num plano horizontal. A mão que o empurrou deixa de tocá-lo. No modelo ideal, despreze atrito e resistência do ar; não há outra interação horizontal. Referencial inercial; movimento vertical ausente. O que acontece com a velocidade depois? Quais forças ainda atuam? Escreva ou dite sua justificativa antes de ver a tabela.

Peso e normal podem continuar presentes e se equilibrar verticalmente. Resultante horizontal zero não é ausência de toda força nem velocidade zero. Nenhum material precisa ser lançado ou experimentado para estudar este roteiro; uma futura atividade física exige planejamento próprio de espaço, medidas e limites.

## Sequência sugerida, adaptável

1. Apresentar objetivo e hipóteses; esclarecer vocabulário sem fornecer a conclusão.
2. Registrar previsão e motivo individualmente, em texto, desenho ou fala. Não registrar dados identificadores neste protótipo.
3. Pedir que cada explicação nomeie interações após a mão sair.
4. Comparar com a tabela SINTÉTICA abaixo e explicitar como ela foi gerada. Ela representa o modelo que queremos estudar, não observação independente que o confirma.
5. Reescrever a justificativa distinguindo força resultante e velocidade; pedir diagrama de forças e uma condição que mudaria a previsão.
6. Transferir para o segundo caso e depois para um carrinho real que desacelera. Comparar explicações, sem pressupor que uma resposta correta encerra a aprendizagem.

Duração não foi validada; ajustar à pessoa, linguagem e condições da aula. A sequência é elaboração nossa, inspirada na necessidade de explicitar e contextualizar ideias, não um protocolo atribuído a Mortimer.

## Tabelas calculadas, não observadas

m=2kg,v0=3m/s,x0=0,t em segundos. CasoA:Fhorizontal=0; casoB:resultante horizontal constante+2N. Peso/normal equilibrados no eixo vertical; sem outras forças horizontais.

| t(s) | xA(m) | vA(m/s) | xB(m) | vB(m/s) |
|---|---|---|---|---|
| 0 | 0 | 3 | 0 | 3 |
| 1 | 3 | 3 | 7/2 | 4 |
| 2 | 6 | 3 | 8 | 5 |
| 3 | 9 | 3 | 27/2 | 6 |

B usa a=F/m=1m/s². A usa a=0. Para força constante,x=v0t+at²/2 e v=v0+at. As condições iniciais têm de aparecer. Estes resultados não demonstram que uma pista real não tem atrito.

## Cartões de resposta fictícios e devolutiva

A: “Vai parar porque a força do empurrão vai acabando.” Hipótese a investigar: a pessoa pode relacionar força a manutenção da velocidade ou estar pensando em resistência real. Pergunta: depois que a mão sai, qual objeto/interação exerce a força horizontal que você está descrevendo? Não atribuir automaticamente uma concepção estável a uma frase.

B: “Continua porque não tem força.” Pedir: você quer dizer resultante horizontal? Peso e normal deixam de existir? A conclusão sobre velocidade pode estar correta e a descrição das forças precisar de precisão.

C: “A resultante horizontal é zero e a velocidade permanece3m/s; peso e normal se equilibram verticalmente.” Pedir um novo caso de força horizontal constante e uma situação real que viole a idealização. Uma explicação adequada aqui não comprova transferência ou domínio geral.

Nenhum cartão veio de estudante real. Não se deduz nível cognitivo, diagnóstico psicológico ou perfil conceitual de uma única resposta.

## Critérios de análise abertos, sem nota automática

| Critério | Evidência a procurar | Próxima pergunta | Limite da inferência |
|---|---|---|---|
| Interações | Nomeia agentes/forças depois do contato | Quem exerce cada força? | Lista de nomes pode não justificar a resultante |
| Relação força–movimento | Relaciona resultante a aceleração | Velocidade zero é necessária? | Fórmula decorada pode coexistir com outra explicação |
| Hipóteses | Separa modelo ideal e pista real | Qual efeito faria desacelerar? | Reconhecer atrito não mede seu valor |
| Transferência | Explica casoB e revê a própria previsão | O que muda se a força muda de sentido? | Um item novo não encerra a avaliação |

Usar o retorno para ajustar a próxima explicação, não para rotular a pessoa. Os exercícios fechados do site verificam leitura/cálculos deste caso; a resposta aberta exige apreciação humana e diálogo.

## Acesso e alternativas

Oferecer tabela e descrição textual junto ao diagrama; não depender só de cor ou arrastar controle. Aceitar descrição oral, escrita ou desenho com explicação. Se programação for barreira, a atividade funciona com a tabela impressa. Isso é planejamento de acesso, não afirmação de que todas as necessidades de uma turma foram atendidas.

## Gerador opcional e verificação

`python3 labs/ensino-forca/model.py`

`python3 -m unittest discover -s labs/ensino-forca -t .`

Só biblioteca padrão, frações exatas. Quatro testes: duas tabelas,54 configurações com recorrência independente por velocidade média/impulso e trabalho–energia, tempos fracionários e contratos. Verificam consistência do MODELO e do programa, não aprendizagem, eficácia ou validade experimental. Código opcional: não é pré-requisito para discutir a atividade.

## Fundamentação e alcance

Mortimer, Linguagem e formação de conceitos no ensino de ciências, Ed.UFMG2000: ficha do excerto Texto7/PDF2, abertura do capítulo1/PDF3 (sem página impressa visível), e continuação Texto7ParteII, páginas marcadas58–61/PDF1–4, consulta parcial em29/10/2026. Abertura e página marcada60/PDF3 da ParteII inspecionadas visualmente. Trata-se de excertos/material de trabalho, não exemplar integral; não transferimos paginação automaticamente entre edições. Programa USP4300356 reaberto em29/10/2026, ativação15/07/2022 e captura indicada de três meses antes; execução da turma não comprovada. Artigo Mortimer1996 localizado no índice público, mas abertura do corpo falhou; não foi usado como leitura integral nem fonte de uma estratégia validada.

A leitura de Mortimer fundamenta o cuidado em não reduzir aprender a apagar expressões cotidianas, nem identificar um pensamento completo com um acerto isolado. A aplicação ao carrinho, os cartões e os critérios são elaboração original: não resultados do autor ou evidências empíricas novas.

[Programa oficial](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=4300356)

Sem cópias dos PDFs privados, dados de alunos ou registro de aula aplicada. Próxima revisão pessoal: responder ao caso sem consultar, revisar física e linguagem, ensaiar as perguntas e justificar o que cada evidência permite concluir. Outros eixos da disciplina continuam pendentes.
