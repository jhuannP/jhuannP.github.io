# Primeira lei: mesmos estados, caminhos diferentes

Rascunho original22/10/2026, revisão pessoal pendente. Aprofunda `f2-primeira-lei` de3/2para14seções/12exercícios, quatro MathML; preserva IDs, exemploΔU7e desafio de compressão/expansão.

## Fonte e convenção

Nussenzveig, *Curso de Física Básica2*, quinta edição Blucher2014: leitura parcial de§§8.5–8.6pp.216–219(PDF217–220), §9.1(d)p.233(PDF234) e§9.2p.235(PDF236), para estado, calor/trabalho, integral quase estática e U(T) no gás ideal. Extrações incluíram vizinhas; não capítulo inteiro. Paginação confirmada no corpo. Nenhuma página/figura/problema reproduzido. Caminhos, valores, esquema, código e exercícios próprios.

Q>0entra; W>0realizado pelo gás; ΔU=Q−W. Trabalho de fronteira usa pressão externa; aqui processos quase estáticos sem atrito permitem p do gás. Não aplicar ∫p_interno dV arbitrariamente em expansão livre.

## Modelo

Gás ideal fechado, nR=1J/K, p₁=100kPa,V₁=3L,T₁=300K. Razão r=V₂/V₁de1/2a3em meios, p₂=100/rkPa,V₂=3rL,T₂=300K. ΔU=0 porque U(T). Isso não é ciclo quando r≠1.

Isotérmico:W=300lnr. Isocórico→isobárico:W=300(1−1/r). Isobárico→isocórico:W=300(r−1). Todos emJ e Q líquido=W. Temperaturas intermediárias nos dois quebrados300/r e300rK; não isotérmicos em geral. kPa·L=J. Compressão conserva orientação negativa do trabalho, sem usar área absoluta.

Tese visual: três curvas/traços em mesmo plano p–V e tabela para calor/trabalho; estados comuns destacados. Conteúdo: um controle de razão, caminhos, balanço e limitações. Interação: expandir/comprimir compara os mesmos extremos dos três caminhos; r1colapsa os caminhos específicos. Sem animação temporal, medição, reservatório real, irreversibilidade, capacidade térmica ou rendimento calculados.

## Verificação e continuação

Quatro testes:seis razões por quadratura Simpson4096 de p(V), retângulos de pressão constante, estados/temperaturas intermediárias, ordenação/sinais/reversão e contratos. Seis referências Decimal80 cruzadas com JS. Apenas biblioteca padrão.

Execute `python3 -m unittest discover -s labs/primeira-lei-caminhos -t .`, `node test_simulations.cjs`, `node test_math.cjs` na raiz.

Próxima revisão: justificar ΔU0com Q/Wdiferentes e explicar por que Tfinaligual não fecha ciclo. Capacidade térmica, gases reais e processos irreversíveis continuam pendentes.
