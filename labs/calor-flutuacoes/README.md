# Flutuação e resposta térmica num ensemble finito

Rascunho original29/10/2026. Fonte pública David Tong,Statistical Physics,§1.3.2, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html#S1.SS3.SSS2 . Consulta parcial às Eqs.1.25–1.27 e contexto;sem leitura integral ou cópia de exemplo/figura. Derivação finita,modelo com degenerescência3,testes e desenho próprios. Nenhum novo livro privado consultado.

Theta=kB*T tem unidade de energia;níveis eTheta são números na mesma unidade. Retorna U,Var(E) e C/kB=Var(E)/Theta². A derivada dU/dTheta equivale a C/kB,não C em J/K sem conversão. Níveis/degenerescências fixos:sem variação de volume,campo,número de partículas ou Hamiltoniano comT. Não simula dinâmica,calorimetria ou autocorrelação.

Da raiz: `python3 -m unittest discover -s labs/calor-flutuacoes -t .`; `python3 labs/calor-flutuacoes/heat.py`.

Quatro testes:fixture,81casos contra enumeração de microestados e diferenças centrais,origem de energia/escala/cópias independentes,contratos. Até30níveis,degenerescências1..1000,energias módulo≤1e4 eTheta1e−4..1e4. Log-pesos deslocados e variância centralizada;underflow pode apagar estados numericamente desprezíveis,sem certificação global de arredondamento. Script anterior preservado,testes novos não certificam todos os seus domínios.

Modelo escolhido E0=0,E1=Δ=1,g0=1,g1=3. EmTheta=1/ln3,as duas probabilidades de nível são1/2,U1/2,variância1/4,C/kB=(ln3)²/4≈0,301737. Alta temperatura tende a população excitada3/4,sem calor específico constante por haver apenas dois níveis finitos. Revisão20min:derive ∂βp e C;distinga nível,microestado,variância física e erro padrão. Sem domínio pessoal ou validação da IC comprovados.
