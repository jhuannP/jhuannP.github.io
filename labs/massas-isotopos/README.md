# Massas — carga, escala e conjunto isotópico ideal

27/10/2026. Primeira aula de massas em Química III, com13seções/12exercícios. Notas, figura, números e código originais com apoio de IA, em rascunho para revisão pessoal de Jhuann. Não atestam domínio, operação de instrumento ou resultado experimental.

## Pergunta e hipóteses

Íon-modelo com massa nominal100u quando todos os sítios são leves; cada pesado acrescenta2u. Sítios independentes, mesma probabilidade p; exemplo n=2,p=1/4. Outras contribuições isotópicas, fragmentação, fundo, ruído, adutos e diferenças de resposta do detector são ignorados. A atribuição do conjunto a uma espécie já é hipótese, não conclusão do programa.

São massas nominais e probabilidades de exercício: não abundâncias naturais medidas. Não se substituem as massas exatas ou tabelas de isótopos por estes números.

## Interpretar os eixos

Para carga positiva q=ze, o valor convencional de m/z é numericamente(m/u)/z. O modelo usa z inteiro positivo e mantém a massa iônica declarada ao comparar cargas. Uma protonação ou outro aduto precisa alterar a contabilidade de massa. O método de ionização e a espécie precisam ser conhecidos para atribuir massa molecular neutra a um sinal.

Pico base é o de maior intensidade, normalizado a100. Pode ser um fragmento. Irel,i=100Ii/Imax não exige soma100 e não é concentração absoluta. Probabilidades normalizadas pela soma respondem a outra pergunta.

## Enumerar e agrupar

| Estado dos sítios | Peso | Massa nominal |
|---|---|---|
| LL | 9/16 | 100u |
| LP | 3/16 | 102u |
| PL | 3/16 | 102u |
| PP | 1/16 | 104u |

LP e PL têm a mesma massa e são somados. Pesos agrupados9/16,6/16,1/16; razão9:6:1. As probabilidades percentuais são56,25%,37,5%,6,25%, soma100%. Intensidades relativas ao maior são100,200/3,100/9, soma1600/9. Se o espectro incluísse outro pico mais intenso, o máximo global seria diferente e a escala teria de ser recalculada.

Com z=1, posições100,102,104; com as mesmas massas e z=2, posições50,51,52. Diferença nominal2u produz espaçamento2/z. Picos vizinhos quaisquer não permitem aplicar essa inferência sem atribuição e resolução adequadas.

Para n sítios iguais e independentes: P(k)=C(n,k)p^k(1−p)^(n−k). A massa nominal éM₀+2k. p=0 ou1 são casos degenerados válidos. Conjunto isotópico não fixa conectividade, isomeria ou identidade de um composto sozinho.

## Laboratório e contratos

`cluster.py` usa Python padrão e Fraction. n inteiro entre0 e12; z inteiro positivo; p entre0 e1; massa nominal inicial positiva. p e m0 aceitam inteiros/Fraction, sem bool ou float. Retorna número de pesados, posição m/z, probabilidade e intensidade relativa ao maior. Pode haver entradas de peso zero nos extremos; mais de um pico pode empatar no máximo.

Não calcula fragmentação, instrumento, massas exatas, estado eletrônico ou abundância empírica. A normalização pelo máximo refere-se somente ao conjunto fornecido. Não estima intervalos ou incertezas de observação.

Rodar da raiz do protótipo:

```sh
python3 -m unittest discover -s labs/massas-isotopos -t .
```

Cinco testes:30configurações por enumeração independente de sítios com sorteios primitivos equiprováveis; normalização/média/variância em65configurações; exemplo e espaçamento; translação de massa e extremos; contratos. O oráculo enumerado não usa a fórmula com coeficiente binomial. Os testes são evidência computacional finita, não validação química ou instrumental.

## Resoluções

1. Massa100u e z2:posição50.
2. LL:(3/4)²=9/16.
3. Um pesado:2(3/4)(1/4)=6/16=3/8.
4. PP:(1/4)²=1/16.
5. Dois pesados:massa104u.
6. Pico intermediário relativo:100(6/16)/(9/16)=200/3.
7. Espaçamento com z2:2/2=1.
8. Três sítios, um pesado:3(1/4)(3/4)²=27/64.
9. Pico base não é necessariamente íon molecular.
10. Normalização pelo máximo não exige soma100.
11. p=1/4 é sintético.
12. Razão compatível não fecha a identificação.

Desafio de três sítios:27/64,27/64,9/64,1/64, soma1. A repetição de massa agrupa escolhas de sítios, não novos picos para cada ordem.

## Fontes e alcance

[Programa CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214), item4, reaberto em27/10/2026; ativação15/07/2024 e captura indicada de dois meses antes. Versão efetivamente ministrada não comprovada. Massas recebe primeiro recorte; identificação integrada no item5 permanece outra lacuna.

Pavia/Lampman/Kriz/Vyvyan, *Introduction to Spectroscopy*, exemplar inglês identificado anteriormente como quinta edição: leitura parcial em27/10 das páginas impressas108,112,135–136, PDF128,132,155–156. P.135/PDF155 conferida visualmente. O corpo tem marcas digitais2013; os metadados anteriores registram copyright editorial2015. Não equiparado à segunda edição brasileira2015 da bibliografia oficial. Fonte usada para etapas de MS, interpretação de conjunto isotópico e cautela de atribuição; não se copiaram tabelas, espectros, valores de abundância ou exemplos. Sem leitura integral ou distribuição do PDF privado.

[OpenStax Organic Chemistry §12.1](https://openstax.org/books/organic-chemistry/pages/12-1-mass-spectrometry-of-small-molecules-magnetic-sector-instruments), leitura parcial em27/10: fonte/analisador/detector, m/z, íons/fragmentos e distinção entre pico base e molecular. Nenhuma figura ou espectro reproduzido.

## Próxima revisão e lacunas

Em20min, construir as quatro escolhas, agrupar massas e comparar as duas normalizações. Explicar o efeito de z sem inferir qualquer molécula real. Registro pessoal fica em branco. Fragmentação, ionização detalhada, resolução, massas exatas, misturas e identificação integrada com IR/RMN permanecem pendentes.
