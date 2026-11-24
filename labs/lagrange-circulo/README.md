# Lagrange no círculo — notas de aula

Rascunho para revisão de Jhuann, 22/10/2026.

## O domínio permitido muda o problema

Queremos extremizar f somente nos pontos que satisfazem g=c. Direções que saem desse conjunto não são variações permitidas. Em um ponto regular de uma curva de nível no plano, a tangente é perpendicular a ∇g. No extremo sobre a curva, a derivada de f em cada direção tangente deve ser zero. Isso leva ao paralelismo entre os gradientes, sem exigir que ∇f seja diferente de zero.

∇f=λ∇g; g=c

## Um círculo dá dois extremos

Para f=x+y e g=x²+y²=1, (1,1)=λ(2x,2y), então x=y. A restrição dá x=y=±1/√2 e os valores ±√2.

máximo √2; mínimo −√2

## Hipóteses e outros candidatos continuam necessários

A condição ∇g≠0 no candidato garante a regularidade usada. Suponha f e g de classe C¹ em uma vizinhança aberta. Resolver ∇f=λ∇g junto de g=c fornece candidatos regulares, não a classificação. Extremos globais, fronteiras, pontos singulares e restrições adicionais pedem análise própria; não se ignora o domínio ao montar o sistema.

Lagrange não elimina verificação do domínio

## A regra da cadeia explica o multiplicador

Se uma curva regular r(s) permanece na restrição e passa pelo candidato, g(r(s))=c é constante. Portanto ∇g·r′=0. No extremo de f∘r, a regra da cadeia também dá ∇f·r′=0. No plano, o espaço normal à tangente é uma reta; como ∇g≠0, existe λ com ∇f=λ∇g. A regularidade local garante as direções tangentes necessárias. Esse argumento mostra a necessidade no extremo, não que todo paralelismo produza um extremo.

(f∘r)′=∇f·r′=0

## Escolher uma convenção e manter a restrição

Defina h=g−c e a função auxiliar ℒ=f−λh. Derivar ℒ em x e y produz ∇f−λ∇h=0; derivar em λ devolve −h=0. A equação da restrição continua parte do sistema: o multiplicador não a substitui. Se escolher ℒ=f+λh, o sinal de λ muda, mas os pontos físicos são os mesmos. Nesta aula usamos o sinal menos.

ℒ(x,y,λ)=f(x,y)−λ[g(x,y)−c]

## Exemplo: uma direção de preferência no círculo

Maximize e minimize f=3x+4y sobre x²+y²=4. Todos os números deste exemplo são adimensionais. A restrição é um círculo de raio 2, e seu gradiente (2x,2y) nunca zera nele. O sistema é 3=2λx, 4=2λy e x²+y²=4. Aqui λ não pode ser zero, pois o gradiente do objetivo é (3,4). Substituindo x=3/(2λ) e y=4/(2λ) na restrição, obtemos 25/(4λ²)=4, logo λ=±5/4.

λ=±5/4; (x,y)=±(6/5,8/5)

## Classificar exige um argumento

Nos dois candidatos, f vale 10 e −10. O círculo é fechado e limitado, portanto compacto; f é contínua e atinge máximo e mínimo. Como a restrição é regular em todos os pontos e encontramos todos os candidatos, comparar esses dois valores resolve os extremos globais. Essa conclusão usa existência, regularidade e exaustão dos candidatos; ela não vem apenas de escolher o maior número de uma lista incompleta.

máximo 10; mínimo −10

## Uma prova global independente

A desigualdade de Cauchy–Schwarz dá |3x+4y|≤√(3²+4²)√(x²+y²)=5×2=10. A igualdade ocorre quando (x,y) é paralelo a (3,4). Os pontos ±(6/5,8/5) pertencem ao círculo e atingem ±10. Assim o limite global e seus pontos de igualdade conferem o sistema de Lagrange sem depender de uma amostragem do círculo.

|3x+4y|≤5×2=10

## Parametrização confere os candidatos

Escreva x=2 cosθ e y=2 senθ. O objetivo vira F(θ)=6 cosθ+8 senθ; sua derivada é −6 senθ+8 cosθ. No máximo, cosθ=3/5 e senθ=4/5 tornam a derivada nula e dão F=10. O ponto oposto dá o mínimo. Essa redução a uma variável confirma a tangência. Varredura numérica de ângulos pode localizar candidatos, mas não substitui a prova global.

F′(θ)=−6 senθ+8 cosθ

## O valor de λ depende de como escrevemos a condição

A mesma circunferência pode ser escrita como h=x²+y²−4=0 ou 3h=0. O gradiente da segunda expressão é três vezes maior. Para manter ∇f=λ∇h, seu multiplicador é dividido por três. No máximo do exemplo, λ=5/4 vira 5/12. A posição e o valor extremo permanecem iguais. Uma interpretação de λ como sensibilidade exige especificar o parâmetro e a escala da condição; seu número isolado não é uma propriedade geométrica invariável.

h↦αh ⇒ λ↦λ/α, α≠0

## Um ponto estacionário pode não ser extremo

Considere f=x³ no círculo unitário. Em (0,1), ∇f=(0,0), de modo que o sistema de Lagrange vale com λ=0; a restrição é regular, pois ∇g=(0,2). Porém pontos próximos da curva com x positivo dão f>0, e com x negativo dão f<0. O candidato não é máximo nem mínimo local. Gradiente zero é permitido no teorema, mas não fornece classificação.



## Quando a regularidade falha

Minimize f=x sobre x²+y²=0. O conjunto permitido contém apenas (0,0), que é simultaneamente máximo e mínimo relativos ao conjunto. Ali ∇g=(0,0), enquanto ∇f=(1,0); não existe λ com ∇f=λ∇g. O sistema sem solução não prova que o problema não tenha extremo: a hipótese do teorema falhou. Também não há tangente regular de uma curva nesse conjunto reduzido a um ponto.



## Uma família resolvida e seus limites

O laboratório trata f=px+qy no círculo de raio R≥0. Para R>0 e (p,q)≠(0,0), os extremos são ±R√(p²+q²), nos pontos ±R(p,q)/√(p²+q²). Se p=q=0, todos os pontos têm valor zero; não há só dois candidatos distintos. Se R=0, há apenas a origem e a restrição é singular. O código distingue esses casos e testa a reescala da restrição. Não é um resolvedor geral de funções, elipses, desigualdades ou condições KKT.

(x,y)₊=R(p,q)/√(p²+q²)

## Exercícios e resoluções

- No exemplo original f=x+y sobre x²+y²=1, o sistema dá x=y. Quanto vale x² nesse candidato? **Resolução:** 2x²=1.
- Resolver Lagrange sozinho classifica todos os candidatos como máximos? **Resolução:** É preciso comparar e analisar condições.
- No exemplo f=3x+4y sobre x²+y²=4, qual é a coordenada x do máximo? **Resolução:** O máximo está em (6/5,8/5).
- No mesmo exemplo, qual é a coordenada y do máximo? **Resolução:** O vetor (3,4), de norma 5, é normalizado e multiplicado por 2.
- Qual é o valor máximo do mesmo objetivo? **Resolução:** 3×6/5+4×8/5=50/5=10.
- Qual é o valor mínimo do mesmo objetivo? **Resolução:** O ponto oposto produz −10.
- Na convenção ℒ=f−λ(x²+y²−4), qual é λ no máximo? **Resolução:** 3=2λ(6/5) fornece λ=5/4.
- Se a restrição for escrita como 3(x²+y²−4)=0, qual será λ no máximo, usando ℒ=f−λh? **Resolução:** O gradiente da restrição triplica; o multiplicador divide por três.
- Para f=3x+4y no círculo de raio 3, qual é o máximo? **Resolução:** R√(p²+q²)=3×5=15.
- Sobre x²+y²=0, o sistema de Lagrange sem solução para f=x prova ausência de extremos? **Resolução:** A origem é o único ponto permitido, e ∇g=0 ali: a hipótese de regularidade falha.
- O candidato (0,1) de f=x³ no círculo unitário é extremo local? **Resolução:** Pontos próximos com x de sinais opostos produzem valores acima e abaixo de zero.
- Se p=q=0 e R>0, quantos pontos do círculo extremizam f=px+qy? **Resolução:** O objetivo é constante e igual a zero.

## Fontes e reprodução

Apostol, Cálculo II, exemplar português privado, §9.14, pp.353–356 (PDF367–370), leitura textual parcial do método, geometria e regularidade. Não se afirma leitura integral de capítulos ou versão da turma. Referência pública parcial: OpenStax Calculus Volume 3, §4.8, teorema 4.20 e demonstração de uma restrição: https://openstax.org/books/calculus-volume-3/pages/4-8-lagrange-multipliers . Exemplos e diagramas das obras não foram copiados; os exemplos numéricos e contraexemplos desta aula são próprios.

Execute na raiz do site: python3 -m labs.lagrange-circulo.experiment; python3 -m unittest discover -s labs/lagrange-circulo -t . . O módulo recebe int/float finitos, sem bool, e retorna cálculos em ponto flutuante. Pode rejeitar escalas cujo resultado não é representável. Casos constantes retornam all_points=True e nenhum par isolado; R=0 retorna a origem e regular=False. Não é algoritmo de otimização geral.

A Cauchy–Schwarz prova os limites globais desta família. A varredura angular dos testes apenas detecta erros de implementação em casos finitos; não é a prova. Reescala de h divide λ pela mesma constante, sem mudar os pontos. O caso f=x³ exemplifica candidato regular sem extremo; o caso do conjunto reduzido à origem mostra por que singularidades exigem análise separada.

Próxima revisão pessoal: resolver o exemplo 3x+4y sem olhar, justificar existência e comparar com a desigualdade. Desigualdades/KKT e teste de segunda ordem restrito seguem pendentes.

Conferência no navegador: exercício de reescala aceitou 5/12; diagrama de tangência carregado e inspecionado a 390 px, sem transbordamento horizontal observado. Prévia lagrange-circulo-mobile.jpg. Catálogo: 498 aulas/2894 exercícios em rascunho. Nenhum modelo JS alterado; suíte global não repetida. Saldo semanal após o bloco: 95%; parada operacional 65%.
