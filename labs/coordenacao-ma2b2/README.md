# MA₂B₂: geometrias ideais e classes de arranjos

22/10/2026. Rascunho didático original para revisão pessoal. Não documenta síntese, medida, uso de instrumento ou domínio de Jhuann.

## Fontes e recorte

- Miessler, Fischer e Tarr, *Química Inorgânica*, quinta edição brasileira, Pearson 2014, acervo privado autorizado. Corpo consultado parcialmente: pp.315–316 (PDF330–331), distinção de isomeria e complexos tetracoordenados; pp.332–333 (PDF347–348), geometrias de coordenação quatro. Página316/PDF331 também inspecionada visualmente. A extração intermediária incluiu páginas317–318, mas elas não fundamentam o recorte de quiralidade e hexacoordenação desta aula. Não se afirma leitura integral. Nenhuma página, figura, exercício ou solução do livro foi distribuída.
- IUPAC, *Brief Guide to the Nomenclature of Inorganic Chemistry*, relatório de2015, [§3, Stereodescriptors](https://iupac.qmul.ac.uk/BriefGuide/inorganic.html), consulta direta parcial em22/10/2026: símbolos de geometria e relação cis/trans no quadrado-planar. Não se ensina aqui o cálculo de índices de configuração/CIP nem nomenclatura completa.
- Vínculo curricular: item6 do [programa USP CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214), conferido na auditoria existente. É apenas abertura parcial de coordenação/isomeria; história dos modelos, isomeria constitucional, quelação, quiralidade e demais geometrias continuam pendentes.

As coordenadas, classificação por órbitas, testes, figuras e exercícios são próprios. As fontes sustentam o contexto químico; não lhes atribuímos o algoritmo computacional ou dados experimentais.

## Hipóteses

M é a origem. Quatro ligantes monodentados pontuais fornecem quatro doadores. Dois ligantes A são equivalentes entre si; o mesmo para B. O número de coordenação conta átomos doadores, não é em geral o número de moléculas de ligante. Forma, carga, metal, ligantes específicos, energia, solvente, cinética e contraíons não foram escolhidos.

Sítios 1..4 na interface, índices0..3 no Python:

- Quadrado: (1,0,0),(0,1,0),(−1,0,0),(0,−1,0).
- Tetraedro: (1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1).

Geometrias são hipóteses separadas. A figura tetraédrica usa projeção ortográfica X=x, Y=(2y−z)/√5, profundidade=(y+2z)/√5, com escala escolhida para leitura. Seus ângulos na tela não medem os ângulos espaciais. Ligações para profundidades negativas são tracejadas; positivas, contínuas. Isso codifica frente/trás, não intensidade ou força de ligação. As ligações desenhadas representam somente M–doador. Sítios numerados não identificam ligantes individualmente.

## Derivação e equivalência

Há C(4,2)=6 escolhas de sítios para A. Geramos matrizes de permutação de eixos com sinais, retemos as ortogonais de determinante+1 que preservam o conjunto de sítios e extraímos suas permutações. Identidade vem primeiro na ordenação lexicográfica. São oito rotações do quadrado e doze do tetraedro. Para estas geometrias, o conjunto está completo: uma isometria do quadrado permuta quatro vértices preservando vizinhança, dando oito possibilidades, cada uma com extensão espacial própria; uma rotação do tetraedro é determinada pela imagem de um vértice (quatro escolhas) e uma rotação ao seu redor (três escolhas). A enumeração constrói exatamente esses8/12 casos.

Para um par A, sua órbita é o conjunto de imagens sob essas rotações. No quadrado, quatro pares adjacentes formam cis, dois opostos formam trans. Produto escalar das direções normalizadas vale0 ou−1: rotações não podem misturar as classes. No tetraedro, todos os pares distintos têm produto escalar−1 e normas²3; cosθ=−1/3. A enumeração mostra uma órbita com seis pares, não apenas igualdade de um invariante.

Estabilizadores dentro do grupo próprio do esqueleto: cis2, trans4, tetraédrico2. Órbita×estabilizador=8/8/12, respectivamente. Esses números não são grupos de ponto completos dos arranjos coloridos. Operações impróprias não foram usadas como equivalências. A estrutura interna dos ligantes não existe no modelo, portanto não extrapolar conclusões de quiralidade para ligantes reais ou outras composições.

Não inferir razão2:1 de produtos a partir dos tamanhos4/2 das órbitas: não foi definida distribuição física. Rotação rígida não é caminho de isomerização; mudar o par no controle escolhe outra distribuição, sem calcular barreira ou mecanismo.

## Executar e conferir

```sh
python3 labs/coordenacao-ma2b2/experiment.py
python3 -m unittest discover -s labs/coordenacao-ma2b2 -t .
```

Quatro testes: grupos espaciais/fechamento (64+144 composições), classificação independente por distâncias, contagem de pares fixos e estabilizadores, estados/ângulos/contratos. A contagem média de pares fixos confirma duas e uma classes sem reutilizar a construção de órbitas. `reference.json` contém144 estados dos controles; JS compara permutações, posições, órbitas, tamanhos, ângulos e limites do controle de rotação com Python. O estado de rotação é limitado ao máximo do grupo ao mudar de geometria.

## Continuidade

Revisão pessoal pendente. Próximo recorte sugerido de coordenação: MA₃B₃ octaédrico, distinção fac/mer por relações trans, após ler o corpo pertinente; não generalizar as duas geometrias atuais. Para o objetivo amplo, alternar antes com outra disciplina identificada no plano. Verificação final e saldo ficam no registro do bloco em `QUIMICA_3.md`.
