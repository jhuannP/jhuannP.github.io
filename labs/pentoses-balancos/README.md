# Via das pentoses: balanços reduzidos

27/10/2026. Notas originais com apoio de IA em rascunho, revisão pessoal pendente. Não constituem experiência laboratorial, resultado da IC ou aplicação clínica.

## Escopo e contas

Fase oxidativa: G6P → 6-fosfoglicono-δ-lactona (6PGL), formando um NADPH; hidrólise a 6PG; descarboxilação oxidativa a Ru5P+CO₂, formando outro NADPH. Saldo acompanhado por G6P: uma pentose, um CO₂, dois NADPH; dois NADP⁺ consumidos. Nenhum ATP direto. H⁺, água/formas de ionização são omitidos: não equação molecular completa.

Ru5P pode isomerizar a R5P e epimerizar a X5P. Para rearranjar três pentoses, escolha 2X5P+R5P. Transferências: X5P+R5P→GAP+S7P (5+5=3+7); S7P+GAP→F6P+E4P (7+3=6+4); X5P+E4P→F6P+GAP (5+4=6+3). Cancelar intermediários dá 2F6P+GAP, 15 carbonos e nenhum NADPH adicional. Somando fase oxidativa de três G6P: 18 carbonos=12 em F6P+3 em GAP+3 em CO₂, seis NADPH formados.

NADPH e NADH são pools distintos, com especificidades enzimáticas. O modelo verifica carbono do esqueleto derivado do substrato e separadamente NADP⁺+NADPH. Os cofatores têm carbono, mas sua estrutura permanece intacta e cancela; a função carbon_backbone não conta esses carbonos. Não é balanço de todos os átomos/cargas.

Exemplo de estoque: 6 mmol G6P,9 mmol NADP⁺, sem regeneração; extensão máxima contábil=min(6,9/2)=4,5 mmol. Sobram 1,5 mmol G6P e formam-se 4,5 mmol Ru5P/CO₂ e 9 mmol NADPH. Não é concentração nem garantia de fluxo/conversão: sem cinética, termodinâmica ou regulação. ATP em redes conectadas, reciclagem completa e demandas celulares não calculados.

## Fonte

Nelson/Cox, Princípios de Bioquímica de Lehninger, 6ª ed., Artmed 2014, §14.5 pp.575–579/PDF605–609, consulta parcial em 27/10/2026; p.577/PDF607 inspecionada visualmente para as duas fases/transferências. Sem incorporar boxes clínicos, ler integralmente o capítulo ou distribuir o PDF privado. Exemplos, números, desenho, redação e exercícios próprios. Fonte curricular não reaberta neste bloco.

## Código e verificação

`pentoses.py`: oito reações reduzidas com extensões int/Fraction; rejeita bool/float, espécies desconhecidas, estoques/extensões negativos e consumo além do disponível. Quantidades em mmol. Retorna novos inventários; original preservado mesmo quando a sequência falha. Não implementa reversibilidade automática, equilíbrio, direção espontânea ou dinâmica.

Da raiz: `python3 -m unittest discover -s labs/pentoses-balancos -t .`. Cinco testes: balanços por cada reação, sequência completa/cancelamento, estoque de cofator limitante/preservação de entrada, escala/escopo do carbono e contratos. Conservação de carbono do substrato e pool do cofator verifica apenas a contabilidade reduzida, não toda a bioquímica.

Respostas dos 12 exercícios:2 NADPH;1 CO₂;5 carbonos;6 NADPH;2 F6P;15 carbonos orgânicos;4,5 mmol;1,5 mmol; NADH/NADPH distintos; sem ATP direto; esquema reduzido; limite não determina fluxo. Resoluções completas na aula.

Revisão proposta em duas sessões: três etapas oxidativas/cofator; depois três transferências/cancelamento e limite de estoque. Pendentes: regulação, mecanismos, integração, reciclagem completa, revisão pessoal e observação experimental.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 763 fórmulas MathML conferidas. Em 390 px, limite de extensão rejeitou 6 e aceitou 4,5 pelo Enter; escopo de contabilidade reduzida aceito. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela, Windows real e experimento pendentes.
