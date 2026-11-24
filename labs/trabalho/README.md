# Trabalho e energia cinética — notas

Conteúdo original aprofundado em 13/10/2026, com apoio de IA para revisão de Jhuann. Não são notas importadas do Samsung Notes.

## Sistema, referencial e grandezas

Pré-requisitos: vetores, produto escalar, leis de Newton, derivada e integral. Tratamos o bloco como partícula para seu movimento de translação, com massa constante, num referencial inercial. K=mv²/2 usa a rapidez v, não uma componente com sinal. Trabalho é um escalar: mede a transferência associada à força ao longo do deslocamento. Força em newtons, posição em metros e trabalho/energia em joules, com 1 J=1 N·m.

`K=mv²/2; [K]=[W]=J`

## Força constante: a componente no deslocamento

Se a força é constante ao longo de um deslocamento retilíneo, W=F·Δr=Fd cosθ. Força alinhada com o deslocamento faz trabalho positivo; oposta, negativo; perpendicular, zero. Use o ângulo entre força e deslocamento, e não um ângulo escolhido no desenho sem relacioná-lo aos vetores. A expressão Fd sem o cosseno só vale quando a força está alinhada com o sentido do deslocamento.

`W=F·Δr=Fd cosθ`

## Força variável: somar ao longo do caminho

Em uma dimensão, W=∫_a^b F(x)dx, respeitando a orientação das fronteiras. Em várias dimensões, W=∫_trajetória F·dr; a integral usa a força avaliada ao longo do movimento real. Em geral o trabalho pode depender do caminho. Não substitua uma força variável pelo seu valor final multiplicado pela distância, salvo se uma aproximação foi declarada e seu erro analisado.

`W=∫_a^b F(x)dx; W=∫ F·dr`

## Deduzir o teorema trabalho–energia

Newton dá F_resultante=m dv/dt. Multiplique escalarmente por v: F_resultante·v=m v·dv/dt=d(m|v|²/2)/dt, usando massa constante. Integrar no tempo e usar dr=v dt produz o trabalho da resultante igual a K_final−K_inicial. O teorema relaciona os estados extremos, mas os trabalhos precisam corresponder à trajetória física. Não se conclui que o trabalho de uma força isolada seja sempre toda a variação de K.

`F_resultante·v=dK/dt ⇒ W_resultante=ΔK`

## Somar trabalhos e interpretar o sinal

A resultante é a soma vetorial das forças; a linearidade do produto escalar/integral dá W_resultante=ΣW_i. Trabalho resultante positivo aumenta K; negativo diminui K; zero mantém K entre os extremos, embora a direção da velocidade possa mudar. Em movimento circular uniforme, uma força centrípeta perpendicular à velocidade muda sua direção sem alterar a rapidez. Conservar K não é o mesmo que ausência de força.

`ΣW_i=K_f−K_i`

## Exemplo de força variável e o cuidado com uma mola

Para F(x)=kx, com k=2 N/m, de x=0 a L=3 m, W=∫_0^3 2x dx=9 J. Usar F(3)·3 daria 18 J, o dobro. Essa força aponta para +x quando x>0; não é a força restauradora usual de uma mola. Uma mola ideal tem F=−kx e faz trabalho −k(b²−a²)/2: ao aumentar o alongamento positivo, seu trabalho é negativo. Declarar o sinal faz parte de declarar o modelo.

`F=+kx ⇒ W=k(b²−a²)/2; mola: F=−kx`

## Exemplo com atrito: balanço completo

O bloco de massa 2 kg já desliza para +x a 2 m/s num plano horizontal. Usamos g=10 m/s² como valor didático, μ_c=0,1 e força aplicada constante de 10 N em +x. N=mg=20 N; atrito cinético=μ_cN=2 N em −x. Ao percorrer 3 m, W_aplicada=30 J e W_atrito=−6 J. Peso e normal são perpendiculares ao deslocamento e fazem trabalho zero neste modelo. K_inicial=4 J, portanto K_final=4+24=28 J e rapidez final √28 m/s.

`W_resultante=30−6=24 J; K_f=28 J; v_f=√28 m/s`

## Quando o bloco para antes do destino

Sem força aplicada no mesmo exemplo, o atrito vale 2 N e o bloco tem apenas 4 J de energia cinética inicial. A distância de parada é 4/2=2 m. Pedir um deslocamento de 5 m e calcular K=4−2·5=−6 J não descreve um estado físico: o bloco já parou. Os trabalhos do experimento são calculados somente até a parada, com K_final=0 e W_atrito=−4 J. Após parar, atrito estático, reinício ou inversão exigiriam outra etapa de modelagem.

`se F_resultante<0: d_parada=K_i/|F_resultante|`

## Energia mecânica e energia térmica não são o mesmo balanço

O teorema trabalho–energia não exige que as forças sejam conservativas. Se uma força tem potencial U e W_conservativa=−ΔU, podemos escrever Δ(K+U)=W_não_conservativas na situação apropriada. No plano horizontal não há variação de potencial gravitacional; força aplicada e atrito alteram a energia mecânica do bloco. O modelo registra o trabalho negativo do atrito, mas não calcula temperaturas nem reparte energia térmica entre bloco e superfície. “Energia não conservada” precisa indicar qual energia e qual sistema estão sendo analisados.

`W_resultante=ΔK; W_conservativa=−ΔU`

## Potência é taxa, não quantidade de energia

A potência instantânea de uma força é P=F·v; a potência resultante é dK/dt. A unidade é watt, 1 W=1 J/s. A letra W também costuma representar trabalho; contexto e unidades distinguem símbolo e unidade. Uma força perpendicular à velocidade tem potência instantânea zero, mas pode alterar a trajetória. Potência média W/Δt em um trecho não é necessariamente a potência instantânea em todo o trecho.

`P=F·v; [P]=watt=J/s`

## Roteiro para resolver e ensinar

Defina o corpo/sistema, referencial e trajetória; desenhe todas as forças; identifique quais são constantes e quais dependem da posição. Calcule cada trabalho com sinal e unidade. Some, relacione com ΔK e confira se o resultado corresponde a um movimento possível. Se o corpo para antes do destino, interrompa o modelo de deslizamento. Para ensinar, explique a diferença entre trabalho de uma força e trabalho resultante e confira o resultado por Newton num caso de aceleração constante.

`forças → trabalhos → soma → ΔK → viabilidade → interpretação`

## Exercícios e resoluções

Tente antes de consultar; explicite sinais, unidades e sistema.

### 1. Para F(x)=2x N, com x em m de 0 a 3, qual o trabalho em joules?

Resolução: 2×9/2=9.

### 2. O trabalho de qualquer força isolada sempre é ΔK total?

- Sim

- Não

Resolução: O teorema usa a soma dos trabalhos de todas as forças.

### 3. Força constante 10 N, deslocamento 2 m e ângulo 60°. Qual o trabalho em J?

Resolução: 10×2×1/2=10 J.

### 4. Qual a energia cinética em J de uma massa 2 kg a 2 m/s?

Resolução: 2×4/2=4 J.

### 5. No bloco do exemplo, qual o trabalho resultante em J?

Resolução: 30−6=24 J.

### 6. No bloco do exemplo, qual a energia cinética final em J?

Resolução: 4+24=28 J.

### 7. Sem força aplicada, com K inicial=4 J e atrito de módulo 2 N, qual a distância de parada em m?

Resolução: d=4/2=2 m.

### 8. Uma conta prevê K final negativa depois de um deslocamento solicitado. No modelo do bloco freado, isso indica:

- Rapidez imaginária que devemos usar

- O bloco para antes e o trecho solicitado não é alcançado

- Energia cinética negativa é normal

Resolução: É preciso localizar a parada e interromper a etapa de deslizamento.

### 9. Uma força de 3 N alinhada com velocidade 2 m/s fornece qual potência em W?

Resolução: 3×2=6 W, unidade equivalente a J/s.

## Experimento

Salve experiment.py e rode `python3 experiment.py`. Com test_experiment.py ao lado, use `python3 -m unittest discover -p 'test_*.py'`. Só biblioteca padrão. Contrato didático: massa de 10⁻⁶ a 1000 kg, força aplicada de 0 a 1000 N, μ de 0 a 5 e distância de 0 a 1000 m. Valores finitos, sem booleanos. Estas faixas limitam a implementação, não são limites da lei física.

## Revisão pessoal

Derive o teorema a partir de Newton; resolva força variável, atrito e parada; explique quando energia mecânica é conservada e qual sistema foi definido. As demais aulas de Física 1 e a revisão pessoal continuam pendentes.
