# Módulos, contratos e testes

Rascunho original de22/10/2026, revisão pessoal pendente. Aprofunda aula existente `modulos-contratos`:14seções/12exercícios, preservando IDs mc1/mc2, exemplos usuais e desafio de amplitude, com validação ampliada. Não é resultado de pesquisa ou comprovação de domínio.

## Arquivos e execução

Baixe estatisticas.py e cliente.py para a mesma pasta; execute `python3 cliente.py` (saída4.0). A biblioteca define media; o cliente importa, fornece dados e imprime. O bloco __main__ evita imprimir a demonstração ao importar. Não nomeie arquivos locais math.py ou fractions.py. Windows pode usar `py` ou `python`, conforme instalação, no lugar de python3. Nenhuma integração de dispositivo foi presumida ou implementada.

Na raiz do protótipo: `python3 -m unittest discover -s labs/modulos-contratos -t .`. Para estudo isolado, baixe também test_estatisticas.py e execute `python3 -m unittest test_estatisticas.py` na pasta dos três arquivos; o teste aceita import como módulo isolado e como parte do protótipo. Somente biblioteca padrão.

## Contrato e escolha numérica

media aceita exatamente list não vazia de tipos embutidos int/float, cada elemento convertível para float finito; rejeita bool, texto, tupla, gerador, NaN, infinito e inteiros fora da conversão finita com ValueError. Não altera a lista nem imprime/lê na função. Inteiros são acumulados como inteiros exatos; floats como seus valores binários recebidos. A média racional é convertida uma vez para float. Escolha de referência didática mais cara, não promessa de desempenho para produção. Não recupera exatidão decimal perdida antes da chamada. A amplitude pode ultrapassar o intervalo float mesmo com entradas válidas; a solução do desafio sinaliza OverflowError.

Quatro testes:780sequências por referência Decimal de1100dígitos, extremos/subnormais/cancelamento e imutabilidade; entradas inválidas; import silencioso, cliente e validação em subprocesso com -O; tolerâncias perto de zero. As validações não usam assert; asserções demonstrativas são auxiliares.

## Fontes consultadas parcialmente

Sedgewick/Wayne, *Computer Science: An Interdisciplinary Approach*, §2.2 pp.226–228 (PDF247–249): modularidade, bibliotecas e clientes em Java. Exemplar local nomeado2016, identificação editorial ainda pendente conforme registro anterior. Não se atribuem ao livro a implementação Python, contrato numérico ou política de erros deste projeto; nenhum programa/figura/PDF transcrito.

Documentação oficial consultada em22/10/2026:
- [Módulos e execução como script](https://docs.python.org/3/tutorial/modules.html): import, __name__ e busca de módulos.
- [Fraction](https://docs.python.org/3/library/fractions.html): valor exato de um float recebido não é necessariamente a fração decimal pretendida.
- [math.isclose](https://docs.python.org/3/library/math.html#math.isclose): tolerâncias relativa/absoluta e comportamento perto de zero.

Consulta parcial; não implica que a versão web da documentação é a versão instalada. O código usa operações antigas da biblioteca padrão, verificadas no runtime local.

Próxima ação pessoal: executar o cliente, prever as entradas rejeitadas e explicar por que assert não é a validação pública. Pendentes: outros formatos de entrada, CSV, unidades físicas, desempenho, empacotamento e publicação; nenhum deles foi implementado neste recorte.

Verificação final:720testes Python e418MathML aprovados, catálogo12testes; execução isolada e como pacote conferidas após ajuste de import. Browser:1/3aceito, zero rejeitado e1e−12aceito para tolerância, recursos presentes;390px sem overflow horizontal e console sem erros observados. Prévia `modulos-contratos-mobile.jpg` na raiz. Viewport restaurado. Saldo77%; parada65%; rascunho para revisão pessoal.
