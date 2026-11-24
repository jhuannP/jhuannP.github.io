# Neoglicogênese: desvios, carbono e custo

Material original preparado com apoio de IA em 28/10/2026. Revisão pessoal pendente. O programa escreve “neoglicogênese”; o Lehninger usa “gliconeogênese”. São denominações da via discutida neste recorte.

## Por que não basta inverter a glicólise

Três etapas glicolíticas muito favoráveis no sentido direto, sob as condições celulares discutidas no livro, precisam de desvios para a síntese de glicose: piruvato→PEP via piruvato-carboxilase e PEP-carboxiquinase; frutose-1,6-bisfosfato→frutose-6-fosfato por uma fosfatase; glicose-6-fosfato→glicose por outra fosfatase. “Irreversível” aqui descreve a direção efetiva nas condições dadas, não uma proibição termodinâmica de qualquer reação inversa sob qualquer composição.

O desvio inicial acrescenta um carbono ao piruvato C3 para obter oxaloacetato C4, gastando ATP; a conversão a PEP C3 libera CO₂ e usa GTP. Para uma glicose, há dois piruvatos: 2×C3→2×C4→2×C3. Adição temporária de carbono não equivale a fabricar glicose C6 a partir de CO₂ líquido. O esquema acompanha contagens, não rastreamento isotópico.

## Inventário reduzido a partir de piruvato

Por mol de glicose no recorte:

- 2 mol de piruvato fornecem os seis carbonos líquidos;
- 2 ATP são usados na piruvato-carboxilase e outros 2 na reação de 3-fosfoglicerato para 1,3-bisfosfoglicerato;
- 2 GTP são usados na formação de dois PEP;
- 2 NADH são consumidos na formação das duas trioses fosfato;
- as duas fosfatases liberam fosfato por hidrólise, sem regenerar os ATP gastos pela hexocinase e PFK-1 na glicólise.

Logo, são 4 ATP + 2 GTP + 2 NADH por glicose a partir de piruvato. Contar seis transferências de grupos fosforil de nucleotídeos não transforma GTP em ATP nem fornece automaticamente energia livre em kJ. Não se transcreve uma reação completa de H₂O/H⁺/carga: o código é um inventário reduzido. A Tabela 14-3 e o texto do livro conferem a decomposição dos custos; sinais e convenções de protonação não são presumidos de uma extração OCR.

## O precursor altera a contagem líquida

Ao partir de dois lactatos, a oxidação lactato→piruvato produz dois NADH no citosol. No inventário combinado, esses dois NADH compensam os dois usados no percurso a partir de piruvato, mantendo os custos ATP/GTP e mudando o consumo líquido de NADH para zero. Isso não diz que a via funciona sem cofatores: NAD⁺/NADH continuam participando. Compartimentalização e transferência de equivalentes redutores importam; NADH não é tratado como livremente permeável à membrana mitocondrial. Rotas de transporte e isoenzimas não foram simuladas. Outros precursores, como glicerol, exigem outra contabilidade e são rejeitados pelo código.

## Modelo de estoques

`limit_from_pyruvate` assume piruvato, ATP, GTP e NADH finitos, sem regeneração, competidores ou restrições de enzimas/compartimentos. O teto é min(piruvato/2, ATP/4, GTP/2, NADH/2). Com estoques 2,4,1,2 mol, o GTP limita o teto a 1/2 mol de glicose. Restam 1 mol de piruvato, 2 ATP, zero GTP e 1 NADH. É somente um limite de consumo por estequiometria; células podem reciclar cofatores e manter fluxos que esse estoque fechado não modela.

```sh
python3 cost.py
python3 -m unittest test_cost.py
```

Python padrão; int/Fraction não negativos em mol. Float/bool/valores negativos e precursores fora do recorte são rejeitados. Quantidades não são concentrações ou taxas. Quatro testes: inventário/carbono e contraste dos precursores, 625 estoques comparados a candidatos enumerados em quartos de mol, exemplo/escala e contratos. A enumeração é uma verificação finita; a cota é deduzida de quatro desigualdades de disponibilidade.

## Fonte e limites

Nelson/Cox, *Princípios de Bioquímica de Lehninger*, 6ª ed., Artmed 2014, original 2013, exemplar autorizado. §14.4 pp.570/PDF600, 572/PDF602 e 573/PDF603 consultadas textualmente e visualmente em 28/10/2026: desvios, rotas alternativas de piruvato/PEP, cofatores e custo. Consulta parcial, sem reproduzir tabela, figura ou exercício. A tabela de reações e a discussão foram usadas para conferir o inventário reduzido, não para copiar a diagramação. Livro privado fora do site.

Programa CCM0111 já registrado, versão ministrada não comprovada; não reaberto neste bloco. O item neoglicogênese passa de lacuna a parcial, com regulação recíproca, compartimentos, precursores gerais e integração metabólica ainda pendentes. Não há cálculo clínico, recomendação alimentar ou protocolo experimental.

Revisão de vinte minutos: justificar os dois desvios enzimáticos de piruvato para PEP, localizar cada custo e explicar o saldo NADH ao trocar piruvato por lactato. Depois reconstruir a desigualdade que faz o GTP limitar o exemplo. Nada foi preenchido como explicação pessoal de Jhuann.
