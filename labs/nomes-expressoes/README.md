# Nomes, tipos e expressões — laboratório guiado

Antes de executar, preveja o resultado de cada bloco. Atribuição calcula uma expressão naquele momento; reatribuir um nome não faz outros cálculos se atualizarem. Mudanças numa lista compartilhada são outro mecanismo. O exemplo de unidades pressupõe movimento uniforme e não usa dados medidos.

## Fontes oficiais parcialmente consultadas —27/10/2026

- [Tutorial Python3.14 §3.1](https://docs.python.org/3.14/tutorial/introduction.html): números, textos, expressões e atribuição.
- [Data Model§3.1 e3.2.4](https://docs.python.org/3.14/reference/datamodel.html): objeto, identidade/tipo/valor, mutabilidade e bool/int.
- [Expressions](https://docs.python.org/3.14/reference/expressions.html): divisão e precedência de potência/sinal.
- [Floating Point§15](https://docs.python.org/3.14/tutorial/floatingpoint.html): aproximação binária, impressão e comparações.
- [math.isclose/isfinite](https://docs.python.org/3.14/library/math.html): tolerância relativa/absoluta e finitude.

Recortes conceituais, sem leitura integral ou cópia da sequência dos exemplos. O traço de minutos/segundos, figura, encadeamento e exercícios são próprios. Sedgewick/Wayne§1.2 permanece referência temática de programação; não houve nova leitura do livro, nem transferência silenciosa de semântica Java para Python.

## Execução

Na raiz: `python3 labs/nomes-expressoes/experimentos.py`.

Somente biblioteca padrão. O programa informa a versão local, que pode diferir da série3.14 da documentação. A parte de float declara representação binária e interrompe se essa hipótese não valer. Sem input, eval, acesso à rede ou arquivos externos. Os assert são checagens dos exemplos, não uma biblioteca de validação geral ou prova de domínio do leitor.

Conferir estados(2,120),(3,120),(3,180); reatribuição/mutação;12 expressões com valor e tipo; TypeError/ValueError esperados; bool versus int; float e comparação tolerada; finitude; conversão de2min a120s e deslocamento360m. O script reúne referências executáveis para comparar as previsões do leitor com os resultados.

Próxima revisão de20min: traçar os três estados e explicar as duas divisões; depois converter unidades e justificar a comparação de float. Tipos personalizados, escopos, unidades automáticas, leitor de tela, Windows real e revisão pessoal pendentes.


## 27/10/2026 — verificação de nomes, tipos e expressões

Consolidada a elaboração previamente existente de `variaveis-tipos`, ampliada de3 seções/2 exercícios para14/12. Atribuição, reatribuição versus mutação, valor/tipo de expressões, divisão inteira com negativos, precedência, conversões, erros esperados, bool/int, aproximação binária e tolerância absoluta/relativa. Figura e laboratório próprios em `labs/nomes-expressoes/`. Exemplo de unidades com movimento uniforme e grandezas declaradas, sem dados reais. Preservados exemplo, código, desafio e identificadores anteriores. ComputaçãoI:27 aulas/160 exercícios e9 introduções curtas, ainda com cobertura curricular parcial e revisão pessoal pendente.

Referências públicas parcialmente consultadas no bloco de elaboração: documentação Python3.14, Tutorial§3.1 e§15, Data Model§3.1/3.2.4, Expressions (divisão/precedência), math.isclose/isfinite. Links no README do laboratório. Nesta continuação foram conferidos os registros e executados os exemplos, sem nova consulta dessas páginas. Sedgewick/Wayne§1.2 é referência temática; sem nova leitura do livro ou transferência de semântica Java para Python. Sem afirmação de domínio de Jhuann.

Verificação desta continuação:14 testes do catálogo aprovados; script guiado executado emPython3.14.5, com12 expressões de valor/tipo, estados(2,120),(3,120),(3,180), mutação/reatribuição, erros esperados, comparação tolerada e conversão de unidades. Não são19 testes: o script é um conjunto de exemplos executáveis. Conferidas819 estruturas MathML do catálogo. No navegador, exercício5 rejeitou180 e aceitou120 porEnter. Documento sem transbordamento em320/320px e390/390px; console sem erros observados. Figura inspecionada em `nomes-expressoes-mobile.jpg`. O ajuste previamente adicionado de quebra de texto no legend do exercício foi preservado; a verificação anterior havia identificado420px de documento para390px de tela e confirmado390px após o ajuste. Windows real e leitor de tela não testados.

Estado global atual:51 trilhas,550 aulas/4453 exercícios e191 introduções curtas, incluindo a extensão de probabilidade feita no bloco anterior. Contagens não provam conclusão do curso. Próxima revisão pessoal20min: prever os três estados sem executar, justificar −7//3 e distinguir mudança de nome de mutação de lista. Próxima elaboração global: auditar o somador de ComputaçãoII cuja verificação/registro final ficou pendente, antes de ampliar outra aula. Saldo semanal79%; parada operacional65% preservada.
