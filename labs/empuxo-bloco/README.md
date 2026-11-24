# Pressão e empuxo: posição e equilíbrio

Rascunho original22/10/2026, revisão de Jhuann pendente. Aprofunda `ef-pressao` de3/2para14seções/12exercícios, quatro MathML, preservando IDs, exemplo200Pa e desafio de área. Reforço escolar, Python opcional; não é prática experimental.

## Fontes consultadas parcialmente

- [OpenStax College Physics2e §11.4](https://openstax.org/books/college-physics-2e/pages/11-4-variation-of-pressure-with-depth-in-a-fluid): derivação de pressão por profundidade e referência da superfície.
- [OpenStax College Physics2e §11.7](https://openstax.org/books/college-physics-2e/pages/11-7-archimedes-principle): empuxo, comparação com peso e fração submersa.

Consulta22/10/2026. Texto, valores, esquema, exercícios e código próprios; nenhuma figura, questão ou solução da fonte reproduzida.

## Modelo

Fluido parado de1000kg/m³; bloco rígido/impermeável com volume total1L=0,001m³, g=10m/s². Densidade médiaρde200a1400kg/m³ e imersão de0a100%. m=ρ/1000kg; P=ρ/100N; E=percent/10N; E−P=(10percent−ρ)/100N. Comparação exata de sinais por numerador inteiro.

Imersão é posição escolhida, não equilíbrio automático. Eventual suporte para manter uma posição desbalanceada não é incluído nas duas forças comparadas. f_eq=ρ/1000seρ≤1000; paraρ<1000é flutuação parcial, igualdade é equilíbrio neutro com imersão total, eρ>1000não permite equilíbrio só por empuxo/peso. Não calcula aceleração, trajetória, arrasto ou profundidade estável.

Sem empuxo do ar, capilaridade, contato com fundo ou deformação; sem torques. Setas laterais comparam módulos em escala comum, não pontos de aplicação. Esquema sem escala espacial. Maior profundidade com imersão total não altera E para fluido uniforme e volume fixo.

Tese visual: separar parte submersa do volume total e peso do empuxo, com rótulos e tabela de unidades. Conteúdo: densidade/imersão, esquema, forças e equilíbrio-alvo. Interação: teclado altera uma hipótese sem recolocar automaticamente o bloco; relatório distingue balanço atual e possibilidade de equilíbrio.

## Verificação e lacunas

Quatro testes:273estados por pressões nas faces de prisma com área0,01m²/altura0,1m, incluindo mudança da referência de profundidade; posição versus equilíbrio;400densidades maiores que a do líquido; contratos.77referências racionais por pressão nas faces cruzadas com JS. Só biblioteca padrão.

Execute `python3 -m unittest discover -s labs/empuxo-bloco -t .`, `node test_simulations.cjs`, `node test_math.cjs` na raiz.

Próxima revisão pessoal: explicar E=P em40%paraρ400e por queρ1200não flutua só por empuxo. Pressão variável em superfícies gerais, gases compressíveis, torques e observação experimental ficam pendentes.

Verificação final:736testes Python,273demos/819cenários básicos e comparações adicionais,428MathML e12testes de catálogo aprovados. Browser conferiu equilíbrio parcial, neutralidade, corpo mais denso, imersão zero, respostas1/2500e−2;390px sem overflow horizontal e console sem erros observados. Prévia `empuxo-bloco-mobile.jpg` na raiz; viewport restaurado. Rascunho pendente de revisão pessoal; saldo75%, parada65%.
