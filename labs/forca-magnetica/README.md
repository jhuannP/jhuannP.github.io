# Força magnética, energia e movimento ideal

Rascunho original · 27/10/2026 · revisão pessoal pendente.

## A força completa contém dois termos

Para uma partícula de carga q e velocidade v, os campos externos E e B exercem a força de Lorentz F=q(E+v×B). Cada campo e a velocidade devem ser avaliados na posição e no instante da partícula. O produto vetorial determina a orientação magnética; o sinal de q pode invertê-la. Neste recorte tratamos uma partícula clássica de prova, sem colisões, reação de radiação ou alteração dos campos pela própria partícula.

F = q(E + v × B)

## O produto vetorial precisa de eixos orientados

Adote eixos cartesianos de mão direita, com x×y=z, y×z=x e z×x=y. Inverter a ordem muda o sinal. Em componentes, v×B=(vᵧBz−vzBᵧ, vzBx−vxBz, vxBᵧ−vᵧBx). No exemplo v=(3,0,0) m/s e B=(0,0,4) T, x×z=−y e a componente y do produto é −12. Multiplicar por q=2 C dá Fᵧ=−24 N. O exemplo usa valores didáticos, sem representar uma partícula real medida.

## Mudar a carga não muda a regra geométrica

Com os mesmos v e B, trocar q por −q inverte F_B. Trocar apenas v por −v ou apenas B por −B também inverte a força magnética; inverter ambos preserva v×B. Para q=−2 C no exemplo, Fᵧ=+24 N. A regra da mão direita determina v×B; depois aplicamos o sinal da carga. Não use a mesma seta de força para cargas de sinais opostos.

## Módulo, ângulo e unidades

O módulo é |F_B|=|q|vB sin θ, com θ entre v e B. Se v é paralela ou antiparalela a B, a força magnética é zero; se é perpendicular, o módulo é máximo para q,v,B fixos. Uma partícula em repouso não recebe esse termo, mas ainda pode receber qE. Em SI, tesla equivale a N·s/(C·m), de modo que C×(m/s)×T fornece newton.

|F_B| = |q| v B sin θ

## Por que a força magnética não realiza trabalho

A potência instantânea é F·v. Como v×B é perpendicular a v, (v×B)·v=0 e a contribuição magnética é nula. Assim dK/dt=qE·v para a força de Lorentz no modelo. A nulidade do termo magnético é uma identidade instantânea; campos que variam no tempo podem estar acompanhados de E induzido, que pode realizar trabalho. Portanto não conclua que um campo magnético variável impede transferência de energia em um sistema completo.

P_B = q(v×B)·v = 0

## Rapidez constante ainda permite aceleração

Com E=0 e sem outras forças, K=mv²/2 e a rapidez permanecem constantes no regime não relativístico, mas o vetor velocidade pode mudar de direção. Uma força perpendicular curva a trajetória. Não confunda ausência de trabalho com ausência de força, aceleração ou mudança de posição. A trajetória circular exige também campo uniforme e componente inicial perpendicular não nula.

## Separar componentes em um campo uniforme

Escolha B=Bz z, constante, E=0, e massa m>0. As equações são dvx/dt=ωvᵧ, dvᵧ/dt=−ωvx e dvz/dt=0, com ω=qBz/m, que pode ter sinal. A componente paralela vz é constante; a componente transversal gira sem mudar seu módulo. Aqui a frequência angular positiva de giro é |ω|: o sinal de ω serve para orientar o movimento, não para definir um período negativo.

ω = qBz/m

## Raio e período usam magnitudes

No plano transversal, a força fornece a aceleração centrípeta: |q|v⊥B=mv⊥²/r. Para v⊥>0 e |q|B>0, r=mv⊥/(|q|B) e T=2πm/(|q|B). A velocidade paralela não entra no raio. Se q=0 ou B=0, não há giro magnético e essas divisões não definem um raio/período. Se v⊥=0, a trajetória é uma reta paralela ao campo, não uma circunferência percorrida com raio zero.

r = mv⊥/(|q|B); T = 2πm/(|q|B)

## Uma componente paralela produz uma hélice

Quando v⊥ e v∥ são não nulos, o giro transversal e o movimento uniforme paralelo compõem uma hélice. O deslocamento axial por volta é v∥T, com sinal relativo ao eixo escolhido; o comprimento do passo da hélice é |v∥|T. Para m=1 kg, q=2 C, Bz=4 T e v(0)=(3,0,4) m/s, a rapidez é 5 m/s, r=3/8 m, |ω|=8 s⁻¹, T=π/4 s e o deslocamento axial por volta é π m. São parâmetros sintéticos da mesma mecânica clássica.

## Uma solução explícita permite conferir sinais

Com os dados anteriores e r(0)=0, uma solução é x(t)=(3/8)sin(8t), y(t)=(3/8)[cos(8t)−1] e z(t)=4t. Derivar fornece v=(3cos(8t),−3sin(8t),4), que começa no sentido +x e curva para −y, como a força inicial. Substituir a derivada de v nas equações confirma a solução. O centro da circunferência projetada é (0,−3/8), não a origem. Após T=π/4, a projeção retorna e z aumenta π m.

## O termo elétrico pode mudar a energia

No mesmo instante inicial, acrescentar E=(1,0,0) N/C dá força elétrica (2,0,0) N e potência qE·v=6 W para v=(3,0,4) m/s. A força magnética continua com potência zero. Isso não autoriza conservar a rapidez da trajetória anterior: as equações agora são outras. Uma hélice de rapidez constante foi deduzida para E=0, não para campos arbitrários superpostos.

## Um integrador pode criar energia que o modelo não permite

No teste transversal, Euler explícito usa vx seguinte=vx+hωvᵧ e vᵧ seguinte=vᵧ−hωvx. Ao elevar ao quadrado e somar, os termos mistos se cancelam e v⊥² seguinte=[1+(ωh)²]v⊥². Para ωh≠0, há ganho artificial em cada passo. A perpendicularidade da força no contínuo não garante conservação na atualização discreta. Essa é uma propriedade do método, não trabalho físico realizado pelo campo.

v⊥,n+1² = [1+(ωh)²] v⊥,n²

## Duas verificações distintas no laboratório

A parte racional calcula produto vetorial, força e potência sem arredondamento para entradas racionais. A solução helicoidal permite conferir posição, velocidade, aceleração, raio e rapidez. Um experimento numérico separado chama o integrador Euler já existente: no exemplo, h=1/8 s faz ωh=1, e a energia transversal dobra por passo. A energia total inicial é 25/2 J; após quatro passos Euler produz 80 J, enquanto a solução física permanece em 25/2 J. Não é uma comparação experimental ou um solver de plasma.

## Onde o modelo deixa de bastar

O raio constante foi deduzido para B uniforme, E=0 e movimento não relativístico. Campos não uniformes podem produzir outros comportamentos; altas velocidades exigem momento relativístico, e sistemas coletivos requerem tratar as fontes e interações. Aulas sobre espelhos magnéticos, deriva, radiação ou plasmas não são substituídas por esta hélice. Do mesmo modo, uma força sobre corrente distribuída exige definir e integrar a distribuição, em outro recorte.

## Uma revisão de vinte minutos

Calcule o produto vetorial antes de aplicar q, confira unidades e prove a potência magnética nula. Depois decomponha v=(3,0,4), obtenha raio/período e interprete o deslocamento por volta. Por fim, derive o fator de ganho de energia do Euler e explique por que ele é numérico. O painel mostra uma força instantânea; não deve ser lido como integração da trajetória. Revisão pessoal e execução de Jhuann permanecem pendentes.

## Exercícios e resoluções

1. Para q=2 C, v=(3,0,0) m/s, E=0 e B=(0,0,4) T, quanto vale Fᵧ em newtons?

   Resolução: q(−vxBz)=−24.

2. A força magnética isolada pode aumentar rapidez pelo trabalho q(v×B)·v?

   Resolução: Esse produto é zero.

3. Com q=−2 C, v=(3,0,0) m/s e B=(0,0,4) T, quanto vale Fᵧ em N?

   Resolução: (−2)(−12)=+24 N.

4. Para E=0 e velocidade paralela ao campo B, qual o módulo da força magnética em N?

   Resolução: O produto vetorial é zero.

5. No exemplo m=1 kg, q=2 C, B=4 T e v=(3,0,4) m/s, qual é o raio em metros?

   Resolução: Use v⊥=3: r=3/(2×4)=3/8 m.

6. Qual a rapidez inicial para v=(3,0,4) m/s?

   Resolução: √(3²+4²)=5 m/s.

7. Qual a frequência angular positiva |ω| em s⁻¹ para m=1 kg, q=2 C e B=4 T?

   Resolução: |q|B/m=8 s⁻¹.

8. Qual a energia cinética em joules para m=1 kg e rapidez 5 m/s?

   Resolução: K=mv²/2=25/2 J.

9. Com q=2 C, E=(1,0,0) N/C e v=(3,0,4) m/s, qual a potência elétrica em watts?

   Resolução: qE·v=2×3=6 W.

10. No teste do laboratório, qual a energia total em J após quatro passos de Euler com ωh=1?

   Resolução: v⊥²=9×2⁴=144, vz²=16; K=(144+16)/2=80 J.

11. Uma força de potência nula pode mudar a direção da velocidade?

   Resolução: Pode produzir aceleração perpendicular, sem mudar a rapidez.

12. A trajetória em um campo B qualquer é sempre uma hélice de raio constante?

   Resolução: A dedução usou campo uniforme, E=0 e regime clássico.

## Fontes e limites da leitura

CCM0212, itens1/5, programa reaberto em27/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212 . Ativação15/07/2025, compatível com semestre de aprovação, sem provar versão ministrada. Versão de2024 não recuperada.

Nussenzveig, Curso de Física Básica, vol.3/Eletromagnetismo, segunda edição revista e ampliada2015, reimpressão2017 e edição digital2018 conforme registro editorial anterior: §7.1 pp.128–129/PDF129–130, consulta textual parcial em27/10. P.128/PDF129 renderizada e inspecionada visualmente: força completa, potência e movimento em campo uniforme. Paginação PDF contada a partir de1; confirmada nesses recortes. Edição oficial citada de1997 não presumida equivalente. Exemplos com sinal usam |q| em grandezas positivas e ω=qBz/m com sinal; não se transporta uma convenção de magnitude sem explicação. Livro privado não distribuído; sem leitura integral.

OpenStax University Physics vol.2 §11.3: https://openstax.org/books/university-physics-volume-2/pages/11-3-motion-of-a-charged-particle-in-a-magnetic-field . Consulta parcial em27/10 para movimento circular, potência e decomposição. Raio/período escritos aqui com magnitudes para permitir carga negativa sem raio negativo. Página inicial de Feynman II também foi aberta, mas não fundamenta recortes adicionais alegados neste bloco. Figuras, parâmetros, exercícios e auditoria são originais, não transcrições de problemas dos autores.

## Laboratório

`force.py`: vetores de três componentes e escalares int/Fraction; rejeita float/bool para manter referências racionais exatas. Calcula produto vetorial, força e potência por produto escalar, com unidades SI declaradas na atividade. Não infere campos a partir de fontes.

`audit.py`: solução analítica fixa para m=1,q=2,Bz=4,v0=(3,0,4),r0=0 e auditoria do Euler em numerics4, importado da raiz. Não é um integrador novo ou arquivo autônomo. Execute da raiz:

```sh
python3 -m labs.forca-magnetica.force
python3 -m labs.forca-magnetica.audit
python3 -m unittest discover -s labs/forca-magnetica -t .
```

Testes conferem bases orientadas, carga com sinal, potência e perpendicularidade em729 pares de vetores; hélice por derivadas numéricas independentes, raio e rapidez; ganho artificial do Euler contra lei algébrica e contratos. A identidade física é provada no texto; a grade finita de testes não substitui a demonstração ou validação experimental.

## Registro pessoal — preencher ao estudar

- Data:
- Como conferi orientação e sinal:
- Como provei potência nula:
- Como interpretei raio, período e passo da hélice:
- Como distingui erro numérico de trabalho físico:

Campos não uniformes, radiação, relatividade, efeitos coletivos e evidências experimentais permanecem fora do recorte. Nenhum domínio pessoal certificado.
