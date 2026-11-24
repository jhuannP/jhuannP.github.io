# Termos, somas e caudas

Rascunho original, sem certificação de domínio. Execute `python3 tails.py`, sem dependências adicionais. Fraction permite conferir exatamente somas finitas; a prova de convergência ou divergência não é substituída pela grade computacional.

## A condição que não basta

Sₙ→S finito implica aₙ=Sₙ−Sₙ₋₁→0. Se o termo não tende a zero, a série diverge. O caso aₙ→0 é inconclusivo.

Na harmônica, o bloco de índicesN+1 até2N contém N parcelas≥1/(2N). Então H(2N)−H(N)≥1/2. Em particular, H(2ᵏ)≥1+k/2; positividade leva a divergência para+∞ em todos os índices. A cauda não satisfaz o critério de Cauchy, apesar de1/n→0.

Para séries reais, Cauchy exige: para todo ε>0, existe N tal que para todos m>n≥N, |Sₘ−Sₙ|<ε. A necessidade segue da desigualdade triangular em relação à soma; a suficiência usa a completude de ℝ. A harmônica viola o critério com ε=1/2 e m=2n para qualquer corte.

Na telescópica bₙ=1/[n(n+1)], cancelamento finito fornece Bₙ=1−1/(n+1). A soma é1, resto1/(n+1), e qualquer cauda posterior é limitada por esse resto. Erro estritamente menor que0,01 pede N mínimo100; erro≤0,01 admite N99. O laboratório confere o corte com busca independente sobre somas finitas.

Agrupar1−1+1−1+… em pares só revela a subsequência par0; a ímpar continua1. A série não converge no sentido usual. Não são usados rearranjos ou métodos de soma generalizada. Alterar uma quantidade finita de termos muda somas parciais por constante a partir de certo índice e preserva convergência/divergência.

## Um acumulador pode parar de mudar

No procedimento testado, iniciar um float em10¹⁶ e adicionar1/n, n1..1000, deixa o acumulador inalterado por arredondamento. A referência racional aumenta cerca de7,48547. Isso é uma demonstração finita de estagnação desse procedimento na máquina testada, não um teste geral de erro, convergência ou divergência. A divergência da série com constante inicial e cauda harmônica é matemática, pela invariância sob alteração finita.

## Fontes consultadas parcialmente em27/10/2026

- Apostol, CalculusVolI,2ª edição1967,§10.11 p.394/PDF414,Teorema10.6 e distinção necessário/suficiente;§10.7 p.386/PDF406,identidade telescópica. Consulta textual parcial, sem nova inspeção visual ou leitura integral; alguns símbolos OCR são imperfeitos. Fórmulas e provas da aula conferidas algebricamente. PDF privado não distribuído.
- [OpenStax CalculusVol2§5.2](https://openstax.org/books/calculus-volume-2/pages/5-2-infinite-series),recortes da definição por somas parciais e telescopagem.
- [Júpiter CCM0123](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0123),reaberto em27/10/2026,ativação01/01/2025. Referência posterior à aprovação2024/1; versão da turma não recuperada. Apoio ao item2 de sequências/séries/integrais impróprias.

Deduções, valores, figura, exercícios e código próprios. Não reproduzimos exemplos dos autores. Outros critérios e teoria de séries continuam parciais; revisão pessoal pendente.

## Verificações

Cinco testes:160 blocos harmônicos e10 cortes diádicos;100 identidades telescópicas e500 caudas;14 cortes de precisão comparados a busca por somas exatas;200 somas oscilantes e prefixo float de1000 termos com referência racional; contratos e exemplos. Essas verificações são finitas; os argumentos gerais estão na aula.
