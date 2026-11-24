# K-means: descida e inicialização

Notas de aula originais, dados artificiais, revisão pessoal pendente. Percurso complementar; não representa disciplina cursada ou experiência de pesquisa.

## Executar

Na raiz do protótipo: `python3 labs/kmeans-inicializacao/lloyd.py` e `python3 -m unittest discover -s labs/kmeans-inicializacao -t .`.

Pontos 0,2,3,5,10. Início 0,3 chega a centros 5/3,15/2 e SSE103/6. Início 0,10 chega a 5/2,10 e SSE13. O teste enumera 32 atribuições para este exemplo, incluindo grupos vazios; não promete ótima solução para qualquer conjunto.

O trace registra custo antes, após a média e após nova atribuição. A identidade SSE(c)=SSE(média)+m(c−média)² prova a primeira queda. Empates escolhem o menor índice e centros vazios são conservados. Parada exige centros exatamente iguais; orçamento esgotado lança erro. Limites: 30 pontos/centros, inteiros ou Fraction, 1D, sem amostragem aleatória, pesos ou tolerância. O código float anterior da aula permanece separado e preservado.

## Fonte e proveniência

[scikit-learn, Clustering §2.3.2](https://scikit-learn.org/stable/modules/clustering.html#k-means), consulta parcial 29/10/2026, página exibida 1.9.1. Apoia objetivo, alternância e dependência da inicialização. Não foi instalado ou executado; nossa política de grupo vazio não é atribuída à biblioteca. Dedução algébrica, dados, código e figura próprios, preparados com apoio de IA. Sem nova consulta de livro privado ou programa oficial.

Próxima revisão de 20 minutos: deduzir a identidade e recalcular as duas partições. Permanecem pendentes avaliação externa, múltiplos atributos, escolha de k, comparação de inicializações e revisão conceitual por Jhuann. Testes finitos não provam convergência geral nem interpretação física.
