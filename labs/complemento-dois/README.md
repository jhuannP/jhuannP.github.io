# Complemento de dois: soma, carry e overflow

22/10/2026. Rascunho original para revisão de Jhuann. Modelo lógico, sem circuito físico ou dados profissionais.

## Fonte

Sedgewick e Wayne, *Computer Science: An Interdisciplinary Approach*, exemplar com copyright Pearson 2017, ISBN 978-0-13-407642-3. Consulta parcial ao §6.1, páginas impressas 886–888/PDF 907–909, por extração local: representação negativa, faixa, soma e negação. O trecho de ponto flutuante na última página não fundamenta este recorte. O nome 2016 do arquivo não prova ano editorial. Não se reproduzem tabelas, figuras, exercícios ou código do livro; o somador e o traçado por carries são próprios. A notação do livro usa n para largura; a aula usa w.

## Contrato

Entradas A e B são padrões inteiros 0–15. Modelo de quatro bits, complemento de dois e carry inicial c₀=0. A palavra armazenada é (A+B) mod 16; sua leitura com sinal pertence a −8…7. Carry é a saída para o quinto bit na soma sem sinal. Overflow indica que a soma matemática das leituras com sinal não cabe. A implementação monta cada coluna de bit; não usa a tabela de referência para calcular resultados.

Exemplos de flags:

| A | B | Leituras com sinal | Palavra | Carry | Overflow |
|---:|---:|---|---|---:|---|
| 7 | 1 | 7+1 |1000|0|sim|
|15|1|−1+1|0000|1|não|
|8|8|−8+(−8)|0000|1|sim|
|1|1|1+1|0010|0|não|

Cálculo de carries: a coluna i recebe cᵢ e produz cᵢ₊₁. A tabela mostra bits da esquerda para a direita, 3 a 0; a conta é feita da direita para a esquerda. O critério V=c₃ XOR c₄ vale para essa adição. A aula deriva Smatemática−Sguardada=16(c3−c4), distinguindo prova algébrica de inspeção de exemplos.

Python int não se torna inteiro de quatro bits; a redução é explícita. Nenhuma promessa de semântica universal de overflow em Java, C, JavaScript ou bibliotecas numéricas. O modelo não calcula tensões, atrasos elétricos, consumo, flags de um processador real ou construção de chip. Negar o mínimo −8 gera o mesmo padrão 1000 porque +8 não cabe; a identidade modular não cria um valor representável.

## Executar e conferir

Na raiz do protótipo:

```sh
python3 labs/complemento-dois/experiment.py
python3 -m unittest discover -s labs/complemento-dois -t .
```

Quatro testes: todos os 256 pares contra divisão/resto e interpretação; três critérios de overflow (faixa, sinais e XOR dos carries); negação nos 16 padrões e quatro combinações de flags; contratos inválidos. API rejeita bool, float e valores fora da faixa. JSON contém 256 referências produzidas por aritmética modular, separadas da implementação bit a bit; todas confrontadas com JavaScript. Isso verifica exaustivamente o domínio finito de quatro bits, não todas as larguras nem hardware.

Aula 14 seções/12 exercícios, preservando os anteriores. Próximas lacunas: extensão de sinal, subtração com empréstimo, outras larguras, contratos de bibliotecas e integração com programas M8. As demais introduções da trilha continuam por aprofundar; revisão conceitual e pessoal pendente.


## Verificação final e continuidade

765 testes Python aprovados; suíte JavaScript com 279 demonstrações/837 cenários básicos e referências adicionais aprovada; 451 estruturas MathML conferidas. No navegador, casos 7+1 e 15+1 apresentaram flags distintas corretas; exercício de leitura −3 aceito. Tela 390 px sem transbordamento horizontal e sem erros de console observados; viewport restaurado. Prévia `complemento-dois-mobile.jpg` na raiz do protótipo.

Percurso complementar: 20 aulas/60 exercícios, 18 introduções curtas e dois recortes desenvolvidos; não é a disciplina CCM0128. Catálogo geral 487 aulas/2547 exercícios. Próxima revisão: reconstruir o XOR dos carries e explicar por que negar o mínimo não cria um oposto representável. Próxima alternância global: revisar cobertura de Matemática III. Saldo semanal após o bloco: 74%; parada em 65%.
