# Spline natural: junções e forma

29/10/2026. Rascunho original para revisão de Jhuann.

Nós estritamente crescentes e valores em int/Fraction. Quantidades sem unidade física implícita. Sistema interno em M=S″, diagonal2(hesq+hdir), ladosh e RHS6(declivedir−decliveesq); pontasM0=Mn=0. Matriz simétrica positiva definida. Eliminação tridiagonal em O(n) operações, sem prometer custo linear em bits de frações. Modelo não resolve contornos arbitrários.

Coeficientes locais (a,b,c,d) em t=x−xi. Avaliação/derivadas0..3, sem extrapolação. Em nó interno a ordem3 usa o lado direito; C2 não implica C3. Resultado exato para entradas racionais, distinto da precisão dos dados ou adequação física. Código float denso e desafio anteriores preservados na aula e comparados nos testes.

Exemplo original x[0,1,3],y[0,1,1]: M[0,−1,0]; primeirotrecho7t/6−t³/6; segundo1+2t/3−t²/2+t³/12. Junção(1,2/3,−1). S(2)=5/4 ultrapassa dados; S′(3)=−1/3. Para x² nos nós0,1,2, M[0,3,0] e S(1/2)=5/16 difere de1/4. Reta reproduzida; quadrática/cúbica arbitrária não têm garantia com contorno natural.

Fonte: Burden/Faires/Burden, tradução10ª edição/terceira brasileiraCengage2016,§3.5 pp158,160,163–165/PDF172,174,177–179, inspeção visual parcial29/10/2026. Livro usa coeficientec=M/2. Exemplos, gráfico e laboratório locais; sem cópia de figura/exercício ouPDF privado.7ªedição é a indicada emCCM0218; não transplantar páginas. Nova consulta aoJúpiter expirou neste bloco; não constitui reconferência bem-sucedida.

```sh
python3 labs/spline-juncoes/spline.py
python3 -B -m unittest discover -s labs/spline-juncoes -t .
```

Seis testes: referência não uniforme/overshoot; quatro malhas×três conjuntos de valores com nós/junções/pontas;49 funções afins×cinco posições; contraexemplo quadrático; comparação independente com Gauss denso em seis conjuntos×17 posições e desafio anterior; contratos. Sem validação experimental, pedagógica ou revisão pessoal. Condições periódicas/fixadas, forma, ruído e análise geral de erro seguem pendentes.
