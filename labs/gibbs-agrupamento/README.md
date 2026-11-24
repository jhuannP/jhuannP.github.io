# Entropia de Gibbs e informação interna dos grupos

27/10/2026. Material original com apoio de IA, rascunho para revisão pessoal. Percurso complementar, estudo sistemático pessoal ainda a iniciar.

## Modelo e contas

M estados rotulados, p_i≥0, Σp_i=1, log natural. H=−Σp_i ln p_i adimensional (nats), S=kB H em J/K se kB em J/K. Na implementação e números kB=1. Extensão em zero: p=e^(−t), −p ln p=t exp(−t)→0.

Máximo sem outras restrições: D(p||u)=ln M−H(p)≥0, u uniforme. A prova usa ln t≤t−1 em t=u_i/p_i, somando somente p_i>0; a massa de u nesses índices é ≤1. Igualdade só na uniforme global. Não supõe dinâmica nem taxa de relaxação.

Exemplo p=[1/2,1/4,1/8,1/8], A={0,1}, B={2,3}. Hmicro=(7/4)ln 2≈1,21301. Massas 3/4,1/4; condicionais [2/3,1/3] e [1/2,1/2]. Hgrupo=2ln 2−(3/4)ln 3≈0,56234; média interna=(3/4)ln 3−(1/4)ln 2≈0,65067. Soma recupera Hmicro.

Regra geral: p_i=P_a r_i|a e ln p_i=ln P_a+ln r_i|a implicam Hmicro=Hgrupo+Σ_a P_a H(r|a). Grupo nulo não tem razão especificada; contribuição ponderada zero. Só se r interno for uniforme vale H(r|a)=ln g_a.

Preservando as massas dos grupos, q=[3/8,3/8,1/8,1/8] maximiza H, com H(q)=3ln 2−(3/4)ln 3≈1,25548. D(p||q)=H(q)−H(p)≈0,04247. Não é a mesma diferença Hmicro−Hgrupo≈0,65067. Uniformizar aumenta Hmicroscópico; registrar só o grupo usa um rótulo com menor H. Nenhuma operação demonstra evolução física ou segunda lei. Os grupos deste exemplo não são definidos como níveis de energia.

## Referência

[David Tong, Statistical Physics, §1.3.3](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html): consulta parcial em 27/10/2026, equação (1.30), caso equiprovável e início de Maximizing Entropy. Fonte HTML sem página impressa atribuída. Regra de agrupamento, prova via desigualdade logarítmica, partições, exemplos, figura, código e exercícios próprios; sem reproduzir problemas ou integralidade das notas.

## Código e verificação

`gibbs.py` exige massas int/Fraction com soma exata 1; rejeita bool/float. Agrupamento exige partição completa dos índices, grupos não vazios e sem repetição. Massas, condicionais e uniforme interna são racionais; entropias e D são float. Condicional de grupo nulo retorna None, não vetor de zeros. D retorna infinito se p_i>0 e q_i=0. Os logaritmos usam numerador/denominador; não há promessa de precisão arbitrária: contribuições abaixo da resolução float podem se perder e desigualdades muito próximas exigem tolerância. Não trata distribuições contínuas, entropia diferencial ou matrizes densidade.

Da raiz: `python3 -m unittest discover -s labs/gibbs-agrupamento -t .`. Cinco testes: referências/uniformes; 320 combinações distribuição-partição verificando cadeia e limites; exemplo e candidatos sob massas fixas; grupos nulos, permutações e suporte de D; contratos. Os testes verificam este laboratório finito, não toda a teoria ou sua adequação a um experimento físico.

Preservados os exercícios eg1/eg2, o exemplo binário, Python anterior, desafio e painel entropyBinary. Dez questões novas: 7/4;3/4;2/3;Hgrupo; média interna;3/8; diferença ≈0,04247; condição de uniformidade; grupo nulo; ausência de dinâmica. Resoluções completas na aula.

Revisão proposta em duas sessões: reconstruir a cadeia com o exemplo; depois maximizar mantendo massas fixas e explicar as duas diferenças de entropia. Pendentes: reservatório/canônico, conexão dinâmica, medidas contínuas e revisão conceitual pessoal.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 746 fórmulas MathML conferidas. Em 390 px, eg5 rejeitou 0,5 e aceitou 2/3 por entrada decimal pelo Enter; eg10 aceitou a condição de uniformidade. Painel nos extremos e no máximo conferido; −0 dos extremos é representação float de zero. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
