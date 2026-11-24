# Domínio e equivalência de expressões

Rascunho didático original, pendente de revisão. Três casos reais:0 raiz/quociente √(x−a)/(x−(a+1));1 cancelamento (x²−a²)/(x−a) com restrição x≠a, comparado à extensão x+a;2 raiz de quadrado |x−a|, comparada à substituição incorreta geral x−a.

O painel usa a em[-2,2] e x em[-4,6]. A figura tem y entre−6 e6. Valores fora da janela são omitidos e não pontos matematicamente indefinidos. Trechos são interrompidos ao encontrar exclusão/valor omitido; o ponto removido do caso1 tem círculo aberto. A curva g pode coincidir com f fora desse ponto; o relato mantém sua avaliação separada. O painel não calcula imagem completa ou composição: esses temas são explicados no texto/exercícios.

A implementação racional confere x≠a antes de usar x+a para evitar cancelamento numérico. O denominador do caso0 é avaliado como x−(a+1), coerente com o ponto excluído, e não exclui vizinhos por tolerância. None/null representam ausência; nunca substituem valores por zero. Algoritmo finito não é álgebra simbólica geral.

## Fontes públicas parcialmente consultadas

- [OpenStax CalculusI1.1](https://openstax.org/books/calculus-volume-1/pages/1-1-review-of-functions): função, domínio/imagem e operações/composição.
- [OpenStax College Algebra2e3.2](https://openstax.org/books/college-algebra-2e/pages/3-2-domain-and-range): restrições reais e notação de intervalos.

Trechos pertinentes consultados; exemplos, sequência e figuras próprios, sem reprodução de exercícios. A página de funções inversas foi aberta como referência exploratória, mas não fundamenta esta unidade e não se afirma cobertura de inversas. Nenhum PDF privado consultado neste bloco. As notas pessoais de CálculoI continuam pendentes.

## Reproduzir

Na raiz:

```sh
python3 labs/dominio-funcoes/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:55pares de parâmetros/entradas nos três casos, contra restrições e fórmulas independentes com Fraction quando racional; extremos e vizinhos imediatos representáveis via nextafter; extensão, módulo e motivos de exclusão; domínio de entrada do laboratório.84referências JS/Python adicionais. Contraexemplos e verificações numéricas não substituem as justificativas de todos os domínios da aula.

Ainda faltam composições mais complexas, funções por partes, problemas de imagem/inversa e integração das notas de Jhuann. Nenhum rascunho conclui CálculoI ou certifica domínio pessoal.
