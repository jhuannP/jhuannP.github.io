# Formas e significado dos eixos

Camada Z_ih=Σ_j X_ij W_hj+b_h; X(B,D), W(H,D), b(H,), saída(B,H). Exemplos e figura próprios. Exemplo, Python, desafio e IDs tf1/tf2 antigos preservados. Rascunho, não framework de tensores ou demonstração de domínio pessoal.

Fontes públicas parcialmente consultadas em27/10/2026:
- D2L1.0.3§2.1.1 reshape e§2.1.4 broadcasting: https://d2l.ai/chapter_preliminaries/ndarray.html
- NumPy2.5 Manual, General broadcasting rules: https://numpy.org/doc/stable/user/basics.broadcasting.html

Sem copiar sequência de exemplos/figuras; sem instalar/executar NumPy ou PyTorch. O script usa biblioteca padrão e Fraction. Não modela strides, cópias/views, tipos de dispositivo, autodiff, eixos vazios ou arrays esparsos. Broadcasting só calcula compatibilidade para formas de tamanhos positivos e escalar(); não valida semântica.

Na raiz: `python3 labs/tensores-eixos/shapes.py`. Conferência da camada numérica, independência de amostras, identidade de deslocamento em9 casos, perda pareada11/3 versus cruzada35/3, broadcast de bias, contratos e reshape versus transposição. Os testes estruturais não provam que um modelo treinou ou generaliza. Próxima revisão20min: calcular quatro saídas e reconstruir as nove diferenças antes de rodar. Revisão pessoal pendente.


## 27/10/2026 — tensores, eixos e broadcasting sem erro semântico

`dl-tensores-formas` ampliada de3 seções/2 exercícios para12/12. Preservados exemplo, Python, desafio e IDs tf1/tf2. Convenção X(B,D), W(H,D), b(H,), saída(B,H): derivação por índices e parâmetros compartilhadosHD+H. Exemplo racional Z=[[2,3],[3,−4]],quatro saídas/oito parâmetros. Broadcasting de(3,1) e(3,) cria perda cruzada35/3 em vez de pareada11/3. Reshape por linhas versus transposição com mesma forma e valores distintos; redução de eixos, dimensão versus posto e limites da analogia com tensor físico. Não há autodiff/framework/GPU ou integração de novos recursos à MLP.

Fontes públicas parcialmente consultadas em27/10/2026: D2L1.0.3§2.1.1 reshape e§2.1.4 broadcasting, https://d2l.ai/chapter_preliminaries/ndarray.html ; NumPy2.5 Manual, General broadcasting rules, https://numpy.org/doc/stable/user/basics.broadcasting.html . Sem cópia da sequência de exemplos ou figuras. Camada, perda cruzada, laboratório e esquema próprios. Não houve instalação/execução de NumPy ou PyTorch; script usa biblioteca padrão e frações.

Verificação:14 testes de catálogo aprovados;821 estruturas MathML do catálogo conferidas. Script executado com camada numérica, independência das amostras/concatenação, deslocamento em9 casos, duas perdas por somas diretas, compatibilidade de broadcast, contratos e reshape/transposição. Não são testes de treinamento/generalização. No navegador390px, exercício5 rejeitou3 e aceitou9 pelo Enter; figura inspecionada em `tensores-eixos-mobile.jpg`, documento390/390px e console sem erros observados. Sem teste no Windows/leitor de tela real. Revisão conceitual pessoal pendente.

DeepLearning:25 aulas/110 exercícios,19 introduções curtas. Catálogo global51 trilhas,552 aulas/4509 exercícios,188 introduções curtas; sem curso completo ou domínio pessoal certificado. Próxima revisão20min: reconstruir a saída, as nove diferenças e explicar o erro de pareamento; depois contrastar reshape/transposição. Próxima elaboração global: consultar uma introdução de MachineLearning e sua referência antes de ampliar, preservando alternância. Saldo semanal78%; parada65% preservada.
