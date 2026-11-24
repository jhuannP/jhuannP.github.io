# Naive Bayes Bernoulli: informação repetida e suavização

22/10/2026. Notas de aula e implementação originais com apoio de IA. Rascunho para revisão de Jhuann; não são avaliação pessoal, pesquisa ou demonstração com dados de cliente.

## Pergunta e pré-requisitos

Depois de condicionar em um evento e normalizar uma posterior, como estimamos seus fatores a partir de um treino? Retome pe-condicional, pe-bayes e ml-separacao-vazamento. O recorte abre estimação Bernoulli e o efeito de copiar atributos. Não pretende resolver todas as distribuições condicionais discretas.

A aula ml-naive-bayes preserva as três seções e duas questões iniciais e passa a 13 seções/12 exercícios. O primeiro exemplo continua sendo uma normalização elementar; o treino abaixo é outro exemplo, identificado no texto.

## Modelo

Y pertence a {0,1}, X é um vetor de bits inteiros. fit exige as duas classes presentes no treino. Para cada classe, N_c é sua contagem, n_jc conta valores 1 da coluna j. Prior N_c/N, sem suavização de classe. Probabilidade de 1: (n_jc+alpha)/(N_c+2alpha); de zero: seu complemento. alpha é int/Fraction não negativo, incluindo zero. O denominador 2alpha decorre das duas categorias possíveis, não do número de colunas.

A fatoração conjunta de todos os atributos condicionada à classe é uma hipótese. Independência apenas aos pares é insuficiente em dimensão maior que dois. Para cada consulta, multiplique prior por todos os fatores, inclusive os dos atributos zero, e normalize pela soma das duas classes. Evidência de massa zero sob o modelo devolve None; não inventa posterior uniforme.

## Exemplo reconstruível

- Classe 0: quatro linhas (1,1), uma (0,0).
- Classe 1: uma linha (1,1), quatro (0,0).
- Priors 1/2, ambas as colunas são cópias.
- Conjunta empírica: para observar (1,1), quatro das cinco linhas selecionadas são classe 0. Posterior 4/5.
- Sem suavizar: likelihoods do Naive Bayes 16/25 e 1/25; scores 8/25 e 1/50; posterior 16/17.
- alpha=1: probabilidades de 1 são 5/7 e 2/7. Scores 25/98 e 4/98; posterior 25/29.
- Com uma coluna e alpha=1, a posterior seria 5/7. Suavizar não desfaz cópias ou garante calibração.
- A consulta (1,0) tem massa empírica zero, mas massa positiva no modelo fatorado sem suavização. Ele dá posterior 1/2, não uma estimativa da condicional empírica indefinida.

O diagrama sinal-duplicado.svg é original, sem reproduzir figura dos livros.

## Execução e contratos

Na raiz do site, somente biblioteca padrão:
    python3 -m labs.naive-bayes-binario.experiment
    python3 -m unittest discover -s labs/naive-bayes-binario -t .

O módulo aceita matrizes não vazias, retangulares, de listas/tuplas; classes e atributos inteiros 0/1, sem bool. Modelo imutável retornado por fit; posterior espera esse estado. Não constitui uma API de desserialização/validação de modelos arbitrariamente construídos à mão. Não há limiar de decisão, seleção de alpha, log-score, validação externa ou estatísticas de calibração implementados. Nenhum pacote foi instalado.

Cinco testes: duplicação versus contagem conjunta; 64 treinos completos × três valores de alpha × quatro consultas (768 casos) com fatores obtidos por contagem direta de zeros/uns; normalização do modelo fatorado e papel da ausência; invariância por permutação, réplica de dados e pseudocontagens, e preservação de entradas; contratos e massa zero. Repetir dados mantendo alpha fixo não preserva necessariamente o modelo suavizado; o teste escala ambos.

## Fontes e limites da consulta

Base dos livros do Magalhães reconferida na continuação anterior: Noções de Probabilidade e Estatística, 7ª ed., §2.2 pp.56–58/PDF71–73; Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3 p.35/PDF22 (página dupla). Leitura parcial sobre independência, partições e independência condicional; não os apresentamos como fonte de um treinamento de Naive Bayes ou deste conjunto sintético.

Nova consulta primária em 22/10/2026: https://scikit-learn.org/stable/modules/naive_bayes.html, introdução §1.9 (fatoração e posterior normalizada) e §1.9.4 (Bernoulli, incluindo ausências). O guia mostra outras famílias, não implementadas aqui. Não afirmamos equivalência à API ou aos padrões numéricos da biblioteca. A página consultada identifica documentação 1.9.1; isso não indica uma versão instalada. Alpha aditivo binário foi derivado acima; nenhum texto, treino ou exercício de fonte externa foi reproduzido.

## Continuidade

Próxima revisão pessoal: reconstituir 4/5, 16/17 e 25/29 sem o programa e explicar por que acerto de classe não comprova calibração. Próximo preparo global: retornar às lacunas de Biologia III, evitando aprofundar indefinidamente a mesma trilha. Distribuições condicionais discretas gerais, famílias não binárias e avaliação externa continuam pendentes.

Verificação do bloco: 864 testes Python aprovados, incluindo catálogo, exemplos e laboratórios; cinco testes novos de Naive Bayes cobrem 768 consultas/treinos por contagem independente e demais invariantes. Corrigida uma conversão do teste de unidades no laboratório de actina ainda em preparação (Q(c)/1000000 em vez de float); modelo biológico não foi alterado ou publicado como aula. No navegador, 25/29 aceito na questão7; figura móvel legível a390px, sem transbordamento horizontal ou erro de console observado. Prévia naive-bayes-binario-mobile.jpg. Nenhum JavaScript ou MathML alterado, suítes correspondentes não repetidas. Catálogo493 aulas/2770 exercícios,289 introduções com até3seções. Saldo96%, parada65%. Próxima revisão pessoal: reconstruir as três posteriores e os denominadores. Próximo bloco global: retomar lacunas de Biologia III e o laboratório de actina ainda sem aula integrada.
