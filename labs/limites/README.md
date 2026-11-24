# Limite e valor no ponto: um furo não impede aproximação

13/10/2026. Conteúdo original com apoio de IA; rascunho para revisão de Jhuann.

## Objetivos

- Distinguir limite de valor no ponto e de continuidade.
- Simplificar uma expressão somente no domínio em que a igualdade vale.
- Justificar um limite pela identidade algébrica e por uma escolha de δ.
- Reconhecer limites de tabelas finitas e cuidado numérico.

## O limite examina um entorno perfurado

Para um limite finito em a, observamos f(x) perto de a com x≠a. A função pode não estar definida em a. O ponto a precisa permitir aproximações pelo domínio: ser um ponto de acumulação. Nesta aula, o domínio do quociente é ℝ sem o ponto 2, com aproximação pelos dois lados.

0<|x−a|<δ

## Substituição direta não resolve uma divisão indefinida

Para f(x)=(x²−4)/(x−2), substituir x=2 produz numerador e denominador zero, mas a divisão 0/0 não é um número. O fato de ambas as partes tenderem a zero não determina o limite do quociente. Por exemplo, x/x tende a 1, x²/x tende a 0 e x/x²=1/x não tem limite real bilateral finito em zero.

0/0 não é uma operação definida

## Fatore e preserve a condição do domínio

x²−4=(x−2)(x+2). Para x≠2, podemos cancelar x−2 e obter f(x)=x+2. Essa igualdade vale no entorno perfurado e justifica o limite 4. Não preenche automaticamente o valor do quociente em 2; a expressão original continua sem definição ali.

(x²−4)/(x−2)=x+2, x≠2

## Uma garantia explícita confirma a aproximação

Fora de 2, |f(x)−4|=|x−2|. Dada ε>0, escolher δ=ε faz 0<|x−2|<δ implicar |f(x)−4|<ε. O argumento cobre todos os x permitidos, não apenas os valores de uma tabela.

|f(x)−4|=|x−2|; δ=ε

## Mudar o valor isolado não muda o limite

Defina g(2)=b e g(x)=x+2 fora de 2. Qualquer b real deixa o limite em 2 igual a 4, pois o limite não usa a entrada x=2. Continuidade em 2 requer o valor definido coincidir com o limite, portanto somente b=4. O círculo aberto e o ponto cheio da demonstração representam esses dois papéis.

## Igualdade local é suficiente

Se duas funções coincidem em um entorno perfurado de a, têm o mesmo limite ali, quando o limite existe. Basta reduzir δ ao mínimo entre o raio onde coincidem e o raio da garantia ε. Comportamento longe de a não decide esse limite. Essa é a razão de a fatoração local ser útil mesmo sem igualdade dos domínios completos.

## O limite é único sob a hipótese de aproximação

Se L₁ e L₂ fossem limites distintos, escolha ε=|L₁−L₂|/3. As duas definições forneceriam raios; num ponto do domínio dentro do menor raio, a desigualdade triangular daria |L₁−L₂|≤|L₁−f(x)|+|f(x)−L₂|<2ε, uma contradição. A existência de pontos do domínio arbitrariamente perto de a é necessária para esse argumento.

## Uma tabela finita pode sugerir o limite errado

Considere uma função que vale 0 apenas em ±0,1; ±0,01; ±0,001 e vale 1 nos demais pontos. Uma tabela nesses seis pontos mostra apenas zeros e poderia sugerir limite 0 em zero. Porém, em 0<|x|<0,0005, a função é sempre 1, então o limite verdadeiro é 1. A tabela precisa de uma justificativa além de seus pontos.

## Matemática real e cálculo aproximado são etapas diferentes

Calcular o quociente original muito perto de 2 em ponto flutuante pode sofrer cancelamento no numerador; o próprio deslocamento pode ser arredondado para zero. A identidade x+2 é uma forma melhor para avaliar o entorno neste exemplo. O laboratório usa frações para conferir a igualdade sem erro de arredondamento, mas testes finitos não substituem a prova.

## Prepare a explicação antes de usar a ferramenta

Descreva o domínio, a aproximação pelos dois lados, a condição de cancelamento e o papel do valor isolado. Peça ao aluno prever o limite antes de mover f(2). Encerre comparando limite e continuidade. O material é original em rascunho; as notas pessoais de Cálculo 1 ainda precisam ser preparadas por Jhuann.

## Exemplo resolvido

Se g(2)=9 e g(x)=x+2 fora de 2, qual o limite e quando haveria continuidade?

1. O limite usa apenas x≠2 perto de 2.
2. Nesse entorno, g(x)−4 = x−2.
3. Para toda ε>0, δ=ε garante a aproximação de 4.
4. Logo o limite é 4, embora g(2)=9.
5. A função é descontínua em 2; escolher g(2)=4 tornaria essa extensão contínua.

## Exercícios e resoluções

### Se g(2)=9 e g(x)=x+2 fora de 2, qual o limite em 2?

O entorno é descrito por x+2.

### A função do exemplo é contínua em 2?

Sim
Não

O valor 9 difere do limite 4.

### Qual valor g(2) torna a extensão contínua?

Deve coincidir com o limite 4.

### Qual o valor do quociente (x²−4)/(x−2) em x=2,01?

Como x≠2, use x+2=4,01.

### Na construção |g(x)−4|=|x−2|, qual δ=ε para ε=0,05?

A identidade permite δ=0,05.

### Na função que vale 0 nos seis pontos ±0,1; ±0,01; ±0,001 e 1 nos demais, qual o limite em zero?

Para 0<|x|<0,0005 não há exceções; a função vale 1.

### Cancelar x−2 define o quociente original em x=2?

Sim
Não

O cancelamento exige x≠2; definir uma extensão é outra etapa.

### Numerador e denominador tendendo a zero determinam um único limite do quociente?

Sim
Não

x/x, x²/x e x/x² têm comportamentos distintos.

### Uma tabela de seis pontos prova o comportamento de todos os reais suficientemente próximos?

Sim
Não

É evidência parcial; o contraexemplo da aula mostra o limite da inferência.

## Laboratório

Baixe experiment.py e execute `python3 experiment.py`. Apenas biblioteca padrão e frações racionais. Os exemplos verificam identidades e casos; não substituem a prova sobre todos os reais. Sem ler dados privados ou escrever resultados externos.

## Preparação manuscrita

Escreva domínio e quantificadores; resolva o exemplo por identidade; justifique a escolha de δ; desenhe o entorno e a tolerância; contraste com um contraexemplo. As notas pessoais de Cálculo 1 ainda precisam ser preparadas por Jhuann.

## Hipóteses e limites

- Limite real relativo ao domínio, com ponto de acumulação.
- Fatoração/cancelamento somente onde o denominador não é zero.
- Amostras e gráficos não substituem a justificativa universal.
- Notas originais em rascunho, distintas das notas pessoais ainda a preparar.
