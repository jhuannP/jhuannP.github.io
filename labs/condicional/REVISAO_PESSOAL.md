# Revisão pessoal: condicionamento e Bayes

Preparado em 28/10/2026 com apoio de IA. Revisão pessoal de Jhuann **pendente**. Este roteiro não atesta domínio nem é um exercício transcrito dos livros.

## Direção da página

Tese visual: folha de trabalho editorial, fundo claro, tipografia e azul do portfólio, com espaço para escrever antes de conferir.
Plano de conteúdo: orientação e tabela → três perguntas → soluções opcionais → registro pessoal e exportação.
Interação: foco e hover discretos nos controles; abertura nativa das soluções sem animação adicional. É uma superfície de estudo, sem necessidade de efeitos de entrada ou rolagem. Respeitar preferência por movimento reduzido.

## Como usar em 20–30 minutos

Abra `/labs/condicional/revisao.html`. Reserve 5 minutos para reconstruir a tabela, 10 para responder às três questões e 5–15 para conferir e modificar uma hipótese. Tente primeiro sem consultar as soluções. Se precisar de ajuda, registre qual foi; consultar não é falhar, é localizar o próximo assunto de estudo.

O modelo reutiliza as probabilidades sintéticas da aula de Bayes: P(H)=1/10, P(+|H)=4/5 e P(+|Hᶜ)=1/5. A tabela usa massas expressas em milésimos; seus números não representam dados coletados. As questões pedem: (1) posterior após sinal e ausência de sinal, com denominadores; (2) recalcular após mudar apenas a base para 1/5, explicitando a hipótese de manter as taxas condicionais; (3) distinguir cópia de registro de uma nova leitura condicionalmente independente.

As respostas começam vazias. Não existe nota automática nem marca de conclusão. Os campos ficam somente na aba: não são enviados, sincronizados nem gravados no armazenamento do navegador. O botão de exportação baixa um Markdown com o texto digitado, sem incorporar soluções. Para usar no outro computador, é necessário transferir o arquivo salvo pelo meio escolhido por Jhuann. Recarregar a página perde os campos; o botão fica disponível também no início da página.

## Fontes e limites

Reconferência **textual parcial** em 28/10/2026, a partir das extrações locais dos livros privados: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.54 e 59 (PDF69 e 74); Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, pp.28–30 (PDF19–20, páginas duplas). Sustentam definição condicional, regra do produto, probabilidade total e Bayes; exemplo, questões e deduções são próprios. Não foi feita nova leitura integral nem nova inspeção visual dos PDFs. Não se servem cópias dos livros.

A razão condicional requer denominador positivo. Uma leitura repetida só fornece a atualização por produto das duas taxas quando esse é o modelo conjunto apropriado; copiar um registro não satisfaz essa hipótese. Taxas constantes sob mudança de base são uma hipótese do exercício, não uma garantia sobre detectores reais. Não há validação de detector, amostra empírica ou resultado científico.

## Verificação e continuidade

As contas podem ser verificadas por enumeração de átomos equiprováveis, independentemente da fórmula de Bayes: para a primeira questão, 80 átomos H,+ e 180 Hᶜ,+; na segunda, 160 e 160; para duas leituras, expandir os resultados condicionais em 25 átomos por hipótese. As soluções explicam os passos e a normalização.

Critério de revisão **a preencher por Jhuann**: explicar cada denominador; modificar a base e reconstruir a tabela; descrever o que muda entre copiar um registro e obter outra leitura. Registrar ajuda utilizada, dúvidas e próximo passo. Só depois decidir se uma amostra pode ser apresentada como trabalho pessoal revisado.
