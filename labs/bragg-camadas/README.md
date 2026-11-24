# Bragg e camadas com motivo de dois espalhadores

Modelo original prescrito, sem dados experimentais. Público: graduação, após interferência, trigonometria e exponenciais complexas. Revisão pessoal e uso com aluno pendentes.

## Convenções e alcance

Espalhamento elástico, coerente, escalar. Células em j d, j=0,…,N−1, cada uma com pesos1 e b reais constantes nos lugares j d e (j+1/2)d. Não representa um cristal3D, fatores atômicos reais ou contagens de um detector. d e λ na mesma unidade; θ é rasante ao plano; ângulo entre direções incidente continuada e saída é2θ.

A diferença de caminho é2d senθ. Candidatos positivos m satisfazem mλ≤2d, incluindo o extremo formal de retroespalhamento. `orders(d,wavelength)` retorna m,θ,2θ em graus. Limites: comprimentos representáveis positivos e no máximo10000 candidatos. Não infere acessibilidade instrumental.

Defina t=2d senθ/λ, φ=2πt. `intensity(N,t,b)` retorna |(1+b exp(iφ/2)) Σ exp(i jφ)|², sem dividir por N². O cálculo usa soma direta, sem divisão removível. N inteiro1…10000, |t|≤10⁶ e0≤b≤1, sem booleanos. A redução de fase é numérica, não aritmética simbólica exata; limites finitos não garantem precisão relativa junto a zeros.

Nos candidatos t=m, a soma é N e o motivo é1+b(−1)^m. Com b=1, I/N² alterna0 e4; com b=1/2, alterna1/4 e9/4; com b=0, vale1. Para pesos iguais, o período mínimo é d/2: usar a célula maior d enumera candidatos redundantes. Não atribuir a regra a uma estrutura3D identificada.

Para N>1, zeros da soma de rede próximos a um inteiro m estão em t=m±1/N. Isso descreve largura em t; não estima tamanho de um cristal real ou resolução angular. Não há absorção, desordem, dependência angular dos pesos, polarização, multiplicidade, fundo ou ajuste.

## Executar e conferir

Da raiz:

```sh
python3 labs/bragg-camadas/bragg.py
python3 -B -m unittest discover -s labs/bragg-camadas -t .
```

Antes de executar, obtenha θ=30° e2θ=60° para m=2,d=0,30nm,λ=0,15nm. Compare N=5 e b=1/2: I=6,25 em m=1 e56,25 em m=2. Os números são unidades arbitrárias prescritas, não resultados publicados ou medidos.

Testes: marcos angulares e escala de unidades; paridade contra valores literais;75 comparações com referência real independente somando pares de posições; zeros próximos e periodicidade; contratos inválidos. Esses testes auditam contas, não teoria cristalográfica completa ou validação pedagógica.

## Fontes consultadas — 29/10/2026

- Nussenzveig, Curso de Física Básica4,2ª edição2014, reimpressão2017/digital2018, §4.11: trechos textuais pp105–106 e109–110/PDF106–107 e110–111. Páginas109–110/PDF110–111 visualmente conferidas para ângulo e equação. Sem leitura integral ou figuras reproduzidas.
- [IUCr, Structure factor](https://dictionary.iucr.org/Structure_factor): definição e soma de fases, consulta parcial. O modelo finito1D é próprio.
- [S. C. Wallwork, IUCr, Introduction to the calculation of structure factors](https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors): trechos de soma de ondas e geometria de Bragg. Sem cópia de imagens, exemplos ou leitura integral.

O programa CCM0222 não foi reaberto neste bloco: mantém conferência27/10/2026, sem prova de versão ministrada. Índices de Miller, redes recíprocas/Laue gerais, cristais3D e análise experimental continuam pendentes. Aprovação e material preparado com IA não certificam domínio pessoal.
