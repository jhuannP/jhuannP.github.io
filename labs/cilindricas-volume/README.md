# Coordenadas cilíndricas e uma região verificável

Atividade original de graduação. Não são dados medidos ou notas pessoais já revisadas. Registro acadêmico RN2023/1 preservado.

## Região, unidades e convenções

A transformação é (r,θ,z)→(r cosθ,r senθ,z), raio r≥0 e ângulo em radianos. Fora do eixo, a inversa numérica escolhe0≤θ<2π por atan2; no eixo não existe ângulo único. Uma carta suave evita uma costura. Intervalos de duas voltas contam multiplicidade. Em volume escalar usa-se o módulo do determinante, r; bordas de volume nulo não justificam integrar sem análise uma função realmente singular.

Fixe L>0, R=r/L, Z=z/L. O exemplo prescreve1≤R≤2,0≤θ≤π/2,0≤Z≤4−R². É um quarto de anel sob paraboloide, com fator L³R no volume. A figura própria apresenta vista superior e seção meridional; não reproduz imagens do livro.

Resultados:

- V=9πL³/8;
- integral de r² dV=9πL⁵/4;
- integral de z dV=9πL⁴/8, dando centroide geométrico z̄=L;
- densidade prescritaρ=ρ₀R² dá M=9πρ₀L³/4 e densidade média2ρ₀. O centro de massa variável precisa de ponderação própria.

Cortes horizontais:0≤Z≤3 e1≤R≤√(4−Z). A área da seção éπL²(3−Z)/4. Sua integral confirma o volume por outra ordem. Não tratar r como distância à origem3D ou usar fator esférico.

## Código e verificações

Execute da raiz:

```sh
python3 labs/cilindricas-volume/cylinder.py
python3 -B -m unittest discover -s labs/cilindricas-volume -t .
```

`integral` opera polinômios com coeficientes/endpoints racionais. `moments` devolve coeficientes deπ com L=1. `midpoint(N)` integra ângulo/altura analiticamente e usa ponto médio apenas no raio. Não é integrador3D geral. O coeficiente aproximado deπ é9/8+3/(16N²). Omitindo o Jacobiano R, converge para5/6+1/(24N²). Refinar essa segunda conta não recupera o volume certo.

N inteiro entre1 e10000; flag do Jacobiano estritamente booleana. Conversões usam floats finitos, r≥0 e |θ|≤10⁶ para limitar a entrada; precisão perto da costura e eixos requer cuidado. `inverse` rejeita o eixo e raio não representável; `point` aceita r=0, com vários ângulos representando o mesmo ponto.

Cinco testes: volume/momentos por cortes independentes e marcos literais; seis malhas com erros racionais exatos e razão4 ao refinar; quatro células anulares de volume exato; trinta conversões ida/volta e seis determinantes por diferenças centrais; contratos inválidos. Não certificam prova geral de mudança de variáveis ou domínio pessoal.

## Fontes — 29/10/2026

Apostol,Cálculo,volumeII,tradução Reverté1996/reimpressão2004 de original segunda edição. Trechos §§11.32–11.33,pp458–460/PDF471–473 consultados parcialmente em texto; pp459–460/PDF472–473 inspecionadas visualmente para transformação,ângulo e Jacobiano. Paginação confirmada nesta parte do exemplar, sem aplicar deslocamento de capítulos anteriores. Fórmulas rederivadas; sem figuras ou exercícios do texto reproduzidos. PDF privado não é servido.

O programa MAT0216 mantém consulta29/10/2026 já registrada, sem nova abertura neste bloco ou comprovação da versão ministrada em2023. OpenStax§5.7 não abriu; não foi usado como leitura de corpo. Região, densidade, valores, SVG, código e exercícios próprios preparados com IA. Outros domínios, funções singulares, teoria geral e revisão pessoal pendentes.
