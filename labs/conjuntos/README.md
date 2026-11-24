# Conjuntos: linguagem para funções e domínios

Material original em rascunho — 16/10/2026. Referência de escopo: CCM0113, programa consultado em 16/10, ativado em 15/07/2024; versão da turma de 2023 não recuperada. https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0113

## Elementos e subconjuntos são relações diferentes

x∈A significa que x é um elemento de A. A⊆B significa que todo elemento de A também está em B. Para A={1,2}, temos 1∈A e {1}⊆A. A escrita {1}∈A não vale nesse exemplo: os elementos listados são números, não o conjunto {1}. Declare que tipos de objetos estão em cada conjunto.

## O conjunto vazio também é subconjunto

O vazio ∅ não tem elementos. Para todo A, ∅⊆A: não há elemento do vazio que possa violar a condição de pertencer a A. Já ∅∈A depende de A. O conjunto {∅} tem um elemento e é diferente de ∅. Essa distinção aparece ao construir famílias de conjuntos e espaços de possibilidades.

## Igualdade exige as duas inclusões

Para provar A=B, mostre A⊆B e B⊆A. Alternativamente, mostre para um elemento arbitrário x que x∈A se e somente se x∈B. Uma lista de exemplos que coincidem não prova igualdade de conjuntos infinitos; é necessário um argumento para todo elemento relevante.

## União, interseção e diferença traduzem conectivos

x∈A∪B significa x∈A ou x∈B, com ou inclusivo. x∈A∩B exige as duas condições. x∈A\B exige x∈A e x∉B. A diferença não é comutativa: se A={1,3} e B={2,3}, A\B={1}, mas B\A={2}. Elementos repetidos não são contados novamente.

## Complemento depende do universo declarado

Fixado U com A⊆U, o complemento de A é U\A. Mudar U muda o complemento. No experimento U={1,2,3,4}; o complemento de {1,3} é {2,4}. Em ℝ, o complemento do mesmo conjunto contém infinitos outros reais. Não conclua uma afirmação sobre ℝ olhando apenas o universo finito.

## Uma identidade pode ser provada por pertinência

Para De Morgan, x∈U\(A∪B) equivale a x∈U e x não pertencer nem a A nem a B. Isso equivale a pertencer simultaneamente a U\A e U\B, logo U\(A∪B)=(U\A)∩(U\B). O argumento vale para todo x de U; a verificação computacional de 256 pares finitos é apenas uma conferência dos exemplos.

## Intervalos organizam restrições contínuas

[a;b] inclui as duas extremidades; (a;b) não inclui nenhuma; [a;b) inclui somente a. Por exemplo, [−1;2)∩(0;3]=(0;2). Um intervalo até +∞ ou −∞ nunca inclui infinito como número real. Resolva domínio de funções combinando restrições por interseção, não por união quando todas precisam valer.

## Domínio, contradomínio e imagem têm papéis próprios

Uma função f:D→C atribui a cada x de D exatamente um valor em C. A imagem f(D) contém os valores efetivamente atingidos e pode ser menor que C. Para f:ℝ→ℝ, f(x)=x², a imagem é [0;+∞). Para S⊆D, f(S) é a imagem do subconjunto; elementos de S diferentes podem produzir o mesmo valor.

## Pré-imagem não exige uma função inversa

Para T⊆C, f⁻¹(T)={x∈D:f(x)∈T}. Essa notação é de conjunto e vale mesmo sem inversibilidade. Para x² em ℝ, a pré-imagem de {1} é {−1,1}. Pré-imagem de interseção é interseção das pré-imagens, pois exigir f(x) em ambos os conjuntos equivale a exigir x em ambas as pré-imagens.

## Quantificadores indicam o alcance da afirmação

A⊆B é uma afirmação universal: para todo x, x∈A implica x∈B. Para refutá-la, basta um contraexemplo x∈A com x∉B. A não inclusão não significa que A e B sejam disjuntos. Para A={1,3} e B={2,3}, A não é subconjunto de B e a interseção contém 3.

## Conjuntos finitos conectam matemática e programação

No Python, set e frozenset representam conjuntos finitos de objetos adequados, sem repetição. No experimento, códigos de 0 a 15 selecionam subconjuntos de quatro números: pesos 1,2,4,8 correspondem a incluir 1,2,3,4. Código 5=1+4 escolhe {1,3}. O código 0 escolhe ∅. São representações computacionais finitas, não um algoritmo para enumerar todos os reais.

## Exemplo resolvido

Para A={1,3}, B={2,3} e U={1,2,3,4}, calcule união, interseção, diferença e complemento de A.

A união reúne os elementos de pelo menos um conjunto: {1,2,3}.

A interseção exige as duas pertenças: {3}.

A diferença A\B remove de A os elementos de B: {1}.

O complemento em U é U\A={2,4}.

A não é subconjunto de B: 1 pertence a A e não a B. A interseção não é vazia, apesar disso.

## Exercícios e resoluções

### Quantos elementos há em {1,3}∪{2,3}?

A união é {1,2,3}.

### Quantos elementos há em {1,3}∩{2,3}?

A interseção é {3}.

### Quantos subconjuntos tem {1,2}?

∅, {1}, {2}, {1,2}.

### Quantos elementos há em {∅}?

O único elemento é o conjunto vazio.

### Quantos reais estão na pré-imagem de {1} pela função x²?

Os números −1 e 1 têm quadrado 1.

### O vazio é subconjunto de qualquer conjunto?

Nenhum elemento do vazio viola a condição universal.

### A\B é sempre igual a B\A?

Com A={1,3}, B={2,3}, as diferenças são {1} e {2}.

### A não ser subconjunto de B implica interseção vazia?

Os conjuntos do exemplo compartilham 3.

### A pré-imagem f⁻¹(T) só existe quando f tem uma função inversa?

Ela é definida pela condição f(x)∈T, independentemente de inversibilidade.

## Preparação manuscrita

Explique ∈ versus ⊆; construa as operações com elementos; prove De Morgan sem depender do desenho; faça uma interseção de intervalos; use x² para imagem e pré-imagem. Peça um contraexemplo à ideia de que não inclusão implica disjunção.

## Limites e próximos assuntos

Ainda faltam relações, produto cartesiano e mais exercícios de demonstração. Reais, indução e outros fundamentos terão aulas próprias. Nenhuma equivalência curricular ou domínio individual está certificado.
