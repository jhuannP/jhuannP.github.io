# Inequações lineares: conjunto solução e reta

Rascunho original de 22/10/2026, para revisão de Jhuann e preparação de reforço geral. Mantém a unidade `em-inequacoes`, o exemplo −2x<6, os dois IDs anteriores e o desafio de conferência numa grade. Python permanece opcional.

## Referência

OpenStax, *Elementary Algebra 2e*, §2.7: https://openstax.org/books/elementary-algebra-2e/pages/2-7-solve-linear-inequalities . Consulta direta parcial em 22/10/2026 a conjunto solução/reta e propriedades de adição/subtração e multiplicação/divisão por sinal conhecido. Não se leu integralmente a seção, nem se copiaram figuras, exercícios ou exemplos resolvidos. Números, exemplos e diagramas do protótipo são próprios. Não há leitura de PDF privado ou alegação de cobertura de um exame específico.

## Algoritmo e prova

Família ax+b □ c com coeficientes constantes reais e □ em <,≤,>,≥. Separar a>0, a<0, a=0 antes de dividir. Para a≠0, a fronteira q=(c−b)/a e o operador isolado determinam uma semirreta aberta ou fechada. Para a=0, avaliar b □ c decide entre ℝ e ∅, sem fronteira. A justificativa algébrica usa operações reversíveis; testar valores não substitui essa prova.

`experiment.py` usa int/Fraction, rejeita bools/floats/entradas não racionais e não limita os coeficientes à faixa visual. O painel é uma exploração finita: a de −3 a 3, b de −4 a 4, c de −6 a 6 inteiros, operador escolhido em quatro posições, ponto de teste em meios inteiros de −8 a 8. Dentro dessa faixa todas as fronteiras ficam em [−10,10]; a janela desenhada é [−12,12]. A solução descrita é global e as setas continuam além da janela. No JS, a expressão do ponto é multiplicada por 2 para usar inteiros exatos; a fronteira tem representação fracionária exata e posição gráfica numérica.

O ponto de teste fica acima da reta, conectado por linha tracejada, para não ocultar a fronteira. ℝ aparece como toda a reta visível com setas em ambos os sentidos; ∅ não recebe segmento azul. O desenho não é método de amostragem para descobrir a solução. Frações exatas, pontos abertos/fechados, intervalo e relatório textual comunicam a mesma condição.

## Executar

```sh
python3 labs/inequacoes-reta/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: expressão original comparada à solução simbólica em 3276 configurações e 49 pontos racionais; fronteira e dois lados; casos constantes e operação não reversível por zero; contratos e coeficientes racionais. 108 estados cruzam Python/JS em 324 pontos, incluindo todos os operadores e coeficiente zero. A grade confere casos; a prova de equivalência é a análise algébrica apresentada na aula.

Fora do painel: a aula demonstra por casos o perigo de multiplicar por variável de sinal desconhecido em 1/x<1, com domínio x≠0. O solver não é anunciado como algoritmo geral para quocientes. Também não resolve automaticamente produtos, módulo, sistemas, desigualdades compostas ou restrições de contexto. Próxima expansão local depende de referências e nova sequência própria.


22/10/2026 — Inequações aprofundadas: 14 seções/12 exercícios, reta interativa, fronteiras e casos constantes, mantendo IDs/exemplo. Fontes parciais e limites em labs/inequacoes-reta/README.md. 606 testes Python, 245 demos/735 cenários, 108 referências e 339 MathML aprovados; UI inclusive/estrita/ℝ/∅, exercícios e 390 px conferidos. Matemática escolar 15 aulas/78 exercícios, cinco recortes desenvolvidos/dez introduções; catálogo 466 aulas/2130 exercícios em rascunho. Próxima ação: cobertura/roteiro de Física escolar. Revisão pessoal pendente; saldo 89%, parada 65%.
