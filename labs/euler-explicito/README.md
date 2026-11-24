# Euler explícito: derivação, erro e estabilidade

Rascunho original · 27/10/2026 · revisão pessoal pendente.

## Da equação a uma atualização

Um problema de valor inicial especifica y′=f(t,y), o valor y(t₀)=y₀ e um intervalo de tempo. Escolha n passos iguais, com h=(T−t₀)/n e tₖ=t₀+kh. Em vez de conhecer a curva inteira, calculamos aproximações yₖ nos nós. Usar a inclinação no início do passo e avançar por uma reta dá Euler explícito. O lado direito depende apenas de valores já conhecidos, sem resolver uma equação para yₖ₊₁.

yₖ₊₁ = yₖ + h f(tₖ,yₖ)

## Derivar a regra com um resto explícito

Se a solução exata y tem segunda derivada contínua, Taylor fornece y(t+h)=y(t)+h y′(t)+(h²/2)y″(ξ), com ξ entre t e t+h. Substituir y′(t)=f(t,y(t)) e omitir o termo final produz Euler. O termo omitido mede o defeito de um passo iniciado na solução exata. Não é automaticamente o erro total depois de muitos passos.

dₖ = y(tₖ₊₁) − y(tₖ) − h f(tₖ,y(tₖ))

## Duas convenções para erro local

Se |y″|≤M no intervalo, o defeito no estado satisfaz |dₖ|≤Mh²/2, de ordem h². Alguns textos chamam de erro de truncamento local o resíduo dividido por h: τₖ=dₖ/h, de ordem h. Antes de comparar ordens, verifique qual objeto foi definido. A expressão “Euler é de primeira ordem” refere-se ao erro global em horizonte fixo, sob hipóteses apropriadas, e não contradiz um defeito no estado de ordem h².

## Um problema de referência

Para y′=−y, y(0)=1, a solução exata é e⁻ᵗ. Euler produz yₖ₊₁=(1−h)yₖ; por indução, yₖ=(1−h)ᵏ. A fórmula fechada descreve exatamente o algoritmo em aritmética exata, enquanto e⁻ᵗ descreve a EDO. Concordar com a recorrência verifica a implementação, mas não torna o método exato para a equação.

yₖ = (1−h)ᵏ

## Estabilidade não é precisão

O fator 1−h deve ter módulo menor que 1 para que as perturbações e valores do teste decaiam quando o número de passos cresce, com h fixo: 0<h<2. Mesmo nessa faixa a aproximação pode ser ruim. Se 1<h<2, os valores alternam sinal; a solução exata continua positiva. Em h=2 o fator é −1: o erro não é amortecido. Distinguir essa fronteira de decaimento estrito evita chamar uma oscilação persistente de solução precisa.

|1−h| < 1 ⇔ 0 < h < 2

## A escala do problema entra pelo produto ah

Para y′=−ay, com a>0, defina q=ah; o fator é 1−q. A condição de decaimento estrito é 0<q<2. Se a representa uma taxa em s⁻¹ e h está em segundos, q é adimensional. Mudar a unidade de tempo sem converter a também muda o problema. Uma taxa dez vezes maior exige um passo dez vezes menor para manter o mesmo fator.

q = ah; yₖ = (1−q)ᵏ y₀

## Positividade exige uma condição mais forte

Com y₀>0, 0<q<1 mantém valores estritamente positivos e decrescentes. q=1 zera a aproximação em um passo, embora a solução exata ainda seja positiva em tempo finito. 1<q<2 decai alternando o sinal; q=2 mantém amplitude; q>2 faz a amplitude crescer. Portanto preservar não negatividade exige q≤1, enquanto o decaimento assintótico permite q<2. A necessidade física de positividade é uma pergunta diferente da estabilidade linear.

## Um passo estável ainda pode ter erro grande

O exemplo inicial usa h=1/2: y₁=1/2 e y₂=1/4 no tempo final T=1. A referência exata é e⁻¹≈0,367879, e o erro absoluto é aproximadamente 0,117879. O método preserva sinal e decai, mas subestima a solução. Estabilidade evita um tipo de crescimento artificial; não determina a tolerância que o resultado atende.

## Acumular erros: a hipótese de Lipschitz

Suponha f contínua na faixa de tempos e Lipschitz em y com constante L≥0, e |y″|≤M ao longo da solução. Compare a solução exata e a aproximação nos mesmos nós: eₖ=y(tₖ)−yₖ. Subtrair a atualização de Euler da identidade com resto dá eₖ₊₁=eₖ+h[f(tₖ,y(tₖ))−f(tₖ,yₖ)]+dₖ. Pela condição de Lipschitz, |eₖ₊₁|≤(1+hL)|eₖ|+Mh²/2. Estas hipóteses devem valer onde comparamos os estados; a formulação global em y é uma condição suficiente simples.

|eₖ₊₁| ≤ (1+hL)|eₖ| + Mh²/2

## Somar a recorrência prova ordem global um

Com condição inicial exata, e₀=0. Iterar a desigualdade anterior soma uma progressão geométrica: para L>0, |eₖ|≤(Mh/2L)[(1+hL)ᵏ−1]. Como (1+hL)ᵏ≤exp(Lkh), em horizonte T−t₀ fixo obtemos |eₖ|≤(Mh/2L)[exp(L(tₖ−t₀))−1], de ordem h. Para L=0, a soma direta dá |eₖ|≤M(tₖ−t₀)h/2. O horizonte fixo importa: não estenda essa conclusão a tempo arbitrariamente longo mantendo a mesma cota.

|eₖ| ≤ (Mh/2L)[exp(L(tₖ−t₀))−1], L>0

## Conferir a cota em um caso conhecido

No problema y′=−y em [0,1], podemos usar L=1 e M=1 porque y″=e⁻ᵗ≤1. A cota no final é h(e−1)/2. Para h=1/2 ela vale aproximadamente 0,42957, maior que o erro observado 0,117879. Uma cota válida pode ser conservadora; não é uma previsão exata do erro. Ela explica a dependência com h e as hipóteses, enquanto a referência permite medir o erro deste caso.

## Refinar no mesmo tempo final

Para estudar convergência, mantenha a EDO, a condição inicial e T=1; varie n=10,20,40,80, usando h=1/n. Compare yₙ com e⁻¹. O erro cai aproximadamente pela metade quando h é dividido por 2, no regime observado. Para dois erros não nulos, a ordem estimada é log₂(E_h/E_h/2). Razão próxima de 2 é evidência experimental deste problema; a prova da ordem exige as hipóteses e a recorrência acima. Não compare “dez passos” de tamanhos diferentes sem conferir os tempos finais.

## Estabilidade absoluta não é zero-estabilidade

No teste linear, manter h fixo e observar muitos passos examina o fator de amplificação 1−ah e sua região de estabilidade absoluta. A convergência em intervalo fixo usa h→0, com o número de passos aumentando. Zero-estabilidade é outro conceito, de controle da propagação de perturbações em intervalo fixo; não conclua que Euler deixa de ser zero-estável por um passo grande no teste de decaimento. Nesta aula, a análise detalhada se limita ao caso escalar real; regiões complexas e teoremas gerais ficam para aprofundamento.

## O laboratório audita o integrador existente

O laboratório chama numerics4.integrate com method="euler"; não cria outro solver. Uma referência racional calcula (1−q)ᵏ em aritmética exata e compara todos os nós do algoritmo. Ela verifica implementação, sinal e fronteiras sem erro de arredondamento na referência. O estudo de refinamento usa a solução contínua e⁻ᵗ para medir discretização. Os dois testes respondem perguntas distintas. O módulo requer executar a partir da raiz do protótipo, onde está numerics4.py.

## Uma revisão de vinte minutos

Derive a atualização por Taylor, diferencie dₖ de dₖ/h e reconstrua a desigualdade do erro. Para q=3/2, explique por que há decaimento numérico com sinal fisicamente inadequado; para q=2, explique por que a amplitude persiste. Refaça o refinamento em T=1 e registre o que conseguiu justificar sem solução. Sistemas, rigidez, eventos, malhas variáveis e referência experimental continuam além deste recorte. Revisão pessoal de Jhuann pendente.

## Exercícios e resoluções

1. Com h=0,25 e y₀=1, qual é y₁ para y′=−y?

   Resolução: y₁=1−0,25×1=0,75.

2. Com h=2,5 o método para y′=−y é:

   Resolução: O fator 1−h=−1,5 tem módulo maior que 1. As amplitudes crescem.

3. No PVI y′=−y, y₀=1, com h=1/2, qual é y₂?

   Resolução: (1−1/2)²=1/4.

4. Com a=4 s⁻¹ e h=0,1 s, qual é q=ah?

   Resolução: 4×0,1=0,4, adimensional.

5. Para q=3/2 e y₀=1, qual é y₁?

   Resolução: 1−3/2=−1/2.

6. Para q=2 e y₀=1, qual é y₂?

   Resolução: (−1)²=1: não houve decaimento.

7. Para q=5/2 e y₀=1, qual é y₂?

   Resolução: (−3/2)²=9/4.

8. Quantos passos iguais de h=1/40 levam de t=0 até T=1?

   Resolução: n=(T−t₀)/h=40.

9. Se o erro cai de 0,02 para 0,01 ao dividir h por 2, qual a ordem estimada log₂(E_h/E_h/2)?

   Resolução: log₂(2)=1.

10. Para 1<q<2, Euler no teste y′=−ay preserva a positividade de y₀>0?

   Resolução: Os valores alternam sinal embora a amplitude decaia.

11. Com solução C² e |y″| limitado, qual a ordem do defeito no estado de um passo iniciado exatamente?

   Resolução: O resto de Taylor no estado é de ordem h²; dividido por h fica de ordem h.

12. Coincidir com (1−h)ⁿ prova que Euler resolve exatamente y′=−y?

   Resolução: Confere o algoritmo; a solução contínua é e⁻ᵗ, geralmente diferente.

## Fontes e limites

Burden, Faires e Burden, Análise Numérica, tradução da 10ª edição norte-americana, 3ª edição brasileira, Cengage 2016: sumário p.xiv/PDF12 e §5.2 pp.290–291 e294–295/PDF304–305 e308–309, consulta visual parcial em 27/10/2026. P.291: Taylor e atualização; p.295: teorema5.9, hipóteses e cota global. PDF contado a partir de 1; offset confirmado nesses recortes. Arquivo é digitalização sem texto útil nos registros anteriores; não se alegou extração ou leitura integral. A referência do programa é a 7ª edição (2000), não presumida equivalente em paginação. Exemplar privado não distribuído.

Fundamentals of Numerical Computation, Driscoll e Braun, §6.2: https://fncbook.com/euler/ . Consulta parcial em 27/10/2026: definição, nós, derivação e resíduo local. O resíduo dividido por h é distinguido do defeito no estado usado aqui. Exemplo de decaimento, diagrama, código e exercícios próprios; não são exercícios transcritos dos autores.

Programa CCM0226 previamente indexado em 22/10/2026, ativação exibida 01/01/2011: https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0226 . Aberturas diretas em 27/10 falharam (timeout/cache miss), portanto não se registra nova verificação do conteúdo oficial. Versão ministrada em 2025 ainda não recuperada. Este recorte desenvolve os métodos de passo simples já mapeados, sem alterar itens do programa.

## Laboratório: duas referências diferentes

`audit.py` importa o integrador existente `numerics4.py` da raiz do protótipo. Não é um arquivo autônomo nem um segundo solver. Execute a partir da raiz:

```sh
python3 -m labs.euler-explicito.audit
python3 -m unittest discover -s labs/euler-explicito -t .
```

`exact_recurrence(q,n)` usa Fraction para conferir a recorrência do algoritmo, aceitando q racional positivo e n inteiro não negativo. `refinement` chama o solver já existente para o PVI fixo em T=1. A referência contínua exp(−1) mede discretização; a referência racional mede implementação. Testes distinguem os objetivos, usam Decimal para defeitos locais pequenos, conferem fronteiras, cota global e erros de entrada do integrador. Não são evidência de execução de EP ou pesquisa pessoal.

## Registro pessoal — preencher ao revisar

- Data:
- Como distingui as duas convenções de erro local:
- Como justifiquei a cota global:
- Por que q=3/2 perde positividade:
- Dúvida que permaneceu:

Sem revisão pessoal concluída. Métodos implícitos, sistemas, rigidez, eventos e malha variável permanecem em outros recortes e não são encerrados por esta aula.
