# RMN: convolução de acoplamentos em primeira ordem

Laboratório original de linhas discretas,sem dados de molécula ou espectro experimental. Um spin observado é acoplado a vizinhos spin1/2 com projeções±1/2,independentes,equiprováveis na aproximação adotada. Deslocamento relativo emHz éΣJj mj. Não se modelam populações térmicas exatas,amplitudes de pulsos,FID,relaxação,troca,largura,ruído ou efeitos de segunda ordem. J são entradas prescritas;sem estrutura ou cálculo de J eletrônico.

`sticks(groups)` aceita lista/tupla de pares(n,J_Hz),n inteiro positivo,J int/Fraction,até12 vizinhos totais. Lista vazia é singleto. Sinais de J são permitidos;com projeções simétricas independentes o padrão isolado não identifica esses sinais. Um grupo com n vizinhos e mesmo J usa pesos binomiais C(n,k)/2^n e posições(k−n/2)J. Convolução entre grupos soma posições e multiplica pesos. Coincidências exatas são agregadas;não há aproximação por tolerância ou simulação de resolução instrumental. J=0 é aceito e agrega todas contribuições. Grupos de igual J não certificam equivalência química/magnética.

O algoritmo assume regime de primeira ordem. Não recebe deslocamentos de todos os vizinhos,não checaΔν/|J| e não decide se a aproximação vale para uma molécula. Especificar centros separadamente não resolve o Hamiltoniano fortemente acoplado. Mesmoδ não basta para equivalência magnética;esta exige acoplamentos iguais a cada outro núcleo relevante. Limite de12 é operacional,didático,não lei física.

`positions_ppm` usaδlinha=δcentro+offsetHz/νrefMHz;νref>0. Racionais exatos em todas as entradas,int/Fraction;floats,bool e texto rejeitados. Retorno crescente por conveniência,a figura química costuma exibir ppm decrescente. Figura deste bloco usaHz relativos crescentes,assim rotulados. `moments` é helper dos traços normalizados;variância de posições não é largura de linha ou incerteza experimental. Conserve área somando pesos de todo o multipleto;num grupo comN prótons observados e resposta quantitativa igual,área relativaN multiplica cada peso. Número de vizinhos não é número de prótons observados.

Exemplos próprios:
- J6,6Hz→linhas−6,0,+6 e pesos1/4,1/2,1/4.
- J6,2Hz→linhas−4,−2,+2,+4 e pesos1/4cada. Intervalos adjacentes2,4,2Hz;não dão diretamente todos osJ. Jgrande=linha3−linha1=6Hz.
- J6,3Hz→linhas−4,5,−1,5,+1,5,+4,5 com pesos1/4cada;quatro linhas igualmente espaçadas não significam quarteto binomial.
- J6,6 em grupos separados produz o mesmo desenho do primeiro caso,sem provar equivalência.
- Centro2ppm,νref400MHz,J6,2→1,99;1,995;2,005;2,01ppm. Em800MHz os offsets emppm caem pela metade,J emHz não muda,mesmas condições químicas.

Roteiro:prever padrões,somar pesos e calcular centro/variância. Para projeções independentes,centro de offsets0 e variânciaΣJj²/4 emHz²,uma prova por momentos que independe da convolução. J6,2 dá10Hz². Isso não é variância de espectro alargado. ParaΔδ0,1ppm e|J|8Hz,referências100/400/800MHz dãoΔν10/40/80Hz e razões1,25/5/10;campo maior melhora separação relativa,sem limiar universal ou validação automática de primeira ordem.

Executar da raiz:
```
python3 labs/rmn-acoplamento/multiplet.py
python3 -B -m unittest discover -s labs/rmn-acoplamento -t .
```
Seis testes:fixtures de coincidências/tripleto/dd;1093 listas de acoplamentos tamanho0…6,em{0,2,3},comparadas a enumeração independente de todas as projeções±1/2;12 tamanhos agrupados versus spins separados;27 casos de momentos/simetrias;três escalas de campo e área;contratos. O oráculo não usa coeficiente binomial nem convolução.

Fontes parcialmente consultadas29/10/2026:
- Pavia,Lampman,Kriz,Vyvyan,Introdução à Espectroscopia,tradução da4ªedição norte-americana,arquivo identificado2010. Cabeçalho da tradução conferido;ano não confirmado em ficha editorial. Não equiparado à2ªedição brasileira2015 citada no programa. Recortes de§3.15–3.18,pp130–135/PDF140–145,e§5.6(B/C)/5.7(A),pp248–250/253–254/PDF258–260/263–264. Textos selecionados,algumas extrações truncadas;sem alegar leitura integral dessas seções. p132/PDF142 e p253/PDF263 conferidas visualmente para pesos/J e limite de primeira ordem. Nenhuma figura,exercício,exemplo ou PDF da fonte distribuído. Arquivo inglês5ªedição foi apenas identificado por capa/ficha,sem corpo usado aqui.
- McMurry/OpenStax,OrganicChemistry,§13.6,trechos de desdobramento,n+1,pesos eJ. §13.7 aberta apenas para contexto de equivalência;sem desenvolver classificação estereoquímica. Uma URL tentativa de seção complexa falhou;fonte principal para múltiplosJ e limites éPavia. https://openstax.org/books/organic-chemistry/pages/13-6-spin-spin-splitting-in-1h-nmr-spectra
- JúpiterCCM0214 reaberto29/10/2026,itens4/5,ativação15/07/2024,compatível com aprovação2024/2,sem provar a versão ministrada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214

Aula,exemplos,código,figura e exercícios próprios preparados comIA;rascunho para revisão pessoal deJhuann. Sem operação de equipamento,identificação real ou certificação de competência.
