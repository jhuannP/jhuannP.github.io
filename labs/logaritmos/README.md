# Logaritmos — aprofundamento da aula existente

## Logaritmo responde qual expoente produz o argumento

A escrita log_b(x)=y significa bʸ=x. Por exemplo, log₂(8)=3 porque 2³=8. A base b informa qual família de potências estamos usando; x é o argumento, e y é o resultado. Não se calcula um logaritmo dividindo argumento por base. Nesta aula trabalhamos apenas com logaritmos reais, em bases positivas diferentes de 1 e argumentos positivos.

log_b(x)=y ⇔ bʸ=x

## As restrições da base garantem uma inversa

Com b>0 e b≠1, a função exponencial bʸ associa a cada expoente real um valor positivo e é estritamente monótona. Cada argumento positivo corresponde a um único expoente. A base 1 não serve: 1ʸ=1 para todos os expoentes e não permite recuperar y. Bases negativas não definem essa função exponencial real para todo expoente real. Argumentos zero ou negativos ficam fora do domínio do logaritmo real desta aula.

## Argumento menor que um pode produzir resultado negativo

Na base 2, (1/2)²=1/4 também é 2⁻²=1/4, portanto log₂(1/4)=−2. O argumento é positivo; o resultado é negativo. Já na base 1/2, (1/2)⁻²=4, logo log_(1/2)(4)=−2. Não conclua que todo logaritmo de número maior que 1 é positivo: isso depende da base. Sempre confira a resposta voltando à potência.

## A regra do produto vem das potências de mesma base

Se r=log_b(u) e s=log_b(v), temos u=bʳ e v=bˢ. Multiplicando, uv=bʳ⁺ˢ; pela definição, log_b(uv)=r+s. As hipóteses u>0 e v>0 permitem escrever os dois logaritmos separados. No exemplo u=8 e v=4, em base 2, a soma é 3+2=5 e 2⁵=32 confirma o produto.

log_b(uv)=log_b(u)+log_b(v), u,v>0

## Quocientes e potências também conservam as hipóteses

Como bʳ/bˢ=bʳ⁻ˢ, obtemos log_b(u/v)=log_b(u)−log_b(v), para u,v>0. Para u>0 e expoente real t, log_b(uᵗ)=t log_b(u). Assim log₃(81/3)=4−1=3 e log₂(8²)=2×3=6. O fato de u² ser positivo não autoriza escrever 2log_b(u) quando u é negativo: o segundo membro não estaria definido nos reais.

## Soma de argumentos não é produto

Compare log₂(2+4)=log₂(6) com log₂(2)+log₂(4)=1+2=3. Se a primeira expressão fosse 3, teríamos 2³=6, mas 2³=8. Logo são diferentes. Um exemplo isolado de igualdade não demonstraria uma regra: para u=v=2 ocorre a coincidência 2+2=2×2, que pode esconder o erro. Ao aplicar uma propriedade, confira a operação que existe dentro do argumento.

## O gráfico muda de sentido quando a base atravessa 1

Para b>1, log_b(x) é crescente; para 0<b<1, é decrescente. Em ambos os casos passa por (1,0), tem domínio x>0 e assume todos os valores reais. A reta x=0 é uma assíntota vertical; ela não pertence ao domínio. Por exemplo, log₂(2)=1 e log₂(4)=2, enquanto log_(1/2)(2)=−1 e log_(1/2)(4)=−2. Esse sentido será essencial nas inequações.

## Mudança de base mantém o mesmo expoente procurado

Se y=log_b(x), então bʸ=x. Aplicando logaritmo em outra base c válida, y log_c(b)=log_c(x); podemos dividir porque b≠1. Portanto log_b(x)=log_c(x)/log_c(b). Podemos usar ln, o logaritmo natural, ou a base 10. A razão não é x/b. Por exemplo, log₄(64)=log₂(64)/log₂(4)=6/2=3.

log_b(x)=ln(x)/ln(b)

## O domínio deve acompanhar cada transformação

Na expressão log₂(x−1)+log₂(x+1), cada argumento precisa ser positivo: x−1>0 e x+1>0, logo x>1. Juntar os termos em log₂(x²−1) só é equivalente nesse domínio original. O logaritmo do produto, sozinho, também estaria definido para x<−1, mas os dois logaritmos separados não. Em uma composição como log₂(log₃(x)), além de x>0 é necessário log₃(x)>0; como a base 3 é crescente, isso exige x>1.

## Exemplo resolvido: a álgebra pode gerar um candidato inválido

Resolva log₂(x−1)+log₂(x+1)=3. Primeiro x>1. Dentro desse domínio, a regra do produto dá log₂(x²−1)=3; pela definição, x²−1=2³=8. Assim x²=9 gera candidatos x=−3 e x=3. A restrição elimina −3. Conferindo 3 na equação original: log₂(2)+log₂(4)=1+2=3. Concluir apenas x=±3 esqueceria as condições que permitiram juntar os logaritmos.

## Em uma base decrescente, a desigualdade inverte o sentido

Considere log_(1/2)(x)>2. O domínio exige x>0. Como a função é decrescente e log_(1/2)(1/4)=2, valores menores que 1/4 produzem logaritmos maiores que 2. A solução é 0<x<1/4. O ponto 1/4 fica fora porque a desigualdade é estrita. Por conferência, x=1/8 produz 3 e satisfaz; x=1/2 produz 1 e não satisfaz.

## Aplicações e código devem preservar a referência

Se uma quantidade positiva passa de Q₀ para Q=8Q₀ em um modelo de duplicações, Q/Q₀=2ⁿ fornece n=log₂(8)=3. O argumento é a razão sem dimensão Q/Q₀. Em Python, log usa uma convenção de base e cálculo aproximado que deve ser conferida; o laboratório desta aula verifica expoentes inteiros por potências racionais exatas e trata a equação do exemplo pelo domínio. Ele não calcula todo logaritmo real nem substitui uma demonstração. Os dados e exercícios são próprios, preparados para sua revisão.

## Exercícios e resoluções

- Quanto é log₂(8)? **Resolução:** Procure o expoente y com 2ʸ=8. Como 2³=8, a resposta é 3.
- log(u+v)=log u+log v é uma identidade geral? **Resolução:** A regra é para produtos.
- Quanto é log₂(1/4)? **Resolução:** 2⁻²=1/4.
- Quanto é log_(1/2)(4)? **Resolução:** (1/2)⁻²=4.
- Quanto é log₂(8×4)? **Resolução:** log₂(8)+log₂(4)=3+2=5.
- Quanto é log₃(81/3)? **Resolução:** 4−1=3, pois 81/3=27=3³.
- Quanto é log₄(64)? **Resolução:** Em base 2, a razão é 6/2=3.
- Qual solução real de log₂(x−1)+log₂(x+1)=3 pertence ao domínio original? **Resolução:** Os candidatos são ±3; x>1 mantém somente 3.
- Resolva log₂(log₃(x))=1. Qual x? **Resolução:** log₃(x)=2, portanto x=3²=9; o argumento externo é 2>0.
- Se Q/Q₀=8=2ⁿ, quantas duplicações n ocorreram? **Resolução:** 2³=8; n=3.
- Qual o domínio de log₂(x−1)+log₂(x+1)? **Resolução:** Cada argumento separado deve ser positivo. A interseção das duas restrições é x>1.
- Qual a solução de log_(1/2)(x)>2? **Resolução:** O domínio é x>0 e a base entre 0 e 1 torna a função decrescente.

## Referências e código

Consulta parcial, 22/10/2026, Jay Abramson, College Algebra 2e (OpenStax, 2021): [§6.3](https://openstax.org/books/college-algebra-2e/pages/6-3-logarithmic-functions), [§6.4](https://openstax.org/books/college-algebra-2e/pages/6-4-graphs-of-logarithmic-functions), [§6.5](https://openstax.org/books/college-algebra-2e/pages/6-5-logarithmic-properties), [§6.6](https://openstax.org/books/college-algebra-2e/pages/6-6-exponential-and-logarithmic-equations). Ideias matemáticas usadas como referência para texto, exemplos, figura e exercícios próprios, sem reprodução do conteúdo do livro. Consulta HTML sem correspondência de páginas impressas verificada.

Na raiz: `python3 -m unittest discover -s labs/logaritmos -t .` e `python3 -m labs.logaritmos.exact`. Só biblioteca padrão. matches_integer_log confere uma proposta com expoente int por potência racional; não encontra todos os logaritmos reais. Rejeita base/argumento inválidos e bool/float/texto. equation_candidate verifica somente a equação específica do exemplo: candidato racional fora do domínio retorna False. Testes combinam potências exatas, comparação aproximada independente e os limites de domínio. Não inferem habilidade pessoal.

Aula em rascunho assistido por IA, aprofundada de três para 12 seções e de dois para 12 exercícios, preservando IDs antigos e corrigindo o enunciado numérico ambíguo. Próxima revisão pessoal: resolver sem calculadora e justificar domínio/base antes da álgebra. Provas de construção das funções reais e inversas trigonométricas pertencem ao nível de Cálculo e continuam pendentes; não se marcou a lacuna de CCM0113 como coberta por esta aula escolar.

Verificação: cinco testes do laboratório aprovados (85 propostas de expoentes inteiros com comparação independente por log aproximado, 81 pares de expoentes para propriedades, domínio, base decrescente e contratos). Falha inicial de descoberta por ausência de __init__.py corrigida; execução posterior aprovada. Treze testes de catálogo e 561 estruturas MathML aprovados. Navegador a 390 px: largura do documento 375 px, figura legível, exercício da equação rejeitou −3 e aceitou 3; console sem erros observados. Prévia logaritmos-dominio-mobile.jpg. Catálogo: 507 aulas/3251 exercícios, 258 aulas com até três seções; relatório de cobertura recalculado. Não houve revalidação global dos demais laboratórios ou revisão pessoal de domínio. Saldo semanal após bloco: 90%; parada em 65%. Próxima ação pessoal: resolver a equação e a inequação sem calculadora, justificando domínio e monotonicidade. Próximo conteúdo deste percurso: trigonometria com círculo e radianos; a lacuna de funções especiais de Cálculo I exige abordagem própria posterior.
