# Replicação: orientação e cópia ideal

Rascunho original22/10/2026, revisão de Jhuann pendente. Nova aula `b2-replicacao-orientacao`:14seções/12exercícios, exemplo e código próprios. Primeiro recorte de II.2/CCM0121, não conclusão de replicação.

## Fonte

Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, tradução Artmed2017: capítulo5 pp.239–243 (PDF275–279) consultado parcialmente para pareamento, síntese, natureza semiconservativa, assimetria da forquilha e extremidade iniciadora. Páginas confirmadas no corpo; extração incluiu244, sem leitura integral ou atribuição de todo o capítulo como estudado. Não confundir paginação da tradução com original inglês2014. Nenhuma figura, exercício ou página do livro acompanha o site.

## Modelo

Moldes fixos no esquema: superior5′à esquerda/3′à direita, inferior3′à esquerda/5′à direita. Forquilha +1direita: filha contínua no molde inferior, fragmentos crescem à esquerda no superior. Forquilha−1esquerda: papéis trocados. Toda seta de síntese indica crescimento5′→3′. Contínua/descontínua são relativas à forquilha, não rótulos globais permanentes. O tracejado é uma frente esquemática; sem escala, geometria helicoidal, velocidade, proteínas ou cronologia.

Três fragmentos são ilustração, não previsão de contagem. Iniciadores, processamento, ligação, topologia, origens, terminação, correção e reparo não são simulados. Mudar controle compara duas orientações, não um filme de reversão de uma mesma forquilha física.

Python: alfabeto ACGT maiúsculo não vazio; complementar alinhada preserva a ordem, complementar reversa recebe/devolve convenção5′→3′. Exemplo inventado ACGTAACC: complementar alinhada TGCATTGG e reversa GGTTACGT. replicate produz dois duplexes antiparalelos, cada um com uma fita parental identificada e uma nova. A cópia é ideal, sem erros, enzimas ou experimento. Rótulos de origem não são dados de marcação experimental.

Tese visual: preto para moldes e azul para novas fitas, com rótulos5′/3′ redundantes à cor e direções explícitas. Conteúdo: um controle, esquema, tabela e limite. Interação: teclado inverte apenas a direção da forquilha; tabela e rótulos mudam mantendo o sentido químico de síntese.

## Verificação e continuação

Quatro testes Python:5460sequências de comprimentos1..6por pareamento e involução;340sequências de1..4para origem parental/antiparalelismo; duas direções por polaridade do molde; entradas inválidas. JavaScript confere as duas direções contra polaridades fixas e contratos.

Execute `python3 -m unittest discover -s labs/replicacao-orientacao -t .`, `node test_simulations.cjs` e `python3 labs/replicacao-orientacao/experiment.py` na raiz.

Próxima revisão pessoal: explicar o exemplo e os dois sentidos sem a tabela. Próximo desenvolvimento local requer leitura de iniciadores/processamento; nenhuma prática de bancada atribuída. Alternar área antes de expandir indefinidamente BiologiaII.

Verificação final:724testes Python, suíte JS270demos/810cenários básicos e comparações adicionais,12testes de catálogo aprovados. Duas direções, respostas2eGGTTACGT,390px sem overflow e console sem erros observados; prévia `replicacao-orientacao-mobile.jpg` na raiz. Viewport restaurado; revisão pessoal pendente. Saldo76%, parada65%.
