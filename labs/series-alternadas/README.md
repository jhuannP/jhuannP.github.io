# Séries alternadas — prova, faixa e tolerância

27/10/2026. Notas de aula originais com apoio de IA, em rascunho; revisão pessoal de Jhuann pendente. Aprofundamento de `c 2-alternadas`, preservando exemplo de nove termos, exercícios anteriores, Python e desafio iniciais, painel `alternatingBounds` e controle N. Não demonstra domínio pessoal ou conclusão do curso.

## Fontes e contexto

Apostol, *Calculus*, volumeI, segunda edição 1967, exemplar privado autorizado já identificado. Consulta parcial em 27/10/2026: §10.17 pp.403–405/PDF 423–425; p.404/PDF 424 renderizada e conferida visualmente, teorema 10.14 e sua prova. A fonte apresenta forma estrita; estas notas declaram módulos não crescentes e provam a forma não estrita, com exemplos próprios de igualdade. Não atribuem esses exemplos ao livro, não copiam a figura ou os exercícios e não distribuem o PDF.

Apoio complementar parcial: [OpenStax Calculus 2 §5.5](https://openstax.org/books/calculus-volume-2/pages/5-5-alternating-series), teoremas 5.13–5.14 e convergência condicional. Não houve leitura integral do capítulo. A prova foi reescrita na convenção destas notas; identidade integral e exemplos foram desenvolvidos para a aula.

Vínculo: apoio ao item 2 do programaCCM 0123 no mapa já preparado, sem equivalência administrativa entre a organização “Cálculo 2” e a disciplina formal. Programa de ativação 2025 é posterior à turma 2024/1, cuja versão não foi recuperada. Aprovação reutiliza panorama, sem nova leitura do histórico ou do programa neste bloco. Notas pessoais incompletas no Samsung Notes não foram importadas.

## Modelo e prova

S_N=∑ de n=1 aN de(−1)ⁿ⁻¹bₙ. Suponha bₙ≥bₙ₊₁≥0 e bₙ→0. S₀=0.

S₂ₘ₊₂−S₂ₘ=b₂ₘ₊₁−b₂ₘ₊₂≥0. S₂ₘ₊₃−S₂ₘ₊₁=−b₂ₘ₊₂+b₂ₘ₊₃≤0. As somas pares são não decrescentes e as ímpares não crescentes; todas ficam entre 0 e b₁, e pares ficam abaixo das ímpares. Cada subsequência monótona limitada converge. A diferença consecutiva b₂ₘ₊₁ tende a zero, logo seus limites coincidem. Isso prova a convergência da sequência completa de somas parciais.

O limite S fica entre S_N e S_(N+1), separados por b_(N+1). Assim |S−S_N|≤b_(N+1). Primeiro termo positivo: pares são limites inferiores, ímpares superiores. Se o resto é não zero, tem a orientação do próximo termo; não se afirma sinal estrito em todo caso. Prefixo finito não muda convergência, mas ao aplicar o critério apenas à cauda é preciso manter a soma e a orientação corretas.

### Por que as hipóteses importam

- b_(2 k−1)=1/k e b_(2 k)=1/(2 k): módulos positivos tendem a zero, sem monotonicidade global. Cada par deixa 1/(2 k), e S_(2 m)=H_m/2 diverge. Alternância e limite zero não bastam.
- b_(2 k−1)=b_(2 k)=1/k: módulos não crescentes tendem a zero. S=0, S_(2 k)=0 e S_(2 k−1)=1/k. No índice ímpar, erro=1/k, igual ao próximo módulo. A forma≤ não pode ser convertida automaticamente em<.

Esses exemplos são argumentos por fórmulas válidas para todos os índices, não inferências baseadas em testar trinta ou cem termos.

## Harmônica alternada e identificação de ln 2

Para bₙ=1/n, a monotonicidade é estrita e o limite é zero. A identidade geométrica finita, para N≥0, é

1/(1+x)=∑ de k=0 aN−1 de(−x)ᵏ+(−x)ᴺ/(1+x).

Integrando de 0 a 1, ln 2=S_N+(−1)ᴺ∫₀¹xᴺ/(1+x)dx. A soma integrada é finita; não foi assumida troca de soma infinita com integral. O resto tende a zero e identifica o limite com ln 2. A integral é estritamente positiva e fica estritamente entre 1/[2(N+1)] e 1/(N+1), pois 1/2<1/(1+x)<1 no interior. Assim o sinal do resto e uma estimativa mais forte são demonstrados especificamente para esta série.

Após nove termos, cota=1/10, mantendo o exemplo inicial. Nove é ímpar e S₉>ln 2. Faixas do gráfico são limites determinísticos do modelo, não intervalos estatísticos de confiança.

### Tolerância da cota versus tolerância do erro

- Menor N com 1/(N+1)≤10⁻³:999.
- Menor N com 1/(N+1)<10⁻³:1000.

São mínimos para essas desigualdades da cota, não mínimos necessários do erro real. Na própria harmônica alternada, a identidade integral dá erro estritamente menor que 1/(N+1); por isso 999 também garante erro<10⁻³, embora a cota numérica não estrita exibida seja exatamente 10⁻³. Não dizer que 999 falha na tolerância estrita do erro.

Na série geométrica 1−1/2+1/4−⋯, soma=2/3. S₃=3/4, erro em módulo 1/12, próximo módulo 1/8. Para tolerância 1/10, três termos já dão erro menor; a regra do próximo módulo só certifica a partir de quatro. Uma garantia suficiente não é uma condição necessária.

## Convergência condicional

A soma dos módulos é a harmônica. Blocos de índices 2ᵏ,…,2ᵏ⁺¹−1 contêm 2ᵏ termos, cada um pelo menos 1/2ᵏ⁺¹, portanto cada bloco soma no mínimo 1/2. Há quantos blocos se queira, logo a soma diverge. A série com sinais converge na ordem dada: convergência condicional. Isso não autoriza rearranjos arbitrários; teoria geral ainda pendente.

## Laboratório, painel e limites

`bounds.py` usa Fraction, apenas Python padrão. `harmonic_bounds(N)` retorna soma parcial, faixa e cota para a harmônica; `geometric_bounds(N,r)` para a família de módulos rⁿ⁻¹, com 0<r<1. Não recebem uma sequência arbitrária e não certificam monotonicidade/limite por amostragem. N é inteiro de 0 a 5000, sem bool/float; limite de trabalho não é critério de convergência. Valores 0,1 ou razão negativa são recusados para essa família geométrica.

`harmonic_bound_count(epsilon,strict=False)` aceita int/Fraction positivo, sem float/bool. Retorna o mínimo N≥0 para cota≤epsilon, ou cota<epsilon se strict=True. Pode retornar N maior que 5000; não executa a soma nem ignora o limite. Casos eps>1 e N=0 também são definidos, com cota inicial 1. Não promete mínimo do erro real.

```sh
python3 -m labs.series-alternadas.bounds
python3 -m unittest discover -s labs/series-alternadas -t .
```

Cinco testes selecionados: referência Decimal.ln a 80 dígitos, intervalos exatos aninhados/paridade, família geométrica contra expressão exata, minimalidade para a desigualdade da cota e contratos/orçamento. Também conferem identidades dos dois contraexemplos em prefixos, sem tratar esses testes como prova de todo o caso infinito. Referência de alta precisão é evidência numérica, não prova de arredondamento rigoroso em todas as implementações.

A prova controla truncamento para soma matemática exata. O painel e o Python inicial usam ponto flutuante; a referência math.log/Math.log também é aproximada. O relatório do painel foi renomeado para “erro contra referência numérica”, mantendo cálculo e controles. Uma garantia total em float requer ainda análise de arredondamento e da referência, não realizada aqui.

## Resoluções dos 12 exercícios

1. Cota após nove termos:1/10.
2. Alternância sozinha não basta.
3. Série geométrica: S₃=3/4.
4. Erro em módulo=1/12.
5. Próximo módulo=1/8, distinto do erro.
6. S₈ da harmônica alternada fica abaixo do limite.
7. Mínimo para cota≤10⁻³:999.
8. Mínimo para cota<10⁻³:1000; não é mínimo do erro real.
9. Módulos repetidos permitem igualdade na cota.
10. Termos alternados tendendo a zero sem outra hipótese não bastam.
11. Harmônica alternada tem convergência condicional.
12. Amostra finita não prova monotonicidade ou limite de sequência arbitrária.

Revisão 20 min proposta: reconstruir prova par/ímpar; explicar os exemplos de igualdade e divergência; diferenciar 1/12 de 1/8 e o significado de 999/1000. Dúvidas e avaliação pessoal ainda não preenchidas. Demais critérios, séries de funções, rearranjos e análise completa de arredondamento seguem pendentes; aula e mapa mantêm cobertura parcial.
