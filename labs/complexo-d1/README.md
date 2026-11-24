# Complexo d¹ ideal: energia e intensidade são perguntas distintas

Modelo original para revisão; sem parâmetros de composto, espectro experimental ou cálculo eletrônico.

## Primeiro percurso — energia (20 minutos)

Um elétron nos cinco orbitais d, campo octaédrico ideal estático, sem spin–órbita ou distorção. t₂g tem três orbitais a −2Δ/5; e_g tem dois a +3Δ/5. O baricentro orbital ponderado fica zero. Incluindo duas orientações de spin, seis e quatro estados preservam os dez do termo livre ²D. Isso é contagem, não dez bandas. A diferença é Δ, não o módulo da energia inferior.

Para Δ/(hc)=16000 cm⁻¹: níveis −6400 e +9600 cm⁻¹, λ=625 nm. Número de onda espectroscópico é 1/λ, diferente de k=2π/λ. A conversão exige cm⁻¹→100 m⁻¹. Constantes SI h=6,62607015×10⁻³⁴ J s e c=299792458 m/s são exatas; Δ aqui é um número escolhido. Não se determina cor percebida ou intensidade com essa conta.

## Segundo percurso — paridade (20 minutos)

Para estados de paridade p_i,p_f e operador de paridade p_μ, o integrando f* μ i troca por p_f p_μ p_i. Em todo espaço simétrico, produto −1 força integral zero. Dipolo elétrico é ímpar e estados d puros são pares: g→g cancela. Mesma multiplicidade permite pelo spin no limite sem mistura, mas não remove Laporte. Produto +1 apenas deixa de impor esse zero; outros cancelamentos/regras podem existir.

`pair_sum` demonstra o cancelamento em pares escolhidos r,−r; não integra orbitais reais. Por exemplo, contribuições (2,−2) dão zero mesmo quando a paridade permite. Não se extrapola essa soma para força do oscilador real.

## Um modelo algébrico separado para mistura

Base ortonormal g₀,g₁,u de paridades +,+,−; estado inicial g₀ e final f=(g₁+εu)/√(1+ε²), ortogonal ao inicial. Tome <u|μ|g₀>=d≠0 e <g₁|μ|g₀>=0. Então |<f|μ|g₀>|²/d²=ε²/(1+ε²). Para ε=1/5, 1/26; para ε=1/10, 1/101. A razão 26/101 aproxima 1/4 para mistura pequena, mas não é exatamente 1/4. Sinal de ε não muda esse módulo nesta construção.

Este modelo de três estados não prevê ε, Hamiltoniano ou energia deslocada; não é cálculo vibrônico. Vibração ímpar, quebra de inversão e mistura orbital podem permitir intensidade em modelos mais completos. Tampouco se afirma que todo modo a produza ou que uma banda observada determine o mecanismo.

## Execução e limites

Python 3, biblioteca padrão. Execute `python3 labs/complexo-d1/spectrum.py`; testes: `python3 -m unittest discover -s labs/complexo-d1 -t .` na raiz do protótipo. Inteiros/Fraction, faixa escolhida 1000..50000 cm⁻¹ e |ε|≤1; são limites didáticos, não leis universais. Nenhum dado privado ou PDF é servido.

Fontes consultadas parcialmente em 29/10/2026: Miessler, Fischer e Tarr, Química Inorgânica, 5ª ed. portuguesa, Pearson 2014, §11.3 pp.404–406/PDF419–421 (texto extraído; sem nova inspeção visual ou leitura integral), para termo d¹, Laporte, seleção de spin e relaxamentos. [OpenStax Chemistry 2e §19.3](https://openstax.org/books/chemistry-2e/pages/19-3-spectroscopic-and-magnetic-properties-of-coordination-compounds), recorte de separação octaédrica. Notação e exemplo próprios; sem tabelas, figuras, exercícios ou código reproduzidos. Programa oficial CCM0214 conforme registro 29/10, ativação 15/07/2024, versão ministrada não comprovada; não reaberto neste bloco.

Ainda faltam: intensidades completas, bandas vibrônicas, Tanabe–Sugano multieletrônico, transferência de carga, intervalência, parâmetros reais e revisão pessoal. Conteúdo assistido por IA não comprova domínio atual.
