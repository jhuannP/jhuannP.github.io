# Reflexo de estiramento — roteiro original

29/10/2026. Elaboração assistida por IA; revisão pessoal pendente. Público: estudante de graduação com organização nervosa e sinapses como pré-requisitos.

## Atividade em papel

1. Desenhe o fuso, aferência Ia, gânglio/raiz dorsal, alfa no corno ventral e saída pela raiz ventral. Separe posição anatômica de conexão funcional.
2. No esquema central, siga Ia→alfa homônimo (+): uma sinapse. Siga Ia→inter (+)→alfa antagonista (−): duas sinapses. A junção neuromuscular fica fora da contagem central.
3. Explique por que Ia continua excitatória no segundo ramo. Um interneurônio inibitório realiza a etapa final. Nem todo interneurônio é inibitório.
4. Discuta a alça mecânica: aumento de carga pode alongar músculo, aumentar sinal aferente e recrutar contração que se opõe ao alongamento. Feedback negativo não exige que o ramo neural seja inibitório. O grafo aberto não calcula estabilidade.
5. Contraste de papel: apague só inter→alfa antagonista. O caminho homônimo continua no desenho. Outras vias biológicas não foram excluídas: não inferir movimento real ou localizar um defeito a partir disso.
6. Produza uma explicação própria separando unidade motora, conjunto motor, fuso/Ia, Golgi/Ib, alfa e gama. Recrutamento e frequência não dão força sem propriedades musculares e mecânicas.

## Código opcional

Na raiz do protótipo:

```sh
python3 labs/reflexo-estiramento/routes.py
python3 -B -m unittest discover -s labs/reflexo-estiramento -t .
```

O programa enumera caminhos simples (sem repetição de nó), conta conexões centrais declaradas e retorna sinal de cada cadeia. Até oito nós/16 conexões, sinais inteiros +1/−1 e conexões únicas. Não modela alças recorrentes; não combina sinais para estimar resposta líquida. Ausência de caminho vale somente para as conexões fornecidas. Nenhum tempo, tensão, frequência ou força é calculado. Não é simulação fisiológica, dado de organismo ou registro de experiência pessoal.

Quatro métodos de teste: dois caminhos definidos/contraste, oráculo independente por permutações em 32 atribuições de sinais, caminhos opostos mantidos separados e contratos. Não é teste do mecanismo biológico.

## Fontes e alcance efetivo

Bear, Connors e Paradiso, *Neurociências: desvendando o sistema nervoso*, 4ª edição brasileira, Artmed2017, original2015. Exemplar já identificado no acervo autorizado; consulta textual parcial em 29/10/2026 ao capítulo13:

- pp.458–459/PDF500–501: unidade/conjunto motor e início do controle graduado;
- p.469/PDF511: fusos e aferência Ia;
- pp.470–471/PDF512–513: arco monossináptico e feedback;
- recortes de pp.473–474/PDF515–516: gama e fibras intrafusais;
- p.477/PDF519: interneurônios/inibição recíproca, página também inspecionada visualmente. Página/figura privada não publicada.

Leitura parcial, sem capítulo inteiro ou reprodução de figura/exercício do livro. Alfa/gama: distinção geral introdutória, detalhes e coativação ainda pendentes. Organização de raízes retomada da aula já existente, sem nova auditoria integral de neuroanatomia.

[OpenStax A&P2e §14.3 Motor Responses](https://openstax.org/books/anatomy-and-physiology-2e/pages/14-3-motor-responses), corpo parcial consultado em 29/10 para contexto da participação de circuitos locais, comandos e informação sensorial; não incorporadas afirmações amplas da página sobre todas as conexões corticoespinhais/corticobulbares ou seus exemplos clínicos.

[Programa CCM0221](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221), consulta anterior de 28/10 mantida: item2.6 é sistema possível, não confirmação do que foi ministrado na turma. Não reaberto neste bloco. Unidade em preparação; outros circuitos e revisão pessoal permanecem pendentes.
