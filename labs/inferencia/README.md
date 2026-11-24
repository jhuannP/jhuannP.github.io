# p-valor: resultado extremo sob a hipótese, não chance de ela ser verdadeira

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Definir hipótese nula, alternativa, estatística e cauda.
- Calcular p-valores no teste normal com σ conhecido.
- Distinguir p-valor, nível de significância e tamanho de efeito.
- Reconhecer limites de não rejeição e de escolhas após olhar os dados.

## O teste começa pelo modelo e pela pergunta

Para testar uma média, defina H₀:μ=μ₀, a alternativa e o desenho da coleta. Nesta aula usamos observações normais iid com σ conhecido. A estatística Z=(X̄−μ₀)/(σ/√n) tem distribuição normal padrão sob H₀. Se o desenho ou as hipóteses mudarem, essa referência pode deixar de ser correta.

Z=(X̄−μ₀)/(σ/√n)

## Extremo depende da alternativa escolhida

Uma alternativa μ>μ₀ leva à cauda direita; μ<μ₀, à esquerda; μ≠μ₀ pode levar ao critério bilateral |Z|. O que conta como extremo precisa ser definido antes de observar o resultado. Não há uma fórmula bilateral universal igual ao dobro de uma cauda para toda distribuição ou estatística; aqui a simetria normal permite essa construção.

## O p-valor é calculado sob a hipótese nula

Depois de observar z, o p-valor é a probabilidade, sob H₀, de uma estatística pelo menos tão extrema pelo critério escolhido. No teste bilateral normal, p=2[1−Φ(|z|)]. À direita, p=1−Φ(z); à esquerda, p=Φ(z). A probabilidade se refere a resultados possíveis do procedimento, não a uma distribuição posterior sobre H₀.

p bilateral=2[1−Φ(|z|)]

## O mesmo z pode gerar perguntas diferentes

Para z=2, o p-valor bilateral é aproximadamente 0,045500; à direita, 0,022750; à esquerda, 0,977250. Não escolha o menor deles depois de ver o resultado. A diferença decorre de alternativas distintas e muda o teste planejado. Para z=0, o bilateral é 1 e cada cauda unilateral vale 1/2.

## O nível α define um critério; não calcula p

Uma regra comum rejeita H₀ quando p≤α. Sob H₀ e o protocolo do teste normal planejado, α controla a probabilidade de erro tipo I, rejeitar uma hipótese nula verdadeira. Alterar α mantém o p-valor observado e muda o limiar da decisão. Não chamar essa regra de probabilidade de erro da hipótese depois dos dados.

## Não rejeitar não é provar ausência de efeito

Quando p>α, o procedimento não rejeita H₀ naquele critério. Isso não prova igualdade exata, ausência de efeito ou equivalência prática. Pode haver pouca informação para detectar um efeito. Demonstrar equivalência exige definir uma margem pertinente e outro protocolo, não apenas inverter a frase de um teste usual.

## Significância e tamanho do efeito não são iguais

O p-valor não mede a magnitude ou a utilidade prática de um efeito. Uma diferença pequena pode produzir z grande com erro padrão muito pequeno. Apresente a estimativa na unidade original, seu intervalo e o contexto. Um efeito grande também pode ter incerteza ampla em uma amostra pequena.

## Poder trata resultados sob uma alternativa

Erro tipo II significa não rejeitar H₀ quando uma alternativa especificada é verdadeira; poder é a probabilidade de rejeitar sob essa alternativa. Ele depende do efeito, da variabilidade, do tamanho e do protocolo. O p-valor observado não substitui uma análise de poder e não revela sozinho essas probabilidades.

## Muitas tentativas e seleção mudam a interpretação

Testar várias hipóteses e reportar apenas a menor cauda, escolher um corte conveniente ou parar ao obter significância não preserva automaticamente a taxa de erro de um teste único planejado. Planejamento, transparência e tratamento de multiplicidade fazem parte da análise. A interface demonstra contas isoladas; não implementa um protocolo para essas situações.

## A ligação com o intervalo normal exige o mesmo procedimento

No teste bilateral normal com σ conhecido e nível α, H₀:μ=μ₀ é rejeitada exatamente quando μ₀ fica fora do intervalo bilateral correspondente de nível 1−α, exceto pela convenção de fronteira. Essa equivalência depende de usar as mesmas hipóteses, quantil e estatística. Não transfira automaticamente a relação a testes ou intervalos diferentes.

## A demonstração não toma decisões de pesquisa

O gráfico usa Z padrão sob H₀ e preenche a parte visível das caudas em [−4;4]. O p-valor inclui também a área fora da janela e é aproximado pela CDF numérica conferida. A regra p≤α descreve o teste sintético; não valida coleta, causalidade, resultados da IC ou uma decisão sobre uma hipótese real.

## Exemplo resolvido

Teste bilateral normal: z=2 e α=0,05. O que a conta permite dizer?

1. Sob H₀, Z tem distribuição normal padrão.
2. A cauda direita em 2 vale aproximadamente 0,022750.
3. Pelo critério bilateral, p ≈ 2 × 0,022750 = 0,045500.
4. Como p<0,05, o teste rejeitaria H₀ sob o modelo e protocolo declarados.
5. À direita seria outro teste, com p≈0,022750, se essa alternativa tivesse sido escolhida antes.
6. Não concluímos P(H₀|dados)=0,045500, nem medimos o tamanho do efeito por esse número.

## Exercícios e resoluções

### No teste bilateral normal com z=0, qual é o p-valor?

Cauda bilateral total igual a 1.

### p=0,03 significa probabilidade posterior de H0 igual a 3%?

Sim
Não

Esse não é o significado de p-valor.

### No teste normal à direita com z=0, qual o p-valor?

A cauda direita da normal padrão em zero é 1/2.

### No teste bilateral normal com z=2, qual o p-valor?

2[1−Φ(2)]≈0,045500.

### No teste normal à direita com z=2, qual o p-valor?

1−Φ(2)≈0,022750.

### Se p=0,0455 e α muda de 0,05 para 0,01, o p-valor:

Muda para 0,01
Permanece 0,0455

O limiar muda; o p-valor calculado a partir de z e da cauda não muda.

### Não rejeitar H₀ prova equivalência prática?

Sim
Não

Equivalência exige margem e protocolo adequados; não rejeição não basta.

### Um p-valor pequeno mede diretamente o tamanho do efeito?

Sim
Não

Magnitude deve ser apresentada em sua unidade e com incerteza; p não mede isso.

### Escolher a cauda que dá menor p depois de ver o resultado preserva automaticamente o teste planejado?

Sim
Não

A seleção pós-observação altera o procedimento e pode alterar taxas de erro.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`, usando biblioteca padrão. p-valores por erfc e momentos conjuntos por frações; a correlação final usa ponto flutuante e retorna None para desvio zero. Sem ler dados privados ou escrever resultados externos.

## Proposta didática

Peça uma previsão antes de mudar controles; identifique hipótese ou distribuição conjunta; resolva um caso à mão; encerre com um contraexemplo à interpretação indevida. A condução precisa de revisão de Jhuann.

## Hipóteses e limites

- Teste normal de média com σ conhecido e referência válida sob H₀.
- Alternativa, estatística, cauda e nível precisam de protocolo apropriado.
- p-valor não é posterior, tamanho de efeito ou prova de equivalência.
- Modelo didático sintético, sem decisão científica sobre a IC.
