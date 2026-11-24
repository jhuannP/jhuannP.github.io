# Fronteiras orientadas: dois campos distintos

Casos analíticos sintéticos paraStokes eGauss, não um integrador geral ou prova dos teoremas. Rascunho assistido porIA,revisão pessoal pendente. Coordenadas numéricas em unidade de comprimento escolhida,campos matemáticos F=(-y,x,z) eG=(x,y,z),não campos físicos medidos.

Da raiz:

```sh
python3 -B -m labs.bordas-orientadas.integrals
python3 -B -m unittest discover -s labs/bordas-orientadas -t .
```

`stokes_rectangle(a,b,c,p,q,orientation)`usa gráfico z=c+p*x+q*y sobre[0,a]×[0,b],a/b>0,orientação+1para cima ou−1para baixo. As bordas reordenam junto com a normal. Fórmula de segmento reto: x0*y1−y0*x1+(z1²−z0²)/2. É específica deF;inclui contribuiçãoz dz,não aplica fórmula plana ignorandoz. A área orientada do gráfico é(-p,-q,1)dxdy. CurlF=(0,0,2),fluxo2ab,independente de inclinação;área escalaréab sqrt(1+p²+q²),nãoab se inclinado.

Referênciaa2,b3,c1,p1,q2: vértices(0,0,1),(2,0,3),(2,3,9),(0,3,7),bordas4,42,−10,−24,soma12. As quatro parcelasz dz telescopam porquez²/2é potencial dessa parte do campo. Inverter somente normal cria sinais incompatíveis;inverter percurso também restaura igualdade.

`gauss_box(lower,lengths)`calculaG em seis faces da caixa,sempre normal externa;comprimentos positivos. Caixa de canto(1,2,3),lados(2,3,4):fluxos−12,36,−16,40,−18,42,soma72;divG3×volume24=72. Somar só as três facesaltas dá118,não fluxo fechado. Rejeitar comprimentos nulos é contrato do exemplo,não caracterização geral de regiões admissíveis.

Entradas int/Fraction sem float/bool,orientação int±1. Cinco testes:referências;108gráficos com432integrais de segmento por quadratura independente de ponto médio(exata aqui por afinidade);nove inclinações/orientações e área;81caixas por normais/pontos médios;snippet/desafio anteriores e contratos. Pontos médios não são regra exata para campo geral. Não modela singularidades ou distribuições;caso com origem excluída já está emcampos-operadores.

Fonte primária:NISTDLMF1.6(v),E55–E58 e contexto de orientação,corpo parcialmente consultado30/10/2026, https://dlmf.nist.gov/1.6#v . Abertura inicial emivnão forneceu teoremas;trecho pertinente localizado e lido antes da elaboração. Sem copiar figura/exercício. Gráfico,campos,contas e implementação locais;semPDFprivado.
