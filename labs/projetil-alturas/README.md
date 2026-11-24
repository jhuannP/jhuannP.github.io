# Projétil: eventos e alturas diferentes

22/10/2026. Notas de aula originais com apoio de IA, em rascunho para revisão de Jhuann.

## Escolher sistema, eixos e instante inicial

Modele o corpo como uma partícula em movimento num plano, sob aceleração constante (0,−g), com g>0. O eixo y aponta para cima e t=0 é o instante de lançamento. Desprezamos resistência do ar, rotação da Terra e variação do campo gravitacional. Defina x₀,y₀ e as componentes iniciais v₀x,v₀y. Os números novos desta aula são dados hipotéticos em metros e segundos, com g=10 m/s² como valor didático.

a=(0,−g)

## Integrar as componentes usa um único tempo

Da aceleração horizontal zero, vₓ=v₀x e x=x₀+v₀xt. Da aceleração vertical −g, vᵧ=v₀y−gt e y=y₀+v₀yt−gt²/2. Os movimentos podem ser calculados por componentes, mas compartilham o mesmo t: não escolha um tempo para cada eixo ao localizar o corpo. As condições iniciais são recuperadas em t=0. Verifique as unidades: v₀yt e gt² são comprimentos, compatíveis com y.

y=y₀+v₀yt−gt²/2

## O exemplo de retorno à mesma altura

No exemplo original abaixo, y₀=0, v₀x=3 m/s, v₀y=4 m/s e g=10 m/s². Resolver y(T)=0 dá T=0 e T=2v₀y/g=0,8 s. A segunda raiz representa o retorno após subir; o alcance horizontal é 3×0,8=2,4 m. Se v₀x=v₀cosθ e v₀y=v₀sinθ, obtemos R=v₀²sin(2θ)/g. Maximizar em 45° pressupõe velocidade inicial fixa, alturas iguais e ausência de arrasto; isso não é uma regra universal.

Tretorno=2v₀y/g

## Um segundo exemplo começa acima do solo

Agora o chão está em y=0, mas o lançamento ocorre em x₀=0 e y₀=15 m, com v₀x=8 m/s, v₀y=10 m/s e g=10 m/s². As equações ficam x=8t e y=15+10t−5t², com t em segundos e posições em metros. O tempo de retorno a 15 m não é o tempo de chegada ao chão. Vamos determinar os dois eventos separadamente, sem reutilizar a fórmula de alturas iguais para o evento errado.

x=8t; y=15+10t−5t²

## O solo define uma equação para o evento final

Imponha y(T)=0 no segundo exemplo: 15+10T−5T²=0. Dividindo por −5, T²−2T−3=0=(T−3)(T+1). As raízes são 3 s e −1 s. Como a descrição começa em t=0, a chegada física ocorre em T=3 s, com x=8×3=24 m. A raiz negativa pertence à extensão matemática para tempos anteriores e não ao voo informado. Para altura inicial positiva, a raiz futura geral é (v₀y+√(v₀y²+2gy₀))/g.

Tsolo=3 s; Δx=24 m

## No ápice, só a componente vertical zera

Resolva vᵧ=10−10t=0: o ápice ocorre em t=1 s. Então x=8 m e y=15+10−5=20 m. A elevação em relação ao ponto de lançamento é 5 m, diferente da altura de 20 m em relação ao chão. No ápice, vₓ continua 8 m/s e a rapidez vale 8 m/s; o corpo não está parado. A aceleração vertical também continua −10 m/s². Velocidade vertical zero não implica força ou aceleração zero.

tápice=1 s; yápice=20 m

## A mesma altura é reencontrada antes do solo

No instante t=2 s, y=15+20−20=15 m e x=16 m. A velocidade vertical é −10 m/s, oposta à inicial. Esse é o retorno à altura do lançamento, não o impacto. Aplicar 2v₀y/g ao tempo de chão teria produzido 2 s e um deslocamento de 16 m, embora o corpo ainda esteja 15 m acima dele. Escrever a condição do evento antes de resolver evita essa troca de perguntas.

t=2 s: y=15 m, não zero

## Eliminar o tempo descreve a curva, não sua rapidez

Quando v₀x≠0, podemos usar t=(x−x₀)/v₀x na equação vertical para obter uma parábola. No segundo exemplo, t=x/8 leva a y=15+(5/4)x−(5/64)x². Essa curva diz quais posições são percorridas, mas a forma de y(x) sozinha não especifica o instante de passagem. Se v₀x=0, essa eliminação divide por zero; o movimento é vertical e deve ser tratado pela parametrização temporal.

y=15+(5/4)x−(5/64)x²

## A velocidade de chegada precisa de duas componentes

Em T=3 s, vₓ=8 m/s e vᵧ=10−30=−20 m/s. A rapidez é √(8²+20²)=√464 m/s, aproximadamente 21,54 m/s. O sinal negativo é da componente vertical, não da rapidez. Para calcular uma direção, use as duas componentes e o quadrante apropriado, por exemplo atan2(vᵧ,vₓ). A velocidade na chegada não tem o mesmo módulo da inicial neste exemplo, pois o corpo termina mais baixo.

v(T)=(8,−20) m/s

## A energia oferece uma conferência independente

Com gravidade uniforme e sem arrasto, a energia mecânica por unidade de massa é e=(vₓ²+vᵧ²)/2+gy, em J/kg. Inicialmente e=(64+100)/2+10×15=82+150=232 J/kg. No chão, e=(64+400)/2=232 J/kg. No ápice, e=64/2+10×20=32+200=232 J/kg. Substituir as expressões temporais e expandir os termos cancela as parcelas em t e t², demonstrando a identidade neste modelo; os testes exatos conferem a implementação.

e=(vₓ²+vᵧ²)/2+gy=232 J/kg

## O painel mostra o caso de alturas iguais

O painel já existente nesta aula trabalha com a trajetória de lançamento e retorno ao mesmo nível. Ele é apoio para esse caso e não foi alterado para representar a altura inicial de 15 m. Para comparar os quatro instantes do segundo exemplo, use a figura e o laboratório. Mudar a condição do solo ou incluir arrasto exige outro problema, não apenas trocar a legenda de uma fórmula de alcance.

## Intervalo físico e extensão algébrica

No segundo exemplo, o voo descrito vai de t=0 a t=3 s. As equações polinomiais continuam produzindo números depois, inclusive y<0, mas não modelam uma colisão com o chão. O laboratório state retorna essa extensão algébrica e deixa o intervalo físico explícito; landing_time calcula a primeira chegada futura ao plano. Se o corpo começa no solo com velocidade vertical nula ou para baixo, o contato é imediato no modelo. Para lançamentos inicialmente descendentes, o máximo no intervalo futuro pode ser a própria altura inicial. Nenhum resultado comprova uma trajetória real sem comparação com dados.

## Exercícios e resoluções

- Qual alcance em metros? **Resolução:** 3×0,8=2,4.
- 45° maximiza alcance para qualquer terreno e resistência? **Resolução:** O resultado depende das hipóteses de mesma altura e ausência de resistência.
- No segundo exemplo, y=15+10t−5t². Qual o tempo futuro de chegada ao solo, em s? **Resolução:** As raízes são 3 e −1; o tempo futuro é três segundos.
- Com v₀x=8 m/s e tempo de chegada de 3 s, qual o deslocamento horizontal, em m? **Resolução:** 8×3=24 m.
- Quanto tempo leva até o ápice no segundo exemplo, em s? **Resolução:** vᵧ=10−10t=0 fornece t=1 s.
- Qual a altura do ápice em relação ao solo, em m? **Resolução:** 15+10×1−5×1²=20 m.
- Qual a posição horizontal no ápice, em m? **Resolução:** x=8×1=8 m.
- Qual a altura y em t=2 s, em m? **Resolução:** 15+20−20=15 m, ainda acima do solo.
- Qual a componente vertical da velocidade em t=3 s, em m/s? **Resolução:** 10−10×3=−20 m/s.
- Qual a rapidez no ápice do segundo exemplo, em m/s? **Resolução:** vᵧ=0 e vₓ=8: rapidez oito.
- Qual a energia mecânica por unidade de massa do exemplo, em J/kg? **Resolução:** (64+100)/2+10×15=232 J/kg.
- A aceleração vertical se anula no ápice desse modelo? **Resolução:** A aceleração permanece −g; apenas vᵧ passa por zero.

## Fontes e execução

Nussenzveig I §3.6, pp.74–75 (PDF75–76), leitura textual parcial; [OpenStax, University Physics Volume 1, §4.3](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion), componentes e condições iniciais. Consultas parciais em 22/10/2026; sem reprodução de exercícios ou figuras. Segundo exemplo e laboratório originais.

Na raiz: python3 -m labs.projetil-alturas.experiment; testes: python3 -m unittest discover -s labs/projetil-alturas -t .

state usa int ou Fraction e devolve extensão polinomial, inclusive após contato; não aplica colisão. landing_time usa raiz em ponto flutuante e forma racionalizada para v₀y<0; isso não garante precisão para parâmetros arbitrariamente grandes. Altura inicial não negativa, g positiva e tempo não negativo.


## Projétil com alturas distintas — 22/10/2026

Aula f1-projetil ampliada de três seções/dois exercícios para 12 seções/12 exercícios. Exemplo antigo (3,4 m/s, altura inicial zero), Python, desafio, IDs e painel de alturas iguais preservados. Novo exemplo: x₀=0, y₀=15 m, v₀x=8 m/s, v₀y=10 m/s e g=10 m/s² didático. Ápice em 1 s, posição (8,20) m; retorno a 15 m em 2 s, posição horizontal 16 m; chegada ao solo em 3 s, posição horizontal 24 m e velocidade (8,−20) m/s. Energia específica 232 J/kg em todos os instantes do voo ideal.

Fontes primárias consultadas parcialmente em 22/10/2026: Nussenzveig I §3.6, pp.74–75 (PDF75–76), leitura textual para hipóteses, componentes, ápice e retorno ao mesmo nível; [OpenStax, University Physics Volume 1, §4.3](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion), equações com condições iniciais. Sem leitura integral, reprodução de figuras ou exercícios. Segundo exemplo, contas, gráfico e laboratório originais.

Laboratório labs/projetil-alturas/: state calcula coordenadas, componentes e energia por unidade de massa com frações exatas; a extensão polinomial não interrompe sozinha no chão. landing_time calcula o evento com raiz em ponto flutuante, incluindo forma racionalizada para velocidade inicial descendente; não há garantia de precisão arbitrária. Sem arrasto, colisão ou validação experimental.

Cinco testes novos e doze testes de catálogo aprovados. Verificações: eventos do exemplo; energia e identidade vertical em grade de parâmetros/tempos racionais; tempos de chegada construídos independentemente; translação horizontal/reflexão e contratos. 536 estruturas MathML aprovadas; catálogo revalidado após figura. Nenhum modelo JavaScript alterado, suíte global não repetida.

Navegador: figura e rótulos inspecionados em 390 px, largura da página igual à tela. Rótulo de chegada reposicionado para evitar cruzamento com a curva. Resposta +20 rejeitada e −20 aceita para a componente vertical final. Nenhum erro de console observado. Prévia: projetil-alturas-mobile.jpg. Imagem com carregamento tardio não reservava altura antes de carregar, observado no DOM; a inspeção foi concluída aproximando a seção. Próximo bloco de UX deve verificar reserva de espaço das figuras e saltos de leitura.

Estado: Física I tem 17 aulas/88 exercícios, seis recortes desenvolvidos e 11 introduções; 13 grupos parciais e uma lacuna, nenhum completo. Catálogo global 501 aulas/3044 exercícios em rascunho. Próxima revisão pessoal: distinguir os eventos de 1,2,3 segundos e reconstruir o balanço de 232 J/kg. Conteúdo assistido por IA não comprova aprendizagem pessoal. Próxima implementação global: conferir renderização de imagens da biblioteca e reservar seu espaço para melhorar navegação, antes de retomar outros conteúdos. Saldo semanal após bloco: 93%; parada operacional em 65%.
