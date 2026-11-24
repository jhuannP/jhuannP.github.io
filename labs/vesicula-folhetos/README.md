# Lipídios, membranas e geometria dos folhetos

Rascunho didático original de 22/10/2026, pendente de revisão de Jhuann. Unidade conceitual com uma exploração geométrica; não é simulação de montagem molecular, experimento de laboratório ou evidência pessoal de domínio.

## Referências e limites da leitura

Nelson/Cox, *Princípios de Bioquímica de Lehninger*, sexta edição, Artmed 2014, original 2013, exemplar privado confirmado na auditoria de Biologia I. Consulta parcial nesta data: §10.2, trecho a partir de p. 362 e parte de p. 363 (PDF 392–393); §11.1, parágrafos de p. 387 e parte de p. 388 (PDF 417–418) sobre bicamada, agregados e vesículas. P. 387/PDF 417 renderizada e inspecionada visualmente. Extração mais ampla também incluiu pp. 364/386, mas não se afirma leitura completa ou uso integral. Figuras, exercícios, tabelas, dados de composição e espessuras do livro não foram reproduzidos ou convertidos em parâmetros do painel. A explicação usa texto, diagramas e exemplos próprios; PDFs privados não são servidos.

CCM0111, item 4: lipídios/micelas/lipossomos/membranas. Vínculo com programa diretamente reconferido na auditoria de 22/10/2026; não se reabriu o histórico ou se comprovou a versão ministrada. O tópico deixa de lacuna total e passa a parcial, sem declarar a disciplina completa. As doze lacunas, incluindo carboidratos, seguem pendentes.

## Modelo geométrico

Duas superfícies esféricas: cabeças internas no raio r, externas no raio r+d. d é separação geométrica escolhida, não inferência de espessura experimental. Áreas 4πr² e 4π(r+d)²; volumes da cavidade e da casca calculados com as mesmas superfícies. A razão de áreas é (1+d/r)². O painel usa r=10,…,100 nm em passos de 10 e d em {2,4,6} nm; a faixa não certifica estabilidade ou validade molecular em cada combinação.

A figura é um corte equatorial, mas as contas são de superfícies esféricas completas. Cabeças orientadas para água interna/externa e caudas para a casca. O mesmo número de símbolos esparsos em cada folheto é convenção de orientação, não contagem de moléculas, densidade ou empacotamento; dimensões dos símbolos não têm escala molecular. O raio gráfico externo é fixo para caber na tela; o interno varia pela razão r/(r+d). Isso não representa uma vesícula crescendo no tempo.

Somente com hipótese adicional de mesma área média por molécula em ambos os folhetos é possível converter razão de áreas em estimativa de razão de quantidades. A fração externa sob essa hipótese é (r+d)²/[r²+(r+d)²]. Não se especifica composição, assimetria química real, densidade ou área molecular experimental. O painel não calcula energia livre, formação, concentração crítica, permeabilidade, fluxo, potencial elétrico ou dinâmica.

## Explorar

```sh
python3 labs/vesicula-folhetos/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Para r=10,d=4 nm, áreas 400π e 784π nm², razão 1,96 e excesso relativo 96%; fração externa condicional 49/74. Para r=20,d=4 nm, razão 1,44; para r=100,d=4 nm, 1,0816. Aumentar r a d fixo aproxima a razão de 1. Escalar ambos os comprimentos por 2 mantém a razão, multiplica áreas por 4 e volumes por 8.

Quatro testes novos: integral independente de faixas esféricas com regra do ponto médio em 2000 subintervalos e fechamento de volumes; razões racionais e fração condicional; monotonicidade e escala; domínio e desigualdades geométricas. 30 estados de referência cruzam áreas, volumes e razões entre Python/JavaScript. Não há validação experimental de membranas nesses testes.

Próximos recortes: classes moleculares, condições de agregação e assimetria/dinâmica, com fontes específicas; carboidratos precisam de sequência própria. Transporte e proteínas de membrana não devem ser inferidos desta geometria. Revisão pessoal e o restante da disciplina permanecem pendentes.


22/10/2026 — Lipídios/membranas: nova unidade de 14 seções/12 exercícios, painel geométrico de vesícula, sem auto-organização ou transporte. Lehninger consultado parcialmente; limites em labs/vesicula-folhetos/README.md. 602 testes Python, 244 demos/732 cenários e 338 MathML aprovados; UI desktop/390 px, controles e respostas 1,96/49/74 conferidos. Biologia I 7 aulas/79 exercícios, sete tópicos parciais/doze lacunas. Catálogo 466 aulas/2120 exercícios em rascunho. Próxima ação global: conferir cobertura e roteiro de Matemática para ensino médio. Revisão pessoal pendente; saldo 89%, parada 65%.
