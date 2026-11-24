# Lorentz e pares de eventos — notas de aula

Rascunho original para revisão de Jhuann, 22/10/2026.

## Coordenadas de eventos dependem do referencial

Um evento é uma ocorrência com lugar e instante definidos, como emissão de um pulso ou passagem por um marcador. S′ move-se em +x com velocidade v em relação a S; as origens e os relógios coincidem em t=t′=0. Eixos paralelos e sincronização de Einstein fixam a transformação padrão. Defina β=v/c e γ=1/√(1−β²), com |β|<1. Usamos ct e x na mesma unidade de comprimento: se x está em metros, ct também deve estar. As coordenadas temporais em segundos são obtidas dividindo ct por c.

ct′=γ(ct−βx); x′=γ(x−βct)

## O intervalo fornece uma conferência independente

Para comparar dois eventos A e B, forme Δct=c(tB−tA) e Δx=xB−xA. O intervalo com assinatura +− é s²=(Δct)²−(Δx)². A origem comum permite interpretar o painel como um evento comparado ao evento origem, mas num par geral devemos usar diferenças. Transladar ambos os eventos pelo mesmo deslocamento não muda suas diferenças. O intervalo é invariável; cada coordenada isolada não é.

s² invariável

## A teoria é especial e inercial

A transformação padrão liga referenciais inerciais em movimento uniforme e não modela gravidade ou buracos negros. A interpretação depende dos eventos e da convenção de velocidade.

|β|<1; referenciais inerciais

## O fator que normaliza a transformação

Para β=3/5, 1−β²=16/25 e γ=5/4. O fator é positivo e maior ou igual a um; β pode ser negativo, invertendo a direção do movimento, mas γ depende de β². Quando β=0, γ=1 e recuperamos as mesmas coordenadas. O sinal de β deve ser declarado antes de usar as equações; não se escolhe o sinal para obter o resultado desejado.

γ=1/√(1−β²)

## Provar a invariância por expansão

Aplique as mesmas fórmulas às diferenças dos eventos. Ao subtrair (Δx′)² de (Δct′)², os termos mistos −2βΔctΔx se cancelam. Sobram γ²(1−β²)[(Δct)²−(Δx)²]. Pela definição de γ, o fator inicial vale um. Assim a igualdade é exata na álgebra. Uma pequena diferença no painel vem do cálculo em ponto flutuante, não de uma violação física do intervalo.

s′²=γ²(1−β²)s²=s²

## Transformar um par temporal

Escolha eventos cuja separação seja Δct=5 e Δx=3, numa mesma unidade de comprimento. Com β=3/5 e γ=5/4: Δct′=(5/4)(5−9/5)=4 e Δx′=(5/4)(3−3)=0. O intervalo passa de 25−9=16 para 16−0=16. S′ é o referencial em que os dois eventos ocorrem no mesmo lugar. Um relógio inercial que percorre essa linha entre eles mede cΔτ=√16=4; em S o intervalo coordenado é cΔt=5. Não substitua Δt por tempo próprio sem identificar a trajetória.

(Δct,Δx)=(5,3) → (4,0)

## Classificar separações sem trocar os eventos

Se s²>0, a separação é temporal: é possível um referencial inercial em que Δx′=0. Se s²<0, é espacial: é possível um referencial em que Δct′=0. Para um par distinto com s²=0, a separação é de luz e satisfaz |Δx|=|Δct|. O par coincidente também tem s²=0, mas não representa um percurso luminoso entre eventos distintos. Estas classificações são preservadas pelo boost.

s²>0 temporal; s²<0 espacial; s²=0 nula

## A ordem temporal pode mudar para um par espacial

Considere Δct=1 e Δx=2: s²=−3. Com o mesmo β=3/5, Δct′=(5/4)(1−6/5)=−1/4 e Δx′=(5/4)(2−3/5)=7/4. B era posterior a A em S e é anterior em S′. Isso não inverte a ordem de causa e efeito: esse par espacial não admite sinal entre A e B com velocidade menor ou igual a c. A expressão descreve tempos coordenados, não a ordem em que uma câmera recebe imagens.

(1,2) → (−1/4,7/4); s²=−3

## Por que a ordem causal futura permanece

Para uma separação causal futura não nula, Δct>0 e |Δx|≤Δct. Então Δct−βΔx≥Δct−|β||Δx|≥(1−|β|)Δct>0. Como γ>0, Δct′ também é positivo para qualquer boost padrão com |β|<1. Essa desigualdade distingue o caso causal do exemplo espacial anterior. Não basta observar um tempo negativo isolado e concluir que toda ordem temporal seja relativa.



## Simultaneidade pertence ao par e ao referencial

Se Δct=0 e Δx≠0 em S, a transformação dá Δct′=−γβΔx, que em geral não é zero. Por exemplo, Δct=0 e Δx=2 com β=3/5 dão Δct′=−3/2 e Δx′=5/2. Os eventos continuam os mesmos. No sentido inverso, para um par espacial há β=Δct/Δx com módulo menor que um que o torna simultâneo. Para o par (3,5), esse valor é 3/5. A escolha de simultaneidade não é atraso de propagação visual.

Δct=0 ⇒ Δct′=−γβΔx

## Conferir a inversa sem mudar a convenção

Para retornar a S, troque β por −β e mantenha γ. As expressões passam a Δct=γ(Δct′+βΔx′) e Δx=γ(Δx′+βΔct′). Aplicá-las ao par espacial (−1/4,7/4) devolve (1,2). Essa conferência e a invariância testam aspectos diferentes: recuperar o par evita aceitar um cálculo que conserve o intervalo, mas use a transformação errada para a velocidade declarada.

Boost inverso: β → −β

## Como usar o painel existente

O painel usa coordenadas ct e x em relação à origem comum. Mantendo β=0,6, escolha ct=1 e x=2 para reproduzir o par espacial e o tempo ct′=−0,25. Os limites dos controles não incluem ct=5 do exemplo temporal maior; esse caso está no laboratório Python. A tabela usa ponto flutuante e não mostra tempo de observação por luz. A grandeza s² tem unidade de comprimento ao quadrado, não de tempo.



## Uma referência exata e seu domínio

O laboratório racional confere os mesmos pares com β=3/5, γ=5/4 e outros boosts de γ racional. Ele rejeita β como 1/2 apenas porque γ é irracional e não cabe em Fraction; isso não torna o referencial fisicamente inválido. O painel aceita valores gerais dentro de seus limites. A referência exata serve para testar álgebra, inversa, diferenças e classificação em casos escolhidos. Não descreve aceleração, gravidade, geometria de buracos negros ou todos os relógios possíveis entre dois eventos.



## Exercícios e resoluções

- No exemplo original c=1, β=0,6 e evento (t=2,x=0), qual é t′? **Resolução:** γt=2,5.
- Esta transformação sozinha descreve gravidade de buraco negro? **Resolução:** É relatividade especial entre referenciais inerciais.
- Para β=3/5, quanto é γ? **Resolução:** 1/√(1−9/25)=5/4.
- No par (Δct,Δx)=(5,3), com β=3/5, quanto é Δct′? **Resolução:** (5/4)(5−9/5)=4.
- No mesmo par temporal, quanto é Δx′? **Resolução:** (5/4)(3−3)=0.
- Qual é s² do par (Δct,Δx)=(5,3)? **Resolução:** 5²−3²=25−9=16.
- No par (Δct,Δx)=(1,2), com β=3/5, quanto é Δct′? **Resolução:** (5/4)(1−6/5)=−1/4.
- No mesmo par espacial, quanto é Δx′? **Resolução:** (5/4)(2−3/5)=7/4.
- Para eventos simultâneos em S com Δx=2, β=3/5, quanto é Δct′? **Resolução:** −γβΔx=−(5/4)(3/5)2=−3/2.
- Um boost padrão com |β|<1 pode inverter a ordem de uma separação causal futura não nula? **Resolução:** A desigualdade Δct−βΔx>0 preserva o sinal futuro.
- O intervalo zero do par coincidente comprova uma viagem de luz entre dois eventos distintos? **Resolução:** A origem repetida é o mesmo evento, não dois eventos distintos ligados por luz.
- O laboratório exato rejeita β=1/2. Isso o torna um referencial inercial fisicamente proibido? **Resolução:** É limitação da representação racional de γ; |β|<1 continua satisfeito.

## Fontes e reprodução

Nussenzveig, Curso de Física Básica 4, exemplar privado previamente identificado, §6.4 pp.155–158/PDF156–159, leitura parcial em 22/10/2026. A extração emitiu avisos de fluxos do PDF e omitiu símbolos; a página impressa 158/PDF159 foi renderizada e inspecionada visualmente para γ e a transformação final. Não se afirma leitura integral da dedução ou de todas as páginas visualmente. Feynman I §15–2: https://www.feynmanlectures.caltech.edu/I_15.html, consulta pública parcial. Não se usou a discussão histórica de massa da fonte na aula. Assinatura temporal positiva, exemplos e demonstrações explícitas originais. Programa e histórico não reconsultados neste bloco; sem nova reivindicação de cobertura curricular integral.

Na raiz do site: python3 -m labs.lorentz-pares.experiment; python3 -m unittest discover -s labs/lorentz-pares -t . . Só biblioteca padrão. Aceita int/Fraction e exige γ racional por verificação de quadrados inteiros. β=1/2 é fisicamente permitido e apenas não representado pelo módulo exato; use a fórmula geral ou o painel existente em ponto flutuante. Não há promessa de aritmética exata para todos os boosts. O painel permite ct até 3; o par (5,3) é reproduzido no laboratório.

Próxima revisão pessoal: comparar os três tipos de par, reconstruir a inversa e explicar por que o exemplo espacial não é uma inversão causal. Derivação completa a partir dos postulados, geometrias gerais e trajetórias aceleradas permanecem pendentes.

Conferência no navegador: controles por teclado reproduziram ct=1,x=2,β=0,6, com ct′=−0,25,x′=1,75 e intervalo −3 nos dois referenciais. Exercício aceitou −1/4. Tabela carregada e inspecionada a 390 px, sem transbordamento horizontal observado. Prévia lorentz-pares-mobile.jpg. Catálogo: 498 aulas/2924 exercícios em rascunho. Saldo semanal: 94%; parada operacional: 65%.
