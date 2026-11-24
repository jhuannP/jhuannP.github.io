# Cadeiras e inversão: face preservada

Unidade didática original de 22/10/2026, rascunho para revisão de Jhuann. Não é evidência de domínio pessoal, otimização molecular ou resultado de pesquisa.

## Referência consultada

Brown e Poon, *Introduction to Organic Chemistry*, sexta edição, exemplar privado Wiley 2016. Consulta parcial de §3.6: texto de cadeira/axial/equatorial em p. 76 (PDF 96) e inversão em p. 79 (PDF 99). P.79 foi renderizada e inspecionada visualmente nesta data; p. 77/PDF 97 havia sido inspecionada na localização do bloco anterior. Figuras serviram à conferência conceitual; não foram copiadas. Trechos sobre populações e energias específicas não fundamentam números deste modelo; nenhum valor desse tipo foi incorporado. Não se leu integralmente a seção. PDFs privados permanecem fora do site.

CCM0224: vínculo com análise conformacional (item 5) do programa reconferido por conteúdo indexado no bloco anterior, em 22/10/2026; abertura direta falhou. Ativação 01/01/2025 não prova versão ministrada. Programa e divergências bibliográficas preservados no mapa, sem nova consulta direta declarada.

## Construção geométrica própria

Para i=0,…,5, carbono C(i+1) em (r cosθᵢ,r sinθᵢ,sᵢ/6), θᵢ=iπ/3, r=√(8/9), sᵢ=(−1)^(i+chair). Direção axial=(0,0,sᵢ), equatorial=(r cosθᵢ,r sinθᵢ,−sᵢ/3). As ligações do anel têm comprimento um, e os quatro vetores de ligação em cada carbono são unitários, com produto mútuo −1/3 e soma zero. A verificação usa as posições dos vizinhos, não apenas rótulos de tipos.

O grupo R fica em carbono fixo de 1 a 6 e face definida pelo sinal da direção z. Mudar chair troca a cadeira ideal; a direção de R é escolhida entre axial/equatorial de modo a preservar a face. Não se reflete a molécula inteira com seus substituintes. O modelo oferece somente dois estados finais; não interpola coordenadas nem mostra intermediários da inversão.

Na cadeira A (chair=0), axiais de C1/C3/C5 acima e C2/C4/C6 abaixo. Na cadeira B o padrão troca. Assim, R em C1 acima é axial→equatorial; R em C2 acima é equatorial→axial. Um R não define relação cis/trans entre dois substituintes; a regra de faces é explicada conceitualmente, sem simular o par.

O desenho é projeção oblíqua própria: coordenadas gráficas (300+140(x+0,4y),260+75y−125z). Posição para cima na tela não define a face; z define. Ligações externas têm comprimento gráfico igual a 0,65 unidade de ligação do anel, escolha de legibilidade sem escala molecular. Só um grupo R é explicitamente nomeado; os demais enlaces externos aparecem em cinza. Axiais em tracejado, equatoriais em traço fino contínuo, anel espesso; R em destaque e identificado por texto. Sem energia, tamanho real de substituintes, população, cinética ou atribuição CIP.

## Executar

```sh
python3 labs/cadeira-ciclohexano/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: fechamento/comprimentos e todos os pares de vetores tetraédricos; preservação de face/carbono e troca de tipo nos 24 estados; alternância das axiais e contagens; contratos. 24 estados JSON cruzam vetores, rótulos e relatório Python/JavaScript. Testes e diagramas não substituem revisão conceitual.

Próximo desenvolvimento local: casos dissubstituídos e relações cis/trans, após referência pertinente; análise de preferência energética exige especificar grupos, condições e modelo. A disciplina e a biblioteca continuam parciais.


22/10/2026 — Cadeira/inversão: unidade própria de 12 seções/12 exercícios, painel de dois estados finais e 24 referências, preservando carbono/face e trocando axial/equatorial. Fontes parciais Brown/Poon e limites em labs/cadeira-ciclohexano/README.md. 598 testes Python, 243 demos/729 cenários e 335 MathML aprovados; teclado, exercícios e legibilidade desktop/390 px conferidos. Química IV 7 aulas/82 exercícios, cobertura parcial. Catálogo 465 aulas/2108 exercícios em rascunho, revisão pessoal pendente. Próxima ação: cobertura/referências de Biologia I, alternando áreas. Saldo 89%; parada 65%.
