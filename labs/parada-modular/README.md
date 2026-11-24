# Parada geral e família modular — notas de aula

Rascunho original assistido por IA, revisão pessoal pendente; não comprova domínio ou conclusão de curso. Percurso complementar próprio, sem equivalência com a disciplina CCM0128.

## Contrato e prova

H é hipotético: sempre termina, sempre acerta, todos os programas/entradas de um modelo universal sem limite fixo de memória. D recebe uma descrição de programa, consulta H sobre executar esse programa com a mesma descrição e faz o contrário da previsão. Ao fornecer a descrição de D a D, os dois casos contradizem H: prevê parada→D repete; prevê não parada→D termina. A prova rejeita a especificação completa, não análises particulares ou ferramentas que podem dizer não sei. Programas entram como cadeias finitas, não objetos mágicos; não se executa H neste projeto.

Simular até parar reconhece casos positivos, mas não responde a todos os negativos. Orçamento excedido não prova não término. Configuração completa repetida em dinâmica determinística sem novas entradas prova ciclo; repetir só PC ou uma variável não basta. Uma execução infinita de uma máquina com memória não limitada pode não repetir a configuração completa.

## Família original e derivação modular

Regra: x←(x+d)mod m; parar se x=0 antes de atualizar. m≥1, x,d em range(m), sem outras variáveis mutáveis. Após k atualizações x_k≡x₀+kd(mod m). Zero alcançável iff g=mdc(d,m) divide x₀. Necessidade: g divide kd e m. Suficiência: dividir a congruência por g torna d/g invertível módulo m/g. Primeiro k é o resíduo de −(x₀/g)(d/g)⁻¹ módulo m/g; inicial zero para imediatamente. Se não alcança zero, período m/g. São hipóteses e prova dessa família, não teorema geral sobre todos os programas.

Exemplos m6: x2,d4→0 após1; x1,d2→3→5→1, ciclo3. Módulo4 tem11 pares que param e5 que ciclam. Um limite de dois passos não vê a parada de x1,d1,m4; no terceiro ela ocorre. O código usa mdc/inverso modular em vez de enumerar, mas não trata custo de inteiros arbitrários como constante. Um espaço finito pode ser enorme em relação ao tamanho binário da entrada.

## Resoluções

Exercícios preservados cp1: não; cp2: ciclo apenas nessa dinâmica. Novos3–12:3 atualizações;1 atualização;período3;11 pares param;0 atualizações;D repete se H prevê parada;D termina se H prevê não parada;ferramenta com não sei tem contrato diferente;só PC não basta;família modular não resolve caso geral.

## Código e verificações

Mantidos exemplo, Python, desafio e IDs anteriores; novo `counter.py` aceita apenas inteiros sem bool, com faixa explícita. `Result` é congelado: status, primeiro tempo se para, período se cicla, divisor g. Estados iniciais zero retornam parada0, sem atribuir período a execução já terminada.

Na raiz do protótipo, Python3.10+ para as anotações de união:

```sh
python3 -m unittest discover -s labs/parada-modular -t .
```

Quatro testes:16 casos originais;oráculo de transições sem mdc ou inverso para todos x,d e m1até40;inteiros de101 dígitos com primeiro tempo conhecido e órbita enorme sem enumeração;contratos. Testes conferem o classificador restrito; não provam a indecidibilidade geral. O traçado completo não é armazenado no classificador.

## Fontes e limites

Sedgewick e Wayne, Computer Science: An Interdisciplinary Approach, exemplar com copyright Pearson2017 conforme metadados previamente conferidos. Nome do arquivo2016 não é o ano editorial adotado. §5.4 pp.808–810/PDF829–831 parcialmente consultado em27/10/2026; p.810/PDF831 visualmente conferida para os dois casos. Sem leitura integral de capítulo; discussão/exemplo de Collatz e exercícios não usados. Esquema, exemplos, código e prova modular originais; PDF privado não distribuído. A prova geral é exposta em notação contemporânea própria com descrição finita de programas. Não foi implementada uma U completa.

Faltam reduções, outros problemas indecidíveis, formalização completa da codificação e eficiência sistemática. H não existe com o contrato proposto; o laboratório tampouco é um verificador geral de software, agentes ou sistemas físicos. Código da família não faz chamadas externas ou executa programas recebidos.

## Registro pessoal

Data: ____ · prova reconstruída: ____ · dúvida: ____
