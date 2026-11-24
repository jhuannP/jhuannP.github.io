# Jacobiano e medida de área — notas de aula

Rascunho para revisão de Jhuann. Conteúdo e exemplos próprios, sem experiência pessoal certificada.

## Coordenadas novas não conservam cada área

Em x=r cosθ, y=r sinθ, pequenas células têm área aproximadamente r dr dθ. Esse fator é o módulo do determinante do Jacobiano. O próprio integrando também deve ser reescrito.

dA=r dr dθ

## O disco tem limites simples

Para raio R, r∈[0,R] e θ∈[0,2π]. Integrar 1 exige incluir r: ∫∫r dr dθ=πR². Ignorar r produz uma conta com escala errada em R.

área=πR²

## Evitar contar o mesmo ponto repetidamente

A transformação deve ser usada com domínio e hipóteses adequadas. O centro r=0 e a duplicação angular da fronteira não alteram esta integral de área, mas a cobertura geral precisa ser controlada.

Jacobiano em módulo e multiplicidade declarada

## O que o teorema afirma neste recorte

Seja Φ(u,v)=(x(u,v),y(u,v)). Numa região onde Φ é C¹, é injetiva e tem determinante não nulo, a mudança de variáveis relaciona integrais sobre a região original e sua imagem, para integrandos e regiões com as condições de integrabilidade apropriadas. Nos exemplos limitados desta aula, as fronteiras têm área nula e o integrando é contínuo. Casos de fronteira ou de sobreposição exigem análise; não basta encontrar uma fórmula para o determinante.

∫∫_D f(x,y) dA=∫∫_E f(Φ(u,v)) |det DΦ(u,v)| du dv

## A derivada transforma uma pequena célula

A matriz DΦ tem como colunas Φ_u e Φ_v, os vetores de variação por unidade dos parâmetros. Um pequeno retângulo com lados Δu e Δv é aproximado por um paralelogramo de lados Φ_u Δu e Φ_v Δv. Sua área é |det DΦ|ΔuΔv. Para mapas não lineares, a imagem real tem bordas curvas: essa interpretação local justifica o fator, mas não é a demonstração global do teorema. O Apostol desenvolve provas posteriores que não foram lidas neste bloco.

Área linearizada=|det DΦ| Δu Δv

## Calcular o determinante polar

Para Φ(r,θ)=(r cosθ,r sinθ), as colunas são (cosθ,sinθ) e (−r sinθ,r cosθ). O determinante é r cos²θ+r sin²θ=r. O raio tem unidade de comprimento; θ, em radianos, é adimensional. Assim r dr dθ tem unidade de área. O painel abaixo continua restrito ao disco, não implementa todas as mudanças desta aula.

det DΦ=r

## A célula finita não tem área exatamente r Δr Δθ

Um setor anular de raio interno r, espessura h e abertura Δθ em radianos tem área exata [(r+h)²−r²]Δθ/2=(rh+h²/2)Δθ. Usar o raio interno no produto dá rhΔθ e omite h²Δθ/2. Com r=2, h=1/10 e Δθ=1/5, a área exata é 41/1000, contra 40/1000. No centro r=0, a aproximação pelo canto inferior é zero para uma célula finita, mas sua área exata não é; isso não invalida a fórmula integral.

A_exata−A_canto=h²Δθ/2

## Orientação muda o sinal, não a área

Uma reflexão x=−r cosθ, y=r sinθ tem determinante −r. Ela inverte orientação. Para integrar uma densidade escalar sobre uma área, usamos o módulo, de modo que o disco mantém a mesma área positiva. Integrais orientadas de formas ou fluxos têm outras convenções; não se deve levar esta regra de módulo indiscriminadamente para qualquer integral.

dA=|−r| dr dθ=r dr dθ, com r≥0

## Uma fronteira repetida difere de cobrir tudo duas vezes

No disco, escolher 0≤θ<2π evita duplicar raios, fora do centro. O centro e a costura angular têm área nula, e podem ser tratados por exclusão e limite. Já usar 0≤θ<4π percorre quase todos os pontos duas vezes. Integrar o mesmo fator r nesse domínio dá 2πR², duas vezes a área do disco. O erro está na multiplicidade em área positiva, não numa borda isolada.

Cobertura dupla: ∫₀⁴π∫₀ᴿ r dr dθ=2πR²

## Mapear o disco unitário em uma elipse

Para a,b>0, use x=a r cosθ e y=b r sinθ, com 0≤r≤1 e 0≤θ<2π. A imagem é x²/a²+y²/b²≤1. O determinante é ab r, porque a escala linear (a,b) multiplica a área por ab. Integrando 1, obtemos área πab. Se a e b são semieixos em metros, ab tem unidade m².

Área da elipse=πab

## O integrando também muda

Na elipse, x²+y² vira r²(a² cos²θ+b² sin²θ). Multiplique por ab r: a integral radial de r³ em [0,1] é 1/4, e cada integral angular de cos²θ ou sin²θ em uma volta é π. Portanto ∫∫(x²+y²)dA=πab(a²+b²)/4. Para a=2 e b=1, a área é 2π e a integral é 5π/2; a média espacial de x²+y² é 5/4. Isso não é massa sem declarar uma densidade.

I/π=ab(a²+b²)/4

## Determinante um também pode curvar a região

Considere x=u, y=v+u² no quadrado 0≤u,v≤1. A inversa é u=x, v=y−x²; a imagem é 0≤x≤1, x²≤y≤x²+1. A matriz tem colunas (1,2u) e (0,1), logo det=1: preserva área, mas não forma nem todos os comprimentos. Para integrar y, usamos v+u², obtendo 1/2+1/3=5/6. Em coordenadas cartesianas, integrar y de x² a x²+1 dá o mesmo resultado.

∫₀¹∫₀¹(v+u²) dv du=5/6

## Como verificar sem transformar o teste em prova

O laboratório confere células por aritmética racional e compara invariantes da elipse com uma malha cartesiana independente. A malha aproxima uma fronteira curva e produz erro de discretização; concordância em alguns eixos não demonstra o teorema geral. O exemplo de elipse, a faixa curva e os exercícios são próprios; o livro fundamenta a fórmula, a leitura geométrica e o caso polar.



## Roteiro antes de calcular

Descreva E nos parâmetros e D nas coordenadas originais; obtenha Φ e sua inversa quando possível; verifique regularidade e cobertura; derive DΦ; escolha o módulo para uma medida escalar; transforme também f; integre e confira escala/unidades. Fronteiras singulares e mapas muitos-para-um não recebem permissão automática por uma lista de verificação. A aula não fornece demonstração geral ou algoritmo para qualquer região.



## Exercícios e resoluções

### Qual área/π?

R²=4.

### Pode omitir o Jacobiano ao mudar variáveis?

Ele corrige a medida de área.

### No setor r=2, h=1/10 e Δθ=1/5, qual é a área exata?

[(2,1)²−2²]/10=41/1000.

### No mesmo setor, qual é o erro área exata menos aproximação pelo raio interno?

h²Δθ/2=(1/100)(1/5)/2=1/1000.

### Na elipse de semieixos 2 e 1, quanto é área/π?

ab=2.

### Na mesma elipse, quanto vale ∫∫(x²+y²)dA dividido por π?

ab(a²+b²)/4=2×5/4=5/2.

### Qual é a média espacial de x²+y² nessa elipse?

I/área=(5π/2)/(2π)=5/4.

### Para x=u, y=v+u² no quadrado unitário, quanto vale ∫∫_D y dA?

Integre v+u²: 1/2+1/3=5/6.

### Um determinante negativo torna negativa a área geométrica?

A medida escalar usa o módulo; o sinal registra orientação.

### Usar θ de 0 a 4π é apenas repetir uma fronteira do disco?

Repete quase todos os pontos, portanto há cobertura dupla em área positiva.

### Determinante igual a um garante conservar todos os comprimentos?

Garante o fator local de área um; a faixa curva mostra que forma e distâncias podem mudar.

### A aproximação r h Δθ ser zero no canto r=0 obriga a célula finita a ter área zero?

A célula finita tem h²Δθ/2; uma aproximação local não é igualdade para uma célula de largura não nula.


## Mudança de variáveis aprofundada — 22/10/2026

Aula `c3-polares` passou de três seções/dois exercícios para 14/12. Preservados exemplo inicial do disco, Python incorporado, desafio de escala e painel `polarMeasure`. O painel continua restrito ao disco. Onze seções e dez exercícios desenvolvem derivada linear/área, hipóteses de mudança de variáveis, módulo/orientação, singularidades na fronteira e multiplicidade, elipse e faixa curva. A interpretação local não é apresentada como demonstração global do teorema.

Exemplos originais: setor r=2,h=1/10,Δθ=1/5 tem medida 41/1000 e aproximação pelo canto 40/1000; erro 1/1000. Para elipse a=2,b=1, área/π=2, integral de (x²+y²)/π=5/2 e média espacial 5/4. Transformação x=u,y=v+u² preserva área e curva a imagem do quadrado; integral de y=5/6. Nenhum desses números é medição física ou densidade estipulada. Cobertura de θ em [0,4π) duplica área positiva; não é simples repetição de uma borda.

Fonte privada: Apostol, Cálculo, volume 2, tradução da segunda edição, Reverté 1996/reimpressão 2004, §§11.26–11.27, leitura parcial de pp.441–446/PDF454–459. Página446/PDF459 inspecionada visualmente. O deslocamento confirmado é 13 páginas neste recorte, diferente do observado em outras partes; não generalizar. A matriz das derivadas é organizada aqui por colunas, de acordo com o restante do site; a transposta do arranjo do livro tem o mesmo determinante. As provas posteriores §§11.29–11.30 não foram lidas ou desenvolvidas integralmente. Texto, exemplos, exercícios e código são próprios. Nenhuma imagem ou PDF privado servido.

Programa CCM0223 reaberto diretamente: ativação 01/01/2025 e quatro itens reconfirmados; item 2 sustenta a integração múltipla. Compatibilidade temporal com aprovação 2025/1 não comprova o programa ministrado. Não houve nova inspeção do histórico pessoal ou da lista de livros ausentes.

Laboratório `labs/jacobiano-area/`: medidas racionais de células e invariantes de elipses. Aceita int/Fraction, eixos/larguras/abertura positivos e raio não negativo; bool/float recusados. Orientação deve ser int ±1. A medida da célula é a integral do Jacobiano sobre os parâmetros: para aberturas maiores que 2π conta multiplicidade, não área da união geométrica. Não é integrador geral. Executar `python3 labs/jacobiano-area/experiment.py` e `python3 -m unittest discover -s labs/jacobiano-area -t .`.

Quatro testes novos: quatro elipses contra integração aproximada em malha cartesiana 400×400; determinante por derivadas das coordenadas em 30 estados; células racionais por diferenças de primitivas, subdivisão e erro de célula; escala, orientação e contratos. A malha tem tolerância de discretização e não prova o teorema. No refinamento, o erro de uma célula com metade da espessura cai por fator 4; não se confunde isso com o erro somado de toda uma partição refinada.

Verificação: 788 testes Python e 465 estruturas MathML aprovados. Nenhum arquivo de simulação JS alterado; sua suíte não foi repetida. Navegador aceitou 5/2 no exercício 6, conferiu fórmulas e texto em 390 px sem transbordamento horizontal e console sem erros. Prévia `jacobiano-elipse-mobile.jpg`; viewport restaurado. Rascunho para revisão pessoal.

Reconciliação do percurso de Cálculo 3: as 16 aulas próprias agora aparecem uma vez cada nas etapas, com apoios externos separados. Incluídos os links que faltavam para limites, Hessiana, Lagrange, potencial e Green. Parte diferencial permanece identificada como apoio de Matemática III; integração pertence ao mapa principal de Matemática IV. Cálculo 3: 16 aulas/89 exercícios, dez introduções curtas e seis recortes mais desenvolvidos. Cinco grupos do mapa de IV continuam parciais; nenhuma disciplina completa. Total global: 488 aulas/2611 exercícios.

Próxima revisão pessoal: resolver o exemplo da elipse e explicar módulo versus multiplicidade sem consulta. Próxima ampliação local: integral escalar de linha ou troca de ordem, com hipóteses e demonstrações pendentes. Próxima alternância global: sequência e lacunas de Física IV. Notas pessoais e Samsung Notes continuam pendentes. Saldo semanal após bloco: 99%; parada operacional: 65%.
