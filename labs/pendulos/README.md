# Pêndulos — notas originais em elaboração

16/10/2026. Revisão pessoal de Jhuann pendente.

## O modelo precisa de vínculo e gravidade

No pêndulo simples, uma massa pontual m fica a uma distância fixa L de um pivô imóvel, sob gravidade uniforme g. Desprezamos resistência e massa do vínculo. O ângulo θ é medido a partir da vertical para baixo, em radianos. Para grandes amplitudes, considere haste rígida leve; um fio pode perder tensão e deixar de impor a trajetória circular.

## A força tangencial fornece a equação exata

A componente tangencial do peso é −mg sinθ. Como a aceleração tangencial é Lθ″, a segunda lei dá mLθ″=−mg sinθ. Cancelando m, obtemos θ″+(g/L)sinθ=0. A tensão não entra na equação tangencial, mas é necessária ao vínculo radial. Esta equação é não linear.

## Linearizar é substituir uma função, não trocar unidades

Perto de zero, sinθ=θ+O(θ³), em radianos. A equação aproximada é θ″+ω₀²θ=0, com ω₀²=g/L. Para soltura do repouso em θ₀, a solução linear é θ≈θ₀cos(ω₀t). Uma função cosseno não é solução exata da equação com seno para amplitude finita.

## O período linear é um limite de pequenas oscilações

A solução linear tem T₀=2π√(L/g), independente de m e de θ₀ dentro dessa aproximação. Dobrar L multiplica T₀ por √2; quadruplicar L dobra T₀. Se θ₀=0 e a velocidade inicial é zero, o corpo está em equilíbrio e não há ciclos observados: T₀ é então o período limite de perturbações.

## A energia conserva a não linearidade

Para soltura em θ₀ com velocidade zero, E=mL²θ̇²/2+mgL(1−cosθ)=mgL(1−cosθ₀). Logo θ̇²=(2g/L)(cosθ−cosθ₀). A energia permite calcular o tempo sem supor uma trajetória harmônica. Oscilações de libragem exigem 0<θ₀<π no modelo de haste; rotações são outro regime.

## O período exato vira uma integral regular

Um quarto de ciclo vai do equilíbrio ao extremo. Integrando dt=dθ/|θ̇| e usando sin(θ/2)=sin(θ₀/2)sin u, resulta T=4√(L/g)∫₀^{π/2}[1−k²sin²u]⁻¹/²du, com k=sin(θ₀/2). A substituição remove a singularidade integrável do extremo original. A integral é K(k); o cálculo numérico tem erro de arredondamento.

## Medir o erro exige declarar o denominador

A razão R=T/T₀=2K(k)/π é maior que 1 para amplitude positiva. Nesta aula mostramos o excesso relativo ao período linear, 100(R−1)%. Isso difere da subestimação relativa ao período exato, 100(1−1/R)%. A 90°, R≈1,18034: o excesso é cerca de 18,03%, e a subestimação é cerca de 15,28%.

## Pequeno deve ser julgado pela tolerância

A expansão inicial é T/T₀=1+θ₀²/16+O(θ₀⁴). A 10°, o excesso é aproximadamente 0,19%; a 30°, aproximadamente 1,74%. Não existe um corte universal de ângulo pequeno: a tolerância do problema decide se T₀ basta. A expansão inicial não controla sozinha o erro em amplitudes grandes.

## Um corpo extenso exige momento de inércia

No pêndulo físico, um corpo rígido gira em torno de eixo fixo horizontal sem atrito, com centro de massa a distância d>0 do eixo e momento I em torno desse mesmo eixo. O torque é −mgd sinθ e Iθ″=−mgd sinθ. O comprimento equivalente é ℓ=I/(md), não necessariamente o comprimento geométrico. Use I do eixo de suspensão, não I do centro de massa sem translação.

## Uma haste uniforme não equivale a massa na extremidade

Para haste uniforme de comprimento a presa numa ponta, I=ma²/3 e d=a/2. Portanto ℓ=2a/3 e T₀=2π√(2a/(3g)). A correção não linear é o mesmo fator R(θ₀), pois a equação tem a forma θ″+(g/ℓ)sinθ=0. Massa cancela se a distribuição relativa é mantida.

## Experimento e fronteira do modelo

Meça o tempo de vários ciclos, divida pelo número de ciclos e repita para amplitudes distintas. Registre incerteza de tempo, comprimento, ponto de suspensão e amplitude; evite afirmar conservação se o amortecimento for perceptível. O gráfico compara períodos de movimentos diferentes, não trajetórias nem dados medidos. Em θ₀→π, T cresce sem limite; a configuração exatamente invertida em repouso é equilíbrio instável e não oscilação periódica. Fio flexível, amortecimento e pivô móvel exigem outro modelo.

## Resoluções

Para L=1 m e g=10 m/s², qual ω₀² em s⁻²?

ω₀²=g/L=10 s⁻².

Se L passa de 1 para 4 m, por qual fator o período linear é multiplicado?

T₀ é proporcional a √L; √4=2.

Para haste de 1,5 m presa numa ponta, qual o comprimento equivalente em metros?

ℓ=2a/3=1 m.

Com I=1,5 kg m², m=2 kg e d=0,75 m, qual ℓ em metros?

I/(md)=1,5/(2×0,75)=1 m.

Se T/T₀=1,18, qual o excesso percentual relativo a T₀?

100×(1,18−1)=18%.

A expressão θ₀cos(ω₀t) é exata para qualquer amplitude do pêndulo com seno?

É solução do modelo linearizado, não da equação não linear em amplitude finita.

No pêndulo físico, qual momento de inércia entra na equação?

O torque e a aceleração angular são escritos em torno do mesmo eixo fixo.

Com amplitude zero e repouso inicial, o corpo completa ciclos?

Ele permanece em equilíbrio; o período exibido é um limite de pequenas perturbações.

Excesso de 18% relativo a T₀ significa subestimação de 18% relativa a T?

Os denominadores diferem: subestimação relativa a T é 1−1/R.

## Roteiro de aula e evidência

Antes: forças, torque, momento de inércia, energia e equações diferenciais elementares. Derivar primeiro o modelo e obter o período linear; depois comparar amplitudes com tolerância declarada. Pedir ao aluno que explique por que massa, amplitude e distribuição de massa têm papéis diferentes. Produto de compreensão: resolução comentada de uma haste e um relatório próprio de tempo de ciclos, com incerteza. Nenhum experimento real foi executado aqui.

## Método numérico e fontes

A integral do período foi obtida acima por energia e substituição. O código usa a média aritmético-geométrica: a←(a+b)/2 e b←√(ab), atualizados simultaneamente, começando por 1 e cos(θ₀/2). A razão T/T₀ é o inverso do limite. A identidade está em [NIST DLMF 19.8.5](https://dlmf.nist.gov/19.8.E5); a definição de K usa módulo k, não parâmetro k²: [DLMF 19.2](https://dlmf.nist.gov/19.2). Fontes consultadas em 16/10/2026.

Escopo curricular: [CCM0122](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0122), versão ativada em 2025, posterior à turma. Material próprio, sem copiar livro. Nussenzveig II e Feynman I estão identificados no acervo; nenhum PDF é disponibilizado.

Teste independente: quadratura de Simpson na integral regularizada, além de escalas, limite de amplitude, haste e contratos. A fórmula do modelo é exata sob hipóteses, mas seus valores calculados são aproximações numéricas. A prova da identidade AGM, integração temporal com controle de erro, perda de tensão de um fio e amortecimento ficam para aprofundamento.
