# Pitágoras e distância — Python opcional

Notas originais para reforço; geometria euclidiana, comprimentos positivos na mesma unidade. Demonstração por áreas, recíproca por congruência lado-lado-lado e exemplos adicionais próprios. Não é relato de aula ministrada ou evidência de domínio de Jhuann.

Fonte pública parcialmente consultada em27/10/2026: OpenStax ElementaryAlgebra2e§3.4, https://openstax.org/books/elementary-algebra-2e/pages/3-4-solve-geometry-applications-triangles-rectangles-and-the-pythagorean-theorem . Sustenta definição de triângulo retângulo/hipotenusa, relação e resolução de aplicações. Montagem, recíproca, coordenadas e atividades adicionais são próprias; sem copiar figuras ou sequência de exercícios. Não confundir este localizador§3.4 de ElementaryAlgebra com§9.3 de Prealgebra.

Na raiz: `python3 labs/pitagoras-distancia/geometry.py`. Biblioteca padrão,int/Fraction positivos, sem bool/float. Retorna quadrado do comprimento e raiz racional exata quando houver; None para raiz não racional não significa ausência de comprimento real. Não arredonda medidas experimentais ou decide perpendicularidade com incertezas.

Script confere exemplos,36 triplas geradas pela parametrização m²−n²,2mn,m²+n² (m2..9,n1..m−1), permutações de lados e três escalas racionais; casos não retângulo/degenerado e contratos. Essa família de exemplos complementa, sem substituir, a prova geométrica. A parametrização não é apresentada como enumeração completa de todas as triplas nesta aula.

Próxima revisão20min: marcar hipotenusa e explicar por que escolher raiz positiva; depois justificar unidade, recíproca e diferença entre linha reta e rota. Estudo e exercícios não exigem programação. Revisão pessoal e validação com aluno permanecem pendentes.


## 27/10/2026 — Pitágoras e distância no plano

Nova aula `em-pitagoras`,12 seções/12 exercícios e Python opcional. Hipotenusa identificada pelo ângulo reto, prova por áreas com quatro triângulos congruentes, raiz positiva, cateto desconhecido, radical exato, recíproca por congruência, desigualdade triangular, unidades, coordenadas e semelhança. Distância euclidiana separada de rota permitida; medidas racionais exatas não confundidas com perpendicularidade inferida de medições arredondadas. Roteiro e módulo atualizados; aulas anteriores preservadas.

Fonte pública parcialmente consultada em27/10/2026: OpenStax ElementaryAlgebra2e§3.4, https://openstax.org/books/elementary-algebra-2e/pages/3-4-solve-geometry-applications-triangles-rectangles-and-the-pythagorean-theorem . Definições e uso da relação; prova por áreas, recíproca, coordenadas, exemplos e figura adicionais próprios. Não copiada sequência de exercícios ou figura do livro; localizador distinto de Prealgebra§9.3.

Verificação:14 testes de catálogo aprovados;827 estruturas MathML conferidas. Script opcional executado:36 triplas parametrizadas por m,n, permutações, três escalas racionais, exemplos, caso de raiz não racional, lados degenerados/não retângulos e contratos. Não é prova da totalidade de triplas ou análise de incerteza experimental. No navegador390px, exercício2 rejeitou10 e aceitou8 pelo Enter; figura inspecionada em `pitagoras-distancia-mobile.jpg`, documento390/390px e console sem erros observados. Dica refinada para explicitar6²+b²=10². Windows real/leitor de tela e uso com aluno não testados. Revisão pessoal pendente.

MatemáticaEscolar:18 aulas/214 exercícios e nenhum recorte de até três seções, sem implicar cobertura completa. Global51 trilhas,553 aulas/4561 exercícios,184 introduções curtas. Nenhum curso completo ou domínio pessoal certificado. Próxima revisão20min: reconstruir prova e solução por desenho, sem depender do código; depois justificar a recíproca e unidades. Próxima elaboração global: conferir cobertura de FísicaEscolar e um recorte que fortaleça interpretação de situações e unidades. Saldo semanal78%; parada65% mantida.
