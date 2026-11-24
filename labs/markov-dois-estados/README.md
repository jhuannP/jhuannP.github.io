# Cadeia de dois estados: compor, propagar e distinguir limites

Modelo próprio com vetor linha e P=[[1−α,α],[β,1−β]]. Entradas racionais em [0,1]; n inteiro de 0 a 200. Não converte floats silenciosamente. Não há estimação de parâmetros nem interpretação física dos estados.

No exemplo α=1/5 e β=1/10, partindo de A: P(X₂=A)=33/50 e P(X₃=A)=281/500. Permanecer em A nos dois passos vale 16/25; voltar por B acrescenta 1/50. A recorrência qₙ₊₁=β+(1−α−β)qₙ dá, se α+β>0, qₙ=β/(α+β)+(q₀−β/(α+β))(1−α−β)ⁿ. Sua estacionária única é (β/(α+β),α/(α+β)). Se α=β=0, todas as distribuições são estacionárias; None na rotina significa ausência de unicidade.

Para α=β=1, a distribuição estacionária é (1/2,1/2), mas a preparação A alterna para sempre. Não se conclui convergência apenas de estacionariedade. No exemplo principal, a estacionária tem conjunta de dois A sucessivos 4/15, diferente do produto 1/9: não são estados independentes.

Na raiz do site:

    python3 -m labs.markov-dois-estados.exact
    python3 -m unittest discover -s labs/markov-dois-estados -t .

Cinco testes com enumeração de todos os caminhos até seis passos em 25 matrizes e duas preparações, fórmula fechada para 625 combinações, estacionariedade, alternância, identidade e rejeição de contratos inválidos. São verificações do modelo finito, não de uma teoria geral.

As oito novas seções e dez exercícios da aula explicam todas essas contas. Resolva as questões sem consultar o resultado e reconstrua os dois caminhos de retorno. O código e o desafio anteriores permanecem; o laboratório labs/markov usa β=0,4, com limite 2/3, diferente deste exemplo. O painel não foi alterado.

Fonte de fundamentos: [James Aspnes, Yale — MarkovChains](https://cs.yale.edu/homes/aspnes/pinewiki/MarkovChains.html), §1 e início do §2, consulta parcial em 22/10/2026. A página arquivada contém aviso sobre fórmulas quebradas; as contas deste laboratório foram derivadas e verificadas independentemente. Chorin–Hald/Pavliotis continuam referências temáticas da trilha; seus capítulos não foram relidos neste bloco. Conteúdo original assistido por IA, em rascunho para revisão de Jhuann. Tempo contínuo, inferência de matriz, teorema geral de convergência, primeira passagem e validação científica continuam pendentes.

Verificação deste bloco: cinco testes novos e 13 de catálogo aprovados; 539 estruturas MathML conferidas. No navegador, o exercício da estacionária rejeitou 2/3 e aceitou 1/3; largura 390 px sem transbordamento horizontal ou erros de console observados. Fórmula legível; prévia markov-dois-estados-mobile.jpg. Não houve revalidação integral da suíte global ou dos painéis, que foram preservados. Total: 501 aulas/3078 exercícios em rascunho; nenhuma disciplina completa. Saldo semanal após o bloco: 92%; parada em 65%.
