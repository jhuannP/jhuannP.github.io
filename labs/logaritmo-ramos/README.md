# Logaritmo complexo: valor, ramo e caminho

Notas originais em rascunho para revisão. Grandezas adimensionais. Conteúdo introdutório próprio para o item amplo de tópicos especiais de Matemática IV; não prova extensão efetivamente ministrada.

## Percurso 1 — definir um domínio (20 minutos)

Se z=r exp(iθ), r>0, os valores w que satisfazem exp(w)=z são ln(r)+i(θ+2πk), k inteiro. Um ramo escolhe um valor continuamente em um domínio. Usamos Log(z)=ln|z|+i Arg(z), −π<Arg<π, no plano sem o semieixo real não positivo. Neste domínio aberto a derivada é 1/z. Não atribuímos valor a −1: valores convencionais no corte e limites laterais são objetos distintos de uma função holomorfa ali.

A derivação local pode usar u=(1/2)ln(x²+y²) e uma escolha suave de v=Arg: u_x=x/r², u_y=y/r²; v_x=−y/r² e v_y=x/r². Assim Cauchy–Riemann vale e Log′=(x−iy)/r²=1/z. Essa conta precisa do ramo suave local, não de uma fórmula global arctan(y/x). A abertura do domínio exclui zero e o corte.

## Percurso 2 — produto e caminho (20 minutos)

Escolha z=w=exp(3πi/4). Ambos estão no ramo aberto e zw=−i também. Log(z)+Log(w)=3πi/2; Log(zw)=−πi/2. A diferença é 2πi. Portanto a regra real de produto pode falhar para o ramo principal, mesmo sem pontos sobre o corte. O código representa ângulos por frações de π e registra esse defeito como inteiro; não avalia um logaritmo transcendente de forma exata.

Caminhos próprios: γ_q(t)=exp(t ln2+iπqt), t de0 a1, q=3/4 ou −5/4. Ambos vão de1 a2exp(3πi/4), sem passar por zero. Como γ′/γ=ln2+iπq, as integrais são ln2+3πi/4 e ln2−5πi/4, diferença2πi. O caminho inferior cruza o corte do ramo principal, onde 1/z continua regular. Não se pode aplicar a primitiva principal ao caminho inteiro; usar apenas os mesmos extremos apagaria a diferença. Um argumento contínuo ao longo do caminho não precisa ser o argumento principal.

Se existisse uma primitiva global L′=1/z em C sem zero, toda integral fechada seria zero. Mas a circunferência unitária parametrizada exp(it),0≤t≤2π, dá2πi. Contradição. Isso não impede ramos locais ou em domínios cortados. O corte não é uma parede física ou singularidade de 1/z em seus pontos não nulos.

## Código e verificação

`principal_angle` usa aritmética racional, −8≤θ/π≤8, e rejeita o corte; `product_defect` exige z,w e zw no ramo. `spiral_integral` aceita raios1/16..16 e mudança de ângulo até8π, retorna a parte real aproximada e o coeficiente imaginário/pi exato. Limites didáticos, não universais. Python3, biblioteca padrão.

Execute `python3 labs/logaritmo-ramos/branches.py`; testes `python3 -m unittest discover -s labs/logaritmo-ramos -t .` na raiz do protótipo. Testes verificam 65 ângulos/cortes, produto, caminhos por diferenças centrais independentes e contratos. Quadratura finita não demonstra a integral ou a inexistência de primitiva global; essas conclusões têm provas nas notas.

Fonte pública consultada parcialmente em29/10/2026: [NIST DLMF §4.2(i)](https://dlmf.nist.gov/4.2.i), equações4.2.1–4.2.7: domínio, argumento, valores gerais e limites no corte. A fonte também descreve uma definição fechada; estas notas fixam explicitamente o ramo aberto. Sem copiar figura ou exercícios. Ahlfors3/Churchill2 e demais edições do programa continuam sem exemplar nominal confirmado conforme busca anterior; não foram presumidos lidos, equivalentes ou ausentes em todo o acervo. Não houve nova leitura de Apostol ou programa oficial neste bloco. Exemplos, argumentos, desenho e código próprios.

Pendente: sequência de análise complexa completa, continuação analítica, raízes e potências gerais, provas dos teoremas integrais e revisão pessoal. Sem afirmar que resíduos ou todos esses tópicos foram ministrados na turma.
