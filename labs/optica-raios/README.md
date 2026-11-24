# Óptica: normal, refração e lente fina

Notas de aula originais assistidas por IA, em rascunho para revisão de Jhuann. Não atestam domínio pessoal, experimento realizado ou conclusão do percurso escolar.

## Referência e limites da leitura

Nussenzveig, *Curso de Física Básica4*, 2ª edição, Blucher2014, reimpressão2017 (edição digital2018). Consulta parcial: §2.2, páginas impressas16–18/PDF17–19; §2.4, impressas22–23/PDF23–24; §2.8, impressas31–34/PDF32–35. PDF contado a partir de1, não pelo rótulo impresso. Leitura textual reconferida nos recortes locais em26/10/2026; algumas fórmulas não saem na extração. Páginas impressas16,23 e33 foram inspecionadas visualmente na preparação anterior; sem nova inspeção dessas imagens neste bloco. Não houve leitura integral do capítulo. A notação relativa do livro foi traduzida para índices absolutos declarados; os desenhos, números, exercícios e código são próprios. O exemplar privado não é distribuído.

## Reconstruir a interface

A normal é perpendicular à superfície no ponto de incidência. Os ângulos de incidência e reflexão têm a mesma medida, em lados opostos da normal. Incidência30° pela normal dá reflexão30°, ou60° com a superfície.

Em meios homogêneos, isotrópicos e transparentes, para uma frequência definida e índices reais positivos, Snell dá n₁ sinθ₁=n₂ sinθ₂. No exemplo hipotético n₁=1,n₂=3/2,θ₁=30°, o seno transmitido é1/3 e o ângulo aproximadamente19,4712°. A refração aproxima o raio da normal. Para interface fixa, linear e estacionária, a componente transmitida mantém a frequência; v=c/n e λ=v/f dão λ₂/λ₁=n₁/n₂=2/3.

Primeiro calcule s=(n₁/n₂)sinθ₁. Se s<1 há ângulo transmitido menor que90°; s=1 é o limite rasante; s>1 é reflexão interna total neste modelo. O crítico existe para n₁>n₂: sinθc=n₂/n₁. Exemplo2→1: θc=30°. Seno exigido3/2 não é arredondado para1. Não se calculam coeficientes de Fresnel ou campos evanescentes; ausência de raio propagante não significa campo eletromagnético nulo no segundo meio.

## Reconstruir a lente

Luz da esquerda para a direita, objeto real à esquerda p>0, imagem real à direita q>0, virtual à esquerda q<0. Foco convergente positivo, divergente negativo. Lente delgada paraxial, mesmo meio externo nos dois lados:1/f=1/p+1/q e q=fp/(p−f) se p≠f. Aumento assinado m=−q/p.

- f=2cm,p=4cm: q=4cm,m=−1. Objeto yₒ=+0,2cm dá yᵢ=−0,2cm. No esquema, alturas foram ampliadas em relação à escala horizontal.
- f=2cm,p=1cm: q=−2cm,m=+2; imagem virtual e direita (mesma orientação vertical).
- f=2cm,p=2cm:1/q=0, sem imagem a distância finita; não dividir por zero.
- f=−2cm,p=4cm: q=−4/3cm,m=1/3.

Use uma única unidade de comprimento. Converter cm para m escala q, preservando m. A lente real pode exigir correção de espessura e aberrações; igualdade algébrica não valida a aproximação experimentalmente.

## Executar e conferir

Na raiz do site:

```sh
python3 -m labs.optica-raios.optics
python3 -m unittest discover -s labs/optica-raios -t .
python3 labs/optica-raios/draw_figures.py
```

`snell` recebe índices e seno incidente em int/Fraction, rejeitando bool/float e incidência rasante de entrada. Decide o regime por comparação racional exata. `angle_degrees` converte só para exibição aproximada. Um valor extremamente próximo de1 pode aparecer como90° em float, sem alterar a classificação exata. `critical_sine` retorna None quando não há crítico inferior a90°. `thin_lens` aceita f não nulo e p>0; não resolve objeto virtual.

Seis testes: ângulos conhecidos; classificação no crítico e vizinhos racionais ±2⁻²⁰⁰; reciprocidade de Snell em90 configurações; exemplos real/virtual/divergente/focal; identidade gaussiana e conversão de unidade em120 configurações; contratos. Esses testes verificam implementação, não demonstram as leis físicas.

## Estudo e lacunas

Em20min, desenhe a normal, refaça sinθ₂=1/3, classifique o caso s=3/2 e resolva p=2f versus p=f/2. Explique que uma imagem virtual vem dos prolongamentos dos raios e não pode ser recolhida diretamente numa tela na posição virtual.

Permanecem fora deste recorte: espelhos curvos, instrumentos, dispersão de múltiplas cores, interferência, difração, intensidades e eletromagnetismo completo. Revisão pessoal e uso com aluno pendentes.
