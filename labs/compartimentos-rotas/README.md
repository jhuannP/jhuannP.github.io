# Compartimentos e rotas selecionadas

Rascunho didático original. Quatro casos de proteínas codificadas no núcleo: nuclear, secretada solúvel, matriz mitocondrial e citosólica. Sinais/maquinaria adequados são hipóteses estipuladas. O painel não lê sequência nem calcula cinética.

Grafo próprio com seis localizações e cinco conexões selecionadas. Citosol→núcleo é passagem por poro; citosol→RE/matriz são translocações agregadas; RE→Golgi→exterior representa transporte vesicular da carga solúvel. Permanência citosólica não envolve deslocamento no grafo. A translocação para matriz agrega múltiplos passos e membranas; contar uma aresta não conta uma membrana física. A via secretora não exige terminar a tradução antes de entrar no RE.

A rede omite exportação nuclear, endocitose, retenção/recuperação, peroxissomos e muitas outras rotas. Ausência de caminho significa ausência no desenho, não impossibilidade biológica. Carga luminal em vesículas não cruza a bicamada a cada trecho. Diagrama não tem escala espacial, temporal ou probabilística.

## Fonte consultada

Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, tradução Artmed 2017, capítulo 12. Consulta parcial de trechos das páginas impressas 641–642 e 645–647; correspondência PDF 677–678 e 681–683. Página 646/PDF 682 inspecionada visualmente. Localização inicial pelo sumário foi conferida no corpo; o deslocamento do PDF é 36 páginas neste recorte, sem presumir regra para o livro inteiro. Seções posteriores sobre transporte nuclear detalhado não foram usadas como leitura integral neste bloco.

Texto, esquema e exemplos próprios. Não se reproduzem figuras do livro ou protocolos. O PDF privado não é servido. Não há dados experimentais, aplicação clínica ou evidência de execução do projeto pessoal antigo.

## Reproduzir e interpretar os testes

Na raiz:

```sh
python3 labs/compartimentos-rotas/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Dois testes locais: caminhos para todos os 36 pares de nós contra enumeração independente; categorias topológicas declaradas, casos e domínio. Quatro roteiros cruzados Python/JS. Esses testes verificam a consistência da representação e do algoritmo de busca; não testam se uma proteína real é importada ou se um mecanismo celular está validado. Busca de caminho é recurso de organização do roteiro, não modelo de reconhecimento molecular.

Próximas unidades: detalhes da maquinaria, direção e energia do transporte nuclear, entrada no RE, mitocôndrias e tráfego vesicular; organização nuclear e contexto tecidual permanecem pendentes. A aula amplia apenas parcialmente o grupo de compartimentos/endereçamento.


## Envelope e reconhecimento nuclear — 22/10/2026

Aula `b3-compartimentos-rotas` aprofundada de 14 seções/12 exercícios para 20/18. Preservados roteiro, laboratório e painel anteriores. Seis seções e seis exercícios distinguem membranas interna/externa, nucleoplasma/espaço perinuclear/citosol, continuidade com RE, caminho aquoso pelo poro, difusão/transporte mediado, NLS/importina/adaptador e introdução a Ran. Não trata massa molecular como limiar universal rígido nem confunde Ran-GEF com hidrólise promovida por Ran-GAP. O ciclo completo ainda não foi desenvolvido.

Fontes privadas: Alberts e colaboradores, Biologia Molecular da Célula, sexta edição, tradução Artmed 2017, capítulo 12, pp. 649–653, PDF 685–689. Extração e leitura parcial desse recorte; p. 649/PDF 685 visualmente inspecionada. Não se transfere paginação para outra edição nem se presume leitura posterior. As fontes de pp. 641–642/645–647 do roteiro anterior continuam registradas. Programa CCM0211 não reaberto neste bloco; preservada a conferência e a ressalva já registradas em 22/10.

Figura vetorial original `labs/compartimentos-rotas/envelope-nuclear.svg`: composição vertical e um único caminho dominante; membranas em preto, espaço perinuclear sombreado e seta azul com rótulo. Não copia figuras do livro, resolve arquitetura molecular do NPC ou mede fluxo. O desenho mantém as membranas contínuas nas margens do poro e separa o canal aquoso do espaço perinuclear. Sem animação ornamental; foco no caminho de leitura e na navegação por teclado. Renderer de aulas passa a aceitar figura opcional com caminho local restrito a /labs/, texto alternativo e legenda; campos escapados. CSS responsivo e carregamento diferido. O catálogo verifica existência/contenção do recurso, alt/legenda e descrição/viewBox SVG. PDF privado não servido.

O roteiro de evidência propõe comparação conceitual de localização com sinal funcional/alterado, discutindo integridade, expressão, exportação, retenção e degradação. Não é protocolo executado, medida de fluxo, resultado de IC ou domínio pessoal. Estado de rascunho mantido.

Mapa reconciliado: três aulas próprias/38 exercícios; cinco grupos parciais/11 lacunas, nenhum completo. Organização nuclear passa a parcial pelo recorte envelope/poro, mas lâmina, cromatina e arquitetura funcional continuam pendentes. Tráfego permanece lacuna, apesar do apoio de rotas; não confundir introdução com cobertura de revestimentos/fusão. Auditoria acima é fotografia anterior, não contagem atual.

Verificação: 780 testes Python e 458 estruturas MathML aprovados; sintaxe de learning.js conferida. Nenhum algoritmo científico Python/JS de laboratório ou simulação alterado; suíte de simulações não repetida. Navegador: figura carregada com texto alternativo, imagem e legenda legíveis em 390 px sem transbordamento horizontal; exercício 18 reconhece a resposta correta. Console sem erros observados. Prévia `envelope-nuclear-mobile.jpg`; viewport restaurado. Catálogo: 487 aulas/2589 exercícios, todos em rascunho.

Próxima ação pessoal: desenhar os três espaços sem consultar a figura e explicar por que nucleoplasma não é lúmen do RE. Próxima ampliação local: estudar ciclo completo de importação/exportação e separar acúmulo de fluxo antes de qualquer modelo quantitativo. Próxima alternância global: conferir a cobertura e a sequência de Química II, evitando desenvolver indefinidamente uma área. Saldo semanal após o bloco: 99%; parada em 65% preservada.

### Envelope nuclear: duas membranas, três espaços

O envelope envolve o material nuclear e possui membranas interna e externa. O nucleoplasma fica do lado nuclear da membrana interna; o citosol fica do lado externo da membrana externa. Entre as duas está o espaço perinuclear. A membrana externa é contínua com a membrana do retículo endoplasmático, e o espaço perinuclear é contínuo com o lúmen do RE. Isso não torna o nucleoplasma parte do lúmen do RE.

### O poro não desemboca no espaço perinuclear

Nas margens de um poro, as membranas interna e externa se unem. O complexo do poro nuclear, formado por proteínas chamadas nucleoporinas, organiza uma passagem aquosa seletiva entre citosol e nucleoplasma. A seta do esquema atravessa esse caminho, sem levar a carga para o espaço entre as membranas. O desenho só representa topologia: não mostra a arquitetura molecular completa do complexo, dimensões, permeabilidade ou velocidade.

### Difusão e transporte mediado são perguntas diferentes

Pequenas moléculas podem difundir pelo poro; a passagem passiva de macromoléculas é progressivamente restringida. Não vamos transformar uma massa molecular em uma fronteira universal e exata de transporte. No transporte mediado, a carga é reconhecida por receptores que interagem com o complexo do poro. Muitas proteínas podem passar dobradas ou em complexos; atravessar o poro não exige o mesmo processo de translocação através de uma bicamada usado em outras organelas.

### Sinal, receptor e adaptador não são a mesma peça

Um sinal de localização nuclear, abreviado NLS, é uma característica da carga reconhecida pelo sistema de importação. Importinas são receptores desse sistema; em algumas rotas, adaptadores fazem a ponte entre sinal e receptor. Existem diferentes sinais e modos de reconhecimento. Encontrar um trecho rico em aminoácidos básicos, isoladamente, não comprova importação: exposição do sinal, reconhecimento e contexto da proteína também importam.

### Reconhecimento permite passagem; direção exige outro mecanismo

Importinas interagem com nucleoporinas que possuem repetições FG, formadas pelos aminoácidos fenilalanina e glicina. Essas interações participam da passagem seletiva. A GTPase Ran alterna estados ligados a GTP e GDP; sua regulação compartimentalizada contribui para a direção do transporte. Ran-GEF nuclear promove troca de nucleotídeos e Ran-GAP citosólica estimula hidrólise de GTP. Não são o mesmo processo. O ciclo completo, a liberação da carga e a reciclagem precisam de uma unidade própria; não estão simulados neste grafo.

### Localização observada precisa de comparação

Um teste conceitual pode comparar a distribuição de uma carga fluorescente com sinal funcional e com sinal alterado, mantendo o restante do desenho comparável. É necessário verificar expressão, integridade da carga, estado celular e se a alteração afetou outras propriedades. Menor acúmulo nuclear é compatível com perda de importação, mas também exige considerar exportação, retenção e degradação. Localização em uma imagem não mede sozinha fluxo através do poro. Este é um roteiro para interpretar evidências, sem protocolo executado, imagens medidas ou resultado pessoal.

### O espaço perinuclear é contínuo com qual espaço?

A continuidade com o RE envolve o espaço entre as membranas nucleares, não o interior do núcleo.

### Uma carga importada pelo poro precisa entrar primeiro no espaço perinuclear?

O poro conecta citosol e nucleoplasma por um caminho aquoso seletivo.

### NLS, importina e adaptador são nomes da mesma molécula?

NLS é sinal da carga; importina é receptor; um adaptador pode mediar o reconhecimento.

### Ran-GEF nuclear e Ran-GAP citosólica catalisam a mesma operação?

GEF promove troca de nucleotídeo; GAP estimula hidrólise de GTP.

### Uma imagem de maior acúmulo nuclear mede sozinha a taxa de importação?

A localização também depende de exportação, retenção, degradação e outras condições.

### A passagem pelo poro exige sempre desenovelar a proteína como na translocação por membrana?

Muitas cargas nucleares atravessam dobradas ou em complexos; as vias têm mecanismos diferentes.
