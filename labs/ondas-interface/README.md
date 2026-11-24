# Reflexão em cordas: amplitude e energia

Modelo original ideal, com apoio de IA e revisão pessoal pendente. Não é ensaio de material, medição ou simulação de uma junção real.

## Hipóteses e convenção

Cordas lineares, pequenas inclinações, tensão comum T>0, densidades μ>0 e junção sem massa, separação ou dissipação em x=0. Incidência pela esquerda, x<0. Velocidade c=√(T/μ), impedância Z=T/c=√(Tμ), unidade kg/s. A amplitude y é transversal; o perfil se propaga ao longo de x, sem transportar cada elemento da corda com velocidade c.

As condições são continuidade de y e de T y_x. Para ondas harmônicas com mesma ω na junção estacionária:

- A_i+A_r=A_t.
- Z₁(A_i−A_r)=Z₂A_t.
- r=(Z₁−Z₂)/(Z₁+Z₂), τ=2Z₁/(Z₁+Z₂).

r é um coeficiente de deslocamento com sinal. A potência média de uma onda harmônica viajante, em módulo, é Zω²A²/2, em W; não é W/m². As frações são R=r² e 𝒯=(Z₂/Z₁)τ², com R+𝒯=1. τ² sozinho não é a transmissão de energia entre meios diferentes.

## Exemplo prescrito

T=18 N, Z₁=2 kg/s, Z₂=6 kg/s dão c₁=9 m/s, c₂=3 m/s, μ₁=2/9 kg/m e μ₂=2 kg/m. r=−1/2, τ=1/2, R=1/4, 𝒯=3/4.

Na componente harmônica com ω=4 rad/s e A_i=0,01 m: potência incidente 1,6 mW, refletida 0,4 mW e transmitida 1,2 mW. Inverter os meios dá r=+1/2 e τ=3/2, mas mantém as frações de energia 1/4 e 3/4. Manter A_i e ω ao inverter os meios muda também a potência incidente absoluta.

## Pulso separado do exemplo harmônico

Perfil original q(s)=[1−(s/Δ)²]³ para |s|<Δ e zero fora, Δ=1/20 s, chegada central t₀=1/3 s. O perfil e suas duas primeiras derivadas são contínuos no suporte. A amplitude inicial é 0,01 m.

À esquerda:

y=A_i[q(t−x/c₁−t₀)+r q(t+x/c₁−t₀)].

À direita:

y=τA_i q(t−x/c₂−t₀).

Antes da interação, em t=0, o incidente tem centro −3 m e suporte [−3,45;−2,55] m. Depois, em t=2/3 s, o refletido tem esse centro/suporte, e o transmitido tem centro 1 m e suporte [0,85;1,15] m. A escala vertical da figura foi ampliada; não representa inclinações físicas em escala gráfica.

O fluxo de energia orientado para +x é −T y_x y_t; a densidade por comprimento é (μ y_t²+T y_x²)/2. A integral espacial permite verificar os pulsos separados. Não aplicamos a potência média harmônica em cada instante do pulso.

## Extremidades ideais

O laboratório retorna os valores apenas na borda x=0 para os casos fixo e livre. No fixo, y=y_t=0. No livre, y_x=0 e o deslocamento na chegada central é 2A_i. Em ambos, a potência que cruza a borda é zero. O código de interface exige impedâncias finitas positivas; não recebe zero ou infinito para simular essas terminações.

## Reproduzir e conferir

Da raiz:

```sh
python3 labs/ondas-interface/waves.py
python3 -B -m unittest discover -s labs/ondas-interface -t .
```

int/Fraction, sem bool/float; unidades SI. Seis métodos de teste: marcos literais e potências; 16 pares de impedâncias contra condições de interface e conservação; 51 combinações de parâmetros/tempo para continuidade e fluxo instantâneo, além das terminações; derivada do pulso por diferenças centrais independentes; três integrais espaciais da densidade por Simpson com 128 subintervalos, contra a integral polinomial expandida do perfil e frações 1/4 e 3/4; contratos.

As integrais espaciais são quadraturas aproximadas, conferidas com erro absoluto inferior a 10⁻⁸ J neste exemplo. Não constituem um solver de ondas em malha ou prova de convergência geral. A integração polinomial de referência usa ∫[d(1−u²)³/du]²du no suporte; não deriva seu valor chamando a implementação do perfil.

## Fontes — 29/10/2026

Nussenzveig, *Curso de Física Básica*, vol.2, 5ª edição 2014/reimpressão 2017, previamente identificado. §5.6, recortes textuais pp.141–144/PDF142–145 para extremidades e junção; pp.143–144/PDF144–145 inspecionadas visualmente. §5.4 p.136/PDF137, recorte textual da potência e densidade cinética. A primeira incidência de extremidade do livro vem do sentido oposto ao adotado aqui; sinais foram derivados na nossa convenção. Modelo, pulso e figuras próprios, sem reprodução de exercícios, exemplos ou diagramas da fonte. PDF privado não servido.

[OpenStax UP1 §16.5](https://openstax.org/books/university-physics-volume-1/pages/16-5-interference-of-waves): consulta parcial nos tipos de borda e sinais da reflexão. Sem figuras/exemplos incorporados; deslocamento total na borda livre e energia foram derivados pelas condições do modelo.

[Júpiter 4302112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=4302112): consulta direta de 29/10/2026 já registrada no bloco de elasticidade, sem nova abertura neste bloco. Programa ativado em 2026, posterior à turma de 2022/2; bibliografia atual cita Nussenzveig 4ª edição. Versão histórica não recuperada; não presumir equivalência de programas ou paginação.

Dissipação, junção com massa, outros meios, geometrias, dispersão, múltiplas interfaces e revisão pessoal continuam pendentes.
