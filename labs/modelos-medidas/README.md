# Modelos e medidas — hipóteses, previsões e evidências

22/10/2026. Aula `f1-modelos-medidas`: 15 seções e 12 exercícios originais, pendentes de revisão pessoal de Jhuann. Primeiro recorte de método científico; não encerra o item oficial.

## Referências consultadas

Nussenzveig, Curso de Física Básica I, quinta edição/Blucher2013, quarta reimpressão2017. Exemplar privado identificado no bloco de auditoria. Corpo consultado: páginas impressas17–19, §1.3, correspondentes aPDF18–20; páginas20–21, parte de§1.4, correspondentes aPDF21–22. P.17/PDF18renderizada e inspecionada visualmente. A leitura cobre observação/experimentação, abstração/modelos, previsões e domínio de validade, além de início da discussão de representação de medidas. Não é leitura integral do capítulo nem transcrição de exemplos, exercícios ou figuras. PDFs privados não distribuídos.

[NIST TN1297, apêndice D.1](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology), aberto em22/10/2026: terminologia para diferenciar resultado, erro, incerteza e repetição. A fonte não fundamenta chamar a faixa deste painel de intervalo de confiança; o limite determinístico é uma convenção explícita do exemplo original. Não se atribui cobertura ou probabilidade a essa faixa.

[Programa USPCCM0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0112), reconferido diretamente no bloco anterior da mesma data, item1. A versão ativa desde2024é posterior à turma de2023; a unidade não reconstitui automaticamente a aula ministrada ou o domínio de Jhuann.

## Hipóteses e dados originais

Coordenada x em metros; tempos t=(0;0,5;1;1,5;2)s. Condições iniciais x₀=0,5m e v₀=0,5m/s, exatas por hipótese. Gerador sintético:

x_dado(tᵢ)=0,5+0,5tᵢ+tᵢ²+eᵢ+b,

e=(0;0,02;−0,02;0,02;−0,02)m, fixo e determinístico. b é um deslocamento comum, selecionado emcm. Sem sorteio, instrumento, coleta física ou ruído iid presumido. Valores com b=0:(0,5;1,02;1,98;3,52;5,48)m.

Candidata: xₘ(t)=0,5+0,5t+at²/2. a=0 é velocidade constante com as mesmas condições iniciais; candidatas a inteiras0..4m/s². Não há ajuste automático ou parâmetros de posição/velocidade estimados.

rᵢ=x_dado−xₘ. Para a=2,b=0, resíduos0ou±0,02m. Para a=0, último resíduo3,98m. Todos são calculados em unidades inteiras de1/200m antes da comparação, para preservar exatamente a fronteira inclusiva |r|≤B no domínio discreto do painel.

B é limite de erro de posição assumido para o exercício, entre0e20cm. Não é incerteza-padrão, desvio-padrão, p-valor ou intervalo de confiança. Sob tempos/condições exatos e a hipótese de erro limitado porB, estar na faixa é condição de compatibilidade; não prova o modelo ou uma lei universal. Se um ponto fica fora, o conjunto das suposições é inconsistente: não se identifica automaticamente o mecanismo que falhou.

Aumentar B muda apenas a faixa/classificação, mantendo dados, previsão e resíduos. Mudar b gera outro cenário sintético e desloca todos os dados, incluindo t=0. Não é nova evidência experimental. Uma referência de posição independente seria uma proposta de controle, não uma medição já realizada.

## Interface e leitura

Tese visual: um plano de resíduos e uma tabela, para comparar grandezas com unidade e hipótese explícitas. Conteúdo: pergunta, definição, exemplos, comparação interativa e exercícios. Interação: controles por teclado preservam foco e atualizam valores; sem animação decorativa.

Cinco pontos pretos sem interpolação; faixa azul±B. Escala vertical adaptativa e explicitamente declarada, para não confundir alturas de gráficos com a mesma escala. A tabela fornece todos os valores e a comparação sem depender de cor. B=0é tratado como limite nulo, sem dividir por zero. Posição inicial, velocidade e domínio temporal permanecem visíveis. Nenhuma figura ou dado do livro foi copiado.

## Execução e verificação

Na raiz:

```sh
python3 labs/modelos-medidas/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: referência independente em Fraction para60configurações; casos padrão e fronteira inclusiva; efeitos separados de desvio/aceleração/limite; contratos.27cenários Python/JS cruzados. Testes verificam implementação e desigualdades, não adequação física a um experimento real.

## Lacunas e sequência

Desenho experimental real, incertezas de tempo/condições iniciais, calibração, propagação, correlação e comparação estatística permanecem pendentes. O exemplo não é uma demonstração abrangente de filosofia da ciência ou metrologia. Revisão pessoal e materiais da turma ainda pendentes.

Próxima alternância global: auditar MatemáticaIII/CálculoIII antes de selecionar um aprofundamento. No retorno a FísicaI, desenvolver energia/potenciais sem tratar as introduções curtas como capítulos completos.


Verificação final:570testes Python,240demonstrações/720cenários e327MathML aprovados;27estados Python/JS. Interface desktop/390px, limite zero/igualdade, desvio comum e resposta negativa conferidos. Roteiro abre a aula; sem erros observados no console ou transbordamento horizontal. Saldo91%; parada65%. Revisão pessoal pendente.
