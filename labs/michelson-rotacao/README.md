# Michelson–Morley: rotação e cancelamento numérico

Laboratório original, entradas prescritas; não usa medições históricas. Todas as distâncias e λ na mesma unidade, c nessa unidade por unidade de tempo. β=v/c real com |β|<1; braços positivos, retos e perpendiculares. Modelo histórico: éter estacionário, velocidade c isotrópica nesse referencial, cinemática galileana, braços sem contração, tempo absoluto. Luz coerente ideal, v alinhada inicialmente ao braço1; rotação90° troca papéis mantendo rótulos. λ é definida por uma frequência prescrita ν=c/λ nesse modelo; efeitos de meio, emissão/detecção, dispersão, placas e vibração omitidos. Fórmula de franjas é a comparação ideal do tempo de percurso, não simulação óptica completa.

`ether_times` retorna tempos por braço antes/depois. `rotation_change` retorna mudança assinada de t1−t2; `fringe_shift` seu módulo vezes c/λ, calculado diretamente. Para r=√(1−β²), g=1/r²−1/r=β²/[r²(1+r)]; forma racionalizada evita subtrair números quase iguais. Não transforma β pequeno em medição física ou precisão ilimitada: float pode perder β² por underflow, intermediários extremos podem transbordar e |β|≈1 é mal condicionado. Entradas finitas garantem domínio formal, não resultado finito para toda escala extrema; testes e exemplos usam escalas moderadas.

`relativistic_proper_times` calcula2Li/c no aparato inercial com comprimentos próprios fixos, nas orientações estáticas. Não simula a rotação transitória. Braços desiguais podem ter diferença estática sem sinal de rotação; igualar uma diferença estática a movimento absoluto é incorreto. Comparar observadores externos requer contração longitudinal e dilatação do tempo consistentes, explicadas na aula.

Exemplo sintético c=1, β=3/5, L1=3,L2=2,λ=1/2: tempos antes75/8 e5; depois15/2 e25/4. Mudança−25/8, sinal6,25franjas. Velocidade grande escolhida para clareza; não representa velocidade orbital ou valores usados em1887. Com L1=L2=4m,λ=500nm e β=10^-4, aproximação dá0,16franja e exato≈0,160000002. Não é previsão calibrada para equipamento real.

Executar da raiz:
```
python3 labs/michelson-rotacao/rotation.py
python3 -B -m unittest discover -s labs/michelson-rotacao -t .
```
Seis testes: interceptações racionais do caso3–4–5,18 comparações de mudança com tempos independentes Decimal80; limite quadrático e cancelamento; escalas/unidades/troca dos braços/sinal de velocidade; tempos próprios e mudanças rotuladas; contratos. Testes de modelos/cálculo não validam pedagogia, experimento ou domínio de Jhuann.

Fontes consultadas parcialmente em29/10/2026: Nussenzveig,Curso de Física Básica4,2ª2014,reimpressão2017/digital2018,§6.1 pp147–149 e§6.2 pp149–152/PDF148–153; p150/PDF151 inspecionada visualmente para equações e construção transversal. Trecho de p153 extraído incidentalmente,sem estudo de§6.3 aqui. Livro privado não copiado. Feynman/Caltech,I§15–3,trecho do aparato/rotação e compensação por contração,consulta parcial online; fonte usa convenções históricas e não é transposta para toda dinâmica. https://www.feynmanlectures.caltech.edu/I_15.html#Ch15-S3
JúpiterCCM0222 reaberto29/10/2026,ativação01/01/2025;itens1–3. Compatível com aprovação2026/1,sem comprovar versão ministrada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0222

Figura,código,exemplos e exercícios próprios com apoio de IA; revisão pessoal pendente. Resultado nulo restringe uma combinação de hipóteses; não prova sozinho toda relatividade ou inexistência de qualquer teoria alternativa. Não há novos limites experimentais ou dados modernos neste recorte.
