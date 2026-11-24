# E/Z: primeiro prioridade, depois lado

Rascunho original para revisão de Jhuann. Alceno simples com desenho plano das ligações aos substituintes. Cada carbono da dupla deve ter dois grupos distintos para que exista a configuração E/Z; essa distinção química exige a estrutura, não só as coordenadas.

## Fronteira do programa

O laboratório decide prioridade SOMENTE se os números atômicos diretamente ligados forem distintos. Igualdade gera erro de empate não resolvido. Não significa grupos idênticos nem ausência de E/Z: etila e metila começam pelo mesmo elemento e exigem comparação posterior. Isótopos, ligações múltiplas em substituintes, anéis e CIP recursivo não são implementados. Números atômicos não são rótulos de prioridade global: compara-se um par por carbono.

## Construção própria

A=(0,0), B=(2,0). Esquerda: Cl em(-1,1), F em(-1,-1); direita: Br em(3,1), I em(3,-1). Cl>F e I>Br por número atômico. Altas prioridades opostas → E. Trocar apenas Br/I dá Z. São diagramas sintéticos de conectividade, sem afirmar síntese, estabilidade, medidas de geometria ou isolamento dessas espécies.

Para v=B−A, use sL=cross(v,Lalto−A) e sR=cross(v,Ralto−B), sempre o mesmo sentido de eixo. Produto positivo significa mesmo lado (Z); negativo significa opostos (E). As duas ligações substituintes de cada carbono devem estar desenhadas em lados opostos do eixo; pontos colineares e eixo nulo são rejeitados. Os comprimentos de ligação não são inferidos das coordenadas.

Se o desenho sofre transformação linear invertível M e translação, cada área orientada ganha det(M), e seu produto ganha det(M)²>0. Portanto preserva o descritor. Isso inclui girar e espelhar o desenho; não calcula energia molecular nem descreve rotação física livre da dupla. Trocar o sentido A/B também preserva o produto após trocar os pares.

## Sem equivalências automáticas

E/Z não é o mesmo tipo de descritor que R/S de centro tetraédrico. Refletir esta representação de alceno não troca E por Z; trocar grupos em apenas um dos carbonos troca. Cis/trans exige referência apropriada a grupos comparáveis e não é um dicionário universal Z=cis/E=trans. E não quer dizer sempre mais estável: prioridade CIP não mede tamanho ou energia.

## Execução

`python3 labs/alceno-ez/ez.py`

`python3 -m unittest discover -s labs/alceno-ez -t .`

Quatro testes: exemplos E/Z e independência da ordem dos pares/eixo;36 desenhos transformados (6 matrizes×3 translações×2 configurações), incluindo rotação racional e reflexão;30 pares atômicos e60 comparações com oráculo horizontal; contratos e empates. Fraction evita arredondamento nos testes geométricos, sem resolver conformações reais ou imagens ruidosas.

## Fontes e revisão

Brown e Poon, Introduction to Organic Chemistry, 6ª edição, Wiley2016, §4.2C, trecho The E,Z System e Priority Rules, p.110/PDF130: consulta textual parcial em29/10/2026. A página111/PDF131 foi localizada, mas seus exemplos não foram usados. Sem nova inspeção visual ou leitura integral. McMurry/OpenStax §7.5 consultado parcialmente na mesma data para convenção e alcance das prioridades. Redação, diagramas com quatro halogênios, argumento geométrico, código e exercícios próprios, sem reprodução de figuras ou exercícios das fontes.

[OpenStax §7.5](https://openstax.org/books/organic-chemistry/pages/7-5-alkene-stereochemistry-and-the-e-z-designation)

Programa CCM0224 e histórico preservados com datas/limitações anteriores; sem nova consulta oficial neste bloco. PDFs privados não são distribuídos. Próxima revisão pessoal: atribuir prioridades por carbono, reconstruir o produto de sinais e explicar por que empate de primeiro átomo não comprova ausência de isomerismo.
