# Inversa e perda de informação — notas de laboratório

Modelo original racional 2×2, vetores coluna. Aula em rascunho: exemplo A=[[2,1],[0,1]], Python, desafio e IDs antigos preservados. Família A_t=[[t,1],[0,1]], invertível exatamente para t≠0; em zero, núcleo gerado por (1,0) e imagem u=v. Não interpreta posto exato como decisão de posto em dados ruidosos.

## Referência consultada

Elon Lages Lima, *Álgebra Linear*, exemplar IMPA2014 localizado no acervo autorizado. §6: p.59/PDF70, inversa à direita e Teorema6.1; p.63/PDF74, inversa à esquerda e Teorema6.5; p.64/PDF75, inversa bilateral e composição. Recortes reconferidos na extração textual paginada em27/10/2026, sem nova inspeção visual ou leitura integral. Texto privado não distribuído. Definições e resultados sustentam a aula; exemplos, família paramétrica e roteiro próprios. Uma tentativa de consulta ao livro interativo da Georgia Tech falhou e não é contada como fonte lida.

## Execução e interpretação

Na raiz: `python3 labs/inversa-familia/inverse.py`.

Biblioteca padrão, int/Fraction, sem bool/float; dimensão exatamente2×2. Matriz singular gera ValueError. O script confere produtos esquerdo/direito de496 matrizes invertíveis com entradas inteiras de−2 a2, rejeita129 singulares e verifica composição, ordem inversa incorreta e caso racional. As verificações executáveis complementam as provas; não são uma implementação geral de álgebra linear ou recomendação de inversão numérica em problemas grandes.

A variação δ/t é amplificação direcional absoluta, não um número de condicionamento relativo completo. Inversas de um lado retangulares não são bilaterais. Pseudoinversa tem outro contrato. Próxima revisão20min: refazer Gauss–Jordan, explicar os dois b na singularidade e comparar composição/ordem. Revisão pessoal de Jhuann pendente.


## 27/10/2026 — inversa, bijetividade e singularidade

`al-inversa` ampliada de3 seções/2 exercícios para11/10. Preservados exemplo A=[[2,1],[0,1]], Python, desafio e IDs originais. Acrescentadas provas de bijetividade/linearidade da inversa, unicidade, distinção retangular esquerda/direita, Gauss–Jordan, ordem inversa da composição e família A_t=[[t,1],[0,1]]. Em t=0, núcleo não trivial e imagem u=v; uma saída tem infinitas soluções, outra nenhuma. Amplificação δ/t explicitamente direcional/absoluta, sem confusão com número de condicionamento relativo completo. Figura original com dois casos ilustra perda de informação; não substitui prova geral.

Lima, Álgebra Linear, exemplar IMPA2014 do acervo: consulta textual parcial reconferida em27/10/2026, §6 p.59/PDF70 (direita/Teorema6.1), p.63/PDF74 (esquerda/Teorema6.5), p.64/PDF75 (bilateral/composição). Correspondência conferida pelos cabeçalhos da extração paginada. Sem nova inspeção visual ou leitura integral; PDF privado não distribuído. Exemplos e deduções próprios. Tentativa de abrir livro interativo da Georgia Tech falhou; não conta como leitura.

Verificação:14 testes do catálogo aprovados;821 estruturas MathML. Laboratório racional executado:496 matrizes invertíveis conferidas nos dois produtos,129 singulares rejeitadas, entradas inteiras−2..2; composição não comutativa, família racional e contratos. São exemplos executáveis, não496 testes unitários distintos. No navegador390px, exercício de sensibilidade rejeitou0,001 e aceitou0,1 pelo Enter. Figura inspecionada em `inversa-familia-mobile.jpg`; documento390/390px e console sem erros observados. Windows real/leitor de tela não testados. Revisão pessoal pendente; não é solver genérico para grandes sistemas.

ÁlgebraLinear:18 aulas/179 exercícios, duas introduções curtas e nove grupos curriculares parciais. Global51 trilhas,550 aulas/4465 exercícios,190 introduções curtas; sem curso completo ou competência individual certificada. Próxima revisão20min: refazer a redução aumentada e explicar os dois b em t=0; depois demonstrar a ordem de composição. Próxima elaboração global: consultar a cobertura de MatemáticaII antes de escolher uma introdução ainda curta. Saldo semanal78%; parada65% preservada.
