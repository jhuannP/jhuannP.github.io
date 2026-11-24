# Estacionariedade, fluxos e balanço detalhado

27/10/2026. Aula `equilibrio-markov` ampliada para14seções/12exercícios, mantendo o exemplo, Python, desafio, painel de dois estados e IDs eq1/eq2. Notas, figura, contas e laboratório originais com apoio de IA. Revisão pessoal de Jhuann pendente; não são resultado ou validação da IC.

## Convenções e relações

Cadeia finita homogênea, Pij=P(Xn+1=j|Xn=i), linhas não negativas somando1. Distribuição vetor-linha:pₙ₊₁=pₙP. Uma candidataπ é estacionária quando não negativa, soma1 eπP=π.

Fij=πiPij é a probabilidade do par(i,j) em passos consecutivos no regimeπ. Jij=Fij−Fji é uma corrente orientada, antissimétrica. Não é uma corrente elétrica ou taxa física por segundo sem definir duração do passo.

Somando as correntes que saem de i:

ΣjJij=πiΣjPij−ΣjπjPji=πi−(πP)i.

Emπ estacionária, a soma é zero, embora cada corrente possa ser não nula. Balanço detalhado exigeJij=0 para todo par. Ele implica estacionariedade pela soma das equações, usando a normalização das linhas. A recíproca não vale em geral.

## Dois estados preservados

P=[[4/5,1/5],[1/10,9/10]]. A equação de estacionariedade e normalização dãoπ=(1/3,2/3), com fluxos opostos1/15. Em dois estados, essa igualdade é forçada pelo balanço de um único par; para mostrar circulação, passamos a três estados.

## Exemplo cíclico original

P=[[1/2,1/2,0],[0,1/2,1/2],[1/2,0,1/2]], ordem A,B,C. Ficar ou avançar A→B→C→A com probabilidades iguais.

Cada coluna soma1, logoπ=(1/3,1/3,1/3) é invariante. FAB=1/6 e FBA=0. As correntes JAB=JBC=JCA=1/6 circulam; em cada estado entrada e saída líquidas se compensam. Não há balanço detalhado.

A cadeia é irreducível, pois o ciclo conecta todos os estados; há permanência positiva, logo é aperiódica. Para cadeias finitas, essas condições asseguram uma estacionária única e convergência de todo início. Não se estende automaticamente essa afirmação a espaços infinitos ou difusões.

### Prova específica sem estimar por uma curva

Para q=p−π, as componentes somam zero. Multiplicando:

qP=((qA+qC)/2,(qA+qB)/2,(qB+qC)/2)=(−qB/2,−qC/2,−qA/2).

Portanto ||qP||₂²=||q||₂²/4. Repetindo:||pₙ−π||₂²=4⁻ⁿ||p₀−π||₂². Essa identidade exata pertence a esta matriz, não é limite de erro para toda cadeia.

De início(1,0,0), as primeiras distribuições são(1,0,0),(1/2,1/2,0),(1/4,1/2,1/4). Há redistribuição e circulação mesmo que a uniforme seja invariante.

### Mesmaπ, outra dinâmica

R=(P+Pᵀ)/2 tem diagonal1/2 e todas as entradas fora da diagonal1/4. É simétrica e reversível emπ uniforme. Seus fluxos opostos são1/12 e as correntes zero. Compartilhar distribuição não implica compartilhar probabilidades de pares.

## Dois contraexemplos de convergência

P=[[0,1],[1,0]]: uniforme estacionária e reversível, mas início(1,0) alterna. Aperiodicidade importa. P=I: toda distribuição estacionária, sem atrator comum único. Irreducibilidade importa. Existência de uma invariante não basta para concluir que qualquer início converge para ela.

## Laboratório e verificação

`balance.py`: Python padrão e Fraction. Recebe P e candidataπ, confere dimensões, não negatividade e normalização exata. `diagnose` devolve próxima lei, fluxos, correntes, estacionariedade e balanço detalhado. Não calcula automaticamenteπ, irreducibilidade, classes ou período. `evolve` aceita0–1000passos e guarda também o início. Entradas int/Fraction, sem bool ou float. Nenhum dado ou matriz de entrada é alterado.

Rodar da raiz:

```sh
python3 -m unittest discover -s labs/markov-balanco -t .
```

Cinco testes: exemplos e comparação de fluxos; oráculo independente de caminhos equiprováveis para0–8passos; identidade exata de contração em três inícios por25passos;15matrizes circulantes e seis relabelings cada, com conservação e simetria de correntes; periodicidade, redutibilidade e contratos. A enumeração soma avanços mod3 e não reutiliza a multiplicação matricial como oráculo. Testes finitos apoiam a implementação; a prova da identidade está nas notas.

## Fontes e alcance

Pavliotis, *Stochastic Processes and Applications*, exemplar privado do acervo: §2.1, páginas impressas31–32/PDF44–45 consultadas parcialmente em27/10/2026. P.32/PDF45 visualmente conferida para a convençãoμ⁽ⁿ⁾=μ⁽⁰⁾Pⁿ. A extração do PDF emitiu aviso de compressão, mas esses recortes estavam legíveis. Não houve leitura integral nem distribuição do PDF. Afirmações de ergodicidade de difusões em outras seções não foram usadas como teoremas gerais de cadeias discretas.

[James Aspnes, Yale, notas arquivadas MarkovChains](https://cs.yale.edu/homes/aspnes/pinewiki/MarkovChains.html), §§2,2.1 e3.2 consultadas parcialmente em27/10 para estacionariedade, convergência e reversibilidade. A própria página alerta para fórmulas quebradas e falta de atualização; usamos definições e raciocínio legíveis, com demonstrações algébricas específicas próprias. Sem reproduzir exemplos ou figuras.

O percurso geral mantém Chorin–Hald como referência temática, sem alegar nova leitura desse livro neste bloco. A unidade é complemento de estudo, não disciplina cursada adicional ou resultado científico pessoal.

## Resoluções e revisão

1. Original:πA=1/3.
2. Distribuição fixa não obriga trajetória imóvel.
3. Nova uniforme:πB=1/3.
4. FAB=1/6.
5. FBA=0.
6. JAB=1/6.
7. Soma líquida por estado=0.
8. De inícioA, P(X1=B)=1/2.
9. De inícioA, P(X2=C)=1/4.
10. EmR, FAB=1/12.
11. Cadeia cíclica com permanência:invariante uniforme, irreducível, aperiódica, não reversível.
12. Mesma marginal não determina fluxos de pares.

Revisão pessoal20min:πP, dois fluxos e uma soma de correntes, antes de comparar R e a cadeia periódica. Campo de compreensão pessoal fica em branco. Amostragem de trajetórias, mistura geral, reversão temporal completa, taxas contínuas, estados infinitos e interpretação termodinâmica permanecem pendentes.
