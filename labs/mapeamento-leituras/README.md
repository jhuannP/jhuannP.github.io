# Leituras curtas, posições e cobertura

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Teste local: python3 -m unittest labs.mapeamento-leituras.test_experiment.

Duas referências sintéticas de 24 bases, cinco origens 0/4/8/12/16,
comprimentos 4..8, fitas alternadas. Referência B repete um bloco de doze.
O buscador recebe apenas letras e referência; nunca recebe a origem.
Busca exata em ambas as orientações, conserva sobreposições e agrupa
palíndromos por intervalo. Unicidade de intervalo não garante a de fita.

Cobertura verdadeira usa origens conhecidas só no gerador. A segunda curva
retém só leituras de intervalo único; não soma a mesma observação inteira em
todas as posições candidatas. Soma de cobertura: 5L ou uL. No exemplo perfeito,
retida<=verdadeira em cada base; não se generaliza isso a qualquer alinhador.
No padrão B/L=6, só R3 é única, em [8,14): médias 1,25 e 0,25.
Zero retido não demonstra ausência de DNA. Sem erros, gaps, qualidade, N,
paired-end, variantes, genes ou calibração de amostragem biológica.

Quatro testes: 5120 buscas contra comparações letra por letra nas duas fitas;
intervalos palindrômicos, ausências e comprimento excessivo; cobertura por
vetor de diferenças independente nas dez coortes; conservação de massa,
origem contida nos resultados, complemento reverso, reversão de coordenadas,
destaque só visual e contratos. Cinquenta referências Python/JavaScript,
com correspondência das letras e massa da cobertura também verificadas em JS.
Um teste inicial detectou referência acidentalmente com 25 bases; a sequência
foi corrigida para duas cópias exatas de doze antes da validação da aula.

Fontes consultadas parcialmente em 16/10/2026:
- Alberts e colaboradores, Biologia Molecular da Célula VI, Artmed 2017,
  p. impressa 477 (PDF 513), sequenciamento/anotação; inspeção visual.
  Difere da quinta edição do programa, sem transferência de paginação.
  Custos e tempos históricos da página não são recomendações atuais.
- [NCBI FASTA](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/): cabeçalho
  e linhas de sequência. FASTA admite ambiguidades IUPAC; o código restringe
  ACGT e não é parser geral nem arquivo com qualidade por base.
- [UCSC bedGraph](https://genome.ucsc.edu/goldenpath/help/bedgraph.html):
  coordenadas com início zero e fim excluído, sem transcrever exemplos.

O arquivo referencias.fasta contém somente sequências inventadas; não é
submissão GenBank. Sem upload ou sequência real. Modelo e desenho próprios.
Visual: faixa de bases, tabela de candidatos, curvas em degraus com contraste
azul/preto. Interação: referência muda ambiguidade, comprimento muda letras,
destaque revela candidatas sem alterar cobertura. Sem animação temporal.
Pendente: qualidade, alinhamento aproximado, montagem, anotação, dados e
práticas da turma, revisão pessoal. Não comprova habilidade de bancada.
