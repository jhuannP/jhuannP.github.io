# Ordem de convergência — notas de aula

## Primeiro declare para qual alvo a sequência deve convergir

Uma sequência xₙ converge para α quando |xₙ−α| tende a zero. Defina eₙ=|xₙ−α| usando uma referência α conhecida ou suficientemente precisa. A redução de eₙ descreve a aproximação ao alvo; o número de dígitos que o programa imprime não faz isso por si só. Os exemplos desta aula têm alvos e expressões exatos, escolhidos para estudar o comportamento sem confundir erro da referência com erro das iteradas.

eₙ=|xₙ−α|

## Ordem relaciona dois erros consecutivos em um limite

Suponha convergência para α e erros positivos a partir de certo índice. A ordem p com constante assintótica λ exige eₙ₊₁/eₙᵖ→λ, com 0<λ<∞. Nesta aula tratamos p≥1; quando p=1, a convergência linear exige também λ<1. A condição eₙ→0 faz parte da definição usada: uma lista de quocientes aparentemente constante não substitui a verificação de convergência.

lim eₙ₊₁/eₙᵖ=λ

## Linear: reduzir o erro por uma fração fixa

No modelo exato e₀=1/2 e eₙ₊₁=eₙ/2, uma indução dá eₙ=2⁻⁽ⁿ⁺¹⁾. O erro tende a zero e o quociente eₙ₊₁/eₙ é sempre 1/2: ordem linear, λ=1/2. A palavra linear descreve a relação assintótica entre erros; não significa que xₙ seja uma reta em função de n. Após três atualizações, e₃=1/16.

eₙ=2⁻⁽ⁿ⁺¹⁾; eₙ₊₁/eₙ=1/2

## Quadrática: a nova escala depende do quadrado do erro

Considere e₀=1/2 e eₙ₊₁=eₙ². A indução agora dá eₙ=2^(−2^n), portanto eₙ→0 e eₙ₊₁/eₙ²=1. A ordem é quadrática com λ=1. Não é necessário exigir λ<1 para p>1: o quadrado de um erro suficientemente pequeno já reduz sua escala. Após três atualizações, e₃=1/256. Em contraste, começar com e₀=1 nesse mesmo modelo mantém todos os erros iguais a 1 e não aproxima o alvo zero.

eₙ=2^(−2^n); eₙ₊₁/eₙ²=1

## Comparar ordens não mede automaticamente o custo total

A figura compara dois modelos exatos começando no mesmo erro 1/2. Ambos dão 1/4 no primeiro passo; depois os comportamentos se separam. O quadrático passa de 1/16 para 1/256 enquanto o linear passa de 1/8 para 1/16. São sequências sintéticas, não medições de desempenho de Newton ou de outro método. Uma comparação de algoritmos reais ainda precisa considerar região de convergência, custo por iteração e a precisão exigida.

## Superlinear não implica quadrática

Se eₙ₊₁/eₙ→0, dizemos aqui que a redução é superlinear. Para eₙ=1/(n+1)!, esse quociente é 1/(n+2) e tende a zero. Entretanto, eₙ₊₁/eₙ²=(n+1)!/(n+2) cresce sem limite: a razão entre coeficientes consecutivos é (n+2)²/(n+3), maior que 2 para n≥1. Portanto não há uma constante quadrática finita e positiva. O exemplo prova que verificar apenas a queda da razão de primeira ordem não autoriza declarar ordem 2. Os nomes de comportamento precisam de seus próprios limites.

eₙ=1/(n+1)! ⇒ eₙ₊₁/eₙ=1/(n+2)

## Convergir lentamente ainda é convergir

A sequência eₙ=1/(n+1) tende a zero, embora eₙ₊₁/eₙ=(n+1)/(n+2) tenda a 1. Ela não atende ao critério linear com λ<1; chamamos esse comportamento de sublinear neste exemplo. Uma razão próxima de 1 não prova divergência. É preciso examinar o limite dos erros, e não apenas um número isolado da tabela.

## Diferença entre iteradas não é o erro em relação ao alvo

O passo dₙ=|xₙ₊₁−xₙ| pode ser calculado sem conhecer α. Mas dₙ pequeno não garante eₙ pequeno. Tome xₙ=1+2⁻ⁿ e alvo α=0: dₙ=2⁻⁽ⁿ⁺¹⁾ tende a zero, enquanto eₙ=1+2⁻ⁿ tende a 1. A sequência está se aproximando de 1, não de 0. Um critério de parada baseado em passos precisa de uma justificativa adicional, como uma estimativa de erro válida para o método.

dₙ→0 não implica eₙ→0

## Um prefixo finito não prova o comportamento futuro

É possível observar os seis primeiros termos de um modelo geométrico e depois mantê-los constantes no último valor. Esse prefixo é idêntico ao da sequência que continua dividindo por dois para sempre, mas a continuação congelada não converge para zero. Um experimento finito pode sugerir um regime e detectar violações, mas não provar o limite de uma sequência arbitrária. Uma prova usa estrutura da recorrência ou hipóteses do método.

## A constante depende da escala do erro

Se a nova unidade ou normalização define e′ₙ=c eₙ, com c>0 constante, então e′ₙ₊₁/(e′ₙ)ᵖ=c¹⁻ᵖ eₙ₊₁/eₙᵖ. A ordem permanece p, mas a constante passa a c¹⁻ᵖλ. Para o modelo quadrático de λ=1 e escala c=3, a constante é 1/3. Por isso comparar constantes sem conferir a escala pode confundir. Uma translação simultânea das iteradas e do alvo conserva os erros.

λ′=c^(1−p)λ

## Ordem de malha compara passos diferentes de discretização

Em E(h)=C hᵖ, reduzir h pela metade dá E(h)/E(h/2)=2ᵖ. O exemplo original E(h)=0,04 e E(h/2)=0,01 fornece razão 4 e sugere p=2 sob essa forma de erro. Esse é um experimento de refinamento de malha; não é a mesma definição de ordem entre iteradas sucessivas de um método de raízes. A fórmula observada p=log₂[E(h)/E(h/2)] depende de erros positivos e de conhecer a referência e o regime.

E(h)/E(h/2)=2ᵖ

## Um piso de erro pode esconder a ordem esperada

Modele o erro total sintético como E(h)=h²+ε, com ε=1/1024 constante. Para h=1/32, E(h)=1/512 e E(h/2)=5/4096; a razão é 8/5, não 4. Quando h fica muito menor, ambos os erros se aproximam de ε e a razão tende a 1: a ordem observada por log₂ tende a zero. O termo de discretização continua sendo h²; o piso domina o total. Esse modelo ilustra referência imprecisa, tolerância interna ou outro limite, sem afirmar que todo arredondamento real é constante.

(h²+ε)/(h²/4+ε) → 1 quando h→0 e ε>0

## Erro zero e estagnação exigem tratamento explícito

Se uma iterada coincide exatamente com o alvo, o próximo quociente com denominador eₙ=0 não é definido por esta razão. O laboratório retorna None; não inventa ordem infinita. Em float, iteradas também podem ficar iguais por arredondamento sem acertar a solução real. A aula anterior mostra como a informação pode se perder. Nosso laboratório usa Fraction para estudar modelos exatos; isso não elimina a necessidade de avaliar a precisão da referência numa aplicação real.

## O laboratório mostra diagnósticos, não emite certificados

diagnostics devolve erros, passos e quocientes para uma referência e um expoente inteiro fornecidos. power_errors gera uma recorrência exata, inclusive casos que não convergem; mesh_comparison calcula o modelo C hᵖ+ε. Nenhuma função classifica automaticamente uma sequência como convergente. Os testes conferem fórmulas, escala, prefixos e casos de denominador zero. Newton, secante, referências numéricas e estimadores sem alvo exato precisam das suas hipóteses próprias. Material assistido por IA, com revisão pessoal pendente.

## Exercícios originais e resoluções

Para erro proporcional a h², qual fator reduz o erro ao dividir h por dois? **Resolução:** (h/2)²=h²/4.

Ordem observada em dois passos prova automaticamente uma garantia global? **Resolução:** É preciso conferir hipóteses e o regime em que os valores foram obtidos.

Para e₀=1/2 e eₙ₊₁=eₙ/2, qual e₃? **Resolução:** 1/2→1/4→1/8→1/16.

Para e₀=1/2 e eₙ₊₁=eₙ², qual e₃? **Resolução:** 1/2→1/4→1/16→1/256.

Se e₀=1/2 e e₁=1/4, quanto é e₁/e₀²? **Resolução:** (1/4)/(1/4)=1. Sozinho, um quociente não prova a ordem assintótica.

Para eₙ=1/(n+1)!, qual e₃/e₂? **Resolução:** (1/24)/(1/6)=1/4.

Se x₅=1+2⁻⁵ e o alvo é0, qual o erro e₅? **Resolução:** |1+1/32−0|=33/32. A diferença para a iterada seguinte é outro valor.

Uma sequência quadrática tem λ=1. Se todos os erros são multiplicados por3, qual a nova constante? **Resolução:** c^(1−2)λ=1/3.

Com E(h)=h²+1/1024 e h=1/32, qual a razão E(h)/E(h/2)? **Resolução:** (1/512)/(5/4096)=8/5.

No mesmo modelo com piso positivo fixo, para qual valor tende E(h)/E(h/2) quando h→0? **Resolução:** Numerador e denominador tendem ao mesmo ε>0.

e₀=1 e eₙ₊₁=eₙ² aproximam o alvo zero com ordem quadrática? **Resolução:** Todos os erros são1. O quociente quadrático é1, mas falta a convergência para zero exigida pela definição.

Passos |xₙ₊₁−xₙ|→0, sem outras hipóteses, provam convergência ao alvo desejado? **Resolução:** xₙ=1+2⁻ⁿ tem passos tendendo a zero e converge para1; se o alvo é0, o erro tende a1.

## Fonte e laboratório

Burden, Faires e Burden — Análise Numérica, tradução da10ª edição, edição brasileira2016 do exemplar autorizado.

§2.4, definição2.7, pp.86–87 (PDF100–101), consulta visual parcial em26/10/2026. Não se leu toda a seção. Notação adaptada: α é o alvo e p a ordem. Recorrências, contraexemplos, figura, código e modelo de piso são próprios; ordem de discretização é uma conexão editorial, não transcrição dessas páginas.

`diagnostics(iterates,target,p=1)` recebe lista/tupla de pelo menos duas iteradas int/Fraction e alvo racional; devolve erros, razões e passos. Razão com erro anterior zero é None. `power_errors(e0,factor,p,steps)` também gera casos que não convergem, sem classificá-los. `mesh_comparison(h,p=2,coefficient=1,floor=0)` compara C hᵖ+ε em h e h/2. p inteiro positivo no código; sem bool ou floats.

Executar: `python3 -m unittest discover -s labs/ordem-convergencia -t .`. Testes finitos conferem implementação; limites gerais são justificados no texto. Sem dados de pesquisa ou páginas do livro distribuídas; rascunho assistido por IA para revisão pessoal.
