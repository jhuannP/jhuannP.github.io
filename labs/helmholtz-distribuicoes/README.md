# Energia livre de distribuições finitas

Material original, rascunho para revisão de Jhuann. Uma entrada por microestado, energias fixas, temperatura positiva e theta=kB*T_física na mesma unidade de energia de E. q é uma distribuição candidata; não uma trajetória medida ou processo de relaxação. O funcional F[q]=U[q]−theta H[q] é distinto da energia livre de equilíbrio F*=−theta lnZ. O excesso é theta D(q||p*).

Exemplo próprio: E=(0,ε,ε), beta ε=ln2; p*=(1/2,1/4,1/4), q=(1/2,1/2,0). Mesma energia média, entropias diferentes. No código ε=1 em unidade escolhida e theta=1/ln2. Uma função de partição de níveis deve incluir g; a lista aqui já explicita os três microestados. Não introduzir degenerescência novamente.

Fonte primária: David Tong, Statistical Physics §1.3.4, equações1.32–1.36, consulta textual parcial em29/10/2026, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html#S1.SS3.SSS4 . Conferidas definição, controles e relação com Z. Prova variacional finita por ln x<=x−1, exemplo, código e figura desenvolvidos localmente; não atribuídos a um exercício da fonte. Sem nova consulta a Chorin/Pavliotis, sem currículo Júpiter alegado: percurso complementar próprio.

Python padrão, sem dependências. Limites didáticos:2..12 microestados, |E_i|<=10 e .1<=theta<=10; números finitos, rejeita bool/string; q não negativa e normalizada com tolerância1e−12. Energias e theta consistentes em unidade definida pelo usuário; o programa não identifica unidades. Exponenciais deslocadas e logp para evitar subfluxo no contrato; aritmética aproximada, não prova numérica universal. Resíduos da ordem do arredondamento não são diferenças físicas.

Execute da raiz: `python3 -m unittest discover -s labs/helmholtz-distribuicoes -t .`; `python3 labs/helmholtz-distribuicoes/free_energy.py`.

Testes: exemplo analítico/entropia interna;819 distribuições em malha com pesos exponenciais diretos independentes; deslocamento, permutação e derivada central de F; contratos, incluindo faixa extrema. Uma malha não prova mínimo global: a prova está na aula. Sem inferir taxa de relaxação, teorema H dinâmico, trabalho extraível sem protocolo ou resultado da IC.
