# Clapeyron: uma curva de coexistência, hipóteses distintas

Notas de aula originais em rascunho. Apoio parcial a fases de QuímicaII, sem atribuir domínio a Jhuann. Pré-requisitos: potencial químico, propriedades molares e derivadas. Parâmetros e gráfico são sintéticos, sem identificar uma substância ou representar dados de pesquisa.

## Da igualdade de potenciais ao declive

Para uma substância pura em duas fases macroscópicas, com interface plana e sem campos externos adicionais, a coexistência satisfaz μ_α(T,p)=μ_β(T,p). Em cada fase, dμ=−S_m dT+V_m dp. Ao longo da linha, as diferenciais também são iguais. Definindo diferenças como faseβ menos faseα:

`ΔV_m dp=ΔS_m dT`, portanto `dp/dT=ΔS_m/ΔV_m` quando ΔV_m≠0.

Como na coexistência ΔG_m=0=ΔH_m−TΔS_m, obtemos Clapeyron:

`dp/dT=ΔH_m/(TΔV_m)`.

T deve ser absoluto positivo. Unidades J/mol divididas por K·m³/mol resultam Pa/K. Inverter a transição muda simultaneamente os sinais de ΔH e ΔV e preserva a razão. ΔG=0 não significa ΔH=0. Um exemplo hipotético ΔH=30000J/mol, ΔV=0,002m³/mol, T=300K dá50000Pa/K. Outro, com ΔH=6000J/mol e ΔV=−2×10⁻⁶m³/mol a300K, dá−10⁷Pa/K. Não são propriedades atribuídas a um material.

## Três aproximações para integrar a pressão de vapor

Na vaporização, escreva L=Δ_vapH_m>0. Primeiro, despreze o volume líquido frente ao vapor: ΔV_m≈V_mg. Segundo, modele o vapor como ideal: V_mg≈RT/p. Assim, d ln(p/p_ref)/dT≈L/(RT²), com p_ref fixo. Terceiro, trate L como constante no intervalo. A integral resulta:

`ln(p₂/p₁)=(L/R)(1/T₁−1/T₂)` dentro desse modelo aproximado.

O logaritmo contém uma razão adimensional; as duas pressões usam a mesma unidade. Não use Celsius nos denominadores. A equação diferencial é uma aproximação da relação geral; a fórmula integrada só acrescenta uma solução exata dessa aproximação com L constante.

Adote R=8,314J/(mol·K), arredondado, L=30000J/mol, T₁=300K e p₁=10000Pa. Para T₂=330K, ln(p₂/p₁)=1,093445885 e p₂=29845,4076Pa. O declive inicial é400,930158Pa/K. Extrapolar a reta tangente por30K daria22027,9047Pa, resultado diferente da curva integrada. O gráfico compara as duas contas com os mesmos parâmetros, sem dados reais.

A inversão é `1/T₂=1/T₁−(R/L)ln(p₂/p₁)`. O lado direito precisa ser positivo; a temperatura resultante deve ficar no intervalo em que o modelo foi assumido. Dobrar a pressão no exemplo dá318,345708K. Relacionar pressão de coexistência à ebulição sob pressão externa exige condições de equilíbrio; não se calcula nucleação, superaquecimento ou taxa de evaporação.

## Extensão separada: L(T) prescrito

Para testar a hipótese de constância, imponha L(T)=L₁+a(T−T₁), mantendo as aproximações gasosas. A integral de L(T)/(RT²) é:

`ln(p/p₁)=[(L₁−aT₁)(1/T₁−1/T)+a ln(T/T₁)]/R`.

Com a=−40J/(mol·K), L(330K)=28800J/mol e p(330K)=29220,0941Pa. O parâmetro a é imposto; não veio de dados. A semelhança com Kirchhoff não permite identificá-lo automaticamente com ΔC_p: ao longo da coexistência a pressão também muda, e a dependência de H com p exige atenção. Aqui há uma função prescrita para a comparação, sem uma identidade calorimétrica exata para uma substância.

## Limites e código

Execute `python3 labs/clapeyron-coexistencia/coexistence.py`. A função Clapeyron recebe grandezas em SI; `pressure` devolve a mesma unidade de p_ref, com padrãoPa. A inversão requer p e p_ref na mesma unidade. O intervalo280–360K é limite didático de implementação, não uma validade universal para materiais. L deve permanecer positivo no segmento de integração usado. O programa rejeita temperaturas fora do intervalo e inversões sem denominador positivo, sem extrapolar silenciosamente.

Seis testes: declives com sinais/unidades; exemplos e tangente; integração independente por RK4 de dp/dT=L(T)p/(RT²) em21 combinações de temperatura e coeficiente; derivadas do logaritmo em nove configurações; inversão/escala; contratos. O RK4 não usa a fórmula fechada nos estágios. Em340K com L constante, os erros para16/32/64 passos foram aproximadamente0,0290/0,00188/0,000120Pa. Essa queda é uma observação numérica, sem limite rigoroso global de erro. As21 comparações com256 passos passaram com tolerância10⁻⁴Pa. Testes de fórmulas não validam o modelo físico de um fluido.

Não há um diagrama completo de estabilidade ou quantidades das fases. Vapor denso, volume líquido relevante, misturas e aproximação do ponto crítico exigem outro tratamento. Se ΔH e ΔV tendem a zero no ponto crítico, a substituição0/0 não determina o declive. A quantidade de fase não vem desta equação; a regra da alavanca é outro problema.

## Fontes consultadas

- [USP — CCM0124 QuímicaII](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124), reaberto em27/10/2026. Item6 de fases; ativação01/01/2025, posterior à turma2024/1 documentada. Não recuperada a versão ministrada.
- Levine, *Physical Chemistry*,6ª ed.,2009: §7.3 pp.214–216/PDF232–234, consulta textual parcial em27/10/2026, com símbolos incompletos na extração. p.215/PDF233 inspecionada visualmente para a derivação, os sinais e as aproximações de volume/vapor. Sem leitura integral do capítulo, reprodução da tabela ou dos exemplos experimentais, ou distribuição do livro/imagens privadas.
- [Howard DeVoe — Thermodynamics and Chemistry, §8.4](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/DeVoes_Thermodynamics_and_Chemistry/08:_Phase_Transitions_and_Equilibria_of_Pure_Substances/8.04:_Coexistence_Curves), consulta parcial em27/10/2026 a§§8.4.2–8.4.3; apoio público complementar à distinção entre relação geral e aproximações. Não se reproduziram as figuras ou dados do autor.

Exposição, números, gráfico, modelo linear prescrito, exercícios e código preparados originalmente para estas notas, com apoio de IA. Não são exercícios atribuídos aos autores ou evidência de formação concluída.

## Próxima revisão — vinte minutos

Derive o declive a partir de μ_α=μ_β; confira sinais e unidades. Liste as três aproximações, refaça29,8454kPa e explique a diferença para a tangente. Depois compare com L(T) prescrito e registre dúvidas, sem apresentar uma curva sintética como validação de substância.
