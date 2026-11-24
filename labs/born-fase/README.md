# Born, fase relativa e probabilidades — notas de aula

Rascunho original para revisão pessoal.

## A amplitude pode ser complexa

Para estado normalizado em uma dimensão, densidade ρ=|ψ|². A probabilidade num intervalo é a integral de ρ. Em uma distribuição contínua regular, um ponto isolado tem probabilidade zero, mesmo com densidade não nula.

P(a≤x≤b)=∫_a^b|ψ|²dx

## Normalização contabiliza o espaço inteiro

∫|ψ|²dx=1. Se ψ é constante dentro de [0,L] como exemplo de densidade e zero fora, seu módulo deve ser 1/√L. Esse exemplo com descontinuidades não é apresentado como estado de energia finita de qualquer Hamiltoniano.

|ψ|²=1/L em [0,L]

## Fase global não muda densidade

Multiplicar ψ por exp(iα) preserva |ψ|². Fases relativas entre componentes, porém, podem alterar interferência e outros resultados.

|exp(iα)ψ|²=|ψ|²

## Unidades antes de escolher a amplitude

Se x e L estão em metros, uma densidade de posição ρ tem unidade m⁻¹ e ψ tem unidade m⁻¹ᐟ²: a integral de |ψ|² dx precisa ser adimensional. A altura da densidade não está limitada a 1; quem precisa ficar entre 0 e 1 é a probabilidade integrada sobre uma região. A regra de Born aqui descreve uma medição de posição numa dimensão, num instante fixo.



## Dois modos com normalização conhecida

Defina φ₁(x)=√(2/L) sin(πx/L) e φ₂(x)=√(2/L) sin(2πx/L), para 0≤x≤L, e zero fora. As integrais de sin² em cada modo valem L/2; multiplicar por 2/L dá norma 1. Pela identidade produto–soma, a integral de sin(πx/L) sin(2πx/L) no intervalo é zero. Assim os modos são ortonormais. Usamos suas formas como base ilustrativa, sem resolver aqui o espectro do Hamiltoniano do poço.

∫φ₁² dx=∫φ₂² dx=1; ∫φ₁φ₂ dx=0

## Formar um estado puro com fase relativa

Considere ψ=(φ₁+e^{iφ}φ₂)/√2. Cada modo tem peso de amplitude 1/√2; os pesos quadráticos somam 1 e o termo cruzado integra zero por ortogonalidade. Portanto ψ tem norma 1 para qualquer φ. Mudar φ não significa multiplicar toda a função pelo mesmo fator: muda a fase de uma componente em relação à outra.

ψ=(φ₁+e^{iφ}φ₂)/√2

## O termo cruzado não desaparece ponto a ponto

Use u=x/L. Como os modos são reais, expandir o módulo quadrado dá Lρ=sin²(πu)+sin²(2πu)+2cosφ sin(πu)sin(2πu). O termo cruzado pode ser positivo ou negativo em uma posição. A densidade total continua não negativa, pois é um módulo quadrado. A integral do termo cruzado no intervalo inteiro é zero, mas ele pode deslocar probabilidade entre suas partes.

Lρ=sin²(πu)+sin²(2πu)+2cosφ sin(πu)sin(2πu)

## Calcular a probabilidade da metade esquerda

Integre em 0≤u≤1/2. Cada termo sin² contribui 1/4. Para o produto, 2sin(πu)sin(2πu)=cos(πu)−cos(3πu), cuja integral é 4/(3π). Logo P_esq=1/2+[4/(3π)]cosφ. Na metade direita o termo tem sinal oposto. O ponto u=1/2 tem probabilidade zero e não altera a escolha de incluir ou excluir a fronteira.

P_esq=1/2+4cosφ/(3π)

## Prever três casos antes de mover o controle

Para φ=0, P_esq≈0,924413; para φ=π, P_esq≈0,075587. Para φ=π/2, vale 1/2. Nenhum caso altera a probabilidade total. O controle compara fases φ=kπ/4 com k inteiro de 0 a 8, e não mostra tempo transcorrido. Uma fase que evolui sob um Hamiltoniano requer uma lei dinâmica adicional.

P_esq(0)+P_esq(π)=1

## A posição média também responde à fase

A média é ∫xρ(x)dx, não a coordenada do máximo. Dividir por L dá ∫₀¹u[Lρ(Lu)]du. Os dois termos sin² somam 1/2 nessa integral, e integrar o termo cruzado por partes fornece −16cosφ/(9π²). Portanto ⟨x⟩/L=1/2−16cosφ/(9π²), entre aproximadamente 0,319873 e 0,680127. Isso é média de resultados do modelo, não uma trajetória da partícula.

⟨x⟩/L=1/2−16cosφ/(9π²)

## Uma mistura soma probabilidades de preparações

Compare com um procedimento que prepara φ₁ em metade dos ensaios e φ₂ na outra metade. Sua densidade é ρ_mist=(|φ₁|²+|φ₂|²)/2: somamos probabilidades com pesos clássicos, sem termo de interferência. Isso difere de preparar a mesma superposição pura em cada ensaio. No gráfico, a mistura é o tracejado preto; a superposição é azul.

ρ_mist=(|φ₁|²+|φ₂|²)/2

## Densidades de posição iguais não identificam o estado

Com φ=π/2 ou 3π/2, cosφ=0 e a densidade de posição da superposição coincide com a mistura neste instante. Isso não torna os estados iguais. Por exemplo, numa medição projetiva ideal que inclui o próprio estado χ=(φ₁+iφ₂)/√2 como alternativa, a preparação pura χ dá probabilidade 1 para essa alternativa. Na mistura de φ₁/φ₂, cada preparação tem sobreposição quadrática 1/2 com χ, dando probabilidade total 1/2. É uma comparação matemática de observáveis, sem propor implementação experimental.



## Normalizar e verificar por integração independente

O laboratório calcula ψ complexa, integra seu módulo quadrado por Simpson e compara com as expressões para intervalo e média. Mudar L escala ψ por L⁻¹ᐟ² e ρ por L⁻¹; as probabilidades em frações iguais da caixa não mudam. As referências do painel vêm de quadratura independente. A verificação numérica tem tolerância e não substitui a prova das integrais.



## O que esta aula ainda não resolve

Não há simulação de contagem de detecções, preparação física, colapso dinâmico, evolução temporal ou reconstrução completa do estado. A base de senos não significa que o espectro do poço tenha sido derivado aqui. O exemplo uniforme antigo continua somente como exemplo de densidade, com sua ressalva de descontinuidade; o novo estado serve a uma pergunta diferente sobre fases. Aprovação da disciplina e material assistido não certificam domínio pessoal.



## Exercícios e resoluções

### Qual probabilidade?

1×1/2=1/2.

### Densidade não nula num ponto implica probabilidade pontual não nula nesse modelo contínuo?

É preciso integrar uma região; ponto tem medida zero.

### Para ψ em uma dimensão com x em metros, qual unidade de |ψ|² permite uma probabilidade adimensional? Dê o expoente de metro.

ρ tem unidade m⁻¹; multiplicar por dx em metros deixa a probabilidade adimensional.

### Nos dois modos ortonormais, quanto vale a integral total de |ψ|²?

Os pesos somam 1 e a integral cruzada é zero.

### Com φ=0, calcule a probabilidade da metade esquerda.

1/2+4/(3π)≈0,924413182.

### Com φ=π, calcule a probabilidade da metade esquerda.

1/2−4/(3π)≈0,075586818.

### Com φ=π/2, qual é ⟨x⟩/L?

cos(π/2)=0, portanto a média normalizada é 1/2.

### Na mistura 50% de cada modo, qual é a probabilidade da metade esquerda?

Cada modo atribui 1/2 à metade esquerda; a média ponderada é 1/2.

### Densidade maior que 1 é sempre erro de normalização?

Densidade tem unidade inversa de comprimento; é a integral de probabilidade que deve estar entre 0 e 1.

### Multiplicar toda a função por e^{iα} altera a densidade de posição?

A fase global tem módulo um e cancela no módulo quadrado.

### Superposição e mistura com a mesma densidade de posição são necessariamente o mesmo estado?

Outras medições podem distingui-los; uma densidade de posição não especifica todo o estado.

### O controle de fase é uma simulação de evolução temporal do poço?

O painel compara estados em um instante e não implementa uma lei temporal.


## Born e fase relativa — 22/10/2026

Aula `f4-born` aprofundada de três seções/dois exercícios para 14/12. Preservados exemplo uniforme, sua ressalva de descontinuidade, código incorporado e desafio antigos. Novo recorte: duas funções senoidais ortonormais em [0,L], estado ψ=(φ₁+exp(iφ)φ₂)/√2 em um instante, normalização, termo cruzado e probabilidades de intervalo. Painel `bornPhase` em arquivo exclusivo `born-phase-models.js`. Três MathML novos. A normalização não depende da fase; o termo cruzado integra zero no espaço inteiro e pode redistribuir probabilidade entre regiões.

Para u=x/L, Lρ=sin²(πu)+sin²(2πu)+2cosφ sin(πu)sin(2πu). P_esq=1/2+4cosφ/(3π), média ⟨x⟩/L=1/2−16cosφ/(9π²). φ=0 dá P_esq≈0,924413; φ=π dá ≈0,075587; φ=π/2 dá 0,5. Densidade tem unidade inversa de comprimento; o gráfico usa Lρ adimensional. Mistura é preparação clássica 50% em cada modo, sem termo cruzado. Coincidência de densidade para φ=π/2 ou 3π/2 não identifica o estado. A aula fornece comparação matemática por projetor para distinguir estado puro e mistura, sem propor instrumento ou protocolo real.

Fonte privada: Nussenzveig, Curso de Física Básica, volume 4, segunda edição 2014, segunda reimpressão 2017/digital 2018 conforme metadados já conferidos. Consulta parcial adicional de §8.2 pp.237–239/PDF238–240 e §9.1 pp.271–273/PDF272–274. Página 272/PDF 273 inspecionada visualmente. Relação densidade/amplitude e normalização conferidas no corpo; exemplos de dois modos e números são próprios. Sem leitura integral dos capítulos, reprodução de figuras, cópia do PDF ou alegação de resolver o poço e sua evolução. Programa oficial não reaberto neste bloco: mapeamento anterior preservado.

Laboratório: `python3 labs/born-fase/experiment.py`; testes `python3 -m unittest discover -s labs/born-fase -t .`. Cinco testes novos: 45 integrais de intervalo por Simpson com amplitude complexa contra primitiva; médias, complementos e simetria; fase global e mistura com mesma densidade/contraste por projetor; escala e fronteiras; contratos. Nove referências independentes em `reference.json` por quadratura de 4096 subintervalos, conferidas no JS. O laboratório e painel comparam estados em um instante; o controle k inteiro 0..8 não é relógio. Não há detecções aleatórias, ajuste ou validação experimental.

Revisão de cobertura reconheceu apoio posterior de Química I `q1-hidrogenio-linhas` para linhas espectrais: energias aproximadas fornecidas e emissões já desenvolvidas. Grupo 22/23 passa de lacuna a parcial, sem atribuir derivação de modelos atômicos completos. Não conta como aula própria de Física IV. Grupo 38, solução do átomo de hidrogênio, continua lacuna; fenda dupla quântica também não recebe cobertura completa por este exemplo de dois modos. O mapa agora registra 18 grupos parciais/oito lacunas, nenhum completo. São 18 aulas próprias/93 exercícios, seis recortes mais desenvolvidos e 12 introduções curtas. Nota pessoal permanece incompleta segundo relato, sem inspeção ou importação.

Verificação: 793 testes Python, 283 demonstrações JS/849 cenários finitos mais referências adicionais e 468 estruturas MathML aprovados. JS repetido após correção de texto no relatório, sem mudança nas equações. No navegador, teclado levou fase a π/2 (densidades coincidentes, meia probabilidade) e π (redistribuição para direita); questão 6 aceitou 0,075586818. Viewport 390 px com gráfico/relatório legíveis, sem transbordamento horizontal e console sem erros observados. Prévia `born-fase-mobile.jpg`, viewport restaurado. Material em rascunho para revisão pessoal. Catálogo global: 488 aulas/2621 exercícios.

Próxima ação pessoal: explicar por que o termo cruzado integra zero no total e não necessariamente em meia região; resolver questões 5–8 sem consulta. Próximo aprofundamento local: integrar Born a Schrödinger/observáveis com hipóteses antes de modelar tempo. Próxima alternância global: cobertura e sequência de Computação IV, preservando os percursos complementares e a distinção entre evidência e rascunho. Saldo semanal após bloco: 99%; parada operacional: 65%.
