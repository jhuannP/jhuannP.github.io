# Peptídeos: cadeia, cortes e contagem de átomos

Rascunho original para revisão de Jhuann. Exemplos estipulados, sem síntese, hidrólise ou determinação estrutural realizadas por ele.

## Fontes consultadas em 16/10/2026

- Nelson/Cox, Princípios de Bioquímica de Lehninger, sexta edição, Artmed 2014: trechos de 3.2, páginas impressas 85–87 (PDF 115–117). Ligação amida, resíduos, terminais, síntese/ativação e limites de extrapolar pKas de grupos livres. Leitura parcial, sem capítulo integral ou cópia de exercício/figura.
- [OpenStax Organic Chemistry 26.4](https://openstax.org/books/organic-chemistry/pages/26-4-peptides-and-proteins): direção N→C, ligação peptídica e conectividade.
- [OpenStax Organic Chemistry 26.9](https://openstax.org/books/organic-chemistry/pages/26-9-protein-structure): níveis estruturais e diferença de desnaturação. Não foi copiada estrutura de proteína ou figura.

Texto, sequências, esquema de resíduos, exercícios, código e balanços são próprios. O PDF privado não é servido.

## Modelo restrito

Uma cadeia linear, não cíclica, sem bloqueios de terminais, pontes dissulfeto, outras ligações laterais ou modificações. Apenas G/A/S: glicina, alanina e serina. S é o código de serina, não um átomo de enxofre. Fórmulas dos aminoácidos livres usadas como referência: C2H5NO2, C3H7NO2 e C3H7NO3, obtidas de suas estruturas usuais.

A fórmula da cadeia é a soma das fórmulas livres menos (n-1) H2O. É contabilidade covalente de referência, sem estados adicionais de protonação e sem mecanismo de biossíntese. Grupos amida internos não são novos grupos amino livres. Alterações de carga por pH exigem outro modelo.

Um conjunto de k cortes distintos consome k H2O e produz k+1 fragmentos, n-1-k ligações e k+1 terminais de cada tipo. Um corte repetido no mesmo índice não consome outra água. A relação de componentes pressupõe cadeia aberta sem outras conexões; não se transfere automaticamente a ciclos ou pontes laterais.

## Reprodução e verificação independente

Na raiz: `python3 -m unittest discover -s labs/peptideos -t .`.

Os quatro testes verificam fórmulas pequenas conhecidas, todos os subconjuntos de cortes em cadeias pequenas contra componentes de um grafo construído separadamente, fechamento de átomos com água, hidrólise completa e domínio. `reference.json` contém 19 configurações JS/Python (16 do painel e três aminoácidos livres). A comparação entre linguagens complementa, sem substituir, a checagem por grafos/átomos.

No exemplo GAS após corte 2: GA+S, uma ligação restante, uma água consumida; C8H15N3O5+H2O=C8H17N3O6. No painel de seis unidades, cortes após 2 e 4 geram três fragmentos e consomem duas águas.

## Como ler a figura

Círculos são resíduos e linhas são ligações peptídicas esquemáticas, não átomos ou distâncias moleculares. N/C azuis indicam grupos terminais livres; × indica conexão hidrolisada. Os modos de corte são escolhidos, não especificidade de uma protease. O modelo não prevê estrutura secundária/terciária, energia, função ou rendimento de reação.

Compare GASGAS e SAGSAG: mesma composição/fórmula e outra ordem. Depois hidrolise todos os elos e confira as seis unidades livres. Isso não é desnaturação: o painel muda ligações covalentes, enquanto perda conformacional pode ocorrer sem quebrar o backbone.

## Conteúdo ainda pendente

Conformações e ângulos, estruturas experimentais, ciclos, pontes laterais, modificações, proteases e mecanismos, síntese/ativação, cinética e relação quantitativa sequência–função. A aula introduz níveis estruturais; não conclui proteínas ou aminoácidos. A aula de enovelamento em dois estados é apoio termodinâmico em outra trilha, não uma previsão atômica.
