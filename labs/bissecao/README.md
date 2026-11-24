# Bisseção: uma raiz com intervalo controlado

Aprofundamento original de 13/10/2026 com apoio de IA para revisão de Jhuann. Referência temática: Burden, Faires e Burden, Análise Numérica, 10ª edição; exemplos próprios, sem transcrição.

## Um intervalo e uma hipótese de continuidade

Para f real contínua em [a,b], com a<b e sinais opostos nos extremos, o Valor Intermediário garante alguma raiz no interior. Se um extremo já é zero exato, ele fornece uma raiz sem reduzir o intervalo. O programa avalia valores, mas não prova continuidade de uma função arbitrária. Antes de usá-lo, declare o domínio e confira se há singularidades ou saltos no intervalo.

`continuidade + sinais opostos ⇒ existência de raiz`

## Uma redução e seu invariante

Calcule m=(a+b)/2. Se f(m)=0 exato, encontramos raiz. Caso contrário, seu sinal concorda com um dos extremos; mantenha a metade cujo par de extremos tem sinais opostos. O Valor Intermediário mantém pelo menos uma raiz nesse novo intervalo. O invariante é: o intervalo continua contendo raiz, sob as hipóteses. A largura cai pela metade; a raiz selecionada pode depender de qual metade foi mantida quando existem várias.

`intervalo com raiz → metade ainda com raiz`

## Convergência dos intervalos

Os intervalos são fechados, aninhados e têm larguras que tendem a zero. Na análise exata, isso os faz convergir a um ponto; a continuidade e o controle de sinais fazem esse ponto ser raiz. A bisseção não exige conhecer a derivada nem que exista uma única raiz no intervalo inicial. Ela localiza uma raiz contida na sequência mantida, sem prometer encontrar todas.

`largura após N reduções=(b₀−a₀)/2^N`

## Cota de posição e convenção de contagem

Aqui N conta reduções já realizadas. O ponto médio do intervalo que sobra depois delas está no máximo a meia largura de qualquer raiz nele, portanto erro≤(b₀−a₀)/2^(N+1). Não confunda N reduções com N avaliações de ponto médio: o código verifica o ponto médio do intervalo atual antes de efetuar a redução seguinte. Registrar essa convenção evita erros de uma potência de dois. A cota é de localização no modelo matemático, separada de erros na avaliação da função.

`|m_N−r|≤(b₀−a₀)/2^(N+1)`

## Exemplo: duas reduções para √2

Use f(x)=x²−2 em [1,2]. Os valores são −1 e 2. Em m=1,5, f é positivo: mantenha [1;1,5]. Em m=1,25, f é negativo: mantenha [1,25;1,5]. Depois dessas duas reduções, largura=0,25 e ponto médio=1,375, com cota de posição 0,125. O ponto médio não precisa ser a raiz exata; o valor da cota é garantido pelas hipóteses e pelo intervalo.

`N=2: largura=1/4; ponto médio=1,375; cota=1/8`

## Planejar a quantidade de reduções

Para uma tolerância absoluta ε de posição, queremos (b₀−a₀)/2^(N+1)≤ε. Se o intervalo inicial já tem meia largura menor que ε, N=0 basta nessa convenção. Caso contrário, escolha N pelo teto de log₂((b₀−a₀)/(2ε)). Para largura inicial 1 e ε=10⁻³, N=9 reduções dão cota 1/1024≈0,00097656. Essa conta planeja a redução do intervalo, não o custo total de avaliar uma f arbitrária.

`N≥max(0,ceil(log₂((b₀−a₀)/(2ε))))`

## Sem mudança de sinal não significa ausência de raiz

O método usa um critério suficiente. f(x)=x² em [−1,1] tem raiz em zero, mas ambos os extremos são positivos. A implementação rejeita esse intervalo porque seu contrato pede mudança de sinal; isso não prova que a função não tenha raiz. Localizar outro intervalo, analisar a função ou escolher outro método são perguntas diferentes. Não transforme uma falha do contrato num teorema de inexistência.

`sem mudança de sinal ≠ sem raiz`

## Sem continuidade, uma largura pequena pode enganar

A função −1 para x<0 e +1 para x≥0 muda de sinal em [−1,1], mas nunca zera. Bisseção aplicada mecanicamente mantém intervalos cada vez menores ao redor do salto. Pode cumprir uma tolerância de largura e retornar um candidato, sem uma raiz verdadeira. O exemplo executável mostra isso explicitamente: a função avaliada no candidato ainda tem módulo 1. A validação dos sinais não substitui a hipótese matemática de continuidade.

`salto: f(x)=±1 e nenhuma raiz`

## Resíduo precisa de escala para controlar posição

|f(m)| mede resíduo, enquanto |m−r| mede erro na raiz. Se f é diferenciável entre m e r e |f′|≥μ>0 nessa região, o Valor Médio dá |m−r|≤|f(m)|/μ. Para x²−2 em [1,2], f′=2x≥2; essa informação fornece uma cota adicional. Sem um limite apropriado da derivada, um resíduo pequeno pode corresponder a grande erro de posição, como na função quase plana da aula anterior.

`|f′|≥μ>0 ⇒ |m−r|≤|f(m)|/μ`

## Parada matemática e limites da máquina

Tolerância de largura, zero avaliado, falta de um novo ponto médio em float e orçamento esgotado são motivos diferentes de término. Um f(m)==0 em float é um zero na representação avaliada, não certificação independente da função matemática. O código evita testar sinais multiplicando f(a)f(b), pois produtos podem perder escala ou exceder a representação. Ele rejeita avaliações não finitas e sinaliza resolução/orçamento, mas não verifica continuidade nem erro dos dados da função.

`critério de largura / zero avaliado / resolução / orçamento`

## Roteiro para usar e ensinar

Declare função e domínio; justifique continuidade; registre extremos e seus valores. Trace reduções, mantenha o invariante e conte N com uma convenção explícita. Diga qual cota foi atingida e qual motivo de parada ocorreu. Confira um caso de raiz conhecida, uma raiz num extremo, um intervalo sem sinais opostos e o contraexemplo de salto. Apresente a garantia condicional completa, em vez de chamar qualquer número retornado de raiz certificada.

`hipóteses → intervalo → invariante → cota → parada → interpretação`

## Exercícios e resoluções

Tente antes de consultar; nomeie a referência, hipóteses e critério.

### 1. Largura inicial 1: qual largura após quatro reduções?

Resolução: 1/2⁴=1/16=0.0625.

### 2. Mudança de sinal garante raiz sem continuidade?

- Sim

- Não

Resolução: Não. 1/x muda de sinal entre valores negativos e positivos, mas não zera e não é contínua em zero.

### 3. Largura inicial 1; depois de quatro reduções, qual a cota para o ponto médio do intervalo restante?

Resolução: 1/2^(4+1)=1/32.

### 4. Largura inicial 1 e tolerância de posição 10⁻³: quantas reduções bastam segundo a convenção da aula?

Resolução: N=9 dá 1/1024≈0,00097656; N=8 ainda dá 1/512≈0,001953.

### 5. x² em [−1,1] não tem sinais opostos nos extremos. Isso prova ausência de raiz?

- Sim

- Não; x=0 é uma raiz

Resolução: O método rejeita esse intervalo, mas a função tem raiz em zero.

### 6. Se uma raiz está na região com |f′|≥2 e o resíduo é 0,04, qual a cota de posição fornecida por resíduo/2?

Resolução: 0,04/2=0,02.

### 7. Atingir o máximo de iterações sem cumprir o critério significa:

- Raiz encontrada automaticamente

- Orçamento esgotado; resultado não foi confirmado pelo critério

Resolução: O código sinaliza a interrupção, sem anunciar convergência.

### 8. A bisseção garante encontrar todas as raízes do intervalo inicial?

- Sim

- Não; mantém uma sequência que contém ao menos uma raiz

Resolução: A garantia é de localização de uma raiz na sequência mantida, não enumeração de todas.

### 9. Cumprir tolerância de largura na função de salto −1/+1 garante raiz?

- Sim

- Não; falta continuidade e a função nunca é zero

Resolução: A garantia matemática dependia da continuidade; o candidato não zera a função.

## Executar

Salve example.py e execute `python3 example.py`. Só biblioteca padrão, sem leitura interativa nem gravação de arquivos. São exemplos de apoio, não certificação de precisão de um problema físico.

## Revisão pessoal

Explique a garantia e seu limite, resolva um exemplo inédito e um caso em que o critério não pode ser aplicado. Os demais temas e a revisão de Computação 3 continuam pendentes.
