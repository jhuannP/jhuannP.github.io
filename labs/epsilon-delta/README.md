# Épsilon e delta: traduzir proximidade em uma garantia

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Interpretar a ordem dos quantificadores e o entorno perfurado.
- Construir δ para funções afins e para x² perto de 1.
- Distinguir escolha suficiente de escolha ingênua.
- Usar um contraexemplo sem tratar verificações finitas como prova.

## A definição estabelece uma garantia universal

Dizer que f(x) tende a L quando x tende a a significa: para toda ε>0, existe δ>0 tal que todo x do domínio com 0<|x−a|<δ satisfaz |f(x)−L|<ε. Assumimos que a é ponto de acumulação do domínio. A distância positiva exclui o valor isolado f(a).

∀ε>0 ∃δ>0: 0<|x−a|<δ ⇒ |f(x)−L|<ε

## A ordem não permite ajustar δ depois de ver cada x

A tolerância ε vem primeiro; δ pode depender dela, da função e do ponto fixado. Depois dessa escolha, a garantia deve valer para todos os x admissíveis. Escolher um δ diferente para salvar cada ponto testado não demonstra a definição. A mesma escolha precisa controlar o intervalo inteiro.

## Função afim: uma identidade fornece δ

Para f(x)=3x−1 perto de a=2, L=5 e |f(x)−5|=3|x−2|. Escolha δ=ε/3. Se 0<|x−2|<δ, então o erro é menor que 3δ=ε. Qualquer δ positivo menor também serve; não precisamos de uma escolha única.

δ=ε/3

## Inclinações negativas e funções constantes

Para f(x)=mx+b, o erro em relação a f(a) é |m||x−a|. Se m≠0, δ=ε/|m| funciona, inclusive com m negativo. Se m=0, o erro de saída é sempre zero, então qualquer δ>0 serve. Usar ε/m sem valor absoluto pode produzir um raio negativo e não atende a definição.

## No caso quadrático, controle um fator primeiro

Para f(x)=x² perto de a=1 e L=1, |x²−1|=|x−1||x+1|. O segundo fator varia com x. Imponha primeiro |x−1|<1; então 0<x<2 e |x+1|<3. Agora podemos limitar o produto por 3|x−1|.

|x²−1|=|x−1||x+1|

## Combine duas restrições com o mínimo

Escolha δ=min(1,ε/3). A hipótese |x−1|<δ garante ao mesmo tempo |x−1|<1 e |x−1|<ε/3. Portanto |x²−1|<3|x−1|<ε. Mesmo se δ=1, a desigualdade estrita na entrada mantém a cota necessária. Essa escolha é suficiente; não alegamos ser o maior raio possível.

δ=min(1,ε/3)

## Uma escolha ingênua pode falhar dentro do intervalo

Se escolhermos δ=ε, tome x=1+ε/2. A distância de entrada ε/2 é positiva e menor que δ, mas |x²−1|=ε+ε²/4>ε. Assim essa escolha não garante a condição. Com ε=0,3, x=1,15 e o erro é 0,3225. O ponto que falha basta para refutar aquela escolha; um ponto que passa não basta para prová-la.

x=1+ε/2 ⇒ |x²−1|=ε+ε²/4

## Fronteiras e centro não pertencem à premissa

A definição usa 0<|x−a|<δ. O centro x=a é excluído, e os pontos com distância exatamente δ não são cobertos por essa premissa. Fora do intervalo, uma saída ainda pode cair na tolerância, mas isso não estabelece a garantia. A demonstração informa separadamente entrada admissível e erro de saída.

## A prova e os testes têm funções diferentes

A prova algébrica controla todos os reais no entorno. Frações exatas conferem identidades e casos racionais sem erro de arredondamento; não enumeram todos os reais. Gráficos e valores selecionados ajudam a interpretar quantificadores, encontrar erros e visualizar contraexemplos, sem substituir o argumento.

## Use a demonstração com uma pergunta de cada vez

Comece com a escolha justificada e peça uma previsão para o ponto. Depois escolha δ=ε, mantendo ε=0,3 e deslocamento 0,5δ, para ver a falha. Mova o ponto para o centro e para fora do intervalo: a premissa deixa de valer. O gráfico muda de escala com δ; a prova deve permanecer independente da aparência.

## Exemplo resolvido

Para x² em a=1 e ε=0,3, qual δ justificado funciona?

1. Fatore o erro: |x²−1| = |x−1| |x+1|.
2. Imponha distância de entrada menor que 1 para garantir |x+1|<3.
3. Escolha δ = min(1; 0,3 / 3) = 0,1.
4. Se 0<|x−1|<0,1, então |x²−1|<0,3.
5. A escolha ingênua δ=0,3 permite x=1,15, cujo erro é 0,3225: um contraexemplo.

## Exercícios e resoluções

### Na função afim 3x−1 em a=2, com ε=0,3, qual δ=ε/3?

0,3/3=0,1.

### Verificar 100 entradas prova sozinho a condição para todos os reais?

Sim
Não

A garantia universal requer o argumento algébrico.

### Na função afim de inclinação −2, com ε=0,4, qual δ=ε/|m|?

0,4/2=0,2; o raio deve ser positivo.

### Para x² em a=1, com ε=0,3, qual δ=min(1,ε/3)?

min(1,0,1)=0,1.

### Na mesma construção, com ε=4, qual δ?

min(1,4/3)=1.

### Para x=1,15, quanto vale |x²−1|?

1,15²−1=1,3225−1=0,3225.

### δ pode ser ajustado separadamente para cada x depois de observar o erro?

Sim
Não

Depois de escolher δ, a condição precisa valer para todos os x admissíveis.

### Um ponto com |x−a|=δ está coberto pela premissa estrita?

Sim
Não

A condição exige distância estritamente menor que δ.

### Se f é constante perto de a, existe uma única escolha possível de δ?

Sim
Não

O erro é zero; qualquer raio positivo contido nesse entorno serve.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Apenas biblioteca padrão e frações racionais. Os exemplos verificam identidades e casos; não substituem a prova sobre todos os reais. Sem ler dados privados ou escrever resultados externos.

## Preparação manuscrita

Escreva domínio e quantificadores; resolva o exemplo por identidade; justifique a escolha de δ; desenhe o entorno e a tolerância; contraste com um contraexemplo. As notas pessoais de Cálculo 1 ainda precisam ser preparadas por Jhuann.

## Hipóteses e limites

- Domínio real com ponto de acumulação para a definição de limite.
- ε e δ positivos; desigualdades estritas e entorno perfurado.
- Construção quadrática específica a f(x)=x² em a=1.
- Verificação finita não é prova do quantificador universal.
