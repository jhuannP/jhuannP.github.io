# Gás ideal: estado não determina o processo

Quantidade fixa de gás ideal, p/T absolutos e estados extremos homogêneos. r=V2/V1, θ=T2/T1, π=p2/p1; a equação de estado exige πr=θ. Escala de energia nRT1=p1V1. Convenção ΔU=Q−W com trabalho positivo feito pelo gás.

Isotérmica reversível: θ=1, π=1/r, W/(nRT1)=ln r, ΔU=0, Q=W. Adiabática reversível com γ=Cp/Cv constante: θ=r^(1−γ), π=r^(−γ), W/(nRT1)=(1−θ)/(γ−1), Q=0 e ΔU=−W. Derivação da relação de temperatura explicitada na aula, usando dU=nCv dT e nCv=nR/(γ−1).

Expansão livre: gás inicialmente em parte de recipiente rígido isolado, outro compartimento evacuado; ao remover separação, Q=W=0. Gás ideal tem U(T), logo θ=1 e π=1/r após equilíbrio. Não existe curva de estados homogêneos ao longo do processo para calcular trabalho como área sob a isoterma. Mesmos extremos da isotérmica, trabalhos/calores diferentes. Não aplicar pV^γ constante apenas porque Q=0.

Exemplo próprio: T1=300 K, V1=0,003 m³, nR=2 J/K, p1=200000 Pa e escala 600 J. Para r=2: isotérmica p2=100000 Pa e W=600 ln2≈415,89 J; adiabática reversível γ=5/3 dá T2≈188,99 K, p2≈62996 Pa e W≈333,04 J; livre dá T2=300 K, p2=100000 Pa, Q=W=0. Não são dados ou gás real identificados.

Na raiz do site:

    python3 -m labs.gas-processos.processes
    python3 -m unittest discover -s labs/gas-processos -t .

Contrato: int/float finitos sem bool, r≥1 e γ>1, processo entre os três nomes documentados no código. Saídas normalizadas. expm1 evita cancelamento na expressão de trabalho perto de γ=1; isso não elimina todo arredondamento nas razões de estado. Valores extremos que arredondam pressão/temperatura positiva para zero são rejeitados. Sem compressões, estimação de parâmetros ou simulador do transiente livre.

Seis testes conferem mesmos extremos/trabalho diferente, referência r=4 γ=3/2, estados e primeira lei em 45 configurações, integração de curvas reversíveis por pontos médios com refinamento, limite γ próximo de 1 e contratos/representação. Integração numérica não é aplicada à expansão livre.

Fontes consultadas parcialmente por texto em 22/10/2026: Nussenzveig, Curso de Física Básica vol.2, 5ª ed., §9.1 pp.229–230/PDF230–231 e início de §9.4 pp.240–241/PDF241–242, incluindo final de §9.3; cabeçalhos confirmam paginação impressa, sem nova inspeção visual. [OpenStax vol.2 §3.6](https://openstax.org/books/university-physics-volume-2/pages/3-6-adiabatic-processes-for-an-ideal-gas) fundamenta adiabática e expansão livre. Constância de capacidades é hipótese, não conclusão universal sobre qualquer gás ideal. Figura, contas e exercícios próprios; nenhum exemplar privado distribuído.

Aula f2-gas-ideal ampliada para onze seções/doze exercícios. As duas frases antigas foram qualificadas para não omitir reversibilidade ou contradizer a expansão livre. Exemplo curto preservado com unidade/reversibilidade explícitas; Python/desafio anteriores preservados. Rascunho assistido por IA para revisão pessoal. Próxima revisão: explicar por que estado final não fornece trabalho e por que adiabático não significa reversível. Entropia, capacidades variáveis, gases reais e tempo de evolução continuam pendentes. Grupo curricular segue parcial.

Verificação: seis testes novos e 13 de catálogo aprovados; 546 estruturas MathML conferidas. No navegador em 390 px, figura legível e questão do trabalho livre rejeitou 415,89 e aceitou 0. Largura igual à tela e nenhum erro de console observado. Prévia: gas-processos-mobile.jpg. Não houve revalidação integral da suíte global ou de outros painéis. Catálogo: 501 aulas/3168 exercícios em rascunho. Saldo semanal após bloco: 91%; parada em 65%.
