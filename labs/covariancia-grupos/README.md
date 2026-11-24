# Covariância total:quando misturar muda o sinal

Extensão original assistida por IA,28/10/2026,revisão pessoal pendente.Distribuição populacional sintética,não amostra ou efeito causal.

## Referências e páginas

Magalhães/Lima,Noções de Probabilidade e Estatística,7ªedição,§5.2 pp.162–163/PDF177–178;Magalhães,Probabilidade e Variáveis Aleatórias,2ªedição,§5.3 p.265/PDF137 (página dupla264–265).Recortes textuais consultados28/10/2026 para covariância/correlação e definição condicional,sem leitura integral,nova inspeção visual ou PDFs servidos.Identidade total e exemplo finito derivados nas notas,sem atribuir sua formulação exata a trecho não conferido.

## Prova

Escreva X−EX=(X−mX)+(mX−EX),mX=E[X|G],e análogo para Y.Ao multiplicar e misturar,a média dos resíduos condicionais é zero:ambos os termos cruzados somem.O termo residual éE[Cov(X,Y|G)];o das médias éCov(mX,mY).Segundos momentos finitos bastam,neste modelo finito todos existem.Grupos de massa zero não recebem condicional por divisão0/0.

## Modelo conhecido

G~Bernoulli(q),U uniforme em{−1,+1},independentes.X=4G+U,Y=4G−U.Cada grupo tem covariância−1 evariâncias1.Médias4G;parcela entre16q(1−q).LogoCovglobal=16q(1−q)−1,VarX=VarY=16q(1−q)+1.

|q|Parcela dentro|Parcela entre|Covglobal|Correlação global|
|---|---:|---:|---:|---:|
|1/2|−1|4|3|3/5|
|1/16|−1|15/16|−1/16|−1/31|
|0|−1|0|−1|−1|

A covariância condicional é centralizada na média de cada grupo.Não é a covariância de todos os pontos seguida de uma média simples de correlações.Nenhuma decomposição causal é inferida.

## Executar

```sh
python3 labs/covariancia-grupos/decomposition.py
python3 -m unittest discover -s labs/covariancia-grupos -t .
```

Inteiros/Fraction para valores e pesos,1–64linhas,pesos não negativos somando1,grupo textual1–32caracteres.Grupos de massa zero omitidos;linhas repetidas somam suas massas.Cálculo racional para referência finita,não estimador empírico ou inferência.O auxiliar moments pressupõe dados já validados/normalizados;entrada pública deste laboratório é decompose.Não controla denominadores racionais arbitrários nem é motor estatístico geral.

Quatro testes:17pesos q e identidade;referência/grupo raro;transformações afins e divisão de linhas;contratos.Painel antigo preservado para o exemplo quadrático,não uma visualização automática desta mistura.

## Revisão20min

Reconstrua o cancelamento dos termos cruzados,os quatro pontos,q1/2 e1/16.Explique por que mudar pesos muda associação epor que isso não prova que condicionar produz um efeito causal.Pendentes:amostra/incerteza,grupos contínuos e revisão pessoal.
