# Micróglia: máscaras, denominadores e níveis de evidência

Atividade original de contabilidade geométrica. Todos os pontos, intensidades e dimensões são fictícios, sem imagens biológicas ou dados do artigo. M representa uma célula escolhida, S sinal binário e L um compartimento fictício. Todas as máscaras estão na mesma grade uniforme e referencial. A interseção de conjuntos não demonstra moléculas, fagocitose, sinapses eliminadas ou consequência funcional.

`measure(M,S,L,spacing)` calcula contagens e volumes. Coordenadas são tuplas de três inteiros; coleções explícitas list/tuple/set/frozenset são aceitas e duplicatas se tornam um voxel. Bool/float ou dimensões inválidas são rejeitados. Spacing tem três int/Fraction positivos. M precisa ser não vazia. L pode ser uma máscara de campo com regiões externas; a conta utiliza interseção com M. Sem registro, interpolação, segmentação automática ou identificação celular.

Modelo: M ocupa x,y∈{0,1},z∈{0,1,2},12 voxels. S no limiar10 tem A(0,0,1),B(1,1,2),C(0,1,4),D(1,0,5),E(2,2,1). Só A/B estão dentro. L contém(0,0,1),(0,1,0),(1,0,1); apenas A é sinal interno coincidente com L. As três razões são ocupação2/12=1/6, fração interna do sinal2/5 e fração lisossomal do sinal interno1/2. Nenhuma é contagem de sinapses. São distintas por denominador e condicionamento.

Voxel0,5×0,5×2µm→0,5µm³. Volume celular6µm³, interno1µm³, razão1/6. Dobrar todas as dimensões multiplica volumes por8 e preserva as razões. Dados de grids diferentes não podem ser cruzados só porque suas listas de índices parecem iguais; código não corrige isso.

`projection_xy_overlap` descarta z e conta posições xy distintas sobrepostas. É projeção binária por união, não integração de intensidade ou análise de microscopia. No modelo,4 de5 posições se sobrepõem emxy, mas2 de5 voxels estão dentro em3D. Mover todos os pontos de S dez unidades emz mantém a projeção e elimina a interseção3D. Sinais diferentes com mesmo xy colapsam na projeção; não se deve usar essa contagem como volume.

`threshold` inclui intensidade≥limiar. A20/B12/C18/D16/E30 são unidades arbitrárias prescritas. Limiar10 dá ocupação1/6;15 dá1/12;25 dá0, sem alterar M ou simular qualquer biologia. `cell_aggregates` recebe contagens(M,I) de células em escala comum: para(10,2),(90,9), média por célula15% e razão agrupada11%. A primeira pesa células igualmente, a segunda pesa volumes. Isso não escolhe unidade experimental ou estimando por conta própria. Células do mesmo animal não equivalem a animais independentes; sem teste estatístico, significância ou inferência populacional.

Quando S é vazio, ocupação0 é legítima com M não vazio, mas fração interna relativa a S éNone. Quando S∩M é vazio, fração lisossomal condicionada ao interno éNone. Não trocar ausência de denominador por zero. Código usa racionais em contas prescritas, sem corrigir máscaras mal definidas.

Da raiz:
```
python3 labs/microglia-mascaras/masks.py
python3 -B -m unittest discover -s labs/microglia-mascaras -t .
```
Seis testes:fixture e escala física;256 configurações de sinal/compartimento em grade reduzida contra lógica booleana por sítio;perda de profundidade pela projeção;limiar e inclusão de igualdade;estimandos de agregação;contratos/denominadores vazios. Verifica cálculo, não biologia ou pedagogia.

Fontes lidas em recortes29/10/2026:
- Bear/Connors/Paradiso,Neurociências,4ªbrasileira2017,p52/PDF94,trecho de função fagocitária e remodelação em Outras Células Não Neuronais,texto e página visual. Origem celular não desenvolvida;figuras e PDF privados não distribuídos.
- Schafer et al.,Neuron74,2012,DOI10.1016/j.neuron.2012.03.026,trechos de resultados e discussão no PDF dos autores. Não houve leitura integral,inspeção de figuras ou suplemento,extração de valores experimentais ou reanálise. A páginaPMC pediu verificação de navegador;usada a cópia pública do laboratório dos autores. Uma chamada de screenshot não forneceu imagem inspecionável;consulta do artigo foi textual. Esta atividade numérica não reproduz a análise experimental do artigo.
https://stevenslab.wordpress.com/wp-content/uploads/2012/07/dori-neuron-paper.pdf
- JúpiterCCM0221,reabertura29/10/2026,ativação01/01/2025,item1.11 como sistema possível. Aprovação2026/1 não comprova versão/seleção efetiva ministrada.
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221

Revisão pessoal de Jhuann pendente. Primeiro recorte de neuroimunologia;não cobre origem e diversidade microglial,patologias,dinâmica ou causalidade geral. Sem resultado biológico próprio.
