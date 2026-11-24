# Itô e Stratonovich: converter a deriva

Complemento original,escalares suaves,com apoio existente `labs/ito-variacao/ito.py`. Executar da raiz para resolver esse módulo; não é arquivo autônomo isolado. Sem instalação ou geração de trajetórias aleatórias.

`python3 -B -m unittest discover -s labs/strato-conversao -t .`
`python3 -B -m labs.strato-conversao.convert`

`conversion(aS,b,bprime)` recebe valores pontuais e devolve aI. Para b(X)=sigmaX,aS(X)=alphaS X, comparar coeficientes com b=sigma,bprime=sigma dáalphaI=alphaS+sigma²/2; não confundir coeficiente com valor da deriva em outro X. `linear_exponent` devolve **log(XT/X0)**,paraX0>0,não XT. W é valor prescrito para avaliar fórmula,sem inferir uma trajetória real ou condicionar a um evento pontual.

`compare` reutiliza `square_sums` do apoio. Soma simétrica usa média dos valores deWnos extremos,**não** o valor em tempo intermediário não observado. ParaW como integrando,é aproximação simétrica padrão; na gradefinita,S−L=Q/2. Pavliotis apresenta ponto médio temporal; não afirmamos igualdade das duas somas em gradefinita.

Grades racionais prescritas com tempo final1 e quatro intervalos: A=(1/2,−1/2,1/2,1/2)temWT1,Q1,L0,S1/2;B=(1/4,1/4,1/4,1/4)temWT1,Q1/4,L3/8,S1/2. Não são amostras certificadas de Browniano. Subdividir cada incremento linearmente em duas metades reduzQpela metade: é refinar interpolação suave,sem demonstrar o limite brownianoQ→T.

Referência teórica separada: incrementos independentes N(0,T/n) implicam E Q=T,VarQ=2T²/n. LimiteL² fornece Itô∫W dW=(WT²−T)/2 e simétricaStratonovich∫W∘dW=WT²/2,comW0=0. A construção geral não é provada aqui. Não há solverSDEgeral.

Fonte local: Pavliotis,Stochastic Processes and Applications2014,§3.2pp58–62/PDF71–75,consulta textual parcial30/10/2026;p62/PDF75visual para sinais da conversão. Notação da fonte b=deriva,σ=difusão; nossa aula usa a,b respectivamente. Capítulo5prévio permanece contexto,mas a conversão lida está em3.2. Não copiados figura/exercício;contas finitas e diagramas locais. Revisão pessoal pendente.
