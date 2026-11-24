# Frações e unidade comum

Rascunho original para revisão de Jhuann, 21/10/2026. Ensino médio com retomada de fundamentos. Estudo e exercícios não exigem programação.

O painel soma p/q+r/s na mesma unidade, com p,r inteiros 0–6 e q,s inteiros 1–6. O denominador comum é o mmc. Os numeradores convertidos são mostrados antes da redução final por mdc. Zero é normalizado como 0/1; frações impróprias ampliam a escala. As três barras compartilham escala, origem e unidade; a soma concatena as parcelas. A figura não representa sinais, subtração, multiplicação ou divisão. Essas operações aparecem no texto e exercícios.

Caso padrão: 1/3+1/4=4/12+3/12=7/12. Ao zerar as parcelas, resta uma unidade vazia no eixo; o domínio continua válido. Em 6/1+6/1, a escala vai até doze unidades. A leitura sempre deve considerar o eixo, pois a escala muda entre configurações. Cor distingue parcelas, mas os rótulos e relato textual também fornecem valores e conversões.

## Fontes consultadas parcialmente

- [OpenStax Prealgebra 2e §4.2](https://openstax.org/books/prealgebra-2e/pages/4-2-multiply-and-divide-fractions): equivalência, simplificação, produto, inverso e divisão.
- [OpenStax Prealgebra 2e §4.5](https://openstax.org/books/prealgebra-2e/pages/4-5-add-and-subtract-fractions-with-different-denominators): múltiplo comum e soma/subtração com denominadores diferentes.

Consulta temática em 21/10/2026; exemplos, figura, controles e exercícios próprios. Não houve consulta nova ao acervo privado nem reprodução de figuras/soluções dos livros. Não se afirma cobertura de currículo escolar ou vestibular completo.

## Verificação

Na raiz:

```sh
python3 labs/fracoes-unidade/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes locais: todos os 1764 estados do painel contra Fraction; mmc por busca independente dos 36 pares de denominadores; troca de parcelas, equivalência, zero e impróprias; entradas fora do domínio. Referências JSON cobrem 81 configurações para confronto exato com JavaScript. As comparações são de inteiros e frações; nenhum sorteio ou tolerância é necessário para provar a soma nesses casos.

Permanecem pendentes problemas graduais com números mistos, expressões compostas, sinais e razão entre grandezas; avaliação com aluno e revisão conceitual de Jhuann. Existência do material não comprova domínio ou conclusão do percurso.
