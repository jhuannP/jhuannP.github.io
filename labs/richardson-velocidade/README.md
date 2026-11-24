# Richardson: o que é cancelado e o que pode ser ampliado

Notas e experimento originais preparados com apoio de IA em 28/10/2026; revisão pessoal de Jhuann pendente. Não são exercício transcrito, dados medidos ou resultado de pesquisa.

## Derivação e hipóteses

Se A(h)=L+Chᵖ+Dhᑫ+o(hᑫ), com q>p>0 e constantes independentes de h, combine R(h)=[2ᵖA(h/2)−A(h)]/(2ᵖ−1). O termo Chᵖ cancela e o próximo coeficiente se torna D(2^(p−q)−1)/(2ᵖ−1). Saber apenas A−L=O(hᵖ) não garante esse cancelamento: falta uma estrutura com coeficiente estável. Nem sempre a ordem seguinte é p+2.

Para diferença central de uma função C⁵ numa vizinhança do ponto, Taylor dá D_c(h)=f′+f‴h²/6+f⁽⁵⁾h⁴/120+o(h⁴). A combinação p=2 produz R=f′−f⁽⁵⁾h⁴/480+o(h⁴). É uma expansão local assintótica, não um limite uniforme de erro calculado a partir de dados quaisquer. C³, suficiente para a cota anterior de ordem dois, não basta para alegar essa expansão de ordem quatro.

## Aplicação física original

s(t)=v₀t+βt³+γt⁵, com v₀=2 m/s, β=1 m/s³ e γ=1 m/s⁵; valores do código em SI. Em t=1 s, v=10 m/s. Expandindo os polinômios, D_c(h)=10+11h²+h⁴ nos valores numéricos SI, e R=10−h⁴/4. Os coeficientes carregam as unidades necessárias.

| h (s) | R(h) (m/s) | R(h)−v (m/s) |
|---:|---:|---:|
| 1/2 | 639/64 = 9,984375 | −1/64 |
| 1/4 | 10239/1024 | −1/1024 |
| 1/8 | 163839/16384 | −1/16384 |

O erro cai por16 a cada metade de h neste polinômio, em aritmética exata. Richardson recupera exatamente a derivada de polinômios de grau até quatro; isso não diz que toda função é um deles nem que todo resultado float será exato.

## Quatro avaliações e perturbação

O mesmo R pode ser escrito com os valores nos pontos x−h, x−h/2, x+h/2, x+h: pesos (1,−8,8,−1)/(6h). Os pesos somam zero para eliminar uma constante. Seus módulos somam 3/h: se cada valor tiver erro limitado por δ, a perturbação no quociente é no máximo 3δ/h. Na diferença central de passo h/2, a cota era 2δ/h. Não compare passos com afastamentos diferentes sem explicitar a escolha.

No quintico, o limite total é γh⁴/4+3δ/h (γ positivo neste exemplo), soma do erro exato de truncamento em módulo e da perturbação. δ=1/4000 m e h=0,05 s dão contribuição dos dados de 0,015 m/s, enquanto o truncamento sem perturbação é apenas 0,0000015625 m/s. A sequência de erros δ,−δ,δ,−δ atinge a cota positiva de perturbação; a sequência oposta soma-se ao erro negativo de truncamento e atinge o limite total em módulo. São casos determinísticos construídos, sem hipótese estatística. Não incluem automaticamente erros adicionais das operações em float.

## Executar

```sh
python3 experiment.py
python3 -m unittest test_experiment.py
```

Somente Python padrão. A referência aceita int/Fraction, rejeitando float/bool; a ordem aceita inteiros 1–20 como limite do laboratório. O código não identifica a ordem a partir dos dados. Quatro testes: 1458 casos polinomiais com derivadas por coeficientes; identidade quíntica e razão16;243 combinações de perturbações e extremos da cota; ordem errada e contratos. O exemplo legado x³ permanece na aula: resultado 3 com p=2; com p=1, dá 23/8, incorreto.

## Fontes e continuidade

Burden/Faires/Burden, *Análise Numérica*, tradução da 10ª edição norte-americana, 3ª brasileira 2016. Inspeção visual parcial de §4.2 em 28/10/2026: p.203 (parte inferior)/PDF217, pp.204–206/PDF218–220; estrutura da expansão, cancelamento, potências pares e recorrência. Não foi lida integralmente a seção nem reproduzida sua tabela/exercício. Edição distinta da 7ª citada em CCM0218; versão ministrada à turma não comprovada. Apoio didático na trilha de Computação III, sem novo tópico inventado na ementa.

Próximo estudo pessoal: deduzir os quatro pesos, reconstruir 639/64 e explicar por que o limite de perturbação é 3δ/h. Antes de extrapolar uma simulação física, verificar se duas malhas representam o mesmo problema, mesmas unidades, condições e observável; limites físicos, erros de modelo e erros estatísticos não somem ao cancelar um termo de malha. Faltam análise geral, estimadores a posteriori, malhas de PDE, dados reais e revisão pessoal. Romberg é uma conexão futura, sem declarar aqui sua tabela completa.
