# Som e Doppler — notas originais em elaboração

16/10/2026. Revisão de Jhuann pendente.

## Som é uma perturbação mecânica do meio

Em um fluido, o som envolve pequenas variações de pressão, densidade e velocidade das partículas em torno de um estado de equilíbrio. Na onda plana longitudinal, as partículas oscilam paralelamente à propagação. Elas não percorrem, junto com a frente, toda a distância entre fonte e receptor. Este modelo não descreve propagação de som no vácuo.

## A rapidez depende das propriedades do meio

Para pequenas perturbações adiabáticas num fluido uniforme, c²=B_s/ρ, com B_s o módulo volumétrico adiabático e ρ a densidade de equilíbrio. Para gás ideal com capacidades constantes, c²=γRT/M. A temperatura entra em kelvin e M é massa molar. Usaremos c=340 m/s como valor sintético constante, não como valor universal para qualquer ar.

## Frequência, comprimento e intensidade descrevem coisas distintas

Uma onda plana harmônica pode ser escrita p′(x,t)=p_a cos(kx−ωt), com k=2π/λ e ω=2πf. No meio em repouso vale c=λf. Para onda progressiva linear, a intensidade média é p_a²/(2ρc), usando amplitude de pressão de pico; com pressão eficaz, seria p_rms²/(ρc). Frequência controla repetição temporal, não a intensidade. A demonstração abaixo não calcula potência ou decibéis.

## Fixe primeiro o eixo e o referencial

O meio está em repouso. A fonte começa em x=0 e o observador em x=D>0. Estudamos frentes que viajam para a direita com rapidez c. v_s e v_o são velocidades algébricas da fonte e do observador nesse referencial: positivo significa direita para ambos. A fórmula vale enquanto o observador está à direita da fonte para as emissões consideradas; após cruzarem, a direção relevante muda.

## Uma fonte móvel muda a distância entre frentes

A fonte emite frentes separadas por T_s=1/f_s. Nesse intervalo, a primeira frente anda cT_s e a fonte avança v_sT_s. À frente da fonte, a separação é λ=(c−v_s)T_s=(c−v_s)/f_s. Se v_s>0, as frentes à direita ficam mais próximas. A emissão mantém f_s no relógio newtoniano da fonte, mas a frequência medida num ponto fixo do meio pode mudar.

## O observador também muda a taxa de encontros

As frentes à direita movem-se a c, e o observador a v_o. A velocidade de encontro é c−v_o. Assim f_o=(c−v_o)/λ=f_s(c−v_o)/(c−v_s). Observador indo para a direita acompanha as frentes e recebe menos por segundo; indo para a esquerda encontra mais. Não use a palavra aproximação para escolher um sinal sem desenhar a geometria.

## O tempo de chegada confirma os dois sinais

A frente emitida no instante t_e sai de x_s=v_st_e e satisfaz x=v_st_e+c(t−t_e). O observador está em D+v_ot. Igualando as posições, t_a=[D+(c−v_s)t_e]/(c−v_o). Para emissões separadas por 1/f_s, as chegadas diferem por Δt_a=(c−v_s)/[f_s(c−v_o)]. O inverso é a frequência recebida. A distância inicial afeta o atraso, não esse intervalo enquanto as velocidades são constantes.

## Mesma velocidade relativa não basta para som

Compare c=340 m/s e f_s=100 Hz. Fonte a +34 com observador parado dá f_o=1000/9≈111,11 Hz. Fonte parada com observador a −34 dá 110 Hz. Nos dois casos a separação diminui a 34 m/s, mas os resultados diferem porque o meio define como se propagam as frentes. Se ambos têm a mesma velocidade subsônica, f_o=f_s nesta geometria.

## Subsônico é uma hipótese do percurso

Exigimos |v_s|<c e |v_o|<c para que os denominadores e a ordem dos encontros tenham a interpretação usada. Em v_s→c pela esquerda, a expressão cresce, mas isso não autoriza uma frequência infinita física: tamanho da fonte, dispersão, não linearidades e choque precisam de outro modelo. Movimento supersônico e cone de Mach não são tratados pela fórmula desta aula.

## Luz e astronomia pedem outro modelo

A fórmula aqui depende de um meio e de velocidades galileanas. Não a use para espectros luminosos, redshift cosmológico ou velocidades relativísticas. Esses assuntos exigem outra derivação e hipóteses. A conexão útil para estudo futuro é aprender a identificar o mecanismo de propagação e o referencial antes de aplicar uma expressão com o mesmo nome.

## Um experimento pode começar pela contagem de encontros

No laboratório Python, cada emissão é acompanhada até sua interseção com o observador. Compare intervalos de chegada e confira a posição de cada frente. Isso é experimento computacional sintético, sem microfone nem gravação. Para medição futura, planeje condições de movimento, rapidez do som, atraso e incerteza antes de interpretar dados. Reflexão/eco pode produzir duas mudanças Doppler e precisa de análise separada.

## Exemplo resolvido

Uma fonte emite 100 Hz e move-se a +34 m/s no meio. Um observador à sua direita move-se a −34 m/s. Use c=340 m/s antes do cruzamento.

A fonte avança para a direita e o observador vem para a esquerda: ambos aproximam-se, com sinais definidos pelo mesmo eixo.

λ=(340−34)/100=3,06 m.

A rapidez de encontro é 340−(−34)=374 m/s.

f_o=374/3,06=1100/9≈122,22 Hz.

O intervalo de chegada é 9/1100 s≈0,00818 s.

Para D=340 m, a primeira frente emitida em t=0 chega em 340/374=10/11 s; esse atraso não é o período recebido.

## Resoluções

Com c=340 m/s, f_s=100 Hz e v_s=+34 m/s, qual λ à direita em metros?

(340−34)/100=3,06 m.

Com fonte parada, f_s=100 Hz, c=340 m/s e observador a +34 m/s, qual f_o em Hz?

100×(340−34)/340=90 Hz.

Nas mesmas condições, mas observador a −34 m/s, qual f_o em Hz?

100×(340+34)/340=110 Hz.

Se fonte e observador se movem ambos a +34 m/s, com f_s=100 Hz, qual f_o em Hz?

Os fatores c−34 cancelam, dando 100 Hz.

No exemplo resolvido, qual f_o em Hz? Aceita fração.

f_o=1100/9≈122,22 Hz.

Uma partícula do fluido viaja junto com a frente sonora até o receptor?

No modelo linear, as partículas oscilam localmente; a perturbação se propaga.

Apenas a velocidade relativa fonte–observador determina o Doppler acústico?

As velocidades em relação ao meio aparecem separadamente.

A distância inicial D muda a frequência com velocidades constantes nesta geometria?

Muda o atraso inicial; a diferença entre chegadas sucessivas não depende de D.

A fórmula acústica pode ser aplicada diretamente ao redshift de luz?

Luz e cosmologia exigem modelos próprios, não um meio acústico galileano.

## Roteiro didático e evidência

Pré-requisitos: onda viajante, frequência, comprimento de onda e equações de movimento uniforme. Desenhar fonte, receptor e direção das frentes; derivar λ e só então a frequência. Pedir duas situações com mesma velocidade relativa e resultados diferentes. Produto de compreensão: diagrama próprio e conferência comentada dos eventos de emissão e chegada. Não há gravação, áudio ou medição real.

## Fontes e limites

Escopo: [CCM0122 no Júpiter](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0122), consultado em 16/10/2026; ativação 2025 posterior à turma. Feynman I e Nussenzveig II identificados no acervo no mapa curricular. Texto e problemas originais, sem reproduzir os livros.

Os testes usam aritmética racional e interseções entre frentes e observador para conferir período recebido e tempo de voo. O gráfico da interface mostra frequência versus velocidade da fonte, para uma velocidade de observador fixada; não é forma de onda nem trajetória. Falta derivar a equação acústica e intensidade a partir das equações do fluido, tratar eco, batimentos e geometrias gerais.
