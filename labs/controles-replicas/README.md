# Controles e réplicas — notas originais

16/10/2026. Complemento didático ao programa amplo de CCM0215, não reconstituição de uma prática. Rascunho para revisão pessoal.

## Comece pela pergunta e pelo contraste

Considere dois grupos hipotéticos C e T e um sinal medido em unidades arbitrárias. A pergunta é como a média de T difere da de C. Antes de calcular, declare o que recebe a intervenção, o que é medido e para qual população se pretende generalizar. Uma diferença numérica entre grupos não identifica, sozinha, um efeito causal.

## Controles respondem a perguntas diferentes

Um branco pode estimar o fundo do procedimento; um controle negativo ajuda a avaliar sinal na ausência da condição de interesse; um controle positivo verifica se a leitura pode detectar uma referência adequada. Se houver veículo, um controle correspondente ajuda a distinguir seu efeito. Um controle não substitui os demais nem prova que todas as etapas funcionaram. Aqui não há ensaio real ou protocolo de bancada.

## A unidade independente vem antes de contar leituras

Uma unidade experimental é definida pelo desenho e pela possibilidade de receber uma condição independentemente das outras. Repetir três leituras da mesma preparação não cria três novas unidades biológicas. No exemplo adotamos n unidades independentes por grupo, cada uma com r leituras técnicas. O nome de uma réplica não garante independência: origem, preparo e alocação precisam sustentá-la.

## Preserve a hierarquia nos dados

O arquivo sintético tem colunas group, unit_id, read_id e signal. Grupo C: unidades C1=[8,10] e C2=[12,14]. Grupo T: T1=[12,14] e T2=[14,16]. São oito leituras no total, mas apenas duas unidades por grupo. Não transforme read_id em identificador de amostra nem apague a associação entre as leituras.

## Um resumo por unidade deixa o contraste auditável

As médias de C1/C2 são 9 e 13, e as de T1/T2, 13 e 15. A média de C é 11 e a de T é 14; o contraste T−C vale 3 unidades de sinal. Com o mesmo número de leituras por unidade, a média de todas as leituras coincide com a média das médias. Essa coincidência do ponto estimado não torna as leituras independentes.

## Estimar incerteza é outra etapa

Para grupos independentes, usando médias por unidade, uma estimativa da variância do contraste é s_T²/n_T+s_C²/n_C. No conjunto sintético, as variâncias amostrais das médias de unidade são 2 e 8; portanto a variância estimada do contraste é 2/2+8/2=5 e seu erro padrão é √5≈2,236. Com duas unidades por grupo, a estimativa é frágil. Não produzimos intervalo, teste ou conclusão de significância.

## Um modelo de componentes ajuda a planejar

Agora use outro cenário, de planejamento: y_gij=μ_g+b_gi+e_gij. O deslocamento b é compartilhado pelas leituras da unidade i e tem variância τ²; e é erro de leitura com variância σ². Ambos têm média zero. Unidades e erros técnicos são independentes entre si, exceto pelo b compartilhado. Os dois grupos têm os mesmos componentes e n unidades, r leituras. τ e σ são parâmetros conhecidos escolhidos, não estimados do pequeno CSV.

## A média técnica reduz uma parte da variância

A média das r leituras de uma unidade tem variância τ²+σ²/r. Ao calcular a média de n unidades independentes, divide-se por n. O contraste de dois grupos independentes soma duas dessas variâncias: Var(d)=2(τ²/n+σ²/(nr)). Leituras da mesma unidade covariam em τ²; ignorar essa covariância elimina informação essencial do desenho.

## A pseudorreplicação pode reduzir artificialmente o erro declarado

Tratar todas as nr leituras de cada grupo como independentes, mantendo a variância marginal τ²+σ², daria Var_ingênua(d)=2(τ²+σ²)/(nr). A razão entre a variância correta e essa referência é D=1+(r−1)ρ, com ρ=τ²/(τ²+σ²), quando o denominador é positivo. Erros padrão têm razão √D, não D. Esse cálculo compara modelos com componentes conhecidos; não é a fórmula universal para todo teste aplicado a dados agrupados.

## Mais leituras e mais unidades têm ganhos diferentes

Com n=4, r=3, τ=2 e σ=1, a variância correta é 13/6 e a ingênua, 5/6; D=13/5=2,6. Dobrar n reduz a variância correta à metade. Aumentar r reduz só σ²/(nr); para τ>0 há um piso 2τ²/n quando r cresce. Leituras técnicas continuam úteis para caracterizar ruído e falhas, mas não substituem novas unidades. Se τ=0, ambas as fórmulas coincidem; se σ=0, repetir leituras não reduz a variância correta.

## Precisão não corrige viés ou confundimento

Alocar todos os controles em um lote e todos os tratados em outro mistura condição e lote. Repetir leituras pode tornar uma estimativa enviesada mais precisa. Planeje alocação, ordem de leitura e blocos conforme a pergunta e registre exclusões antes de olhar o efeito. Um instrumento muito preciso não torna uma amostra representativa. O modelo de componentes não resolve esses problemas de desenho.

## Um relatório precisa preservar o que foi feito e o que foi calculado

Informe unidades independentes, leituras técnicas, controles, condições, unidades do sinal, processamento e limitações. Separe dados brutos de médias e de parâmetros de planejamento. Duplicar linhas já existentes não acrescenta informação: o código mantém o resumo por unidade nesse caso. Esta aula é complementar ao programa amplo de CCM0215; não comprova prática pessoal, domínio de técnica molecular ou resultado do projeto de Jhuann.

## Resoluções

Com quatro unidades independentes por grupo e três leituras por unidade, quantas unidades independentes há por grupo?

n=4; as 12 leituras por grupo não são 12 unidades independentes.

No CSV sintético, qual o contraste entre a média de T e a média de C?

As médias das unidades são C=[9,13], T=[13,15]; 14−11=3.

No planejamento n=4,r=3,τ=2,σ=1, qual a variância correta do contraste?

2(4/4+1/12)=13/6.

Nesse planejamento, qual a variância ingênua que ignora a dependência?

2(4+1)/(4×3)=5/6.

Nesse planejamento, qual a correlação ρ entre duas leituras da mesma unidade?

τ²/(τ²+σ²)=4/5.

Nesse planejamento, qual a razão D entre variância correta e ingênua?

(13/6)/(5/6)=13/5=2,6.

Um controle negativo substitui um positivo?

Ausência de sinal no negativo não demonstra que a técnica detectaria uma referência positiva.

Duplicar no arquivo as mesmas leituras cria novas unidades independentes?

É duplicação de informação, não nova replicação.

Se todo grupo C é lido num lote e todo T em outro, mais leituras resolvem o confundimento?

Condição e lote continuam inseparáveis nesse desenho.

A diferença observada de 3 no CSV, por si só, comprova um efeito causal?

Faltam elementos do desenho e evidências para sustentar essa interpretação.

## Roteiro e verificação

Use data.csv para reconstruir as médias sem perder unit_id. Explique os dois controles e proponha como distinguir condição de lote. No planejamento, compare acrescentar leituras e acrescentar unidades; justifique o piso de variância. Não confunda os parâmetros conhecidos com estimativas do CSV. Produto de estudo: resumo próprio e uma hipótese explícita que permitiria interpretar o contraste.

Quatro testes verificam valores racionais, soma independente de covariâncias (27 configurações), resumo do CSV/invariância a duplicação e contratos. O arquivo reference.json reúne 36 configurações de planejamento para JavaScript. O laboratório não gera amostras aleatórias, intervalos ou valores-p. Se τ=σ=0, o erro é zero no modelo, mas correlação e razão de variâncias são indefinidas e aparecem como tal, sem divisão por zero. Execute a suíte na raiz: `python3 -m unittest discover -p 'test_*.py'`.

## Fontes e limites

[USP CCM0215](https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0215): programa geral consultado por indexação em 16/10/2026; a aula é complemento metodológico, não protocolo listado. [NC3Rs EDA — unidade experimental](https://eda.nc3rs.org.uk/experimental-design-unit), consultado diretamente, fundamenta a relação entre unidade, intervenção e independência. [Altman e Krzywinski, Sources of variation](https://www.nature.com/articles/nmeth.3224), 2015: página editorial, resumo e legenda suplementar acessíveis; texto integral por assinatura não consultado. Não foram reproduzidos seus exemplos/figuras. Modelo de dois componentes, derivações, CSV e código são próprios.

Pendentes: análises para desenhos desbalanceados/pareados, variâncias estimadas com incerteza, intervalos, poder e técnicas moleculares específicas. Não se atribui a Jhuann execução de experimento, produto de pesquisa ou domínio de técnica a partir deste material.
