# Backpropagation: cadeia, redução e acumulação

Rascunho original para revisão de Jhuann.

## O erro local da saída é simples

Com BCE e sigmoide, a derivada em relação ao logit é p−y. Com média de N exemplos, dividimos a contribuição de cada exemplo por N. Isso combina derivadas da perda e da ativação, não elimina a cadeia anterior.

delta=(p−y)/N

## A unidade oculta recebe o peso da saída

Para h_j=tanh(a_j), dL/da_j=delta v_j(1−h_j²). A partir daí, dL/dW_jk soma essa contribuição vezes x_k, e dL/db_j soma a contribuição. O gradiente de v_j soma delta h_j.

regra da cadeia em cada conexão

## Gradientes são calculados no mesmo estado

Acumule contribuições de todos os exemplos antes de atualizar parâmetros no batch completo usado aqui. Alterar um peso no meio da derivação altera o cálculo. Diferenciação automática organiza a mesma cadeia por um grafo; nosso código é manual.

calcular → acumular → atualizar

## Definir o objetivo antes de derivar

O exemplo escalar preservado mais adiante usa perda quadrática com fator1/2. O novo desenvolvimento usa a rede 2→H→1 da biblioteca: a=Wx+b, h=tanh(a), logit z=v·h+c e p=σ(z). W tem forma H×2; b,v têm H componentes e c é escalar. Para N registros binários, J é a média das perdas BCE mais λ/2 vezes a soma dos quadrados de W e v. Biases b,c não recebem penalidade aqui.



## Derivar p−y pela cadeia completa

Para um registro com alvo y∈{0,1}, ℓ=−y ln p−(1−y)ln(1−p). Derivar em p dá −y/p+(1−y)/(1−p)=(p−y)/[p(1−p)]. A sigmoide tem derivada dp/dz=p(1−p). Multiplicar os fatores cancela o denominador, resultando em ∂ℓ/∂z=p−y. A identidade vale para o modelo em aritmética real; a avaliação numérica não deve calcular logaritmos de probabilidades arredondadas para zero.

∂ℓ/∂z=p−y

## Estabilidade da perda não dispensa a derivação

Uma forma equivalente da BCE por logit é log(1+e^z)−yz. O código a avalia por max(z,0)+log1p(exp(−|z|))−yz, evitando exponenciais grandes e log de probabilidade arredondada. A função equivalente suave tem derivada σ(z)−y, inclusive em z=0. Não estamos definindo uma perda com uma quina real porque a expressão de avaliação contém max e módulo. O painel antigo continua sendo o exemplo escalar quadrático, não uma BCE.



## A média define o erro que entra em cada registro

Se J_dados=(1/N)Σℓ_n, a contribuição no logit n é δ_n=(p_n−y_n)/N. Dividir por N uma segunda vez no acumulador mudaria o objetivo. Se a redução fosse soma, esse fator não apareceria. A convenção precisa ficar visível antes de comparar taxas de aprendizagem, batches ou bibliotecas.

δ_n=(p_n−y_n)/N

## Voltar da saída para cada unidade oculta

Como z_n=Σ_j v_j h_nj+c, temos contribuições δ_n para c e δ_n h_nj para v_j. Para a pré-ativação a_nj, a cadeia passa pelo peso v_j e pela tanh: r_nj=δ_n v_j(1−h_nj²). A tanh atua componente a componente; não substituímos esse produto por uma soma entre unidades. Todos esses fatores são avaliados nos pesos do mesmo forward.

r_nj=δ_n v_j(1−h_nj²)

## Acumular nos parâmetros compartilhados pelos registros

Cada registro usa os mesmos W,b,v,c. Portanto ∂J_dados/∂W_jk=Σ_n r_nj x_nk, ∂J_dados/∂b_j=Σ_n r_nj, ∂J_dados/∂v_j=Σ_n δ_n h_nj e ∂J_dados/∂c=Σ_n δ_n. O gradiente de W tem a mesma forma H×2. Substituir o acumulador pela última contribuição perderia os outros registros; atualizar pesos a cada registro seria outro procedimento, não o batch completo descrito aqui.

∂J_dados/∂W_jk=Σ_n r_nj x_nk

## Somar a regularização uma vez

Para λ/2 ΣW_jk²+λ/2 Σv_j², os gradientes acrescentam λW_jk e λv_j. Esses termos são adicionados uma vez ao gradiente do objetivo do batch, depois de acumular as contribuições dos dados. Não se acrescenta λb ou λc nesta convenção. Outras definições podem dividir a penalidade por N; isso alteraria o objetivo e a interpretação de λ, e deve ser declarado.



## Somar caminhos também aparece num grafo mínimo

Tome r=u², s=3u e z=r+s. O mesmo u é usado em dois ramos. A cadeia total é dz/du=(dz/dr)(dr/du)+(dz/ds)(ds/du)=1×2u+1×3. Em u=2, r=4, s=6, z=10 e dz/du=7. A contribuição do ramo r não apaga a do ramo s. Este desenho é uma aplicação de cálculo, não uma nova arquitetura treinada.

dz/du=2u+3

## Um batch de dois registros com contas exatas

Escolha H=2, W e b nulos, v=(2,−1), c=0, entradas x₁=(1,2), x₂=(−1,1), alvos y₁=1,y₂=0 e λ=0. Nos dois casos h=(0,0), z=0 e p=1/2. Como N=2, δ₁=−1/4 e δ₂=1/4. Para a primeira unidade, r₁₁=−1/2 e r₂₁=1/2; para a segunda, r₁₂=1/4 e r₂₂=−1/4. A perda média é ln2, distinta da perda quadrática do exemplo antigo.



## Abrir a soma para W e conferir os zeros

A primeira linha de W recebe (−1/2)(1,2)+(1/2)(−1,1)=(−1,−1/2). A segunda recebe (1/4)(1,2)+(−1/4)(−1,1)=(1/2,1/4). Os gradientes de b,c somam zero e os de v são zero porque h é zero. Isso não implica que todo o gradiente seja zero: W recebe contribuições não nulas. Se λ=1/2, o gradiente de v passa a (1,−1/2), pela penalidade.

∇_W J=[(−1,−1/2);(1/2,1/4)]

## Gradiente, atualização e autograd são etapas distintas

Backprop calcula derivadas. Uma atualização como θ_novo=θ−η∇J é uma escolha de otimizador, feita após o cálculo no estado atual. Um motor de diferenciação automática registra operações e organiza a cadeia; esta biblioteca usa fórmulas manuais e o novo laboratório expõe contribuições por registro. Não foram instalados ou executados frameworks. Comparar com autograd será um estudo futuro, sem pressupor que já exista aqui.



## O que os testes conseguem conferir

O laboratório usa a rede da raiz do protótipo, expõe δ/r e gradientes de cada exemplo e confere o agregado contra o gradiente existente. Diferenças centrais da perda verificam todos os nove parâmetros num caso não nulo, com erro de passo e arredondamento. Repetir o batch não altera o gradiente da perda média com a penalidade adotada. A conferência apoia implementação; não demonstra generalização, capacidade de treinar qualquer rede ou uma prova de convergência do otimizador.



## Exemplo escalar original preservado

No exemplo escalar L=(a tanh(wx+b)−y)²/2, use x=1,w=b=0,a=2,y=1. Qual dL/dw?

1. A tanh vale zero e a saída vale zero.
2. Erro é −1.
3. Derivada da tanh na origem é 1.
4. Produto: (−1)×2×1×1=−2.

## Exercícios e resoluções

### Qual gradiente escalar do exemplo?

Produto dos quatro fatores.

### Podemos atualizar pesos antes de terminar as contribuições do mesmo batch sem mudar o método?

Os gradientes devem corresponder ao mesmo estado.

### Para BCE com p=1/2,y=1 e N=2, quanto é δ desse registro?

(1/2−1)/2=−1/4.

### No mesmo registro, com v₁=2 e h₁=0, quanto é r₁?

(−1/4)×2×(1−0)=−1/2.

### No batch de dois registros, quanto é ∂J/∂W₁₁ sem regularização?

(−1/2)×1+(1/2)×(−1)=−1.

### No mesmo batch, quanto é ∂J/∂W₁₂ sem regularização?

(−1/2)×2+(1/2)×1=−1/2.

### No grafo r=u²,s=3u,z=r+s, quanto é dz/du em u=2?

2u+3=4+3=7; os caminhos se somam.

### No batch descrito, λ=1/2 e v₁=2. Quanto é o gradiente total de v₁?

O termo de dados é zero e λv₁=1.

### Se ∇b e ∇v forem zero no exemplo, todo o gradiente necessariamente é zero?

As linhas de W têm contribuições não nulas.

### Trocar a perda média por soma conserva todos os gradientes sem mudar escala?

O termo de dados perde o fator1/N; a convenção da penalidade também precisa ser mantida explícita.

### No objetivo da aula, biases recebem λb e λc?

A penalidade foi definida somente sobre W e v.

### Backpropagation sozinho já especifica a regra de atualização do otimizador?

Ele fornece gradientes; a atualização é outra etapa.
