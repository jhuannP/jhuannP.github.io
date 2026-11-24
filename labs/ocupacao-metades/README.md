# Ocupação em duas metades: probabilidade não é dinâmica

Rascunho próprio de FísicaII para revisão de Jhuann. A geometria tem duas regiões iguais, sem viés externo; posições independentes e uniformes num retrato de equilíbrio do gás clássico ideal. N é fixo. Cada partícula é marcada só para a contabilidade; não calculamos efeitos de indistinguibilidade quântica ou entropia de mistura.

## Estados e contagem

Uma sequência binária informa apenas a metade ocupada por cada índice. É uma configuração reduzida, não um microestado clássico completo de posições e momentos. Há 2^N sequências equiprováveis. K conta quantas partículas estão à esquerda; W(k)=C(N,k) é o número de sequências com K=k e P(K=k)=W(k)/2^N. Macroestados não são equiprováveis.

A razão W(k+1)/W(k)=(N−k)/(k+1) localiza o máximo: N/2 se N é par, dois centrais se ímpar. Para N=8, W=(1,8,28,56,70,56,28,8,1). P(K=4)=35/128; P(K=0 ou8)=1/128; P(2≤K≤6)=119/128; P(|K−4|≥3)=9/128. Exemplos e enumeração próprios, sem dados de um experimento.

## Flutuação: qual normalização?

K=ΣXi, Xi indicador de estar à esquerda. E[Xi]=1/2 e Var(Xi)=1/4. Independência elimina covariâncias: E[K]=N/2 e Var(K)=N/4. Assim σK=√N/2 cresce, σ(K/N)=1/(2√N) diminui e σK/E[K]=1/√N diminui. Não confundir fração de partículas e desvio relativo à média.

Concentração da fração não quer dizer aumento da probabilidade do único valor K=N/2: para N par, P_N+2(centro)/P_N(centro)=(N+1)/(N+2)<1. Compare regiões com largura relativa escolhida, não só um valor exato.

Se todas as partículas fossem forçadas a compartilhar o mesmo indicador, cada uma ainda teria probabilidade marginal1/2 e E[K]=N/2, mas Var(K)=N²/4. Isso viola independência e não descreve o gás ideal do modelo. Mesmas probabilidades marginais não garantem a mesma flutuação.

## Cota demonstrada

Para a>0, (K−E[K])²≥a² no evento |K−E[K]|≥a. A média do quadrado é portanto≥a² P(evento), dando P(evento)≤Var(K)/a². Com N=8,a=3, a cota2/9 é maior que a probabilidade exata9/128. Ela não fornece uma igualdade nem uma trajetória temporal.

## Ponte para entropia

S_conf(k)/kB=ln W(k) é contribuição configuracional reduzida do modelo; o logaritmo leva produtos de pesos independentes a somas. W=70 no centro versus1 num extremo dá diferença ln70 em unidades de kB. Não é toda a entropia do gás: não inclui momentos nem a resolução contínua do espaço. Nenhuma dinâmica foi construída para concluir aumento monótono ao longo de cada trajetória.

## Execução e verificação

`python3 labs/ocupacao-metades/occupancy.py`

`python3 -m unittest discover -s labs/ocupacao-metades -t .`

A distribuição exata usa comb/Fraction até512 partículas; enumeração de máscaras binárias é limitada a16 pelo custo2^N. Quatro testes: enumeração independente até12 partículas (8190 configurações no total); normalização/simetria/momentos em64 tamanhos; eventos, razão de probabilidades centrais e contraexemplo correlacionado; contratos. Isso testa aritmética e hipóteses implementadas, não valida um gás real.

Probabilidade de ocupação não determina tempo de retorno. Precisaríamos de dinâmica e correlações temporais; quadros consecutivos de uma simulação não são automaticamente amostras independentes. Sem temperatura, velocidades, colisões, relógio ou previsão de relaxação no código.

## Fontes

Nussenzveig, Curso de Física Básica vol.II, 5ª edição (2014), §12.5(a), pp.341–343/PDF342–344, consulta textual parcial em29/10/2026; p.343/PDF344 também renderizada e inspecionada para flutuação relativa e a distinção de microestado completo. §12.5(b), p.344/PDF345, leitura textual parcial sobre peso e logaritmo. Sem leitura integral. Contagens para oito partículas, demonstrações, exercícios, figura e código próprios; sem reprodução de tabelas, figuras ou exercícios do livro.

Aprovação de FísicaII2024/1 e programa CCM0122, versão2025 posterior à turma, permanecem registrados com limitações. Não houve nova consulta ao programa neste bloco. Sem distribuição do PDF privado. Próxima revisão pessoal: reconstruir a contagem e explicar por que σK pode crescer enquanto σ(K/N) diminui.
