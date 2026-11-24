# Gram–Schmidt: ortogonalização racional e resíduo nulo

22/10/2026. Rascunho original para revisão de Jhuann, sem dados ou resultados da IC.

## Fonte e propriedade curricular

Apostol, *Cálculo*, volume II, original de segunda edição, tradução portuguesa Reverté 1996/reimpressão 2004, §1.14, páginas impressas 25–27/PDF 43–45, consultado parcialmente por extração local. Construção, preservação do espaço e resíduo nulo fundamentam o texto próprio. As páginas 25 e 26 foram lidas no recorte; a discussão inicial de 27 sobre dependência também. Páginas 28–31 foram extraídas junto, mas exemplos do livro, polinômios e decomposição posterior não são material desta aula. Sem leitura integral ou cópia de figuras/exercícios. Apostol é apoio complementar ao mapa de Matemática III; sua presença na bibliografia oficial de Matemática IV não o torna automaticamente referência oficial de III.

## Algoritmo e contrato

`orthogonalize` recebe uma família não vazia de vetores list/tuple de mesma dimensão positiva, com coordenadas int/Fraction; bool e float são rejeitados. Produto interno usual, vetores reais racionais. O algoritmo subtrai projeções nas direções ortogonais anteriores, conserva vetores não normalizados e descarta resíduos exatamente zero, registrando índices na lista skipped (base zero). Uma família só de zeros retorna base vazia do subespaço {0}. Não estima posto numérico ou tolerância.

`model(t)` limita t a int/Fraction em quartos entre −2 e 2. Família v1=(1,1),v2=(1+t,1−t); projeção=(1,1), resíduo=(t,−t), norma²=2t², determinante=−2t. Em t=0 a dimensão é 1 e q2=None; fora disso é 2, q1=(1,1)/√2 e q2=sgn(t)(1,−1)/√2. Só a normalização da família visual usa ponto flutuante. O JavaScript aceita os números de quarto de unidade correspondentes; não executa o algoritmo racional geral.

O gráfico usa escalas cartesianas iguais e fixas de −2,5 a 3,5 em ambos os eixos. Azul é v2; tracejado preto é v1 e a projeção; roxo é o resíduo na origem e seu traslado pontilhado da projeção até v2. Pontos azuis marcam extremos; segmentos são vetores, não trajetórias. Em t=0 os vetores iniciais coincidem. Não é análise de estabilidade por simulação de ruído.

## Verificação

Na raiz do protótipo:

```sh
python3 labs/gram-schmidt-exato/experiment.py
python3 -m unittest discover -s labs/gram-schmidt-exato -t .
```

Quatro testes: 625 pares de vetores inteiros em {−2,…,2}², com posto por determinante e reconstrução de cada entrada pela projeção na base produzida; 17 parâmetros da família visual, incluindo normalização/singularidade; ordem, entradas nulas/redundantes e coordenadas racionais em três dimensões; contratos inválidos. JSON contém 17 referências racionais para a família, confrontadas com JavaScript. Testes finitos não substituem a prova geral por ortogonalidade e duas inclusões do espaço, apresentada na aula.

Aula 14 seções/12 exercícios. Faltam produto interno complexo, análise de estabilidade, reortogonalização, Householder e problemas integradores de mínimos quadrados. Dependência exata não fornece tolerância universal para dados de máquina; revisão conceitual e pessoal continua pendente.


## Verificação final e continuidade

769 testes Python aprovados; suíte JavaScript com 280 demonstrações/840 cenários básicos e referências adicionais aprovada; 453 estruturas MathML conferidas. Navegador: t=0 identificado como resíduo nulo sem divisão, exercício de dimensão aceitou 1 e t=0,5 mostrou reconstrução geométrica. Largura 390 px sem transbordamento horizontal e sem erros de console observados; viewport restaurado. Prévia `gram-schmidt-mobile.jpg` na raiz do protótipo.

Álgebra linear: 18 aulas/101 exercícios, dez introduções curtas e oito recortes desenvolvidos. Percurso reconciliado em sete etapas com 18 aulas próprias e cinco apoios, todos uma vez. Nove grupos de Matemática III continuam parciais. Catálogo geral 487 aulas/2557 exercícios. Próxima revisão: prova de preservação do espaço e tratamento da redundância; próxima alternância global: cobertura de Física III. Saldo inicial 74%; duas consultas finais informaram 100% restante na janela de 10080 minutos, com resetsAt=1793293778, diferente da leitura inicial. Nenhum resgate ou alteração de limite foi executado; não se infere a causa da mudança. Parada operacional em 65% permanece.
