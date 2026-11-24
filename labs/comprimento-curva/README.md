# Comprimento: uma integral e cordas certificadas

Rascunho original para revisão pessoal, sem evidência de domínio atual de Jhuann. Recorte de Matemática II, item de funções vetoriais; não certifica cobertura completa de geometria diferencial.

## Modelo e demonstração

Para r C1 num intervalo compacto, define-se L como supremo das somas de comprimentos de cordas, sobre todas as partições ordenadas do parâmetro. A desigualdade triangular e o teorema fundamental dão soma≤integral da norma de r'.

Se ω(δ) é o módulo de continuidade uniforme de r', então em cada intervalo de tamanho h≤δ, a diferença entre o vetor da corda e r'(a_i)h tem norma≤ω(δ)h. Pela desigualdade triangular reversa, a diferença entre os respectivos comprimentos também. Somando: a soma de cordas difere da soma de Riemann à esquerda por no máximo ω(δ)(b−a). Quando a malha tende a zero, ambas convergem à integral. Como cada soma≤L, obtemos a desigualdade oposta e L=integral||r'||. Não usamos um único ponto de valor médio comum a todas as componentes.

Comprimento conta percurso e multiplicidade, não apenas a imagem geométrica. Reparametrização C1 monótona bijetiva preserva comprimento por regra da cadeia e substituição (com valor absoluto para orientação inversa). Uma parametrização que vai e volta não é essa mudança bijetiva.

## Exemplo próprio

r(t)=(3t−t³,3t²), 0≤t≤1. A identidade (3−3t²)²+(6t)²=9(1+t²)² dá rapidez3(1+t²), comprimento3t+t³ entre0 e1 igual4, distância dos extremos√13. O comprimento acumulado até1/2 é13/8. As unidades de coordenadas são abstratas e t é adimensional.

r(u²) tem rapidez6u(1+u⁴), integral3u²+u⁶ igual4; derivada nula na extremidade u=0 não impede a fórmula de comprimento. Para estudar tangente unitária nessa parametrização seria preciso tratar o ponto separadamente.

## Código e limites de aproximação

`python3 labs/comprimento-curva/length.py`

`python3 -m unittest discover -s labs/comprimento-curva -t .`

Pontos, quadrados de cordas e comprimento exato usam Fraction. Para cada raiz racional q, isqrt calcula k=floor(10^d sqrt(q)); a raiz fica entre k/10^d e (k+1)/10^d, com igualdade detectada. Ao somar n intervalos, a largura total é≤n/10^d. São limites da POLIGONAL, não limites bilaterais do arco. A curva tem comprimento4 por prova analítica; a soma de cordas é≤4. Refino por inclusão de vértices não diminui a poligonal, mas comparar partições arbitrárias só pelo número de pontos não é válido.

Neste exemplo ||r''||≤9, logo a estimativa pela continuidade uniforme dá 0≤4−L_poligonal≤9/n em malha uniforme. O limite inferior calculado tem erro até9/n+n/10^d; é uma cota suficiente, pouco apertada. O código não calcula comprimento de curvas arbitrárias nem mede dados experimentais ruidosos.

Quatro testes: identidades exatas em101 parâmetros e aditividade; somas de cordas comparadas com Decimal65 dígitos em sete partições; refino e raízes limitadas por desigualdades racionais; contratos. Testes não substituem a prova para todo parâmetro.

## Fontes

Apostol, Calculus vol. I, 2ª edição (1967): §§14.10 e14.12, pp.529–531/PDF549–551 e533–534/PDF553–554, consulta textual parcial em29/10/2026. Cabeçalhos conferidos; sem nova inspeção visual ou leitura integral. OpenStax Calculus vol.2 §7.2, trecho de comprimento paramétrico, consulta parcial na mesma data. A prova por continuidade uniforme, a curva polinomial, os exemplos, o desenho, os exercícios e o laboratório são redação e construções próprias, sem copiar figuras ou exercícios das fontes.

[OpenStax §7.2](https://openstax.org/books/calculus-volume-2/pages/7-2-calculus-of-parametric-curves)

Programa de CCM0123 reconferido anteriormente em29/10/2026, versão2025 posterior à turma2024/1; essa limitação permanece. PDFs privados não são distribuídos.
