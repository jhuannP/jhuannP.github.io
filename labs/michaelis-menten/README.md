# Michaelis–Menten e formação do complexo ES

Rascunho original para revisão de Jhuann. Parâmetros sintéticos; nenhum ensaio de bancada ou resultado da IC atribuído a ele.

## Fontes consultadas em 16/10/2026

- Nelson/Cox, Princípios de Bioquímica de Lehninger, sexta edição, Artmed 2014: sumário PDF 19 e trechos de 6.3, páginas impressas 202–204 (PDF 232–234). Fase pré-estacionária, equação, KM/Kd e parâmetros. Leitura parcial; sem capítulo integral, figura ou exercício reproduzido.
- [IUPAC — mecanismo, M03893](https://goldbook.iupac.org/terms/view/M03893) e [cinética, M03892](https://goldbook.iupac.org/terms/view/M03892): definições consultadas por resultados indexados; abertura direta retornou 403. Não se afirmou leitura integral da página.

Texto, exemplos, parâmetros, gráficos, exercícios e solução de reservatório próprios. Nenhum PDF privado servido. A hipérbole não identifica sozinha um mecanismo real.

## Mecanismo e unidades

E+S ⇌ ES → E+P, com k1=1 μM⁻¹s⁻¹, k−1=1 s⁻¹ e kcat variável em s⁻¹. Eₜ e S em μM; v em μM/s. KM=(k−1+kcat)/k1, Kd=k−1/k1, Vmax=kcatEₜ. Ocupação estacionária S/(KM+S). KM≈Kd apenas no limite kcat≪k−1 neste mecanismo.

O substrato livre é mantido por reservatório, sem consumo líquido que altere S. A enzima total é conservada, mas não o inventário de substrato de um frasco fechado. Com ES(0)=P(0)=0, λ=k1S+k−1+kcat e τ=λt:

- ES(t)=ES∞(1−exp(−τ)); ES∞=EₜS/(KM+S).
- v(t)=kcatES(t); v∞=Vmax S/(KM+S).
- P(t)=(v∞/λ)(τ−1+exp(−τ)). A implementação evita cancelamento perto de τ=0.

Esse transiente é exato no sistema aberto definido; não valida a aproximação de um ensaio fechado. Produto continua acumulando mesmo quando ES se aproxima do estacionário. v₀ usual é medido após a fase rápida e antes de alterações importantes, não necessariamente no instante matemático zero.

## Verificação

Na raiz: `python3 -m unittest discover -s labs/michaelis-menten -t .`.

Quatro testes: conservação de enzima, fluxo estacionário e limites em 144 configurações; derivadas centradas de ES/P contra EDO e taxa em 54 casos; 27 referências Decimal de 70 dígitos, incluindo τ=1e−8; parâmetros distintos e domínio. `reference.json` contém 81 configurações JS/Python. Comparação entre linguagens não substitui balanços, solução analítica ou análise de hipóteses.

Duas vistas: saturação normalizada com comparação que usa Kd, e formação temporal normalizada com platô estacionário. Normalizar por Vmax retira o fator Eₜ: conferir velocidades absolutas na tabela. Alterar kcat também muda KM. O painel não ajusta dados nem mede afinidade de uma proteína.

## Pendências

A primeira comparação de mistura fechada e depleção/sequestro está disponível no [laboratório seguinte](../enzima-fechada/README.md), limitada a três presets. Reação inversa, inibição e cooperatividade, mecanismos específicos, vários substratos, pH/temperatura, ajuste e incerteza continuam pendentes. Biologia I continua parcial e aguarda revisão pessoal.
