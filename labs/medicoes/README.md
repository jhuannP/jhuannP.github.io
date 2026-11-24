# Laboratório: medições e ajuste linear

Projeto original em Python 3 e português brasileiro, com biblioteca padrão. Os cinco dados de `measurements.csv` foram inventados para ensino; não são experimento ou evidência da IC. A tarefa é produzir uma saída auditável, não provar movimento retilíneo uniforme de um corpo real.

## O que receber e produzir

Entrada: CSV UTF-8 com cabeçalho exato `time_s,position_m`, pelo menos duas linhas, números finitos, tempos não negativos e estritamente crescentes. Essa ordem é um contrato didático; medições repetidas no mesmo tempo podem ser válidas em outros desenhos de coleta.

Saída: intercepto em m, inclinação em m/s, resíduos, SSE em m² e RMSE em m; relatório JSON com parâmetros, identidade dos dados e do código, versão de Python e declaração de origem.

## Como executar

Abra um terminal na pasta extraída. Com Python 3 disponível:

```sh
python3 analyze.py --input measurements.csv --source-kind synthetic
python3 analyze.py --input measurements.csv --source-kind synthetic --output meu-resultado.json
python3 -m unittest discover -p 'test_*.py'
```

No Windows, use o comando do Python 3 disponível no seu ambiente no lugar de `python3`, por exemplo `python` ou `py -3`, se configurados. Nenhum pacote externo é necessário.

O primeiro comando imprime o relatório; o segundo cria um arquivo novo e recusa substituir arquivo existente. `example-output.json` é uma referência já gerada. Hashes/versões podem diferir se código, dados ou ambiente mudarem.

## Etapas para construir sua versão

1. Leia o CSV e diga as unidades e o contrato em suas palavras. Observe que posição não precisa ser positiva.
2. Copie `starter.py` para um arquivo de trabalho e implemente o parser. Rejeite cabeçalho errado, campos ausentes, NaN/infinito, duplicatas e ordem inversa.
3. Calcule médias, soma de quadrados dos tempos centrados e soma cruzada. Use inclinação = soma cruzada / soma quadrática e intercepto = média de posição − inclinação × média de tempo.
4. Calcule cada resíduo observado − previsto, SSE e RMSE. Compare com as referências abaixo; confira soma dos resíduos e produto deles pelos tempos.
5. Separe cálculo da leitura/escrita. Preserve a lista original de medições; documente a interface.
6. Acrescente parâmetros de CLI e relatório. Registre origem e unidades; o hash identifica bytes, não valida cientificamente o arquivo.
7. Execute os testes. Tente uma reta exata crescente, uma decrescente, dados inválidos e tentativa de sobrescrever saída.
8. Em uma cópia, altere um ponto e compare o ajuste. Explique por que um ponto extremo pode influenciar OLS; não eliminar dados silenciosamente.
9. Escreva uma conclusão curta: que resultado o programa calcula, o que foi verificado e o que faltaria para analisar medições reais.

## Referências independentes

Para os cinco dados fornecidos:

- média de tempo = 2 s; média de posição = 5 m;
- soma quadrática de tempos centrados = 10 s²;
- soma cruzada = 19,8 m s;
- inclinação = 1,98 m/s; intercepto = 1,04 m;
- resíduos = −0,04; 0,08; −0,10; 0,12; −0,06 m;
- SSE = 0,036 m²; RMSE ≈ 0,0848528 m;
- soma dos resíduos e soma tempo×resíduo = zero até arredondamento.

Essas contas fornecem referência independente para o código. Repetir a implementação em um teste não seria tão informativo.

## Critério de conclusão do laboratório

A sua versão deve executar com o CSV, tratar os casos inválidos, preservar entradas, produzir unidades corretas, passar nas referências de reta e resíduos, e incluir instruções de execução e uma interpretação limitada ao ajuste. Compare os próprios resultados antes de olhar a implementação de referência `analyze.py`.

O ajuste é não ponderado com intercepto. Não há barras de erro, inferência de parâmetros, detecção de outliers, validação experimental ou modelo geral de dinâmica neste laboratório.

## Validação da entrada —27/10/2026

O cabeçalho também é lido dentro do tratamento de erros CSV: aspas incompletas nessa etapa geram ValueError e a CLI apresenta mensagem/status2, sem traceback ou ajuste parcial. A API parse_csv exige str. Os campos seguem a sintaxe de float e passam depois por finitude e domínio. Campo vazio não é zero; posições negativas são permitidas; linhas de dados inteiramente vazias após o cabeçalho são ignoradas pelo DictReader. CSV com outro delimitador ou nomes de campos não é convertido automaticamente.

Sete testes locais incluem cabeçalho malformado, ida e volta pelo writer com LF/CRLF, aspas, não finitos e perda de distinção temporal por underflow. O ajuste matemático permanece igual. example-output.json foi regenerado com os mesmos dados sintéticos e hashes atuais; a biblioteca de entrada/saída aponta para estas mesmas fontes.
