# Doppler relativístico longitudinal

16/10/2026. Rascunho para revisão de Jhuann.

## Fixe a geometria antes de escolher o sinal

No referencial S, a fonte está em x=0 e emite luz em +x com período próprio T_e=1/f_e. O receptor segue x=d+vt, com d>0, |v|<c e β=v/c. β positivo significa afastamento; β negativo significa aproximação enquanto a luz ainda chega pelo lado +x. São movimentos inerciais no vácuo, sem gravidade.

## Duas emissões e duas recepções são eventos diferentes

Uma crista emitida em t_e obedece x=c(t−t_e). Ao encontrar o receptor, c(t−t_e)=d+vt, logo t_r=(d+ct_e)/(c−v). Para emissões separadas por T_e, as recepções em S ficam separadas por Δt_r=T_e/(1−β). A distância inicial cancela nessa diferença; não cancela no instante de cada chegada.

## O receptor mede o intervalo em seu próprio relógio

As duas recepções ocorrem no mesmo receptor, portanto sua separação temporal própria é Δτ_r=Δt_r/γ, com γ=1/√(1−β²). A frequência medida por ele é 1/Δτ_r. Usar apenas os instantes coordenados de S deixaria de fora essa diferença de relógios.

## A razão de frequências combina os dois efeitos

Dividindo a frequência recebida pela emitida, D=f_r/f_e=γ(1−β)=√[(1−β)/(1+β)]. Para afastamento, D<1; para aproximação, D>1. A expressão é longitudinal e usa a convenção de sinal definida acima. Só a dilatação do tempo, isolada da geometria das recepções, não fornece o resultado.

## Lorentz oferece uma conferência independente

Entre as recepções, Δx=vΔt_r. Aplicando Δt′=γ(Δt_r−vΔx/c²), obtemos Δt′=Δt_r/γ=Δτ_r. Também Δx′=γ(Δx−vΔt_r)=0: o receptor permanece na mesma posição em seu referencial. O laboratório confere essas relações com eventos de chegada, em unidades c=1 e T_e=1.

## Frequência e comprimento de onda variam inversamente

Cada referencial inercial mede velocidade da luz c, então λ_r/λ_e=f_e/f_r=1/D. Aumentar comprimento de onda reduz frequência. Frequência é medida por unidade de tempo próprio do observador; não se deve misturar um período num referencial com um comprimento em outro para calcular c.

## Defina o deslocamento espectral pela razão observável

Adote z=(λ_r−λ_e)/λ_e=λ_r/λ_e−1=1/D−1. Neste modelo, β>0 produz z>0 e β<0 produz −1<z<0. Inverter a razão de frequências dá β=(1−D²)/(1+D²). Essa inferência só descreve o movimento longitudinal sob as hipóteses do exemplo.

## Um caso racional evita depender só de números aproximados

Para β=3/5, γ=5/4 e D=(5/4)(2/5)=1/2. O período entre chegadas em S vale (5/2)T_e, e no relógio do receptor vale 2T_e. Uma linha sintética de 600 THz é recebida a 300 THz; λ_r/λ_e=2 e z=1. THz significa 10¹² Hz.

## Inverter o movimento inverte a razão, não o sinal da frequência

D(−β)=1/D(β). Para β=−3/5, a razão é 2, z=−1/2 e a mesma linha sintética seria medida a 1200 THz. Frequência e período continuam positivos. Uma mudança de sinal na velocidade não é uma frequência negativa.

## O limite lento e a composição verificam o modelo

Para |β| pequeno, expandir a raiz dá D=1−β+β²/2+O(β³). O termo linear não basta em velocidades grandes. Para composições colineares com a convenção mantida, β₁₂=(β₁+β₂)/(1+β₁β₂), e D(β₁₂)=D(β₁)D(β₂). Essa identidade ajuda a conferir contas e implementação.

## O Doppler acústico usa outras hipóteses

Na aula de som, a velocidade de propagação é definida em relação ao meio. Aqui c tem o mesmo valor em referenciais inerciais e o período recebido usa tempo próprio. Transplantar a fórmula acústica para a luz ignora essas hipóteses. Doppler transversal, ângulos e aceleração pedem outros desenvolvimentos.

## Uma ligação com astronomia exige distinguir modelos

A razão entre comprimentos de onda pode ser medida em espectros, mas interpretar seu deslocamento exige identificar a linha e a geometria. Este laboratório não modela redshift gravitacional ou expansão cosmológica e não atribui todo z a uma velocidade desta fórmula. As linhas do exemplo são sintéticas; não há observação ou análise de dados astronômicos de Jhuann.

## Resoluções

Para β=3/5, qual f_r/f_e? Aceita fração.

γ=5/4 e 1−β=2/5, portanto D=1/2.

No mesmo caso, qual Δτ_r/T_e?

O período próprio recebido é inverso da razão D: 2.

Para β=3/5, qual z pela definição usada?

z=1/D−1=2−1=1.

Para β=−3/5, qual a razão de frequências?

D(−β)=1/D(β)=2.

Se f_e=600 THz e β=3/5, qual f_r em THz?

f_r=Df_e=300 THz.

Se D=1/2 neste modelo longitudinal, qual β? Aceita fração.

(1−1/4)/(1+1/4)=3/5.

O período entre chegadas em S já é o período próprio do receptor em movimento?

É preciso dividir Δt_r por γ.

Ao trocar β por −β, a frequência deve ficar negativa?

As razões são recíprocas e positivas.

Todo deslocamento espectral astronômico é descrito por esta fórmula longitudinal sem outras hipóteses?

Geometria, gravidade e cosmologia exigem modelos pertinentes; não se infere tudo de um único z.

## Fontes e roteiro

Escopo: CCM0222, item 9, programa consultado em 16/10. Apoio: [Feynman/Caltech, volume I, seção 34–6](https://www.feynmanlectures.caltech.edu/I_34.html#Ch34-S6), consultada diretamente em 16/10/2026. A convenção de velocidade da fonte é diferente: aqui fixamos luz em +x e β positivo para receptor afastando-se. Fórmulas são relações físicas usuais; organização, distância inicial normalizada, exercícios e código são próprios, sem transcrição da fonte.

Pré-requisitos: eventos, Lorentz, tempo próprio e equação de uma reta. Roteiro: desenhar dois raios e o receptor; resolver encontros; subtrair tempos; transformar intervalo; verificar β=3/5; inverter o movimento; explicar quais interpretações astronômicas não estão no modelo. Produto: cálculo comentado com sinal, relógios, unidades e hipóteses explícitos.

O laboratório usa distância inicial 3cT_e para manter as duas recepções antes do cruzamento para aproximação; unidades normalizadas não alteram razões. As contas de ponto flutuante são aproximadas, sobretudo perto de |β|=1, onde a interface não chega. Pendentes: ângulos, efeito transversal, aceleração, modelos gravitacionais/cosmológicos e análise de linhas reais.
