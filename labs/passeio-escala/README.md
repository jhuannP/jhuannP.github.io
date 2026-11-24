# Passeio binário, escala e browniano

Material original em rascunho. Exemplo de100 passos, código gaussiano, desafio e painel anteriores preservados. Laboratório novo enumera exatamente2^n caminhos de±a e não representa um processo contínuo. Domínio: n inteiro0..10, a int/Fraction positivo, sem bool/float. Armazenamento cresce exponencialmente; não é MonteCarlo escalável.

Pavliotis, Stochastic Processes and Applications, exemplar autorizado do acervo: §1.3 p.11/PDF25, definição1.8; p.12/PDF26, passeio reescalado/interpolado e convergência fraca citada; p.10/PDF24, convenção de difusão2Dt em discussão de transporte. Consulta textual parcial em27/10/2026, cabeçalhos impressos/PDF conferidos. Sem nova inspeção visual, leitura integral ou reprodução de figuras. Chorin–Hald permanece referência temática, sem nova leitura neste bloco. Contagens, deduções, figura e exercícios próprios. PDF privado não distribuído.

Na raiz: `python3 labs/passeio-escala/walk.py`. Confere distribuição binomial por contagem independente de caminhos, momentos/covariâncias em todos os pares de tempos para n0..8, caso de referência e contratos. Para h1/4,a1/2,n4, os pesos finais em−2,−1,0,1,2 são1,4,6,4,1 sobre16. Variância1 igual à de W1 padrão, mas massa3/8 em zero, diferente de uma normal contínua. Com amplitude errada h, variância1/4 em vez de1.

A escala a=σ√h mantém Var(X_T)=σ²T. Para X=√(2D)W, Var=2Dt, com unidades declaradas. A malha gaussiana reproduz distribuições nos nós sob amostragem ideal, mas interpolação linear não reconstrói a lei do caminho entre nós. A mesma semente não prova acoplamento de malhas/erro forte. Nenhuma prova do teorema funcional ou validação de gerador foi realizada.

Próxima revisão20min: reconstruir tabela, derivar escala e distinguir variáveis de incrementos de valores do processo. Revisão pessoal de Jhuann, EDEs, convergência forte/fraca detalhada, interpolação condicional e dados reais pendentes.


## 27/10/2026 — passeio, escala e lei browniana na malha

`passeio-browniano` ampliada de3 seções/2 exercícios para12/12. Preservados exemplo de100 passos, código gaussiano, desafio, painel e IDs w1/w2. Derivação de momentos e covariância por independência, lei binomial exata, escala a=σ√h e falha de a=σh. Exemplo h1/4,a1/2,n4 tem variância1 e massa3/8 em zero, distinguindo passeio discreto de normal contínua com os mesmos momentos. Lei gaussiana nos nós não equivale à interpolação de caminho; mesma semente não prova acoplamento forte. Convenção física X=√(2D)W,Var=2Dt e unidades explicitadas. Teorema funcional citado, não demonstrado.

Pavliotis, Stochastic Processes and Applications: consulta textual parcial em27/10/2026,§1.3 pp.11–12/PDF25–26, definição1.8 e passeio reescalado/interpolado; p.10/PDF24 para convenção2Dt em discussão de transporte. Cabeçalhos impressos/PDF conferidos na extração. Sem nova inspeção visual, leitura integral ou nova consulta a Chorin–Hald; exemplar privado não distribuído. Contagens, figura e exercícios próprios; sem dados ou resultados da IC.

Verificação:14 testes de catálogo aprovados;823 estruturas MathML conferidas. Laboratório racional executado para n0..8: enumera todos os caminhos e compara lei final com coeficientes binomiais; médias e covariâncias em todos os pares de tempos; caso de referência, amplitude errada e contratos. Domínio n0..10 explicitamente pequeno/exponencial. Não é prova do limite funcional, gerador gaussiano ou fenômeno físico. No navegador390px, exercício4 rejeitou0 e aceitou3/8 pelo Enter; figura inspecionada em `passeio-escala-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados. Revisão pessoal pendente.

ProcessosEstocásticos:25 aulas/120 exercícios, sete recortes desenvolvidos e18 introduções curtas. Global51 trilhas,552 aulas/4539 exercícios e185 introduções curtas; sem curso completo ou domínio pessoal certificado. Próxima revisão20min: reconstruir a tabela de quatro passos, derivar escala e explicar independência de incrementos versus correlação de valores. Próxima elaboração global: consultar uma introdução de FísicaMatemática e suas fontes, mantendo alternância. Saldo semanal78%; parada65% mantida.
