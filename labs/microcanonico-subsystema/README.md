# Microcanônico: declarar o conjunto acessível de energia

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: combinações, probabilidade condicional, médias e variância. Não é disciplina adicional do histórico; estudo sistemático da trilha continua a iniciar, conforme registro pessoal.


## Um sítio é um rótulo físico do modelo

Considere N sítios distinguíveis e fixos, cada um com dois níveis: sᵢ=0 tem energia zero e sᵢ=1 tem energia ε, com ε>0. O microestado é a sequência completa (s₁,…,s_N). A energia de interação é desprezada no cálculo de energia. Fixar a energia total E=qε exige exatamente q sítios excitados, com q inteiro entre 0 e N. Aqui q cumpre o papel do m usado no exemplo inicial. Os rótulos são dos sítios, não de partículas idênticas livres; não estamos construindo um gás de bósons ou férmions.

E(s)=εΣᵢsᵢ; Σᵢsᵢ=q

## O ensemble parte das restrições

Num modelo finito com energia E=epsilon sum(s_i), fixar E=m epsilon restringe o número de excitações. O microcanônico ideal atribui pesos iguais aos estados acessíveis sob a hipótese adotada. Não diz que uma trajetória visita todos imediatamente.

energia fixa → subconjunto acessível

## A energia fixa reduz o conjunto acessível

Sem impor energia há 2ᴺ sequências binárias. Com q excitações, basta escolher quais q dos N sítios contêm 1. Logo a multiplicidade global é Ω(N,q)=C(N,q). Para N=8 e q=3, há 56 microestados acessíveis entre os 256 possíveis sem a restrição. As outras sequências recebem probabilidade zero neste ensemble, e não uma pequena chance térmica.

Ω(N,q)=C(N,q)

## Equiprobabilidade é uma hipótese sobre o ensemble

Atribuímos probabilidade 1/Ω a cada sequência acessível. Essa escolha descreve uma distribuição de equilíbrio idealizada; não é uma prova de que qualquer dinâmica alcance ou percorra todos os estados. Sítios estritamente desacoplados não redistribuem energia entre si por esse Hamiltoniano. Preparação do ensemble ou mecanismos fracos de troca exigem hipóteses adicionais, que este laboratório não simula. A uniformidade vale nas sequências globais acessíveis, não automaticamente nos valores de toda grandeza observada.



## Separe o todo em dois conjuntos fixos de sítios

Escolha um subsistema A com a sítios e o complemento B com N−a sítios. Seja X o número de excitações em A. Se X=k, B precisa conter q−k excitações para conservar a energia total. A tem C(a,k) configurações e B tem C(N−a,q−k) configurações. Cada combinação de uma configuração local com outra do complemento produz um microestado global distinto. A contagem de pares é o produto dessas duas multiplicidades.

número global compatível com X=k: C(a,k)C(N−a,q−k)

## Derive a probabilidade da energia local

Divida a contagem de pares compatíveis por Ω(N,q). Isso fornece P(X=k)=C(a,k)C(N−a,q−k)/C(N,q), com max(0,q−(N−a))≤k≤min(a,q). Fora desse suporte a probabilidade é zero. É a mesma forma hipergeométrica da aula de amostragem sem reposição. Aqui não retiramos fisicamente os sítios: observamos um subconjunto fixo de um todo cujas excitações se distribuem uniformemente entre os microestados admitidos.

P(X=k)=C(a,k)C(N−a,q−k)/C(N,q)

## Conte um exemplo finito antes de aproximar

Use N=8, q=3 e a=3. Para k=0,1,2,3, as contagens são C(3,k)C(5,3−k): 10,30,15,1. Somam 56. Portanto as probabilidades são 5/28,15/28,15/56,1/56. A maior massa é X=1, pois esse valor admite 30 dos 56 estados globais. Não há quatro valores locais equiprováveis, mesmo que todos os microestados globais admitidos tenham o mesmo peso.



## Um padrão local não é o mesmo evento que uma contagem

O padrão local 100 tem k=1 e admite C(5,2)=10 configurações do complemento, portanto sua chance é 10/56. O evento X=1 reúne 100,010 e 001: sua chance é 30/56. Já 111 admite apenas uma configuração do complemento, 00000, com chance 1/56. Para um padrão específico de a sítios com k excitações, a probabilidade é C(N−a,q−k)/C(N,q); o fator C(a,k) só aparece quando reunimos todos os padrões com aquela contagem.



## A energia do todo não flutua; a de uma parte pode flutuar

No exemplo, E[X]=(30+2×15+3×1)/56=9/8. E[X²]=(30+4×15+9×1)/56=99/56; subtraindo (9/8)² obtemos Var(X)=225/448. Assim E_A=εX tem média 9ε/8 e variância 225ε²/448. Em cada estado E_B=ε(q−X), de modo que as flutuações das duas partes se compensam exatamente: Cov(E_A,E_B)=−Var(E_A). Uma distribuição não é uma trajetória temporal; não foi calculado tempo de relaxação ou taxa de troca.

E_A+E_B=3ε em todo microestado acessível

## Entropia de Boltzmann usa multiplicidade

S=kB log Omega. Nos exemplos numéricos, kB=1 e log é natural. Para energia contínua, largura da camada e medida de fase precisam ser especificadas; não substitua tudo por uma igualdade exata de floats.

S=log Omega nas unidades usadas

## A entropia global precisa de sua unidade

Para a distribuição global uniforme adotada, S_total=k_B lnΩ. O logaritmo é natural, Ω é contagem sem unidade e S tem unidade J/K quando k_B está em J/K. Escrever lnΩ fornece S/k_B, não uma entropia em joules por kelvin por si só. Com Ω=56, S/k_B=ln56; nos extremos q=0 ou q=N, Ω=1 e S=0 neste modelo. Como os padrões do subsistema não são uniformes, não atribuímos sua entropia simplesmente pelo logaritmo do número de padrões possíveis.

S_total/k_B=ln C(N,q)

## A temperatura envolve uma derivada

Na formulação macroscópica, 1/T=(∂S/∂E) com demais controles fixos. Em sistemas discretos finitos, uma diferença precisa de convenção e não é automaticamente uma temperatura contínua exata.

restrições e escala definem a derivada

## Um complemento finito não é automaticamente um banho canônico

O peso exato de um padrão local depende da multiplicidade do complemento no restante da energia. Não é preciso atribuir temperatura ou peso exponencial para fazer essa contagem finita. A obtenção de um peso canônico envolve uma aproximação da entropia de um reservatório suficientemente grande, com condições próprias. Esse desenvolvimento pertence à aula sobre o reservatório e o peso canônico. Não ajustamos uma temperatura para transformar a tabela finita em distribuição canônica exata.



## O painel e o código respondem perguntas distintas

O painel de multiplicidades já existente explora a contagem global por número de excitações. A nova figura e o laboratório mostram a distribuição de uma parte quando a energia do todo foi fixada. O código usa combinações e frações exatas; testes independentes enumeram sequências binárias pequenas. Energia contínua, medida de fase, largura de camada, dinâmica, ergodicidade e limite termodinâmico continuam pendentes. Esta é uma trilha complementar em rascunho; não comprova disciplina cursada, estudo pessoal ou resultado da IC.



## Exercícios e resoluções

1. Qual S/log6 do exemplo?

   Resolução: S=log6.

2. Microcanônico permite ignorar a restrição de energia na contagem?

   Resolução: A energia define o conjunto acessível.

3. Para N=8 e q=3, quantos microestados globais são acessíveis?

   Resolução: C(8,3)=56, não 2⁸=256.

4. Com a=3, quantos microestados globais são compatíveis com X=1?

   Resolução: C(3,1)C(5,2)=3×10=30.

5. No mesmo exemplo, qual é P(X=1)?

   Resolução: 30/56=15/28.

6. Quanto vale E[X] no exemplo N=8,q=3,a=3?

   Resolução: (30+2×15+3×1)/56=9/8.

7. Qual a probabilidade do padrão local específico 111?

   Resolução: Apenas o complemento 00000 é compatível: 1/56.

8. Com q=3 fixado, qual a chance de um microestado global com só duas excitações?

   Resolução: Ele está fora do conjunto de energia acessível.

9. Os quatro valores X=0,1,2,3 são equiprováveis porque os microestados globais são?

   Resolução: As degenerescências são diferentes: 10,30,15,1.

10. Energia total fixa impede toda flutuação da energia de uma parte?

   Resolução: As partes podem ter energias diferentes entre estados, compensadas no complemento.

11. Se o subsistema contém todos os oito sítios e q=3, qual é Var(X)?

   Resolução: X=3 em todos os estados: não há flutuação da energia total.

12. Para q=0, quanto vale S_total/k_B neste modelo?

   Resolução: Ω=1 e ln1=0.

## Fonte, autoria e limites

[David Tong, Statistical Physics, §1.2 e §1.2.1](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html): consulta parcial em 22/10/2026 para ensemble, equiprobabilidade e entropia de Boltzmann. Os valores N=8,q=3,a=3, o cálculo local por combinações, figura, código e exercícios são desenvolvimento próprio. Não foram copiados enunciados, figuras, soluções ou notas da fonte.

O exemplo inicial de N=4,q=2 e a demonstração global foram mantidos. O novo recorte não assume que energia finita exata substitua a definição por camada em modelos contínuos. A energia de interação é omitida na contagem, sem deduzir daí uma dinâmica de termalização. Nenhuma temperatura, trajetória, taxa de troca ou tempo de relaxação foi modelado. O resultado é sobre o ensemble especificado.

## Reprodução

Na raiz do site, execute python3 -m labs.microcanonico-subsystema.experiment e python3 -m unittest discover -s labs/microcanonico-subsystema -t .

A função subsystem devolve multiplicidade global, contagens e probabilidades por X. pattern_probability trata um padrão local específico. Os testes usam sequências binárias e subconjuntos de sítios, separados da fórmula combinatória. Enumeração é limitada a populações pequenas nos testes; o algoritmo de contagens usa combinações, não simulação de sorteios.

O significado de S/k_B é adimensional, e log é natural. Não estimamos entropia ou temperatura de um sistema real. Entropia do subsistema, aproximação canônica, medidas contínuas e sistemas interagentes gerais ainda precisam de desenvolvimento.

## Verificação de 22/10/2026

Cinco testes novos aprovados; suíte completa de 839 testes Python e 488 estruturas MathML aprovada. No navegador, respostas 15/28 e 1/56 aceitas, primeira etapa aberta por teclado e figura inspecionada em 390 px sem transbordamento horizontal ou erros de console observados. Revisão de Jhuann pendente.
