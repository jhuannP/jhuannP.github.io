# Inversas trigonométricas — ramos, derivadas e direção

## Inverter uma função exige recuperar um único argumento

O seno no domínio real inteiro não é injetivo: sin(π/6)=sin(5π/6)=1/2, além de repetições por voltas completas. Portanto não existe uma única inversa que devolva todo ângulo original a partir de seu seno. Restringimos o domínio a um intervalo em que a função é estritamente monótona. Escolher esse intervalo, chamado ramo, faz parte da definição; não é um detalhe que pode ser resolvido depois da conta.

## O ramo principal de arcsin inclui os dois extremos

Restringimos sin a [−π/2,π/2], onde é estritamente crescente e sua imagem é [−1,1]. A inversa arcsin tem domínio [−1,1] e imagem [−π/2,π/2]. Assim arcsin(1/2)=π/6. A expressão sin⁻¹ pode ser usada para a inversa em algumas referências, mas nesta aula escrevemos arcsin para não confundir com o recíproco 1/sin.

arcsin:[−1,1]→[−π/2,π/2]

## arccos e arctan usam intervalos diferentes

Para arccos, restringimos cos a [0,π], onde é decrescente; seu domínio de entrada também é [−1,1] e sua imagem é [0,π]. Por exemplo, arccos(−1/2)=2π/3. Para arctan, restringimos tan a (−π/2,π/2); ela é crescente e atinge todo real. Assim arctan tem domínio ℝ e imagem aberta (−π/2,π/2). Os extremos não entram porque a tangente não está definida neles.

## Uma composição recupera o número; a outra depende do ramo

Para x em [−1,1], sin(arcsin x)=x. Já arcsin(sin θ)=θ só vale se θ estiver no ramo [−π/2,π/2]. Em θ=5π/6, a composição devolve π/6. Do mesmo modo, arctan(tan(3π/4))=−π/4: são ângulos com a mesma tangente, e apenas −π/4 pertence ao intervalo principal. Não simplifique uma composição sem conferir o domínio e a imagem envolvidos.

## O quociente de incrementos justifica a derivada da inversa

Se y=f(θ) e a função é contínua e estritamente monótona no intervalo escolhido, sua inversa g é contínua. Quando f′(θ) existe e é diferente de zero, o quociente Δθ/Δy é o recíproco de Δy/Δθ. Ao tomar o limite no ponto correspondente, obtemos g′(y)=1/f′(g(y)). A hipótese de derivada não nula importa; não usamos essa conclusão onde f′ zera.

g′(x)=1/f′(g(x))

## A raiz positiva na derivada de arcsin vem do ramo

Escreva θ=arcsin x, então sin θ=x. No interior do ramo, cos θ>0. Pela identidade do círculo, cos θ=√(1−x²), com raiz positiva. Aplicando a derivada da inversa, (arcsin x)′=1/√(1−x²), válida para −1<x<1. Em x=±1 a função está definida, mas a fórmula não fornece uma derivada finita; a derivada do seno nos pontos correspondentes é zero.

(arcsin x)′=1/√(1−x²), |x|<1

## O sinal negativo de arccos também vem da função original

Para θ=arccos x no interior de (0,π), sin θ=√(1−x²)>0, enquanto a derivada de cos θ é −sin θ. Portanto (arccos x)′=−1/√(1−x²), para −1<x<1. O sinal acompanha a monotonicidade decrescente de arccos. O domínio da função inclui ±1; o domínio desta fórmula de derivada exclui esses extremos.

## A derivada de arctan usa a identidade da tangente

Se θ=arctan x, então tan θ=x e a derivada da tangente é 1+tan²θ. Aplicar a regra da inversa fornece (arctan x)′=1/(1+x²), para todo x real. Por exemplo, em x=1 a derivada é 1/2. O fato de a imagem de arctan ser um intervalo limitado não limita seu domínio de entrada.

(arctan x)′=1/(1+x²)

## Na regra da cadeia, a derivada interna permanece

Para F(x)=arctan(2x), a derivada é F′(x)=2/[1+(2x)²], definida em todo real; em x=0 vale 2. Para G(x)=arcsin(x²), o domínio real é [−1,1], mas a derivada G′(x)=2x/√(1−x⁴) vale em (−1,1). Verificar o domínio da função e o da derivada separadamente evita usar uma fração formal em um ponto onde ela não representa a operação original.

## Um valor principal não lista todas as soluções de uma equação

A equação sin θ=1/2 tem duas famílias de soluções: θ=π/6+2kπ ou θ=5π/6+2kπ, com k inteiro. No intervalo [0,2π), há exatamente duas. Calcular arcsin(1/2) fornece apenas a solução principal π/6; o círculo e a periodicidade recuperam as demais. Em um problema físico, o intervalo e a orientação admissíveis devem vir da situação, não de uma escolha silenciosa da calculadora.

## arctan(y/x) perde informação de quadrante

Para o ponto (x,y)=(−1,+1), a razão y/x é −1 e arctan(−1)=−π/4. Esse ângulo aponta para o quarto quadrante, enquanto o ponto está no segundo. A função atan2(y,x) recebe os dois sinais e fornece 3π/4. Ela também trata o eixo vertical sem formar uma divisão por zero. Não determina uma direção geométrica na origem, onde não existe vetor não nulo. O laboratório rejeita esse caso explicitamente.

## A direção orientada usa uma convenção de intervalo

No laboratório, direction_angle(x,y) devolve um representante em [−π,π), com início no eixo x positivo e sentido positivo anti-horário. No semieixo x negativo, escolhemos −π, equivalente a +π módulo uma volta. Unificamos também as saídas +0 e −0. Esses ajustes são uma convenção da interface didática; a documentação de atan2 permite resultados entre −π e +π e seu comportamento nos zeros assinados não deve ser confundido com unicidade de um ângulo físico.

## Valores aproximados não devem ser tratados como identidades exatas

O código aceita int/float finitos, rejeita bool, texto, valores não finitos e argumentos fora de [−1,1] para asin/acos. Não força um argumento ligeiramente inválido a caber no domínio. As respostas são floats em radianos. Para entradas muito grandes, o valor aproximado de atan pode arredondar até π/2, apesar de a imagem matemática ser aberta. Perto do corte de direção também há limitações de arredondamento. A convenção deve acompanhar qualquer interpretação numérica.

## A revisão precisa reconstruir a escolha do sinal e do ramo

Confira as três inversas principais, refaça a raiz positiva em arcsin e a derivada negativa em arccos, depois explique o exemplo do segundo quadrante. Os testes verificam composições, coordenadas normalizadas, eixos e fronteiras; não substituem as demonstrações. A consulta ao Apostol foi parcial e os exemplos destas notas de aula são originais, preparados com apoio de IA. O curso continua com aprofundamentos e revisão pessoal pendentes, mesmo com os primeiros recortes de funções especiais disponíveis.

## Exercícios e resoluções

- Escreva arcsin(1/2)=cπ rad no ramo principal. Qual c? **Resolução:** O ramo é [−π/2,π/2], então o ângulo é π/6.
- Escreva arccos(−1/2)=cπ rad. Qual c? **Resolução:** O ramo [0,π] contém 2π/3.
- Escreva arctan(−1)=cπ rad. Qual c? **Resolução:** A solução no intervalo aberto (−π/2,π/2) é −π/4.
- Escreva arcsin(sin(5π/6))=cπ rad. Qual c? **Resolução:** O seno é 1/2 e a inversa principal devolve π/6.
- Escreva arctan(tan(3π/4))=cπ rad. Qual c? **Resolução:** A tangente é −1; a inversa principal devolve −π/4.
- Quanto é (arcsin x)′ em x=0? **Resolução:** 1/√(1−0²)=1.
- Quanto é (arccos x)′ em x=0? **Resolução:** −1/√(1−0²)=−1.
- Quanto é (arctan x)′ em x=1? **Resolução:** 1/(1+1²)=1/2.
- Quanto é a derivada de arctan(2x) em x=0? **Resolução:** 2/[1+4x²], em zero vale 2.
- Para (x,y)=(−1,+1), escreva a direção de atan2(y,x)=cπ rad. Qual c? **Resolução:** O ponto está no segundo quadrante: 3π/4.
- No ramo [−π,π) do laboratório, escreva a direção de (−1,0)=cπ rad. Qual c? **Resolução:** Escolhemos −π como representante do semieixo negativo.
- Quantas soluções de sin θ=1/2 existem em [0,2π)? **Resolução:** π/6 e 5π/6 pertencem ao intervalo.

## Código e fontes

Na raiz: `python3 -m unittest discover -s labs/inversas-trigonometricas -t .` e `python3 -m labs.inversas-trigonometricas.principal`. Só biblioteca padrão. inverse aceita kind asin/acos/atan e int/float finito; argumentos asin/acos precisam estar em [−1,1] sem margem de tolerância ou clamp. direction_angle(x,y) usa math.atan2(y,x), rejeita origem, troca +π por −π e unifica zeros na saída. Entradas inteiras que não cabem em float são rejeitadas. Saídas aproximadas podem arredondar para extremidades matematicamente abertas ou para o corte; não há garantia astrométrica.

Testes: 41 entradas de asin/acos, sete de atan, 80 vetores inteiros não nulos com coordenadas normalizadas e escala positiva, eixos/zeros assinados/corte, vizinhos nextafter fora do domínio e atan(1e300) arredondado até π/2. Não são um teste de leitor de tela ou uma prova de identidades para todo real.

Fonte do acervo autorizado: Apostol, Calculus I, 2ª ed. (1967), §§6.20–6.21, pp.252–255 (PDF272–275), consulta textual parcial em 22/10/2026; mantida limitação de avisos de extração/OCR, sem cópia de páginas ou exercícios. Complemento de implementação: [Python 3.14 math](https://docs.python.org/3.14/library/math.html#math.atan2), consulta parcial na mesma data, contratos das inversas e quadrantes de atan2. Página da série 3.14 pode ter patch diferente do runtime local; não se declarou igualdade de versões. Exemplos, figura e notas próprios assistidos por IA.

14 seções/12 exercícios. Curso com 24 aulas/204 exercícios, dez grupos parciais; nenhum completo. Aprovação histórica e limitação de programa da turma preservadas. Próxima revisão pessoal: justificar ramo/sinal das raízes e comparar arctan/atan2. Próximo desenvolvimento deve revisar aulas curtas de funções/integração e o restante das trilhas, sem aprofundar indefinidamente um único recorte.

Verificação: cinco testes locais aprovados após incluir __init__.py para descoberta do pacote. Conferidos 41 argumentos de asin/acos, sete de atan, 80 vetores não nulos, escala, eixos, zeros assinados, corte, nextafter e arredondamento em atan grande. Treze testes de catálogo e 575 estruturas MathML aprovados. Navegador em 390 px: documento de 375 px, figura inspecionada; questão 5 rejeitou 3/4 e aceitou −1/4 como coeficiente de π. Console sem erros observados. Prévia inversas-trigonometricas-mobile.jpg. Catálogo 509 aulas/3315 exercícios, 254 aulas com até três seções; cobertura recalculada. Sem revalidação global, leitura integral do capítulo ou revisão pessoal. Saldo semanal confirmado após bloco: 89%; parada em 65%. Próxima revisão pessoal: demonstrar sinais/ramos e comparar razão com direção; próximo bloco deve rever conteúdo curto em outra parte do catálogo ou consolidar Riemann/assíntotas.
