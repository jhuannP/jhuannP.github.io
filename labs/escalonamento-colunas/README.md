# Escalonamento por coluna e estado de treino

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão pessoal de Jhuann.

## Linhas são exemplos; colunas são características

Representamos o treino por uma matriz com N linhas e d colunas. Cada linha é um exemplo e cada coluna mantém o mesmo significado no treino e nos dados novos. Padronizar por característica significa aprender d médias e d escalas, não uma média para cada linha. O exemplo novo usa duas características numéricas sintéticas, sem inferir propriedades de um sistema físico ou de uma base real.

X tem forma N×d

## Aprender estatísticas exige uma convenção

Para a coluna j, calcule a média μⱼ=(1/N)Σᵢxᵢⱼ e a variância empírica vⱼ=(1/N)Σᵢ(xᵢⱼ−μⱼ)². A escala é sⱼ=√vⱼ quando vⱼ>0. O divisor N é a convenção deste transformador; não estamos estimando uma variância populacional conhecida nem usando a fórmula amostral com N−1. Com uma única linha, toda coluna tem variância empírica zero e precisa da regra para constantes.

vⱼ=(1/N)Σᵢ(xᵢⱼ−μⱼ)²

## Separar ajuste e transformação

fit recebe somente as linhas autorizadas de treino e devolve médias, variâncias, escalas e o número de linhas usado. transform aplica zᵢⱼ=(xᵢⱼ−μⱼ)/sⱼ, sem recalcular essas estatísticas. O estado faz parte do procedimento aprendido, mesmo sem consultar rótulos. Reajustar separadamente no teste muda a representação; incluir o teste no ajuste deixa sua informação influenciar a preparação do modelo.

zᵢⱼ=(xᵢⱼ−μⱼ)/sⱼ

## Exemplo resolvido com duas escalas

Use treino com linhas (0,100) e (2,300). A primeira coluna tem μ₁=(0+2)/2=1 e v₁=[(−1)²+1²]/2=1, logo s₁=1. Na segunda, μ₂=200 e v₂=[(−100)²+100²]/2=10000, logo s₂=100. Transformando cada coluna, as duas linhas tornam-se (−1,−1) e (1,1). Cada coordenada é calculada com o estado da sua coluna.

μ=(1,200); s=(1,100)

## Dados novos podem ficar longe de zero

Para a linha de teste (4,500), reaplique o estado anterior: z₁=(4−1)/1=3 e z₂=(500−200)/100=3. O resultado é (3,3). Não há obrigação de o teste ter média zero ou variância um; essas propriedades descrevem o treino transformado, quando a coluna é não constante. Um valor três não é automaticamente um erro, uma probabilidade ou um limiar universal de anomalia. A interpretação depende da variável e do procedimento.

Teste (4,500) → (3,3)

## Por que o treino fica centrado?

Somar os valores transformados de uma coluna fornece Σᵢ(xᵢⱼ−μⱼ)/sⱼ=(Σᵢxᵢⱼ−Nμⱼ)/sⱼ=0. Quando vⱼ>0, a média dos quadrados transformados é vⱼ/sⱼ²=1. Essas identidades usam as mesmas linhas que definiram μ e s. No computador, podem existir pequenos resíduos de arredondamento; o laboratório verifica as identidades com tolerância, não por igualdade binária em todos os dados.

Treino não constante: média 0, variância 1

## Coluna constante não tem desvio para dividir

Se todos os valores de treino de uma coluna são dez, μ=10 e v=0. Adotamos escala numérica um para evitar divisão por zero. Os valores dez tornam-se zero, mas um valor novo doze se torna dois, não zero. Isso não cria evidência de que o modelo tenha aprendido a responder a essa variação. Em variáveis com unidades, a convenção de escala um precisa ser interpretada na unidade escolhida; não é uma escala física deduzida dos dados.

Treino constante 10: novo 12 → 2

## Misturar teste e treino altera o estado

Se a linha de teste (4,500) entrar indevidamente no ajuste, as três linhas darão médias (2,300). A variância da primeira coluna vira 8/3 e a escala √(8/3); o valor quatro passa a √(3/2)≈1,2247, em vez de três. O número pode parecer mais próximo do centro porque o próprio teste ajudou a defini-lo. A mudança do estado já demonstra a contaminação neste exemplo; não calculamos um score nem afirmamos que toda contaminação melhora numericamente qualquer avaliação.

Ajuste indevido: μ₁=2, não 1

## Converter unidades e inverter a transformação

Em uma coluna não constante, substituir x por ax+c com a>0 no treino e nos dados novos produz μnovo=aμ+c e snovo=as. Portanto os valores padronizados permanecem iguais. O argumento não vale da mesma forma na convenção de coluna constante. A transformação com escala positiva também tem inversa x=z s+μ; para z₂=3, s₂=100 e μ₂=200, recuperamos quinhentos. Guardar o estado permite essa reconstrução e a consistência entre etapas.

x=z s+μ

## Escalonar não torna as características independentes

No exemplo, as colunas transformadas são idênticas: uma vale −1,1 e a outra também. Elas continuam perfeitamente correlacionadas. Centrar e dividir pela escala não remove correlação, não demonstra independência e não transforma automaticamente uma distribuição em gaussiana. Média e variância também são sensíveis a valores extremos. A decisão de padronizar depende do algoritmo, da função de custo, das unidades e do desenho da avaliação, não de uma regra de que todo modelo precise disso.

## Validação cruzada precisa repetir o ajuste no lugar certo

Em cada divisão de validação cruzada, ajuste o transformador somente nas linhas de treino daquela divisão e reaplique o estado na validação. Não reutilize um estado aprendido com todas as linhas antes de dividi-las. Depois de fixar o procedimento sem escolher pelo teste final, o treinamento final usa os dados autorizados e gera seu próprio estado. As aulas de separação e validação cruzada da trilha desenvolvem esses papéis; o painel desta aula permanece uma demonstração simples de escala, sem avaliação de um modelo.

## Contrato do laboratório e limites

O código novo usa matrizes pequenas de números reais finitos e estado imutável. fit exige treino não vazio e colunas consistentes; transform e inverse aceitam lote vazio depois do ajuste, mas rejeitam dimensão incompatível e valores não finitos. A implementação usa divisor N e escala um para variância zero, sem dados faltantes, pesos, atualização incremental ou estruturas esparsas. Não é uma cópia completa da API de scikit-learn, nem uma garantia de precisão para amplitudes extremas. Os exemplos são didáticos e não comprovam desempenho em dados de clientes.

## Exercícios e resoluções

- Qual valor transformado de x=4 no exemplo? **Resolução:** (4−1)/1=3.
- O teste deve aprender uma nova média própria nesse procedimento? **Resolução:** Reaplique o estado aprendido no treino.
- Quantas linhas tem o treino com exemplos (0,100) e (2,300)? **Resolução:** São duas linhas, cada uma com duas características.
- Qual a média de treino da primeira coluna, com valores 0 e 2? **Resolução:** (0+2)/2=1.
- Qual a média de treino da segunda coluna, com valores 100 e 300? **Resolução:** (100+300)/2=200.
- Qual a variância da primeira coluna com divisor N? **Resolução:** [(0−1)²+(2−1)²]/2=1.
- Qual a escala da segunda coluna no exemplo? **Resolução:** √10000=100.
- Com o estado correto de treino, quanto é a primeira coordenada transformada do teste (4,500)? **Resolução:** (4−1)/1=3.
- Com o mesmo estado, quanto é a segunda coordenada transformada do teste (4,500)? **Resolução:** (500−200)/100=3.
- Uma coluna de treino constante em 10 usa escala um. Quanto vira o novo valor 12? **Resolução:** (12−10)/1=2.
- Se a primeira coluna de teste 4 fosse misturada aos valores de treino 0 e 2, qual média indevida seria aprendida? **Resolução:** (0+2+4)/3=2, diferente da média correta um.
- Padronizar cada coluna garante que as características fiquem independentes? **Resolução:** As duas colunas do exemplo continuam idênticas e correlacionadas após padronizar.

## Fontes e execução

[scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html), definição, atributos e Notes; [Common pitfalls §§12.1–12.2](https://scikit-learn.org/stable/common_pitfalls.html), consistência e vazamento. Consultas parciais em 22/10/2026; páginas exibiram versão 1.9.1. Código próprio, sem biblioteca instalada ou reprodução dos exemplos da documentação.

Na raiz: python3 -m labs.escalonamento-colunas.experiment; testes: python3 -m unittest discover -s labs/escalonamento-colunas -t .

ScaleState deve vir de fit. Dados finitos em lista/tupla, sem NaN. O estado é imutável e os nomes/ordem das características precisam ser mantidos externamente; o código verifica dimensão, não semântica dos rótulos. Sem framework ou modelo treinado neste laboratório.


## Escalonamento por coluna — 22/10/2026

Aula ml-escalonamento ampliada de três seções/dois exercícios para 12 seções/12 exercícios. Exemplo antigo 1D, código, desafio, IDs e painel preservados. Novo laboratório tem matriz pequena, estatísticas por coluna, estado imutável, transformação e inversa. Foram desenvolvidas identidades do treino, diferença para teste, convenção de variância com divisor N, coluna constante e limites: não remove correlação, não cria normalidade e não comprova desempenho.

Fonte primária consultada parcialmente em 22/10/2026: [scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html), definição, atributos e Notes; [Common pitfalls §§12.1–12.2](https://scikit-learn.org/stable/common_pitfalls.html), consistência e vazamento. Páginas exibiram versão 1.9.1; nenhuma biblioteca instalada ou chamada. Dados, contas, identidades, figura e código locais originais, sem reprodução dos exemplos da documentação. A implementação didática é mais restrita: números finitos, sem NaN, pesos ou esparsidade.

Exemplo de treino (0,100),(2,300): médias (1,200), variâncias (1,10000), escalas (1,100). Treino transformado (−1,−1),(1,1), teste (4,500) vira (3,3). Incluir indevidamente esse teste no ajuste muda médias para (2,300) e a primeira coordenada de teste para √(3/2)≈1,2247. Nenhum score foi calculado; não se afirma que todo vazamento melhora qualquer resultado. Coluna constante dez com escala um transforma novo doze em dois.

Seis testes novos aprovados em labs/escalonamento-colunas/: caso exato; momentos/inversa em diferentes matrizes; estado sem reajuste e efeito de incluir teste; mudança positiva de unidades; constante/divisor/lote vazio; contratos. Treze testes de catálogo e 537 estruturas MathML aprovados. Figura nova já declara dimensões 440×410, preservando a reserva de espaço. Nenhum modelo JavaScript alterado; suíte global não repetida.

Navegador: figura e texto inspecionados em 390 px, largura da página igual à tela e nenhum erro de console observado. Na variância de treino, resposta dois rejeitada e um aceita; caso constante respondeu dois corretamente. Prévia escalonamento-colunas-mobile.jpg. Material assistido por IA em rascunho, sem domínio pessoal ou desempenho de produção inferidos.

Reconciliação: antes do bloco, as aulas de ML somavam 90 exercícios e quatro recortes desenvolvidos, mas curriculumNote ainda dizia 80/três. A nova contagem foi calculada das aulas, não desse resumo antigo. Estado atual: 25 aulas/100 exercícios, cinco recortes desenvolvidos e 20 introduções curtas. Percurso complementar próprio, sem equivalência com disciplina cursada. Catálogo global: 501 aulas/3054 exercícios.

Próxima revisão pessoal: reconstruir médias/escalas, transformar o teste sem reajustar e explicar o comportamento da coluna constante. Próximo bloco global: retomar integrais duplas e Fubini em Matemática III, conferindo fontes e cobertura atual. Saldo semanal após bloco: 92%; parada operacional em 65%.
