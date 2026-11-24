# Disco exponencial: luminosidade, abertura e escala

Execute `python3 experiment.py`. Na raiz, `python3 -m unittest discover -p 'test_*.py'` inclui os quatro testes deste laboratório. Sem catálogo, rede ou dependências adicionais.

Disco circular, visto de frente, I(R)=I₀ exp(−R/h), sem poeira ou outras componentes. I₀ em uL/kpc², h/R em kpc; uL é unidade sintética de luminosidade de uma banda. L∞=2πI₀h² extrapola o perfil até infinito. A fração interna é 1−(1+x)exp(−x), x=R/h. Raio de meia-luz é calculado por bisseção; não é ln2 vezes h nem o raio da metade do brilho local.

A rotina usa série para x<0,01 para evitar cancelamento próximo ao centro; nos demais casos usa expm1. Testes independentes com Simpson, Decimal de alta precisão em x minúsculo, derivada, monotonicidade, conversão de unidades e escala. `reference.json`: 36 casos comparados ao JavaScript. Entradas finitas em escala representável; não é biblioteca de magnitudes ou comprimentos extremos.

Demonstração: curva azul de fração acumulada e pontilhada de brilho local normalizado; ambas adimensionais, mas diferentes. Alterar I₀ muda luminosidades, sem alterar razões. Não é evolução temporal, ajuste de imagem ou perfil de massa. Não estima matéria escura ou razão massa/luz.

Fonte consultada diretamente em 16/10/2026: [Bovy, seção 1.2.1](https://galaxiesbook.org/chapters/0-02.-Introduction_2-A-brief-tour-of-galaxy-observations.html), para perfil exponencial e limites da interpretação. Aulas Yale sobre o tema apareceram indexadas, mas o PDF não abriu; não foi declarado como leitura integral. Integrações, exemplos, código e exercícios desta aula são originais, com apoio de IA e revisão pessoal pendente. Nenhuma figura ou exercício de fonte foi reproduzido.
