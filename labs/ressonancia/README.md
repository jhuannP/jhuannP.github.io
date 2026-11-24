# Cargas formais e ressonância

Material original em rascunho. Contabilidade de Lewis, não simulação quântica nem evidência de domínio pessoal ou de experiência experimental.

Exemplos curados: acetato C₂H₃O₂⁻ e acetamida C₂H₅NO. Cada um tem 24 elétrons de valência. Os H permanecem nos mesmos átomos. A e B selecionam dois contribuintes de octeto completo; o teste 2 conserva carga e elétrons, mas mantém duas duplas no carbono central além da ligação ao metil, produzindo dez elétrons ao redor desse carbono. Não é um contribuinte aceitável. Carbocátions/radicais e outros contribuintes ficam fora da enumeração; octeto completo não é requisito universal de Lewis.

`B` soma ordens de ligação ao átomo, incluindo H; `L` conta pares livres. CF=v−2L−B. A carga formal assume partilha igual de pares ligantes; não é uma carga parcial física. Contar 2(B+L) informa elétrons ao redor, com compartilhamento; somar esses valores não dá o inventário global. Este exige contar cada ligação distinta uma única vez.

As duas setas curvas relacionam formalmente a figura selecionada à outra: par livre do terminal vira par pi e o par pi anterior vira par livre no O. Duas redistribuições simultâneas, sem eixo de tempo. No teste inválido as setas são ocultas. Trocar o controle não anima uma molécula alternando entre espécies. As posições são uma disposição gráfica, não geometria otimizada.

Acetato ideal: oxigênios equivalentes; ambiente e coordenação não modelados. Amida: contribuintes não equivalentes e sem percentuais atribuídos. O contador não prevê pesos, comprimento, energia, pKa ou local de protonação. Conservar elétrons/octetos não prova estabilidade. Não se trata de gerador geral de ressonância.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/ressonancia/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes: enumeração independente de 64 combinações por exemplo (ordens 1/2 e pares 0..3 nos terminais); contagens e cargas explícitas nos seis desenhos; conectividade fixa, redistribuição de pares e simetria dos oxigênios; domínios, perda de um par e identidade de contabilidade em 36 combinações genéricas. A enumeração restrita encontra os dois contribuintes de octeto completo selecionados, sem provar exaustividade química geral. Seis referências Python em `reference.json` para comparação com JavaScript; não são dados experimentais.

## Fontes consultadas parcialmente — 16/10/2026

- Brown e Poon, *Introduction to Organic Chemistry*, sexta edição, Wiley 2016, exemplar privado já localizado no acervo. Seção 1.2D: p. impressa 10 (PDF 30); seção 1.5: pp. 18–20 (PDF 38–40). Extração dos trechos e inspeção visual das páginas 10 e 18; sem reprodução de PDF, figuras ou exercícios. A referência curricular tem ressalva de ano/versão mantida no mapa.
- [OpenStax, 2.3](https://openstax.org/books/organic-chemistry/pages/2-3-formal-charges): convenção de carga formal.
- [OpenStax, 2.5](https://openstax.org/books/organic-chemistry/pages/2-5-rules-for-resonance-forms): contribuintes, núcleos fixos e valência. Não se adotou uma regra de estimar estabilidade contando desenhos.
- [OpenStax, trecho de amidas em 24.3](https://openstax.org/books/organic-chemistry/pages/24-3-basicity-of-amines): conjugação do par de N e carbonila. Não se adotam afirmações universais sobre protonação em qualquer condição nem dados de pKa.
- [IUPAC R05326](https://goldbook.iupac.org/terms/view/R05326), definição de ressonância por resultado indexado; abertura direta retornou 403. [C01309](https://goldbook.iupac.org/terms/view/C01309), significado formal de estrutura contribuinte por resultado indexado. Não se declarou leitura integral dessas páginas.

Pendentes: orbitais/conjugação geral, ligação química quantitativa, pesos de contribuintes, acidez orgânica e revisão pessoal de Jhuann.
