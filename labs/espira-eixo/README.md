# Campo de uma espira no eixo — laboratório original

Espira filamentar circular de raio a>0 no plano xy, corrente estacionária I orientada em φ crescente; observação P=(0,0,z) no vácuo. O circuito é fechado; um elemento de corrente isolado é apenas parte da integral. Campo axial Bz=μ0 I a²/[2(a²+z²)^(3/2)]. Para I≠0 defina B0=μ0 I/(2a), incluindo seu sinal: Bz/B0=(1+(z/a)²)^(-3/2). Para I=0 o campo é zero; a razão física por B0 fica indefinida, embora a função geométrica continue definida.

Na parametrização da fonte r'=(a cosφ,a sinφ,0), dl=a(−sinφ,cosφ,0)dφ e R=P−r'. O produto dl×R=(a z cosφ,a z sinφ,a²)dφ. A distância não depende deφ. Os termos transversais integram zero, enquanto o axial soma. A direção de B não inverte ao trocar z por−z; inverte ao inverter I. Fora do eixo esta rotina não se aplica.

Exemplo próprio: a=4 cm,z=3 cm dá distância5 cm e Bz/B0=64/125=0,512. Não somamos módulos de vetores. Para |z|≫a, o campo dipolar axial é μ0 m/(2π|z|³),m=Iπa², orientado em+z para I>0 em ambos os lados do eixo. Seu erro relativo à expressão exata é (1+(a/z)²)^(3/2)−1, não uma garantia de precisão em qualquer ponto.

```sh
python3 labs/espira-eixo/loop.py
python3 -m unittest discover -s labs/espira-eixo -t .
```

O código usa float e somente biblioteca padrão. Quadratura de pontos médios na variável angular, normalizada:35 combinações de u e n. No eixo o integrando axial é constante; por isso a boa concordância não demonstra convergência de um integrador em geometria geral. A quadratura verifica componentes, simetria e normalização neste caso restrito. Não modela segmentos de polígono finitos, material magnético, transiente, fio de seção finita ou medições. |u|≤1000,4≤n≤4096 são limites do laboratório, não limites físicos universais. μ0 fica simbólico; nenhum valor SI histórico é declarado exato.

Fonte privada: Nussenzveig, Curso de Física Básica3,2ªed.,Blucher2015,§8.3 Exemplo2(a),p.147/PDF148, consulta textual parcial29/10/2026 à derivação axial; sem leitura integral ou nova inspeção visual. Complemento público [OpenStax UP2§12.4](https://openstax.org/books/university-physics-volume-2/pages/12-4-magnetic-field-of-a-current-loop),consulta parcial29/10, Eq.12.13–12.19, eixo,centro e limite distante. Nosso plano xy/eixo z,dados,vetores,figura,código e exercícios são próprios; sem reprodução de figuras,tabelas ou exercícios. Programa/turma preservados; conteúdo preparado não prova domínio de Jhuann. Revisão pessoal pendente.
