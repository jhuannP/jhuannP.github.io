# Bézier: construção, derivadas e subdivisão

Laboratório geométrico original, com apoio de IA e revisão pessoal pendente. Coordenadas em uma mesma unidade geométrica; t é adimensional. Não é medição, interpolação obrigatória de dados ou trajetória dinâmica de pesquisa.

## Modelo preservado

Os controles da aula anterior são P₀=(0,0), P₁=(1,2), P₂=(2,2), P₃=(3,0). O painel e o snippet float foram preservados. O laboratório separado aceita somente int/Fraction, até 17 controles, dimensão 1..3 e t∈[0,1]; bool/float são rejeitados. Não modifica os controles de entrada.

A construção de de Casteljau interpola pares vizinhos e repete até restar um ponto. Quatro controles dão uma representação de grau no máximo três. Neste exemplo específico, x=3t e y=6t(1−t), de grau dois. Em t=1/2:

- Q: (1/2,1), (3/2,2), (5/2,1).
- R: (1,3/2), (2,3/2).
- B: (3/2,3/2).

A fórmula de Bernstein usa pesos C(n,i)tⁱ(1−t)ⁿ⁻ⁱ. São não negativos e somam 1 no intervalo: a curva permanece no fecho convexo dos controles e comuta com transformações afins. O teste de limites coordenados é uma consequência necessária dessa propriedade, não uma prova algorítmica geral de pertença ao fecho; a justificativa vem dos pesos.

## Hermite e escalas

Na cúbica, B′(0)=3(P₁−P₀) e B′(1)=3(P₃−P₂). Vetores derivada T₀ e T₁ de Hermite correspondem a P₁=P₀+T₀/3 e P₂=P₃−T₁/3. Os pontos-guia usados na apresentação de Hermite do Burden não devem ser substituídos diretamente pelos controles de Bernstein sem converter essa escala.

Alterar só P₁ por δ desloca B(t) pelo peso 3t(1−t)² vezes δ. Para δ=(0,1), a alteração de y é 3/8 em t=1/2 e atinge máximo 4/9 em t=1/3. A cota convexa de erro absoluto nos dados não é uma prova completa de estabilidade de ponto flutuante ou erro relativo pequeno perto de zero.

## Dividir sem alterar o desenho

No corte τ=1/2, os controles esquerdos são P₀, Q₀, R₀, B; os direitos são B, R₁, Q₂, P₃. Em parâmetro local s∈[0,1], B_esq(s)=B(τs) e B_dir(s)=B(τ+(1−τ)s). Isso preserva as partes da curva exatamente.

Derivadas locais são multiplicadas por τ e 1−τ, respectivamente. Elas podem diferir no corte apenas pela mudança de escala. O código aceita também τ=0 ou 1, que produz uma parte degenerada; a discussão de duas partes não degeneradas usa 0<τ<1.

Na junção de duas curvas cúbicas independentes, C⁰ exige extremos iguais. Para derivadas não nulas, G¹ exige múltiplos positivos; C¹ em parâmetros unitários exige igualdade dos vetores. O exemplo Q=[(3,0),(5,−4),(6,−4),(7,0)] começa com derivada (6,−12), enquanto a primeira termina com (3,−6). Durações 2 e 1, respectivamente, igualam as velocidades, sem garantir aceleração contínua ou uma dinâmica válida.

## Executar e verificar

Da raiz:

```sh
python3 labs/bezier-subdivisao/curves.py
python3 -B -m unittest discover -s labs/bezier-subdivisao -t .
```

Seis métodos: triângulo literal e 17 avaliações do polinômio independente; 63 combinações grau/parâmetro contra a fórmula de Bernstein; nove transformações afins e perturbações; três cortes com nove parâmetros por parte (54 igualdades de reparametrização) e escalas de derivada; derivadas e junção; contratos e preservação das entradas. As contagens não representam aplicações reais ou testes pedagógicos com alunos.

Armazenar todo o triângulo custa O(n²d) espaço e operações aritméticas; a implementação por linha usa O(nd) espaço. Esses custos contam operações, sem afirmar custo constante de números racionais com tamanho de bits arbitrário. Não implementamos comprimento de arco, curvatura, curvas racionais, B-splines, ajuste de dados ou análise geral de arredondamento.

## Fontes — 29/10/2026

Burden, Faires e Burden, *Análise Numérica*, 10ª edição, §3.6. Recortes visuais das pp.179,181–182,184/PDF193,195–196,198 consultados para contexto paramétrico e derivadas de Hermite. A figura, exemplos e exercícios deste laboratório são próprios, sem reproduzir imagens ou soluções do livro. PDF privado não servido. Programa formal de CCM0218 cita edição diferente; a situação acadêmica e a consulta anterior ao programa não foram alteradas neste bloco. Bézier é um complemento geométrico, sem obrigação curricular presumida.

[C.-K. Shene/MTU — Finding a Point on a Bézier Curve](https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/de-casteljau.html): consulta parcial na recorrência e no custo da recursão ingênua. Nenhum código ou figura copiado. A recorrência já existia na aula e foi aprofundada por provas e verificações independentes.

A revisão pessoal deve reconstruir as duas partes e explicar as escalas de derivada, antes de usar a página como demonstração de competência.
