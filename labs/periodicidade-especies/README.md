# Periodicidade: espécies, definições e escalas

Material original de 27/10/2026, em rascunho para revisão de Jhuann. Pré-requisitos: configurações eletrônicas, carga e orbitais. É o primeiro recorte do grupo de periodicidade, que continua parcial.

## Estudo em dois blocos de vinte minutos

1. Reconstrua a contagem de dez elétrons e explique por que isoeletronicidade não iguala raio ou energia. Defina qual raio seria comparado.
2. Use os conjuntos fictícios I/II: n=2 e S=5, com Z=8 e Z=10. Derive r*=n²/(Z−S), B*=(Z−S)²/n² e as razões 3/5 e 25/9. Explique por que isso não fornece os valores experimentais de O ou Ne. Depois reveja o sinal da afinidade e os estados iniciais das ionizações sucessivas.

## Código e figura

Execute `python3 labs/periodicidade-especies/scales.py` na pasta do protótipo. Frações exatas, sem dependências externas. O programa confere conservação de carga, razões e dependências de um modelo simplificado. Não calcula estrutura eletrônica, raios reais, orbitais ou energias de ionização. A figura é uma tabela original de contagem; nenhuma dimensão representa tamanho físico.

O modelo mantém S por hipótese: S não é automaticamente o número dos outros elétrons, nem valor empírico atribuído aos elementos escolhidos. n e Z_eff podem mudar simultaneamente numa comparação real. O script não é um preditor de tendências com exceções.

## Fontes e alcance

- [USP — CCM0114](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114), reaberto em27/10/2026. O programa inclui propriedades periódicas; ativação15/07/2024, posterior à turma2023. Versão da turma não recuperada. A aprovação é mantida como registro histórico, sem pressupor domínio atual.
- Atkins, Jones e Laverman, *Princípios de Química*, 7ª ed., Bookman2018: Tópico1F §§1F.2–1F.5, pp.53–59/PDF185–191, extração textual parcial em27/10/2026 no acervo autorizado. Confere definições operacionais, raios, ionização e convenção de afinidade positiva para energia liberada. Edição diferente da terceira citada no programa; sem leitura integral, nova inspeção visual ou distribuição do PDF.
- [OpenStax Chemistry2e §6.5](https://openstax.org/books/chemistry-2e/pages/6-5-periodic-variations-in-element-properties), consulta textual parcial em27/10/2026: definições de raios, blindagem e carga efetiva. Sem transcrição de exemplos, tabelas ou figuras.

Figura, organização das notas, modelo de sensibilidade, código e exercícios próprios. A representação de escalas hidrogenoides é limitada: r* não é raio covalente, e B* não é ionização multieletrônica. Sem comparação quantitativa com dados reais. Efeitos relativísticos, par inerte, relações diagonais, detalhes de metais de transição e revisão pessoal permanecem pendentes.
