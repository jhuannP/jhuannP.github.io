# Neurônios, glia e medida de um traçado

22/10/2026. Rascunho original assistido por IA, pendente de revisão pessoal de Jhuann. Aula `b4-neuronios-glia`:14seções/12exercícios. Recorte de estrutura celular e introdução à sinapse química, sem declarar comunicação neural completa.

## Fontes consultadas

- Bear, Connors e Paradiso, Neurociências: Desvendando o Sistema Nervoso,4ªedição brasileira,Artmed2017. Ficha e folha de rosto reconferidas no exemplar privado. Capítulo2:leitura parcial das páginas impressas24,29,39,42–44,49,52(PDF66,71,81,84–86,91,94). Página49/PDF91renderizada e inspecionada visualmente. Páginas50–51apareceram na extração, mas seus quadros de engenharia genética não fundamentam a aula. Não é leitura integral. A extração troca algumas unidades µm por mm; números morfológicos de referência não foram importados por esse OCR. Nenhuma figura, página ou PDF privado distribuído.
- [NICHD — partes do sistema nervoso](https://www.nichd.nih.gov/health/topics/neuro/conditioninfo/Pages/parts.aspx),aberto em22/10/2026:visão introdutória de neurônios, comunicação e glia. Não foram importadas contagens globais de neurônios ou a apresentação simplificada como regra universal de sinapse.
- [BrainFacts/Society for Neuroscience — Neurons and Glia](https://www.brainfacts.org/brain-anatomy-and-function/cells-and-circuits/2022/neurons-and-glia-113022),aberto em22/10/2026:estrutura e contribuições celulares introdutórias; não é revisão contemporânea de todos os mecanismos.
- [USP CCM0221](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221):programa reconferido no bloco anterior na mesma data;item2.2permanece parcialmente coberto. Seleção da turma e evidência pessoal não demonstradas pelo programa.

Não se adota proporção universal entre neurônios/glia, nem afirmação de origem de toda micróglia pelo sangue. Comunicação elétrica, potencial de repouso/ação, canais e integração sináptica ainda exigem desenvolvimento. Oligodendrócito/SNC eSchwann/SNPsão distinguidos;glia não é apenas preenchimento. O projeto de geometria abaixo é original, não exemplo copiado dos livros.

## Pergunta do projeto

Um traçado de três pontos2Dem pixels:(0,0),(120,h),(240,0). O comprimento da linha quebrada completa é2√(120²+h²)px. A distância entre pontas é240px. Com h160e calibração0,1µm/px, são40µm e24µm. Omitir o ponto intermediário mede a corda24µm. A razão5/3independe da calibração comum; um percurso fechado na rotina geral tem distância zero e razãoNone.

O painel varia altura0–160px,calibração isotrópica0,1–1µm/px e amostragem(três pontos ou só pontas). Desenho em pixels e mesma escala nos eixos; calibração muda os números físicos sem mudar a geometria. Preto:caminho completo sintético.Azul tracejado:caminho efetivamente medido. A tabela textual permite ler as medidas sem depender de cor ou desenho.

Não é imagem microscópica ou reconstrução3Dreal. Cada mudança de altura cria outra geometria sintética; não é deformação observada de um neurônio. Ruído,segmentação,ramos,calibração incerta e dimensãozestão fora do modelo. Para pontos correspondentes, projetar em2Dnão aumenta a distância euclidiana; isso não garante que uma reconstrução arbitrária/ruidosa seja um limite inferior preciso do comprimento real.

A geometria não identifica axônio/dendrito, sinapse, neurotransmissor, função ou velocidade. Não há tempos ou atividade simulados. Comprimento de uma linha quebrada não é área,volume ou superfície celular.

## Execução e verificação

Na raiz:

```sh
python3 labs/tracado-neurito/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos:triângulo3–4–5escalado e amostragem;invariância por translação/rotação/reversão e calibração;refinamento/projeção em161alturas;contratos e segmentos nulos.18estados Python/JScom três alturas,três calibrações e dois modos. A verificação geométrica não valida a neurobiologia ou um método experimental de rastreamento.

## Próximo passo

Revisão pessoal e confronto com materiais da turma pendentes. No próximo retorno neural, estudar gradientes iônicos e potencial de membrana no capítulo3do Bear; RC/osmose são apoios, não substitutos. Antes, alternar para outro percurso da biblioteca para preservar amplitude do objetivo.


Verificação final:566testes Python;239demonstrações/717cenários;325MathML;18estados de referência e interface desktop/390px conferidos. Teclado e resposta40 aprovados, sem erros observados no console ou transbordamento horizontal. Saldo91%; parada65%. Registro detalhado em PLANO_BIBLIOTECA.md na raiz. Revisão pessoal pendente.
