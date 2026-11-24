# Maturação de T — fontes e limites

22/10/2026. Rascunho didático original, assistido por IA e pendente de revisão pessoal. Aula `b4-maturacao-t`:14seções/12exercícios, primeiro recorte; não encerra o tema ou BiologiaIV.

## Fonte e páginas efetivamente consultadas

[USP CCM0221](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221), consulta direta hoje, ativação01/01/2025. Item1.3 prevê maturação de T no timo; item1.5 distingue ativação e mecanismos efetores. Seleção efetiva dos tópicos da turma não demonstrada pelo programa público.

Janeway, Imunobiologia, oitava edição/Artmed2014, exemplar privado já identificado no acervo. Leitura parcial do corpo: páginas impressas291,296–297,305–307 e311–313, correspondentes aPDF310,315–316,324–326 e330–332. A extração de duas colunas foi confrontada visualmente na p.312/PDF331. Metadados e sumário previamente inspecionados. Não houve leitura integral do capítulo8; os mecanismos e resultados não são atualizados para uma revisão de literatura contemporânea. A fonte pública complementar NCBI encontrada em https://www.ncbi.nlm.nih.gov/books/NBK27123/ apresentou verificação de acesso e não foi usada como texto lido. Nenhuma página ou figura privada distribuída.

O material original separa geração/montagem do receptor, seleção no timo e ativação periférica. Não atribui valores universais a afinidade, sobrevivência ou duração. Recorte da linhagem convencionalαβ; γδ, iNKT, Treg, vias detalhadas, ativação e tolerância periféricas ainda requerem desenvolvimento próprio. A relação CD4/classeII eCD8/classeI é contextualizada; marcador isolado não demonstra maturidade.

## Laboratório de leitura de dados

`experiment.py` apenas organiza observações de marcadores já classificadas como booleanos. Oito registros sintéticos:DN1,DP4,CD4único2,CD8único1. FraçãoDP1/2. Não recebe intensidades de citometria, não escolhe gates, não atribui idade/função ou destino, nem calcula taxa de seleção. Categorias vazias permanecem no resultado. Lista vazia produz zeros; uma fração nela precisaria de tratamento para denominador zero.

Comparar contagens em duas fotografias não identifica sozinho transição, morte, migração ou proliferação. A expressão de marcadores e a escolha de observáveis precisam de validação experimental; aqui não há dados de pesquisa ou recomendação clínica.

Quatro testes:combinações de marcadores;partição e invariância de ordem em341coortes de zero a quatro registros;limite estrutural de uma fotografia;contratos/entrada vazia. Esses testes validam o organizador de dados, não a imunologia.

Execute na raiz:

```sh
python3 labs/maturacao-t/experiment.py
python3 -m unittest discover -p 'test_*.py'
```

## Próxima ação

Revisar pessoalmente o percurso e distinguir os mecanismos que as contagens não identificam. Para distribuir o avanço entre os sistemas, próxima preparação em BiologiaIV: selecionar uma pergunta de células/comunicação neural a partir do Bear; não reutilizar o circuitoRC como se cobrisse fisiologia neural.


Verificação final — 22/10/2026:562testes Python aprovados, incluindo os quatro do novo laboratório, com descoberta confirmada após inclusão de __init__.py. SuíteJS e324MathML aprovadas; nenhuma demonstração nova, permanecem238/714cenários. Exercício1/2 e questão de interpretação por teclado conferidos no navegador; celular390px sem transbordamento horizontal, console sem erros observados. Roteiro da disciplina abriu passo3por teclado e seu link abriu a nova aula. Viewport restaurado. [Desktop](maturacao-t.jpg) e [móvel](maturacao-t-mobile.jpg). Aula permanece rascunho, revisão pessoal pendente. Saldo semanal final91%; parada65%. Próxima ação: conferir no Bear uma primeira sequência de células/comunicação neural, alternando os sistemas.
