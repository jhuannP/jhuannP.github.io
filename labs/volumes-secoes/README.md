# Volumes por seções, discos e anéis

27/10/2026. Material original com apoio de IA, rascunho para revisão pessoal. Ligado ao grupo parcial de aplicações da integração em Matemática I, sem certificar cobertura ou domínio.

## Hipóteses e dedução

No enquadramento de sólidos mensuráveis e seções integráveis, Cavalieri compara sólidos pela área dos cortes. Degraus s≤A≤t dão sólidos de volumes ∫s e ∫t; aprisionar V entre essas integrais e usar integrabilidade dá V=∫A. Isso resume o argumento, sem construir toda a teoria de medida. Cortes são perpendiculares ao eixo de integração.

Região original x≤y≤2−x, 0≤x≤1, giro em y=0: R=2−x,r=x e A=π(4−4x). V=2π unidades³. Em x=1/2: R=3/2,r=1/2,A=2π. Não é π(R−r)²: a fórmula errada daria volume 4π/3. Coordenadas têm a mesma unidade de comprimento; área em unidade² e volume em unidade³.

Somas uniformes em [0,1], área decrescente: esquerda/π=2+2/n e direita/π=2−2/n, limites superior/inferior. Diferença 4π/n. Em n=4, fatores 3/2 e 5/2; a aula usa esses limites. O volume está contido em cilindro de raio 2/comprimento 1, volume 4π. Não extrapolar a regra de limites para qualquer função.

Estender a região entre as retas para [0,2] exige trocar raios em x=1: A=π|4−4x| e V=4π. A integral assinada sem troca daria zero, incorretamente. Em [0,1], eixo y=3 dá R=3−x,r=1+x,A=π(8−8x), V=4π. Eixo y=1 atravessa o segmento: disco de raio 1−x, V=π/3; não anel de área zero. Ao ampliar todas as dimensões por λ, o volume muda por λ³.

## Fonte

Apostol, Calculus vol. I, 2ª edição (1967), §2.12 pp.111–114/PDF131–134; Teorema 2.7 p.113/PDF133 e discos/anéis p.114/PDF134. Consulta textual parcial e correspondência paginada em 27/10/2026; p.114/PDF134 também inspecionada visualmente. Resumo próprio do enquadramento/prova; região, números, figura e exercícios originais. Não se distribui o PDF privado nem se reproduzem problemas da fonte. O programa curricular público não foi reaberto; mapa preserva a limitação de versão da turma.

## Código e verificação

`slices.py`: int/Fraction, sem bool/float; x∈[0,2], eixos implementados y=0,1,3. A/π calculada por distâncias com teste se eixo cruza segmento. `riemann` usa n=1..4096, esquerda/direita/meio em [0,1]. `exact_volume_factor` retorna V/π para [0,1] ou [0,2]. Não é integrador geral, não implementa cascas, área de superfície ou todos os sólidos de revolução.

Da raiz: `python3 -m unittest discover -s labs/volumes-secoes -t .`. Cinco testes: geometria em 33 cortes e três eixos; integração de Simpson independente e exata para os polinômios de cada metade; limites e erro de ponto médio; contraexemplos/simetria; contratos. Em eixo y=1, volume/pi menos ponto médio =1/(12n²); nos outros dois eixos ponto médio é exato neste modelo linear. Garantias não generalizadas a integrandos arbitrários.

Respostas dos 12 exercícios: 3/2;1/2;2;2;5/2;3/2;4;4;1/3;8; área de anel como diferença de quadrados; troca de raios necessária. Resoluções na aula.

Revisão proposta em duas sessões: região/corte/volume e limites; depois novos domínios/eixos. Pendentes: cascas, sólidos gerais, trabalho e outras aplicações, revisão pessoal e preparação das notas pessoais de Jhuann.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 755 fórmulas MathML conferidas. Texto dos limites n=4 revisto para 3π/2 e 5π/2. A 390 px, volume/pi rejeitou 4/3 e aceitou 2 pelo Enter; interpretação do anel aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.


## Extensão de28/10/2026 — outra região e o cone

Preserva o estudo anterior acima. `sections.py` integra V/π para raios lineares R=R0+R1x e r=r0+r1x em[a,b]. Verifica0≤r≤R nos extremos; linearidade garante essas desigualdades no intervalo. Não generalizar esse teste a funções não lineares. Entradas int/Fraction, coordenadas na mesma unidade; volume em unidade³ depois de multiplicar porπ.

Novos exemplos originais: cone R=x,r=0,[0,1],V/π=1/3; R=1+x,r=x,V/π=2; região0≤y≤x girada em y=2,R=2,r=2−x,V/π=5/3. O laboratório não calcula área de superfície. Para o cone, somas esquerda/meio/direita n4:7/32,21/64,15/32. Erro exato do meio1/(12n²), não uma regra para todo integrando.

Fonte adicional reconferida parcialmente: ApostolI §2.12 pp.111–113/PDF131–133 por texto; p.113/PDF133 também por imagem,28/10. Enquadramento de Cavalieri, seções integráveis e Teorema2.7, sem leitura integral ou cópia. Figura `raios-lineares.svg` original.

Da raiz, execute `python3 labs/volumes-secoes/sections.py` e `python3 -m unittest discover -s labs/volumes-secoes -t .`. Nove testes aprovados: cinco anteriores e quatro da extensão (exemplos, aditividade/escala, somas e contratos). Revisão pessoal pendente.
