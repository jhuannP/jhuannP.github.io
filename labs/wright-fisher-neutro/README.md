# Wright–Fisher neutro — notas originais

16/10/2026. Rascunho para revisão de Jhuann, separado do projeto antigo.

## Um alelo é uma variante, não uma vantagem automática

Considere um locus com duas variantes A e a. O modelo acompanha quantas cópias são A; os rótulos não dizem que A é melhor, dominante ou associado a uma característica clínica. Na versão neutra, as variantes têm a mesma contribuição reprodutiva esperada. Mesmo assim, sua frequência pode mudar por amostragem finita.

## Declare população, cópias e geração

Há N indivíduos diploides e M=2N cópias do locus, com gerações não sobrepostas e tamanho constante. A próxima geração é formada por M escolhas independentes, com reposição, das cópias da geração atual. Excluímos seleção, mutação, migração e estrutura espacial. Aqui N é o tamanho da população ideal, não uma estimativa de tamanho efetivo de uma população real.

## A amostragem com reposição gera a binomial

Se há i cópias A, p=i/M. O número X_{t+1} de cópias A na próxima geração tem distribuição Binomial(M,p). Logo P_ij=C(M,j)(i/M)^j(1−i/M)^(M−j). Nos extremos i=0 e i=M, a distribuição é uma massa pontual; o código trata esses casos explicitamente. Uma geração não mantém necessariamente o mesmo número de A.

## Os momentos condicionais distinguem contagem e frequência

A binomial dá E[X_{t+1}|X_t=i]=Mp=i e Var(X_{t+1}|X_t=i)=Mp(1−p). Para a frequência p_{t+1}=X_{t+1}/M, a variância divide por M²: Var(p_{t+1}|p_t=p)=p(1−p)/M. N e 2N não podem ser trocados sem alterar a escala da deriva.

## Média constante não significa trajetória constante

Como E[p_{t+1}|p_t]=p_t, tomar a expectativa novamente dá E[p_t]=p_0 quando o estado inicial é fixo. Essa é uma propriedade de martingal. Uma população particular pode subir, cair, perder A ou fixá-lo. A média compara repetições hipotéticas do modelo; não descreve o caminho de cada população.

## Diversidade esperada decai sem seleção

Defina H(p)=2p(1−p): probabilidade de duas escolhas independentes com reposição encontrarem alelos diferentes. Não é automaticamente a fração observada de indivíduos heterozigotos. Usando E[p_{t+1}²|p]=p²+p(1−p)/M, obtemos E[H(p_{t+1})|p]=(1−1/M)H(p). Portanto E[H(p_t)]=2p_0(1−p_0)(1−1/M)^t. Amostragem sem reposição exige o fator M/(M−1).

## A variância entre populações cresce enquanto a média fica

E[H(p_t)]=2(E[p_t]−E[p_t²]) e Var(p_t)=E[p_t²]−p_0². Substituindo a média e a diversidade, resulta Var(p_t)=p_0(1−p_0)[1−(1−1/M)^t]. A dispersão cresce em direção a p_0(1−p_0), embora cada estado possível fique no intervalo [0,1]. Em t=0, com frequência inicial fixa, a variância entre repetições é zero.

## Propagar a distribuição não exige sortear trajetórias

Se q_t(i)=P(X_t=i), a lei da probabilidade total dá q_{t+1}(j)=Σ_i q_t(i)P_ij. O laboratório começa com massa 1 em k_0 e aplica essa recorrência. É a distribuição da cadeia discreta finita, calculada em ponto flutuante, sem ruído de Monte Carlo. Não usamos aproximação por difusão; existem erros de arredondamento. O custo direto é O(tM²), inadequado para populações arbitrariamente grandes.

## Absorção eventual tem uma probabilidade simples

Sem mutação, 0 e M são absorventes. De qualquer estado interior há chance positiva de alcançar um extremo na próxima geração; como há finitos estados, existe um limite inferior positivo para essa chance. Assim a probabilidade de continuar interior para sempre é zero. Como p_t é limitado e mantém expectativa p_0, no limite p_∞ só vale 0 ou 1 e E[p_∞]=p_0. Portanto a probabilidade eventual de fixação de A é p_0.

## Um exemplo pequeno permite conferir todos os estados

Com N=1, M=2 e k_0=1, p_0=1/2. Após uma geração, as probabilidades para X=0,1,2 são 1/4,1/2,1/4. Na segunda geração, ficam 3/8,1/4,3/8. A média de frequência é 1/2 em ambas; a variância passa de 1/8 a 3/16. A diversidade média passa de 1/4 a 1/8. É um exemplo matemático mínimo, não uma descrição realista da reprodução de uma espécie.

## Horizonte finito e destino eventual são perguntas distintas

No exemplo, a chance de A já estar fixado na segunda geração é 3/8, menor que a chance eventual de 1/2. A massa interior ainda pode terminar em qualquer extremo. O gráfico mostra probabilidades em estados discretos numa geração escolhida; as linhas apenas conectam pontos para leitura, não uma densidade contínua nem uma trajetória temporal. Compare populações diferentes mantendo uma frequência inicial compatível com a malha de cópias.

## O que este laboratório demonstra e o que permanece aberto

Confira massa total, média, variância, diversidade e extremos. Não renormalizamos os vetores a cada geração para esconder deriva numérica. Seleção, sazonalidade, mutação, genótipos, estrutura e dados de uma espécie exigem outros modelos. O roteiro antigo de projeto de Jhuann ainda precisa de revisão de código, contribuição e entrega; esta aula original não valida aquele projeto nem constitui resultado científico pessoal.

## Resoluções

Com N=10 indivíduos diploides, quantas cópias do locus há no modelo?

M=2N=20.

Com N=10 e p=1/2, qual a variância da frequência após uma geração condicionada a esse estado?

p(1−p)/(2N)=(1/4)/20=1/80=0,0125.

No exemplo N=1, k_0=1, qual a chance de A já estar fixado após duas gerações?

A distribuição é [3/8,1/4,3/8]; o estado X=2 tem massa 3/8.

Nesse exemplo, qual a variância da frequência na segunda geração?

(1/4)[1−(1/2)²]=3/16.

Nesse exemplo, qual a diversidade média E[2p(1−p)] após duas gerações?

2(1/2)(1/2)(1−1/2)²=1/8.

Se há 4 cópias A em uma população ideal de N=10 indivíduos, qual a chance eventual de fixação neutra de A?

k_0/(2N)=4/20=1/5.

Neutralidade exige que toda população mantenha p_t=p_0?

Deriva é flutuação por amostragem finita, mesmo sem seleção.

O gráfico calculado por q_{t+1}=q_t P é uma trajetória amostrada?

Não houve sorteio de uma população particular.

Sem mutação, um alelo perdido pode reaparecer neste modelo?

O estado X=0 é absorvente; não existe mecanismo de reintrodução.

H=2p(1−p) é automaticamente a fração observada de indivíduos heterozigotos?

Uma estatística de alelos não é, por definição, uma contagem de genótipos observados.

## Roteiro e verificação

Explique primeiro o processo de amostragem. Derive a média e a variância da frequência, obtenha a recorrência de H e compare a fórmula com a propagação qP. Explore os estados absorventes e um estado inicial não simétrico. Produto pessoal: solução própria do exemplo mínimo e comentário sobre perda/fixação eventual versus horizonte finito. Não se pressupõe execução pessoal.

Quatro testes: referência racional independente para cadeias pequenas; linhas, momentos e função harmônica de fixação; momentos globais/diversidade/simetria/massa absorvida; contratos. As referências racionais percorrem 75 estados iniciais/horizontes de N=1,2,3. O arquivo reference.json contém 51 configurações para comparação entre Python/JavaScript. A interface usa N=5,10,15,20, frequência inicial em décimos e até 40 gerações; cada frequência corresponde a número inteiro de cópias. Não são estimados tempos de fixação. Rode `python3 -m unittest discover -p 'test_*.py'` na raiz.

## Fontes e limites

[USP CCM0211](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211), itens 10 e 13; consulta 16/10/2026. [Rick Durrett, Probability Models for DNA Sequence Evolution](https://sites.math.duke.edu/~rtd/Gbook/PM4DNA_0317.pdf), segunda edição, copyright 2008 no PDF do autor, seção 1.2, páginas impressas 5–7, consultadas diretamente em 16/10/2026. N representa diploides e há 2N cópias. A fonte distingue a diversidade com e sem reposição; a aula declara a convenção com reposição. Sem reprodução de seus exercícios ou figuras; derivações, exemplo mínimo e código preparados para este material.

Não inclui seleção, sazonalidade, mutação, migração, estrutura, ligação entre loci ou comparação com dados. O roteiro antigo localizado não foi reimplementado nem validado e não se torna evidência de competência por esta aula. Próxima ação global: mapas de Biologia IV e Laboratório I.
