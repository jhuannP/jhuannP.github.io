# Medidas indiretas e covariância — diferença linear

## Uma grandeza pode ser calculada a partir de duas leituras

Queremos estimar a diferença orientada L entre duas posições na mesma escala: L=X₂−X₁. Se as estimativas são x₁=20 cm e x₂=70 cm, o resultado é l=50 cm. Trocar a ordem daria −50 cm; o módulo seria outra função. Os números desta aula são sintéticos e não representam um objeto ou instrumento usado por Jhuann. O modelo precisa explicar também como as incertezas das duas entradas se relacionam.

## Expanda as flutuações antes de combinar incertezas

Escreva δX₁=X₁−E[X₁] e δX₂=X₂−E[X₂], ambos de média zero. A flutuação da diferença é δL=δX₂−δX₁. Elevando ao quadrado, obtemos (δL)²=(δX₂)²+(δX₁)²−2δX₁δX₂. A média desse produto cruzado é a covariância C₁₂. Assim Var(L)=v₁+v₂−2C₁₂, onde vᵢ=Var(Xᵢ). Para esta função linear, a identidade é exata quando os segundos momentos existem; não depende de uma aproximação por derivadas ou da hipótese de normalidade.

u²(L)=v₁+v₂−2C₁₂

## O sinal da operação altera o termo de covariância

Na diferença, os coeficientes de X₁ e X₂ são −1 e +1, daí o sinal negativo do termo cruzado. Para a soma X₁+X₂, os dois coeficientes são +1 e a variância contém +2C₁₂. Portanto uma covariância positiva reduz a variância da diferença, mas aumenta a da soma. Não existe uma regra geral de que correlação sempre aumenta a incerteza de qualquer grandeza derivada.

## Covariância nula é uma hipótese sobre o modelo

Se v₁=v₂=0,04 cm² e C₁₂=0, então u²(L)=0,08 cm² e u(L)≈0,2828 cm. Independência com variâncias finitas implica covariância nula, mas covariância nula não demonstra independência em geral. Saber apenas que cada leitura tem incerteza padrão 0,2 cm não informa C₁₂. Não podemos completar o orçamento escolhendo zero silenciosamente.

## Uma componente aditiva comum desaparece na subtração

Considere perturbações X₁=20 cm+B+E₁ e X₂=70 cm+B+E₂. No modelo, B, E₁ e E₂ têm média zero e são independentes; Var(B)=0,03 cm² e Var(E₁)=Var(E₂)=0,01 cm². Cada entrada tem variância 0,04 cm². Como B aparece nas duas, C₁₂=Var(B)=0,03 cm². Ao subtrair, L=50 cm+E₂−E₁: B cancela algebricamente. A variância restante é 0,02 cm². Os valores foram escolhidos para o exemplo, sem estimativa instrumental real.

(70+B+E₂)−(20+B+E₁)=50+E₂−E₁

## Conferir pelas marginais recupera o mesmo resultado

Usando as variâncias das entradas e sua covariância, u²(L)=0,04+0,04−2×0,03=0,02 cm²; a incerteza padrão é aproximadamente 0,1414 cm. Ignorar C₁₂ daria 0,08 cm², quatro vezes a variância correta deste modelo. A incerteza padrão errada seria duas vezes maior, pois é a raiz da variância. A distribuição sintética do laboratório permite conferir a conta diretamente, sem estimar covariância por uma amostra pequena.

## Duas correções independentes não são a mesma componente comum

Agora substitua B por B₁ na primeira leitura e B₂ na segunda, com B₁ e B₂ independentes e cada uma com variância 0,03 cm². As variâncias marginais continuam 0,04 cm², mas a covariância passa a zero. Logo a diferença volta a ter variância 0,08 cm². Os nomes “calibração” ou “mesmo tipo de instrumento” não determinam sozinhos se as componentes são compartilhadas. Isso depende da referência, do procedimento e dos dados disponíveis.

## Nem todo número pode ser uma covariância válida

Com v₁ e v₂ não negativas, uma matriz de covariância de duas entradas exige C₁₂²≤v₁v₂. Para v₁=v₂=0,04 cm², isso limita C₁₂ ao intervalo [−0,04,+0,04] cm². O valor +0,05 cm² é incompatível com essas variâncias e ainda produziria variância negativa para a diferença. O código rejeita tal entrada, em vez de transformar o resultado em zero. Se uma variância é zero, a covariância com essa entrada também deve ser zero.

C₁₂²≤v₁v₂

## Cancelamento tem condições: aditivo, comum e com mesmo coeficiente

Subtrair a mesma correção estimada b de ambas as posições preserva a diferença: (x₂−b)−(x₁−b)=x₂−x₁. Isso não autoriza cancelar dois efeitos apenas parecidos, uma deriva entre leituras ou um fator de escala multiplicativo. Se as posições são multiplicadas por um fator incerto k, a diferença também é multiplicada por k. O próximo modelo precisa então incluir esse fator; o laboratório desta aula trata apenas a combinação linear declarada.

## Unidades também entram na matriz de covariância

As entradas devem usar a mesma unidade de posição. Se passamos de cm para mm, multiplicamos as posições por 10 e as variâncias e a covariância por 100. Assim l=500 mm, v₁=v₂=4 mm² e C₁₂=3 mm² fornecem u²(L)=2 mm². Misturar posições em mm com covariância em cm² produz uma conta dimensionalmente inconsistente. A função não reconhece a unidade: ela deve ser declarada por quem prepara os dados.

## A identidade é exata; o orçamento pode continuar incompleto

Para a diferença linear, não houve truncamento de uma expansão de Taylor. Mesmo assim, o resultado depende da escolha das componentes, da estimativa de suas variâncias/covariâncias e da adequação do modelo de medição. Uma variância zero em um modelo de componente perfeitamente comum não demonstra ausência de toda incerteza experimental. Para medidas indiretas não lineares, como energia cinética ou g de um pêndulo, será preciso analisar sensibilidade e a validade da aproximação de primeira ordem.

## O laboratório compara dois espaços probabilísticos explícitos

O código recebe estimativas, variâncias e covariância como int ou Fraction; retorna diferença orientada e variância, sem escolher C₁₂ automaticamente. Os testes constroem distribuições finitas: uma com B compartilhado e outra com B₁/B₂ independentes. Somam probabilidades e momentos diretamente para conferir os resultados, além de testar mudança de unidade, limites e entradas inválidas. Os testes conferem essas contas; não provam o protocolo de um experimento real nem uma habilidade pessoal de bancada.

## Exercícios originais

- Com x₁=20 cm e x₂=70 cm, quanto vale l=x₂−x₁, em cm? **Resolução:** 70−20=50 cm.
- Com v₁=v₂=0,04 cm² e covariância nula, qual a variância de L, em cm²? **Resolução:** 0,04+0,04=0,08 cm².
- No modelo B compartilhado, Var(B)=0,03 cm². Quanto é C₁₂, em cm²? **Resolução:** As parcelas independentes não contribuem ao produto cruzado: C₁₂=Var(B).
- Com C₁₂=0,03 cm², quanto é o termo 2C₁₂, em cm²? **Resolução:** 2×0,03=0,06 cm².
- Com v₁=v₂=0,04 e C₁₂=0,03 cm², qual u²(L), em cm²? **Resolução:** 0,04+0,04−0,06=0,02 cm².
- Qual a razão entre a variância obtida ignorando a componente comum e a correta deste modelo? **Resolução:** 0,08/0,02=4. A razão entre incertezas padrão seria 2.
- Para a soma das mesmas entradas, com v₁=v₂=0,04 e C₁₂=0,03 cm², qual a variância, em cm²? **Resolução:** 0,04+0,04+2×0,03=0,14 cm².
- Para v₁=v₂=0,04 cm², qual o maior valor permitido de C₁₂, em cm²? **Resolução:** √(v₁v₂)=0,04 cm².
- Converta a covariância 0,03 cm² para mm². **Resolução:** 0,03×100=3 mm².
- Se v₁=v₂=0,04 e C₁₂=−0,04 cm², qual a variância da diferença, em cm²? **Resolução:** 0,04+0,04−2×(−0,04)=0,16 cm².

## Código, oráculo e fontes

Na raiz: `python3 -m unittest discover -s labs/medidas-indiretas -t .` e `python3 -m labs.medidas-indiretas.difference`. Só biblioteca padrão. Função aceita int/Fraction e valida v₁,v₂≥0 e C₁₂²≤v₁v₂. Posições podem ser assinadas; a saída é diferença orientada, não módulo de distância. Não escolhe covariância nem reconhece unidades automaticamente.

Oráculo sintético: B toma −0,3;0;+0,3 cm com probabilidades 1/6;4/6;1/6, enquanto E₁/E₂ tomam ±0,1 cm com probabilidades iguais. Var(B)=0,03 cm² e Var(Eᵢ)=0,01 cm². Os 12 átomos de B,E₁,E₂ geram C₁₂=0,03 e Var(L)=0,02. O segundo oráculo tem 36 átomos de B₁,B₂,E₁,E₂ independentes, preserva marginais, mas gera C₁₂=0 e Var(L)=0,08. Todos os pesos e momentos são racionais exatos.

Referência: [NIST TN1297 §5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty), consulta parcial reconfirmada em 22/10/2026; [Apêndice A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty), A.1–A.3 lido no bloco anterior em 22/10/2026, com nova abertura falhando neste bloco. Os exemplos e derivação linear são originais. Bibliografia nominal e programa efetivo da turma não foram reconferidos. Rascunho assistido por IA para revisão pessoal. Próxima revisão: refazer 0,02 por covariância e cancelamento; próximo conteúdo: sensibilidade em medida indireta não linear, com critério de validade da aproximação.

Verificação do bloco: cinco testes do laboratório aprovados, incluindo oráculos independentes por 12/36 átomos de distribuições finitas, limites da matriz de covariância e mudança de unidade. Treze testes de catálogo e 556 estruturas MathML aprovados. Navegador a 390 px: documento 375 px sem transbordamento, figura inspecionada, questão 5 rejeitou 0,08 e aceitou 1/50 cm²; console sem erros observados. Prévia covariancia-medidas-mobile.jpg. Catálogo 506 aulas/3231 exercícios; cobertura recalculada. Não houve revalidação da suíte global, leitura nova de livros da turma ou experiência real. Próxima revisão pessoal: derivar a identidade expandindo o quadrado, comparar modelos e conferir limites de covariância; próximo conteúdo: sensibilidade não linear. Saldo semanal confirmado após bloco: 90%; parada em 65%.
