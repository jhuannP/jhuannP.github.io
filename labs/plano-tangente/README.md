# Plano tangente e erro em duas direções

Rascunho original para revisão de Jhuann, 16/10/2026. Coordenadas adimensionais.

`python3 experiment.py` executa o exemplo; da raiz do protótipo,
`python3 -m unittest labs.plano-tangente.test_experiment` executa quatro testes.
O nome com hífen é aceito por importlib/unittest; o pacote não exige importação manual na notação Python de instrução import.

Duas famílias: x²+2y² e x²−2y². A expansão dá R=h²±2k²,
|R|≤2ρ² e resto relativo tendendo a zero. A normal ao gráfico
(−fx,−fy,1) continua não nula no ponto crítico. Na sela, o plano
atravessa a superfície; erro zero numa direção não implica igualdade global.
O painel mostra cortes (x,y)=p+t·u; escala vertical automática, sem reconstrução 3D.

Os testes usam 72 expansões racionais exatas, tangentes de curvas parametrizadas,
refinamento, uma integral do resto pela Hessiana, limite uniforme, cancelamento,
ponto crítico e validação de domínio. `remainder` usa a expressão estável exata da
família; `exact-linear` pode ter arredondamento de ponto flutuante. Em ρ=0,
`scaled` é None. Não é um classificador geral de diferenciabilidade.

Fonte consultada parcialmente: [OpenStax Calculus Volume 3, 4.4](https://openstax.org/books/calculus-volume-3/pages/4-4-tangent-planes-and-linear-approximations),
16/10/2026: definições de plano tangente e diferenciabilidade e aproximação linear.
A conexão com Apostol II está registrada na aula anterior de gradiente; não se
atribui paginação nova sem conferência. Exemplos e códigos próprios, sem imagens
ou exercícios reproduzidos. A aula e a disciplina permanecem em elaboração.
