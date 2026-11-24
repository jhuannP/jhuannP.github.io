# Movimento circular e componentes da aceleração

27/10/2026. Notas originais com apoio de IA, rascunho para revisão pessoal. Conteúdo preparado não comprova domínio ou experimento de Jhuann.

## Convenções e derivação

Referencial inercial, raio R>0 fixo, θ em radianos, anti-horário positivo. e_r=(cosθ,sinθ),e_θ=(−sinθ,cosθ), r=Re_r. Derivar dá v=Rωe_θ e a=−Rω²e_r+Rαe_θ. Rapidez R|ω|, período uniforme 2π/|ω| para ω≠0. A componente tangencial Rα é assinada na base crescente, não sempre a derivada da rapidez: para ω<0 o sinal muda, em ω=0 a rapidez pode não ser diferenciável.

Exemplo preservado R=2 m, rapidez 4 m/s: |ω|=2; em θ=0 e ω>0, r=(2,0),v=(0,4),a=(−8,0). Reverter ω muda v mas não a radial no mesmo ponto. No uniforme v·a=0, potência resultante zero e energia cinética constante, sem aceleração vetorial nula. No não uniforme, |a|²=(Rω²)²+(Rα)².

Contato horizontal fictício: m=0,5 kg,R=2 m,μs=0,5,g=10 m/s²,N=mg=5 N, limite 2,5 N. Rapidez 2 m/s uniforme exige 1 N, 4 m/s exige 4 N e não cabe no limite estático. vmax²=μs gR=10. Atrito real não é sempre μsN. Para componente tangencial at, condição de módulo: sqrt((v²/R)²+at²)≤μs g. v=2,at=3 dá sqrt13<5; v=3,at=3 dá sqrt29,25>5, embora componentes separadas sejam menores que 5.

A resultante radial não é uma força extra. O teste de contato é separado da trajetória cinemática prescrita: falhar não simula o movimento após deslizamento. N=mg exige as hipóteses verticais declaradas. Sem círculos verticais, tensão variável, rotação de corpo rígido ou experimento.

## Fonte

Nussenzveig, Curso de Física Básica vol.1, 5ª ed., Blucher 2013, §§3.7–3.8 pp.77–82/PDF78–83, consulta parcial em 27/10/2026; p.81/PDF82, equações (3.8.7)–(3.8.9), inspecionada visualmente. Figuras, exemplos, números e exercícios próprios; PDF privado não distribuído. Fonte curricular não reaberta neste bloco; mapa preserva a limitação de versão da turma.

## Código e verificações

`circle.py`: θ=θ0+ω0t+αt²/2, α constante, entradas/saídas float finitas e R>0. Resultados em SI, radianos. `friction` recebe m,R,rapidez,at,μ,g e compara módulos; exige m,R,g>0, rapidez/μ≥0. Não valida resolução numérica para valores/ângulos extremos; um resultado finito não garante precisão arbitrária. Comparação de limite usa valores float e não é certificado intervalar. Não há integrador dinâmico.

Da raiz: `python3 -m unittest discover -s labs/circular-componentes -t .`. Cinco testes: referência uniforme e sentido; derivadas centrais em 54 estados moderados e identidade de norma; componentes/potência e instante de ω=0; atrito e escala de massa; contratos. Diferenças finitas usam h=1e−4 com tolerâncias, não uma prova geral.

Preservados IDs/exemplo/código/desafio originais. Dez questões novas: |ω|=2;ax=−8;N=5;atrito necessário=1;necessidade radial=4;vmax²=10;componente tangencial=2 no instante parado; não somar força centrípeta; combinar componentes pelo módulo; sentido não muda ω². Resoluções na aula.

Revisão proposta em duas sessões: derivar v/a e seus sinais; depois desenhar forças e testar contato. Pendentes: dinâmica após deslizamento, círculos verticais, sistemas acoplados, revisão pessoal e experimento.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 761 fórmulas MathML conferidas. Em 390 px, atrito necessário rejeitou 2,5 e aceitou 1 pelo Enter; condição pelo módulo aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela, Windows real e experimento pendentes.
