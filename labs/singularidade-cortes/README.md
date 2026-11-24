# Singularidades, cortes e valor principal

27/10/2026. Notas originais com apoio de IA em rascunho, revisão pessoal pendente. Convenções de limite são parte da pergunta.

## Definições e contas

Integral usual em (0,1]: limite finito de ∫ε¹f ao fazer ε→0⁺. Para x^(−p), p≠1, corte=(1−ε^(1−p))/(1−p); converge se p<1. Para p=1, −ln ε diverge. No infinito a condição é p>1; nenhum p resolve simultaneamente ∫₀∞x^(−p).

Para p=1/2: total 2, corte 2−2√ε, parcela omitida 2√ε. Erro≤τ se ε≤τ²/4. Com τ=1/100, ε≤1/40000; na grade ε=1/4ᵏ, menor k=8, ε=1/65536, erro=1/128. Corte e quadratura/arredondamento são erros diferentes.

Interior: ∫₋₁^(−εL)dx/x=ln εL→−∞, ∫εR¹dx/x=−ln εR→+∞. Integral usual exige ambos finitos; não admite cancelar infinitos. Soma truncada=ln(εL/εR). Razão 1 dá 0 (PV simétrico definido aqui); razão 2 dá ln 2; εL=εR² dá ln εR→−∞. Caminho com cancelamento não demonstra limite independente.

Para 1/x², corte simétrico 2(1/ε−1) diverge, sem PV finito. Para |x|^(−p),0<p<1, usual=2/(1−p); versão ímpar sign(x)|x|^(−p) tem usual zero no mesmo regime, mas só cancelamento simétrico quando p≥1. Redefinir o valor no ponto não muda integrais truncadas ou corrige divergência.

## Fonte e escopo

Apostol I, 2ª ed./1967, §10.23 pp.418–419/PDF438–439, consulta parcial em 27/10/2026. P.419/PDF439 inspecionada visualmente: potências e separação de integrais de segunda espécie. PV não é atribuído a esse trecho: o protocolo e cortes assimétricos são definidos/deduzidos nas notas. Tolerâncias, exemplos, figura e exercícios próprios. PDF privado não distribuído; Júpiter não reaberto neste bloco.

## Código e verificações

`cuts.py` aceita int/Fraction, sem bool/float para cortes/tolerâncias. `power_cut(k,degree)` usa p=1−1/degree, degree=2 ou3, k=0..256: ε=2^(−degree*k), total=degree, cauda=degree/2ᵏ. `choose_cut` escolhe primeiro k com erro≤tolerância, rejeitando metas fora do intervalo implementado. `signed_cut` devolve lados e soma via razão exata dos cortes; logaritmos são float, não valores racionais exatos ou certificados intervalares. Não decide convergência por experimentar cortes nem implementa quadratura geral.

Da raiz: `python3 -m unittest discover -s labs/singularidade-cortes -t .`. Cinco testes: transformação x=u^degree para remover singularidade/confirmar cortes, seleção/mínimo de k, caminhos simétricos e assimétricos, logaritmos contra Decimal de 60 dígitos e contratos. Evidência finita complementa as deduções; não cobre singularidades oscilatórias ou distribuições generalizadas.

Preservados exemplo 1/√x, IDs iniciais, Python e desafio. Dez novas respostas:1/2;3/2;1/40000;k8;ln 2;4; condições incompatíveis; sem PV finito para 1/x²; redefinir ponto não resolve; um caminho não basta. Resoluções na aula.

Revisão proposta em duas sessões: critério/tolerância; depois limites laterais e caminhos. Pendentes: singularidades mais amplas, critérios gerais, notas pessoais e revisão conceitual.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 766 fórmulas MathML conferidas. Em 390 px, razão de cortes 2 rejeitou 0 e aceitou ln 2 pelo Enter; dependência do caminho aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
