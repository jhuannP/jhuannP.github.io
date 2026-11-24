# Glicina livre: três macrostados e carga média

Rascunho didático original, pendente da revisão de Jhuann. Sem titulação executada, dados experimentais ou resultado pessoal presumido.

## Fontes e parâmetros consultados em 16/10/2026

- Nelson/Cox, Princípios de Bioquímica de Lehninger, tradução da sexta edição, Artmed 2014: sumário e trechos das páginas impressas 81–83 (PDF 111–113), no acervo privado. Anfólitos, zwitteríon, dois estágios e valores de referência da glicina. Não houve leitura integral do capítulo ou cópia de figura/exercício.
- [OpenStax Organic Chemistry 26.1](https://openstax.org/books/organic-chemistry/pages/26-1-structures-of-amino-acids), tabela 26.1: glicina, pKa1=2,34, pKa2=9,60, pI=5,97.
- [OpenStax Organic Chemistry 26.2](https://openstax.org/books/organic-chemistry/pages/26-2-amino-acids-and-the-henderson-hasselbalch-equation-isoelectric-points): relação de equilíbrio e pI. O modelo conserva formas minoritárias, sem transformar predominância em fração exatamente 1.

Texto, derivação, exemplos, exercícios, gráficos e código próprios. Os pKas são valores adotados da referência, não universais; não se reconstruíram condições experimentais de temperatura/força iônica. O livro privado não é servido pelo protótipo.

## Sistema e limites

H2G+ -> HG0 -> G- são os macrostados com cargas +1,0,-1. HG0 é representado pelo zwitteríon predominante H3N+-CH2-COO-; não se resolve a distribuição de todos os microestados internos. Glicina livre não tem cadeia lateral ionizável no modelo.

O pH é imposto externamente. Aproximam-se atividades idealmente; h=10^-pH e as concentrações podem ser normalizadas por c°=1 mol/L. Não se calcula o pH de uma solução isolada nem a carga de todos os íons do reservatório. Alterar C com pH fixo apenas escala C*alpha; não simula diluição sem reservatório.

## Distribuição e checagens

Pesos h², K1*h, K1*K2; denominador é a soma. O código usa logaritmos com deslocamento comum para preservar a normalização. Carga média z=alphaPlus-alphaMinus, prótons médios ligados n=2alphaPlus+alphaZero=1+z. Cada espécie tem sua carga inteira; uma média não inteira não representa próton fracionário por molécula.

No pI, h²=K1*K2 e pI=(pK1+pK2)/2 para este modelo de duas etapas. As formas carregadas têm frações iguais, não nulas. Para glicina no pI: cada forma carregada aproximadamente 0,0234313%; forma zero aproximadamente 99,9531374%.

A derivada dz/dpH=-ln(10)*Var(n) vem da derivação dos pesos normalizados e é não positiva. Como z=n-1, Var(n)=Var(z). Pequenos valores negativos de variância por arredondamento são truncados para zero no cálculo numérico. Não é uma medida de proteína.

Na raiz: `python3 -m unittest discover -s labs/aminoacidos -t .`. Quatro testes conferem normalização/ação das massas, referência Decimal de 80 dígitos usando pesos diretos, simetria/pI e derivada por diferenças finitas. `reference.json` contém 27 configurações JS/Python: glicina e dois pares hipotéticos de pKas para testar a generalidade algébrica. O núcleo limita valores absolutos dos parâmetros a 100 por motivo numérico; a UI mostra pH 0–14 e somente os pKas da glicina. A faixa exibida não é um limite universal de pH.

## Exploração proposta

1. No pI=5,97, encontre as duas pequenas frações carregadas e explique a média zero.
2. Compare pH 0 e 14; depois alterne frações e carga média.
3. Perto dos pKas, confira igualdade de duas formas, lembrando que a terceira não foi removida do cálculo.
4. Mude C mantendo pH imposto: frações fixas, concentrações escaladas.

Cadeias laterais ionizáveis, pKas microscópicos, efeitos de ambiente, atividade não ideal, carga de peptídeos/proteínas, titulação com volume e solução isolada continuam pendentes. A média de todos os pKas não é uma fórmula geral de pI. Não se contou este primeiro caso como cobertura completa de aminoácidos ou proteínas.
