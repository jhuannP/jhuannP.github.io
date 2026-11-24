# Acompanhar o forward sem treinar

Laboratório original da MLP2→H→1 já existente. Importa `dense_net.py` da raiz; não é arquivo autônomo isolado. Não instala framework, não calcula gradientes e não executa atualização.

Da raiz: `python3 -B -m unittest discover -s labs/forward-estados -t .` e `python3 -B -m labs.forward-estados.trace`.

`trace` faz cópia numérica local dos parâmetros, exige int/float finitos, duas entradas e formas da rede original (1≤H≤16). Rejeita texto e booleano nesse contrato. Devolve pré-ativação, hidden, logit, probabilidade e contagem4H+1. Isso não torna a API existente um framework geral. Intermediários não finitos também são rejeitados; entradas finitas podem produzir overflow durante multiplicação.

Referência própria: a=ln3/2, x=(a,1), W=((1,0),(−1,0)), b=(0,0), v=(2,−2), c=0. Pré-ativações(a,−a), tanh=(1/2,−1/2), logit2, p≈0,880797. Segunda entrada tem peso zero neste exemplo. Nove parâmetros armazenados; não são nove operações, dados ou garantias de capacidade.

`decision` usa p≥limiar, limiar estritamente entre0e1. Para p≈0,880797, limiar0,5dá1 e0,9dá0, sem mudar a probabilidade. Não há calibração validada ou escolha do limiar por custos/dados aqui.

Sigmoide real para z finito fica estritamente entre0e1, mas float pode devolver exatamente0ou1 em logits extremos. Isso é arredondamento/underflow; não certeza empírica. O núcleo já calcula os ramos com exp de argumento não positivo. A aula de perda por logits trata a etapa seguinte; não recalculamos log da probabilidade arredondada.

Cinco testes: referência não nula,27estados por Decimal de60dígitos com tanh via exponencial,imutabilidade e simetrias de unidades,extremos/contratos,material anterior. A avaliação Decimal usa as representações decimais dos floats para comparação tolerante, não certifica erro de toda entrada.

Fonte primária parcialmente consultada30/10/2026: [D2L1.0.3§5.3.1](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html),ordem das dependências e§5.3.4para reutilização de estados. Fonte omite biases no recorte,que nosso modelo já possuía; notaçãozda fonte é pré-ativação, aqui usous para ela e zpara logit. Exemplo,figura e testes locais;sem copiar figura,código ou exercício. Revisão pessoal pendente.
