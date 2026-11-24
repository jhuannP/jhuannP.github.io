# Momento e colisão: o sistema escolhido importa

22/10/2026. Notas de aula em rascunho para revisão de Jhuann. Percurso próprio de reforço do Ensino Médio; não nova disciplina do histórico. Pré-requisitos: massa, velocidade com sinais, força resultante, energia cinética e álgebra de primeiro grau. Python é opcional.

## Momento inclui direção e massa

Em um eixo, p=mv tem sinal. Dois corpos em sentidos opostos podem ter momento total zero mesmo ambos se movendo. Momento não é energia cinética.

p_total=Σmi vi

## Conservar requer impulso externo desprezível

Durante colisão, se o impulso externo no sistema é pequeno, p_total se conserva. Se os corpos ficam juntos, a velocidade final comum é momento inicial dividido pela massa total.

v_final=(m1u1+m2u2)/(m1+m2)

## Energia cinética pode diminuir

Uma colisão em que corpos se unem normalmente transforma parte de K em deformação/calor. Isso não significa desaparecimento de energia total; exige ampliar a contabilidade do sistema.

momento conservado não garante K conservada

## Escolha o sistema antes de escrever a conservação

Vamos acompanhar dois corpos de massas positivas e constantes m₁ e m₂ em uma direção. O eixo positivo é escolhido uma única vez. u₁ e u₂ são velocidades imediatamente antes do contato; v₁ e v₂, imediatamente depois. Os sinais pertencem às velocidades, não às massas. Momento total P=m₁u₁+m₂u₂ tem unidade kg·m/s; energia cinética K=(m₁u₁²+m₂u₂²)/2 tem unidade joule. A direção não desaparece de P, mas o quadrado retira o sinal da velocidade em K.



## Impulso é a mudança de momento no intervalo

Para um corpo, J=Δp. Se conhecemos a força resultante média no intervalo Δt, podemos escrever J=F_média Δt. A unidade N·s equivale a kg·m/s. Não é necessário que a força instantânea seja constante: média e duração precisam corresponder ao mesmo intervalo. Para o sistema de dois corpos, é o impulso resultante externo que determina ΔP. Na aproximação de impulso externo desprezível, usamos P_final=P_inicial.

J_ext=P_final−P_inicial

## As forças internas mudam cada corpo sem mudar o total

Durante o contato, um corpo exerce força no outro, e recebe uma força oposta no mesmo instante. Integrando no mesmo intervalo, os impulsos internos também são opostos: J₁,interno+J₂,interno=0. Essas forças atuam em corpos diferentes. No balanço de cada corpo elas importam; no balanço do sistema, cancelam. Com impulso externo desprezível, cada momento individual pode mudar muito enquanto a soma se conserva. Massas diferentes não tornam as forças de interação diferentes em módulo.

Δp₁+Δp₂=0, se J_ext≈0

## Se os corpos aderem há uma única velocidade final

A hipótese de adesão acrescenta v₁=v₂=v. Substitua no balanço: m₁u₁+m₂u₂=m₁v+m₂v=(m₁+m₂)v. Como a massa total é positiva, podemos dividir por ela. A velocidade comum é uma média ponderada pelas massas e fica entre u₁ e u₂. Não é em geral a média aritmética: isso ocorre quando as massas são iguais.

v=(m₁u₁+m₂u₂)/(m₁+m₂)

## Dois corpos de 1 kg aderem: confira os balanços

Dois corpos de 1 kg, com u₁=4 m/s e u₂=0, aderem. Antes, P=1×4+1×0=4 kg·m/s e K=(1×4²+1×0²)/2=8 J. Depois, a massa total é 2 kg e v=2 m/s: P=2×2=4 kg·m/s, K=2×2²/2=4 J. O primeiro recebe impulso −2 N·s; o segundo, +2 N·s. Momento total é preservado, mas a energia cinética de translação cai 4 J.



## Momento total zero não significa energia cinética zero

Agora use massas de 1 kg com velocidades +3 e −3 m/s. O momento total é 0 e, após aderirem, v=0. Antes, K=(9+9)/2=9 J; depois, K=0. Os momentos de sentidos opostos cancelam na soma; as energias cinéticas positivas somam. O sistema pode estar sem movimento do centro de massa e ainda ter movimento relativo entre seus componentes.

P_inicial=0; K_inicial=9 J; K_final=0

## Derive a redução da energia cinética

Na adesão, K_final=(m₁+m₂)v²/2=(m₁u₁+m₂u₂)²/[2(m₁+m₂)]. Faça K_inicial−K_final com o mesmo denominador. O numerador é (m₁+m₂)(m₁u₁²+m₂u₂²)−(m₁u₁+m₂u₂)². Os termos m₁²u₁² e m₂²u₂² cancelam; restam m₁m₂(u₁²−2u₁u₂+u₂²)=m₁m₂(u₁−u₂)². A queda é, portanto, não negativa e vale zero se as velocidades iniciais forem iguais. Definindo μ=m₁m₂/(m₁+m₂), a escrita curta é μ(u₁−u₂)²/2.

K_inicial−K_final = m₁m₂(u₁−u₂)²/[2(m₁+m₂)]

## A energia total exige um balanço mais amplo

K aqui é a soma das energias cinéticas de translação dos dois corpos. Durante uma adesão real, deformações e outros movimentos internos podem armazenar parte da energia. Se o sistema puder ser tratado como energeticamente isolado no intervalo, com outras energias macroscópicas desprezíveis, a queda de K corresponde ao aumento de energia interna. Momento conservado, sozinho, não garante isolamento energético. Som, transferência térmica e trabalho externo, quando relevantes, precisam entrar no balanço; a conta de K não fornece temperatura ou mecanismo de dissipação.



## Uma colisão elástica precisa de outra condição

Na colisão elástica ideal também se conserva a soma das energias cinéticas. Os corpos não precisam terminar com velocidade comum. Por exemplo, para massas iguais com velocidades iniciais 4 e 0 m/s, a solução de colisão elástica em uma dimensão troca as velocidades: 0 e 4 m/s. O momento continua 4 kg·m/s e K continua 8 J. Essa comparação usa outro modelo de contato; não aplique a fórmula da velocidade comum a toda colisão. O laboratório desta aula implementa apenas adesão, não colisões elásticas gerais.



## O que os estados antes e depois não determinam

Dos valores iniciais e finais, calculamos impulsos, mas não a duração do contato ou o pico de força. No exemplo inicial, J₁=−2 N·s. Se uma duração de 0,1 s fosse fornecida como hipótese adicional, a força média seria −20 N; com 0,2 s seria −10 N. Ambos têm o mesmo impulso. Não confunda essa média com a força máxima, nem tente deduzir Δt só pela conservação de momento.

F_média=J/Δt, com Δt fornecido e positivo

## Reconstrua o balanço antes de executar o código

Primeiro escolha os dois corpos como sistema, fixe o eixo e registre a hipótese de impulso externo desprezível. Depois use a adesão para obter v e calcule P e K antes/depois. O Python opcional usa frações exatas e devolve também impulsos individuais; ele não decide se os corpos se encontram, aderem ou ficam isolados na situação real. Velocidades iguais representam um limite algébrico sem movimento relativo, e não comprovam uma colisão. Geometria de encontro, contato deformável, força no tempo, rotação e colisões em duas dimensões permanecem pendentes.



## Exemplo preservado e conferido

Dois corpos de 1 kg com velocidades 4 e 0 m/s aderem: v=2 m/s; momento total 4 kg·m/s antes e depois; K passa de 8 para 4 J. Os impulsos individuais são −2 e +2 N·s.

## Exercícios e resoluções

1. Qual velocidade em m/s?

   Resolução: 4/2=2.

2. Conservar momento garante conservar K em toda colisão?

   Resolução: Colisões inelásticas podem reduzir K.

3. Dois corpos de 1 kg têm velocidades +3 e −3 m/s. Qual é o momento total em kg·m/s?

   Resolução: 3−3=0; os momentos têm sinais opostos.

4. Nos mesmos dois corpos, qual é a energia cinética total inicial em J?

   Resolução: (1×3²+1×(−3)²)/2=9 J.

5. Corpos de 2 kg e 1 kg, com u₁=3 e u₂=0 m/s, aderem. Qual é v em m/s?

   Resolução: Momento 6 kg·m/s dividido pela massa total 3 kg: 2 m/s.

6. No exemplo original de dois corpos de 1 kg, qual é o impulso no primeiro corpo, que passa de 4 para 2 m/s, em N·s?

   Resolução: J₁=1(2−4)=−2 N·s.

7. No exemplo original, qual a queda K_inicial−K_final em J?

   Resolução: K_inicial=8 J; K_final=4 J; diferença 4 J.

8. Se o impulso no primeiro corpo é −2 N·s e a duração fornecida é 0,1 s, qual a força média em N?

   Resolução: F_média=−2/0,1=−20 N; isso não determina a força máxima.

9. As forças internas de contato cancelam no balanço de qual sistema?

   Resolução: São forças em corpos diferentes. Cancelam ao somar os dois balanços.

10. A fórmula de uma velocidade final comum vale automaticamente para colisões elásticas?

   Resolução: Ela inclui a hipótese de adesão; a colisão elástica ideal conserva K e em geral tem duas velocidades finais distintas.

11. Só conservar momento prova que a queda de K é inteiramente aumento de energia interna do sistema?

   Resolução: É preciso verificar também trabalho externo, transferências de energia e outras formas de energia relevantes.

12. No limite algébrico u₁=u₂, qual a queda de K prevista pela fórmula da adesão, em J?

   Resolução: O fator (u₁−u₂)² é zero; velocidades iguais não comprovam que uma colisão aconteceu.

## Fontes e limites

Consulta pública parcial em 22/10/2026:

- [OpenStax Physics §8.1](https://openstax.org/books/physics/pages/8-1-linear-momentum-force-and-impulse): momento, sinais, unidades e impulso por força média.
- [OpenStax Physics §8.2](https://openstax.org/books/physics/pages/8-2-conservation-of-momentum): escolha de sistema e cancelamento das forças internas.
- [OpenStax Physics §8.3](https://openstax.org/books/physics/pages/8-3-elastic-and-inelastic-collisions): comparação entre adesão e colisão elástica ideal.
- [OpenStax College Physics 2e §8.4](https://openstax.org/books/college-physics-2e/pages/8-4-elastic-collisions-in-one-dimension): duas equações de conservação e necessidade de duas velocidades finais no caso elástico.

Não foram copiados textos, exercícios, soluções ou figuras das fontes. Não se afirma leitura integral, vídeo assistido, execução de experimento ou alinhamento a um exame específico. O código implementa apenas o balanço de adesão; o exemplo elástico é comparação teórica, sem solucionador elástico geral. A queda de K não determina temperatura, som ou deformação. Ausência de impulso externo não substitui o balanço energético.

## Reprodução

Na raiz do site, sem pacotes adicionais:

```sh
python3 -m labs.colisao-sistema.experiment
python3 -m unittest discover -s labs/colisao-sistema -t .
```

A função aceita inteiros e Fraction, excluindo bool e float para preservar seu contrato exato. Não decide se objetos se encontram ou aderem fisicamente. Nenhuma posição, duração de contato ou força instantânea é simulada. Os estados são sintéticos; não representam ensaio experimental, resultado da IC ou comprovação de domínio pessoal.

## Verificação em 22/10/2026

Cinco testes novos aprovados; suíte global com 829 testes Python e 485 estruturas MathML. Navegador aceitou −2 para impulso e 4 para redução de K. Figura com texto alternativo inspecionada em 390 px, sem rolagem horizontal e sem erros de console observados. Revisão de Jhuann e uso com aluno pendentes.
