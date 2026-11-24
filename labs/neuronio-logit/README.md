# Unidade logística: do logit ao primeiro passo

22/10/2026. Notas de aula originais com apoio de IA; rascunho para revisão pessoal de Jhuann.

## Entradas, parâmetros e saída têm papéis diferentes

Considere um vetor de entrada x com d características, pesos w do mesmo tamanho e um viés escalar b. A unidade calcula z=w·x+b e depois uma ativação p=σ(z). Neste exemplo, x e o rótulo y são dados; w e b são parâmetros que podemos ajustar. O escalar z é chamado logit. As grandezas do exemplo são adimensionais. Em uma aplicação com unidades físicas, os produtos e o viés precisam ser compatíveis antes de aplicar uma exponencial.

z=w·x+b

## O viés desloca a resposta

Para uma entrada escalar x=2, peso w=1 e viés b=−2, o logit é zero e a saída sigmoide é 0,5, como no exemplo original abaixo. O peso controla a contribuição da entrada; o viés altera a resposta mesmo quando x=0. Para d entradas, há d+1 parâmetros nesta unidade. Um vetor de tamanho incompatível não define o produto escalar: o código sinaliza esse erro em vez de descartar coordenadas.

d entradas → d+1 parâmetros

## A sigmoide e sua derivada

A função σ(z)=1/(1+exp(−z)) é estritamente crescente e fica entre zero e um para todo z real finito. Derivar a expressão fornece σ′(z)=exp(−z)/(1+exp(−z))²=p(1−p). O maior valor da derivada é 1/4, em p=1/2; longe de zero, a curva se achata. Em ponto flutuante, a saída pode arredondar para zero ou um mesmo para entrada finita. Isso é um efeito numérico e não muda o intervalo aberto da função matemática.

σ′(z)=p(1−p)

## Entre zero e um não basta para medir confiança

Como modelo de classificação binária, podemos interpretar p como uma estimativa de P(y=1|x) sob hipóteses de modelagem e ajuste. Isso não garante calibração, nem qualidade em novos dados. Um limiar, como 0,5, converte a saída em uma decisão, mas deve considerar o problema e o custo dos erros. Nesta aula usamos rótulos inteiros y∈{0,1}; não afirmamos que a saída de um parâmetro escolhido manualmente já seja uma probabilidade bem estimada.

## A perda compara a saída a um rótulo

Adote a perda de entropia cruzada binária L=−y ln(p)−(1−y)ln(1−p), sem pesos de classe ou regularização e para apenas um exemplo. Se y=1, a perda é −ln(p), menor quando p aumenta. Se y=0, ela é −ln(1−p), menor quando p diminui. Com p=1/2, os dois rótulos produzem ln2. A perda é um critério de ajuste; seu valor em um único exemplo não é uma avaliação externa do modelo.

L=−y ln(p)−(1−y)ln(1−p)

## Calcular a perda diretamente do logit

Calcular primeiro p e depois seus logaritmos pode produzir log(0) quando a sigmoide arredonda. Substituindo a definição na perda, obtemos L=ln(1+exp(z))−yz. Reescreva ln(1+exp(z))=max(z,0)+ln(1+exp(−|z|)). Assim a exponencial recebe argumento não positivo; o código usa log1p para calcular ln(1+u) quando u é pequeno. Para z=1000 e y=0, a perda fica próxima de 1000, finita. Esta é uma implementação didática própria com Python básico, não uma chamada a um framework.

L=max(z,0)−yz+log1p(exp(−|z|))

## A regra da cadeia simplifica o gradiente

Na matemática exata, 0<p<1. Derivar L em relação a p dá (p−y)/[p(1−p)]. Multiplicar por dp/dz=p(1−p) cancela esses fatores e fornece dL/dz=p−y. Como dz/dwⱼ=xⱼ e dz/db=1, temos dL/dwⱼ=(p−y)xⱼ e dL/db=p−y. A simplificação evita calcular numericamente uma divisão por p(1−p). O gradiente desta perda não recebe um fator extra de derivada da sigmoide após esse cancelamento.

dL/dz=p−y

## Exemplo resolvido: calcular antes de atualizar

Use x=(2,1), w=(1,−1), b=−1 e rótulo y=1. O logit é 1×2+(−1)×1−1=0. Logo p=1/2 e L=ln2. O gradiente do logit é −1/2. Para os pesos, multiplique pelas entradas: gradiente de w₁ é −1 e de w₂ é −1/2; o do viés é −1/2. Os dois pesos participam do cálculo e serão atualizados juntos a partir desses valores antigos.

∇wL=(−1,−1/2); ∂L/∂b=−1/2

## Um passo de descida muda os parâmetros

Com taxa η=0,2, aplique wnovo=w−η∇wL e bnovo=b−η∂L/∂b. Isso dá primeiro peso novo igual a 1,2 e segundo igual a −0,9; bnovo=−0,9. O novo logit é 1,2×2−0,9−0,9=0,6. A nova saída é aproximadamente 0,6457, e a perda aproximadamente 0,4375, menor que ln2≈0,6931. Esse cálculo é uma atualização sobre um exemplo, não um treinamento avaliado em uma base.

znovo=0,6; Lnovo≈0,4375

## Saturação depende da cadeia completa

A derivada da sigmoide fica pequena em logit de grande módulo. Mas para esta perda com logits, o gradiente em z é p−y: se z=1000 e y=0, p arredonda para um e o gradiente fica próximo de um, não de zero. Se a predição já corresponde ao rótulo, o gradiente pode ser pequeno, como esperado. Em redes com camadas ocultas, outras ativações e produtos de derivadas precisam ser analisados separadamente. Não transfira uma conclusão sobre esta saída escalar para qualquer rede profunda.

z=1000, y=0 ⇒ dL/dz≈1

## Mover o painel e ajustar por gradiente são ações distintas

O painel desta aula recebe escolhas manuais de entrada, peso e viés; ele apenas reconstrói z e a saída. O laboratório novo calcula uma perda e um gradiente e executa um passo explícito. Para falar em um procedimento de treinamento com evidência, ainda precisamos declarar conjunto de dados, redução da perda, separação de treino/validação/teste, algoritmo e critérios de avaliação. Uma queda de perda no exemplo usado para atualizar não demonstra generalização. A unidade logística é um fundamento, não uma rede profunda completa.

## O que o laboratório verifica e o que falta

Os testes comparam gradientes analíticos a diferenças centrais, verificam a atualização numérica e confrontam a perda estável com a forma usual em logits moderados. Entradas extremas ±1000 testam ausência de overflow ou logaritmo de zero nesse recorte. O código valida formas, valores finitos e rótulos binários, sem autodiferenciação. A rede de backprop da trilha tem material próprio; bibliotecas, treinamento sistemático, calibração e aplicação a problemas físicos permanecem por estudar e validar. Conteúdo preparado com apoio de IA, sujeito à revisão pessoal.

## Exercícios e resoluções

- Qual é a saída sigmoide para z=0? **Resolução:** σ(0)=1/(1+1)=0,5.
- A demonstração com sliders ajusta pesos por aprendizado? **Resolução:** Mover controles não equivale a treinar um modelo com dados e uma função de perda.
- Quantos parâmetros tem esta unidade com duas entradas e um viés? **Resolução:** Dois pesos mais um viés: três.
- Para x=(2,1), w=(1,−1), b=−1, quanto é z? **Resolução:** 2−1−1=0.
- Quanto vale σ′(0)? **Resolução:** p(1−p)=(1/2)(1/2)=1/4.
- No exemplo com p=1/2 e y=1, quanto é dL/dz? **Resolução:** p−y=1/2−1=−1/2.
- Com x₁=2 no mesmo exemplo, quanto é ∂L/∂w₁? **Resolução:** (p−y)x₁=(−1/2)×2=−1.
- No mesmo exemplo, quanto é ∂L/∂b? **Resolução:** dz/db=1, então o gradiente do viés é −1/2.
- Com peso inicial w₁=1, gradiente −1 e taxa 0,2, qual o novo peso? **Resolução:** 1−0,2×(−1)=1,2.
- Com b=−1, gradiente −1/2 e taxa 0,2, qual o novo viés? **Resolução:** −1−0,2×(−1/2)=−0,9.
- Após a atualização, pesos 1,2 e −0,9, b=−0,9 e x=(2,1): qual o novo logit? **Resolução:** 1,2×2−0,9−0,9=0,6.
- Reduzir a perda no único exemplo usado para atualizar prova bom desempenho em novos dados? **Resolução:** A queda no exemplo de ajuste não é uma avaliação externa; precisamos de dados e procedimento de validação.

## Fontes e execução

Bishop, PRML, §4.3.2, pp.205–206 (PDF223–224), leitura textual parcial. [Deep Learning, início do §4.1](https://www.deeplearningbook.org/contents/numerical.html), arredondamento; [PyTorch, BCEWithLogitsLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BCEWithLogitsLoss.html), introdução sobre estabilidade. Consultas parciais em 22/10/2026. O capítulo público de MLP do Deep Learning não pôde ser recuperado por tamanho; não é contado como leitura. Exemplos, atualização, figura e código são próprios.

Na raiz: python3 -m labs.neuronio-logit.experiment; testes: python3 -m unittest discover -s labs/neuronio-logit -t .

Sem framework ou autodiferenciação. Vetores como listas/tuplas não vazias, valores finitos, alvo inteiro 0 ou 1 e taxa não negativa. Nenhum conjunto real treinado ou desempenho externo avaliado.


## Unidade logística, perda e um passo de gradiente — 22/10/2026

Aula neuronio ampliada de três seções/dois exercícios para 12 seções/12 exercícios, preservando exemplo escalar antigo, Python, desafio e painel manual. Novos recortes: papéis de entrada/rótulo/parâmetros, formas, sigmoide e derivada, interpretação probabilística condicionada ao modelo, perda binária, estabilidade em logits e regra da cadeia. A unidade é fundamento de classificação, não uma rede profunda completa. Painel não foi convertido em treinamento automático.

Fontes primárias consultadas parcialmente em 22/10/2026: Bishop, Pattern Recognition and Machine Learning, §4.3.2, pp.205–206 (PDF223–224), leitura textual para modelo logístico, perda e gradiente; [Deep Learning, início de §4.1](https://www.deeplearningbook.org/contents/numerical.html), arredondamento; [documentação de BCEWithLogitsLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BCEWithLogitsLoss.html), introdução sobre estabilidade conjunta. Capítulo MLP público não recuperado por tamanho; não contado como leitura. Não se afirma leitura integral das fontes. Derivações, exemplo, passo, figura e código locais são originais.

Exemplo x=(2,1), w=(1,−1), b=−1 e y=1: z=0, p=1/2, L=ln2. Gradientes de w são (−1,−1/2), do viés −1/2. Com taxa 0,2: pesos novos 1,2 e −0,9, viés −0,9, z=0,6, p≈0,6456563, L≈0,437488. Um ajuste no próprio exemplo não demonstra generalização ou calibração. A perda usa max(z,0)−yz+log1p(exp(−|z|)); gradiente simplificado em z é p−y, sem multiplicar novamente por σ′.

Laboratório labs/neuronio-logit/: Python básico, sem framework ou autodiferenciação. Cinco testes novos aprovados: números do passo; 24 derivadas comparadas a diferenças centrais em oito cenários; estabilidade em logits até ±1000 e simetrias; gradiente com saturação e passo nulo; contratos. Doze testes de catálogo e 535 estruturas MathML aprovados; catálogo revalidado após a figura. Nenhum modelo JavaScript alterado; suíte global não repetida.

Navegador: tabela antes/depois legível em 390 px, largura da página igual à tela, nenhum erro de console observado. Gradiente −1 aceito, assim como o logit 0,6 com vírgula decimal. Prévia: neuronio-logit-mobile.jpg. Estado de rascunho assistido por IA e revisão pessoal pendente preservados.

Deep learning: 25 aulas/70 exercícios, dois recortes desenvolvidos e 23 introduções curtas. Percurso próprio, sem equivalência curricular automática ou domínio pessoal inferido. Catálogo global: 500 aulas/3022 exercícios em rascunho. Próxima revisão pessoal: reconstruir a regra da cadeia e a atualização sem consultar a solução, distinguindo painel manual de ajuste. Próximo bloco global: aprofundar tema de Biologia II ou revisar sua cobertura antes de ampliar, preservando a alternância entre disciplinas formais e percursos complementares. Saldo semanal após bloco: 93%; parada operacional em 65%.
