# Alinhamento aproximado sem gaps

22/10/2026. Rascunho original, pendente de revisão pessoal. Continua `lab1-mapeamento-leituras` e `lab1-qualidade-fastq`; não substitui os modelos anteriores. É recorte complementar do tema amplo Genômica em CCM0215, sem afirmar que esse algoritmo foi ensinado na turma ou executado por Jhuann em pesquisa.

## Modelo, parâmetros e coordenadas

Referência inventada `ACGTTACGAT`; cinco leituras de quatro bases: `CGTT`, `GGTT`, `CGCT`, `CCCC`, `ACGT`. São sete janelas × duas orientações, incluindo candidatas palindrômicas em ambas as fitas. Custo de Hamming: número de discrepâncias letra a letra, sem gaps, recorte, bases ambíguas ou leitura pareada. Aceitar d≤k e conservar todas as melhores pelo menor custo são operações distintas. Nenhuma origem conhecida é passada à busca.

API: DNA ACGT maiúsculo com 1..256 bases; limite inteiro de zero ao comprimento da leitura; Q10/20/30/40. Leitura maior que referência produz lista vazia. Início zero e fim excluído na API; painel mostra início um e extremos inclusivos. `GGTT` tem melhor comparação + em [1,5) na API, [2,5] no painel. `CGCT` empata em posições 2–5 e 7–10, orientação +. `CCCC` tem custo mínimo três e não passa pelo corte máximo dois. `ACGT` tem um intervalo e duas orientações melhores; não são duas observações independentes.

## Qualidade, custo e verossimilhança

Q é uniforme em todas as bases, escolhido hipoteticamente. p=10^(−Q/10). Modelo adicional: probabilidade 1−p para uma letra correta, p/3 para cada letra incorreta e independência entre posições. Logo L=(1−p)^(Lread−d)(p/3)^d. Para quatro bases, Q20 e d=1: 0,00323433. A esperança de erros é 0,04; discrepância observada, esperança e probabilidade são objetos diferentes.

O cálculo é P(leitura|janela e orientação verdadeiras, modelo), sem prior de origem ou alternativa de referência ausente; não é posterior nem MAPQ. Para p≤0,1, aumentar d reduz a verossimilhança. Com qualidades homogêneas e comprimentos iguais, a ordenação coincide com Hamming e empates continuam empatados. Não generalizar para qualidades heterogêneas. O painel não recebe registros FASTQ reais nem reverte um vetor de qualidades heterogêneas. A quantidade de discrepâncias não identifica variante ou erro de sequenciamento.

## Fontes e limites de atribuição

- Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, Artmed 2017, p. 477 (PDF 513): texto reconferido parcialmente por extração em 22/10/2026, blocos de sequenciamento e anotação. Já havia consulta/inspeção visual registrada na aula de mapeamento em 16/10. É contexto biológico, não fonte da implementação Hamming ou da verossimilhança própria. Custos/tempos históricos não usados como recomendações atuais. A quinta edição citada no programa continua não confirmada. Arquivo privado não distribuído.
- [SAM v1.6, especificação, impressão de 12/08/2025](https://samtools.github.io/hts-specs/SAMv1.pdf), consulta parcial direta em 22/10/2026: §§1.2 e 1.4, múltiplos mapeamentos, coordenadas, qualidade por base, MAPQ e operações CIGAR. MAPQ refere-se à probabilidade de a posição estar errada, diferente da qualidade por base. O laboratório não exporta SAM/BAM/CIGAR nem calcula MAPQ.
- [Manual BWA](https://bio-bwa.sourceforge.net/bwa.shtml), consulta parcial direta em 22/10/2026, descrição BWA-MEM e opções: sementes, extensão com gaps e penalidades são recursos que esta enumeração curta não implementa. Sem executar ou recomendar BWA para dados deste usuário.
- A escala de qualidade usa também a documentação NCBI SRA/Illumina já registrada na aula FASTQ. Política de corte e modelo equiprovável de substituições são escolhas didáticas próprias, não protocolo validado.

## Verificação

Quatro testes Python: 256 referências de quatro bases × 16 leituras de duas bases × três cortes, com enumeração independente de ambas as orientações; distribuição racional de todas as 256 leituras de quatro bases dada uma janela, em três qualidades, soma um; empates, palíndromos, monotonicidade do corte e invariância da ordenação em Q homogêneo; contratos e leitura longa. Testes não demonstram qualidade de um alinhador real.

`reference.json`: 60 estados (cinco leituras × três cortes × quatro qualidades), cada um com 14 candidatas e suas probabilidades convertidas de Fraction. JS confere custo, letras, posições, orientações, aceitação, melhores/intervalos e verossimilhança. Cálculo Python exato; gráfico e valores JS em ponto flutuante.

Tese visual: bases alinhadas no mesmo eixo, sem decoração. Conteúdo: teoria → comparação resolvida → letras e discrepâncias → tabela completa → Python/exercícios. Interações: leitura muda ambiguidade; corte muda aceitação; Q muda verossimilhanças; tabela se revela por teclado. × e texto acompanham o destaque de cor. O gráfico limita a três melhores linhas; a tabela mantém todas as candidatas. Nenhum movimento sugere produção de dados.

## Pendências

Revisão pessoal, gaps e modelos mais gerais, qualidades heterogêneas, calibração, montagem, anotação, sequências reais autorizadas e rastreabilidade de práticas. Próximo desenvolvimento conceitual de Laboratório I: técnica/pergunta/controle, com leitura do corpo correspondente do Alberts e distinção explícita de atividade proposta e experiência pessoal. Cinco grupos do mapa continuam sem desenvolvimento próprio; este recorte não completa Genômica ou a disciplina.
