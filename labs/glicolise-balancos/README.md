# Glicólise e inventários — notas de aula

Rascunho original para revisão de Jhuann, 22/10/2026. Não é experimento realizado ou resultado de pesquisa.

## Uma via transforma matéria em etapas

Na glicólise clássica, ou via de Embden–Meyerhof–Parnas, uma glicose de seis carbonos dá origem a dois piruvatos de três carbonos. A sequência usual tem dez reações enzimáticas e ocorre no citosol. Aqui acompanhamos o esqueleto carbonado, transferências de fosforil e NAD⁺/NADH. Existem variantes e desvios em organismos e contextos diferentes; o roteiro não é um mapa universal de toda célula.



## Preparar não é ainda receber o saldo

A fase inicial converte glicose em intermediários fosforilados e investe ATP. Por glicose que percorre a via completa descrita, uma reação de hexocinase usa um ATP, e a fosfofrutocinase-1 usa outro. Dizer que a glicólise rende dois ATP líquidos não significa que nenhuma reação consuma ATP. O investimento e a produção devem aparecer separadamente no balanço.



## Etapas 1 a 3: duas fosforilações e uma isomerização

1. Hexocinase: glicose+ATP → glicose-6-fosfato+ADP. 2. Fosfoglicose-isomerase: glicose-6-fosfato ⇌ frutose-6-fosfato. 3. Fosfofrutocinase-1: frutose-6-fosfato+ATP → frutose-1,6-bisfosfato+ADP. Os esqueletos ainda têm seis carbonos. As expressões são abreviadas: omitem prótons, cargas e complexos com magnésio. As setas indicam o sentido contado, sem provar a reversibilidade de cada reação em qualquer composição.



## Etapas 4 e 5: duas trioses, uma mesma rota seguinte

A aldolase cliva frutose-1,6-bisfosfato em di-hidroxiacetona-fosfato, DHAP, e gliceraldeído-3-fosfato, GAP. Ambos têm três carbonos, mas não são a mesma espécie. A triose-fosfato-isomerase interconverte DHAP e GAP. Ao contar uma glicose inteiramente convertida a piruvato por esta via, as duas metades alimentam a sequência como dois GAP. Não conte só um porque o desenho da segunda fase tem uma única coluna.



## Etapa 6: oxidação, NADH e fosfato inorgânico

A gliceraldeído-3-fosfato-desidrogenase transforma GAP em 1,3-bisfosfoglicerato. A reação usa NAD⁺, que recebe equivalentes redutores e se torna NADH, e fosfato inorgânico Pi. O grupo fosforil acrescentado nessa etapa não vem de outro ATP. Como há dois GAP por glicose, contamos duas formações de NADH e o uso de dois Pi. O mecanismo de acoplamento não é substituído pela simples soma de espécies.



## Etapas 7 a 10: formar ATP nas duas cópias

7. Fosfoglicerato-cinase transfere um grupo fosforil de 1,3-bisfosfoglicerato ao ADP, gerando ATP e 3-fosfoglicerato. 8. Fosfoglicerato-mutase rearranja 3-fosfoglicerato em 2-fosfoglicerato. 9. Enolase remove água e forma fosfoenolpiruvato, PEP. 10. Piruvato-cinase transfere o grupo fosforil do PEP ao ADP e forma ATP e piruvato. Cada GAP que segue essa fase gera dois ATP; as duas cópias geram quatro.



## Conferir carbono antes de contar energia

Uma glicose tem seis carbonos e dois piruvatos têm 2×3=6. Na glicólise descrita não há liberação de CO₂. A quebra de uma molécula em duas não implica perder carbono. A tabela do laboratório segue apenas o esqueleto derivado da glicose; ATP e NAD também contêm carbonos, mas não são esse esqueleto e não entram nessa contagem reduzida. Um balanço atômico completo exigiria fórmulas e protonação das espécies.

6 C da glicose = 2×3 C dos piruvatos

## ATP bruto, gasto e líquido são contas distintas

Por glicose na via completa, duas formações de ATP ocorrem na etapa 7 e duas na etapa 10. A produção bruta é quatro. As duas fosforilações iniciais consomem dois. O saldo é quatro menos dois, ou dois ATP, acompanhado de dois NADH e dois piruvatos. NADH não é outro nome para ATP. Não converta NADH em uma quantidade universal de ATP sem especificar o processo posterior.

ATP líquido = 4−2 = 2

## Uma soma de reações cancela intermediários

No laboratório, cada reação é um vetor de consumo negativo e produção positiva. Para uma unidade de glicose, as extensões das etapas 1 a 5 são uma unidade cada, e das etapas 6 a 10 são duas. Ao somar, os intermediários G6P, F6P, FBP, DHAP, GAP, BPG, 3PG, 2PG e PEP têm saldo zero. No código, G6P é glicose-6-fosfato, F6P é frutose-6-fosfato, FBP é frutose-1,6-bisfosfato e BPG é 1,3-bisfosfoglicerato; PG3 e PG2 são 3-fosfoglicerato e 2-fosfoglicerato. GAP, DHAP e PEP foram definidos nas etapas acima. O resultado reduzido consome glicose, dois ADP, dois Pi e dois NAD⁺ e forma dois piruvatos, dois ATP, dois NADH e duas águas. Prótons/cargas ficam omitidos; não é uma equação completa balanceada para todos os átomos.



## O erro de esquecer a segunda triose

Se todas as dez reações forem contadas uma única vez, sobra um GAP, só um piruvato é formado e o saldo de ATP aparece como zero. Essa soma não representa a conversão completa de uma glicose a dois piruvatos. O carbono ainda pode fechar incluindo o GAP que sobrou; por isso conferir apenas seis carbonos no inventário não basta. Também precisamos verificar quais intermediários devem se cancelar. Esse erro é um dos testes do código.



## NAD⁺ precisa voltar a estar disponível

A etapa oxidativa reduz NAD⁺ a NADH. Para manter fluxo repetido, a célula precisa reoxidar NADH, por outras reações, regenerando NAD⁺. A glicólise em si não consome O₂ diretamente, e sua produção de ATP é por fosforilação no nível do substrato. Respiração e fermentação têm papéis distintos na regeneração e nos destinos do piruvato; não estão implementadas neste inventário. A ausência de O₂ na soma não torna dispensável o balanço redox.



## Regulação não pode ser lida só do saldo

A fosfofrutocinase-1 é um ponto importante de controle na via usual. Sua atividade responde ao estado metabólico e a efetores; não basta contar quantos ATP aparecem no final para prever a taxa. A variação real de energia livre depende das atividades de reagentes e produtos, como discutido na aula de acoplamento. Aqui não há concentrações, parâmetros cinéticos ou previsão de qual etapa controla o fluxo em uma condição real.



## O que a verificação computacional demonstra

O programa trabalha com extensões de reação em mol, incluindo frações de mol. Uma entrada 1/2 representa meio mol de glicose, não meia molécula individual. Ele confere estoques selecionados, cancelamentos e saldo de ATP. Não verifica disponibilidade inicial de ATP/NAD⁺, transientes, viabilidade termodinâmica ou conservação de todos os átomos e cargas. Alterar extensões é uma experiência de contabilidade química, não simular inibição de uma enzima.



## Revisar a química antes de usar como evidência

Reconstrua as dez transformações, identifique de onde vem cada grupo fosforil contado e explique o fator dois da segunda fase. Depois execute o laboratório e provoque o erro de uma só triose para interpretar o intermediário restante. As notas são rascunho assistido por IA. Regulação detalhada, mecanismos, rotas alimentadoras, fermentações, desvios e integração com outras vias ainda precisam de desenvolvimento e revisão pessoal.



## Exercícios e resoluções

- Quantos mol de piruvato surgem por mol de glicose que percorre integralmente a via clássica descrita? **Resolução:** Cada glicose fornece dois esqueletos de três carbonos.
- Quantos mol de ATP são consumidos na preparação por mol de glicose? **Resolução:** Um na hexocinase e um na PFK-1.
- Quantos mol de ATP são produzidos, antes de descontar o gasto, por mol de glicose? **Resolução:** Dois na etapa 7 e dois na etapa 10.
- Qual é o saldo líquido de ATP em mol por mol de glicose? **Resolução:** 4−2=2.
- Quantos mol de NADH são formados por mol de glicose neste recorte? **Resolução:** A etapa 6 ocorre duas vezes por glicose.
- Quantos carbonos da glicose estão nos dois piruvatos? **Resolução:** Dois piruvatos com três carbonos: 2×3=6.
- Para 1/2 mol de glicose completamente convertida, qual é o saldo de ATP em mol? **Resolução:** (1/2)×2=1 mol.
- Para converter 1 mol de glicose, alguém contou cada uma das dez etapas com extensão de 1 mol. Quanto GAP sobra no inventário, em mol? **Resolução:** Duas trioses alimentam GAP, mas a segunda fase consome só uma nessa contagem errada.
- O fosfato acrescentado na etapa da GAP-desidrogenase vem de outro ATP? **Resolução:** Essa etapa usa Pi e NAD⁺; não consome ATP diretamente.
- A glicólise descrita consome O₂ diretamente em uma de suas dez etapas? **Resolução:** O₂ não é reagente da via; reoxidação de NADH e vias posteriores são questões separadas.
- O inventário calcula a velocidade da glicólise em uma célula real? **Resolução:** Extensões e saldos não fornecem concentrações, parâmetros cinéticos ou mecanismos regulatórios.
- Os dois NADH podem ser contados automaticamente como mais dois ATP da própria glicólise? **Resolução:** São espécies e processos distintos; conversão posterior depende do sistema especificado.

## Fontes e reprodução

Nelson e Cox, Princípios de Bioquímica de Lehninger, sexta edição brasileira Artmed 2014, §14.1, pp.544–546,550,552–555/PDF574–576,580,582–585, consulta textual parcial em 22/10/2026. Página impressa e PDF usam convenção distinta; não é leitura integral do capítulo. Não foram copiados mecanismos, figuras, exemplos ou exercícios do livro. OpenStax Biology 2e §7.2, https://openstax.org/books/biology-2e/pages/7-2-glycolysis, apoio de visão geral e saldo, sem reprodução de imagens ou texto. Programa CCM0111, item 10, consultado em 22/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0111 ; ativação 15/07/2024. Ferramenta web informa captura de duas semanas antes; não demonstra versão ministrada à turma. Histórico não reaberto.

Na raiz do site: python3 -m labs.glicolise-balancos.experiment; python3 -m unittest discover -s labs/glicolise-balancos -t . . Só biblioteca padrão; entradas int/Fraction não negativas, sem bool ou float. Extensões em mol, não em segundos. combine aceita dez extensões para estudar somas parciais; isso não é um resolvedor de concentrações ou uma simulação de intervenção. O desafio importa o módulo local: conserve a pasta labs e execute na raiz.

Testes de estoques selecionados não são verificação de conservação de todos os átomos/cargas. O carbono mapeado é o esqueleto derivado da glicose; o mapa de fosforil exclui NAD, cujos grupos se conservam na transformação NAD⁺/NADH. Não se atribui a identificação de estoques a evidência de mecanismo ou fluxo. Próxima revisão pessoal: reconstruir a dupla contagem da segunda fase e explicar o erro de deixar GAP no final. Regulação detalhada, destinos do piruvato e vias seguintes continuam pendentes.

Conferência no navegador: pergunta de ATP líquido rejeitou 4 e aceitou 2. Esquema das trioses carregado e inspecionado a 390 px; fórmula de destaque encurtada e reconferida para caber em leitura direta. Siglas do código e unidade do exercício de GAP explicitadas. Sem transbordamento horizontal da página observado. Prévia glicolise-balancos-mobile.jpg. Catálogo: 499 aulas/2936 exercícios em rascunho. Saldo semanal 94%; parada operacional 65%.
