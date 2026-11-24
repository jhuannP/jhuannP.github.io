# Qualidade e FASTQ — dados sintéticos

22/10/2026. Rascunho original preparado com apoio de IA, pendente de revisão de Jhuann. Não comprova sequenciamento, análise de amostra pessoal ou prática de CCM0215.

## Modelo e limites

Três perfis de seis qualidades: uniforme 20; quatro 40 seguidas de duas 10; uniforme 30. Sequência inventada ACGTAC em todos. Não há erros sorteados nem medidos. O controle soma um deslocamento inteiro de −10 a zero a todas as qualidades. Isso é alteração hipotética, sem calibração. O seletor muda só o destaque, sem alterar o conjunto.

O laboratório deriva a esperança de uma soma de indicadores, os limites de união e o resultado sob independência. A comparação é de marginais declaradas. Não há teste ou evidência de independência, acurácia de sequenciador, variantes, anotação, alinhamento ou MAPQ. E não é uma contagem observada; não precisa ser inteiro nem ficar abaixo de um. Uma soma de probabilidades e um produto de complementos respondem a perguntas distintas.

A política inventada retém a leitura inteira se E≤limite, sem tolerância acrescentada ao corte; limite 0..3. Valores decimais são calculados em ponto flutuante. O painel não recomenda um limiar, não recorta bases e não reestima cobertura. Em padrão, E=[0,06;0,2004;0,006]; limite 0,1 retém leituras 0 e 2. A média aritmética de Q da heterogênea é maior, mas seu E também é maior. O Q equivalente é uma transformação da probabilidade média, não certificado de confiança.

O leitor é deliberadamente restrito: quatro linhas por registro, separador exatamente +, identificador não vazio, ACGTN maiúsculo e Q0..40 em Phred+33. Não é parser FASTQ geral: sem detecção automática de offset, variantes de codificação, linhas dobradas, compressão, streaming de arquivos grandes ou pareamento. Qualidade e sequência têm o mesmo comprimento. N é preservado como chamada não resolvida, sem inferir base verdadeira. O arquivo synthetic.fastq contém somente os três registros inventados; não inclui dado privado.

## Fontes

- [NCBI SRA, File Format Guide](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/): consulta direta parcial, bloco FASTQ e convenções de codificação, em 22/10/2026. Exemplos oficiais não foram copiados. O recorte do parser não representa toda a especificação ou regras de submissão.
- [Illumina, Quality Scores](https://help.basespace.illumina.com/files-used-by-basespace/quality-scores): consulta direta sobre escala e codificação, em 22/10/2026; sem avaliar tabelas reais de calibração ou binning.
- Alberts, sexta edição, Artmed 2017: o sumário anteriormente extraído localiza sequenciamento/anotação em p.477. Corpo não lido neste bloco; não atribuir a ele a especificação FASTQ, as fórmulas derivadas ou a política do painel. Quinta edição citada no programa continua não confirmada.

Uma tentativa de acessar FASTQ.pdf em hts-specs retornou 404; não é referência usada.

## Verificação e uso

Na raiz:

```sh
python3 labs/qualidade-fastq/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes: codificação de todos os 41 valores e registros inválidos; enumeração de distribuições conjuntas independentes com frações exatas para quatro perfis; monotonicidade dos 61 cortes em 11 deslocamentos, invariantes e fronteira; contratos inválidos. A enumeração verifica esperança/probabilidade por outro caminho, sem usar Monte Carlo como prova. O contraexemplo de dependência preserva marginais com união distinta.

reference.json tem 27 estados (3 destaques × 3 deslocamentos × 3 cortes) cruzados com JS: estatísticas, codificação, decisões e quantidade retida. Testes de software não demonstram calibração experimental. A regra de corte é somente ferramenta para discutir seleção e perda de informação.

## Composição e interação

Tese visual: manter a superfície editorial clara da biblioteca, com um perfil por base como figura central. Plano: teoria → contraste resolvido → perfil/tabela → Python → exercícios e limites. Interação: controles atualizam perfil e decisões; destaque seleciona uma leitura sem alterar as outras; tabela por base se revela sob demanda. Sem animação que sugira aquisição de dados ou tempo experimental.

## Pendências

Revisão pessoal; calibração com fonte/dados adequados; erros reais e alinhamento aproximado, montagem e anotação; conferir práticas e entregas da turma. Não transformar o material sintético em experiência profissional demonstrada sem evidência pessoal.
