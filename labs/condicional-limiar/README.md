# Condicionamento com limiar — laboratório original

X~Uniforme[0,1]; Y=max(0,X−a), 0<a<1 conhecido. Grandezas adimensionais. Modelo determinístico sintético, sem ruído, arredondamento ou ajuste a dados. Não é validação de sensor real.

- Massa P(Y=0)=a; parte contínua com densidade 1 em (0,1−a). A conjunta não possui densidade ordinária em relação à área.
- Em Y=0, posterior uniforme [0,a]. Para 0<y<1−a, versão concentrada em a+y. O extremo marginalmente nulo y=1−a retorna None; fora do suporte gera ValueError.
- Faixa Y≤b inclui o átomo; 0<Y≤b o exclui. 0<b≤1−a.
- Esperança iterada e variância total somam massa e integral. Risco residual a³/12 sob perda quadrática e modelo conhecido; sem treinamento.
- A API aceita int/Fraction, rejeita bool/float. A figura é original e acessível.

## Fontes e proveniência

Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2 pp.54–55/PDF69–70: definição por eventos e produto. Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §3.2 pp.128–129/PDF69: distribuição condicional por eventos; §5.3 pp.260–265/PDF135–137: esperança condicional, esperança iterada e variância. Recortes textuais privados parcialmente reconferidos em 27/10/2026; páginas duplas/intercaladas em PVA. Não houve nova inspeção visual ou leitura integral. Os livros não são distribuídos. O sensor misto, deduções, exercícios e verificações são próprios, sem atribuí-los a um exemplo dos autores.

## Verificação

Na raiz do protótipo: `python3 -m unittest discover -s labs/condicional-limiar -t .`.
Os testes confrontam a lei observada com pré-imagens, momentos de faixa por integração polinomial, esperança iterada por quadratura independente, variância total e contratos. Verificação computacional não substitui revisão conceitual pessoal.

Próximo passo: reconstruir as três mensagens com a=1/2 e explicar a perda de informação. Ruído adicional, limiar desconhecido, dados reais, leitor de tela e revisão por Jhuann pendentes.

Conferência em27/10/2026: cinco testes locais e14 de catálogo aprovados;802 fórmulas estruturais. Interface390px: rejeição3/4/aceite3/8 pelo Enter e alternativa sobre densidade conferidas; figura inspecionada, largura390px e console sem erros. Captura na raiz: `condicional-limiar-mobile.jpg`.


## 27/10/2026 — probabilidade condicional com resolução finita

Aula `pe-condicional-limiar` ampliada de 12 seções/10 exercícios para 17/14, preservando o modelo ideal e acrescentando explicitamente uma observação por faixas. Com a=1/2, duas faixas de Y de largura1/4 dão pré-imagens [0,3/4) e [3/4,1], médias3/8 e7/8 e risco7/192. Quatro faixas dão risco1/48; o limite é1/96, devido ao limiar. Deduções de normalização, esperança iterada, variância total, minimização quadrática e garantia média sob refinamentos encaixados. Código de faixa não é leitura exata nem arredondamento ao mais próximo. Não há dados reais, ajuste de parâmetros ou validação de sensor.

Referências parcialmente reconferidas por extração textual: Magalhães e Lima, Noções de Probabilidade e Estatística,7ª ed.,§2.2 pp.54–55/PDF69–70; Magalhães, Probabilidade e Variáveis Aleatórias,2ª ed.,§3.2 pp.128–131/PDF69–70. Fundamentos de condicionamento por eventos e lei da probabilidade total. O risco quadrático retoma a consulta parcial anterior de PVA§5.3 pp.260–265/PDF135–137, sem nova leitura dessa seção nesta extensão. PDF de PVA com páginas duplas e colunas intercaladas. Sem leitura integral, nova inspeção visual dos livros ou distribuição de exemplares privados. Exemplo, deduções, código e exercícios próprios.

Verificação:14 testes do catálogo e8 do laboratório aprovados (5 anteriores e3 novos). Novos testes confrontam o risco com integração independente de Simpson, em15 combinações de limiar/resolução, além de esperança iterada, refinamentos encaixados, limites de mensagens e contratos. Exemplo executável `labs/condicional-limiar/resolution.py` conferido;819 estruturas MathML no catálogo. No navegador390px, exercício11 rejeitou3/4 e aceitou7/8 pelo Enter; documento390/390px, console sem erros observados. Texto inspecionado na captura `condicional-resolucao-mobile.jpg`. Windows real e leitor de tela não testados; revisão pessoal pendente.

Probabilidade:25 aulas/313 exercícios. Global51 trilhas,550 aulas/4453 exercícios,191 introduções curtas; inclui elaboração de ComputaçãoI já existente no início desta extensão. Contagens não certificam curso completo nem domínio pessoal. Próxima ação20min: desenhar as duas pré-imagens e reconstruir7/192, depois comparar com quatro faixas e1/96. Depois incorporar dúvidas antes de acrescentar ruído ou parâmetros desconhecidos. Saldo semanal79%; parada operacional65% preservada.


## 27/10/2026 — distribuição inicial e posterior no sensor com limiar

Aula `pe-condicional-limiar` ampliada de 17 seções/14 exercícios para 21/18. Mantido o modelo uniforme e explicitamente separada a extensão com f_X(x)=2x em [0,1], mesmo sensor ideal Y=max(0,X−a). Na leitura zero: evidência a², densidade 2x/a² no intervalo [0,a], média 2a/3, variância a²/18; risco médio a⁴/18. Para a=1/2: evidência1/4, média1/3, variância1/72, risco1/288. A pré-imagem permanece igual, mas os pesos mudam. Normalização da lei mista, esperança iterada e variância total reconstruídas. Comparar riscos de leis iniciais diferentes não prova superioridade do sensor. Não houve ajuste a dados nem escolha empírica da lei.

Fontes privadas parcialmente reconferidas por extração textual: Magalhães e Lima, Noções de Probabilidade e Estatística,7ª ed.,§2.2 pp.54–55/PDF69–70; Magalhães, Probabilidade e Variáveis Aleatórias,2ª ed.,§3.2 pp.128–129/PDF69,§5.3 pp.260–263/PDF135–136. Fundamentos de condicionamento por eventos e esperança iterada; páginas duplas/intercaladas em PVA. Sem leitura integral, nova inspeção visual ou reprodução dos livros. Sensor e comparação de leis são exemplos originais, não exercícios atribuídos aos autores.

Verificações: `python3 labs/condicional-limiar/prior.py` compara normalização, momentos condicionais, esperança iterada e variância total com integração independente de Simpson em19 limiares; exemplo racional e contratos conferidos.14 testes de catálogo aprovados após regenerar a cobertura (primeira execução sinalizou apenas o retrato derivado desatualizado);835 estruturas MathML conferidas. Na interface390px, exercício da média rejeitou1/4 e aceitou1/3 pelo Enter; largura390/390px, console sem erros observados. Texto inspecionado na captura `condicional-prior-mobile.jpg`. Windows real, leitor de tela e revisão pessoal pendentes.

Probabilidade:25 aulas/317 exercícios. Global51 trilhas,555 aulas/4609 exercícios,182 introduções curtas; inclui a aula de cascas cilíndricas já existente no início deste bloco, cuja revisão própria não foi assumida aqui. Contagens não certificam cobertura integral ou domínio. Próxima ação20min: reconstruir a posterior dado zero nas duas leis e explicar por que a pré-imagem não basta para determinar probabilidades. Depois revisar dúvidas e decidir se cabe estudar limiar desconhecido ou retomar lacunas de outras disciplinas. Saldo semanal77%; parada operacional65% preservada.


## 27/10/2026 — probabilidade condicional com limiar desconhecido

A pedido de Jhuann, retomada a aula `pe-condicional-limiar`: de 21 seções/18 exercícios para 26/24, preservando as extensões anteriores. Nesta extensão separada, X volta a ser uniforme [0,1]; A independente vale 1/4 ou 1/2 com probabilidades iguais. Uma única leitura Y=max(0,X−A). Não é ruído aditivo, inferência com dados ou aprendizagem de um limiar fixo a partir de observações repetidas.

Zero tem massa 3/8; os pesos posteriores de A são 1/3 e 2/3. X dado zero tem média 5/24 e variância 11/576. Para 0<y<1/2, uma versão construída por faixas interiores dá dois valores y+1/4 e y+1/2 equiprováveis: média y+3/8, variância 1/64. Para 1/2<y<3/4 só o limiar 1/4 é compatível; variância zero. Fronteiras marginalmente nulas não especificadas no código. Normalização da lei mista e esperança iterada conferidas; risco sem A: 23/1536, com A informado: 3/512. Diferença média 7/768, sem garantia por observação nem validação de instrumento real.

Fontes: reconferência textual parcial nos acervos já extraídos de Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2 pp.54–55 e 59 (PDF69–70 e 74); Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §3.2 pp.128–129 (PDF69) e §5.3 pp.260–263 (PDF135–136). Fundamentos de Bayes, condicionamento por eventos/faixas e esperança condicional. PVA tem páginas duplas com extração intercalada. Sem nova inspeção visual dos livros, leitura integral ou cópia de exemplos dos autores. Modelo, deduções, código e exercícios originais.

Verificação: `python3 labs/condicional-limiar/unknown.py` aprovado. Posteriores confrontadas com pré-imagens de 94 pequenas faixas interiores; normalização, momentos, exemplos e contratos conferidos por Fraction. Risco confrontado com integração de Simpson de polinômios no espaço original (A,X), independente da soma de variâncias condicionais; não simula dados reais. 14 testes de catálogo aprovados, 836 estruturas MathML conferidas. No navegador a 390px, exercício posterior rejeitou 1/2 e aceitou 2/3 via Enter; largura 390/390, console sem erros observados. Texto da extensão inspecionado em `condicional-limiar-incerto-mobile.jpg`. Windows real, leitor de tela e revisão pessoal pendentes.

Probabilidade: 25 aulas/323 exercícios; catálogo atual: 51 trilhas, 558 aulas/4735 exercícios, 173 introduções curtas. Inclui o aprofundamento de equipartição já existente no início desta retomada, cuja inspeção final não foi assumida aqui. As contagens não certificam cobertura integral nem domínio pessoal. Próxima ação de 20 min: reconstruir os pesos 1/3 e 2/3, desenhar os dois valores de X para Y=1/8 e explicar por que uma leitura exata não basta com A desconhecido. Depois incorporar dúvidas antes de ampliar o modelo. Saldo semanal antes/depois: 75%; parada operacional em 65% mantida.
