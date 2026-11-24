# Centro de massa e movimento relativo

Material original preparado com apoio de IA em 28/10/2026. Revisão pessoal pendente. Partículas clássicas com massas individuais constantes, referencial inercial e forças internas que se compensam aos pares. O código trata somente uma dimensão e valores racionais em SI; o texto usa notação vetorial quando indicado.

## Da posição ao movimento coletivo

R=Σmᵢrᵢ/M, com M=Σmᵢ, é uma média ponderada. Derivando com massas constantes, V=P/M. Somar Newton para o sistema fixo cancela as forças internas newtonianas, resultando em M A=F_ext. F_ext=0 implica V constante, sem exigir que cada partícula esteja em repouso ou que R seja fixo. Massa que cruza a fronteira e momento de campos exigem outra descrição.

Defina ρᵢ=rᵢ−R e uᵢ=vᵢ−V. Então Σmᵢρᵢ=0 e Σmᵢuᵢ=0. O segundo zero é o momento total no referencial do CM, não a velocidade individual de cada corpo. Para K=Σmᵢ|vᵢ|²/2, substitua vᵢ=V+uᵢ: o termo cruzado V·Σmᵢuᵢ desaparece. Logo K=M|V|²/2+Σmᵢ|uᵢ|²/2. Trata-se de uma identidade de estado, não de conservação de K.

Para dois corpos, μ=m₁m₂/(m₁+m₂), u₁=(m₂/M)(v₁−v₂) e u₂=−(m₁/M)(v₁−v₂). Substituir dá K_rel=μ|v₁−v₂|²/2. A massa reduzida é uma combinação dos parâmetros, sem acrescentar uma terceira partícula. K_rel é cinética do movimento relativo macroscópico, não toda a energia interna termodinâmica de corpos extensos.

## Exemplo original ligado ao exemplo anterior

Massas 1 kg e 3 kg nas posições 0 e 4 m têm R=3 m, preservando o exemplo da aula. Acrescente velocidades 4 m/s e 0: P=4 kg m/s e V=1 m/s. As velocidades relativas são 3 e −1 m/s; seu momento ponderado é zero. K=8 J, K_CM=2 J e K_rel=6 J, de modo que 8=2+6. μ=3/4 kg e velocidade relativa 4 m/s também dão K_rel=(1/2)(3/4)16=6 J.

Imponha impulsos internos J₁=−3 e J₂=+3 kg m/s. As velocidades finais são 1 e 1 m/s, com mesmo P=4 e V=1. K cai para 2 J: os 6 J do movimento relativo não estão mais na cinética translacional das duas partículas. Um mecanismo dissipativo poderia transferir essa parcela a deformação/calor; o código não modela mecanismo ou história de forças e não identifica o destino energético real. As posições são mantidas como comparação de estados, sem integração temporal. Não é uma simulação de colisão medida nem afirma que a energia total desapareceu.

## Referência e invariância

Transladar todas as posições por c move R por c, preservando as posições relativas. Num referencial galileano que se move com velocidade U, vᵢ′=vᵢ−U e V′=V−U: as velocidades relativas e K_rel permanecem iguais. K total depende do referencial. O teste adiciona b a todas as velocidades e verifica K_novo=K+bP+Mb²/2, equivalente a U=−b em uma dimensão.

## Executar

```sh
python3 collective.py
python3 -m unittest test_collective.py
```

Python padrão. Listas/tuplas não vazias de mesmo comprimento, massas positivas, int/Fraction; float/bool são rejeitados. Unidades: kg, m, m/s; resultados de energia em J. `internal_impulse` recebe os impulsos já integrados, sem calcular pico, duração, forças ou acelerações. Não impõe conservação de energia, elasticidade ou aderência.

Quatro testes: 225 estados de dois corpos contra fórmula por massa reduzida; 27 estados de três corpos e 81 mudanças comuns de posição/velocidade; 45 impulsos internos e o exemplo com variação de K; contratos. Confere identidades e hipóteses do modelo, não certifica domínio de Jhuann.

## Fontes e limites

Nussenzveig, *Curso de Física Básica*, vol.1, 5ª edição (edição previamente confirmada no exemplar autorizado), §8.1 pp.186–189/PDF187–190: consulta textual/visual parcial em 28/10/2026, forças internas newtonianas, CM e movimento relativo. P.226/PDF227, parágrafo inicial de §9.7, consultado para massa reduzida em caso específico de colisão. Sem leitura integral das seções nem reprodução de exercícios/figuras. A identidade geral de energia e o exemplo 1 kg/3 kg foram deduzidos nas notas; não se atribui esse exemplo ao livro. Referência complementar ao programa registrado; não comprova livro efetivamente usado na turma. PDF privado fora do site.

Permanecem pendentes distribuição contínua, corpos extensos, rotação, sistemas abertos/relativísticos e análise completa de colisões. Próxima revisão pessoal: reconstruir 8=2+6, explicar por que Σmᵢuᵢ=0 e distinguir V constante de R constante.
