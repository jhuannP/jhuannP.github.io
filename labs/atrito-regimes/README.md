# Atrito: regimes e parada

Rascunho original —27/10/2026; revisão de Jhuann pendente.

## Desenhe as forças sobre o bloco

Pré-requisitos: forças vetoriais, segunda lei de Newton e cinemática1D. O sistema é um bloco de massa m sobre um piso horizontal fixo, com força aplicada F horizontal. Escolha o sentido positivo para a direita. As forças no bloco são peso mg para baixo, normal N para cima, F e atrito f horizontais. Não há aceleração vertical nem outra força vertical: por isso N=mg. Essa igualdade decorre das hipóteses, não é uma definição universal de normal. Forças sobre o piso não entram no diagrama do bloco.

N−mg=0; ma=F+f

## Coeficientes descrevem um modelo empírico

Adotamos atrito seco de Coulomb, com coeficientes estático μs e cinético μk constantes e 0≤μk≤μs. São adimensionais: multiplicar por N produz uma força. Os valores didáticos são m=2 kg, g=10 m/s², μs=0,5 e μk=0,3. Eles não identificam um par real de materiais. O modelo simplifica superfícies e velocidades; não cobre automaticamente lubrificação, aderência microscópica ou desgaste.

## Atrito estático ajusta-se à necessidade

Se o bloco está em repouso relativo ao piso, o equilíbrio horizontal requer f=−F. Essa solução estática só é admissível quando |F|≤μsN. No exemplo, N=20 N e o limite é10 N. Para F=6 N, o atrito é−6 N, e não−10 N; para F=0, é zero. Se F=−6 N, o atrito é+6 N. O atrito estático ajusta seu valor até o limite, sem precisar saturá-lo.

|f_s|≤μsN

## A igualdade no limiar precisa de convenção explícita

Em |F|=10 N, o atrito estático máximo ainda pode equilibrar o bloco. Na decisão idealizada desta aula e do painel, mantemos o repouso na igualdade; só iniciamos movimento se |F|>10 N. Essa escolha deve ser lida junto das hipóteses, sem tratar uma superfície real como tendo um limiar perfeitamente uniforme. Um bloco que já desliza usa outro ramo do modelo, mesmo quando |F| está abaixo do limite estático.

## Após ultrapassar o limiar

A partir do repouso, se |F| ultrapassa10 N, não existe f estático admissível que zere a resultante. Com F=12 N, o início é para a direita; o atrito cinético vale−μkN=−6 N. A resultante é6 N e a aceleração é3 m/s². Com F=−12 N, o início é para a esquerda, f=+6 N e a=−3 m/s². O painel abaixo decide esse início a partir do repouso; ele não acompanha a velocidade ao longo do tempo.

|f_k|=μkN

## Não trocar velocidade por força aplicada

No deslizamento, use a velocidade do bloco relativa ao piso, v_rel. O atrito tem sinal oposto a v_rel, não necessariamente a F. Se o bloco já desliza para a esquerda, v_rel<0 e f=+6 N. Com F=+6 N também para a direita, ambas as forças apontam para a direita e a=(6+6)/2=6 m/s², reduzindo a rapidez enquanto v permanece negativa. Se o bloco desliza para a direita sob a mesma F, o atrito é−6 N e a=0: ele continua movendo-se com velocidade constante.

v_rel≠0 ⇒ f=−μkN sgn(v_rel)

## Uma força resultante nula não exige repouso

Nos dois estados com F=6 N, a condição inicial muda a resposta. Partindo do repouso, f=−6 N e o bloco fica parado. Já deslizando para a direita, f também vale−6 N, porém o bloco mantém sua velocidade positiva. A equação ma=0 fornece velocidade constante, que pode ser nula ou não. Comparar apenas força aplicada com μsN não basta para decidir a evolução de um corpo cuja velocidade inicial não é zero.

## O diagrama de força não é um gráfico de velocidade

A figura compara F=6 N em dois estados: repouso e deslizamento para a esquerda. Os pares verticais se equilibram nos dois casos. Na primeira linha, as forças horizontais se cancelam; na segunda, apontam ambas para a direita. As setas de velocidade são identificadas separadamente e não representam forças extras. Os diagramas ilustram valores próprios, não uma figura copiada do livro.

## Sem força aplicada, o atrito freia até um evento

Agora o bloco começa com v₀=3 m/s para a direita e F=0. Enquanto desliza, f=−6 N e a=−3 m/s². A velocidade é v(t)=3−3t, válida até a primeira parada: t_p=1 s. Nesse intervalo, x(t)−x₀=3t−3t²/2 e a distância de parada é3/2 m. Essa não é uma fórmula para continuar com o mesmo atrito depois da parada. Em v=0, precisamos avaliar novamente o ramo estático.

t_p=1 s; D_p=3/2 m

## Depois da parada, não invente movimento de volta

Na parada, F continua zero. Existe equilíbrio estático com f=0, portanto o bloco permanece parado. Em t=2 s, sua velocidade é0 e a posição continua x₀+3/2 m. Prolongar v=3−3t até 2 s daria−3 m/s e um retorno que o modelo por regimes não permite. Para inverter, seria necessária outra força ou condição capaz de iniciar o deslizamento no sentido oposto. O laboratório de trajetória trata apenas F=0 e faz essa troca de regime exatamente na parada.

## O trabalho confere a frenagem neste piso fixo

A energia cinética inicial é K₀=mv₀²/2=9 J. Na frenagem, o atrito realiza trabalho W_f=−6×(3/2)=−9 J, igual a K_final−K₀=−9 J. O bloco termina com energia cinética zero, sem precisar acumular energia cinética negativa. Esse balanço é para o bloco e o piso fixo do exemplo. A energia mecânica perdida é dissipada na interação; o modelo não prevê temperaturas. Em contatos estáticos com superfícies móveis, não se deve declarar universalmente trabalho zero do atrito.

## O painel e o laboratório respondem perguntas diferentes

O painel existente varia F e m e parte do repouso a cada avaliação. μs=0,5, μk=0,3 e g=10 ficam fixos; confira F negativo, a igualdade no limiar e a troca para o ramo cinético. Ele não é uma trajetória temporal. O laboratório racional permite avaliar forças para v_rel positivo ou negativo e calcula a frenagem com F=0, incluindo a parada. Não integra trajetórias sob força aplicada variável nem simula rolamento ou esteira móvel.

## A normal precisa ser recalculada se o cenário mudar

Se a força aplicada tiver componente vertical, a equação vertical deixa de ser simplesmente N=mg. Num plano inclinado, a projeção do peso normal ao plano é outra. Como os limites do atrito dependem de N, reaproveitar20 N sem redesenhar as forças produziria um problema diferente. A implementação desta aula mantém plano horizontal e força aplicada horizontal; ela não resolve esses cenários por inferência automática.

## Uma sequência de decisão evita trocar os ramos

Primeiro defina sistema, eixos, contato e forças verticais. Depois verifique a velocidade relativa: se for não nula, use o ramo cinético com sinal oposto. Se estiver em repouso, calcule o atrito necessário e compare seu módulo ao limite estático. Só então obtenha a aceleração pela resultante. Ao prever uma parada, encerre o trecho e refaça a decisão. Limites, sinais e unidades são parte da solução, não uma conferência opcional ao final.

## Revisão pessoal e próximos recortes

Em vinte minutos, explique os dois estados com F=6 N, calcule o início com F=−12 N e reconstrua a frenagem de v₀=3 m/s. Use palavras para justificar por que o bloco não volta após parar. O material permanece em rascunho para sua revisão, sem comprovar domínio pessoal. Plano inclinado com transições, rolamento, superfícies móveis, coeficientes estimados e comparação com dados experimentais ainda precisam de desenvolvimento.

## Exercícios e resoluções

Para o bloco em repouso de 2 kg, g=10 m/s², μs=0,5 e F=6 N, qual é o módulo do atrito em newtons?

**Resolução:** Atrito estático ajusta-se a 6 N.

Atrito estático sempre tem módulo μsN?

**Resolução:** Esse é apenas o limite máximo.

No exemplo horizontal sem outras forças verticais, qual é N em newtons?

**Resolução:** N=mg=2×10=20 N.

Qual é o limite estático μsN, em newtons?

**Resolução:** 0,5×20=10 N.

Partindo do repouso com F=12 N, qual é a aceleração em m/s²?

**Resolução:** f=−6 N; a=(12−6)/2=3 m/s².

Partindo do repouso com F=−12 N, qual é a aceleração com sinal, em m/s²?

**Resolução:** O início é para a esquerda, f=+6 N; a=(−12+6)/2=−3 m/s².

Já deslizando à esquerda com F=+6 N, qual é o atrito com sinal, em newtons?

**Resolução:** v_rel<0: atrito cinético para a direita, +6 N.

No mesmo estado de deslizamento à esquerda, qual é a aceleração em m/s²?

**Resolução:** a=(6+6)/2=6 m/s².

Com F=0 e v₀=3 m/s, em que tempo o bloco para, em segundos?

**Resolução:** Enquanto desliza, a=−3 m/s²; 3−3t=0 dá1 s.

No mesmo caso, qual é a distância de parada em metros?

**Resolução:** 3×1−(3/2)×1²=3/2 m.

No mesmo caso F=0, qual é a velocidade em t=2 s, em m/s?

**Resolução:** O bloco para em 1 s; depois permanece parado com f=0.

Qual é o trabalho do atrito até essa parada, em joules?

**Resolução:** −6 N×(3/2)m=−9 J, igual à variação de energia cinética.

## Fontes e limites

Nussenzveig, Curso de Física Básica, vol.1 Mecânica,5ª ed. Blucher2013/reimpressão2017 conforme inventário anterior. Consulta textual parcial de §5.2(ii), pp.115–117/PDF116–118 em27/10; p.116/PDF117 também inspecionada visualmente. Correspondência reconferida no cabeçalho, PDF contado a partir de1. Usa μe/μc, aqui μs/μk. Não se afirma leitura integral do capítulo. No livro, o valor crítico é discutido como início experimental; código/painel adotam explicitamente equilíbrio na igualdade ideal.

[OpenStax University Physics1, §6.2](https://openstax.org/books/university-physics-volume-1/pages/6-2-friction), consulta parcial em27/10: força estática ajustável, módulo cinético, força normal e caráter empírico. Exemplos, números, figura, códigos e exercícios são próprios. PDF e figuras dos livros não distribuídos. Sem nova consulta ao Júpiter ou recuperação da versão curricular da turma.

## Laboratório

`python3 -m unittest discover -s labs/atrito-regimes -t .` e `python3 labs/atrito-regimes/model.py`. state recebe v,F e parâmetros int/Fraction; coast apenas v inicial e duração com F=0. Massa e g positivos;0≤μk≤μs; duração não negativa. Rejeita bool/float. Não há integração geral, plano inclinado ou superfície móvel. A solução do desafio foi corrigida para forças negativas usando abs(F) no limiar e sinal no ramo cinético; casos positivos originais preservados. Painel e seu JavaScript não modificados.

Seis testes:164 decisões a partir do repouso; sentidos com velocidades positivas/negativas; parada e repouso posterior; composição temporal atravessando a parada;35 casos de energia/reflexão e atrito zero; contratos. Provas e interpretação física da aula não são substituídas por testes.

Próxima revisão20min: comparar estados sob F=6N e refazer frenagem. Próximo desenvolvimento: plano inclinado e transições; alternar com lacunas de outras disciplinas antes de continuar.
