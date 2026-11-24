# Corpos finitos e trabalho máximo

Modelo original: dois corpos rígidos em equilíbrio interno, mesma capacidade térmica total C constante, temperaturas absolutas, sem mudança de fase ou outras reservas energéticas. O conjunto troca apenas trabalho com o exterior; motor ideal retorna ao estado inicial e não acumula energia ou entropia. Sem previsão de duração ou potência.

## Derivação

No contato direto sem trabalho: Tf=(Th+Tc)/2 e ΔS=C ln(Tf/Th)+C ln(Tf/Tc)>0 quando Th≠Tc.

Para extrair trabalho reversivelmente por uma sucessão ideal de ciclos entre as temperaturas instantâneas dos corpos, a entropia total é constante. Ao terminar com temperatura comum Tr: C ln(Tr/Th)+C ln(Tr/Tc)=0, portanto Tr=√(ThTc). A primeira lei dá Wmax=C(Th+Tc−2Tr)=C(√Th−√Tc)². São capacidades iguais; para capacidades distintas, esta média geométrica simples não vale.

Para qualquer processo no mesmo sistema, com mesmo estado final comum e motor retornado, ΔS≥0 exige Tf≥√(ThTc). Como W=C(Th+Tc−2Tf), segue W≤Wmax. O limite exige reversibilidade ideal; não garante motor real ou potência finita.

Cenário próprio: C=2 J/K, Th=400 K,Tc=100 K. Reversível: Tr=200 K,Qh=400 J,Qc=200 J,Wmax=200 J. Contato direto: Tf=250 K,W=0,ΔS=2 ln(25/16) J/K. O armazenamento inicial de energia é igual, mas os estados finais diferem em energia e entropia.

Ao longo da trajetória reversível, H*K=ThTc. O rendimento instantâneo 1−K/H diminui até0. Qh é removido do quente, Qc adicionado ao frio, ambos positivos. δW=(1−K/H)δQh; δQh=−C dH. A integral C∫[√(ThTc),Th](1−ThTc/H²)dH recupera Wmax. Usar ηinicial=3/4 com todo Qh=400 J daria300 J, incorreto. Este erro não viola uma identidade de Carnot; troca temperaturas variáveis por constantes.

## Código

Python3, biblioteca padrão. `compare` calcula dois cenários; `path` amostra estados da solução analítica, não executa ciclos discretos reais. Raios/pressões não entram. Limites didáticos:50≤Tc≤Th≤2000 K,0,01≤C≤10000 J/K,até200 intervalos. Não se assume capacidade real constante nessa faixa para qualquer material.

Execute `python3 labs/corpos-trabalho/work.py`; testes `python3 -m unittest discover -s labs/corpos-trabalho -t .`. Quatro testes: cenário/primeira lei, entropia e escala, trajetória/quadratura Simpson independente e contratos. Erros float pequenos não substituem provas ou medição.

Fontes consultadas parcialmente em29/10/2026: Nussenzveig, Curso de Física Básica2,5ªed2014,§10.8(iii),pp.275–276/PDF276–277, texto de contato térmico e entropia (sem nova inspeção visual/leitura integral); [MIT16.050, Applications of the Second Law §1.C.1](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/43887003168fb3f855d788324fac0527_05_part1c.pdf), pp.1C-1–1C-2/PDF1–2, consulta textual parcial a balanço de motor, entropia e máximo reversível para reservatórios fixos. As convenções de sinal da fonte diferem; aqui Qh e Qc são módulos. Extensão de corpos finitos e exemplo derivados nas notas; não atribuídos como exemplo da fonte. Sem figura, exercícios ou código copiados/PDF distribuído.

Programa CCM0122 não reaberto neste bloco; registro29/10/ativação01/01/2025 posterior à turma2024 preservado, versão ministrada desconhecida. Material em rascunho; capacidades variáveis, transições de fase, irreversibilidade dinâmica e revisão pessoal pendentes.
