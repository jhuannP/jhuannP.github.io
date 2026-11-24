# Calor implícito, Dirichlet e duas escalas de erro

Rascunho original assistido por IA, para revisão de Jhuann. Sem medição física ou resultado pessoal atribuído.

## Fonte

Fonte temática complementar consultada em 16/10/2026: [Gilbert Strang, MIT, seção 5.4, 2006](https://math.mit.edu/classes/18.086/2006/am54.pdf), especialmente diferenças explícitas/implícitas e o intervalo com contorno. A fonte fundamenta a escolha do esquema e o contraste entre estabilidade e precisão. Exemplos, demonstrações discretas, implementação e verificações desta aula são próprios, sem reprodução de figuras, exercícios ou tabelas.

## Contrato e modelo

u_t=u_xx, intervalo [0,1], bordas zero, T=0,2, posição/tempo/amplitude adimensionais. n subintervalos espaciais e m passos temporais; r=Δt/Δx². A demonstração admite n=4,8,12,16; m=4,8,…,40. Python admite n de 4 a 64 e m de 1 a 4096.

Implícito: A=tridiag(−r,1+2r,−r); resolver A U_new=U_old. Bordas entram no RHS com sinal positivo, no instante novo. FTCS usa bordas antigas. O teste unitário de um nó interior usa r=1 e retorna 1/3 com bordas zero, 2/3 com bordas 2 e −1. Python permite um passo com valores de borda prescritos, mas não integra um calendário de bordas variáveis.

Thomas é O(n) por passo e refaz a fatoração nesta implementação didática. A matriz específica tem pivôs positivos; isso não autoriza usá-lo sem análise em qualquer tridiagonal. Um perfil linear com bordas compatíveis permanece estacionário e verifica a montagem independentemente dos modos senoidais.

## Referências e erros

Dado inicial sin(πx), opcionalmente mais 0,1 sin((n−1)πx). Esse modo alto muda com n e deve ficar desligado ao comparar convergência espacial do mesmo dado.

Contínua: amplitudes exp(−(ℓπ)²T). Semidiscreta: exp(−4n²sin²(ℓπ/(2n))T). Numérica: solver passo a passo; referência independente dos testes: G_ℓ^m. Implícito G=1/(1+rμ), explícito G=1−rμ, μ=4sin²(ℓπ/(2n)). O raio exibido considera todos os modos da malha, não só os presentes no dado.

Erros tempo/espaço/total são máximos absolutos nos nós em T, com decomposição por referência semidiscreta e desigualdade triangular. Não são erros relativos, medições ou máximos ao longo de toda a evolução. Implícito contrai norma infinito e preserva positividade neste problema; defeito normalizado O(Δt+Δx²) sob suavidade e sistemas resolvidos corretamente.

## Verificar

```sh
python3 labs/calor-implicito/experiment.py
python3 -m unittest discover -s labs/calor-implicito -t . -p 'test_*.py'
```

Quatro testes: solução densa racional independente em 16 configurações (incluindo um único nó e bordas não nulas), modo exato discreto, estabilidade/positividade, erro triangular, refinamentos separados e contratos. Contraste ordenado de dados testa contração/monotonicidade. Trinta configurações cruzam Python/JavaScript. Comparação modal em configurações instáveis usa escala global do perfil, pois cancelamentos nodais deixam resíduos de arredondamento.

Modo alto desligado + explícito instável não é usado para exigir coincidência numérica entre linguagens: arredondamento pode semear modos ausentes e ser amplificado. O comportamento não certifica estabilidade por ausência inicial de um modo. Os casos com modo alto presente verificam a amplificação de forma independente.

## Roteiro e resoluções

Padrão n=8,m=16,modo alto ligado: implícito estável, r=0,8. Troque para explícito: raio≈2,078 e forte crescimento. A escala vertical se ajusta. Reduza a malha espacial ou aumente m para estudar a restrição. Para ordem temporal, n=16 fixo, modo alto desligado, m=20,40,80, compare com semidiscreta: razão próxima de 2. Para ordem espacial, compare semidiscreta/contínua com n=8,16,32, sem modo alto: razão próxima de 4.

Respostas: 1) r=0,8; 2) diagonal 2,6; 3) adjacentes −0,8; 4) 1/3; 5) 2/3; 6) estabilidade não garante precisão; 7) razão 2; 8) razão 4; 9) desligar modo n−1; 10) um dado especial não certifica todos os modos.

Lacunas: Crank–Nicolson, fonte, difusividade variável, outros contornos/domínios, características e elementos finitos. Não há extensão automática das provas a esses casos.
