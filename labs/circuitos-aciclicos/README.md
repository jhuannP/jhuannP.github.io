# Circuitos combinacionais: dependência e função

28/10/2026. Notas e laboratório originais com apoio de IA; revisão pessoal pendente. Sem eletrônica física, clock, memória ou simulação temporal.

A rede tem entradas primárias e portas AND, OR, NOT e XOR. Cada nome tem um único produtor. Uma dependência referencia um sinal existente. Saídas podem ser entradas primárias. Sinais podem alimentar várias portas; não há custo de fan-out modelado. A rotina valida e avalia todas as portas declaradas, inclusive as que não alimentam as saídas. Ciclos em componentes desconectados também são rejeitados. Não há remoção de lógica morta nem otimização.

A construção própria u=A OR B, v=A AND B, w=NOT v, z=u AND w implementa XOR. A tabela em ordem 00,01,10,11 resulta em 0,1,1,0. A entrada11 diferencia OR de XOR. São quatro portas, com profundidades u=v=1,w=2,z=3, entradas no nível0. Uma XOR primitiva representa a mesma função com tamanho1/profundidade1 sob outra base de portas. Isso não compara área, consumo ou atraso reais.

O avaliador declara as portas em ordem invertida e procura as que têm dependências disponíveis. A cada rodada remove as prontas; numa rede finita acíclica sempre há uma. Valores únicos são justificados por indução sobre dependências. Se nenhuma porta estiver pronta, com nomes já validados, existe ciclo. A equação x=NOT x não tem ponto fixo binário; x=NOT y,y=NOT x tem dois, sem regra para selecionar estado. Ambos são rejeitados neste contrato combinacional.

Entradas e portas são dicionários; operações e nomes são strings; cada porta é uma tupla (operação, tupla de sinais); saídas são tupla não vazia. Bits estritamente int0/1; bool/float rejeitados. Até64 nós, limite didático. Pode haver portas repetindo uma mesma dependência. A entrada não é alterada. A busca da ordem por varreduras pode exigir O(G²) verificações com aridade limitada, embora cada porta seja calculada uma vez. Contadores e fila permitiriam outro algoritmo; não implementado aqui. Armazenamento linear no número de nós/arestas e avaliações booleanas de tamanho fixo, sem medição de runtime.

`gate_count` conta todas as portas declaradas. `output_depth` é o maior nível das saídas pedidas, podendo ser0 mesmo com portas não utilizadas. As camadas são agrupamentos de dependências, não paralelismo executado pelo Python, ciclos de clock ou nanosegundos.

Fonte privada: Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar com copyright Pearson2017, ISBN978-0-13-407642-3, arquivo nomeado2016. Consulta textual parcial em28/10/2026 de §7.2 pp.1002–1004/PDF1023–1025, sobre interfaces, conexões e modelo de fios/chaves. Sem leitura integral ou nova inspeção visual. Não equiparar essa abstração à implementação por portas destas notas, nem à TOY ou à M8. Provas, rede, figura e Python próprios; PDF não disponibilizado. Exemplo anterior de De Morgan, seu código e desafio preservados na aula.

Verificação: `python3 -m unittest discover -s labs/circuitos-aciclicos -t .` e `python3 labs/circuitos-aciclicos/network.py`. Quatro testes: XOR em4 entradas ×24 ordens de declaração, profundidades e preservação; De Morgan nas4 entradas e contraexemplo OR/XOR; base/fan-out/portas não utilizadas;14 contratos inválidos, incluindo ciclos. Testes finitos não substituem a prova de término/correção nem revisão conceitual.
