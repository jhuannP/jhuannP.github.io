# Diversidade: coleção, amostra e esperança

22/10/2026. Proposta didática original, pendente de revisão pessoal. Recorte de amostragem no tema amplo Diversidade de CCM0215; não identifica o protocolo da turma nem experiência de coleta ou bancada.

## Pergunta e fontes

Pergunta: o que a ausência de uma categoria numa amostra permite concluir? Observável: indivíduos classificados em categorias, com contagem e unidade definidas. O gerador conhece a composição completa; uma pesquisa real pode não conhecê-la.

- [Hurlbert (1971), The Nonconcept of Species Diversity: A Critique and Alternative Parameters](https://esajournals.onlinelibrary.wiley.com/doi/10.2307/1934145). Consulta direta parcial em 22/10/2026: resumo da página editorial e texto de *Species Richness*, p.581, na [cópia pública do artigo](https://ricottalab.com/wp-content/uploads/2015/10/hurlbert-1971.pdf). Referência para a esperança em subamostras sem reposição e o alcance da comparação. Equação também disponível no resumo editorial; não se dependeu de interpretar a imagem de fórmula do PDF. Não houve leitura integral, reprodução de tabelas ou adoção de todos os argumentos históricos do artigo.
- Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §3.3, p.94/PDF109: modelo hipergeométrico consultado parcialmente por extração local; p.95 foi extraída junto, mas seus exercícios não fundamentam a aula. Apoio matemático complementar, sem afirmar que o livro foi usado na turma de Laboratório I.
- Alberts permanece a referência bibliográfica do programa; não se atribui a ele a fórmula de riqueza esperada deste recorte. Exemplar de quinta edição continua não confirmado. Nenhum PDF ou página privada foi incluído no site.

## Coleções e desenho

Três coleções conhecidas de N=12 indivíduos e quatro categorias A–D: (6,3,2,1), (3,3,3,3), (9,1,1,1). Cada indivíduo tem uma identidade distinta; a categoria é reconhecida sem erro. A–D não são espécies reais, sequências, leituras ou amostras pessoais. A categoria D é menos abundante nas coleções 0/2, mas não na coleção equilibrada.

Desenho de referência: cada subconjunto de n identidades tem a mesma probabilidade, sem reposição; n=0..12. As ordens mostradas são prefixos deliberados: agrupamento por categoria, alternância por categoria e uma permutação fixa de identidades. Não se amostra aleatoriamente por esse seletor; a curva do exemplo não é uma réplica sorteada, e seus prefixos não são réplicas independentes.

Para Nᵢ indivíduos da categoria i, a chance de não ver i é C(N−Nᵢ,n)/C(N,n), com numerador zero quando n>N−Nᵢ. A chance de ver ao menos um é o complemento. Riqueza é soma de indicadores de presença; a esperança é soma das probabilidades de detecção, sem hipótese de independência entre categorias. O caso de n=0 tem esperança zero; examinar a coleção inteira recupera suas categorias positivas.

Na coleção padrão e n=4, existem 495 subconjuntos; 330 deixam D de fora. P(D aparecer)=1/3 e P(D ausente)=2/3. As quatro chances de aparecer são 32/33, 41/55, 19/33 e 1/3; riqueza esperada 433/165≈2,62424. A ordem agrupada ilustra riqueza um; a alternada, quatro. Esperança fracionária é média de inteiros, não uma fração de categoria em uma amostra.

## Limites

Calculamos a riqueza esperada ao subamostrar uma coleção conhecida, sem extrapolar categorias desconhecidas ou estimar riqueza de uma região. Mesmo N e mesma riqueza não implicam curvas idênticas: abundâncias diferentes mudam a inclusão. Essa expectativa não é diversidade funcional/filogenética, intervalo de confiança ou posterior de existência. Não há classificação imperfeita, inclusão desigual, espaço, extração, PCR ou detecção molecular modelados. Leituras de sequenciamento não são contagens de indivíduos por definição. Ausência na amostra não prova ausência na coleção.

## Verificação e composição

Quatro testes Python: 255 coleções pequenas comparadas por enumeração de 50624 subconjuntos de identidades (incluindo os vazios) e estratificação por n; ordens com identidades únicas, prefixos aninhados e conservação de contagens; exemplos/fronteiras/categorias vazias; contratos. `reference.json`: 117 estados, três coleções × 13 tamanhos × três ordens. JavaScript confere contagens, índices, riqueza, esperança e chance de D, além de saída visual finita. Python usa Fraction e combinações inteiras; JS limita-se a N=12 e usa combinações pequenas, sem pretensão de biblioteca combinatória geral.

Tese visual: duas curvas em eixos comuns e tabela de contagens. Azul é a esperança uniforme; preto tracejado é a ordem ilustrativa. Controle n muda o destaque/amostra; ordem muda só a amostra e a curva preta; coleção muda composição e referência. Segmentos entre pontos inteiros são guias, não extensão para n fracionário. Sem animação que sugira coleta ou experimento real.

Próxima entrega pessoal: explicar o denominador, a riqueza esperada fracionária e um desenho de coleta que possa violar a uniformidade. Faltam identificação, dados e evidências pessoais; diversidade segue parcial. Descobertas e seminários continuam lacunas.
