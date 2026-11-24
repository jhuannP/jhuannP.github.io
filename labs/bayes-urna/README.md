# Composição desconhecida: Bayes e previsão

## A composição fica fixa; nossa informação muda

Uma urna hipotética tem três bolas. H₁ significa uma vermelha e duas azuis; H₂, duas vermelhas e uma azul. Antes de observar cores, atribuímos P(H₁)=P(H₂)=1/2. Uma dessas composições permanece fixa durante o experimento. A distribuição prévia representa a incerteza do modelo sobre qual é ela; observar uma cor muda a informação disponível. Não estamos estimando essas probabilidades com dados reais.

## Declare o protocolo antes de usar Bayes

Retiramos bolas identificáveis, uniformemente entre as restantes, sem reposição, e registramos as cores em ordem. R₁ é primeira vermelha; R₂ é segunda vermelha. Sob H₁, P(R₁|H₁)=1/3; sob H₂, vale 2/3. Essas são verossimilhanças: probabilidades da observação sob cada hipótese. Não são as probabilidades das hipóteses depois da observação.

## A evidência soma caminhos mutuamente exclusivos

H₁ e H₂ são disjuntos e cobrem as composições admitidas. A probabilidade de observar R₁ é a soma das conjuntas: (1/2)(1/3)+(1/2)(2/3)=1/2. Esse denominador é chamado aqui de evidência: a probabilidade da observação dentro do modelo, anterior à atualização. Modelos alternativos ou outras probabilidades prévias podem dar outro resultado.

P(R₁)=1/6+1/3=1/2

## Atualizar é dividir cada contribuição pela evidência

Depois de R₁, H₂ recebe (1/2)(2/3)/(1/2)=2/3, e H₁ recebe 1/3. Os valores somam 1. A observação favorece a composição com mais vermelhas, mas não prova H₂: ambas poderiam produzir a primeira vermelha. A fórmula é a de Bayes aplicada a duas hipóteses de composição.

P(H₂|R₁)=2/3; P(H₁|R₁)=1/3

## Prever a próxima cor exige a urna restante

Após R₁, H₁ deixa zero vermelhas entre duas bolas; H₂ deixa uma entre duas. A probabilidade total dentro de R₁ usa os pesos posteriores e essas novas taxas: (1/3)×0+(2/3)×(1/2)=1/3. Usar 1/3 e 2/3 como taxas da próxima retirada esqueceria que uma bola já saiu. É preciso atualizar tanto a informação sobre a hipótese quanto o inventário condicionado.

P(R₂|R₁)=1/3

## Uma segunda vermelha elimina uma hipótese neste modelo

Sob H₁ é impossível retirar duas vermelhas sem reposição: só havia uma. Sob H₂, P(R₁∩R₂|H₂)=(2/3)(1/2)=1/3. A evidência da sequência RR é (1/2)×0+(1/2)(1/3)=1/6. Assim P(H₂|RR)=1. Isso é certeza dentro das hipóteses e do registro idealizados; não valida a composição assumida, o protocolo ou a ausência de erro de observação no mundo real. Depois de RR, a última bola é azul.

P(H₂|R₁∩R₂)=1; P(R₃|R₁∩R₂)=0

## A sequência vermelha–azul pode restaurar pesos iguais

Chame A₂ a segunda azul. Sob H₁, P(R₁∩A₂|H₁)=(1/3)×1=1/3. Sob H₂, a taxa é (2/3)×(1/2)=1/3. As duas hipóteses contribuem 1/6 para a evidência 1/3: a posterior de H₂ volta a 1/2. H₁ deixa uma azul; H₂ deixa uma vermelha. A próxima vermelha tem então probabilidade 1/2. Receber mais informação não exige que toda posterior se afaste sempre da prévia.

## Ordem registrada e contagem são observações distintas

O evento “uma vermelha e uma azul em duas retiradas” é a união disjunta de VA e AV. Cada caminho tem probabilidade 1/3 sob cada hipótese, totalizando 2/3. Com as mesmas prévias, a posterior de H₂ continua 1/2, embora a evidência seja 2/3 em vez de 1/3 para VA. Neste protocolo uniforme a ordem não muda a verossimilhança entre sequências com a mesma contagem. Essa propriedade precisa ser justificada pelo modelo; não vale para qualquer mecanismo de observação.

## Com reposição, a mesma sequência tem outra força de informação

Se cada bola retorna e as retiradas são independentes dado Hᵢ, as chances de RR sob H₁ e H₂ são 1/9 e 4/9. A evidência é 5/18, e P(H₂|RR)=(2/9)/(5/18)=4/5. Agora RR não elimina H₁. A previsão da terceira vermelha é (1/5)(1/3)+(4/5)(2/3)=3/5. Trocar o protocolo depois de observar os dados troca o problema.

Reposição: P(H₂|RR)=4/5; P(R₃|RR)=3/5

## Independência dentro de cada hipótese não garante independência na mistura

Com reposição, R₁ e R₂ são independentes dado H₁ e dado H₂ por hipótese do sorteio. Sem conhecer a composição, P(R₁)=P(R₂)=1/2, mas P(R₁∩R₂)=5/18 difere de 1/4. A composição desconhecida é informação compartilhada entre as previsões. Após uma vermelha, a chance da próxima é (1/3)(1/3)+(2/3)(2/3)=5/9. Este é também um exemplo do sentido inverso da distinção discutida na aula de independência condicional.

5/18 ≠ (1/2)(1/2); P(R₂|R₁)=5/9 com reposição

## Repetir o relato não equivale a uma nova retirada

Atualizar com R₁ e depois receber novamente o mesmo relato R₁ mantém a condição R₁∩R₁=R₁. A posterior continua 2/3. Para usar duas verossimilhanças há que observar duas retiradas, levando em conta a dependência apropriada. Mesmo com reposição, as retiradas só foram declaradas independentes dado a composição; multiplicar probabilidades marginais perde essa distinção.

## O laboratório verifica uma mistura finita, com limites explícitos

O código calcula a verossimilhança da sequência ordenada sob cada número de vermelhas, multiplica pelos pesos prévios normalizados e divide pela evidência. Só então mistura as taxas da próxima cor. Fraction conserva contas racionais exatas. Evidência zero retorna posterior indefinida; urna esgotada pode ter posterior definida, mas não há próxima retirada. Não há estimação da prévia, ruído de classificação, inferência contínua ou validação experimental. Pré-requisitos: aulas de condicionamento, Bayes e amostragem sem reposição. Próximo passo: justificar a mesma posterior usando contagens e explicar o fator combinatório que cancela.

## Exercícios originais e resoluções

Sem reposição, H₁ tem 1 vermelha em 3 e H₂ tem 2 em 3, com prévias 1/2. Quanto é P(R₁)? **Resolução:** (1/2)(1/3)+(1/2)(2/3)=1/2.

No mesmo modelo, após a primeira vermelha, quanto é P(H₂|R₁)? **Resolução:** (1/3)/(1/2)=2/3.

Após a primeira vermelha, qual é a chance da segunda vermelha sem reposição? **Resolução:** Sob H₁ a taxa restante é 0; sob H₂ é 1/2. A mistura posterior dá (1/3)0+(2/3)(1/2)=1/3.

Qual é a evidência da sequência RR sem reposição, antes de observar qualquer cor? **Resolução:** Apenas H₂ contribui: (1/2)(2/3)(1/2)=1/6.

Após RR sem reposição, quanto é P(H₂|RR)? **Resolução:** H₁ dá verossimilhança zero; toda a evidência vem de H₂.

Após uma vermelha e depois uma azul, sem reposição, quanto é P(H₂|VA)? **Resolução:** As verossimilhanças são ambas 1/3; prévias iguais permanecem iguais.

Qual é a evidência de exatamente uma vermelha nas duas primeiras retiradas sem reposição? **Resolução:** VA e AV são disjuntos, cada um com evidência 1/3; soma 2/3.

Com reposição e retiradas independentes dado Hᵢ, quanto é P(H₂|RR)? **Resolução:** As conjuntas são 1/18 e 2/9. Normalizando: (2/9)/(5/18)=4/5.

Após RR com reposição, qual é a previsão da próxima vermelha? **Resolução:** (1/5)(1/3)+(4/5)(2/3)=3/5.

Com reposição, depois de apenas R₁, quanto é P(R₂|R₁)? **Resolução:** A posterior é (1/3,2/3); a previsão é (1/3)(1/3)+(2/3)(2/3)=5/9.

Receber duas vezes o relato da mesma primeira vermelha autoriza usar a verossimilhança de duas retiradas? **Resolução:** A informação é o mesmo evento: R₁∩R₁=R₁. Duas retiradas seriam outro experimento.

Se todas as hipóteses com peso prévio positivo tornam uma sequência impossível, o código deve produzir posterior uniforme? **Resolução:** A evidência é zero. A razão de Bayes fica indefinida; é necessário rever modelo, prévia ou observação.

## Referências e limites

Fundamentos: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, p.54 e p.59 (PDF69 e PDF74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, Teorema1.4, p.30 (PDF20, página dupla). Consulta textual parcial aos recortes locais em 22/10/2026. Urnas, deduções, figura e exercícios originais; não são transcrições dos livros.

Rascunho assistido por IA; revisão de Jhuann e aplicação com aluno pendentes. Sem dados experimentais, calibração da prévia ou distribuição de PDFs. `infer(n, weights, observed, replacement=False)` aceita pesos racionais não negativos sobre o número de vermelhas. Retorna evidência da sequência ordenada, posterior e previsão. `None` na posterior indica evidência zero; `None` apenas na previsão indica urna esgotada. Não interpreta dados contínuos nem erro de cor.

Executar: `python3 -m unittest discover -s labs/bayes-urna -t .`. O teste enumera bolas identificadas para 1–5 bolas e sequências de até três retiradas, com os dois protocolos, sem reutilizar a fórmula sequencial como oráculo.

## Continuação: sequência e contagem — 26/10/2026

### Uma sequência tem menos massa que a união de suas ordens

Agora a urna tem N=6 bolas. H₂ significa K=2 vermelhas; H₄, K=4. As duas prévias valem 1/2. São três retiradas uniformes sem reposição. A sequência VVA é um evento específico. A contagem X=2 vermelhas reúne VVA, VAV e AVV, eventos disjuntos. Para K fixo, essas três sequências têm a mesma massa: os numeradores apenas permutam os mesmos fatores, e o denominador é 6×5×4. Não atribuímos probabilidades iguais a todos os rótulos de contagem.

### A verossimilhança da contagem é hipergeométrica

Para N bolas, K vermelhas e m retiradas sem reposição, todos os subconjuntos de m objetos têm a mesma chance. Há C(N,m) no total e C(K,k)C(N−K,m−k) com k vermelhas. Assim a verossimilhança da contagem, vista como função de K com k observado fixo, é essa razão. Ela é zero se k>K ou m−k>N−K. Neste bloco N≥1 e 0≤m≤N; os extremos m=0 e m=N também são tratados por contagem direta. Os livros consultados apresentam o modelo para retirada própria menor que a população.

P(X=k|K)=C(K,k)C(N−K,m−k)/C(N,m)

### O fator combinatório cancela na posterior

Uma sequência específica s com k vermelhas em m posições tem verossimilhança (K)ₖ(N−K)ₘ₋ₖ/(N)ₘ, onde (a)ⱼ=a(a−1)…(a−j+1) e (a)₀=1. Cada uma das C(m,k) ordens tem essa massa, logo P(X=k|K)=C(m,k)P(s|K). Esse fator é o mesmo para todas as hipóteses K: ao multiplicar pelas prévias e normalizar, ele cancela entre numerador e denominador. A posterior de K e a previsão da próxima cor coincidem. As evidências continuam diferentes por esse fator.

P(K|X=k)=P(K|s), se s tem k vermelhas e evidência positiva

### Exemplo: probabilidades diferentes, posterior igual

Com m=3 e k=2, sob H₂ a contagem tem massa C(2,2)C(4,1)/C(6,3)=1/5; sob H₄, C(4,2)C(2,1)/C(6,3)=3/5. A evidência é (1/2)(1/5)+(1/2)(3/5)=2/5. A posterior de H₄ é (3/10)/(2/5)=3/4. Para VVA, divida as verossimilhanças por C(3,2)=3: 1/15 e 1/5. A evidência cai para 2/15, mas a posterior continua 3/4. Após duas vermelhas e uma azul, restam zero vermelhas sob H₂ e duas entre três sob H₄; previsão=(1/4)×0+(3/4)(2/3)=1/2.

### Quando é seguro descartar a ordem?

A equivalência foi demonstrada para N conhecido, composição fixa, retiradas uniformes sem reposição e cores sem erro. Não basta dizer que ordem nunca importa: se o mecanismo muda com a posição, permite reposição seletiva ou seleciona relatos de modo dependente da composição, as ordens podem ter razões de verossimilhanças diferentes. Nesses casos precisamos explicitar o mecanismo antes de reduzir os dados a uma contagem. O código infer_count usa apenas o protocolo declarado. Enumerar exemplos confere a implementação; o argumento algébrico justifica a equivalência geral.

### Exercícios e resoluções

Quantas sequências de três cores contêm exatamente duas vermelhas? **Resolução:** C(3,2)=3: VVA, VAV e AVV.

N=6, K=2 e três retiradas sem reposição: qual a chance de exatamente duas vermelhas? **Resolução:** C(2,2)C(4,1)/C(6,3)=4/20=1/5.

Com prévias iguais para K=2 e K=4, qual é a evidência de duas vermelhas em três retiradas? **Resolução:** (1/2)(1/5)+(1/2)(3/5)=2/5.

No mesmo modelo, qual a posterior de K=4 após observar exatamente duas vermelhas em três retiradas? **Resolução:** (1/2)(3/5)/(2/5)=3/4.

No mesmo modelo de N=6, qual a evidência da sequência específica VVA? **Resolução:** Há três ordens com a mesma massa. Dividindo 2/5 por 3: 2/15.

No mesmo modelo, após duas vermelhas e uma azul, qual a chance da próxima vermelha? **Resolução:** Posteriores de K=2 e K=4 são 1/4 e 3/4. Restam taxas 0 e 2/3: previsão=1/2.

Continuação em 26/10/2026: Noções, 7ª ed., §3.3, definição3.8, p.94 (PDF109); PVA, 2ª ed., §2.3, definição2.11, p.87 (PDF48, página dupla). Consulta textual parcial aos modelos hipergeométricos; extensão aos extremos por contagem direta e dedução do cancelamento são próprias. Extração PVA com colunas intercaladas; sem leitura integral do capítulo.

`counts.infer_count(n, weights, draws, red)` retorna a evidência da contagem, posterior e previsão sem reposição. Pesos e composição têm os mesmos contratos de urn.infer. Retiradas e contagem devem ser inteiros válidos, sem bool. Evidência nula retorna posterior/previsão None; amostra esgotando a urna pode ter posterior definida mas previsão None. O código não modela seleção de relatos.


## Observação com erro: composição e cor latente — 26/10/2026

Aula `pe-bayes-urna` ampliada de 17 para 23 seções e de 18 para 24 exercícios, preservando o conteúdo anterior. Extensão original: uma retirada uniforme sem reposição, duas composições possíveis (1 ou 2 vermelhas em 3), prévias iguais e sensor com P(R|V)=4/5, P(R|Vᶜ)=1/5. O relato R é distinto da cor V. Pela partição das cores, as verossimilhanças são 2/5 e 3/5; evidência 1/2; posterior de H₂=3/5. A conjunta posterior sobre hipótese e cor removida tem pesos 4/15,2/15,8/15,1/15; P(V|R)=4/5 e previsão da próxima vermelha=2/5. Subtrair uma vermelha como se o relato fosse perfeito produz 3/10 incorretamente. A igualdade numérica entre P(V|R) e a sensibilidade é específica da prévia do exemplo. Casos perfeito, não informativo, evidência nula e urna esgotada distinguem-se.

Fontes dos fundamentos reconferidas por leitura textual parcial dos recortes locais: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, p.54 e p.59 (PDF69 e74); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, Teorema1.4, p.30 (PDF20, página dupla; colunas intercaladas na extração). Sem nova inspeção visual das páginas dos livros nem leitura integral do capítulo. A aplicação ao sensor, números, deduções, figura e exercícios são próprios. PDFs privados não distribuídos. A razão elementar exige evidência positiva; retorno None não reproduz a convenção de extensão arbitrária de Noções p.54.

`labs/bayes-urna/noisy.py`: frações exatas, uma retirada e um relato binário, taxas conhecidas e independência do sensor em relação à hipótese e próxima bola dada a cor verdadeira. Não estima taxas nem implementa relatos sucessivos. Três testes novos, com oráculo independente de bolas identificadas e cinco saídas equiprováveis do sensor para populações de1–7 bolas, 16 pares de taxas e ambos os relatos (224 configurações). Mais limites, contratos e exemplo. Os 12 testes do laboratório de urnas e 13 de catálogo passaram; 604 estruturas MathML e verificações de foco/ajuda/redimensionamento passaram. Não se repetiu a suíte de todos os outros laboratórios.

Navegador móvel390px: questão23 rejeitou3/10 e aceitou2/5 com Enter; documento390px, sem transbordamento observado. Figura conferida visualmente em `condicional-sensor-mobile.jpg`. Sem teste no Windows ou leitor de tela real neste bloco. Material em rascunho, revisão de Jhuann pendente; nenhuma disciplina completa ou domínio pessoal certificado.

Trilha complementar de probabilidade:17 aulas/213 exercícios. Catálogo:510 aulas/3439 exercícios, 244 introduções de até três seções. Próxima revisão pessoal de20min: reconstruir as quatro conjuntas e explicar por que não se pode retirar uma vermelha apenas pelo relato. Próxima preparação do tema: roteiro de estudo que articule os exemplos já existentes antes de ampliar para séries de relatos; estimação das taxas e condicionamento contínuo permanecem outros recortes. Saldo semanal após bloco97%; parada operacional65% preservada.
