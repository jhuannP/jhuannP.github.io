# Escalas gráficas — roteiro original

29/10/2026. Rascunho assistido por IA; revisão de Jhuann pendente.

## Pergunta e pré-requisitos

Qual transformação torna uma relação prescrita linear? Funções, logaritmos e unidades são pré-requisitos. Sem dados de bancada, ajuste ou validação experimental.

## Tabelas sintéticas

| t (s) | posição (m) | tensão (mV) | tensão com fundo (mV) |
|---|---|---|---|
|0|2|64|69|
|2|8|32|37|
|4|14|16|21|
|6|20|8|13|

A figura linear usa os tempos 0,1,2 s com posições 2,5,8 m, do mesmo modelo x=2+3t. O monolog usa log₂(tensão / 1 mV). No exemplo de potência, distância 1,2,4,8 cm e força 3,12,48,192 mN; ambos eixos transformados com referências 1 cm e 1 mN.

1. Refaça inclinações lineares e logarítmicas por dois pontos.
2. Obtenha meia-vida 2 s, taxa natural −ln2/2 s⁻¹ e expoente 2.
3. Mostre que as razões de 69,37,21,13 não são constantes. Subtrair fundo requer conhecimento independente e propagação da sua incerteza.
4. Compare erros absolutos 2−1 e 11−10 com ln2 e ln1,1. Ajustar depois do log muda o objetivo; ruído e pesos não ficam automaticamente adequados.
5. Escreva o que faltaria num relatório real: procedimento, unidades, dados íntegros, instrumentos, incertezas, modelo de erro, diagnóstico e limites.

Logaritmos usam razões sem dimensão; y>0 no monolog, x,y>0 no dilog. Zero no tempo é permitido no monolog. Não excluir pontos nem somar offset arbitrário para tornar o log possível.

## Código e verificação

Na raiz do protótipo:

```sh
python3 labs/escalas-graficas/scales.py
python3 -B -m unittest discover -s labs/escalas-graficas -t .
```

`coordinates` transforma dados finitos, não altera a lista e não ajusta modelos. `secants` calcula inclinações consecutivas; abscissas iguais são rejeitadas. Os exemplos são modestos: não há promessa de estabilidade para toda entrada extrema de ponto flutuante. Quatro métodos de teste: 36 comparações de log por Decimal com 60 dígitos; 45 combinações de amplitude/expoente/base e mudança coerente de unidades; offset/resíduos; contratos. São testes de cálculo, não validação metrológica/pedagógica.

## Fontes efetivamente consultadas

- [AMSI, Logarithmic plots](https://amsi.org.au/ESA_Senior_Years/SeniorTopic3/3e/3e_4history_4.html), corpo parcial em 29/10/2026: linearização exponencial/potência e limites empíricos. Não reproduzimos dados históricos ou figura.
- [NIST/SEMATECH, Scatter Plot: Exponential Relationship, §1.3.3.26.6](https://www.itl.nist.gov/div898/handbook/eda/section3/scatter6.htm), corpo parcial em 29/10/2026: modelo exponencial com offset e inadequação de reta simples. Sem usar CHWIRUT2.
- Programa 4302113: mapeamento indexado em 16/10 já registrado no catálogo. Abertura de uspdigital em 29/10 falhou; não é uma nova conferência do corpo ou da versão de 2023.

Bibliografia efetivamente adotada na turma e exemplar correspondente ainda não auditados. Estas são referências complementares públicas. Equações com referências dimensionais, exemplos, deduções de perda e testes são elaboração própria para revisão, não transcrição de um livro.
