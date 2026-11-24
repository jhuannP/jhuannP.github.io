# Cobertura: conferir o procedimento sob modelos explícitos

Material original de estudo, com apoio de IA e revisão pessoal pendente. Modelos sintéticos; nenhum dado de pesquisa, cliente, instrumento ou aluno foi utilizado.

## Modelo normal preservado

Com observações normais IID, média μ e desvio populacional σ>0 conhecido, o intervalo é X̄±cσ/√n. Para nível γ, c=Φ⁻¹((1+γ)/2). Usar c=1,96 dá cobertura normal ≈0,9500042097, por arredondamento do quantil. O exemplo anterior permanece: média observada 10, σ=2 e n=100 dão erro padrão 0,2, margem 0,392 e limites [9,608;10,392]. Todos têm a unidade da variável observada, exceto n e c, adimensionais.

O livro usa uma tabela de área entre zero e o quantil: γ/2. Uma CDF acumulada à esquerda exige (1+γ)/2. Não trocar as convenções.

## Distribuição discreta exata

Cada Xᵢ vale −1 ou +1, independentemente, com probabilidades 1/2. Média μ=0 e σ=1 conhecidos. Para n=4, as 16 sequências equiprováveis dão cinco médias com multiplicidades 1,4,6,4,1. Aplicar a regra normal com margem 0,98 cobre zero apenas nas três médias centrais: 14/16=7/8. Isso é uma probabilidade exata para a regra aplicada ao modelo binário, não uma estimativa de Monte Carlo.

Para n genérico, K conta os valores +1 e a cobertura soma C(n,k)/2ⁿ quando (2k−n)²≤c²n. O código usa inteiros e Fraction para decidir a inclusão dos extremos sem arredondamento. Limite educativo: 1≤n≤128, c positivo inteiro ou Fraction; floats não são aceitos nessa função. A figura foi criada a partir do caso n=4; não copia uma figura do livro.

## Contrapontos separados

Se um único valor R=±1 é copiado quatro vezes, as marginais continuam iguais, mas a média tem variância 1. A margem incorreta 0,98 não cobre zero em nenhum resultado. Isso não é o modelo IID anterior.

Outra função avalia erros padronizados normais da forma b+sZ, Z normal padrão, s>0. A cobertura é Φ((c−b)/s)−Φ((−c−b)/s). b e s são prescritos em unidades do erro padrão usado no intervalo; não são estimados por esta função. No caso b=5 e s=1, a cobertura é ≈0,00118289. O cálculo usa floats/erf e não promete precisão relativa nas caudas extremas.

## Reproduzir

Da raiz do protótipo:

```sh
python3 labs/confianca-cobertura/coverage.py
python3 -B -m unittest discover -s labs/confianca-cobertura -t .
```

Cinco métodos de teste: limites literais e mudanças de escala; seis comparações de cobertura normal contra integração independente da densidade por Simpson; trinta modelos binários contra enumeração completa de todas as sequências (6138 sequências no total); contraponto de dependência; contratos. Não são testes de validade de uma coleta real.

O snippet, desafio e painel normal anteriores foram preservados. A nova figura e este laboratório não foram ligados ao painel de simulações; ele continua gerando médias normais. Em B repetições independentes, a fração coberta tem variância q(1−q)/B. B não é o tamanho n de cada amostra.

## Fontes e alcance da consulta — 29/10/2026

Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição (2010), primeira reimpressão (2011), Edusp, confirmação em CIP. §7.4, recortes das pp.244–247/PDF259–262 consultados para pivô normal, interpretação, largura e aproximação. P.245/PDF260 inspecionada visualmente para fórmulas e convenção de área. Sem reproduzir exercícios, tabelas ou exemplos. *Probabilidade e Variáveis Aleatórias*, 2ª edição, permanece referência complementar do percurso, sem nova leitura neste bloco. PDFs privados não servidos.

[NIST/SEMATECH, Confidence Limits for the Mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm): consulta parcial na interpretação de cobertura e fórmula t; sem usar dados ou exemplos da fonte. A aula mantém distintas as hipóteses de σ conhecido e estimado.

Não implementamos intervalo t, bootstrap, correções de dependência, uma posterior bayesiana, seleção de modelo ou plano amostral de pesquisa. A enumeração binária é um contraponto à utilização automática de uma regra, não um novo intervalo universal. Inferência no curso formal, versão ministrada e domínio pessoal continuam separados.
