# Cascas, raio e união

Notas originais: R={0≤x≤1,0≤y≤x²}, coordenadas adimensionais. Volumes multiplicam porℓ³ se uma unidade gráfica representa comprimentoℓ. Cascas no eixo externo têm raios distintos por faixa; eixo interno exige conferir união/sobreposição antes da integral.

Fonte pública parcialmente consultada em27/10/2026: OpenStax CalculusVolume1§6.3, https://openstax.org/books/calculus-volume-1/pages/6-3-volumes-of-revolution-cylindrical-shells . Derivação por anéis/somas de Riemann e comparação de cortes. Não copiados exemplos, checkpoint, soluções ou figuras; região-base, casos de eixos−1,2,1/2 e contraexemplo de sobreposição são desenvolvimento próprio. Apostol permanece referência temática, sem nova leitura nesta extensão.

Na raiz: `python3 labs/cascas-uniao/shells.py`. Biblioteca padrão,Fraction; integra polinômios fornecidos em coeficientes por grau, limites racionais ordenados. Não recebe regiões geométricas gerais, não decide união automaticamente e não faz análise numérica adaptativa. O script confere15 integrais cúbicas contra Simpson exato,101raios com contenção das alturas, casos de referência e corte por y com raiz quadrada/quadratura float independente.

Volumes divididos porπ: eixo0 dá1/2; eixo−1 dá7/6; eixo2 dá5/6; eixo1/2 dá17/96. Soma dos dois lados com módulo de raio dá18/96: excesso1/96 da parte esquerda já contida no giro direito. Para eixo interno, cortes emy mudam de disco para arruela em1/4. A nova aula não declara completude da integração ou domínio pessoal.

Próxima revisão20min: desenhar raio/altura antes de calcular, conferirπ/2 por duas ordens e explicar17/96 versus18/96. Revisão pessoal, regiões gerais, densidade, superfície e modelos reais pendentes.


## 27/10/2026 — revisão das cascas cilíndricas e sobreposição

Concluída a verificação pendente da aula já existente `c1-cascas-cilindricas`,12 seções/12 exercícios. Melhorada a separação entre palavras, símbolos e números na prosa, sem mudar IDs, fórmulas ou respostas. Corrigida a abertura desatualizada destas notas: cascas e trabalho já possuem primeiros recortes, não cobertura integral. Mantidas as notas pessoais de CálculoI como ainda não preparadas.

Região original R={0≤x≤1,0≤y≤x²}, coordenadas adimensionais. Raios dos eixos0,−1,2 dão V/π=1/2,7/6,5/6. Eixo interno1/2 exige união: faixa direita contém o giro da esquerda de mesmo raio, V/π=17/96; soma com módulo dá18/96, excesso1/96. Cortes por y mudam de disco para arruela em y=1/4 e confirmam17/96. Escala físicaℓ multiplica volumes porℓ³. Laboratório não decide uniões de regiões gerais nem representa material real.

Fonte pública reaberta e parcialmente reconferida: OpenStax Calculus Volume1,§6.3, https://openstax.org/books/calculus-volume-1/pages/6-3-volumes-of-revolution-cylindrical-shells — derivação por anéis, soma de Riemann/regra6.6 e comparação de métodos. Não se atribuem à fonte os eixos deslocados, o contraexemplo de sobreposição, números ou desenho próprios. Apostol continua referência temática, sem nova leitura privada neste bloco. Sem cópia de exemplos, exercícios ou figuras da fonte.

Verificações:14 testes de catálogo aprovados;835 estruturas MathML conferidas no catálogo. `labs/cascas-uniao/shells.py` aprovado:15 integrais polinomiais contra Simpson exato para cúbicas,101 raios com contenção das alturas, casos racionais, contratos e quadratura independente dos cortes em y. No navegador390px, exercício do eixo interno rejeitou3/16 e aceitou17/96 pelo Enter; documento390/390px, console sem erros observados. Desenho inspecionado em `cascas-uniao-mobile.jpg`. Windows real, leitor de tela, revisão pessoal e regiões gerais pendentes.

CálculoI:27 aulas/270 exercícios, dez grupos ainda parciais. Catálogo atual51 trilhas,556 aulas/4617 exercícios,182 introduções curtas; não foram acrescentadas novas aulas neste bloco. Contagens não certificam domínio ou cobertura integral. Próxima ação20min: desenhar a união dos giros no eixo interno e reconstruir17/96 por dois cortes. Próxima elaboração global: voltar às lacunas de BiologiaIII/QuímicaIV após conferir o mapa, sem reapresentar aulas desenvolvidas como introduções vazias. Saldo semanal77%; parada operacional65% preservada.
