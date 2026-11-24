# Transgene: distinguir herança, detecção e expressão

Modelo conceitual original; não é instrução de produção, manejo ou modificação de organismos. Grandezas são probabilidades e contagens. Não há amostra, ensaio ou resultado produzido por Jhuann.

## Percurso de20 minutos

Defina T como um estado cromossômico com inserção e + como o correspondente sem ela, em um único locus autossômico diploide. Uma inserção pode conter mais de uma cópia molecular: T/+ não conta cópias de DNA. Assumimos segregação equiprovável, gametas independentes entre progenitores, ausência de distorção, genótipos conhecidos e nenhuma diferença de sobrevivência inicialmente.

T/+×+/+ dá1/2 T/+ e1/2 +/+. T/+×T/+ dá1/4 +/+,1/2 T/+,1/4 T/T; se a leitura apenas distingue presença de T, sua probabilidade é3/4. Não se obtém uma razão de expressão ou função dessa distribuição.

Se T/T não sobrevive no cenário escolhido, as probabilidades na concepção continuam1/4,1/2,1/4. Entre sobreviventes, normalize por3/4:1/3 +/+ e2/3 T/+. Isso é condicionamento, não uma mudança da segregação. Não se presume letalidade em organismos reais.

Em oito descendentes independentes e todos observados, com p=1/2 de presença, a probabilidade de exatamente seis é C(8,6)/2⁸=7/64. O número esperado é4, sem exigir exatamente quatro em toda família. Desvio da razão não prova uma explicação alternativa; amostra, seleção e detecção devem ser avaliadas.

## Mesma proporção, modelos distintos

Duas inserções em loci diferentes, ambas presentes em uma das duas cópias cromossômicas e independentes, dão probabilidade3/4 de pelo menos uma na descendência de uma comparação com indivíduo sem ambas. Porém dois sítios em ligação completa cis podem viajar juntos nos gametas:00 ou11, cada um com1/2, e dar presença1/2. Uma proporção não determina número de sítios, cópias ou posição genômica. Independência precisa ser hipótese, não inferência do número de sítios.

Em organismo com populações de células geneticamente distintas, resultado de um tecido não determina composição da linhagem germinativa. Não se atribui automaticamente p=1/2 a qualquer fundador. Quimerismo e mosaicismo têm origens diferentes e não são usados como sinônimos. A expressão também depende de regulação, tecido, estágio e condições; presença de DNA, expressão e função são afirmações distintas.

## Camada de observação

Se p é presença real, s a sensibilidade e f a chance de positivo sem presença, P(positivo)=p s+(1−p)f. Parâmetros são sintéticos, não desempenho de método. Para p=1/2,s=3/4,f=0, resultado3/8 e expectativa3 em oito. Um ensaio positivo não fornece sozinho posição da inserção, cópias, transmissão ou atividade. Controles e medidas independentes precisam corresponder à afirmação investigada; não há protocolo de bancada neste laboratório.

## Execução e verificação

Python3, biblioteca padrão e Fraction. Execute `python3 labs/transgene-heranca/inheritance.py`; testes `python3 -m unittest discover -s labs/transgene-heranca -t .` na raiz. Contratos: doses de locus0,1,2, até8 loci independentes, até20 descendentes e probabilidades exatas; limites didáticos. Quatro testes com enumeração de gametas, estados independentes e512 sequências de oito resultados, além de casos ligados/seleção/contratos. Não são simulações de organismo real nem cálculo de significância de um experimento.

Fontes consultadas parcialmente em29/10/2026: Alberts e colaboradores, Biologia Molecular da Célula, tradução6ªed., Artmed2017, cap8 pp.495–496/PDF531–532 (texto extraído: engenharia, modificação genômica, linhagem germinativa, genótipos e consequência de ausência de gene; sem nova inspeção visual ou leitura integral). [NHGRI: Transgenic](https://www.genome.gov/genetics-glossary/Transgenic), definição e contexto geral. As fontes usam amplitude terminológica diferente: Alberts inclui alterações/substituições; o glossário NHGRI enfatiza DNA de outra espécie. Aqui o caso é explicitamente uma inserção T, sem chamar toda edição genômica de transgenia. Página específica Germ-Line não acessível, não contada como leitura. Programa oficial CCM0121 conforme registro29/10, ativação01/01/2025, versão ministrada não comprovada; não reaberto neste bloco.

Exemplos, probabilidades, desenho, código e exercícios próprios; sem copiar figura ou estudo do livro e sem distribuir PDFs. Pendentes: métodos e espécies reais, efeitos de posição, validação de inserção, evidências pessoais e revisão de Jhuann.
