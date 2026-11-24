# Lewis, octeto e carga formal — rascunho

Aula `q1-lewis-octeto`, QuímicaI/CCM0114:14 seções,12 exercícios,4MathML, exemplo, Python e painel. Primeiro recorte estrutural; não completa ligação/geometria. Aprovação histórica ou material elaborado não certificam domínio atual.

## Fontes e autoria

Consulta parcial ao acervo autorizado,22/10/2026: Atkins/Jones/Laverman, Princípios de Química,7ªed., Bookman2018, Tópico2B, pp.77–85 (PDF209–217). Definições de Lewis, ressonância e carga formal reconferidas textualmente. Edição distinta da3ªcitada no programa. Consulta direta parcial complementar: [OpenStax Chemistry2e §7.4](https://openstax.org/books/chemistry-2e/pages/7-4-formal-charges-and-resonance). Não se declara leitura integral. Nenhum PDF, figura ou solução foi redistribuído.

Nitrato e carbonato são exemplos conceituais comuns nas fontes. A enumeração exaustiva dos27 candidatos por espécie, os contrastes, textos, exercícios, diagrama e testes aqui são próprios, não transcrição de exercícios ou figuras. Não há medição, dado pessoal, cliente ou evidência da IC.

## Modelo e limites

Conectividade fixa X–O₁/X–O₂/X–O₃, X=N ouC. Ordens candidatas1..3, sem pares isolados no centro. Cada O recebe8−2b elétrons não ligantes. Total2Σb+Σ(8−2b)=24 em todos os27 candidatos; centro tem2Σb no entorno. CF centralV−Σb, CF porO=b−2. A soma é−1 em NO₃⁻ e−2 em CO₃²⁻, mesmo quando o octeto central é violado. Portanto total/carga corretos não bastam.

Octeto central exige soma4; três triplas positivas(2,1,1) e permutações. Médias formais sob equivalência: ordem4/3 e CF doO−2/3. Não são carga parcial ou ordem de ligação obtidas de cálculo quântico/experimento. Não atribuir pesos iguais a contribuintes não equivalentes. Ressonância não é equilíbrio, alternância temporal ou movimento dos núcleos.

Desenho esquemático com traços e pontos; posições fixas apenas para legibilidade. Não calcula ângulos, comprimentos, energia, distribuição real de carga ou estabilidade. C/N do segundo período não têm octeto expandido no recorte. Não há busca geral de estruturas, outras conectividades, radicais ou centros com pares isolados.

## Experiência de leitura e exploração

Tese visual: esquema azul com contagens em tabela e leitura editorial calma. Sequência: total → entorno → CF → restrição → ressonância → limites. Controles escolhem candidatos sem animar elétrons ou sugerir uma trajetória temporal. Tabela fornece os números também a quem não lê o diagrama. Controles em coluna no celular; navegação e soluções por teclado preservadas.

1. Comece no nitrato(2,1,1). Confira24,octetos e cargas+1/0/−1/−1.
2. Use(1,1,1):total e carga permanecem corretos,mas centro tem6.
3. Use(2,2,1):centro tem10,não admitido neste recorte.
4. Compare carbonato com o mesmo padrão e explique a diferença no centro.

## Verificação

`python3 -m unittest discover -s labs/lewis-octeto -t .`

Quatro testes: distribuição independente de elétrons com identidade em54 casos; enumeração dos contribuintes/médias racionais;324 permutações de sítios; contratos.54 referências Python/JS, incluindo contagem de pontos e traços no SVG. Testes não substituem revisão conceitual pessoal.

Próxima ação: explicar sem solução a diferença entre total da espécie e entorno de cada átomo. Estrutura eletrônica, periodicidade, VSEPR, polaridade, exceções ao octeto, orbitais, energia e aplicações experimentais permanecem pendentes.
