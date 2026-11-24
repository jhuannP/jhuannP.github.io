# Resíduos físicos — referência, amostragem e erro

29/10/2026. Rascunho assistido por IA, revisão pessoal pendente. Percurso complementar; sem interferência na IC, framework ou rede neural geral.

## Modelo e contas

Problema adimensional−u″=2 em[0,1],bordas zero, referência u*=x(1−x). Envelope u=x(1−x)N fixa as bordas. Na forma forte, r=2N−2(1−2x)N′−x(1−x)N″−2. Exige regularidade compatível; ReLU por trechos não equivale automaticamente a solução C². Métodos fracos não implementados.

Baseline N=a+bx: r=2(a−1)+(6x−2)b. Pontos1/4,3/4 e perda médiaJ=(r1²+r2²)/2. Na origem,J=4,gradiente(−8,−4). Passoη=1/16 dá(1/2,1/4),resíduos−9/8,−3/8 eJ=45/64. O mínimo exato da família é(1,0); isso não prova convergência de rede geral. SomarC+Dx a uma solução deixa o resíduo interior intacto e pode violar bordas.

Contraexemplo original: v=x(1−x)+(1/8)sin(4πx). Emj/4, resíduo teórico zero e bordas corretas; em1/8,erro1/8 e resíduo2π². Pontos deslocados(1,3,5,7)/8 detectam este erro, sem certificar todas as funções. Flutuante deixa arredondamentos nos zeros do seno; testes têm tolerância.

Ligação com Green: e=u−u*,−e″=r,bordas zero. Parae C²,r contínuo, e=∫Gr;G≥0 e∫G=x(1−x)/2≤1/8 dão||e||∞≤||r||∞/8. Em[0,L],L²/8. Média finita do treino não determina norma máxima. Não substituir a premissa global por poucas amostras. Problema direto com coeficiente conhecido; inferência de parâmetros e identificabilidade não avaliadas.

## Execução

```sh
python3 labs/residuo-fisico/residual.py
python3 -B -m unittest discover -s labs/residuo-fisico -t .
```

Baseline usa int/Fraction,pontos[0,1],listas não vazias de até1000 pontos. `alias` usa seno em float,amplitude racional e frequência inteira1..32. Não há autodiff,treino neural,rede ou dado experimental. Python/desafio iniciais da aula preservados.

Cinco métodos de teste:75 resíduos por segunda diferença exata de cúbicas/25 bordas;18 gradientes por diferenças racionais de perda independente;passo e referência;contraexemplo em duas grades;contratos. Segunda diferença é exata para essas cúbicas; não pressupor o mesmo para uma rede arbitrária.

## Fontes e alcance

- [Raissi,Perdikaris,Karniadakis, página dos autores](https://maziarraissi.github.io/PINNs/), seçãoContinuous Time Models: leitura parcial29/10/2026 a construção de resíduo,grafo/derivadas,perdas por colocação e fronteira. Não reproduzimos código,figura,benchmarks ou números. Não executamos TensorFlow. arXiv1711.10561 falhou na abertura; não foi lido o artigo integral.
- [Johnson, Notes on the1d-Laplacian Green’s function](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/e1dc3f76e50d80b7f00a8040a25c0ddf_MIT18_303F14_Green_explicit.pdf),pp.1–2 já consultadas parcialmente29/10 na aulaGreen. Não reaberto aqui. Usamos a representação do problema unitário para deduzir nosso limite de norma máxima, não um teorema universal de erro de PINNs.

Exemplos,contraexemplo,prova,figura e verificações são próprios para estudo. Livro privado não buscado nesta unidade; referências públicas complementares. Material não demonstra pesquisa aplicada,compreensão pessoal ou validação científica. Próxima integração precisa de rede suave,derivadas conferidas,treino e avaliação independente.
