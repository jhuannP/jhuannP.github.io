# Referenciais acelerados: translação em uma dimensão

Material original em rascunho — 16/10/2026. Referência de escopo: CCM0112, consultada em 16/10, ativação 15/07/2024; versão da turma de 2023 não recuperada. https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0112

## O referencial faz parte da descrição

Um referencial associa posições e tempos aos acontecimentos. Nesta aula, S é inercial no modelo newtoniano e S′ tem origem X(t) medida por S. Os eixos permanecem paralelos, sem rotação, e usamos o mesmo tempo t. Não é uma transformação relativística e não inclui Coriolis nem força centrífuga.



## A posição relativa vem de subtrair a origem

Se o corpo tem coordenada x(t) em S, sua coordenada em S′ é x′(t)=x(t)−X(t). O apóstrofo indica referencial, não derivada. Para velocidades e acelerações, usaremos v′ e a′ como valores medidos em S′, obtidos por derivadas temporais de x′.

x′=x−X

## Duas derivadas mostram a diferença nas acelerações

Derivando no mesmo tempo: v′=v−V, com V=dX/dt. Derivando de novo: a′=a−A, com A=d²X/dt². Não é necessário que A seja constante para essa relação cinemática; a demonstração interativa usa A constante para integrar trajetórias simples.

v′=v−V; a′=a−A

## Velocidade relativa constante não altera a aceleração

Se X=X₀+V₀t, então A=0 e a′=a, mesmo que posições e velocidades sejam diferentes. Dentro das hipóteses newtonianas, uma translação com velocidade constante entre referenciais inerciais preserva a forma da segunda lei com as mesmas forças físicas avaliadas de maneira consistente. Não confunda mover-se com velocidade diferente e acelerar a origem.



## A segunda lei em S′ exige um termo adicional

Em S, a resultante das forças de interação é F=m a para massa constante. Como a=a′+A, temos F=m(a′+A). Reorganizando, m a′=F−mA. O termo F_in=−mA permite escrever uma equação de movimento no referencial acelerado. Ele é oposto à aceleração da origem, não necessariamente à velocidade do corpo.

m a′=F−mA

## O termo de inércia não é um novo par de interação

Forças físicas como gravidade e contato têm agentes de interação. O termo −mA decorre da escolha do referencial e não representa um segundo corpo exercendo uma força adicional. Não se deve procurar para ele um par de ação e reação físico no sentido da terceira lei. Chamar esse termo de força fictícia não significa que as acelerações relativas observadas sejam imaginárias.



## Uma partícula livre pode acelerar em coordenadas relativas

Considere F=0, massa 2 kg e origem com A=+1 m/s², inicialmente em repouso na mesma origem da partícula. Em S, a=0 e x=0. Em S′, a′=−1 m/s² e x′=−t²/2. Em t=2 s, x′=−2 m. Não apareceu uma interação nova; mudou a descrição do mesmo movimento.



## Repouso relativo também pode exigir força física

Com m=2 kg, F=2 N e A=1 m/s², temos a=1 m/s² e a′=0. Se o corpo e a origem também têm posição e velocidade iniciais iguais, x′ permanece zero. Aceleração relativa zero sozinha não garante repouso relativo: uma velocidade relativa inicial diferente de zero persistiria.



## No elevador, contato e gravidade continuam identificáveis

Escolha vertical positiva para cima. Para um corpo apoiado no piso e acompanhando o elevador de aceleração A, a equação em S é N−mg=mA. Em S′, o corpo está em repouso relativo: N−mg−mA=0. Assim N=m(g+A). Para m=2 kg, g=10 m/s² e A=2 m/s², N=24 N. O peso gravitacional tem módulo mg=20 N; a força de contato mudou.



## O modelo de contato tem um limite

Em A=−g, a expressão dá N=0, condição de perda do apoio compressivo. Para A<−g, uma normal negativa não pode ser produzida por um piso que só empurra: a hipótese de acompanhar o elevador em contato falha. Seria necessário analisar movimento relativo ou outro tipo de vínculo. A fórmula não deve ser aplicada como se o piso pudesse puxar o corpo.



## Conferir os dois referenciais evita contar forças duas vezes

Escreva a equação de S com apenas forças de interação. Transforme a aceleração e só então acrescente −mA em S′. Confira posições e condições iniciais nos dois sistemas. A simulação usa F, m e A constantes, x(0)=X(0)=0 e velocidades iniciais zero; ela compara curvas de posição, sem executar uma experiência de laboratório. Referenciais em rotação exigem outros termos e não estão cobertos aqui.



## Exemplo resolvido

Um corpo de 2 kg sofre resultante constante de 6 N. Uma origem acelera a 1 m/s² no mesmo sentido. Ambos começam em x=0 e em repouso. Compare as posições em 2 s.

Em S, a=F/m=3 m/s² e x(t)=3t²/2. Em 2 s, x=6 m.

A origem tem X(t)=t²/2, logo X(2)=2 m.

Em S′, a′=3−1=2 m/s² e x′(2)=4 m.

Confira a transformação: x′=x−X=6−2=4 m.

O termo de inércia é −mA=−2 N; F−mA=4 N=m a′.

As duas descrições concordam sobre o mesmo movimento; a força física continua 6 N.

## Exercícios e resoluções

### No exemplo com m=2 kg, F=6 N e A=1 m/s², qual a aceleração em S′?

F/m−A=3−1=2 m/s².

### Qual o termo de inércia para m=2 kg e A=1 m/s²?

−mA=−2 N.

### No exemplo resolvido, qual x′ em t=2 s?

x−X=6−2=4 m.

### Com m=2 kg, g=10 m/s² e elevador acelerando 2 m/s² para cima, qual N?

m(g+A)=2×12=24 N.

### Uma partícula livre vista de origem com A=1 m/s² tem qual aceleração relativa?

a′=0−1=−1 m/s².

### Aceleração relativa zero garante repouso relativo sem conferir a velocidade inicial?

A velocidade relativa pode ser uma constante não nula.

### O termo −mA representa uma nova interação física com um corpo agente?

Ele vem da mudança de referencial.

### Um piso que só empurra pode sustentar a normal negativa prevista para A<−g?

A hipótese de contato acompanhando o elevador deixa de valer.

### Esta transformação sem rotação já inclui o termo de Coriolis?

Coriolis exige analisar um referencial em rotação.

## Preparação de aula

Desenhe as origens e a coordenada relativa; derive duas vezes; escreva Newton nos dois sistemas; compare a partícula livre e o repouso relativo; analise elevador e perda de contato. Termine pedindo para identificar o erro de somar −mA também no referencial inercial.

## Pendências

Rotações, Coriolis, centrífuga e mais problemas de mudança de referencial. A aula não comprova domínio pessoal nem cobre integralmente o programa.
