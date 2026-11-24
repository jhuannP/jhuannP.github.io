# Compton: energia e momento em duas componentes

Material original em rascunho para revisão de Jhuann; não é dado experimental ou resultado da IC. Elétron livre inicialmente em repouso, um fóton incidente e um fóton final, sem campos, ligação, partículas adicionais ou energia externa.

Unidades: α=Eγ/(mₑc²), q=p/(mₑc), λC=h/(mₑc). Fóton entra em +x; θ é o ângulo do fóton final acima desse eixo. Energia: 1+α=α′+Ee*. Momento: (α,0)=α′(cosθ,sinθ)+qₑ. A norma do elétron é Ee*²−|qₑ|²=1.

Com d=1−cosθ: α′=α/(1+αd), k=α²d/(1+αd), qe,x=α(1+α)d/(1+αd), qe,y=−α′sinθ. λ′/λC=1/α+d, de modo que Δλ/λC=d. O código usa d=2sin²(θ/2), k e qe,x sem subtrair números quase iguais; em 90° usa o cosseno exato conhecido. Nos extremos 0/180° o seno é zero explícito. O ângulo de recuo é indefinido se o elétron permanecer parado.

A vista de energia mostra frações, não intensidade. A vista de momentos divide todos os vetores pelo momento incidente; é um triângulo de soma vetorial, com o vetor eletrônico transladado. Nos casos colineares, faixas separadas evitam sobreposição. Não são trajetórias nem posições dos objetos. A tabela usa novamente mₑc² e mₑc, sem a divisão pela energia incidente.

Cinemática não fornece distribuição angular, seção de choque de Klein–Nishina, fluxo ou espectro instrumental. Não se implementam elétrons ligados/móveis, Compton inverso, espalhamentos múltiplos ou efeitos de polarização. A energia do fóton não cresce neste recorte; não generalizar a elétron inicial em movimento.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/compton/experiment.py
python3 labs/compton/verify_decimal.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes: vinte referências independentes por bisseção da norma do elétron em Decimal 80 dígitos (cossenos exatos de 0/60/90/120/180°); conservação de energia e momento em x/y e norma em 52 cenários; monotonicidade, deslocamento/frações e extremos; recuo indefinido em 0°, pequeno ângulo e domínio. Em θ=10⁻⁹ graus, a transferência calculada diretamente continua positiva enquanto α−α′ em binary64 zera. Tolerâncias verificam esses casos, sem prova geral de precisão. Vinte e quatro configurações JS/Python e as vinte raízes Decimal comparadas diretamente com JS.

O verificador e `decimal_reference.json` estão disponíveis para reprodução. O parâmetro α é 0,1..2 no painel, sem atribuição a um material. O exercício em pm fornece λC=2,43 pm arredondado; não é um resultado medido pelo site.

## Fontes consultadas parcialmente — 16/10/2026

- Nussenzveig, *Curso de Física Básica*, vol. IV, segunda edição, 2014, exemplar privado do acervo: seção 7.4, trechos das pp. 210–212 (PDF 211–213), com inspeção visual de pp. 210 e 211. Trecho final de p. 212 apenas para a fórmula/deslocamento, sem declarar leitura do capítulo seguinte.
- [OpenStax III 6.3](https://openstax.org/books/university-physics-volume-3/pages/6-3-the-compton-effect): trechos de momento do fóton, balanços e deslocamento, sem reprodução de dados/figura experimental.

Exemplo, exercícios, desenho e implementação próprios; nenhuma página, figura ou espectro copiado. Pendentes: seção de choque, dados/incertezas, materiais, elétrons em movimento/inverso e revisão pessoal.
