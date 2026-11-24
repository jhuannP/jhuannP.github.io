# Erro absoluto, relativo e a escala da pergunta

Aprofundamento original de 13/10/2026 com apoio de IA para revisão de Jhuann. Referência temática: Burden, Faires e Burden, Análise Numérica, 10ª edição; exemplos próprios, sem transcrição.

## Antes da conta: referência e quantidade

Declare o que está sendo comparado e de onde vem a referência: solução analítica, valor racional exato, cálculo de precisão maior ou dado fornecido. Um método mais sofisticado não se torna automaticamente a verdade. Diferença entre dois métodos é uma diferença observada; só pode ser chamada de erro em relação à referência quando essa referência foi justificada. Em medições, a grandeza verdadeira pode não ser conhecida.

`referência identificada → comparação com significado`

## Erro absoluto mantém a unidade

Para referência x e aproximação x̂, e_abs=|x̂−x|. O módulo mede distância sem sinal. Se a grandeza é em metros, o erro também é em metros. O erro assinado x̂−x pode ajudar a detectar superestimação ou subestimação, mas não é o mesmo que o erro absoluto. Para x=2 e x̂=1,98, o erro assinado é −0,02 e o absoluto 0,02.

`e_abs=|x̂−x|`

## Erro relativo depende da escala de referência

Quando x≠0, e_rel=e_abs/|x| é adimensional. No exemplo, 0,02/2=0,01, ou 1%. O mesmo erro absoluto 0,02 para referência 0,1 equivale a 20%, mostrando por que escala importa. Escolher outra grandeza ou unidade exige transformar também a referência e interpretar o resultado. Converter de metros para centímetros muda os números do erro absoluto, mas não esse erro relativo.

`e_rel=|x̂−x|/|x|, para x≠0`

## Referência zero e valores próximos de zero

Se x=0, a divisão da definição não existe. Para aproximação 0,0005, o erro absoluto é 0,0005 e o relativo dessa definição fica indefinido, não zero. Perto de zero, até uma diferença absoluta pequena pode produzir razão grande. Uma escala externa pode ser usada, mas precisa ser nomeada: erro dividido por uma escala de referência escolhida é outro indicador, não a mesma definição.

`x=0: e_rel indefinido; usar critério absoluto ou escala declarada`

## Tolerância é uma decisão explícita

Uma política possível de aceitação é e_abs≤atol+rtol|x|, com referência x, tolerância absoluta na mesma unidade e relativa adimensional. Para atol=0,001, rtol=0,01 e x=2, a faixa permitida é 0,021. Com x=0, permanece atol. Essa é uma política declarada, não uma lei universal nem automaticamente a regra de toda biblioteca. Não confunda calcular o erro com escolher se ele é aceitável para uma aplicação.

`e_abs≤atol+rtol|x|`

## Fontes diferentes pedem controles diferentes

O resultado pode incorporar escolha de modelo, erro dos dados, discretização, término de iteração e arredondamento. Refinar a malha não corrige um modelo físico inadequado. Aumentar iterações não recupera informação perdida nos dados. Aumentar precisão de representação não resolve automaticamente falta de convergência. Nomeie qual fonte está sendo estudada e quais permanecem fora do experimento.

`modelo / dados / discretização / iteração / arredondamento`

## Uma decomposição produz cota, não soma exata dos módulos

Se distinguimos valor real, solução do modelo, solução discretizada e resultado calculado, podemos inserir diferenças intermediárias. Pela desigualdade triangular, o erro total é limitado pela soma dos módulos dessas diferenças. Eles podem cancelar ou reforçar, então a soma dos erros absolutos não é necessariamente o erro total exato. A cota só é útil se os termos também forem conhecidos ou controlados.

`|x_calc−x_real|≤|x_calc−x_disc|+|x_disc−x_modelo|+|x_modelo−x_real|`

## Resíduo é outra pergunta

Num problema f(r)=0, o resíduo da aproximação é |f(x̂)|. Ele mede a falha na equação, enquanto |x̂−r| mede erro na raiz. Para f(x)=10⁻¹²(x−1), x̂=0 tem resíduo 10⁻¹², mas erro de posição 1. A função tem escala muito pequena. Se uma cota adequada da derivada está disponível, ela pode ligar as duas quantidades; sem essa informação, não use resíduo pequeno como certificado universal.

`resíduo |f(x̂)| ≠ erro de posição |x̂−r|`

## Representação e impressão

O valor matemático decimal 0,02 não precisa ser representado exatamente por um float binário. O código pode produzir 0,020000000000000018 ao subtrair 2 e 1,98. Arredondar a impressão facilita a leitura, mas não altera o cálculo anterior nem elimina suas fontes de erro. O exemplo com Fraction confere a referência decimal exata, enquanto a função numérica trabalha com float e declara sua referência zero por None no erro relativo.

`arredondar a saída ≠ tornar a conta exata`

## Roteiro para estudar e comunicar

Registre quantidade, unidade, referência e aproximação. Calcule absoluto e relativo quando definido; escolha tolerâncias com significado. Nomeie as fontes controladas e os limites da verificação. Use um caso conhecido e uma mudança de escala para conferir interpretação. Num relatório, dê contexto ao número do erro: um valor sem referência, unidade ou critério não demonstra precisão do modelo.

`quantidade → referência → erro → critério → limites`

## Exercícios e resoluções

Tente antes de consultar; nomeie a referência, hipóteses e critério.

### 1. Referência 10, aproximação 9,5: qual erro absoluto?

Resolução: |9.5−10|=0.5.

### 2. No mesmo caso, qual erro relativo?

Resolução: 0.5/10=0.05, ou 5%.

### 3. Referência 2 e aproximação 1,98: qual erro relativo em porcentagem?

Resolução: 0,02/2=0,01=1%.

### 4. Para referência zero, o erro relativo |x̂−x|/|x| é:

- Sempre zero

- Indefinido

- Sempre igual ao absoluto

Resolução: A definição não se aplica; use um critério absoluto ou uma escala declarada.

### 5. Na política atol+rtol|x|, com atol=0,001, rtol=0,01 e x=2, qual a faixa permitida?

Resolução: 0,001+0,02=0,021.

### 6. Diferença entre dois métodos sem referência justificada prova o erro verdadeiro de um deles?

- Sim

- Não

Resolução: Ela mede divergência entre resultados, sem escolher automaticamente a referência correta.

### 7. Para f(x)=10⁻¹²(x−1), raiz r=1 e aproximação 0, qual erro de posição?

Resolução: |0−1|=1.

### 8. Refinar o passo resolve automaticamente erro de modelo físico?

- Sim

- Não

Resolução: Um algoritmo pode convergir para a solução de um modelo inadequado.

### 9. A soma dos módulos de diferenças intermediárias é sempre o erro total exato?

- Sim

- Não; em geral fornece uma cota por desigualdade triangular

Resolução: O módulo da soma pode ser menor que a soma dos módulos.

## Executar

Salve example.py e execute `python3 example.py`. Só biblioteca padrão, sem leitura interativa nem gravação de arquivos. São exemplos de apoio, não certificação de precisão de um problema físico.

## Revisão pessoal

Explique a garantia e seu limite, resolva um exemplo inédito e um caso em que o critério não pode ser aplicado. Os demais temas e a revisão de Computação 3 continuam pendentes.
