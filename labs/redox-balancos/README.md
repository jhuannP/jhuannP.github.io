# Redox: conservar os átomos não basta

Notas, deduções e verificações originais preparadas com apoio de IA em 28/10/2026. Revisão pessoal pendente. Apoio a Química I; não é protocolo experimental, resultado de IC ou prova de domínio de Jhuann.

## O problema e os limites

Dados reagentes MnO₄⁻ e Fe²⁺ e produtos Mn²⁺ e Fe³⁺, em meio aquoso ácido, buscamos coeficientes que conservem átomos e carga. O esqueleto e o meio são informações dadas: o balanceamento não os descobre. H⁺ é a notação convencional simplificada para o balanço aquoso, sem afirmar prótons isolados em água. Estados: íons em solução aquosa; H₂O líquida; elétrons apenas nas semirreações formais.

Mn no permanganato: x+4(−2)=−1, portanto x=+7, usando oxigênio com Nox −2 nesta espécie, não em todo composto. Fe²⁺ passa de +2 a +3 e perde um elétron formal; Mn passa de +7 a +2 e recebe cinco. O oxidante é MnO₄⁻, que se reduz; o redutor é Fe²⁺, que se oxida. Nox é contabilidade formal, não carga parcial medida em cada átomo.

Redução: MnO₄⁻+8H⁺+5e⁻→Mn²⁺+4H₂O. Oxidação: Fe²⁺→Fe³⁺+e⁻. Multiplique a segunda por cinco, some e cancele os cinco elétrons de cada lado:

MnO₄⁻+5Fe²⁺+8H⁺→Mn²⁺+5Fe³⁺+4H₂O.

Há Mn=1, Fe=5, O=4 e H=8 de cada lado. A soma das cargas, em múltiplos da carga elementar positiva, é −1+5·2+8=+17 à esquerda e 2+5·3=+17 à direita. As cargas dos dois lados são iguais, sem exigir que sejam zero; contraíons omitidos da equação iônica podem garantir a eletroneutralidade da solução completa. Com quatro Fe de cada lado, todos os átomos ainda batem, mas as cargas são +15 e +14: o candidato falha.

## Outro meio, outra escrita formal

Para a semirreação de oxigênio com produto H₂O especificado: O₂+4H⁺+4e⁻→2H₂O. Some 4OH⁻ aos dois lados, agrupe 4H⁺+4OH⁻ como 4H₂O e cancele duas águas. Resta O₂+2H₂O+4e⁻→4OH⁻. O resultado conserva O=4 e H=4, com carga −4 nos dois lados. Isso demonstra uma transformação algébrica de escrita; não determina o produto de qualquer redução de O₂ ou a estabilidade de uma espécie em um pH arbitrário. Não convertemos o exemplo Mn/Fe em previsão química para outro meio.

## Código e verificação

```sh
python3 balance.py
python3 -m unittest test_balance.py
```

Python padrão, sem pacotes. Cadastro explícito de espécies, composição e carga: não interpreta fórmulas, não escolhe produtos, não calcula Nox automaticamente e não resolve equilíbrio. Coeficientes int/Fraction não negativos; bool/float, espécies não cadastradas e lados inteiramente nulos são rejeitados. O resíduo é produtos menos reagentes. Coeficientes são proporções adimensionais; os totais podem ser lidos como contagens relativas ou mol de átomos por unidade de extensão. A linha de carga é contabilidade estequiométrica em unidades de carga elementar, não corrente elétrica ou potencial.

Cinco testes: semirreações e soma; candidato que falha somente em carga; enumeração de 1536 candidatos inteiros com Mn fixado em um; escalonamento racional e adição igual de água aos dois lados; redução de O₂ em duas escritas e contratos. A enumeração finita não é prova geral de unicidade: a prova algébrica usa O→4H₂O, H→8H⁺ e carga para impor cinco Fe por Mn.

## Fontes consultadas

Atkins/Jones/Laverman, *Princípios de Química*, 7ª ed., Bookman 2018, exemplar autorizado: leitura textual parcial e inspeção visual de Fundamentos K.2 p.F80/PDF106, K.4 p.F85/PDF111, e §6K.2 p.538/PDF670 em 28/10/2026. Números de oxidação, conservação de carga e método de meias-reações. Consulta parcial, sem copiar exercícios, figuras ou tabelas. O exemplar difere da 3ª edição citada no programa; não se presume equivalência de paginação ou turma. A extração do PDF emitiu avisos de sintaxe e corrompeu sinais; as páginas relevantes foram conferidas visualmente. Os sinais usados nestas notas também foram verificados por contagem independente.

[OpenStax, Chemistry 2e, §17.1, Review of Redox Chemistry](https://openstax.org/books/chemistry-2e/pages/17-1-review-of-redox-chemistry): consulta textual parcial em 28/10/2026 para método em solução aquosa e distinção dos meios. Uma primeira URL presumida para 2e não abriu; a página correta foi localizada e aberta. Não se usa a falha como evidência de conteúdo. Deduções dos exemplos, texto, figura e código próprios.

Programa CCM0114 já registrado: ativação em 2024 posterior à turma de 2023; não revalidado neste bloco e versão da turma não comprovada. O grupo redox/complexação passa de lacuna a parcial por este recorte de balanço, com complexação ainda pendente.

## Revisão de 20 minutos

Reconstrua os números de oxidação, explique os cinco elétrons e confira as duas cargas +17 antes do código. Depois encontre um candidato que conserva átomos mas falha em carga e explique por que um balanço correto não certifica reação espontânea, mecanismo ou conversão completa. Registro pessoal a preencher por Jhuann. Permanecem pendentes complexação, equilíbrio redox, potenciais, atividades e outros sistemas.
