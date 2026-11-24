# Teste da razão e cota do resto

27/10/2026. Rascunho original de12 seções/12 exercícios; revisão pessoal pendente. Pré-requisitos: limites, comparação e série geométrica.

## Estudar em dois blocos

1. Escolha q entre L e1 e demonstre a cota eventual de todos os termos seguintes. Explique por que a harmônica não admite uma margem uniforme q<1, embora cada razão seja menor que1. Compare com 1/n² e a alternada harmônica: os três comportamentos cabem em L=1.
2. Para bₙ=3ⁿ/n!, some de n=0 até N e derive a cota a partir da primeira parcela omitida. Em N=8, b₉=243/4480 e q=3/10, produzindo243/3136. Diferencie a cota do erro real.

## Código

Execute `python3 labs/razao-cauda/ratio.py` na pasta do protótipo. Usa Fraction, sem dependências externas. Compara termos fatoriais com a razão simplificada, quarenta parcelas de cada cauda com uma majorante geométrica e somas finitas com a cota. Esses testes são finitos; a garantia para a série infinita vem da demonstração, não da enumeração.

`choose_N` busca o primeiro índice aprovado pela cota estrita, não necessariamente o primeiro com erro real suficiente. Para c=3,ε=1/1000, retorna12. Se o orçamento acaba sem certificado, retorna None, sem concluir divergência. `tail_bound` rejeita uma escolha com q>=1; isso apenas torna aquela majorante inadequada.

A figura mostra razões de termos consecutivos, não somas parciais. A harmônica diverge e a série1/n² converge, apesar de razões menores que1 em todos os índices. O script não implementa um classificador geral de séries, manipulação simbólica ou provas a partir de amostras.

## Fontes e limites

- Apostol, Calculus,vol.1,2ªedição1967, §10.15 pp.400–401/PDF420–421, consulta textual parcial em27/10/2026 no acervo autorizado. Teorema10.13 e advertência sobre razões menores que1. Sem leitura integral, nova inspeção visual ou distribuição do PDF privado.
- [OpenStax Calculus2 §5.6](https://openstax.org/books/calculus-volume-2/pages/5-6-ratio-and-root-tests), consulta textual parcial ao enunciado e à prova do teste da razão, em27/10/2026. Redação própria explicita a cota geométrica e o critério do termo geral. Sem copiar figuras ou exercícios.

O exemplo fatorial com c=3, desenho, código e exercícios são próprios. Teste da raiz, limsup, razões sem limite e critérios mais finos continuam pendentes. MatemáticaII e seu grupo de séries seguem parciais. Material preparado não comprova estudo ou domínio de Jhuann.
