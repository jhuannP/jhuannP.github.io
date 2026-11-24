# Colisão oblíqua lisa — rascunho original

29/10/2026. Apoio de IA para revisão pessoal de Jhuann; não medição,resultado da IC ou certificação de domínio.

## Reprodução e domínio

Da raiz do protótipo:

```sh
python3 -B -m labs.colisao-obliqua.impact
python3 -B -m unittest discover -s labs/colisao-obliqua -t .
```

Inteiros/Fraction,sem bool ou float. Massas kg>0,velocidades2D em m/s,e racional em[0,1],normal racional exatamente unitária orientada do1 ao2. Impulso N·s,energia J. Normal não é calculada de posições;contato já é fornecido. Não há detector,integração temporal,raios ou trajetórias. Para g≤0 o algoritmo devolve velocidades intactas/J0,sem adesão. O modelo é binário,normal fixa,liso,sem impulso externo e sem mudança de spin. Seis métodos aprovados,casos internos não são métodos adicionais.

## Deduções e exemplos

### Do encontro frontal ao contato oblíquo

As seções iniciais tratam a colisão em uma dimensão; sua velocidade comum com e=0 pertence a esse caso. Agora imagine dois discos ou esferas lisos no instante de um contato binário. Defina a normal unitária n do centro 1 para o centro 2 e uma tangente unitária τ perpendicular a ela. Em2D, conservamos duas componentes do momento total, mas isso não determina sozinho quatro componentes de velocidades finais. A geometria do contato e a lei de interação também importam. O laboratório recebe n pronta; não deduz o contato a partir de trajetórias.

### As hipóteses tornam o impulso puramente normal

Massas constantes positivas, corpos sem atrito no contato, sem adesão e impulso externo desprezível durante a colisão. A normal é considerada fixa no curto evento. Não há impulso tangencial e, por isso, cada corpo conserva sua própria componente tangencial de velocidade. Como a força normal passa pelos centros, não há torque de contato que mude o spin nesse modelo; não resolvemos rotações ou contato rugoso. Usamos e normal prescrito entre 0 e 1, sem liberação de energia interna: colisões superelásticas e materiais reais não são descritos por esse recorte.

### Aproximação usa velocidade relativa com sinal

Escreva g=(u₁−u₂)·n. Se g>0, os centros estão se aproximando na direção normal: a distância diminuiria na ausência do impulso. A separação normal depois deve satisfazer (v₂−v₁)·n=e g, ou (v₁−v₂)·n=−e g. A componente tangencial relativa não é multiplicada por e. Aplicar v₂−v₁=e(u₁−u₂) como igualdade vetorial em 2D mudaria também a tangente e violaria a hipótese de contato liso.

### Impulsos opostos fecham o balanço vetorial

Se J≥0 é a magnitude do impulso normal repulsivo, o corpo 1 recebe −Jn e o corpo 2 recebe +Jn. Assim v₁=u₁−(J/m₁)n e v₂=u₂+(J/m₂)n. Multiplicar por cada massa e somar cancela o impulso interno exatamente, conservando P=m₁u₁+m₂u₂. Projetar emτ mostra v_i·τ=u_i·τ. O impulso tem unidade N·s=kg·m/s; sem duração ou história do contato ele não fornece força máxima ou potência instantânea.

### A restituição determina a magnitude do impulso

A nova velocidade relativa normal é g−J(1/m₁+1/m₂). Igualar a −e g dá J=(1+e)g/(1/m₁+1/m₂)=μ(1+e)g, com μ=m₁m₂/(m₁+m₂). Essa dedução só aplica o impulso quando g>0 e contato já foi identificado. Para g≤0, o modelo unilateral usa J=0: não cria uma força atrativa para forçar outra colisão entre corpos que já se afastam. e não é determinado pela conservação do momento nem calculado pelas massas.

### A perda depende da aproximação normal, não de todo o movimento

Para duas massas, K=|P|²/[2(m₁+m₂)]+μ|u₁−u₂|²/2. O primeiro termo e a componente tangencial relativa não mudam. O módulo da componente normal cai de g para e g, logo K_antes−K_depois=μ(1−e²)g²/2. Alternativamente, substituir as velocidades com impulso dá ΔK=−Jg+J²/(2μ). Essa segunda forma confere sinais e unidades sem repetir a decomposição do centro de massa. A energia convertida em outros modos não desapareceu; o cálculo não a separa em calor, som ou deformação.

### Um exemplo próprio fixa a orientação antes das contas

Use m₁=2 kg, m₂=3 kg, u₁=(3, 1)m/s, u₂=(−1, 0)m/s e n=(3/5, 4/5). A tangente escolhida é τ=(−4/5, 3/5). A normal é unitária porque 9/25+16/25=1. As componentes normais iniciais são 13/5 e −3/5 m/s, logo g=16/5 m/s; as tangenciais são −9/5 e 4/5 m/s. Com e=1/2 e μ=6/5 kg, o impulso é J=144/25 N·s. Os valores são prescritos para estudo, não medições de uma colisão real.

### Reconstruir velocidades e energia dá duas conferências

Aplicando os impulsos, v₁=(159/125,−163/125)m/s e v₂=(19/125,192/125)m/s. O momento total permanece P=(3,2)kg·m/s. As componentes normais finais são −7/25 e 33/25 m/s; portanto (v₁−v₂)·n=−8/5 m/s, metade da aproximação inicial com sinal invertido. K cai de 23/2 J para 1723/250 J: a diferença é 576/125 J=4,608 J. As duas velocidades tangenciais individuais permanecem −9/5 e 4/5 m/s. A figura separa componentes e balanço energético, sem representar deslocamento ou trajetória.

### e igual a zero não exige colagem na colisão oblíqua

Se e=0, a velocidade relativa normal final é zero. Na colisão 1D isso deixa uma única velocidade comum, como no exemplo antigo. Em2D liso, a diferença tangencial pode continuar não nula. Nos dados novos ela vale −13/5 m/s e permanece assim mesmo com e=0; logo v₁≠v₂. Colagem completa exigiria também anular essa diferença e uma descrição de adesão ou outro impulso tangencial. Não extrapole o significado do caso frontal para um modelo que preserva a tangente.

### Elasticidade e geometria não dispensam condições adicionais

Com e=1, toda a energia cinética translacional deste modelo se conserva. Ainda assim o resultado depende da normal de contato: conservar P e K não determina uma direção arbitrária de espalhamento. Para massas iguais, uma inicialmente em repouso e colisão elástica com ambas as velocidades finais não nulas, elevar P_final=P_inicial ao quadrado e usar K dá v₁·v₂=0. Se uma velocidade é zero, não se define um ângulo de 90° com esse vetor. A lei de contato fornece a informação geométrica que faltava.

### Mudar referencial é um teste do modelo

Adicionar a mesma velocidade constante às duas partículas mantém g,J e a redução de K: o momento total se conserva, então os termos de mudança de referencial se cancelam na diferença energética. K_antes e K_depois individualmente mudam. Girar os eixos exige girar também n e ambas as velocidades; os valores escalares de J e da perda não mudam. Trocar os rótulos 1/2 exige inverter n. Inverter só a normal sem trocar os corpos mudaria a identificação de aproximação e não representa a mesma entrada física.

### O que o laboratório pode e não pode demonstrar

O código usa frações racionais exatas para massas, componentes, e e normal unitária racional. Compara a solução por impulso à solução das componentes normais pelo centro de massa, fecha momento e energia e testa mudanças de eixos/referencial. Não determina posições, raios, instante ou existência de contato, sobreposição, forças máximas, tempo de colisão ou energia de spin. Uma normal fornecida não é evidência de que trajetórias reais se interceptam. Contato rugoso, deformação temporal, medições e revisão pessoal seguem pendentes; a simulação anterior continua sendo frontal 1D.

## Verificações independentes

Seis métodos:fixture numérica exata;144 modelos em base normal/tangente comparados ao oráculo independente pelo movimento do CM normal e restituição;144 balanços de momento/perda deK e trabalho do impulso;12 transformações de eixos/reflexão/boost e troca de rótulos;limites1D elástico/inelástico,caso oblíquo e0 sem colagem e ausência de impulso para separação/tangência;contratos.

O código de produção isola J e aplica impulsos. O oráculo usa diretamente a velocidade normal do CM e a diferença relativa normal final,conservando as duas componentes tangenciais antes de recompor vetores. Os dois balanços energéticos usam expressões independentes:decomposição relativa e trabalho−Jg+J²/(2μ). Frações removem arredondamento do exemplo,não validam a lei de contato. Não há regressão a dados de material,e não se determina e a partir de massas.

## Fontes efetivamente consultadas

- Nussenzveig,Curso de Física Básica1,5ªedição2013,reimpressão2017,confirmado no texto inicial do exemplar. Consulta textual parcial29/10/2026 de§§9.2–9.3 pp.212–213/PDF213–214 e§9.6 pp.219–221/PDF220–222; p.220/PDF221 inspecionada visualmente,Eq.9.6.4 e insuficiência das conservações sem dado extra. Não copiados figuras,exemplos,exercícios ouPDF. A seção9.6 trata configuração elástica geral,não é apresentada como fonte do nosso código de restituição inelástica oblíqua.
- [JönköpingUniversity,Applied Mechanics§7.5](https://mechanics.ju.se/Kinetics/ImpulseMomentum.html),trechos Central impact e Oblique impact,consulta textual parcial29/10/2026. Normal,tangente e restituição consultados;sem incorporar exemplos de futebol,tênis,simulador de piso ou comportamento material real. Vetores,números,figura,derivação e testes locais próprios.
- [JúpiterCCM0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0112),reaberto29/10/2026,item9 colisões e bibliografia Feynman/Nussenzveig. Ativação15/07/2024 posterior à aprovação2023/2;versão ministrada não recuperada. Registro do IF é distinto,sem equivalência administrativa inferida.

OpenStaxUP1§9.7 foi tentado mas inacessível nesta consulta,não usado como capítulo lido. Nenhum PDF ou caminho privado servido no site. Colisão frontal anterior,IDs,snippet,desafio e simulação preservados. Contato rugoso,spin,deformações,experimento real e revisão pessoal pendentes.
