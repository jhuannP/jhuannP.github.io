# Dielétricos e interfaces — notas originais

16/10/2026. Rascunho para revisão de Jhuann.

## Os campos macroscópicos fazem uma média

Em um dielétrico, pequenas separações de cargas e orientações de dipolos podem produzir polarização sem transporte livre de carga pelo volume. P é momento de dipolo por volume, em C/m². E, P e as densidades aqui são grandezas macroscópicas; não descrevemos o campo singular de cada molécula. Separar carga livre e ligada depende do modelo material adotado.

## Carga ligada aparece quando a polarização varia

A contabilidade de dipolos em uma região produz carga ligada volumétrica ρ_b=−∇·P. Na superfície externa do material, σ_b=P·n_out, com normal apontando para fora do material. Polarização uniforme pode ter ρ_b=0 no interior e cargas não nulas nas duas faces de uma lâmina. Portanto interior neutro não implica ausência de carga de polarização na superfície.

## D reorganiza Gauss, sem substituir o campo elétrico

Defina D=ε₀E+P. Como ∇·E=(ρ_f+ρ_b)/ε₀ e ρ_b=−∇·P, segue ∇·D=ρ_f. A lei de Gauss para E continua contando carga total; a de D conta a parcela livre nessa decomposição. D e P têm unidade C/m², enquanto E tem V/m. D não é simplesmente outro nome para E.

## A relação constitutiva tem hipóteses

Para material linear, isotrópico e local no regime eletrostático, P=ε₀χ_eE e D=εE, com ε=ε₀(1+χ_e)=ε₀κ. Usaremos κ>0 e constante em cada meio. Anisotropia pede tensor, e resposta não linear ou dependente da história exige outra relação. Permissividade relativa não tem unidade; não confunda κ com ε em F/m.

## Escolher a normal fixa os sinais da interface

Separe dois meios por uma interface plana e escolha n apontando do meio 1 para o 2. Escreva E_in=E_i·n e componentes tangenciais no mesmo eixo. Uma caixa gaussiana muito fina atravessando a superfície tem fluxo de D dado por (D₂−D₁)·n vezes a área. A carga livre dentro é σ_f vezes essa área. No limite de espessura zero, D₂n−D₁n=σ_f.

## A componente tangencial vem da circulação eletrostática

Um retângulo estreito atravessando a interface satisfaz ∮E·dl=0 na eletrostática. Quando sua altura tende a zero e os campos permanecem finitos nas faces, as contribuições curtas desaparecem e E₂t=E₁t. Isso não obriga E₂n=E₁n. A derivação não cobre uma camada dipolar ideal com singularidade de potencial nem campos dinâmicos singulares.

## A carga ligada da interface envolve os dois materiais

Cada material contribui com sua normal externa: n para o meio 1 e −n para o meio 2. A densidade ligada líquida na interface é σ_b=(P₁−P₂)·n. Então ε₀(E₂n−E₁n)=σ_f+σ_b, consistente com Gauss para E. Aplicar P·n com a mesma normal para ambos os materiais daria um sinal errado.

## Sem carga livre, D normal continua; E normal pode saltar

Para meios lineares, ε₂E₂n−ε₁E₁n=σ_f. Se σ_f=0, E₂n=(ε₁/ε₂)E₁n; não se deve impor continuidade de E normal sem olhar as permissividades. Com componente tangencial comum não nula, as direções dos campos podem mudar na interface. Não confunda esse ajuste eletrostático com refração de uma onda luminosa.

## Um exemplo normalizado confere as duas leis de Gauss

Escolha κ₁=2, κ₂=4, E₁n=1 e E_t=1, com σ_f=0. Os campos E são medidos em E_ref; D, P e σ em ε₀E_ref, tornando ε₀=1 nas contas normalizadas. Obtemos E₂n=1/2, D₁n=D₂n=2, P₁n=1 e P₂n=3/2. Logo σ_b=−1/2 e E₂n−E₁n=−1/2=σ_total. O salto vem de carga ligada, apesar da carga livre nula.

## Adicionar carga livre muda a condição normal

Mantendo κ₁=2, κ₂=4 e E₁n=1, mas agora σ_f=1 nas unidades normalizadas, E₂n=(2+1)/4=3/4. D₂n−D₁n=3−2=1. P₁n=1 e P₂n=9/4, portanto σ_b=−5/4. A carga total é −1/4, igual ao salto de E normal. Carga livre positiva não obriga a carga total da interface a ser positiva.

## Uma condição local não resolve qualquer geometria

As relações de interface restringem campos compatíveis, mas o problema completo também exige fontes, condições externas e solução de potencial. O laboratório constrói campos uniformes por partes numa interface ideal, com uma lâmina livre imposta; não representa uma amostra real nem calcula força, ruptura, aquecimento ou radiação. Um experimento futuro precisa definir geometria e medição; não há dados experimentais nesta aula.

## Resoluções

Sem carga livre, κ₁=2, κ₂=4 e E₁n=1. Qual E₂n normalizado?

E₂n=(2/4)×1=1/2.

Nesse caso sem carga livre, qual D₂n−D₁n?

O salto normal de D é σ_f=0.

Nesse caso sem carga livre, qual a carga ligada líquida normalizada?

P₁n−P₂n=1−3/2=−1/2.

No exemplo com σ_f=1, qual E₂n? Aceita fração.

(2+1)/4=3/4.

No exemplo com σ_f=1, qual a carga total normalizada?

σ_f+σ_b=1−5/4=−1/4.

Sem carga livre, E normal é sempre contínuo entre permissividades diferentes?

D normal é contínuo; E normal pode mudar com ε.

Na eletrostática com campos finitos, E tangencial é contínuo?

A circulação num retângulo estreito dá E₂t=E₁t.

A lei de Gauss para E conta somente carga livre?

Ela conta carga total; D reorganiza a parcela de polarização.

Polarização uniforme implica ausência de carga ligada nas faces externas?

O volume pode ter ρ_b=0, mas nas faces vale σ_b=P·n_out.

## Roteiro didático e evidência

Pré-requisitos: Gauss, fluxo, circulação e vetores. Desenhar a normal; derivar a condição com caixa gaussiana e a tangencial com retângulo; depois conferir E, D e P separadamente. Pedir uma troca de orientação e um exemplo com carga livre positiva e total negativa. Produto de compreensão: solução comentada de outra interface, explicitando unidades. Não há experimento real ou domínio pessoal comprovado.

## Fontes e pendências

Escopo curricular: [CCM0212](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212), consulta de 16/10/2026. Apoio de leitura: [Feynman II, capítulo 10](https://www.feynmanlectures.caltech.edu/II_10.html), consultado hoje para definições de polarização e carga ligada. As contas de interface e testes são originais; não se reproduzem problemas ou trechos do livro.

Os testes racionais verificam as leis de contorno e a contabilidade de carga, inclusive ao inverter a normal e trocar os meios. Não resolvem geometrias gerais nem validam um material físico. Pendentes: derivação microscópica aprofundada, anisotropia, interfaces curvas e condições de potencial em problemas globais.
