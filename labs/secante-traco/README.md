# Secante — traço exato e interpretação dos critérios

Exemplo anterior f=x²−2,x0=1,x1=2 preservado, assim como Python float, desafio e IDs ms1/ms2. Novo laboratório racional com função determinística/pura, dois pontos distintos e orçamento1..8. Retorno distingue raiz exata de orçamento; denominador nulo gera ArithmeticError. Sem rotina global salvaguardada, função ruidosa ou recomendação de tolerância universal.

Fonte pública parcialmente consultada em27/10/2026: Driscoll/Braun, Fundamentals of Numerical Computation§4.4, https://fncbook.com/secant/ : eq4.4.1–2 para reta/passos, discussão de custo e ordem eq4.4.6. Não copiados código, exemplos ou tabelas. Burden10 continua referência temática do curso; não houve nova leitura do exemplar neste bloco. Traço racional, análise de escala, limite de erro do exemplo, figura e exercícios adicionais próprios. Motivação da ordem local não é prova geral de convergência.

Na raiz: `python3 labs/secante-traco/secant.py`. Biblioteca padrão,Fraction; callback deve devolver int/Fraction, sem bool/float. Confere4/3,7/5,58/41,816/577, seis avaliações em quatro passos, invariância por três escalas não nulas, funções afins em três inclinações, diagnóstico de valores iguais e contratos. Referência Decimal70 dígitos suplementa limite analítico de resíduo/2 em[1,2], sem se tornar certificado geral de todas as funções.

Não manter um bracket é intencional na secante padrão. O par recente4/3,7/5 tem ambos f negativos, embora o par inicial cercasse a raiz. Na função escalada10^-12(x−1000), resíduo10^-9 emx0 está associado a erro1000: escala importa. Para o exemplo quadrático, a derivada≥2 entre x e raiz dá limite de erro|f(x)|/2; as hipóteses fazem parte da conclusão.

Próxima revisão20min: reconstruir7/5, contar chamadas e justificar1/50. Revisão pessoal de Jhuann pendente; método geral salvaguardado, análise completa de ordem e dados ruidosos não preparados aqui.


## 27/10/2026 — secante: traço, avaliações e erro

`metodo-secante` ampliada de3 seções/2 exercícios para12/12. Preservados exemplo f=x²−2,Python float, desafio e IDs ms1/ms2. Derivada a atualização pela reta, traço4/3,7/5,58/41,816/577, perda do bracket, resíduo versus erro/escala, contagem de chamadas e identidade exata de erro quadrático. Motivação da ordem localφ é delimitada, sem garantia global ou prova geral. Quatro atualizações usam seis avaliações; callback determinística/pura. Novo laboratório racional retorna raiz exata/orçamento e diagnostica valores iguais, sem chamar orçamento de divergência ou ausência de raiz.

Fonte pública parcialmente consultada em27/10/2026: Driscoll/Braun,FNC§4.4,eq4.4.1–2 e discussão de custo/ordem4.4.6, https://fncbook.com/secant/ . Não copiados código, exemplos ou tabelas. Burden10 permanece referência temática, sem nova leitura do livro nesta continuação. Exemplo anterior e novas derivações/figura próprios.

Verificação:14 testes do catálogo aprovados;831 estruturas MathML conferidas. Script racional executado com traço, contagem real de chamadas, invariância por três escalas não nulas, funções afins de três inclinações, denominador nulo e contratos. Comparação Decimal70 dígitos suplementa limite analítico|f|/2 em[1,2]; não é certificado geral. No navegador390px, exercício5 rejeitou1/25 e aceitou1/50 pelo Enter; figura inspecionada em `secante-traco-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados; revisão pessoal pendente.

ComputaçãoIII:33 aulas/217 exercícios,17 recortes com mais de três seções e16 introduções curtas; onze grupos curriculares parciais. Global51 trilhas,554 aulas/4583 exercícios,183 introduções curtas. Sem curso completo ou domínio pessoal certificado. Próxima revisão20min: reconstruir7/5, identificar perda de bracket, contar avaliações e justificar1/50. Próxima elaboração global: conferir uma introdução de ComputaçãoIV e seu suporte bibliográfico antes de ampliar. Saldo semanal77%; parada65% preservada.
