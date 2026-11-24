# Trabalho, atrito e domínio — rascunho

Aula `ef-energia`, percurso próprio de Física do Ensino Médio, 14 seções/12 exercícios. Preserva título, exemplo K=9 J, dois exercícios antigos e desafio de quadruplicar K. Código original, Python opcional, sem evidência de experimento real ou domínio pessoal.

## Fontes consultadas parcialmente em 22/10/2026

- OpenStax Physics [§9.1](https://openstax.org/books/physics/pages/9-1-work-power-and-the-work-energy-theorem): trabalho–energia e unidades; [§9.2](https://openstax.org/books/physics/pages/9-2-mechanical-energy-and-conservation-of-energy): energia mecânica e transformações.
- OpenStax College Physics 2e [§7.1](https://openstax.org/books/college-physics-2e/pages/7-1-work-the-scientific-definition): ângulo e sinais; [§7.3](https://openstax.org/books/college-physics-2e/pages/7-3-gravitational-potential-energy): sistema, referência e ΔU.

Síntese original e derivações próprias. Sem transcrição de exercícios ou figuras; nenhum livro privado consultado ou copiado neste bloco. Esses textos apoiam um percurso próprio, não equivalência de programa oficial USP. Conservação mecânica exige condições além do isolamento: o texto distingue as conversões internas.

## Modelo e limites

Bloco inicialmente deslizando à direita, m1..4kg, v₀1..6m/s, força aplicada F0..8N à direita, atrito cinético f0..8N contrário. Apoio horizontal fixo. Peso e normal têm trabalho nulo. O módulo f é fornecido, não estimado por μ. Distância inteira0..12m. K=mv₀²/2+(F−f)d somente enquanto a trajetória for admissível até a primeira parada. Se f>F, d_s=K₀/(f−F). Além de d_s, `reachable=False` e `query_k=None`; os campos de balanço terminam explicitamente em `end=d_s`. Não há extrapolação de energia negativa, parada mantida por hipótese escondida ou inversão com atrito de sinal fixo.

No sistema bloco+superfície, sob ausência de outras trocas/armazenamentos macroscópicos, ΔK+ΔE_interna=Fd e ΔE_interna=fd. Não se determina quanto aquece cada corpo nem sua temperatura. Padrão m2,v3,F2,f5,d2: K0=9,K=3,WF4,Wf−10,Wtotal−6 J; parada3m. Na parada: WF6,Wf−15,ΔK−9,ΔE_interna15 J.

## Experiência de leitura

Manter composição editorial clara, fórmulas curtas em azul e controles com unidades. Sequência: sistema e sinais → derivação → exemplo → domínio → conservação → exercícios. Gráfico de energia versus distância com tabela, sem animação decorativa ou associação entre distância e tempo. Navegação e soluções já existentes preservadas.

## Verificação e revisão

`python3 -m unittest discover -s labs/trabalho-atrito -t .`

Quatro testes: 1944 configurações de forças/massa/velocidade conferidas por Newton e cinemática em tempo escolhido; 1053 configurações de consulta com balanços e domínio; fronteira exata/resultante zero/escala; contratos. `reference.json`:405 estados para comparação com JavaScript. Uma consulta fora do domínio não é evidência de comportamento depois da parada.

Próxima revisão pessoal: resolver o caso padrão sem consultar soluções e explicar os dois sistemas. Cobertura restante: molas, rampas, forças variáveis, problemas integradores, escolha de referencial, medições reais e plano de aula com aluno. Nenhum curso completo.
