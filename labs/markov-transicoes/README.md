# Markov: distribuição, convergência e primeira chegada

Expansão da aula existente. Três seções iniciais, IDs mk1/mk2, exemplo, Python, desafio e demonstração preservados. Rascunho original para revisão pessoal, sem domínio atual certificado.

## Hipóteses e conservação

Estado suficiente para P(Xn+1=j|Xn=i,história)=Pij quando a condição tem probabilidade positiva. Matriz homogênea: mesma regra a cada passo. P é estocástica por linhas; p é vetor linha. Atualização p′j=Σi pi Pij vem da probabilidade total. Entradas não negativas e soma_j p′j=Σi pi Σj Pij=1. A distribuição não é uma trajetória e os estados de uma trajetória não são independentes em geral.

## Modelo preservado e fórmula exata

P=[[4/5,1/5],[2/5,3/5]], início A. Se an=P(Xn=A), an+1=4/5 an+2/5(1−an)=2/5+2/5 an. A estacionária é π=(2/3,1/3). Subtrair2/3 dá en+1=(2/5)en e, por indução, an=2/3+(2/5)^n(a0−2/3). Para a0=1, erro=(1/3)(2/5)^n. Na distância de variação total de dois estados, metade da soma dos desvios absolutos é |an−2/3|.

n=2: a2=18/25; n=3 erro8/375>1/100; n=4 erro16/1875<1/100. Como o erro decresce, quatro passos são o primeiro instante dessa tolerância para esta condição inicial/modelo. Não é estimativa empírica nem validação de uma rede real.

Para P=[[1−α,α],[β,1−β]], α+β>0, πA=β/(α+β) e an−πA=(1−α−β)^n(a0−πA). Isso permite os testes de famílias sem usar um teorema geral não demonstrado.

## Estacionária não basta

Alternância determinística α=β=1 tem estacionária única(1/2,1/2), mas o início A alterna sem convergir. Identidade α=β=0 mantém qualquer distribuição e não tem estacionária única. A afirmação de convergência do exemplo positivo não deve ser transportada a qualquer matriz por mera normalização.

## Primeira chegada

TB=min{n≥1:Xn=B}, partindo de A. TB>n significa permanecer em A em todos os n passos, então P(TB>n)=(4/5)^n. Assim E[TB]=Σn≥0 P(TB>n)=1/(1−4/5)=5 passos. A identidade da soma de caudas vem de TB=Σn≥0 1{TB>n}; aqui os termos são não negativos e a série geométrica é convergente.

O modelo lento [[9/10,1/10],[1/5,4/5]] tem a mesma estacionária(2/3,1/3), mas primeira chegada média10 passos. Estado estacionário sozinho não determina tempos de chegada. Um passo não foi convertido em segundo; sem calibração não há duração física prevista.

## Código e custo

`python3 labs/markov-transicoes/chain.py`

`python3 -m unittest discover -s labs/markov-transicoes -t .`

Frações racionais exatas, 1–8 estados e0–100 passos. Valida forma quadrada, não negatividade, somas exatas e dimensão de p; rejeita float sem convertê-lo silenciosamente. Entrada preservada. A rotina step geral propaga qualquer matriz no contrato; estacionária/primeira chegada são auxiliares APENAS para dois estados com hipóteses declaradas. Não resolve o problema geral de primeira passagem.

Cada passo denso usa ordem m² operações aritméticas e o histórico n+1 vetores usa ordem nm entradas. Fraction aumenta tamanhos de inteiros ao longo do tempo: essa contagem não é análise completa de custo em bits ou benchmark. Não coletamos dados nem ajustamos transições.

Quatro testes: somas de caminhos explícitos para dois inícios e passos0–6;675 distribuições comparadas com fórmula fechada (25 matrizes×3 inícios×9 instantes); alternância/identidade, primeira chegada e dois modelos de mesma estacionária; contratos e preservação da entrada. Não substituem demonstração nem revisão individual.

## Fontes e contexto curricular

Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, exemplar com copyright2017/ISBN978-0-13-407642-3 (arquivo e referências anteriores usam2016), §1.6: pp.179–180/PDF200–201, Mixing a Markov chain, consulta textual parcial em29/10/2026 para multiplicação, dois passos e vetor–matriz; p.174/PDF195 consultada parcialmente para distinguir trajetória simulada. Sem nova inspeção visual ou leitura integral. Código Java, rede, números e exemplos do livro não foram copiados; usamos a rede sintética já existente e demonstrações próprias. As páginas públicas Princeton Java/Python retornaram403 nesta consulta e não foram usadas como evidência de leitura.

É estudo editorial de programação com listas, matrizes e laços, não um item isolado afirmado da ementa ministrada. Programa e histórico de ComputaçãoI permanecem com versão posterior à turma e limites anteriores. PDF privado não distribuído. Próxima revisão pessoal: explicar a orientação de pP, reconstruir a recorrência e diferenciar probabilidade em n de primeira chegada até n.
