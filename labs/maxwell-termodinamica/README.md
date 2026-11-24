# Maxwell termodinâmico — notas de aula

Rascunho original para revisão de Jhuann. Relações de equilíbrio, sem mecanismo temporal ou dados medidos.


## A pergunta: obter uma mudança de entropia sem um entropímetro

Se conhecemos como a pressão muda com a temperatura a volume fixo, podemos inferir como a entropia muda com o volume a temperatura fixa. A ligação vem de uma função de estado com derivadas regulares. Esta aula deduz essa ligação e testa um modelo de gás ideal; não usa dados medidos e não confunde estas relações com as equações de Maxwell do eletromagnetismo.


## Domínio e o que permanece fixo

Consideramos um sistema simples compressível em equilíbrio, de composição fixa, com trabalho de pressão–volume. T é temperatura absoluta em K, p pressão em Pa, V volume em m³, S entropia em J/K e U energia interna em J. Trabalhamos dentro de uma região monofásica em que os potenciais têm derivadas contínuas até segunda ordem. Nos símbolos seguintes, as quantidades de matéria ficam fixas, mesmo quando omitidas dos índices.


## A diferencial fundamental não é uma trajetória qualquer

Entre estados de equilíbrio, dU=T dS−p dV. Para obter essa expressão por uma transformação reversível, usamos calor recebido δq_rev=T dS e trabalho realizado pelo sistema δW_rev=p dV, com dU=δq−δW. U e S são funções de estado; calor e trabalho dependem do processo. Numa transformação irreversível não podemos substituir automaticamente o calor real por T dS.
dU=T dS−p dV

## Transformar o potencial troca as variáveis naturais

Defina H=U+pV, F=U−TS e G=H−TS. Levine usa A para a energia de Helmholtz; aqui F é a mesma função. Aplicando a regra do produto: dH=dU+p dV+V dp=T dS+V dp. Para F, os termos T dS se cancelam; para G, ocorre cancelamento análogo. Assim U usa (S,V), H usa (S,p), F usa (T,V) e G usa (T,p).
dF=−S dT−p dV; dG=−S dT+V dp

## Ler o coeficiente de cada diferencial

Se F=F(T,V), sua diferencial é F_T dT+F_V dV. Comparar com dF=−S dT−p dV fornece F_T|V=−S e F_V|T=−p. O índice informa qual variável fica fixa; não é decoração. Uma derivada a volume fixo e outra a pressão fixa descrevem restrições diferentes.
(∂F/∂T)_V=−S; (∂F/∂V)_T=−p

## Derivar a relação de Helmholtz sem perder o sinal

Derive F_T=−S em relação a V mantendo T fixo: F_TV=−(∂S/∂V)_T. Derive F_V=−p em relação a T mantendo V fixo: F_VT=−(∂p/∂T)_V. A continuidade das derivadas de segunda ordem permite igualar F_TV e F_VT. Os dois sinais negativos se cancelam. Essa é a relação usada no exemplo.
(∂S/∂V)_T=(∂p/∂T)_V

## A relação de Gibbs tem outro sinal

Agora G_T|p=−S e G_p|T=V. Igualar as derivadas cruzadas dá −(∂S/∂p)_T=(∂V/∂T)_p. Portanto o sinal negativo permanece. Uma confusão comum é transportar o sinal da relação de Helmholtz para esta, sem refazer a comparação dos coeficientes.
(∂S/∂p)_T=−(∂V/∂T)_p

## Reconstruir as duas relações restantes

Para U(S,V), os coeficientes são T e −p; derivadas cruzadas fornecem (∂T/∂V)_S=−(∂p/∂S)_V. Para H(S,p), são T e V, de modo que (∂T/∂p)_S=(∂V/∂S)_p. O mesmo procedimento produz as quatro relações. Nenhuma autoriza trocar uma variável mantida fixa sem usar relações adicionais.
U: (∂T/∂V)_S=−(∂p/∂S)_V; H: (∂T/∂p)_S=(∂V/∂S)_p

## Um gás ideal fornece a derivada necessária

No modelo p=nRT/V, n é a quantidade em mol e R=8,314 J/(mol K), arredondado para os cálculos. A volume e quantidade fixos, (∂p/∂T)_V=nR/V. Por Maxwell, essa também é (∂S/∂V)_T. Para n=1 mol e V=0,010 m³, o valor é 831,4 Pa/K. Como Pa=J/m³, a unidade também é J/(K m³), apropriada à derivada da entropia pelo volume.
(∂S/∂V)_T=nR/V

## Integrar ao longo da isoterma

Para T fixa e n fixo, integre nR/V de V₁ até V₂. O resultado é nR ln(V₂/V₁); o argumento do logaritmo é adimensional. A expansão dá ΔS>0 e a compressão ΔS<0. A integral calcula diferença entre estados de equilíbrio do modelo; não informa quanto tempo o processo leva ou quão próximo um gás real está do ideal.
ΔS=nR ln(V₂/V₁)

## Conferir por pressão e por energia interna

Na mesma isoterma ideal, p₁V₁=p₂V₂, portanto ln(V₂/V₁)=−ln(p₂/p₁). A relação de Gibbs também dá ΔS=−nR ln(p₂/p₁). Outra consequência vem da diferencial fundamental: (∂U/∂V)_T=T(∂S/∂V)_T−p=T(∂p/∂T)_V−p. Para p=nRT/V, os termos se cancelam. Esta conclusão depende da equação ideal, não é uma regra universal sobre fluidos.
(∂U/∂V)_T=T(∂p/∂T)_V−p

## Uma função geradora para verificar o código

O laboratório escolhe F=n c_v T[1−ln(T/T₀)]−nRT ln[V/(n v₀)], com c_v=20 J/(mol K) constante ilustrativa, T₀=300 K e v₀=0,010 m³/mol. Derivar F fornece S=n c_v ln(T/T₀)+nR ln[V/(n v₀)], p=nRT/V e U=n c_v T. A referência faz S=0 em T₀ e V=n v₀ por escolha; não calcula entropia absoluta nem aplica a terceira lei. Trata-se de um modelo consistente para os exemplos, não parâmetros ajustados de uma substância.


## O que a diferença finita verifica

O código aproxima derivadas por diferenças centrais e compara com a equação de estado e com a integral por quadratura. Há erro de truncamento e arredondamento; diminuir o passo indefinidamente pode piorar a subtração de valores próximos. Os testes conferem sinais, restrições e implementação em estados selecionados, mas não substituem a prova pela regularidade das derivadas e não validam dados experimentais.


## Limites antes de generalizar

Em coexistência de fases ou em pontos singulares, não aplique a hipótese de um potencial suave atravessando o domínio sem análise. Com composição variável, aparecem termos químicos e novas variáveis mantidas fixas. Campos, deformações e outros tipos de trabalho exigem termos adicionais. Um resultado termodinâmico relaciona estados e respostas; não fornece cinética molecular, causalidade ou um mecanismo de reação.


## Exemplo resolvido

Um mol ideal a 300 K passa de 0,010 para 0,020 m³. Qual é ΔS?

1. Dados: n=1 mol, T fixa, R=8,314 J/(mol K). Estados monofásicos do modelo ideal.
2. A equação p=nRT/V dá (∂p/∂T)_V=nR/V; Maxwell transfere essa derivada para (∂S/∂V)_T.
3. Integre de 0,010 a 0,020 m³: ΔS=nR ln(0,020/0,010).
4. ΔS=8,314 ln 2≈5,762826 J/K; p cai de 249420 a 124710 Pa.
5. A inversão dos estados troca o sinal. Para este gás ideal, ΔU=0 na isoterma; isso não transforma o processo em ciclo.

## Exercícios e resoluções

### Quais são as variáveis naturais de F neste recorte?

dF=−S dT−p dV: F=F(T,V), com composição fixa.

### Qual coeficiente multiplica dV em dF?

O trabalho de expansão aparece com sinal negativo na convenção adotada.

### Que hipótese permite igualar as derivadas cruzadas usadas aqui?

A regularidade do potencial é essencial à comutação das derivadas.

### A relação derivada de G mantém qual sinal?

G_T=−S e G_p=V; o sinal negativo permanece.

### Com n=1 mol, R=8,314 e V=0,010 m³, quanto vale (∂p/∂T)_V em Pa/K?

nR/V=8,314/0,010=831,4 Pa/K.

### Com os mesmos n e V, T=300 K, qual é a pressão ideal em Pa?

8,314×300/0,010=249420 Pa.

### Um mol ideal dobra de volume isotermicamente. Calcule ΔS em J/K, usando R=8,314.

ΔS=8,314 ln 2≈5,762825659 J/K.

### Invertendo a transformação anterior, qual é ΔS em J/K?

Trocar os extremos muda o sinal: −8,314 ln 2.

### No modelo ideal da aula, qual é (∂U/∂V)_T em J/m³?

T nR/V−nRT/V=0.

### S=0 no estado de referência do laboratório significa entropia absoluta nula medida?

É escolha de referência do modelo, não resultado da terceira lei.

### Podemos identificar sempre o calor real de um processo irreversível com T dS?

A identidade δq_rev=T dS descreve calor reversível; não vale automaticamente para o calor real irreversível.

### As relações de Maxwell determinam a velocidade da transformação?

São relações entre propriedades de equilíbrio, sem uma lei temporal de evolução.


## Fonte, reprodução e limites da verificação

Levine, Physical Chemistry, sexta edição, McGraw-Hill 2009, §4.4: consulta parcial de pp.115–120/PDF133–138. Extração gerou avisos de fontes; p.118/PDF136 inspecionada visualmente para conferir os sinais das quatro relações. Sumário apenas orientou a localização; o corpo foi consultado depois. Levine usa A para Helmholtz; estas notas usam F. Referência aos números do livro não implica que os exemplos, exercícios ou código sejam seus. Material próprio; PDF e figuras privadas não copiados para o site. As hipóteses aqui são mais restritas: composição fixa.

Programa oficial CCM0124 aberto em 22/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124 . Item 4 prevê relações de Maxwell. Ativação 01/01/2025 permanece posterior à aprovação registrada em 2024/1; versão da turma não recuperada. Não há nova conferência do histórico pessoal neste bloco.

Na raiz do protótipo:

```sh
python3 labs/maxwell-termodinamica/experiment.py
python3 -m unittest discover -s labs/maxwell-termodinamica -t .
```

Constantes ilustrativas e unidades: T em K, V em m³, n em mol, capacidade molar cv em J/(mol K), R=8,314 J/(mol K) arredondado. F e U em J, S em J/K e p em Pa. Referência de S é convencional; não representa entropia absoluta, terceira lei, substância calibrada ou domínio pessoal. T,V,n,cv positivos finitos, sem promessa de estabilidade numérica para escalas arbitrárias. Derivadas numéricas têm erro de passo e arredondamento.

Quatro testes locais: gradientes de F contra S/p em 27 estados e identidade U=F+TS; derivada mista e Maxwell em seis estados; integração Simpson independente em 12 transformações e aditividade/inversão; referência e contratos inválidos. Esses testes verificam implementação em estados selecionados, não provam a identidade para todos os sistemas nem validam experimentos.

Verificação global: 784 testes Python e 462 estruturas MathML aprovados. Não houve alteração de simulação JS; sua suíte não foi repetida. No navegador, resposta 5,762825659 aceita na questão 7; quatro fórmulas MathML, viewport 390px sem transbordamento horizontal observado, console sem erros. Prévia maxwell-termodinamica-mobile.jpg. Revisão conceitual pessoal pendente. Próxima ação: refazer a derivação de Helmholtz e comparar com o sinal de Gibbs antes de resolver o exemplo sem consulta. Saldo semanal após o bloco: 99%; parada operacional 65%.
