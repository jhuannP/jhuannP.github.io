# Superposição coerente e mistura no poço

27/10/2026. Notas de aula originais assistidas por IA, em rascunho para revisão pessoal. Modelo ideal, sem experimento ou resultado de pesquisa pessoal.

Poço infinito0<x<L, duas autofunções ortonormais n1/n2, E₂=4E₁. No painel existente, u=x/L, τ=E₁t/ℏ e coeficientes iniciais reais positivos√w e√(1−w). A densidade em u é adimensional e a densidade física em x é dividida por L. Densidade local pode exceder1; probabilidade de intervalo exige integral.

A amplitude complexa tem fases e^(−iτ) e e^(−4iτ). O módulo ao quadrado fornece o termo cruzado2√[w(1−w)]ϕ₁ϕ₂cos3τ. Sua integral global zera por ortogonalidade, mas na metade esquerda a integral deϕ₁ϕ₂ vale4/(3π). Assim P_esq=1/2+2√[w(1−w)]4/(3π)cos3τ. Para pesos iguais,0,924413 emτ0 e0,075587 emτπ/3; a mistura dos mesmos níveis permanece1/2. Energia média(4−3w)E₁ é constante em ambos, sem criar nível intermediário. A fase global não altera medições; a relativa muda a interferência. Média uniforme de fase remove o termo cruzado neste modelo, sem simular um mecanismo de decoerência.

O desafio original é uma soma de amplitudes locais iguais sem função de onda espacial normalizada; seu valor2 não é probabilidade pontual. O painel tem passo temporal0,1 e não atingeπ/3 exatamente. A figura e o laboratório avaliam o parâmetro matemático, não alegam que o painel tenha esse valor exato. Nenhum código do painel foi modificado.

## Fontes parcialmente consultadas

Nussenzveig, Curso de Física Básica vol.4, 2ª ed.: §8.2 p.237/PDF238, amplitudes e Born; §8.7 p.249/PDF250, base ortonormal e superposição, consulta textual parcial em27/10/2026. PDF contado a partir de1; OCR imperfeito, sem nova inspeção visual ou leitura integral. [OpenStax University Physics vol.3 §7.4](https://openstax.org/books/university-physics-volume-3/pages/7-4-the-quantum-particle-in-a-box), poço, normalização, níveis e estados estacionários, consulta parcial. Comparação coerência/mistura e cálculos desta aula elaborados separadamente; não apresentados como exemplo transcrito dos autores. Livros privados não distribuídos. Júpiter não reaberto; limites curriculares registrados em FISICA_4.md preservados.

## Verificação reproduzível

Execute `python3 labs/superposicao-coerencia/superposition.py`. Quatro testes:2525 comparações de amplitude complexa versus expansão real;25 casos de normalização, probabilidade esquerda integrada por Simpson versus expressão analítica e energia esperada por ação diagonal de H;18 casos de fase global/média sobre16 fases e limites estacionários, mais fronteiras;contratos. Integrais usam256 subintervalos e tolerância; normalização geral vem da ortogonalidade, não dos testes finitos. Não há solução numérica de Schrödinger com potenciais gerais, medidor ou ambiente.

Próxima ação de20min: obter o termo cruzado, integrar4/(3π) e explicar energia média constante com densidade variável. Potenciais finitos, medição, decoerência dinâmica e revisão pessoal permanecem pendentes. Python opcional.
