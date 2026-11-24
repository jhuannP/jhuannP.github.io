# Instâncias, referências e atualização de estado

Aula `classes-estado`, ampliada para 12 seções/12 exercícios. Rascunho original para revisão pessoal. Preserva IDs, exemplo do MRU e desafio do contador; não representa experiência de pesquisa realizada.

## Ideia central

Uma instância reúne estado e operações. `r=p` associa outro nome ao mesmo objeto; outra chamada ao construtor cria outra instância. `avancar` altera posição, mantém velocidade e retorna `None`. Não atribuir esse retorno ao nome da partícula quando se pretende continuar usando o objeto.

O modelo é MRU em uma dimensão, com SI informado pelo usuário. Entradas são `int`/`float` nativos finitos, convertidos a float; bool/texto/complexos e outros tipos ficam fora do contrato. Um resultado pode transbordar mesmo com entradas finitas: o método verifica a posição candidata antes de alterar o estado. Campos continuam públicos; reatribuição externa contorna o contrato. Não se promete encapsulamento, concorrência ou tratamento de forças.

## Fontes

Sedgewick e Wayne, *Computer Science*, ©2017, §3.2 pp.382–384/PDF403–405: consulta textual parcial em 27/10/2026. O livro ensina Java e apresenta outro objeto; não se copiam implementação, figura ou exercício. Sem leitura integral ou nova inspeção visual do PDF. Exemplos e contrato em Python são próprios.

[Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html): trechos de §9.1 e §§9.3.2–9.3.5, inicialização, métodos, referências e atributos de classe/instância. Consulta parcial em 27/10/2026; sem afirmar leitura integral. Programa oficial da disciplina não reaberto; limites curriculares previamente documentados continuam válidos.

## Executar e interpretar

```sh
python3 labs/classes-estado/particle.py
python3 labs/classes-estado/test_particle.py
```

Seis testes: 729 casos contra a lei fechada com frações; 225 composições de tempo; alias/retorno; entradas rejeitadas; transbordamento da multiplicação e da soma sem alteração de estado; histórico compartilhado versus próprio. A grade usa pequenos valores binários exatos, não prova igualdade geral entre operações float. A lei física, o contrato e a semântica das referências são justificados nas notas, não pelo número de testes.

Para revisar em vinte minutos, desenhe `p`, `q`, `r`, preveja os estados e explique `None` antes de executar. Depois provoque um passo inválido e um resultado infinito. Encapsulamento, cópia profunda e outros modelos físicos permanecem pendentes. Nenhum campo de aprendizagem pessoal foi preenchido.


## 27/10/2026 — classes e estado: instância, alias e falha de atualização

`classes-estado` ampliada de3 seções/2 exercícios para12/12, preservando IDs, exemplo MRU e desafio do contador. Explica inicialização, self, instâncias independentes, alias, retorno None e lista compartilhada. Código original validava argumentos, mas podia gravar posição infinita; agora usa float candidato, rejeita resultado não finito antes de alterar x. Entradas int/float nativos, sem bool ou texto; campos permanecem públicos e a preservação não protege contra reatribuição externa. Não se promete encapsulamento, transação concorrente, cópia profunda ou integração sob forças.

Fontes parciais em27/10/2026: Sedgewick/Wayne ComputerScience ©2017 §3.2 pp.382–384/PDF403–405, abstração/API/estado em Java, sem copiar a implementação ou nova inspeção visual. Python Tutorial cap.9, https://docs.python.org/3/tutorial/classes.html , trechos9.1 e9.3.2–9.3.5 sobre nomes, inicialização, métodos e atributos. Sem leitura integral ou nova consulta ao programa oficial. Exemplo MRU, código, figura e testes próprios.

Seis testes aprovados em `labs/classes-estado/test_particle.py`:729 casos contra lei fechada racional,225 composições de tempo, alias/retorno, entradas rejeitadas, transbordamento de produto/soma com preservação e propriedade da lista. Grade binária pequena escolhida para igualdade exata; não extrapolar para floats gerais.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou1 e aceitou7 para a posição via alias; documento390/390px, console sem erros observados. Figura inspecionada em `classes-estado-mobile.jpg`; viewport restaurada. Windows real, leitor de tela e revisão pessoal pendentes.

ComputaçãoI27 aulas/200 exercícios, cinco introduções curtas; nove grupos oficiais parciais preservados. Aula de criação de tipos integra o percurso do livro, sem criar novo grupo oficial por inferência. Global51 trilhas,574 aulas/5236 exercícios,144 introduções curtas; sem certificação de cobertura ou domínio. Próxima ação20min: prever p/q/r, None e estado após rejeição antes de executar. Próxima elaboração global: revisar uma lacuna de BiologiaIII/IV ou aprofundar uma introdução de FísicaIV após fontes, alternando áreas. Saldo semanal antes/depois67%; parada operacional65% preservada.
