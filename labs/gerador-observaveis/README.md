# Gerador e observáveis do OU

Laboratório original de contas exatas, sem trajetórias amostradas ou dados de pesquisa. Não é solução numérica geral de EDEs nem prova funcional completa.

## Processo e representação

OU centrado dX=−θX dt+σdW,θ>0,σ≥0. Para grau finito e condição inicial fixa, os momentos necessários existem. Polinômios não estão automaticamente no domínio de um semigrupo em C₀(ℝ); usamos aqui a expressão estendida de Itô, com as condições de integrabilidade descritas na aula. σ=0 é limite determinístico, não uma densidade gaussiana não degenerada.

`apply` calcula Lf=−θx f′+σ²f″/2 em coeficientes de potências crescentes. `evaluate` usa Horner. Entradas são int/Fraction, sem bool/float, polinômio não vazio e grau≤12.

`transition(f,rho)` calcula E[f(ρx+√q Z)] pela expansão binomial, q=S(1−ρ²),S=σ²/(2θ),Z normal padrão. Só usa momentos gaussianos, não amostra Z. ρ racional está em[0,1];para0<ρ≤1,ρ=e^(−θt). ρ=0 é limite de tempo infinito, não um intervalo finito. A rotina parametriza a transição pela contração, não pelo tempo. Compor tempos equivale a multiplicar contrações.

No exemploθ=2,σ=2,S=1:

- Lx=−2x;
- L(x²−1)=−4(x²−1);
- L(x³−3x)=−6(x³−3x);
- L(x⁴−6x²+3)=−8(x⁴−6x²+3).

Para X₀=2 eρ=1/2, E[X_t]=1 e E[X_t²]=7/4,logo variância3/4. No tempo inicial, o segundo momento tem derivada−12 e a variância tem derivada4. Não confundir momento bruto e variância.

## Executar

Da raiz:

```sh
python3 labs/gerador-observaveis/generator.py
python3 -B -m unittest discover -s labs/gerador-observaveis -t .
```

Cinco testes cobrem observáveis/eigenvalores literais;54 composições e18 comutações de operador/transição;16 regras de produto e médias estacionárias;quatro diferenças de tempo curto contra Decimal70;contratos. Há também limites determinísticos e variação de parâmetros. O teste de tempo usa diretamente E[X_t²|X₀=2]=1+3exp(−4t), sem passo Euler.

Na fronteira temporal,3(exp(−4t)−1)/t tende a−12. Seu erro positivo é≤24t. `expm1` evita subtração de números quase iguais em ponto flutuante. Conferir poucas médias estacionárias não determina uma distribuição desconhecida; o núcleo gaussiano usado aqui é hipótese conhecida do OU.

## Domínio e adjunto

A identidade integral de Itô exige controlar o integral estocástico para ter esperança zero e a integrabilidade da deriva. A derivada temporal da esperança exige condições adicionais; não é uma derivada de trajetória.

O adjunto formal em dx é L*ρ=−(bρ)′+(σ²ρ)″/2, com fronteiras apropriadas. Não substitua automaticamente L por L* ou ignore absorção/reflexão em domínio limitado. A aula apenas introduz esse caminho para Fokker–Planck.

## Fonte — 29/10/2026

Pavliotis,Stochastic Processes and Applications,Springer2014,§2.3 pp38–40/PDF51–53 e§3.4 pp66–68/PDF79–81,trechos textuais de semigrupo,gerador,adjunto e Itô. P66/PDF79 visualmente conferida paraσ σᵀ e fator1/2. Leitura parcial,sem livro/capítulos completos,figuras ou exercícios reproduzidos. PDF privado não servido.

Chorin/Hald segue referência temática do percurso,sem nova leitura pertinente neste bloco. Código,exemplos,figura e exercícios próprios preparados com apoio de IA. Revisão pessoal e uso na IC pendentes; não são resultados ou validação científica da pesquisa.
