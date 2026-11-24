# Arrasto linear — solução, transiente e energia

Modelo de massa constante, eixo para baixo, fluido em repouso num referencial inercial. m v′=mg−bv; m>0, b≥0, g≥0, t≥0, SI. Empuxo desprezado. Valores m=2 kg,b=4 kg/s,g=10 m/s² são didáticos, não ajustados nem validação do regime. v0 pode ser negativo ou acima da terminal.

Para b>0: τ=m/b, vT=gτ, v=vT+(v0−vT)exp(−t/τ), Δy=vTt+(v0−vT)τ(1−exp(−t/τ)). O arrasto sempre dissipa potência−bv². Com U=−mgy: D=b∫v²dt=mgΔy−ΔK. O balanço não é uma descrição microscópica do aquecimento do meio.

## Fontes e proveniência —27/10/2026

Nussenzveig, Curso de Física Básica Volume1, 5ª ed., §5.2, p.118/PDF119: recorte textual parcial de resistência em fluidos. No livro o coeficiente do termo linear é chamado a e o quadrático b; o b desta aula representa somente o coeficiente linear. Não se copiam exemplos ou figuras e não houve nova inspeção visual do exemplar neste bloco.

[OpenStax University Physics1 §14.7](https://openstax.org/books/university-physics-volume-1/pages/14-7-viscosity-and-turbulence): introdução linear/quadrático e contexto de regime, consulta parcial. Limiares de Reynolds para tubos não foram usados como critério universal de queda. Sem reproduzir tabelas, figuras, exercícios ou números de fluidos da fonte. Deduções, valores, curvas e verificações próprios.

## Código e limites

`state` recebe parâmetros finitos (bool rejeitado), b=0 tem solução separada e retorna None para τ/terminal. Para b>0 a escala derivada também deve ser finita e positiva. Usa expm1 e séries de kernels em r=t/τ pequeno para melhorar o cancelamento na posição, mas não promete aritmética exata. Não mede parâmetros, calcula empuxo ou resolve arrasto quadrático, vento variável ou escoamento.

Na raiz: `python3 -m unittest discover -s labs/arrasto-linear -t .`.

Casos de referência e terminal, subida/inversão, diferenças finitas para posição/velocidade e EDO, quadratura independente do trabalho dissipado, limite de tempo curto e b→0, contratos e ausência de ultrapassagem da terminal no modelo. Quadraturas/diferenças usam tolerâncias declaradas e não demonstram adequação experimental.

Próxima revisão de20min: desenhar forças nas duas direções e derivar a velocidade; depois integrar posição e reconstruir a energia. Regime de Stokes com geometria e empuxo, outros arrastos, dados reais, leitor de tela, Windows real e revisão pessoal pendentes.

Conferência em27/10/2026: cinco testes locais e14 de catálogo aprovados;817 estruturas MathML globais. Interface390px: sinal rejeitou−20 e aceitou20 pelo Enter; inversão com peso persistente aceita. Figura inspecionada, largura390px e console sem erros; captura na raiz `arrasto-linear-mobile.jpg`. Saldo79%, parada65%.
