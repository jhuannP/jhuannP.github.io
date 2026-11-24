# Resistência, fonte e faixa de validade

Material original em rascunho. Unidades SI: resistência em Ω, resistividade em Ω·m, comprimento em m, área em m², potência em W e elevação de temperatura Δ em K. O código pode ser executado com `python3 resistor.py`, sem dependências adicionais.

## Duas perguntas que exigem fontes diferentes

A tensão fixa dá P=V²/R. A corrente fixa dá P=I²R. Ao dobrar R, a primeira potência cai à metade e a segunda dobra. Isso compara estados ideais; não é experimento ou recomendação de montagem.

No fio uniforme, J=σE, I=JA e V=Eℓ implicam R=ρℓ/A, com ρ=1/σ. A área de 1 mm² é 10⁻⁶ m². O exemplo sintético ρ=1,5×10⁻⁸ Ω·m, ℓ=2 m e A=1 mm² produz 0,030 Ω.

## Fechar um balanço térmico

Um corpo a temperatura uniforme troca calor com ambiente fixo. R=R₀(1+αΔ), perda GΔ, capacidade térmica positiva Cₜₕ. Na tensão fixa:

Cₜₕ Δ′ = V²/[R₀(1+αΔ)] − GΔ.

R₀>0, G>0 e α≥0. Para o exemplo R₀=10 Ω, α=0,01 K⁻¹, G=0,2 W/K e V=10 V, a raiz é 36,602540 K, com R=13,660254 Ω e P=7,320508 W. A faixa **0≤Δ≤60 K** é adotada por hipótese didática, sem validação para material ou equipamento. A derivada negativa do balanço, dividida por Cₜₕ>0, dá retorno local; não calculamos uma trajetória temporal neste laboratório.

Sob corrente fixa, Cₜₕ Δ′=I²R₀+(I²R₀α−G)Δ. Com I=0,5 A, a raiz 100/7 K é estável e está na faixa. I=1 A tem raiz formal 100 K: fora da faixa, portanto não é uma previsão aceita aqui. I=2 A não tem raiz não negativa na lei linear; ela prevê crescimento sem autorizar extrapolação indefinida. No limiar de coeficiente linear nulo, o termo constante ainda positivo também impede equilíbrio. O código separa esses casos.

A raiz algébrica de tensão é escrita sem cancelamento: seja b=V²/(R₀G); então Δ*=2b/[1+√(1+4αb)]. Ela pode ficar fora da faixa. A bisseção só usa o intervalo declarado e retorna `None` quando não encontra raiz ali, sem afirmar inexistência em todo o domínio. Entradas são magnitudes não negativas de tensão/corrente neste modelo; as identidades elétricas também são testadas com referências de sinal.

## Fontes consultadas parcialmente em 27/10/2026

- Nussenzveig, Curso de Física Básica, vol.3, 2ª edição revista e ampliada, Blucher2015 (digital2018), §6.3 pp.105–106/PDF106–107: lei local, geometria, unidades e coeficiente de temperatura. Reconferência textual, sem nova inspeção visual ou leitura integral. Exemplar privado não distribuído.
- [OpenStax, University Physics vol.2, §9.3](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance): resistência, resistividade e temperatura, leitura parcial.
- [OpenStax, §9.5](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power): potência e energia, leitura parcial.
- [Júpiter CCM0212](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212): programa reaberto, ativação15/07/2025. A data não prova a versão efetivamente ministrada. Circuitos são apoio editorial ao programa, sem inventar um item oficial autônomo.

Balanço térmico, números, figura, deduções, exercícios e código são próprios. Não se atribui o modelo térmico a esses recortes dos livros. São deixados de fora dependência de frequência, mecanismos microscópicos, anisotropia, contatos, fontes reais, variação geométrica, medições e validação experimental.

## Verificação

Cinco testes locais: geometria/unidades/potências por Fraction; 108 configurações de equilíbrio de tensão comparando fórmula e bisseção, inclusive raízes fora da faixa e α=0; distinção de retorno térmico, raiz fora da faixa e ausência de raiz não negativa em corrente fixa; exemplo e contratos. Verificações float usam tolerâncias explícitas; não garantem precisão para parâmetros arbitrariamente grandes ou uma previsão física real. Revisão pessoal pendente.
