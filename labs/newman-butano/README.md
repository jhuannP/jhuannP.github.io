# Newman do butano: seis orientações características

Rascunho didático original, 22/10/2026, pendente de revisão de Jhuann. Complementa o modelo de etano sem transportar sua equivalência de 120° nem seu potencial hipotético.

## Fonte e procedência

CCM0224: conteúdo oficial indexado reconferido em 22/10/2026; abertura direta do portal e do resultado indexado retornou cache miss. Ativação exibida 01/01/2025; não prova versão ministrada. Item 5: análise conformacional. Bibliografia e divergências editoriais anteriores preservadas no mapa; não se presume nova auditoria integral dos históricos ou livros.

Brown e Poon, *Introduction to Organic Chemistry*, sexta edição, exemplar privado Wiley 2016 (ano da referência online do programa difere): consulta parcial a §3.6, início p. 73 (PDF 93), p. 75 (PDF 95), pp. 76–79 (PDF 96–99). A p. 77/PDF 97 foi inspecionada visualmente. O início de p. 73 e exemplos de nomenclatura não fundamentam esta unidade. Os trechos de ciclos foram localizados para a sequência seguinte; não se afirma que esta aula já ensine cadeiras. A base conceitual é representação tridimensional e eclipsamento; os rótulos anti/gauche do butano foram conferidos na fonte complementar abaixo, não atribuídos a um trecho do Brown que não os apresenta.

McMurry/OpenStax, *Organic Chemistry*, §3.7, consulta direta parcial em 22/10/2026 aos parágrafos sobre anti/gauche, tipos de eclipsamento e distinção entre estabilidade e exclusividade de uma conformação: https://openstax.org/books/organic-chemistry/pages/3-7-conformations-of-other-alkanes . Não utilizados exercícios, figuras, números de energia ou curvas dessa fonte. Diagramas, texto, dados e código deste laboratório são originais. Não se distribuem PDFs privados.

## Modelo

Vista C2→C3 da cadeia C1–C2–C3–C4. Cada carbono central tem um CH3 e dois H. Índice zero de cada conjunto é CH3; os outros dois índices são H equivalentes, rotulados apenas para rastrear. Vetores tetraédricos unitários: componente axial ∓1/3, raio projetado √(8/9), azimutes π/2+2πk/3, com rotação φ apenas no conjunto de trás. φ é o diedro orientado entre as projeções das metilas nessa vista.

Sete posições do controle (0 a 360°, passo 60°) representam seis orientações distintas. 0°/360°: eclipsada, MM=1 e HH=2; 120°/240°: eclipsada, MH=2 e HH=1; 60°/300°: gauche, sem pares eclipsados; 180°: anti, sem pares eclipsados. Critério de alinhamento por diferença angular módulo 360, sem aproximar ângulos intermediários. Contagem geométrica não é estimativa de energia ou distância real.

O diagrama usa ponto/círculo, traço contínuo/tracejado, cor e rótulos f/t para distinguir frente/trás. Raios gráficos têm comprimentos diferentes para que os rótulos não desapareçam na eclipsada; não medem comprimentos de ligação. Não há rotâmeros internos de metila, relaxação, potencial, populações ou dinâmica. O modelo não determina forças ou atribuição CIP/R/S. Não se apresenta toda conformação alternada como anti nem se infere igualdade de energia da ausência de eclipsamento.

## Executar e verificar

```sh
python3 labs/newman-butano/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: vetores/ângulos espaciais e contagem independente por coincidência de projeções cartesianas; tipos e equivalências; diedro por produto escalar projetado; domínio. Sete estados JSON cruzam Python/JavaScript, incluindo o retorno em 360°. Casos de domínio fora da malha de 60° são rejeitados.

Próximo recorte local: cadeira do ciclohexano, preservação acima/abaixo na inversão e troca axial/equatorial; confirmar fontes e desenhar modelos próprios antes de desenvolver. Energia quantitativa e populações exigem outro modelo e referências. A disciplina continua parcial.


22/10/2026 — Nova unidade de butano em Newman: 12 seções/12 exercícios, seis orientações distintas, geometria/pares sem energia. Programa indexado e referências parciais Brown/Poon e McMurry reconferidos; limites em labs/newman-butano/README.md. 594 testes Python, 242 demos/726 cenários e 334 MathML aprovados; painel e respostas em desktop/390 px conferidos. Química IV: 6 aulas/70 exercícios, cobertura parcial; catálogo 464 aulas/2096 exercícios em rascunho. Próximo recorte: cadeira/inversão, mantendo acima/abaixo; depois alternar área. Saldo 89%, parada 65%; revisão pessoal pendente.
