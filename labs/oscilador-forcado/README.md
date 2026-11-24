# Forçamento: particular, homogênea e energia

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Teste local: python3 -m unittest labs.oscilador-forcado.test_experiment.

q''+2ζq'+q=cos(rτ), q=kx/F0, τ=ω0t, r=Ω/ω0.
ζ=b/(2mω0), 0..0,9. Não crítico/superamortecido. Repouso, particular ou
q0=1/v0=0. Na particular periódica D=(1−r²)²+(2ζr)², amplitude 1/√D.
Na singularidade ζ=0/r=1 usa q_p=τsenτ/2 e amplitude=None, sem substituição
por denominador pequeno. A homogênea sem amortecimento pode persistir.
Curva de frequência preservada; lacuna junto da singularidade não é valor zero.

Energia E*=(q'²+q²)/2; taxa=cos(rτ)q'−2ζq'². Média da particular periódica
ζr²/D. Para ζ>0, máximo de potência em r=1; pico de deslocamento em
√(1−2ζ²) só para ζ<1/√2. Não confundir esses máximos ou frequência livre.
No r=0, limite estático e potência média nula. Unidades de potência F0²ω0/k.

Quatro testes: 180 estados com condições iniciais, EDO, energia e envoltória;
18 trajetórias por RK4 independente com refinamento .05→.025, integrando
trabalho líquido; nove médias de ciclo com 1024 pontos; máximos de amplitude
/potência, singularidade, conversão dimensional e contratos. 108 referências
Python/JS. O gráfico usa solução fechada, não a integração de verificação.

Fontes parciais em 16/10/2026:
- Nussenzveig, Curso de Física Básica 2, exemplar local, 4.4, pp. 107–108
  (PDF 108–109). Página 107 inspecionada visualmente. O arquivo contém
  data de composição 2014; não foi inferida nova edição nesta consulta.
- [Feynman I, 23–1/23–2](https://www.feynmanlectures.caltech.edu/I_23.html),
  solução complexa e dissipação linear, consulta direta parcial.
As fontes escrevem γ=b/m, enquanto a aula anterior usava 2γ=b/m.
A conversão está explícita; não se trocou símbolo mantendo valor numérico.
Não se usa a aproximação de ressonância estreita como máximo exato de
amplitude. Exemplos, código e curvas próprios; nenhum PDF privado é servido.

Visual: três contribuições no tempo e curva de frequência; tabela auditável,
azul/tracejado/pontilhado sem animação que esconda preparação ou escala.
Limites: sem hardware, ajuste, não linearidade, caso crítico, Q detalhado ou
experiência de bancada atribuída. Aula e dois IDs originais preservados;
revisão pessoal e aplicações permanecem pendentes.
