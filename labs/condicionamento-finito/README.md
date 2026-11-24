# Condicionar num espaço finito

Rascunho didático original, 21/10/2026, pendente de revisão de Jhuann. Modelo sintético; não contém dados de pesquisa ou de clientes.

Quatro regiões disjuntas: a=A∩B, b=A∩Bᶜ, c=Aᶜ∩B, d=Aᶜ∩Bᶜ. As contagens representam átomos equiprováveis, e não quatro regiões equiprováveis. Se n=a+b+c+d>0, as massas são as contagens divididas por n. Condicionar em B conserva somente as regiões a,c e renormaliza por a+c. A tabela mostra também a massa zero fora de B.

## Exploração

- Padrão (2,1,1,2): P(A|B)=2/3. Recupera o exemplo do dado justo.
- (2,1,3,4): P(A|B)=2/5, mas P(B|A)=2/3.
- (1,1,1,1): independência, com produto de marginais igual à interseção.
- (0,2,3,0): disjunção de eventos positivos, logo dependência.
- a=c=0: condicionamento em B sem denominador positivo, explicitamente não definido.
- Tudo zero: não existe distribuição para normalizar.

O critério de independência usa a n=(a+b)(a+c), sem tolerância flutuante. O painel limita cada contagem a dez; a API JS aceita inteiros seguros entre zero e um milhão, preservando os produtos exatos neste intervalo. A rotina Python usa inteiros e Fraction, sem esse limite superior. Não há inferência de frequências populacionais nem simulação aleatória.

Na raiz do protótipo:

```sh
python3 labs/condicionamento-finito/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes locais: enumeração independente de átomos nas 256 tabelas com células 0–3; produto, total, Bayes e complemento nas 81 tabelas estritamente positivas com células 1–3; invariância por escala e troca de eventos em 81 tabelas; singularidades, independência e entradas inválidas. Arquivo reference.json: 81 tabelas com células em {0,1,3}, incluindo total zero, cruzadas com JavaScript. Tabelas de total zero não recebem uma conclusão de independência.

## Fontes consultadas parcialmente

1. Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição atualizada, 2010/1ª reimpressão 2011, §2.2. Páginas impressas 54–59 (PDF 69–74 do exemplar privado): condição, produto, independência, partição e Bayes. Página impressa 54 inspecionada visualmente.
2. Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, Edusp, 2006, §1.3. Páginas impressas 26–30 (PDF 18–20, páginas duplas) e 35 (PDF 22): construção por restrição/normalização, produto, total, Bayes e independência. PDF 20 inspecionado visualmente; a página vizinha 31 aparece na imagem, mas não é referência temática desta aula.

Nos dois livros, o caso P(B)=0 recebe a convenção P(A|B)=P(A), com comentário sobre outras escolhas. Aqui esse caso retorna None/null: a extensão não é consequência do quociente e deve ser distinguida de condicionamento com massa positiva. A diferença é explícita na aula e no simulador. Não se reproduzem exemplos, exercícios, figuras ou páginas dos livros. Os PDFs privados não são distribuídos.

A aula não cobre condicionais regulares, densidades condicionais ou construção por σ-álgebras. Independência condicional é apenas diferenciada da independência sem condição; a demonstração finita não prova independência num sistema físico real. Faltam esses aprofundamentos e a revisão pessoal para ampliar o percurso.


## Continuação: sequência sem reposição — 22/10/2026

A aula `probabilidade-condicional` ganhou duas seções, quatro exercícios próprios e um desafio executável sobre retiradas sem reposição. São 17 seções e 16 exercícios; a demonstração interativa de quatro regiões permanece disponível. Exemplo original: três vermelhos e dois azuis; primeira marginal3/5, condicional após vermelho1/2, conjuntaRR3/10. Marginal da segunda continua3/5 por probabilidade total; isso não implica independência. Exatamente uma vermelha tem massa3/5; com reposição independente, RR muda para9/25.

`sequential.py` multiplica probabilidades de cores com contagens atualizadas. Caminho impossível retorna conjunta zero antes de qualquer condicional posterior indefinida. Sequência vazia tem massa um; mais retiradas que objetos e símbolos/contagens inválidos são rejeitados. Não é modelo de mecanismo físico, simulação aleatória ou evidência pessoal de domínio.

Referências reconferidas por extração local: Magalhães e Lima, Noções7, §2.2/pp.54–59; Magalhães, PVA2, §1.3/pp.26–30. Regra do produto e probabilidade total orientam a construção, sem copiar os exercícios dos livros; permanece válida a nota anterior sobre a convenção de condicionamento em massa zero. Não houve leitura integral dos capítulos. A convenção do laboratório e os demais limites permanecem explícitos.

Quatro testes novos: enumeração independente de objetos distintos até oito objetos e três retiradas; partição por todas as sequências e troca de cores; condicionais/dependência; contratos e caminhos impossíveis. Verificação final e próxima ação registradas após os testes.


Verificação final deste bloco:558 testes Python aprovados, incluindo os quatro novos; suíte JavaScript e324estruturas MathML aprovadas. No navegador, respostas3/10 e0,36 aceitas nos novos exercícios;390px sem transbordamento horizontal, console sem erros observados e viewport restaurado. [Prévia móvel](condicional-sequencial-mobile.jpg). Catálogo459aulas/2008exercícios; nenhum curso declarado completo. Próximo aprofundamento sugerido neste tema: construir um contraexemplo finito de independência que desaparece após condicionamento, com tabela e justificativa. Revisão pessoal de Jhuann pendente. Saldo semanal consultado após o bloco:91%; parada operacional65%.


## Continuação: independência sob seleção — 22/10/2026

A aula `probabilidade-condicional` agora tem 20 seções e 20 exercícios. Acrescentadas três seções e quatro exercícios originais: quatro pares binários equiprováveis, A=primeira coordenada 1, B=segunda coordenada 1, C=pelo menos um 1. Originalmente P(A∩B)=1/4=P(A)P(B). Dado C, a conjunta é 1/3 e o produto das marginais é 4/9; P(A|B∩C)=1/2 difere de P(A|C)=2/3. No complemento, ambos os eventos têm massa zero e são independentes. Não se infere causalidade nem se afirma que todos os filtros induzem dependência.

Fontes locais reconferidas parcialmente: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §2.2, pp. 54–59 (PDF 69–74); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, §1.3, p. 35 (PDF 22, página dupla), definição de independência condicional. A extração do primeiro PDF emitiu avisos de fluxo; os trechos conceituais usados ficaram legíveis e foram conferidos no texto. A página dupla do segundo inclui também p. 34, que não fundamenta este exemplo. Não houve leitura integral, transcrição de exemplos dos livros ou distribuição dos PDFs. A convenção de condicionamento em massa zero permanece distinguida da razão para massa positiva.

`labs/condicionamento-finito/selection.py` aceita quatro pesos inteiros não negativos e quatro seletores booleanos; normaliza apenas os átomos retidos. Rejeita modelo de massa total zero; retorna None para seleção de massa zero e para a razão adicional com denominador zero. Compara independência por frações exatas. Quatro testes novos: enumeração independente de átomos nas 80 tabelas não nulas com pesos em {0,1,2}, cruzadas com 16 seleções (1280 configurações); contraexemplo e complemento; invariância por escala; contratos e condições nulas. Código sintético, sem dados pessoais, físicos ou de clientes.

Verificação: 582 testes Python aprovados; suíte JavaScript com 241 demonstrações/723 cenários e comparações adicionais aprovada; 331 estruturas MathML aprovadas. No navegador, respostas 1/3 e 4/9 aceitas nos novos exercícios. Tela de 390 pixels sem transbordamento horizontal, console sem erros observados, viewport restaurado. Prévias `condicional-selecao.jpg` e `condicional-selecao-mobile.jpg`. Catálogo: 463 aulas/2070 exercícios, todos rascunhos pendentes de revisão pessoal; nenhuma disciplina declarada completa.

Próxima ação neste tema: construir o exemplo inverso — uma mistura de dois grupos independentes internamente, mas dependentes no agregado — usando probabilidade total e distinguindo descrição estatística de causalidade. Densidades condicionais e condicionais regulares permanecem pendentes. Saldo semanal consultado após implementação: 90%; parada operacional em 65%.


## Continuação: mistura de componentes produto — 22/10/2026

A aula `probabilidade-condicional` passa a 23 seções e 24 exercícios: três seções e quatro exercícios originais sobre independência em cada grupo e dependência no agregado. Exemplo sintético: G uniforme em {0,1}; marginais internas 1/4 e 3/4 para os dois eventos, independentes dado cada grupo. Tabelas por grupo (9,3,3,1)/16 e (1,3,3,9)/16, na ordem (A,B)=(0,0),(0,1),(1,0),(1,1). No agregado, conjunta 5/16, marginais 1/2, diferença 1/16, P(A|B)=5/8. Não é uma amostra real nem uma demonstração de causalidade ou de inversão de tendências.

Derivação apresentada: com componentes produto, a conjunta menos o produto das marginais vale λ(1−λ)(p₁−p₀)(q₁−q₀). São explicitados a expansão algébrica, sinais, marginais iguais e componentes de peso zero. Sem independência dentro das componentes, a identidade não se aplica nesta forma. Condicionais no grupo ausente não são identificáveis.

Referências temáticas reconferidas no texto extraído local já disponível: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §2.2, pp. 58–59, partição e probabilidade total (PDF 73–74); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, §1.3, p. 35 (PDF 22), independência e independência condicional. Consulta parcial, não leitura integral; exemplo, derivação aplicada e exercícios próprios. PDFs e suas páginas permanecem privados.

Laboratório `mixture.py`: parâmetros racionais ou inteiros em [0,1], distribuição exata da mistura, marginais, conjunta, diferença, independência e condicional com massa positiva. Rejeita floats, bools e valores inválidos; usa None para razões e grupos de massa zero. Quatro testes novos: 3125 configurações comparadas com enumeração independente de 64 átomos; exemplo e associação de sinal oposto; troca dos grupos/marginal igual; contratos e grupos vazios. Não há amostragem aleatória nem inferência a partir de dados.

Verificação: 586 testes Python aprovados; suítes JavaScript e 331 estruturas MathML aprovadas. Após abreviar a fórmula exibida para leitura móvel, 12 testes de catálogo novamente aprovados. No navegador, 5/16 e 0,625 aceitos; 390 px sem transbordamento horizontal, console sem erros observados e viewport restaurado. Prévia móvel atualizada: `condicional-mistura-mobile.jpg`. Catálogo 463 aulas/2074 exercícios, rascunhos para revisão pessoal; nenhuma disciplina completa. Saldo semanal após bloco 90%, parada em 65%.

Próxima ação global: retomar o recorte de controle de erro e passo adaptativo no roteiro auditado de Computação IV, consultando o corpo de Burden 10, §§5.4–5.5; distinguir duplicação de passo RK4 de RK–Fehlberg. Em probabilidade, permanecem pendentes uma visualização comparativa de misturas e o desenvolvimento de condicionais contínuas, com revisão pessoal dos recortes já preparados.

## Visualização comparativa — 22/10/2026

A aula complementar `mistura-independencia` apresenta duas componentes produto e o agregado em barras com a mesma escala e frações exatas. Preserva o painel anterior `conditionalFinite`. Veja [roteiro e fontes](VISUALIZACAO_MISTURA.md). Dez seções, oito exercícios, exemplo Python e comparação de 245 referências racionais com JavaScript; 3125 configurações também enumeradas por 64 átomos em JavaScript. Parâmetros de quartos permitem sinais positivo/negativo, igualdade de uma marginal, grupo ausente e P(B)=0. Material sintético, pendente de revisão pessoal.

## 22/10/2026 — Evidências sucessivas e duplicação de informação

`probabilidade-condicional` passa a 29 seções/30 exercícios (seis de cada novos). Modelo próprio: P(H)=1/10, taxas individuais 4/5 dado H e 1/5 dado Hᶜ para ambos os sinais. Independência dentro das duas hipóteses dá posterior 16/25 após dois sinais; cópia S₂=S₁ preserva 4/13; interseções mínimas admissíveis 3/5 e zero dão posterior um no modelo ideal. Mesmas marginais não determinam a conjunta. Derivadas a regra do produto com o novo condicionamento e as restrições max(0,2t−1)≤j≤t. Nenhum dado observado ou claim de detector real.

Referências reconferidas parcialmente no corpo: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §2.2, pp.56–59 (PDF71–74), independência, árvore, partição e Bayes; Magalhães, Probabilidade e Variáveis Aleatórias, 2ª ed., §1.3, pp.34–35 (PDF22, página dupla), Bayes e independência condicional. O PDF de Noções emitiu avisos de fluxo, mas os trechos usados estavam legíveis na extração. Derivação, cenários, código e exercícios originais; não transcritos dos livros. Não foi feita leitura integral nem distribuído material privado.

`labs/condicionamento-finito/repeated.py` constrói oito massas com Fraction, valida marginais/interseções e retorna None para razões com denominador zero. Quatro testes: exemplos, enumeração independente de conjuntos equiprováveis, identidade da cópia e contratos/zeros. 641 testes Python e 361 estruturas MathML aprovados. Catálogo: 474 aulas/2238 exercícios em rascunho. Navegador: respostas 16/25 e 4/13 conferidas; celular390px sem transbordamento horizontal, console sem erros observados, viewport restaurado. Prévias `condicional-dois-sinais.jpg` e `condicional-dois-sinais-mobile.jpg`. Revisão pessoal pendente; nenhuma disciplina concluída.

Próxima ação neste eixo: revisar os três modelos e explicar em palavras os denominadores antes de preparar uma árvore visual de atualização sequencial. Saldo semanal conferido 86%; parada operacional em65%, piso60%.

## 22/10/2026 — Painel de evidências sucessivas

O turno anterior foi progresso: seis seções/exercícios e laboratório exato registrados. Neste bloco, a mesma aula ganhou o painel `repeatedEvidence`, preservando `conditionalFinite`. A biblioteca agora aceita `additionalSimulations` opcionais; nenhuma outra aula mudou de painel. Sem acrescentar aula/exercício: catálogo permanece 474/2238, aula 29 seções/30 exercícios, rascunhos para revisão.

Controles: base em décimos 0..10 e três modelos (independência condicional em ambos os grupos, cópia, interseções mínimas). Etapas mostram base, posterior após S₁ e após S₁∩S₂; barras em escala comum, tabela de massas e condicionais do segundo ramo. Com base zero e interseções mínimas, o evento conjunto tem massa zero e a razão é não definida. Condicionais em grupos ausentes não são apresentadas como identificáveis. Denominador comum250 mantém massas inteiras no JavaScript; 33 configurações comparadas com Fraction no Python já verificado por enumeração independente.

Fontes: continuação do recorte parcial de Magalhães registrado no bloco anterior (Noções7 §2.2 pp.56–59; PVA2 §1.3 pp.34–35). Não houve nova consulta externa, leitura integral ou reprodução de figuras/exemplos. Painel e números são próprios, sem dados ou experimento pessoal.

Verificação: 641 testes Python; suíte JS com254 modelos/762 cenários básicos e comparações adicionais, incluindo33 estados de evidência; 361 fórmulas MathML. Teclado conferiu cópia (posterior permanece4/13) e evento conjunto nulo.390px sem overflow horizontal; controles finais em coluna e prévias desktop/móvel inspecionadas. Console sem erros observados. Arquivos `evidencias-sucessivas.jpg` e `evidencias-sucessivas-mobile.jpg`. Saldo86%, parada65%.

Próxima ação global: alternar para geometria/isomeria de coordenação em QuímicaIII, lendo antes o corpo pertinente de Miessler. Revisão pessoal deste painel segue pendente; nenhuma disciplina completa.
