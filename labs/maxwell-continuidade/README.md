# Maxwell e continuidade de carga

27/10/2026. Notas de aula originais assistidas por IA, em rascunho para revisão pessoal. A aula não certifica domínio nem conclusão de Física III.

A aula `f3-maxwell` mantém o exemplo local ∂ρ/∂t=2 e ∇·J=−2, agora com unidades explícitas. Distingue taxa de densidade de taxa de carga total, fluxo fechado de circulação, normal externa de orientação da borda. O cancelamento de derivadas mistas dá div curl=0; Ampère–Maxwell mais Gauss elétrico fornecem continuidade. A conservação não determina unicamente todas as equações.

No capacitor ideal quase estático, E=Q/(ε₀A) e I_D=ε₀d(EA)/dt=dQ/dt=I. Essa igualdade não é transporte de elétrons pelo vácuo. Para superfícies com a mesma borda, compare a soma de condução e deslocamento. A figura é um esquema dos termos dominantes, não uma geometria completa ou solução exata. A razão de B para placas circulares despreza borda e propagação; perto da borda e fora da placa essa idealização precisa cuidado, explicitado na aula. Corrente zero torna B/B(R) indefinida (0/0), e o código retorna None para essa razão, embora I_D=0 seja válido.

## Fontes e alcance

Nussenzveig, Curso de Física Básica vol.3, 2ª ed., exemplar do acervo: §12.2 pp.246–248/PDF247–249, consulta textual parcial em 27/10/2026. Equações, corrente de deslocamento e consistência com conservação. OCR tem imperfeições; não transferimos números ou unidades ambíguos de exemplos do texto. Sem nova inspeção visual ou leitura integral. Páginas PDF contadas a partir de1.

[OpenStax University Physics vol.2 §16.1](https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves), correção de Ampère, superfícies no capacitor e formas integrais, consulta parcial em27/10/2026. Exemplos, figura, exercícios e código próprios; sem transcrever exercícios ou distribuir livros privados. Júpiter não reaberto neste bloco; limite curricular de FISICA_3.md preservado.

## Conferência reproduzível

Execute `python3 labs/maxwell-continuidade/continuity.py`. Quatro testes, frações exatas. Fluxo de J pelas seis faces de um cubo, com normais explicitamente assinadas, versus derivada da carga volumétrica em162 combinações de coeficientes, tempos e semilados. Modelo local E=ρr/(3ε₀), J=−ρ′r/3, B=0: cancelamento de corrente total em162 casos de pontos, taxas e permissividades positivas; divergências por derivadas explícitas. Esse modelo satisfaz Maxwell com as fontes declaradas em uma região; não representa dispositivo isolado ou valida origem/transporte físico dessas fontes.

Capacitor:36 combinações de corrente orientada, raio da placa e razão radial; geometria de área versus lei de circulação normalizada, limite no eixo, igualdade no raio da placa e corrente nula. Contratos rejeitam dimensões geométricas inválidas, float e booleanos. Números e contagens são verificações locais, não demonstração do teorema geral ou simulação de campos em meios materiais.

Próxima ação de20min: obter a continuidade, explicar −2 e −16 com unidades diferentes e reconstruir I_D=I. Ondas, energia, condições materiais, singularidades de superfície e revisão pessoal permanecem pendentes. Python é opcional para estudar a teoria.
