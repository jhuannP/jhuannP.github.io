# Campo octaédrico d⁶: ocupação, energia e pareamento

22/10/2026. Notas de aula originais em rascunho para revisão de Jhuann. Pré-requisitos: orbitais d, Pauli/Hund, elétrons de valência e álgebra básica. Não são dados de um complexo real nem comprovação de domínio pessoal.

## A geometria é uma hipótese do problema

Escolhemos um centro d⁶ em geometria octaédrica ideal: seis ligantes nas direções ±x,±y,±z. d⁶ significa seis elétrons no conjunto de cinco orbitais d considerado, não carga +6. Aqui não deduzimos a geometria a partir de um metal ou ligante real. O recorte começa com a geometria e parâmetros de energia fornecidos; Jahn–Teller, covalência, vibrações e mudança de geometria não são calculados.



## Os cinco orbitais se separam em dois conjuntos

No modelo octaédrico, d_xy,d_xz,d_yz formam t₂g e d_z²,d_x²−y² formam e_g. O primeiro conjunto tem três orbitais; o segundo, dois. O campo cristalino ideal coloca t₂g abaixo de e_g. As formas espaciais ajudam a interpretar a diferença, mas não calculamos aqui uma interação eletrostática completa. Em uma descrição por orbitais moleculares o caráter ligante/antiligante e a composição dos orbitais exigem outro modelo; este recorte não é a teoria de campo ligante completa.



## Defina Δ e a referência de energia antes de somar

Sejam a energia de cada orbital inferior e b a de cada superior, ambas relativas ao baricentro escolhido. Defina Δ=b−a>0 e imponha 3a+2b=0. Substituindo b=a+Δ, obtemos 5a+2Δ=0, portanto a=−2Δ/5 e b=3Δ/5. Os números são energias relativas: não afirmam que a energia total metal–ligante ou de ligação seja zero.

3(−2Δ/5)+2(3Δ/5)=0

## Conte elétrons, pares e orbitais simples

Cada orbital espacial admite zero, um ou dois elétrons; no caso de dois, os spins são opostos. Para a contagem d⁶, uma ocupação usual de spin alto é t₂g⁴e_g²: um par e quatro orbitais simples. A ocupação usual de spin baixo t₂g⁶e_g⁰ tem três pares e nenhum orbital simples. A figura usa a convenção usual de Hund para ilustrar esses casos. Contar orbitais simples não é resolver todos os estados de spin do íon.



## Escolha explicitamente o custo de pareamento

O laboratório adota E=Σᵢnᵢεᵢ+PN_par, com P≥0 um custo constante por orbital duplamente ocupado. Todos os termos usam a mesma unidade de energia. É um modelo reduzido definido nesta aula. A discussão do livro distingue repulsão coulombiana e troca; nosso P não calcula separadamente essas contribuições, termos espectroscópicos, parâmetros de Racah ou acoplamento spin–órbita. Ele permite comparar ocupações sob hipóteses dadas, não determinar todo o estado eletrônico real.

E_modelo=E_campo+P N_par

## Some campo e pareamento nas duas ocupações usuais

Para t₂g⁴e_g², a contribuição do campo é 4(−2Δ/5)+2(3Δ/5)=−2Δ/5; há um par. Para t₂g⁶e_g⁰, a contribuição é 6(−2Δ/5)=−12Δ/5; há três pares. Baixar elétrons para t₂g ganha energia de campo, mas forma dois pares a mais. Comparar só a contribuição de campo apagaria o custo que o modelo decidiu incluir.

E_alto=−2Δ/5+P; E_baixo=−12Δ/5+3P

## Derive a diferença em vez de decorar a desigualdade

Subtraia a energia da ocupação usual alta da baixa: E_baixo−E_alto=−2Δ+2P=2(P−Δ). Neste modelo, se Δ>P a diferença é negativa e a ocupação baixa custa menos. Se Δ<P, a alta custa menos. A igualdade Δ=P é um caso de empate do modelo reduzido, não uma previsão de transição em uma substância real ou de proporção entre estados.

E_baixo−E_alto=2(P−Δ)

## Confronte números com a conta simbólica

Use unidades de energia arbitrárias coerentes. Com Δ=10 e P=12, a ocupação alta tem E=−4+12=8 e a baixa E=−24+36=12. Com Δ=20 mantendo P=12, a alta tem E=−8+12=4 e a baixa E=−48+36=−12. Energia negativa aqui depende da referência relativa; não significa energia de ligação medida, instabilidade ou emissão espontânea de um fóton. O sinal da diferença é que responde à comparação feita.



## Enumere ocupações sem chamá-las de microestados completos

O Python enumera os 45 padrões (n₁,…,n₅) com nᵢ∈{0,1,2} e soma seis. Os três primeiros orbitais são t₂g; os dois últimos, e_g. Para cada padrão calcula campo, pares, orbitais simples e energia do modelo. Esses padrões não enumeram orientações de todos os spins nem resolvem S ou sua multiplicidade. Permutações de rótulos dentro de um conjunto degenerado preservam a energia deste modelo. O programa não usa a contagem de padrões para calcular populações.



## O caso de empate revela o limite da aproximação

Além das ocupações usuais alta e baixa, há padrões t₂g⁵e_g¹, com dois pares e dois orbitais simples, cuja energia é −7Δ/5+2P. Eles ficam entre as duas energias anteriores e empatam com ambas quando Δ=P. A enumeração encontra três categorias orbitais nesse ponto. Fora dele essa categoria não é mínimo do modelo. Isso não é previsão de spin intermediário real: faltam as interações e os estados que o custo constante P não resolve.

Em Δ=P: E_alto=E_intermediário=E_baixo=3P/5

## O que podemos dizer sobre magnetismo ainda é limitado

As ocupações usuais comparadas têm quatro ou zero elétrons desemparelhados na representação de Hund. Isso é uma primeira relação entre ocupação e magnetismo. Não calculamos suscetibilidade, momento magnético, contribuição orbital, dependência térmica ou interações entre centros. O código conta orbitais simples, sem determinar acoplamentos de spin. O grupo mais amplo de propriedades magnéticas continua em lacuna no mapa, com esta aula apenas como apoio.



## O desdobramento não é um espectro eletrônico completo

Um Δ fornecido não fornece sozinho intensidades, regras de seleção ou todas as transições de um sistema multieletrônico d⁶. Também não produz diagramas de Tanabe–Sugano, transferência de carga ou uma série espectroquímica. A soma de energias de ocupação não é automaticamente a energia de um fóton observado. Estados eletrônicos e momento de transição precisam ser tratados antes de interpretar espectros reais.



## O teste verifica a hipótese matemática declarada

As energias são frações exatas. Os testes comparam os padrões orbitais com outra enumeração, de dez posições binárias de spin–orbital contendo seis elétrons, agrupando depois por orbital espacial. Isso confere capacidades e contagens, mas não adiciona um Hamiltoniano de spin ao modelo. Testes também conferem o baricentro, o cruzamento, escala de energia e permutações dentro de t₂g/e_g. Nenhum cálculo eletrônico, pacote químico ou dado medido foi usado.



## O que este recorte abre no programa

O item 8 de CCM0214 passa a ter um primeiro apoio para desdobramento e estabilização em octaedro ideal. Ele continua parcial: faltam campo ligante por orbitais moleculares, distorções, outras geometrias e Jahn–Teller. O item de estrutura eletrônica com Russell–Saunders e Racah não foi substituído por esta contagem. Aulas, notas e competências pessoais continuam por revisar; o livro é referência de preparação, não prova de domínio de Jhuann.



## Exercícios e resoluções

1. Quantos orbitais espaciais existem no conjunto t₂g octaédrico?

   Resolução: t₂g tem três orbitais; e_g tem dois.

2. Qual é E_campo/Δ para a ocupação t₂g⁶e_g⁰?

   Resolução: Seis elétrons a −2Δ/5: −12Δ/5.

3. Qual é E_campo/Δ para t₂g⁴e_g²?

   Resolução: 4(−2/5)+2(3/5)=−2/5.

4. Quantos pares há na ocupação usual t₂g⁴e_g² de spin alto?

   Resolução: Um orbital é duplamente ocupado e quatro são simples.

5. Quantos pares há em t₂g⁶e_g⁰?

   Resolução: Cada um dos três orbitais t₂g tem dois elétrons.

6. Com Δ=10 e P=12, qual a energia total da ocupação alta no modelo?

   Resolução: −(2/5)10+12=8.

7. Com Δ=20 e P=12, qual a energia total da ocupação baixa no modelo?

   Resolução: −(12/5)20+3×12=−12.

8. Com Δ=10 e P=12, quanto é E_baixo−E_alto?

   Resolução: 2(P−Δ)=2(12−10)=4.

9. Em Δ=P, o empate desta função de energia prova uma transição física real?

   Resolução: Ele é uma consequência do modelo reduzido; não inclui todos os estados e contribuições reais.

10. Os 45 padrões orbitais são todos os estados de spin resolvidos do íon?

   Resolução: A ocupação não especifica todos os spins nem resolve seu acoplamento.

11. Conhecer só Δ e P determina intensidades de um espectro eletrônico?

   Resolução: Faltam estados, momento de transição, regras de seleção e outros dados.

12. Qual a contribuição de campo, dividida por Δ, para t₂g⁶e_g⁴ (d¹⁰)?

   Resolução: 6(−2/5)+4(3/5)=0, pela referência do baricentro.

## Fontes e crítica da leitura

Miessler, Fischer e Tarr, Química Inorgânica, 5ª ed., Pearson 2014, §§10.3.2–10.3.3, pp.363–366 (PDF378–381), consulta parcial no exemplar autorizado em 22/10/2026. A p.365/PDF380 foi inspecionada visualmente. As páginas distinguem repulsão e troca e apresentam a comparação de desdobramento/pareamento como aproximação, não determinante universal do estado real.

Na segunda afirmação de p.365 para Δ<P, a edição consultada repete a expressão “spin baixo”, em aparente conflito com o resumo de p.363 e com a comparação de energias. Registramos a observação de leitura, sem apresentá-la como errata publicada nem alterar o PDF. Nesta aula a desigualdade é derivada da função de energia explicitamente escolhida. Não se copia essa conclusão isolada.

[CCM0214 no Júpiter](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214), conteúdo recuperado pela ferramenta web em 22/10/2026, com rastreamento indicado há dois meses e ativação 15/07/2024. Item 8: campo ligante, desdobramento, estabilização e Jahn–Teller. Este recorte abre somente parte do item; a versão efetivamente ministrada continua não comprovada.

Diagrama, código, parâmetros, exercícios e desenvolvimento matemático próprios. Nenhum PDF privado, figura, tabela ou questão do livro foi distribuído. O custo P por par é uma simplificação; não reproduz a análise microscópica completa de troca da fonte. Em especial, os mínimos em Δ=P não predizem spin intermediário, transição ou população real.

## Reprodução

Na raiz do site, execute python3 -m labs.campo-octaedrico-d6.experiment e python3 -m unittest discover -s labs/campo-octaedrico-d6 -t .

Ordem dos orbitais no código: três t₂g seguidos de dois e_g. Entradas são int/Fraction; Δ>0 e P≥0. state pode auditar qualquer ocupação com até dois elétrons por orbital; d6_states e minima restringem a soma a seis. A enumeração de dez spin-orbitais nos testes verifica os padrões permitidos, sem resolver seus acoplamentos ou usar a contagem como peso estatístico.

O código não calcula Δ a partir de ligantes, não executa química quântica e não estima intensidades, magnetismo ou estrutura real. O caso de empate ilustra a insuficiência do modelo para resolver todas essas perguntas.

## Verificação de 22/10/2026

Cinco testes novos aprovados, incluindo duas enumerações e 156 pares de parâmetros. Suíte completa: 849 testes Python; 494 estruturas MathML aprovadas. No navegador, respostas −12/5 e −12 aceitas, etapa aberta por teclado e figura inspecionada em 390 px sem transbordamento horizontal ou erros de console observados. Revisão de Jhuann pendente.
