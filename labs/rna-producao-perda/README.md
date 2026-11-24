# Abundância de RNA: produção e perda

22/10/2026. Rascunho original para revisão de Jhuann. Recorte do tema amplo Regulação da expressão gênica de CCM0215, sem atribuir o modelo à turma ou a uma pesquisa pessoal. Pré-requisitos: abundância versus taxa, unidade de tempo, exponencial e EDO linear.

## Fontes e alcance

- Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, Artmed 2017: p.372 (PDF408), vários níveis de controle entre DNA e proteína, e bloco de estabilidade do mRNA em p.426 (PDF462), consultados parcialmente por extração local. Não se usaram tempos de vida ou dados específicos do livro como parâmetros do modelo. A extração de p.427 também foi obtida, mas não fundamenta o conteúdo redigido. A quinta edição do programa continua não confirmada; PDFs e figuras privados não distribuídos.
- [Dori-Bachash, Shema e Tirosh (2011), Coupled Evolution of Transcription and mRNA Degradation](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001106), consulta direta parcial em 22/10/2026: resumo e seção *Analysis of Transcription Rates*. A fonte relaciona produção, degradação e nível estacionário e explicita limites da inferência sob essa hipótese. Não houve leitura integral, reanálise de dados ou reprodução de resultados. O exemplo, as curvas e os parâmetros abaixo são próprios.

## Modelo, unidades e comparação

M é abundância média contínua em unidades arbitrárias u, tempo em h, produção α em u/h e coeficiente de perda δ em h⁻¹. Balanço assumido: dM/dt=α−δM, α≥0, δ>0. Solução própria por subtração do estacionário: M*=α/δ; M(t)=M*+(M₀−M*)exp(−δt). A implementação equivalente com expm1 evita cancelamento próximo de t=0.

Referência α₀=2 u/h, δ₀=0,2 h⁻¹, razão 10 u. Comparação para r=1..4:

- A: α=2r, δ=0,2, M*=10r.
- B: α=2, δ=0,2/r, M*=10r.

M₀ é condição inicial livre, 0..50 em passos de cinco. Somente o padrão M₀=10 coincide com o estacionário de referência; não se presume que todas as outras escolhas sejam um estado anterior estacionário. Parâmetros são mantidos constantes para t≥0. Em r=2, M₀=10 e t=10: A≈18,646647 u, B≈16,321206 u, ambas com estacionário 20 u.

Uma observação estacionária identifica a razão no modelo, não os dois parâmetros. Se M₀=M*, ambas as trajetórias são planas e não se separam mesmo ao longo do tempo neste desenho ideal. Fora do estacionário, a aproximação tem escala 1/δ. Em ln(2)/δ a distância ao estacionário cai pela metade; sem produção, isso é também meia-vida da abundância. Com produção, não é necessariamente metade da abundância total.

## Pergunta, observação e limites

Pergunta proposta: uma diferença de abundância é compatível com produção, perda ou ambas? Observável: nível de RNA em uma escala e ao longo de um tempo definidos. Um sinal de PCR ou medida de abundância não fornece diretamente taxas de produção/perda. Resolver um balanço conhecido não equivale a estimar parâmetros em dados. Ruído, normalização, resolução temporal, desenho e validação de evidências adicionais continuam necessários.

O modelo exclui processamento, compartimentos, divisão/diluição, proteína, flutuações e retroalimentação. A perda efetiva real pode conter outros termos. Não cobre controles experimentais de uma medida de RNA, modelos estocásticos ou identificabilidade estatística geral. Não são dados biológicos, unidades de moléculas/célula, TPM, Cq ou RNA-seq. Não há procedimento experimental prescrito.

## Verificação e apresentação

Quatro testes Python: 1364 estados comparados com referência Decimal de 65 dígitos em duas hipóteses; integração RK4 independente em 72 trajetórias; família estacionária, limites/positividade, direção da aproximação e meia redução da distância; contratos. `reference.json` reúne 80 estados, comparados com JavaScript em taxas, estacionário, nível, derivada e meia-vida. A solução fechada não é usada como seu próprio verificador numérico.

Tese visual: uma comparação de trajetórias em eixos comuns. A azul contínua e B preta tracejada; marcadores acompanham o instante escolhido e os valores numéricos ficam no relatório. Conteúdo: pergunta → balanço → contraexemplo de taxas → trajetórias → Python/exercícios. Fator altera as duas hipóteses, início testa aproximação ascendente/descendente e instante muda só o destaque. Sem animação que sugira aquisição de dados.

Revisão pessoal pendente. Próxima entrega: explicar as duas taxas, o caso plano e a diferença entre meia-vida e tempo de resposta; propor evidência adicional com limites. Diversidade, descobertas e seminários permanecem lacunas da disciplina, e regulação ainda é parcial.
