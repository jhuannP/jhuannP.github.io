# Deslocamentos e classificação vibracional

22/10/2026. Aula `q3-deslocamentos-simetria`:14seções/12exercícios originais, pendentes de revisão pessoal. Geometrias AB₂ adimensionais; nenhuma espécie, frequência, intensidade ou medida experimental identificada.

## Fonte e leitura

Miessler/Fischer/Tarr,Química Inorgânica,quinta edição brasileira/Pearson2014. Recortes do corpo consultados:pp.92,96,101–103 e107(PDF107,111,116–118,122). Página96/PDF111renderizada e inspecionada visualmente para convenções deC₂v e vetores/rotações. Parte da extração intermediária depp.93–95não foi necessária à redação e não é alegada como leitura integral. Fonte confirma distinção de coordenadas3N,movimentos rígidos e classificação, além de contextualizar atividade infravermelha. O exemplo do livro não foi transcrito; não se copiam figuras, exercícios ou soluções. A construção algorítmica e a extensão ao caso linear como subgrupo são próprias. Paginação só do exemplar português confirmado.

O [material público de Newcastle sobre água/C₂v](https://www.staff.ncl.ac.uk/j.p.goss/symmetry/Water/water0.html), já referido pela aula inicial, foi aberto novamente como apoio de convenção. A geometria deste projeto é esquemática e não reproduz ângulo ou constante de uma molécula. As aulas de cadeia longitudinal e classificação geométrica respondem a perguntas diferentes.

## Geometrias e convenção

Angular:b=(A,B₁,B₂)=((0,0,0),(1,0,1),(−1,0,1)). Linear:((0,0,0),(1,0,0),(−1,0,0)). Dois B equivalentes. Ordem das operações:E,C₂z,σxz,σyz. O grupo escolhido éC₂v para a geometria angular; na linear é apenas um subgrupo da simetria ampliada. Não se usa essa restrição para inferir a classificação completa, degenerescência ou regras completas da estrutura linear.

As matrizes3D são diagonais com sinais (1,1,1),(−1,−1,1),(1,−1,1),(−1,1,1). A matriz9×9envia um deslocamento do átomo i para a posição do átomo j correspondente à operação e transforma seu vetor por esses sinais. Isso separa permutação nuclear e transformação espacial. D(g)D(h)=D(gh)é verificado para todos os16pares nas duas geometrias.

## Subespaços e projetores exatos

Três colunas de translação repetem cada vetor cartesiano nos três átomos. Três colunas rotacionais são e_axis×r_i. Ortogonalização racional constrói o projetor euclidiano PTnas translações e PRno espaço gerado por translações+rotações. PV=I−PRprojeta no complemento geométrico. PR−PTrepresenta as rotações módulo translação, sem exigir que a origem coincida com o centro de massa.

São projetores para uma construção geométrica; não normalização por massas ou autovetores de uma matriz dinâmica. As representações são ortogonais e o subespaço rígido é invariante; por isso os projetores comutam com todas as matrizes do grupo. Os caracteres são traços de D, DPT, D(PR−PT) eDPV.

| Geometria | Dimensão total | Posto rígido | Dimensão interna | Caracteres internos nesta ordem |
|---|---:|---:|---:|---|
| Angular |9|6|3|(3,1,3,1)|
| Linear |9|5|4|(4,0,2,2)|

Caracteres totais:(9,−1,3,1), nas duas geometrias. Translação:(3,−1,1,1). Rotação angular:(3,−1,−1,−1); rotação linear:(2,0,0,−2). No caso linear, a coluna de rotação emxé nula. Esse é um teste estrutural da diferença entre3N−6 e3N−5, não frequência nula artificialmente feita oscilar.

Para as linhas C₂v A₁=(1,1,1,1), A₂=(1,1,−1,−1), B₁=(1,−1,1,−1), B₂=(1,−1,−1,1), o produto interno dos caracteres dividido por4dá multiplicidades. Resultado angular:2A₁+B₁. Restrição linear:2A₁+B₁+B₂. O cálculo deriva os traços pelas matrizes/projetores antes de reduzir; não recebe as multiplicidades esperadas como entrada.

## Limites físicos

Contagem e simetria não determinam massas, constantes de força, autovetores dinâmicos, frequências ou intensidades. A associação dos tipos de simetria com componentes do dipolo fornece uma condição de permissão por simetria; não calcula uma derivada não nula, intensidade ou espectro observado. Não é afirmação de que todo tipo permitido tenha necessariamente intensidade detectável.

No cenário linear, mais operações de simetria podem impor restrições que não aparecem emC₂v; nenhuma regra espectroscópica completa é derivada só desse subgrupo. Não há cálculo de Raman, forma de banda, resposta eletrônica ou identificação de compostos. Aulas e testes não validam uma molécula real ou domínio pessoal deJhuann.

## Executar e verificar

Na raiz:

```sh
python3 labs/deslocamentos-simetria/experiment.py
python3 -m unittest discover -p 'test_*.py'
```

Quatro testes novos:composição e traço independente por átomos fixos;projetores/invariância e posto por eliminação independente;ortogonalidade/reconstrução dos caracteres;rotação axial nula e contratos. Todos os cálculos de projetores e caracteres usam Fraction, sem limiar numérico de posto. Os testes validam a construção finita, sem demonstrar afirmações físicas fora dela.

## Continuidade

Revisão pessoal, materiais da turma e Samsung Notes pendentes. Próxima alternância global:auditar ComputaçãoIV. No retorno deQuímicaIII, avançar em dinâmica com massas e regras de seleção/intensidade a partir de fontes específicas; não declarar as demais frentes ou espectroscopia concluídas.


Verificação final:578testes Python,241demonstrações/723cenários e331MathML aprovados. Catálogo repetido após notação/redução explícita. Resposta−1e interface desktop/390px conferidas sem transbordamento horizontal ou erros observados no console; roteiro abre a aula,viewport restaurado. Revisão pessoal pendente. Saldo90%; parada65%.
