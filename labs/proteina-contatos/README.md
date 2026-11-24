# Proteínas: sequência, distâncias e contatos Cα

22/10/2026. Rascunho para revisão pessoal. Análise geométrica original de dados públicos de terceiros; não é determinação estrutural ou experiência de bancada de Jhuann.

## Fontes consultadas e procedência

- Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, tradução Artmed2017: p.112/PDF148, ligação peptídica, cadeia principal e Cα, inspecionada em texto e imagem; pp.115–116/PDF151–152, representações e motivos α/β, consulta parcial por texto. A extração incluiu113–114/117, sem usar essas páginas como base de classificação de domínios ou energia. Não houve leitura integral do capítulo nem cópia de figura, exercício ou página privada. A edição é tradução da sexta confirmada no acervo; não transferir paginação ao inglês.
- [RCSB PDB1CRN](https://www.rcsb.org/structure/1CRN), consulta direta em22/10/2026. Crambina, cadeia A,46 resíduos modelados; difração de raiosX, resolução da entrada1,50Å. Depositores W.A.Hendrickson/M.M.Teeter. [DOI da entrada](https://doi.org/10.2210/pdb1CRN/pdb). A página vincula artigo de M.M.Teeter, PNAS1984, DOI10.1073/pnas.81.19.6014, mas o artigo não foi lido integralmente. Seu resumo menciona dados de outra resolução; o metadado usado neste recorte é o da entrada baixada, sem fundir as duas afirmações.
- [Coordenadas públicas originais](https://files.rcsb.org/download/1CRN.pdb), baixadas em22/10/2026,49491bytes. SHA-256: `42199a30a0701864a2a5cc76cd7f35cc544cd0e65fbcf63e03c166543249b811`. Cópia offline `1CRN.pdb`; não é documento pessoal. Acesso de rede foi necessário somente para a fonte pública, não há requisições externas no painel.
- [RCSB Usage Policies](https://www.rcsb.org/pages/usage-policy), consulta direta: arquivos de dados PDB sob CC0 1.0. Isso não foi tratado como autorização geral para reproduzir artigos/textos/figuras do site. Mapa e material didático são próprios.
- Vínculo curricular já mapeado: BiologiaII/CCM0121, itemI.2, estrutura de proteínas. O recorte abre parcialmente o tópico; não substitui a sequência completa de estrutura/função, conformações e técnicas.

## Seleção e representação

Selecionados registros `ATOM`, nome de átomo `CA`, cadeiaA, resíduos1..46, sem altloc ou código de inserção nesta cópia. Foram conferidos46registros, um por resíduo. Nomes e coordenadas de três casas decimais geram `ca.json`; coordenadas são inteiros em0,001Å, preservando exatamente os decimais publicados. É recorte específico, não parser universal; arquivos com lacunas, múltiplas cadeias, modelos ou posições alternativas precisam de outra seleção.

Somente Cα. Não se representam cadeias laterais, solvente, outras cópias cristalinas ou parceiros. Distâncias Cα consecutivos não são comprimentos de uma ligação covalente direta. O arquivo original continua disponível para conferir a seleção; o código e o JavaScript incorporam o recorte, permitindo uso offline.

## Critério e contas

Para i<j, inclua se |i−j|≥s e dᵢⱼ≤r. A comparação usa distâncias ao quadrado dos inteiros, com limite `(1000*r)²`, evitando arredondar a raiz antes do filtro. No Python, `cutoff` é inteiro em meiosÅ (16significa8Å); no controle do navegador ele é exibido diretamente emÅ. Somente a tabela arredonda a distância para leitura.

N=46. Há1035pares distintos antes do filtro. Para separação s, candidatos=(46−s)(47−s)/2; s=3 dá946, s=10 dá666. Não inclui diagonal. Graus satisfazem Σk=2E. O mapa mostra cada par em duas células, mas o contador usa somentei<j.

Par4–32: separação28; diferença de coordenadas(−2,506;2,703;−1,773)Å; d²=16,729774Å²; d≈4,090204640Å. Em r=5Å/s=10, resíduo4 tem vizinhos32/44/46 e há5pares únicos na cadeia. Em r=8Å/s=3, há114pares únicos e nove vizinhos para4. Essas quantidades são resultados do critério sobre esta cópia estrutural, não energias, abundâncias ou probabilidades medidas.

Contato Cα não determina ponte de hidrogênio, ligação dissulfeto, função ou causalidade. Resolução do experimento não é erro individual±resolução; decimais do arquivo não quantificam precisão física. Não foram analisados densidade eletrônica, fatoresB, estrutura secundária automática, dinâmica ou mudanças de coordenadas. Um mapa estático não fornece populações F/U ou caminho de enovelamento.

## Executar e verificar

```sh
python3 labs/proteina-contatos/experiment.py
python3 -m unittest discover -s labs/proteina-contatos -t .
```

Quatro testes novos: hash/seleção dos46Cα contra arquivo original; todos os17limites e10separações contra contas independentes emÅ com Decimal; invariância por rotação/translação, monotonicidade e pares explícitos; candidatos, diagonal e contratos. Não há simulação aleatória como prova nem validação experimental do critério.36estados em `reference.json` cruzam Python/JavaScript em pares, distâncias quadradas, graus e vizinhos.

Próximo estudo local: ler sobre torções da cadeia principal e métodos de estrutura antes de desenvolver φ/ψ ou atribuição de estrutura secundária; mapa de proximidade não cobre esses assuntos. Revisão pessoal permanece pendente.
