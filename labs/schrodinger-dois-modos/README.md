# Schrödinger: dois modos no tempo — notas de aula

Rascunho original assistido por IA, revisão pessoal pendente. Não comprova experimento, domínio pessoal ou conclusão da disciplina.

## Modelo e derivação

Partícula sem spin não relativística em0<x<L, V=0 no interior, ψ=0 nas paredes. Modos φₙ=√(2/L)sin(nπx/L), energias Eₙ=n²π²ℏ²/(2mL²). Substituir φₙa(t) na equação temporal dá a'=−iEₙa/ℏ, portanto fase exp(−iEₙt/ℏ). Um modo tem densidade fixa; uma superposição pode ter termos cruzados temporais.

No laboratório s=x/L, τ=E₁t/ℏ e Ψ=√Lψ. Dois coeficientes iniciais iguais1/√2 dão Ψ=sin(πs)e⁻ⁱτ+sin(2πs)e⁻⁴ⁱτ e i∂τΨ=−∂s²Ψ/π². Densidade:sin²πs+sin²2πs+2sinπs sin2πs cos3τ. Integral total1; os cruzados integram zero no domínio inteiro.

Na metade esquerda as diagonais dão1/4 cada. Integral de2sinπs sin2πs entre0e1/2: [sinπs/π−sin3πs/(3π)]₀¹ᐟ²=4/(3π). Assim P_esq=1/2+4cos3τ/(3π). Valores:τ0→0,92441318;π/6→1/2;π/3→0,07558682. Densidade repete após2π/3; função repete a menos de fase globalexp(−2πi/3). Emπ/3 o produto interno com o estado inicial é zero, embora os pesos energéticos permaneçam iguais.

Pesos1/2 nos níveis E₁e4E₁: média5E₁/2, média quadrática17E₁²/2, variância9E₁²/4. Uma medida retorna um dos níveis, não obrigatoriamente a média. Mudar H por H+C produz fase global comum; `shift`=C/E₁ adimensional. Não é mudança local do potencial.

## Conservação local e unidades

ρ=|ψ|² tem unidade1/comprimento. j=(ℏ/m)Im(ψ*∂xψ) tem unidade1/tempo em1D. ∂tρ+∂xj=0; integrar na metade esquerda dá dP_esq/dt=j(0)−j(L/2). Paredes têm corrente zero. No meio j=2πℏ sin3τ/(mL²). Corrente em tempo reduzido J=jℏ/E₁=4sin3τ/π. Logo dP_esq/dτ=−J. A densidade Ψ do laboratório é adimensional e integra em ds, não em dx. Tempo físico t=ℏτ/E₁.

## Preservação e resoluções

Mantidos exemplo, Python, desafio e IDs dos dois exercícios anteriores. Razão de densidades1 apenas onde densidade inicial não nula; zero sobre zero não definido. Superposição de energias diferentes pode variar a densidade. Dez novas respostas:0,92441318;1/2;0,07558682;5/2;9/4;4/π; mudança global não altera densidade; medida de energia retornaE₁ou4E₁; fluxo entre regiões não perde norma; solução fixa não é integrador geral.

## Executar

Na raiz do protótipo:

```sh
python3 -m unittest discover -s labs/schrodinger-dois-modos -t .
```

Seis testes: integração Simpson das amplitudes em25 tempos comparada à norma e à fórmula regional, com refinamento100→1000 subintervalos; módulos e momentos da energia; fase global, shift e recorrência; continuidade por derivada temporal independente; resíduo de Schrödinger por diferenças finitas, reduzindo erro ao refinar; contratos. O resíduo é uma verificação de consistência, não um solucionador de EDP ou análise geral de convergência. Entradas finitas, sem bool;0≤s≤1. Valores extremos de fase em float não têm garantia de precisão arbitrária.

## Fontes e limites

Programa CCM0222, item28: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0222 . Reaberto27/10/2026, ativação01/01/2025, versão da turma2026/1 não comprovada.

Nussenzveig, Curso de Física Básica, vol.4, segunda edição2014, reimpressão2017/digital2018 conforme metadados previamente conferidos. Consulta parcial27/10: §9.1 pp.271–273/PDF272–274, §9.6 pp.280–281/PDF281–282; pp.273/281 inspecionadas visualmente para equação e sinal de corrente. §10.3 pp.298–299/PDF299–300 lido parcialmente para fronteiras: o livro usa caixa centrada; aqui coordenadas transladadas para0<x<L e modos/exemplo derivados nas notas. Extração omite fórmulas em alguns trechos, por isso equação e corrente foram conferidas nas imagens. Sem leitura integral de capítulos, reprodução de exercícios, figuras ou distribuição do PDF privado.

Feynman/Caltech, III§7–1: https://www.feynmanlectures.caltech.edu/III_07.html#Ch7-S1 , consulta parcial de fase temporal e deslocamento comum de energia. Não se usou a discussão relativística ou a formulação histórica de incerteza para este recorte. Derivações, números, figura e verificações originais.

Falta evolução com potenciais gerais, Hamiltoniano dependente do tempo, simulação numérica geral, instrumentos de medida e ambiente. Não confundir evolução unitária isolada com redução de estado por medição; o painel de Born anterior continua sem tempo. Diagrama original mostra probabilidades de regiões, não trajetórias.

## Registro pessoal

Data: ____ · derivação reconstruída: ____ · dúvida: ____
