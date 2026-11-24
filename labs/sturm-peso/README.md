# Sturm–Liouville com peso — rascunho original

29/10/2026. Material com apoio de IA para revisão de Jhuann, não resultado experimental, domínio certificado ou teoria espectral completa.

## Reprodução

Da raiz do protótipo:

```sh
python3 -B -m labs.sturm-peso.modes
python3 -B -m unittest discover -s labs/sturm-peso -t .
```

Modelo adimensional p=1+x,q=0,w=1/(1+x),x em[0,1],Dirichlet nos dois extremos. Nenhum material, unidade física ou medição inferida. modes.py usa apenas biblioteca padrão,modos1…12,x real finito0…1,flags bool explícitas. Simpson pede número par de painéis2…65536. Limites de execução didáticos,não limites matemáticos do espectro. O painel antigo do site continua sendo coeficientes constantes;snippet/desafio anteriores preservados. Não é solver geral de autovalores por malha.

## Teoria e exemplos originais

### Do caso inicial ao problema com peso

As três seções iniciais fixam o ponto de partida p=w=1 e q=0. Agora considere um intervalo finito [a,b], p real com derivada contínua, q e w reais contínuos, p>0 e w>0 inclusive nos extremos. Impomos condições homogêneas separadas reais; a dedução principal usa Dirichlet y(a)=y(b)=0. A expressão ℒy=−(py′)′+qy aparece na equação generalizada ℒy=λwy. Uma autofunção deve ser não nula e satisfazer tanto a equação quanto o domínio de contorno. Casos com p ou w singular ou nulo na borda exigem outra análise.

### O peso liga o operador ao produto interno

Defina A=w⁻¹ℒ e ⟨f,g⟩_w=∫_a^b w(x)f̄(x)g(x)dx, linear no segundo argumento. Então Ay=λy é a versão de autovalor usual e ⟨f,Ag⟩_w=∫f̄ℒg. Não se deve trocar A por ℒ mantendo esse mesmo produto e assumir a mesma propriedade. O peso é determinado por esse problema: pode representar, após a escolha de unidades de um modelo, densidade de massa ou capacidade térmica. Aqui trabalhamos apenas com funções adimensionais prescritas, sem identificar material real.

### Integrar por partes expõe o que as bordas precisam fazer

Para funções suaves, duas integrações por partes dão ⟨f,Ag⟩_w−⟨Af,g⟩_w=[p(f̄′g−f̄g′)]_a^b. Os termos de q se cancelam por q real. Se f e g obedecem ao mesmo Dirichlet homogêneo, o termo de borda desaparece. Condições reais separadas do tipo αy+βpy′=0, com α e β não simultaneamente nulos em cada extremo, também o anulam por proporcionalidade. Isso demonstra simetria no domínio de teste escolhido; identificar o domínio do adjunto e provar auto-adjunticidade é uma etapa funcional que não fazemos aqui. Uma expressão diferencial sozinha não garante essa conclusão.

### Realidade e ortogonalidade podem ser deduzidas diretamente

Sob Dirichlet, multiplicar ℒy=λwy por ȳ e integrar fornece λ=∫(p|y′|²+q|y|²)dx / ∫w|y|²dx. O denominador é positivo e o numerador real, portanto λ é real. Para dois modos, a identidade de borda dá (λ_n−λ_m)⟨y_m,y_n⟩_w=0. Se os autovalores são distintos, os modos são ortogonais nesse peso. A prova não afirma que duas autofunções de um autovalor repetido já sejam ortogonais nem demonstra completude ou existência de todos os modos.

### Real não significa automaticamente positivo

Se q≥0 e o contorno é Dirichlet, o numerador é positivo para qualquer autofunção não nula: derivada identicamente zero faria y constante, e as bordas a tornariam zero. Logo λ>0 nesse recorte. Com Neumann, o modo constante pode existir e ter λ=0 quando q=0. Se q puder ser negativo, o sinal muda: −y″−2y=λy em [0,π], Dirichlet, admite y=sin x e λ=−1. Não se deve aplicar a cota positiva sem suas hipóteses. Esse exemplo de contraste tem outro q e intervalo, não é o laboratório variável abaixo.

### Um coeficiente variável que podemos resolver por transformação

Escolha p(x)=1+x, q=0, w(x)=1/(1+x), 0≤x≤1 e y(0)=y(1)=0. Faça t=ln(1+x) e y(x)=v(t). Como dt/dx=1/(1+x), temos py′=v_t e (py′)′=v_tt/(1+x). A equação vira −v_tt=λv em 0≤t≤ln2. Não abandonamos o peso: a medida muda junto, wdx=dt. Este é um exemplo próprio da transformação, não a afirmação de que qualquer p,w pode ser eliminado apenas com esse mesmo logaritmo.

### A nova extensão do intervalo seleciona o espectro

A forma transformada tem Dirichlet nos dois extremos. A solução não nula exige λ_n=(nπ/ln2)² e y_n(x)=sin[nπln(1+x)/ln2], n=1,2,… . λ=0 dá v linear com extremos nulos e apenas solução zero; λ<0 dá a mesma impossibilidade ou contradiz o quociente positivo. O n=0 da expressão senoidal também é função zero. Os n−1 nós internos ocorrem em x_j=2^(j/n)−1, j=1,…,n−1. Para n=2 o nó é √2−1≈0,414214, não o meio geométrico x=0,5.

### Normalizar exige integrar na medida certa

Pela mudança t=ln(1+x), ∫_0^1 w y_m y_n dx=∫_0^ln2 sin(mπt/ln2)sin(nπt/ln2)dt. A identidade produto–soma dá zero para m≠n e ln2/2 para m=n. Assim a norma quadrada não normalizada é ln2/2≈0,346574; a norma é sua raiz. Defina ψ_n=√(2/ln2)y_n para ter norma 1. Multiplicar uma autofunção por constante não muda seu autovalor nem seus nós. Na variável τ=t/ln2, a medida é wdx=ln2dτ, fator que não pode ser omitido.

### Omitir o peso produz um contraexemplo verificável

Para os modos 1 e 2, o produto ponderado é zero. Já ∫_0^1 y₁y₂ dx não é zero: escreva a=ln2, x=e^(aτ)−1 e dx=ae^(aτ)dτ. A identidade seno–seno fornece (a/2)∫_0^1 e^(aτ)[cos(πτ)−cos(3πτ)]dτ. Usando a primitiva e^(aτ)[a cos(kπτ)+kπ sin(kπτ)]/[a²+k²π²], resulta −3a²/2×[1/(a²+π²)−1/(a²+9π²)]≈−0,06156079. Esse valor é diferente de zero por um efeito de medida, não por erro de arredondamento. A quadratura do laboratório apenas confere essa dedução.

### Projetar uma combinação finita mostra a função da ortogonalidade

Tome f=2y₁−y₂. Como os modos são ortogonais no peso, a projeção de f sobre y₁ é ⟨y₁,f⟩_w/‖y₁‖²_w=2. A norma quadrada de f é (4+1)ln2/2=5ln2/2. Se ficar só com 2y₁, o resíduo −y₂ tem norma quadrada ln2/2. Não precisamos de uma hipótese sobre troca de soma infinita e integral: a combinação aqui é finita. A expansão de uma função arbitrária, seus sentidos de convergência e completude do sistema continuam como desenvolvimento posterior.

### Modos e taxas precisam do sinal da equação de evolução

Na equação adimensional w u_t=(pu_x)_x, q=0 e bordas fixas nulas, u_n(x,t)=y_n(x)e^(−λ_nt) resolve a dinâmica; o sinal negativo produz decaimento. Para a onda w u_tt=(pu_x)_x, a frequência angular é √λ_n nas unidades desse modelo. Um autovalor não é automaticamente uma frequência: depende de qual derivada temporal foi especificada. Nenhum tempo físico, densidade material ou unidade experimental foi estimado neste recorte.

### O laboratório confere identidades, não prova um teorema geral

A figura e o código usam p=1+x,w=1/(1+x) e modos 1…12; a simulação anterior continua sendo o caso de coeficientes constantes. Conferimos nós fabricados pela transformação, integrais ponderadas e não ponderadas, quociente energético e resíduo por diferenças conservativas no x original. Quadratura e diferenças têm erros distintos; valores pequenos de resíduo em uma malha não demonstram domínio funcional, completude ou correção de um material real. Problemas singulares, espectros contínuos, operadores não auto-adjuntos e revisão pessoal seguem pendentes.

## Verificações e seus limites

Seis métodos:27 zeros e21 antinós para modos1…6;matrizesGram4x4 com/sem normalização e contraexemplo sem peso fechado;27 resíduos conservativos em9 combinações modo/ponto com três passos;quocientes energéticos e12 derivadas por diferenças centrais;forma bilinear de borda em polinômios que não são autofunções,integrada independentemente por Gauss3pontos e caso semDirichlet;contratos. Contagens internas não são métodos adicionais.

A transformação fornece exatamente os zeros,autovalores e normas. No x original,a quadratura confere essas referências com tolerância declarada no teste. O resíduo usa apenas amostras do modo e fluxos por diferença,sem reutilizar derivative();o refinamento aproximadamente quadrático é evidência de consistência nesse recorte,não cota global. A fórmula fechada do produto sem peso vem de produto–soma e primitiva exponencial,trabalho original independente da quadratura. Não há validação experimental,screenreader ou garantia de teoria funcional a partir de ponto flutuante.

## Fontes e alcance

- [NIST DLMF§1.13(viii)](https://dlmf.nist.gov/1.13#viii),consulta textual parcial29/10/2026,Eqs.1.13.26–1.13.31:forma,contornos e transformação. A fonte usaρ para peso e w para função transformada; aqui w é peso e v é função transformada. Não confundir notações. Exemplo próprio com produto pw=1,sem copiar exemplo ou figura.
- [UVic/Lebl–Bazett,DiffyQs§6.1](https://web.uvic.ca/~tbazett/diffyqs/slproblems_section.html),consulta parcial29/10/2026 de§§6.1.1–6.1.2,hipóteses de contorno e peso. Notação r da fonte equivale a w. A fonte inclui q≥0 e sinais no seu uso restrito de regular; aqui regular não é sinônimo de operador positivo,como mostra o exemplo q negativo. Fredholm e séries infinitas não foram adotados como teoremas demonstrados.
- [MIT18.303,Lecture10](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/resources/mit18_303f14_lecture10/),PDFpp.1–2 consultadas textualmente29/10/2026 para domínio,bordas,Neumann e modo constante. Sem nova inspeção visual do PDF ou aula integral; não é a fonte de um exemplo variável que ela não contém.

Busca nominal autorizada encontrou Arfken/Weber em inglês e tradução portuguesa no acervo de pesquisa; arquivos não inspecionados neste bloco,edição/capítulo não verificados. Babusci e colaboradores também apareceu por nome. A presença nominal não constitui leitura ou atribuição de bibliografia oficial. Este percurso é complementar e não tem código de disciplina formal ou equivalência presumida. Nenhum PDF privado ou caminho do acervo servido no site.

Auto-adjunticidade abstrata,completude,problemas singulares,operadores não auto-adjuntos e revisão pessoal permanecem pendentes. Fontes foram consultadas em recortes;deduções do exemplo,figura,código e exercícios originais.
