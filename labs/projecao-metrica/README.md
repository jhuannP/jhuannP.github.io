# Projeção com uma métrica — laboratório original

Em R², G simétrica definida positiva fornece produto interno xᵀGy. Sobre reta span(u),u≠0, a projeção é p=αu com α=(uᵀGb)/(uᵀGu). Resíduo r=b−p satisfaz uᵀGr=0. Para qualquer t, ‖b−tu‖²_G=‖r‖²_G+(t−α)²‖u‖²_G, provando mínimo único. O resultado depende de G, não apenas da reta.

Exemplo próprio G=diag(1,4),u=(1,1),b=(2,0): α=2/5,p=(2/5,2/5),r=(8/5,−2/5),erro ponderado16/5. A projeção usual(1,1) tem erro ponderado5. r·u=6/5,portanto não há perpendicularidade usual; uᵀGr=0. Com W=diag(1,2),G=WᵀW: projetar Wb na reta de Wu em coordenadas usuais e aplicar W⁻¹ retorna o mesmo p.

P=[[1,4],[1,4]]/5 satisfaz P²=P e PᵀG=GP,mas Pᵀ≠P. Simetria usual não é requisito correto nessa métrica. Pesos devem ser definidos pelo problema e suas unidades: não são automaticamente probabilidades ou inversos de variância. Sem modelo estatístico, não há inferência de incerteza.

```sh
python3 labs/projecao-metrica/metric.py
python3 -m unittest discover -s labs/projecao-metrica -t .
```

Fraction e biblioteca padrão,apenas dimensão2/reta; sem solver geral,ruído ou dados experimentais. Critério SPD2x2:a>0,simetria e detG>0. Sem positividade,o quadrático pode ser ilimitado inferiormente;G=diag(1,−1),b=0,u=(0,1) dá erro−t². Não é uma distância. Frações exatas não certificam estabilidade de implementação float geral.

Fonte privada:Lima,Álgebra Linear,2014,§10 pp.118–119,consulta textual parcial29/10/2026 a axiomas,norma e produto usual. Não foi confirmada neste bloco a paginação física do PDF nem realizada inspeção visual;capítulo e páginas impressas conferidos no cabeçalho extraído. Exemplo ponderado e deduções redigidas próprios,sem atribuí-los ao livro. Fonte complementar [MIT18.06,Spring2022,finalsol.pdf,p.15–16,problema7](https://www.mit.edu/~18.06/Spring2022/finalsol.pdf),consulta textual parcial29/10: transformação de quadrático SPD em norma usual. Não reproduzidos enunciado,gabarito ou exercício;dados,código,figura e atividades próprios. Sem leitura integral ou distribuição de PDFs privados. Revisão pessoal pendente.
