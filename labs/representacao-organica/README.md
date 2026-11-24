# Representação e conectividade orgânica

Para o laboratório, baixe `experiment.py` e `molecules.json` na mesma pasta e execute `python3 experiment.py`. O exemplo Python da própria aula é autossuficiente, com esses seis dados incorporados. Na raiz do protótipo, `python3 -m unittest discover -p 'test_*.py'` inclui quatro testes deste laboratório.

Seis exemplos originais selecionados: etanol/éter dimetílico, propanal/propanona e ácido etanoico/metanoato de metila. Só C/H/O neutros de camada fechada. `analyze` completa H pela soma das ordens de ligação, verifica conectividade e produz fórmula/DBE no recorte. Não prevê estabilidade, cargas, ressonância ou estereoquímica. `isomorphic` compara grafos com elementos/ordens; não é teste completo de identidade química.

Notação 0 mostra grupos condensados, não todos os H separados. Notação 1 omite C e H ligados a C, mantendo O/OH. Coordenadas são diagramação, não geometria medida. Grupos funcionais dos seis exemplos são metadados curados; o programa não os infere para estruturas gerais.

Quatro testes cobrem fórmulas e H por átomo independentes, balanço, 108 renumerações, três pares constitucionais e grafos inválidos. Os seis resultados foram comparados ao JavaScript; doze estados visuais (três pares × duas estruturas × duas notações) também verificados automaticamente.

Fontes consultadas em 16/10/2026:

- [McMurry/OpenStax 1.12](https://openstax.org/books/organic-chemistry/pages/1-12-drawing-chemical-structures): convenções de representação.
- [McMurry/OpenStax 3.1](https://openstax.org/books/organic-chemistry/pages/3-1-functional-groups): definições dos grupos.
- Brown/Poon, sexta edição, exemplar 2016 já identificado no acervo: sumário conferido neste bloco inclui isomeria constitucional, sem declarar capítulo integralmente lido.

Júpiter CCM0224 e IUPAC apareceram indexados, mas não abriram diretamente neste bloco; não apresentados como leituras integrais novas. As limitações do mapa e referências editoriais foram preservadas. Texto, exemplos, gráficos, exercícios e código originais com apoio de IA; figuras, enunciados e tabelas das fontes não foram reproduzidos. Revisão de Jhuann pendente.
