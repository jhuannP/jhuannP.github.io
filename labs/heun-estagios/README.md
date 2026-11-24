# Heun nesta trilha: trapézio explícito de duas avaliações

Rascunho original · 27/10/2026 · revisão pessoal pendente.

## A fórmula identifica o método, além do nome

Nesta aula, Heun significa o Runge–Kutta explícito de duas avaliações que faz uma previsão de Euler e corrige pela média das inclinações nos extremos. Também o chamamos trapézio explícito. A nomenclatura varia: Burden10 traduzido chama essa fórmula de Euler modificado na p.314 e usa Heun para um esquema diferente de ordem três na p.315. O improved Euler apresentado em FNC usa ponto médio, outra fórmula de ordem dois. Compare os estágios antes de transportar um nome ou um código entre fontes.

## Uma previsão ainda não é a correção

Dado yₙ no tempo tₙ, avalie k₁=f(tₙ,yₙ). Faça a previsão y*=yₙ+h k₁ no final do passo. Essa previsão permite obter uma inclinação no tempo seguinte sem resolver uma equação implícita. Ela é um estado intermediário: não substitua yₙ por y* antes de terminar a combinação das inclinações.

k₁=f(tₙ,yₙ); y*=yₙ+h k₁

## Use a média das inclinações

Avalie k₂=f(tₙ+h,y*). O valor aceito é yₙ₊₁=yₙ+h(k₁+k₂)/2. Os dois k têm unidades de derivada; só a multiplicação por h produz uma variação de y. Algumas fontes definem k como incremento e já incluem h; misturar convenções introduz um fator de passo a mais. O segundo estágio usa o tempo final e o estado previsto.

yₙ₊₁=yₙ+h(k₁+k₂)/2

## Por que isso atinge segunda ordem?

No caso escalar suave, escreva f=f(t,y) e expanda o segundo estágio: f(t+h,y+hf)=f+h f_t+h f_y f+O(h²). A atualização fica y+h f+(h²/2)(f_t+f_y f)+O(h³). Pela regra da cadeia, a solução exata tem y″=f_t+f_y f, de modo que os termos até h² coincidem. O defeito de um passo iniciado exatamente é O(h³); o resíduo dividido por h é O(h²). Essa dedução requer derivadas e restos limitados na região dos estágios.

## De defeito local a erro global

Se f é Lipschitz em y com constante L e os estágios permanecem na região considerada, a aplicação de um passo tem fator de propagação limitado por 1+hL+h²L²/2. Com defeito ≤Ch³, o erro satisfaz |eₙ₊₁|≤(1+hL+h²L²/2)|eₙ|+Ch³. Para h≤h₀, limite o fator por 1+hA, com A=L+h₀L²/2. Somar a progressão geométrica em horizonte fixo dá |eₙ|≤(Ch²/A)[exp(A(tₙ−t₀))−1] para A>0 e condição inicial exata. Se A=0, a soma direta dá C(tₙ−t₀)h². Assim a ordem global é dois sob essas hipóteses.

## Um passo com todos os números à vista

No exemplo y′=−y, y₀=1 e h=1/2: k₁=−1, y*=1/2, k₂=−1/2, média=−3/4 e variação=−3/8. O valor corrigido é 5/8=0,625, no tempo 1/2. A referência exata nesse tempo é e⁻¹ᐟ²≈0,606531. A correção melhora este passo em relação a Euler, que daria 0,5, mas ainda tem erro de discretização.

## Derivar o fator de amplificação

Para y′=−ay, a>0, ponha q=ah. A previsão é (1−q)yₙ e a segunda inclinação é −a(1−q)yₙ. Substituindo na média, yₙ₊₁=R(−q)yₙ, com R(−q)=1−q+q²/2. Essa expressão é exata para a recorrência em aritmética exata; e⁻ᵃʰ é o fator da solução contínua.

R(−q)=1−q+q²/2

## Mais ordem não amplia este intervalo real

Como R(−q)=[(q−1)²+1]/2, o fator é sempre positivo. Para haver decaimento estrito, R(−q)<1 equivale a 0<q<2, o mesmo intervalo real de Euler. Em q=2, R=1 e a aproximação mantém o valor em vez de decair. Para q>2, ela cresce. Portanto segunda ordem não remove a limitação de estabilidade deste teste nem resolve automaticamente rigidez.

## Um estágio negativo pode gerar um resultado positivo

Para q=3/2 e yₙ=1, a previsão é −1/2, mas o fator final é 5/8. A aproximação aceita permanece positiva e decai neste teste, enquanto Euler alternaria sinais. Para q>2, o valor final continua positivo, mas cresce artificialmente. Nem a positividade do resultado nem o nome do método garantem precisão; além disso, um estágio negativo pode impedir avaliar um f que só esteja definido para estados não negativos. A positividade aqui não é um teorema para toda EDO.

## O trapézio implícito resolve outra equação

No trapézio implícito, a inclinação final usa yₙ₊₁, ainda desconhecido: yₙ₊₁=yₙ+h[f(tₙ,yₙ)+f(tₙ+h,yₙ₊₁)]/2. Para o decaimento linear, seu fator é (1−q/2)/(1+q/2), diferente do polinômio do método explícito. Em q=1/2, o fator implícito é 3/5, enquanto o explícito é 5/8. Uma única correção a partir de Euler não é a resolução exata dessa equação implícita.

## O teste linear não distingue todos os métodos de ordem dois

O ponto médio explícito usa f(t+h/2,y+h f(t,y)/2), em vez da média nas duas extremidades. Ele tem o mesmo fator 1−q+q²/2 no teste linear, mas não é o mesmo algoritmo. Por exemplo, em y′=y², y₀=1 e h=1/2, o trapézio explícito dá 29/16=1,8125; o ponto médio dá 57/32=1,78125. A solução exata em t=1/2 é 2. Conferir apenas y′=−y pode deixar passar uma troca de estágios.

## Duas avaliações por passo precisam entrar na comparação

O método implementado faz duas chamadas a f em cada passo; Euler faz uma. Em [0,1], 20 passos de Heun custam 40 avaliações, enquanto 20 de Euler custam 20. Para comparar com igual número de avaliações, podemos usar Heun com 10 passos e Euler com 20, mantendo o mesmo problema e tempo final. Neste exemplo o primeiro tem menor erro; não é uma afirmação universal. Tempo de execução, memória e custo de cada chamada são outras medidas possíveis.

## A diferença entre previsão e correção não é o erro de Heun

A diferença yₙ₊₁−y*=h(k₂−k₁)/2 é tipicamente O(h²), enquanto o defeito local do valor corrigido é O(h³). No decaimento com q=1/2 e yₙ=1, essa diferença é 1/8, mas o erro do valor corrigido é aproximadamente 0,018469. A diferença contém principalmente informação sobre a previsão de Euler; não a use sem análise como estimativa de mesma ordem do erro local de Heun ou como tolerância global garantida.

## Refinamento e testes do integrador existente

O laboratório chama numerics4.step e integrate com method="heun". Registra os argumentos reais das duas chamadas de f, confere todos os nós contra a recorrência racional no teste linear e usa uma derivada afim no tempo para detectar um segundo estágio com tempo errado. Depois compara erros em T=1 com 10,20,40 e80 passos: a razão tende a 4 no regime observado. Uma referência do algoritmo não substitui a solução contínua; ambas entram na verificação.

## Uma revisão de vinte minutos

Refaça os quatro estágios do exemplo inicial, derive R(−q) e explique por que q=2 não decai. Compare a fórmula explícita com a implícita e com a de ponto médio. Por fim, estime a razão de erros no mesmo T=1 e conte avaliações de f. A ordem global depende de regularidade, estabilidade de propagação e horizonte fixo; eventos, singularidades, rigidez e malhas variáveis exigem outros cuidados. Revisão pessoal de Jhuann pendente.

## Exercícios e resoluções

1. Em y′=−y, y₀=1, após um passo h=1/2 do trapézio explícito desta aula, qual é o valor corrigido?

   Resolução: A média das inclinações é −0,75; a variação é −0,375.

2. Heun explícito remove toda restrição de estabilidade?

   Resolução: A região de estabilidade continua limitada.

3. No exemplo y′=−y, y₀=1 e h=1/2, quanto vale a previsão y*?

   Resolução: 1+(1/2)(−1)=1/2.

4. No mesmo exemplo, quanto vale a segunda inclinação k₂?

   Resolução: f(1/2,1/2)=−1/2.

5. Qual a média das inclinações −1 e −1/2?

   Resolução: (−1−1/2)/2=−3/4.

6. Para q=3/2, qual o fator de amplificação do trapézio explícito?

   Resolução: 1−3/2+(3/2)²/2=5/8.

7. Para q=2, qual o fator de amplificação?

   Resolução: 1−2+4/2=1: não decai.

8. Para q=1/2, qual o fator do trapézio implícito?

   Resolução: (1−1/4)/(1+1/4)=3/5.

9. Quantas chamadas a f fazem 20 passos do método explícito de duas avaliações desta aula?

   Resolução: 2×20=40, sem reaproveitamento externo.

10. Heun desta aula e ponto médio explícito são o mesmo algoritmo só porque coincidem no teste linear?

   Resolução: Em y′=y², os valores de um passo já diferem.

11. A diferença entre previsão e correção é automaticamente o defeito local de ordem três do valor corrigido?

   Resolução: Ela é tipicamente O(h²), dominada pela previsão de Euler.

12. Ao abrir uma fonte que usa o nome Heun, o que deve ser conferido?

   Resolução: Burden usa Heun para um esquema de ordem três; esta aula fixa explicitamente outro uso do nome.

## Fontes e convenções verificadas

Burden, Faires e Burden, Análise Numérica, tradução da 10ª edição norte-americana/3ª edição brasileira, Cengage2016: §5.4, pp.314–315/PDF328–329, consulta visual parcial em 27/10. P.314: Euler modificado com previsão e média dos extremos; p.315: nome Heun usado para esquema de ordem três. A aula preserva a fórmula RK2 já implementada e explicita a convenção local de nome, sem atribuir ao livro o mesmo nome. Exemplar digitalizado, sem extração de texto ou leitura integral. PDF contado a partir de 1; páginas editoriais previamente conferidas, exemplar privado não distribuído. Edição7 do programa não é presumida equivalente em paginação.

Driscoll e Braun, Fundamentals of Numerical Computation, §6.4: https://fncbook.com/rk/ . Consulta parcial em 27/10 de Taylor multivariável, derivação de ordem dois e ponto médio explícito chamado improved Euler. A fórmula exibida nessa fonte não é o trapézio explícito do site; o exemplo não foi copiado como se fosse. Código, diagrama, deduções e contraexemplo não linear próprios.

Programa CCM0226 segue o registro indexado de22/10; tentativas diretas de27/10, documentadas no bloco de Euler, falharam. Nenhuma nova abertura ou alegação de reconferência oficial neste bloco. Versão ministrada em2025 não recuperada. A aula desenvolve o tópico de métodos de passo simples, sem presumir quais métodos a turma usou.

## Laboratório

`audit.py` importa numerics4.integrate e usa a implementação existente method='heun'. Não é um solver autônomo. Rode da raiz do protótipo:

```sh
python3 -m labs.heun-estagios.audit
python3 -m unittest discover -s labs/heun-estagios -t .
```

A função racional `factor` descreve apenas o teste de decaimento q>0. Os testes registram argumentos reais dos dois estágios, usam y′=y² para distinguir ponto médio, conferem todos os nós de recorrências lineares e usam derivada afim no tempo para detectar avaliação na hora errada. Decimal confere escala do defeito local; a referência exp(−1) mede discretização global. Comparação a custo igual usa Euler20 versus RK2/Heun10, ambos20 avaliações; não é garantia geral nem benchmark de tempo.

## Registro pessoal — preencher ao estudar

- Data:
- Fórmula e nome que encontrei na minha fonte:
- Diferença entre previsto e aceito:
- Como contei o custo e interpretei q=2:
- Dúvida que restou:
