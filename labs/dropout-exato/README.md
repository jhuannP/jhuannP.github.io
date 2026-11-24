# Dropout — notas de aula

Aula existente aprofundada; exemplo escalarx=3/p=1/2, Python e desafio preservados. Rascunho; revisão pessoal pendente. Operação permanece isolada do treino/backprop da MLP XOR.

Fontes: Dive into Deep Learning5.6 eq.5.6.1 e§§5.6.1–5.6.2, consulta parcial em27/10/2026 para escala invertida, esperança e treino/avaliação. https://d2l.ai/chapter_multilayer-perceptrons/dropout.html . PyTorch2.14 nn.Dropout, referência oficial parcialmente consultada, sem instalar/executar framework: https://docs.pytorch.org/docs/2.14/generated/torch.nn.Dropout.html . Código, dados, figura, enumeração e deduções próprios, sem reproduzir exemplos das fontes.

h′ᵢ=mᵢhᵢ/q,q=1−p; média hᵢ e variânciahᵢ²p/q. Para h=(2,−1),p=1/2, somas0,4,−2,2 dão média1/variância5; média de ReLU=3/2, enquanto avaliação dá1. Para duas cópias, média com máscaras independentes tem variância5/2; máscara compartilhada dá5. Não é incerteza calibrada nem garantia de generalização. Backward deve reutilizar máscara do forward; não integrado aqui.

Rodar na raiz: `python3 -m unittest discover -s labs/dropout-exato -t .`. Biblioteca padrão, int/Fraction. Enumeração até10 componentes, exclui estados de massa zero. p em[0,1),p=1 rejeitado; bibliotecas podem ter caso especial diferente. apply usa máscara explícita no treino e identidade em avaliação. Não treina pesos, não escolhe p e não implementa tensores/GPU. Python antigo reinicia RNG por chamada, propósito didático; um treino real precisa gerenciar o estado do gerador.

## 27/10/2026 — dropout, média, variância e modos

Aula `dl-dropout` aprofundada de3 para14 seções e2 para12 exercícios. IDs dr1/dr2, exemplo escalarx3, Python e desafio anteriores preservados. Prova de média/variância condicionais, enumeração de quatro máscaras, contraexemplo ReLU, variância linear e identidade de perda quadrática sob hipóteses específicas. Gradiente de máscara fixa/reutilização no backward; batch com máscaras independentes versus compartilhadas; domínio p<1 e estado do RNG. Não integrado à MLP/backprop do treino nem apresentado como melhoria empírica.

Fontes: D2L5.6 eq.5.6.1 e§§5.6.1–5.6.2, https://d2l.ai/chapter_multilayer-perceptrons/dropout.html ; PyTorch2.14 nn.Dropout, https://docs.pytorch.org/docs/2.14/generated/torch.nn.Dropout.html . Consulta parcial em27/10/2026: sorteio, escala e identidade em avaliação. Sem instalação/execução de framework ou cópia de exemplos/figuras. Enumeração, variância, dados e figura próprios. Média não linear/penalidade do caso linear não generalizadas a qualquer rede, perda ou incerteza calibrada.

Verificação:14 testes do catálogo e cinco locais aprovados;795 estruturas MathML conferidas. Enumeração de108 combinações de vetor/probabilidade para médias, variâncias e covariâncias; perda quadrática em32 casos;16 pares de máscaras de batch versus compartilhamento; gradiente com máscara fixa, avaliação/p0 e contratos. Limite de dez componentes para enumeração; Fraction sem Monte Carlo. No navegador390px, média de ReLU rejeitou1 e aceitou1,5 pelo Enter; reutilizar máscara no backward aceito. Figura inspecionada em`dropout-exato-mobile.jpg`; documento390px, console sem erros. Leitor de tela, Windows real e revisão pessoal pendentes.

Deep learning25 aulas/100 exercícios,20 introduções curtas. Global51 trilhas,546 aulas/4313 exercícios e200 introduções curtas. Contagens não comprovam formação ou domínio pessoal. Próxima ação: reconstruir os quatro casos e comparar média de ReLU/saída em avaliação em20min. Próximo bloco global: inspecionar introdução de FísicaIV e referência para aprofundamento quântico. Saldo semanal81%; parada operacional65% mantida.
