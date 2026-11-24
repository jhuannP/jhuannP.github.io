# Inequação racional — domínio, sinais e fronteiras

27/10/2026. Nova aula do percurso escolar próprio, com13seções/12exercícios e atividade para preparar explicação. Material original com apoio de IA, em rascunho para revisão pessoal. Nenhuma experiência com aluno ou domínio de Jhuann foi inferido.

## Caso principal e justificativa

Resolver f(x)=(x−1)/(x+2)≥0. Primeiro declarar x≠−2. Numerador zera em1; denominador zera em−2. Particionar a reta:

| Intervalo | x−1 | x+2 | Quociente |
|---|---|---|---|
| x<−2 | − | − | + |
| −2<x<1 | − | + | − |
| x>1 | + | + | + |

Os fatores lineares mantêm sinal em cada intervalo porque seus zeros estão nas fronteiras. Pontos−3,0,2 conferem o quadro, mas não substituem a justificativa para todos os reais. f(−3)=4 refuta a conclusão incompleta x≥1 que surgiria ao multiplicar pelo denominador sem conhecer seu sinal.

Em1 a expressão é zero e entra em≥; em−2 é indefinida e nunca entra. Solução:(−∞,−2)∪[1,∞), isto é,x<−2 ou x≥1. União não é interseção; infinito não é extremo incluído.

Outras relações:

- f>0:(−∞,−2)∪(1,∞);
- f≤0:(−2,1];
- f<0:(−2,1).

### Multiplicação por quadrado positivo

No domínio, (x+2)²>0. Assim f(x)≥0 equivale a(x−1)(x+2)≥0 **com x≠−2 mantido**. O produto sozinho incluiria−2, pois vale zero ali. A transformação algébrica não cria um valor da fração no polo.

## Cancelar preservando a restrição

g(x)=[(x−2)(x+1)]/(x−2)≥0. Primeiro x≠2. No domínio, g=x+1; logo x≥−1, excluindo2. Solução:[−1,2)∪(2,∞). A fórmula simplificada pode ser avaliada em2, mas essa extensão não é a expressão original. Não confundir cancelamento de fatores com cancelamento de termos de uma soma.

## Zero duplo

h(x)=(x−1)²/(x+2)>0. O numerador é positivo dos dois lados de1, onde vale zero. Com denominador positivo para x>−2, solução:(−2,1)∪(1,∞). Não se alternam sinais mecanicamente em toda raiz; a multiplicidade do fator importa.

## Laboratório e verificação

`examples.py` avalia esses três casos em Fraction, com inteiros ou frações, sem bool/float. Retorna None onde a expressão original é indefinida. `satisfies` trata None como fora do conjunto solução, distinguindo> e≥. Não é um resolvedor simbólico geral.

```sh
python3 -m unittest discover -s labs/inequacao-racional -t .
```

Cinco testes:1001pontos racionais para os conjuntos deduzidos; fronteiras a distâncias10⁻¹,10⁻¹⁰,10⁻³⁰,10⁻¹⁰⁰ sem arredondamento; cancelamento com domínio; equivalência com denominador ao quadrado; contratos e valores extremos. Amostragem finita é uma conferência de implementação, não prova geral dos intervalos. A prova está na análise dos fatores e fronteiras acima.

## Fonte e autoria

[OpenStax Intermediate Algebra2e, §7.6 Solve Rational Inequalities](https://openstax.org/books/intermediate-algebra-2e/pages/7-6-solve-rational-inequalities), consulta parcial em27/10/2026 para domínio, partição, sinais e fronteiras. Não houve leitura integral do livro. Expressões e variações, contas, figura, exercícios e código são próprios, sem reprodução de problemas, gabaritos ou figuras. Percurso escolar de reforço; não é uma disciplina universitária cursada ou equivalência curricular.

## Resoluções

1. Proibido−2.
2. Zero1, com denominador3.
3. f(−3)=4.
4. f(0)=−1/2.
5. f(2)=1/4.
6. f≥0:(−∞,−2)∪[1,∞).
7. Em>,1 sai e−2 continua proibido.
8. Não manter sempre o sentido ao multiplicar por x+2; seu sinal depende de x.
9. A equivalência com o produto mantém x≠−2.
10. Cancelamento:g≥0 dá[−1,2)∪(2,∞).
11. Zero duplo:h>0 dá(−2,1)∪(1,∞).
12. Grade finita não prova uma afirmação em todos os reais.

## Preparar uma aula

Em20min, desenhar o quadro, pedir uma justificativa para cada intervalo e trocar≥ por>. Depois usar o cancelamento para perguntar por que2 continua proibido. Registrar eventuais dúvidas só depois da experiência real; os campos pessoais ficam em branco. Módulo, sistemas, fatorações gerais e aplicações seguem pendentes.
