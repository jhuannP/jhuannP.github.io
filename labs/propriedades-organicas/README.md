# Estrutura e propriedades — interações, ebulição e solvente

27/10/2026. Notas de aula originais com apoio de IA, em rascunho; revisão pessoal de Jhuann pendente. Aula `q4-interacoes-propriedades`, primeiro recorte do item3 do mapa de QuímicaIV. Não demonstra prática experimental ou domínio pessoal.

## Formação e fontes

CCM0224: trancada2025/1 e aprovada2026/1 conforme panorama baseado no histórico atualizado, sem nova leitura do histórico neste bloco. O programa público não abriu diretamente em27/10/2026; preservado o resultado oficial indexado conferido em22/10, ativação01/01/2025, sem comprovar a versão ministrada. Não foi registrado sucesso de uma consulta que falhou.

Brown e Poon, *Introduction to Organic Chemistry*, sexta edição, Wiley2016, exemplar autorizado em Quim4/QuimicaIV/Livros. A fonte curricular cita sexta edição online2017; o exemplar é2016 e não se presume identidade de paginação. Consulta parcial: §3.8 pp.84–85/PDF104–105, §8.1C pp.231–232/PDF251–252, §8.3C p.247/PDF267. Esta última página foi renderizada e conferida visualmente. Não foram copiados tabelas, figuras ou exercícios; livro privado não distribuído. Não houve leitura integral das seções ou capítulos.

[NIST Chemistry WebBook — etanol](https://webbook.nist.gov/cgi/cbook.cgi?ID=C64175&Mask=4) e [éter dimetílico](https://webbook.nist.gov/cgi/cbook.cgi?ID=C115106&Mask=4), tabelas Antoine consultadas em27/10/2026. Coeficientes factuais abaixo preservados com unidades, faixa e atribuição; programa não acessa a rede ao executar. O NIST informa que calculou os coeficientes a partir dos dados dos autores indicados; não foram ajustados por Jhuann.

Apoio parcial: [McMurry/OpenStax §2.12](https://openstax.org/books/organic-chemistry/pages/2-12-noncovalent-interactions-between-molecules), distinção entre contribuições dispersivas, dipolares e ligações de hidrogênio; sem copiar figuras ou atividades. Formulação, exemplo de pressão comum, inversão, figura e código são próprios.

## Pergunta e interpretação molecular

Mesma fórmula não significa mesma conectividade. EtanolCH₃CH₂OH e éter dimetílicoCH₃OCH₃ têm fórmulaC₂H₆O e mesma massa molar. Interações entre moléculas, temperatura, pressão e composição participam das propriedades de uma fase.

Dispersão também existe em moléculas polares; não há escolha excludente entre “ter dipolo” e “ter dispersão”. A soma vetorial e a geometria importam para o dipolo molecular; contar oxigênios não ordena propriedades de forma universal. Vaporização sem reação não significa romper todas as ligações covalentes dentro da molécula.

No recorte neutro, o grupoO–H do etanol pode doar ligação de hidrogênio, e o oxigênio pode aceitar. Éter dimetílico não temO–H; ainda assim seu oxigênio aceita uma ligação de hidrogênio da água. A possibilidade de interação na mistura não é idêntica à associação entre moléculas da substância pura. “Doar” ligação de hidrogênio aqui não implica transferência de próton. Análise de outras famílias, geometria detalhada e estados de protonação requerem preparação adicional.

## Dados, modelo e pressão

Ebulição compara pressão de vapor com pressão externa; não há temperatura única independente de pressão. A relação de Antoine ajusta empiricamente a pressão de vapor de uma substância pura:

log₁₀(P/bar)=A−B/(T/K+C).

| Substância | A | B | C | Faixa emK | Dados usados peloNIST |
|---|---:|---:|---:|---|---|
| Etanol |5,37229|1670,409|−40,191|273–351,70|Kretschmer e Wiebe1949|
| Éter dimetílico |4,11475|894,669|−30,604|194,93–248,24|Kennedy e colaboradores1941|

T/K eP/bar indicam valores numéricos nas unidades definidas. Não inserir Celsius na expressão parametrizada em kelvin, nem converter pressão sem usar a mesma convenção dos coeficientes. Os conjuntos selecionados não são fórmulas válidas para qualquer temperatura ou pressão.

Inversão original para a aula:

B/(T+C)=A−log₁₀(P), logo T=B/[A−log₁₀(P)]−C, com a convenção de valores numéricos indicada.

P precisa ser positiva; o denominador e o resultado precisam corresponder ao domínio adotado. No cálculo a0,9bar:

- Etanol:348,495607K=75,345607°C, dentro da faixa.
- Éter:245,642430K=−27,507570°C, dentro da faixa.

As casas decimais mostram o resultado numérico dos coeficientes, não uma incerteza experimental avaliada. Valores arredondados da figura:75,35 e−27,51°C. A associação estrutural ajuda na explicação qualitativa, mas não forneceu os coeficientes nem demonstrou sozinha esses números. Não foi feita medição, simulação molecular ou estimativa por grupos.

A escolha de0,9bar mantém os dois resultados dentro das faixas. Não é1atm:1atm=101,325kPa=1,01325bar. Para o éter, a inversão a1atm daria cerca de248,336K, acima de248,24K; o código recusa. Isso não diz que a substância não possa entrar em ebulição nessa condição, apenas que o conjunto escolhido não cobre o cálculo. É preciso outro ajuste/dado antes de avançar. Nenhum valorT_boil de outra linha foi usado para estender essa faixa silenciosamente.

A derivada dlog₁₀P/dT=B/(T+C)² é positiva nas faixas. Portanto menor pressão externa é atingida a uma temperatura menor pelo ajuste; o código confere0,5 versus0,9bar. Inverter e substituir de volta é verificação de álgebra, não validação física independente do ajuste.

## O que não se conclui sobre solubilidade

Mistura envolve reorganizar interações de todos os componentes e entropia. A discussão deΔG mistura=ΔH mistura−TΔS mistura contextualiza a pergunta, sem fornecer um modelo quantitativo nesta aula. Aceitador presente não garante miscibilidade em toda proporção, e ordem de ebulição não determina a ordem de solubilidade. O programa cobre substâncias puras, não mistura etanol/água, equilíbrio líquido–líquido ou azeótropos.

## Código e verificação

`vapor.py` usa apenas Python padrão. Duas espécies cadastradas e coeficientes fixos com fonte. Entrada numéricaint/float finita, sembool; pressão positiva. Rejeita temperatura fora da faixa e inversão que sairia dela. Apenas a inversão tolera erro de ponto flutuante de até10⁻¹⁰K nos extremos e recorta essa diferença aos limites; não aceita extrapolação física. Valores enormes não convertíveis a float são rejeitados. Retorna pressão embar ou temperatura emK, nunca Celsius implicitamente.

```sh
python3 -m labs.propriedades-organicas.vapor
python3 -m unittest discover -s labs/propriedades-organicas -t .
```

Cinco testes: inversão contra bisseção separada com coeficientes da fonte, em cinco pressões comuns; monotonicidade e inversão nos101pontos de cada faixa; exemplo e mudança de pressão; extrapolação rejeitada, incluindo1atm no éter; contratos e fontes. A bisseção verifica a implementação da inversão por outro método usando a mesma relação, não é medição independente nem avaliação de incerteza do modelo.

## Resoluções e próxima revisão

1. Mesma fórmula não garante propriedades idênticas.
2. Mudança de fase sem reação não rompe todas as ligações covalentes internas.
3. O oxigênio do éter pode aceitar ligação de hidrogênio da água.
4. Dispersão também contribui em moléculas polares.
5. Pressão comum:0,9bar.
6. Etanol:348,4956K no ajuste escolhido.
7. Éter:−27,5076°C, depois de converter a partir de kelvin.
8. 1atm=1,01325bar.
9. Não extrapolar além de248,24K com o conjunto do éter.
10. Ebulição não determina solubilidade em água.
11. Reduzir pressão externa reduz a temperatura modelada nas faixas.
12. Os números dependem de coeficientes empíricos e condições.

Revisão20min: desenhar conectividades e papéis; depois reconstruir os dois cálculos, unidades e faixas. Análise em papel/código proposta, sem manipular substâncias. Dúvidas, avaliação pessoal e comprovação de domínio continuam pendentes. Preparar fusão/empacotamento, outras famílias, modelos de solubilidade e dados experimentais com incerteza; item3 segue parcial, nenhum tópico declarado completo.
