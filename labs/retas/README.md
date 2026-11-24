# Retas no espaço: ponto, direção e pertencimento

Material original em rascunho — 16/10/2026. Escopo: CCM0123, programa consultado em 16/10/2026, ativação 01/01/2025. Versão da turma de 2024/1 não recuperada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123

## Um ponto e uma direção descrevem uma reta

Em ℝ³, escolha um ponto P=(p₁,p₂,p₃) e um vetor não nulo v=(v₁,v₂,v₃). A reta é o conjunto dos pontos r(t)=P+t v para t∈ℝ. P fixa uma posição de apoio e v fixa uma direção. Não confunda o ponto com o vetor: P muda sob translação da origem, enquanto a diferença entre dois pontos define um deslocamento.

r(t)=P+t v, v≠0

## O parâmetro precisa servir às três coordenadas

A forma paramétrica é x=p₁+t v₁, y=p₂+t v₂, z=p₃+t v₃, com o mesmo t em todas. Para P=(1,2,−1), v=(2,−1,2), t=2 gera (5,0,3). Escolher valores independentes de t para cada coordenada produz pontos que podem não estar na reta.



## Pertencimento é uma condição, não uma impressão visual

Para testar R, resolva R−P=t v. Escolha uma coordenada de v não nula para obter um candidato t e confira as três equações. Se qualquer uma falhar, R não pertence. Para R=(5,0,4), a primeira equação dá t=2, a segunda confere, mas a terceira exigiria z=3: esse ponto está fora.



## Componentes nulas pedem equações, não divisão por zero

Se v₁=0, a condição correspondente é x=p₁, sem determinar t. Use outra componente não nula. Para v=(0,0,1), a reta por (1,2,−1) exige x=1, y=2 e permite qualquer z. A escrita simétrica (x−p₁)/v₁=(y−p₂)/v₂=(z−p₃)/v₃ só pode usar denominadores não nulos; mantenha as demais condições separadas.



## Direção zero é uma degeneração da descrição

Se v=(0,0,0), P+t v é sempre P. A imagem é um único ponto, não uma reta. O laboratório rejeita esse caso nas operações de reta e a demonstração o identifica explicitamente. A ausência de uma direção válida não deve gerar uma divisão por zero ou uma conclusão automática de pertencimento.



## Dois pontos distintos fornecem a direção

Dados A e B distintos, use P=A e v=B−A. Então r(0)=A e r(1)=B. Para A=(1,2,−1), B=(5,0,3), a direção é (4,−2,4). Se A=B, a diferença é zero e os dados não selecionam uma reta única. Existem infinitas retas que passam por um ponto.



## Escalar a direção muda o parâmetro, não a reta

Substituir v por λv com λ≠0 preserva o conjunto: P+s(λv)=P+t v quando s=t/λ. Para λ negativo, a orientação do parâmetro se inverte. Escolher outro ponto de apoio P′=P+t₀v na mesma reta também preserva o conjunto, com novo parâmetro s=t−t₀.



## Reta, semirreta e segmento têm domínios diferentes

A mesma expressão A+t(B−A) descreve a reta para t∈ℝ, o segmento de A até B para 0≤t≤1 e uma semirreta a partir de A em direção a B para t≥0. Valores fora de [0;1] continuam na reta, mas não no segmento. O domínio do parâmetro faz parte da definição do objeto.



## Parâmetro não é automaticamente tempo

A curva r(t)=P+t v tem derivada vetorial v, calculada componente a componente. Se t for tempo em segundos e as posições estiverem em metros, v é velocidade em m/s e a rapidez é ||v||. Para v=(2,−1,2), a norma é 3. Se t for apenas parâmetro geométrico, não atribua a ele uma unidade física sem definir o modelo.



## Uma projeção plana pode esconder informação

Projetar (x,y,z) no plano xy descarta z. Os pontos (5,0,3) e (5,0,4) têm a mesma projeção, mas só o primeiro está na reta do exemplo. Uma reta vertical paralela ao eixo z projeta-se num único ponto. Por isso a demonstração combina projeção xy com tabela das três coordenadas e teste de pertencimento.



## Exato e aproximado exigem critérios distintos

O laboratório usa frações para testar igualdade exata e direção não nula. Com dados medidos ou ponto flutuante, um teste de proximidade exigiria escala, unidade e tolerância declaradas. Não adicione uma tolerância arbitrária para esconder inconsistências. Esta aula não desenvolve a distância de ponto a reta, posições relativas de duas retas nem planos; esses são próximos blocos.



## Exemplo resolvido

Para r(t)=(1,2,−1)+t(2,−1,2), verifique se R=(5,0,3) e Q=(5,0,4) pertencem à reta.

A primeira coordenada exige 5=1+2t, portanto t=2.

A segunda exige 0=2−t e confere em t=2.

Para R, a terceira é 3=−1+2×2: confere. Logo R pertence.

Para Q, seria necessário 4=3: falha. Q não pertence.

R e Q têm a mesma projeção xy, mostrando por que é preciso conferir z.

## Exercícios e resoluções

### Na reta do exemplo, qual t gera R=(5,0,3)?

5=1+2t dá t=2, que também satisfaz as outras coordenadas.

### Na reta do exemplo, qual z para t=2?

z=−1+2×2=3.

### Qual a norma do vetor (2,−1,2)?

√(4+1+4)=3.

### Na parametrização A+t(B−A), qual t gera B?

A+(B−A)=B.

### Se v for substituído por 2v, qual novo parâmetro corresponde ao antigo t=2?

s=t/2=1.

### O vetor diretor nulo define uma reta única?

A expressão fica constante e sua imagem é só um ponto.

### Conferir somente x e y garante pertencimento em ℝ³?

Dois pontos com o mesmo x,y podem ter z distintos.

### O parâmetro t=2 pertence ao domínio de um segmento definido por 0≤t≤1?

Ele pode estar na reta, mas está fora do segmento.

### Uma componente nula do vetor diretor torna a reta inteira inválida?

Basta que o vetor não seja totalmente nulo; a coordenada correspondente fica constante.

## Preparação de aula

Comece por dois pontos; forme o vetor diretor; teste um ponto usando um único parâmetro; explore componente zero; troque a escala e o ponto de apoio; compare segmento e reta; termine com a projeção xy que oculta diferença em z.

## Pendências

Planos, incidência, distâncias, posições relativas e mais exercícios de demonstração. A aula é cobertura parcial e não certifica domínio individual.
