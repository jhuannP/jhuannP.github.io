# Pulso numa corda: derivação, borda e energia

Material didático original em rascunho, pendente da revisão pessoal. Não é uma experiência realizada nem resultado de pesquisa de Jhuann.

## Fontes consultadas em 16/10/2026

- [OpenStax University Physics I, 16.3](https://openstax.org/books/university-physics-volume-1/pages/16-3-wave-speed-on-a-stretched-string): balanço de força transversal, aproximações e c²=T/mu.
- [OpenStax University Physics I, 16.5](https://openstax.org/books/university-physics-volume-1/pages/16-5-interference-of-waves): reflexão fixa e livre transversal, com anel ideal sem massa/atrito.

As fontes apoiam a física geral. Texto, perfil polinomial compacto, solução de imagens, exercícios e figuras são próprios. Não foram copiados figuras, exercícios, capítulos ou livros privados. O acervo universitário já mapeado continua privado; esta consulta online não é uma nova identificação de edição local.

## Perfil e domínio

A=0,02 m, w=0,5 m, mu=0,1 kg/m. F(s)=A[1-(s/w)²]³ para |s|<w, zero fora. F, F' e F'' são contínuos; F'= -6As/w²[1-(s/w)²]² no interior. Perfil incidente inicialmente em [-2,5;-1,5] m, viajando para a direita. A velocidade transversal inicial é -cF'(x+2), não zero.

Para x<=0 e t>=0, y=F(x-ct+2)+R F(x+ct-2), com R=-1 na fixa e +1 na livre. A forma refletida usa a paridade de F. A formulação geral é f(x-ct)+R f(-x-ct), f(x)=F(x+2); a extensão além da borda é uma ferramenta matemática, não outro meio.

Chegada da frente: 1,5/c s; centro: 2/c s; fim do contato do suporte com a borda: 2,5/c s. No encontro livre o deslocamento da borda alcança 2A, mas depois o pulso refletido isolado tem amplitude A. No encontro fixo simétrico a soma dos deslocamentos pode zerar em todo o domínio enquanto a energia permanece cinética.

## Modelo e energia

Velocidade c=sqrt(T/mu), com T constante em cada cenário. O controle de T define um novo cenário; não simula variação temporal da tensão. A janela [-8,0] m contém todo o suporte para 0<=t<=4 s e 1<=c<=2 m/s. Não há reflexão na borda esquerda da janela: o modelo vive no semieixo.

Densidade u=mu*y_t²/2+T*y_x²/2, potência P=-T*y_x*y_t. Na fixa y_t(0,t)=0; na livre y_x(0,t)=0. Logo não há trabalho transmitido à borda ideal e a energia total se conserva. Não há absorção nem transmissão.

Referência fechada: E=T integral F'² ds = 1024 T A²/(385w). Ela resulta de integrar o polinômio 36A²/w * z²(1-z²)^4 em [-1,1]. Os termos cruzados da densidade das duas ondas se cancelam usando T=mu*c², R²=1. O valor exibido é a energia global do modelo, não uma medição.

## Reprodução e checagens

Na raiz: `python3 -m unittest discover -s labs/reflexao-corda -t .`. Quatro testes incluem:

- perfil, dados iniciais e equação da onda por diferenças finitas;
- condições de borda e sinais antes/durante/depois da reflexão;
- energia por Simpson com 4000 subintervalos, comparada à referência fechada em dez pares borda/tempo para cada uma de duas velocidades;
- suporte, tempos e entradas fora do domínio.

`reference.json` contém 150 configurações cruzadas com JS: duas bordas, três velocidades, cinco instantes e cinco posições. A comparação entre linguagens é complementar às referências analíticas e à quadratura independente.

## Exploração e limites

1. Use T=0,1 N, mu=0,1 kg/m: c=1 m/s. Compare t=0; 1,5; 2; 2,5 e 3 s nas duas bordas.
2. Na fixa confira y(0,t)=0. Na livre confira inclinação zero e o dobro do deslocamento da borda no encontro do centro.
3. No encontro fixo t=2 s, explique a energia positiva apesar da curva total horizontal.
4. Aumente T para 0,4 N e preveja o novo tempo do centro antes de mover o relógio.

Solução analítica de imagens: não é FDTD ou outro integrador temporal. Não há dispersão, interface, transmissão, dissipação, variação espacial do meio ou solução geral de dados iniciais. Esses assuntos e modos normais gerais permanecem pendentes; a disciplina não está concluída.
