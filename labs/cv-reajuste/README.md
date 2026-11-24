# Validação cruzada e reajuste — notas de aula

Rascunho original para revisão de Jhuann.

## Cada fold cria um novo treino

Em k folds, cada bloco pode ser usado para validar o procedimento ajustado nos demais. Transformações e modelo precisam ser reaprendidos no treino daquele fold. Usar um transformador ajustado em todos os dados vaza informação.

fit do pipeline em cada fold

## A estratégia segue a estrutura dos dados

K-fold usual supõe uma divisão compatível com a tarefa. Grupos ou tempo podem exigir GroupKFold ou validação temporal. A média dos scores não corrige automaticamente uma divisão inadequada.

escolha da divisão é parte do método

## O teste final continua separado

Se os folds são usados para escolher hiperparâmetros, seus scores participam da seleção. Uma estimativa de todo o processo pode exigir teste separado ou validação aninhada. Scores de folds compartilham treinos e não são réplicas IID simples.

seleção interna ≠ avaliação externa

## Seis registros e três divisões explícitas

Use registros indexados de 0 a 5, com x=[−3,−2,−1,1,2,3] e y=[−5,−3,−1,3,5,11], todos adimensionais e inventados. Os blocos de validação são [0,5], [1,4] e [2,3]. Em cada linha, os outros quatro registros são treino. Os blocos foram fornecidos para tornar as contas reconstruíveis, não escolhidos como regra universal de divisão. Não há teste externo neste conjunto.



## Escolher uma família e uma convenção de perda

Ajustamos y≈a+bx minimizando a soma dos erros quadráticos no treino mais λb², sem penalizar a. Para cada treino, calcule suas médias x̄ e ȳ, Sxx=Σ(x−x̄)² e Sxy=Σ(x−x̄)(y−ȳ). Resolver as equações normais dá b=Sxy/(Sxx+λ) e a=ȳ−bx̄. Os candidatos são λ∈{0,1,4,16}; λ=0 é mínimos quadrados ordinários quando a inclinação é identificável. Não chamamos um solver externo.

b=Sxy/(Sxx+λ)

## Não reutilizar médias ou coeficientes de outro treino

As médias e somas do ajuste são recalculadas somente nos quatro registros de treino. Não há padronizador extra nesta implementação; se existisse imputação, escala ou seleção de atributos, cada etapa aprendida também teria que ser refeita com o treino do fold. O exemplo está ligado à aula anterior de vazamento, mas aqui já há ajuste de um modelo diferente por divisão.



## Abrir a primeira divisão sem saltos

Com validação [0,5], treinamos nos x=−2,−1,1,2 e y=−3,−1,3,5. Nesse treino, x̄=0, ȳ=1, Sxx=10 e Sxy=20. Para λ=0, a=1 e b=2. As previsões dos dois registros reservados são −5 e 7, frente a alvos −5 e 11. Os resíduos previsão−alvo são 0 e −4, os quadrados são 0 e 16 e o MSE do fold é 8. O alvo 11 não entrou no ajuste dessa reta.

MSE_fold0=(0²+(−4)²)/2=8

## Juntar previsões fora do treino

Para λ=0, os MSE dos três folds são 8, 61/25 e 205/169. Nosso score de seleção é o MSE agregado sobre os seis registros, cada um previsto pelo modelo que não o treinou. Como os blocos têm dois registros cada, a média dos três MSE coincide aqui com a média dos seis erros quadráticos: 49234/12675≈3,884339. Não são previsões de uma única reta ajustada em todos os registros.

MSE_OOF=(1/N)Σᵢ(ŷᵢ,fora−yᵢ)²

## Pesos importam quando os blocos têm tamanhos diferentes

Em blocos desiguais, a média simples dos MSE dá o mesmo peso a cada bloco; o MSE agregado dá o mesmo peso a cada registro. Por exemplo, blocos com tamanhos 1 e 3 e MSE 1 e 9 produzem média simples 5 e agregado (1× 1+3× 9)/4=7. Ambos respondem a convenções diferentes. Este laboratório retorna os dois valores e usa o agregado na seleção; não o apresenta como o comportamento universal de bibliotecas.



## Escolher entre candidatos usa informação da validação

Nos blocos fornecidos, o MSE agregado é aproximadamente 3,884339 para λ=0; 4,507848 para λ=1; 6,641602 para λ=4; e 13,287897 para λ=16. O menor candidato é λ=0, com desempate pelo menor λ caso os scores coincidam. Mais regularização não foi melhor neste exemplo. A grade de candidatos e a regra de desempate são parte do procedimento, não resultados universais.



## Reajustar não significa avaliar no teste final

Após selecionar λ, ajuste novamente nos seis registros de desenvolvimento. Aqui λ=0 dá a=5/3 e b=17/7, distintos dos coeficientes da primeira divisão. O score mínimo usado para selecionar não é uma avaliação externa independente desse processo de seleção. Não há teste externo implementado nesta unidade; reservar outro conjunto ou fazer uma avaliação aninhada é um passo posterior, não algo implicitamente realizado.



## Variar um alvo esclarece quem o utilizou

No laboratório, trocar o alvo do registro 5 não muda a reta ajustada no fold 0, porque 5 estava reservado naquela linha. Sua previsão fica igual e o erro muda. Nos outros folds, esse registro pertence ao treino e pode mudar o ajuste. Essa distinção permite testar o fluxo da informação; exigir que nenhum modelo use esse alvo em nenhuma linha destruiria o próprio procedimento de validação cruzada.



## Os três scores não são três experimentos independentes

Os treinos das divisões se sobrepõem e os scores são dependentes. Dispersão entre folds não autoriza automaticamente um intervalo de confiança usando desvio dividido por √k. Estratégias por tempo, por grupos e a seleção repetida de hiperparâmetros precisam ser estudadas no contexto da pergunta; o pequeno exemplo não fornece uma garantia de generalização.



## O que deve constar numa demonstração profissional

Registre origem e disponibilidade de x/y, unidade de observação, partição, transformações ajustadas, objetivo/penalidade, candidatos, métrica, regra de agregação e reajuste. Depois acrescente avaliação apropriada e limites. Os dados aqui são inventados, não física medida, pesquisa pessoal ou dados de cliente; o código demonstra um procedimento verificável, não experiência profissional concluída.



## Exemplo inicial preservado

Em quatro folds com 20 pontos balanceados, quantos entram na validação de cada fold?

1. Divida 20 por 4.
2. Cada bloco contém 5 pontos.
3. O treino contém os outros 15.
4. Todo ajuste precisa usar somente esses 15.

## Exercícios e resoluções

### Qual tamanho da validação no exemplo?

20/4=5.

### A escala pode ser aprendida uma vez em todos os folds antes de avaliar?

Ela deve ser ajustada no treino de cada fold.

### Quantos registros treinam cada reta do exemplo de seis registros em três blocos de dois?

Cada treino usa os outros dois blocos: quatro registros.

### No fold 0, λ=0, Sxx=10 e Sxy=20. Qual é a inclinação b?

20/10=2.

### No fold 0, previsões −5 e 7 têm alvos −5 e 11. Qual é o MSE?

Erros 0 e −4: (0+16)/2=8.

### Qual candidato λ é escolhido entre 0,1,4,16 neste exemplo?

λ=0 tem o menor MSE agregado nos folds fornecidos.

### Blocos de tamanhos 1 e 3 têm MSE 1 e 9. Qual é o MSE agregado por registro?

(1× 1+3× 9)/4=7.

### Após reajustar em todos os seis registros, qual é o intercepto a para λ=0?

x̄=0 e ȳ=5/3, portanto a=5/3.

### As previsões OOF do conjunto inteiro vêm de uma única reta global?

Cada registro é previsto por uma reta de treino que o exclui.

### O menor score usado para escolher λ já é uma avaliação externa independente da seleção?

Ele participa da escolha; o procedimento completo ainda precisa de avaliação apropriada.

### Alterar o alvo do registro 5 pode mudar o ajuste do fold 0 neste protocolo?

Esse registro está fora do treino do fold 0; muda a pontuação, não sua reta.

### Podemos tratar os três scores dos folds como três réplicas IID simples?

Os treinos se sobrepõem e induzem dependência; a dispersão não autoriza automaticamente um SE por √k.


## Validação cruzada: reajuste e seleção — 22/10/2026

`ml-validacao-cruzada` aprofundada de 3 seções/2 exercícios para 14/12, preservando vc1/vc2, exemplo inicial de 20 registros, Python incorporado e desafio. Onze seções/dez questões novas mostram três divisões explícitas, uma reta por treino, erro fora do treino, convenção de agregação, seleção e reajuste. Duas MathML e figura própria `labs/cv-reajuste/divisoes-cv.svg` com letras T/V e contraste, sem depender de cor. Nenhum modelo de simulação JS alterado.

Seis dados inventados adimensionais: x=[−3,−2,−1,1,2,3], y=[−5,−3,−1,3,5,11]; validação nos pares [0,5],[1,4],[2,3]. Cada treino tem quatro registros, cada observação valida uma vez. Objetivo SSE+λb² sem penalizar intercepto; λ=0 é OLS identificável. Para λ=0/fold 0: a=1,b=2, previsões −5 e 7, alvos −5 e 11, MSE=8. Outros MSE são 61/25 e 205/169; agregado 49234/12675≈3,884339. Candidatos 0,1,4,16 têm erros crescentes neste exemplo e selecionam 0. Reajuste em todos os seis dá a=5/3,b=17/7. O score de seleção não é avaliação externa; não há teste final ou CV aninhada implementados.

A média simples dos scores e o erro agregado por registro são distintos em blocos de tamanhos diferentes; aqui coincidem porque os tamanhos são iguais. Laboratório retorna ambos e usa o agregado para escolher. Scores de folds não são tratados como réplicas IID. Diagrama e números são próprios, sem dados de cliente, IC ou fenômeno físico observado.

Fontes primárias consultadas parcialmente em 22/10/2026: documentação oficial scikit-learn, Cross-validation §3.1 (treino/validação/teste e previsões fora do treino), https://scikit-learn.org/stable/modules/cross_validation.html ; Ridge, objetivo e parâmetros, https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html . Documentação exibida como 1.9.1; isso não significa biblioteca instalada/executada. Código próprio usa somente biblioteca padrão e Fraction, sem reproduzir exemplos, imagens ou solvers da documentação. Não houve nova leitura do Bishop neste bloco; registros anteriores permanecem delimitados.

Execução: `python3 labs/cv-reajuste/experiment.py`; testes `python3 -m unittest discover -s labs/cv-reajuste -t .`. Dados e λ aceitam int/Fraction, sem float/bool. Folds precisam cobrir índices exatamente uma vez, sem blocos vazios ou índices repetidos; cada treino exige pelo menos dois registros e inclinação identificável para λ=0. Constant x com penalidade positiva produz inclinação 0. Sem gerador aleatório, rotina de escalonamento, solver multivariado ou garantia para dados arbitrários.

Cinco testes novos: contas manuais e seleção/reajuste; 81 ajustes contra equações normais 2×2 independentes da forma centralizada; alterar alvo de validação não altera seu próprio treino, mas altera erro e outros treinos; agregação em blocos desiguais e ordem dos blocos; contratos. Suíte global: 811 testes Python e 476 estruturas MathML aprovados. Nenhuma simulação científica JS mudou; sua suíte não foi repetida neste bloco.

Navegador: figura com alt carregada, letras e legenda legíveis em 390 px, sem transbordamento horizontal e console sem erros observados. Resposta 5/3 aceita para intercepto do reajuste. Prévia `cv-reajuste-mobile.jpg`; viewport restaurado. Catálogo: 490 aulas/2665 exercícios, rascunhos para revisão pessoal.

ML agora tem 25 aulas/80 exercícios: três recortes desenvolvidos (logística, separação/vazamento, validação cruzada), 22 introduções curtas. Percurso complementar, sem disciplina formal ou domínio profissional certificado. Etapa 7 atualizada, mantendo métricas, bootstrap, tempo/grupos e avaliação externa ainda em preparação.

Próxima revisão pessoal: reproduzir fold 0, distinguir previsão fora do treino de reajuste completo e justificar o denominador do MSE. Próxima ampliação local: avaliação externa/aninhada e dependências por grupo/tempo, após delimitar a pergunta e os dados. Próxima alternância global: auditar profundidade e sequência de deep learning, antes de escolher outro recorte. Notas pessoais e objetivo integral seguem pendentes. Saldo semanal após bloco: 98%; parada operacional: 65%.
