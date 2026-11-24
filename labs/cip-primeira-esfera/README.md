# R/S: prioridades antes de orientação

Recorte original, não um resolvedor CIP geral. Quatro átomos diretamente ligados ao carbono central; prioridade por número atômico Z e, somente entre isótopos do mesmo elemento, número de massa A. Entradas isotópicas são explícitas, não massas atômicas médias. O código não valida existência ou estabilidade de todo núcleo permitido pelo contrato.

## Sessão1 — atribuir e olhar

Para os ligantes diretamente ligados ⁷⁹Br,³⁵Cl,¹⁹F e¹H, temos prioridades1,2,3,4 porque35>17>9>1. Eletronegatividade não é o critério. Entre²H e¹H, o primeiro tem prioridade maior, embora Z seja igual. Empates entre dois carbonos com grupos posteriores distintos exigem examinar a conectividade; somar todos os números atômicos do grupo é inadequado. Essas regras posteriores e ligações múltiplas não são implementadas.

Eixos destros, observador em+z olhando para a origem, x para direita e y para cima. Coordenadas escolhidas na ordem de prioridade: r1=(0,2,1),r2=(2,−1,1),r3=(−2,−1,1),r4=(0,0,−3). O grupo4 aponta para longe; a projeção1→2→3 é horária, logoR. A imagem refletida em x éS. É geometria esquemática, não estrutura molecular medida ou tetraedro regular exigido pelo programa.

## Sessão2 — calibrar o cálculo

D=det(r1−r4,r2−r4,r3−r4), com os três vetores como linhas (ou como colunas, dando o mesmo determinante transposto). Na referênciaD=−48, correspondente aR sob a convenção explícita. Não se atribuiR/S ao sinal de qualquer determinante arbitrário: ordem de prioridades, eixos e calibração são essenciais. A figura da aula anterior de quiralidade usava um escalar auxiliar diferente e continua sem atribuição automática.

Rotação própria aplica matriz de determinante+1, preservandoD e configuração; reflexão espacial muda o sinal. Trocar fisicamente dois grupos distintos mantendo os demais fixa inverte a configuração. Reordenar registros junto com suas coordenadas não troca os grupos na molécula. Translação desaparece nas diferenças. Dzero sinaliza geometria degenerada para esta representação; não é um teste universal de quiralidade molecular.

R/S descreve configuração, não sinal ou magnitude da rotação óptica. Reconhecer um centro não classifica automaticamente uma molécula inteira com vários centros, simetrias ou meso. Atribuição correta depende da estrutura e não é medição de uma amostra.

## Código

Python3, biblioteca padrão. `priority` retorna índices de registros em ordem decrescente; `configuration` reordena posições correspondentes e calculaD. Rejeita prioridades empatadas sem concluir automaticamente aquiralidade: grupos podem exigir esferas posteriores. Coordenadas inteiras em módulo até20 e quatro átomos(Z,A) são limites didáticos. Sem inferir geometria, ligações múltiplas ou estruturas a partir de um desenho arbitrário.

Execute `python3 labs/cip-primeira-esfera/configuration.py`; testes `python3 -m unittest discover -s labs/cip-primeira-esfera -t .`. Quatro testes: prioridade/isótopos e calibração projetada;24 rotações próprias/24 reflexões por permutações assinadas dos eixos;24 reordenações, troca física e translação;contratos. Testes finitos não substituem regras CIP completas ou revisão pessoal.

Fontes consultadas parcialmente em29/10/2026: Brown/Poon, Introduction to Organic Chemistry,6ªed2016,§6.3 p.166/PDF186, convenção de orientar grupo4 e ler1→2→3 (texto extraído; sem nova inspeção visual/leitura integral). [McMurry/OpenStax §5.5](https://openstax.org/books/organic-chemistry/pages/5-5-sequence-rules-for-specifying-configuration), regras de primeira esfera/isótopos, orientação e independência da rotação óptica. Sem copiar modelos moleculares, exemplos resolvidos, figuras ou exercícios das fontes. Todas as coordenadas,comparações,código e diagrama são próprios. Programa oficial CCM0224 não reaberto: registro22/10/ativação01/01/2025 preservado, versão ministrada desconhecida.

Pendentes: regras recursivas,empates avançados,pseudoassimetria,E/Z,centros múltiplos,meso e revisão pessoal. Conteúdo preparado com IA não é evidência de domínio de Jhuann.
