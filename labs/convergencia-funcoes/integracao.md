# Integração do limite uniforme — complemento de29/10/2026

## Somas superiores e inferiores tornam a integrabilidade verificável

Fixe [a,b] com comprimento L=b−a>0. Uma partição finita P divide o intervalo em partes de larguras Δxᵢ. Para uma função limitada v, defina U(P,v)=Σ(sup v na parte i)Δxᵢ e D(P,v)=Σ(inf v na parte i)Δxᵢ. Usamos D para soma inferior, evitando confundir com L, o comprimento. O critério de Darboux diz: v é Riemann-integrável se, para todo ε>0, alguma partição satisfaz U(P,v)−D(P,v)<ε. Esse critério é um resultado prévio da teoria da integral; não o provamos novamente aqui.

## Primeiro a função limite precisa ser limitada

Pela convergência uniforme, escolha um índice N₀ com |f−f_N₀|≤1 em todo o intervalo. Como f_N₀ é integrável, é limitada por algum M. A desigualdade triangular fornece |f|≤M+1. Assim as somas superiores e inferiores de f estão definidas e são finitas. Não podemos começar usando a integral de f antes de justificar que ela existe. Esta primeira etapa usa um único aproximante, não um limite informal de integrais.

## A mesma partição controla a oscilação do limite

Dado ε>0, escolha um aproximante g=f_N com sup|f−g|<δ=ε/(4L). Como g é integrável, existe P com U(P,g)−D(P,g)<ε/2. Em cada parte, sup f≤sup g+δ e inf f≥inf g−δ. Subtrair, multiplicar por Δxᵢ e somar dá U(P,f)−D(P,f)≤U(P,g)−D(P,g)+2δL<ε/2+ε/2=ε. Pelo critério de Darboux, f é integrável. Aqui a mesma partição serve para comparar g e f; não precisamos de uma malha universal para todos os índices.

## Agora a integral e as funções integrais têm uma cota

Com f já integrável, linearidade e monotonicidade dão |∫ₐᵇ(fₙ−f)|≤∫ₐᵇ|fₙ−f|≤L Eₙ→0. Também vale, para todo x∈[a,b], |∫ₐˣ(fₙ−f)|≤(x−a)Eₙ≤L Eₙ. Portanto as funções integrais Gₙ(x)=∫ₐˣfₙ convergem uniformemente para G(x)=∫ₐˣf. Em [2,5], fₙ=1/n e f=0 dão cota3/n, atingida em x=5. Para erro estritamente menor que0,01 em todas essas integrais, escolha n≥301. Isso não envolve derivar uma sequência de funções.

## Num domínio ilimitado a mesma conclusão pode falhar

No domínio fixo [0,+∞), tome hₙ(x)=1/n para0≤x≤n e zero para x>n. O supremo do erro em relação a zero é1/n, portanto a convergência é uniforme no semieixo inteiro. Cada integral imprópria é finita e vale n·(1/n)=1, mas a integral do limite é0. Não há L finito para converter erro uniforme em erro global da integral; a região que contribui cresce. Em cada intervalo compacto fixo a troca funciona. Controle de caudas, integração de Lebesgue e outros teoremas de passagem ao limite ficam para outra etapa.

## Fontes e alcance

ApostolI2ªed.1967,§11.4 pp.425–426/PDF445–446,consulta textual parcial,cabeçalhos conferidos. Oteorema11.3 usa aproximantes contínuos; sua extensão a Riemann-integráveis é apoiada pelo enunciado/prova de Lebl, https://jirilebl.github.io/ra/html/sec_liminter.html ,§6.2.2,Teorema6.2.4,consulta parcial29/10. Sem nova inspeção visual/leitura integral ou cópia de PDFs. Prova por partições e exemplos acima são redação/deduções próprias;critério de Darboux assumido como pré-requisito. Não afirma prova de toda a teoria da integral. Sem nova consulta de programa/histórico.

Nenhum algoritmo ou painel anterior alterado. O código existente continua conferindo exemplos finitos; não prova teoremas. O exemplo constante de intervalo3 tem integral3/n; para n300 a cota é1/100, para301 é3/301<1/100. Para diferença de Darboux≤1/5,δ1/100,L3,a cota é13/50. A área dos retângulos no semieixo vale1 para todo n;é uma prova algébrica,sem amostragem ou experimento físico. Revisão pessoal pendente;critérios de séries uniformes e teoria geral continuam abertos.

As funções integrais não são chamadas de primitivas em todos os pontos:integrabilidade de Riemann não implica continuidade do integrando.
