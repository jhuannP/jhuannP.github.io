# Softmax e perda por logits

27/10/2026. Notas originais com apoio de IA, rascunho para revisão pessoal. Operação multiclasse isolada, não integrada ao treino XOR. Sem framework ou dados reais.

## Convenções e deduções

K logits reais, um alvo inteiro k∈{0,…,K−1}, classes mutuamente exclusivas. p_i=exp(z_i)/Σexp(z_j), CE=−ln(p_k), logs naturais/nats. Sem pesos, smoothing, ignore_index ou máscara na CE. Softmax aceita máscara própria, com pelo menos uma opção; uma linha toda bloqueada é erro.

Deslocar z por c·1 cancela exp(c) e preserva p e CE. Log-sum-exp isolado muda por c, não é invariante. Dobrar z em geral muda p. Exemplo original z=[ln 2,0,0]: p=[1/2,1/4,1/4], alvo 0 dá ln 2 e gradiente [−1/2,1/4,1/4]. Dobrar os logits dá [2/3,1/6,1/6]. A figura usa barras de origem zero e escala comum.

Jacobian ∂p_i/∂z_j=p_i(δ_ij−p_j), pela regra do quociente. ∂L/∂z_i=p_i−1[i=k], derivando log-sum-exp e o alvo; soma do gradiente zero. Para N exemplos independentes na normalização, redução mean divide perdas e gradientes por N; sum não divide. Não significa independência estatística validada de dados reais: aqui apenas cada linha tem seu próprio denominador.

Passar [1/2,1/4,1/4] como logits produz perda ln(1+2exp(−1/4))≈0,939 para alvo 0; não ln 2. A API não detecta probabilidades e não muda a interpretação da entrada.

## Correção numérica

Regressão reproduzida no código antigo de deep_ops.py e no download da aula: CE([1e20,1e20,1e20],1) retornava 0, pois (1e20+ln 3)−1e20 perde ln 3. Corrigido nos dois lugares: primeiro calcular m−z_k, depois somar log1p da soma de pesos deslocados, excluindo exatamente um peso máximo igual a 1. Empates mantêm os outros máximos na soma. O laboratório contém a mesma função autocontida.

Para z=[1000,0,−1000], alvo 2, p_2 arredonda a zero; a perda por logits dá 2000. Para [50,0], alvo 0, log1p preserva a perda muito pequena, aproximadamente exp(−50). Não recortamos probabilidades. Entradas finitas não garantem diferenças/resultados finitos: CE([1e308,−1e308],1) rejeita perda fora da faixa de float. Diferenças já perdidas na entrada (1e20+1==1e20) não podem ser recuperadas; underflow ainda ocorre em probabilidades. Não se promete precisão arbitrária.

## Fontes

[Dive into Deep Learning 1.0.3, §4.1](https://d2l.ai/chapter_linear-classification/softmax-regression.html): consulta parcial em 27/10/2026, §4.1.1.2 e §4.1.2.2 para normalização e derivada da perda. [PyTorch 2.14, CrossEntropyLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html): introdução, alvo índice, redução e equivalência LogSoftmax/NLLLoss, consulta parcial na mesma data. Exemplos, figuras, derivação escrita e código originais. Nenhum framework instalado/executado ou material integral reproduzido.

## Código e verificação

Da raiz: `python3 -m unittest discover -s labs/softmax-perda -t .`. Cinco testes: regressão de offset grande e perdas pequenas, 81 casos moderados contra expressão direta; gradiente e jacobiano por diferenças centrais em quatro vetores; deslocamento e perda de resolução das entradas; redução de batch e seus gradientes; máscaras/contratos. Comparação do código autocontido com deep_ops.py. `batch_loss_gradient` usa linhas de mesmo K e uma classe por linha, sem máscara.

Os 12 exercícios preservam so1/so2 e acrescentam: p=1/2, perda ln 2, gradiente alvo −1/2, soma zero, média ln 2, perda 2000, perda ln 3 sob offset, escala altera p, cálculo por logits e entrada não normalizada. As resoluções estão na aula.

O painel existente mostra [a,0,−a] e máscaras, sem CE, gradiente ou treino. Revisão proposta em duas sessões: invariância/gradiente; depois extremos e reduções. Pendentes: treino multiclasse, calibração, perdas com pesos/smoothing, framework e revisão pessoal.

Conferência da entrega: cinco testes locais, sete das operações de DL e 14 do catálogo aprovados; 743 fórmulas MathML conferidas. Exercício so9 rejeitou 0 e aceitou ln 3 pelo teclado; máscara completamente bloqueada rejeitada e restaurada. Figura inspecionada em 390 px, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
