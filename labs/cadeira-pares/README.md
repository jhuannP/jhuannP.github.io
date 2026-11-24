# Duas cadeiras, duas faces e dois grupos

29/10/2026. Conteúdo original para revisão de Jhuann. Modelo ideal de duas cadeiras, não otimização molecular, dinâmica, medida ou previsão de composto.

Carbonos1..6 mantêm identidade. Faces+1/−1; na cadeira A, axiais acima em1,3,5 e abaixo em2,4,6. Cadeira B troca axial/equatorial, preserva face e carbono de cada grupo. Dois grupos genéricos R/T em carbonos distintos; nomes não são descritores CIP. Mesmo sinal de face é cis; oposto é trans. Sem casos geminais.

## Tabela por distância relativa

| Par | cis | trans |
|---|---|---|
|1,2|ax/eq ⇄ eq/ax|ax/ax ⇄ eq/eq|
|1,3|ax/ax ⇄ eq/eq|ax/eq ⇄ eq/ax|
|1,4|ax/eq ⇄ eq/ax|ax/ax ⇄ eq/eq|

A ordem das cadeiras depende da face inicial. A inversão não transforma cis em trans. Axial não significa acima, nem cis significa ambos axiais.

## Pesos prescritos e limites energéticos

Cada grupo tem penalidade axial adimensional r≥1. Peso de uma cadeira é o produto de1/r para grupos axiais e1 para equatoriais. Só normalizamos os dois pesos compatíveis com a configuração fixa. Uma interpretação opcional é ΔG_ax=RT ln r e diferenças aditivas de energia livre a temperatura fixada. Não usamos valores A experimentais, nem derivamos essas penalidades da geometria. Interações entre grupos, solvente, degenerescências extras e outras conformações não estão modeladas.

Em cis1,2 com ambos acima,rR=3 e rT=5: cadeira A axR/eqT,peso1/3;B eqR/axT,peso1/5. Populações5/8 e3/8. Ambas têm um axial: contar axiais não resolve a comparação quando grupos diferem. Se rR=rT, ficam iguais neste modelo. Em trans1,2 com R acima/T abaixo:A ambos axiais peso1/15,B ambos equatoriais peso1;populações1/16 e15/16. Estes são parâmetros hipotéticos,não dados químicos.

Não comparar diretamente populações de cis e trans: são configurações fixas distintas, e a inversão não as interconverte. Equilíbrio pressuposto não fornece barreira ou taxa. O painel anterior acompanha apenas um R e não representa este novo modelo de pares.

## Execução

`python3 labs/cadeira-pares/pairs.py`

`python3 -B -m unittest discover -s labs/cadeira-pares -t .`

Cinco testes:cenários;tabela de seis casos;60 pares/combinações de faces e inversão;16 pares de penalidades comparados a pesos independentes de dois indicadores condicionados às duas cadeiras;contratos. Modelo discreto exato não valida composto real.

## Fontes

Brown/Poon,Introduction to Organic Chemistry,6ªedição,imprint2016,§3.7 pp82–83/PDF102–103: consulta textual parcial29/10/2026; p83/PDF103 inspecionada visualmente para cadeiras e conservação cis/trans. Página contém exemplo do livro, não adotado como exercício do site. Quadro, cenário1,2, parâmetros, código e figura próprios; sem copiar desenho ou distribuir PDF privado. Fonte apoia geometria e comparação qualitativa de casos com metilas, não os fatores3/5 fictícios.

Júpiter CCM0224: resultado oficial indexado reconferido29/10/2026 indica ativação01/01/2025. Abertura direta e abertura do resultado falharam; não alegar nova leitura integral do programa. Mapa existente relaciona a análise conformacional ao item5. Aprovação2026/1 não prova versão ministrada nem domínio pessoal.

Próximo estudo:desenhar as duas cadeiras, registrar faces e só então classificar posições. Reconstruir5/8 e15/16; explicar por que não são proporções cis/trans. Revisão pessoal, modelos não aditivos, casos gerais e evidência experimental pendentes.
