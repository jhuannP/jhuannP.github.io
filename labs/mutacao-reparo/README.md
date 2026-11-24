# Mutação e reparo — dano, sequência e consequência

27/10/2026. Notas de aula originais com apoio de IA, em rascunho. Revisão pessoal de Jhuann pendente. Não demonstram experiência de bancada nem domínio atual.

## Lugar na formação e fontes

CCM0121, Biologia II, itemII.3: mutação e reparo. Programa oficial reaberto em 27/10/2026, ativação exibida 01/01/2025. Aprovação 2025/1 vem do panorama baseado no histórico, sem nova conferência do histórico neste bloco; compatibilidade temporal não prova a versão ministrada.

- [Programa oficial](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121).
- Alberts e colaboradores, *Biologia Molecular da Célula*, 6ª edição em português, Artmed 2017, versão traduzida do original inglês 2014 indicado no programa. Exemplar privado autorizado já localizado em Bio 2/Livros; não distribuído. Consulta textual parcial ao capítulo 5: pp.250–251 (PDF286–287), para reparo de pareamento; pp.266–271 (PDF302–307), para lesões e vias de excisão. Página 268/PDF304 renderizada e conferida visualmente. Sem leitura integral do capítulo; detalhes e avaliações clínicas não são objeto destas notas.
- [NCBI, código padrão, tabela 1](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG1), reconferida em 27/10/2026, página informa atualização 23/09/2024. Fonte factual das atribuições dos códons; não usada para inferir início real da tradução. Apoio de tradução em Alberts capítulo 6 reutiliza referência parcial anterior, sem nova leitura deste capítulo.

Pré-requisitos: orientação e complementaridade, cópia semiconservativa, DNA codificante versus molde, RNA e quadro de leitura. A aula se liga a `b 2-replicacao-orientacao` e `b 2-traducao-quadro`. Capacidades pretendidas: comparar representações, explicar a preservação da informação, interpretar limites de um modelo e planejar evidências. Não certificadas pessoalmente.

## Três níveis que não devem ser confundidos

Lesão é uma alteração química/estrutural do DNA; malpareamento é uma combinação incorreta entre bases das fitas; mutação é alteração da sequência que pode ser mantida nas cópias. Uma lesão pode ser corrigida, bloquear a cópia ou ter outros destinos. O código desta aula não produz nem simula lesão química.

O exemplo local G antigo:T novo contém informação sobre qual fita foi copiada. Corrigir a nova paraC restauraG:C; alterar oG antigo paraA leva aA:T. O par isolado não identifica qual lado deve ser corrigido. Sinais de fita nova e mecanismos variam entre organismos; não generalizar a estratégia de uma bactéria.

Se o malpareamentoG:T for copiado uma vez sem reparo e cada fita orientar sua complementar, os dois descendentes ideais sãoG:C eA:T. A alteração já pode propagar-se como par complementar canônico. “Estável nas cópias” não significa fixação de um alelo na população. O esquema não fornece frequência de mutação ou viabilidade de clones.

A fita complementar intacta pode fornecer informação para recompor uma região danificada. Excisão de bases começa, em casos apropriados, com uma glicosilase que remove a base reconhecida, seguida por processamento do sítio e preenchimento/ligação. Excisão de nucleotídeos remove um segmento contendo determinada lesão e recompõe a fita. Não são a mesma via repetida, nem cobrem todas as lesões. Quebras duplas, recombinação, taxas e mecanismos detalhados permanecem pendentes.

## Exemplo original: comparar a mesma região codificante

DNA codificante 5′-ATGGAATTTTAA-3′, posições 1–12. Quadro inicial 0, código padrão, sem íntrons no trecho. Conversão para representação de RNA éT→U, não complementar novamente. Os resíduos são escritosN→C. Parada não é aminoácido.

| Operação na referência | DNA agrupado | Leitura representada |
|---|---|---|
| Nenhuma | ATG GAA TTT TAA | MEF; parada |
| Posição 6 A→G | ATG GAG TTT TAA | MEF; substituição sinônima |
| Posição 5 A→T | ATG GTA TTT TAA | MVF; trocaE→V |
| Posição 4 G→T | ATG TAA TTT TAA | M; parada antecipada |
| Deleção da posição 4 | ATG AAT TTT AA | MNF; duas bases incompletas, sem parada completa na janela |
| Deleção das posições 4–6 | ATG TTT TAA | MF; fase a jusante preservada |

A primeira substituição mudaDNA, mas não a sequência de resíduos representada. Isso não prova neutralidade celular. A troca de resíduo ou a parada antecipada não provam patogenicidade. Uma deleção isolada de tamanho não múltiplo de 3 desloca a fase a jusante na região considerada; uma deleção de 3 pode manter a fase e ainda remover um resíduo importante. A ausência de parada na janela de 11 bases não fixa o tamanho da cadeia biológica: falta a continuação da sequência.

Sequência, expressão de RNA, quantidade/estado de proteína e função são perguntas diferentes. Uma medição de uma delas não substitui automaticamente as outras. Qualidade das leituras, orientação e referência importam; uma função requer ensaio adequado e controles. Nenhum experimento biológico foi executado neste bloco.

## Resoluções dos 12 exercícios

1. Lesão não torna mutação obrigatória; há reparo e outros destinos.
2. O par G:T sozinho não revela qual fita foi copiada incorretamente.
3. Um dos dois descendentes ideais apresentaA:T; o outroG:C.
4. A glicosilase pode iniciar a excisão de bases ao remover uma base inadequada.
5. Quatro trincas,12 bases.
6. GAA e GAG correspondem aE no código padrão; sinônima na representação.
7. A posição 5 A→T produz GTA/GUA e a cadeiaMVF.
8. A posição 4 G→T produz TAA/UAA; apenas M vem antes da parada.
9. A deleção deixa 11 bases=3×3+2; sobram 2.
10. RemoverGAA preserva a fase a jusante, mas não demonstra função preservada.
11. Sem continuação, não se pode localizar uma parada posterior.
12. O laboratório demonstra apenas edição e leitura de representações sintéticas.

## Python opcional: escopo e execução

`variants.py` usa apenas Python padrão. Reutiliza `labs/traducao-quadro/experiment.py`, que contém a tabela factual e o decodificador já existentes, sem alterar esse apoio. Execute da raiz do protótipo; um download isolado de `variants.py` precisa também do apoio e da mesma estrutura de pastas.

```sh
python 3 -m labs.mutacao-reparo.variants
python 3 -m unittest discover -s labs/mutacao-reparo -t .
```

Entradas: strings de DNA maiúsculoACGT. Não aceitaU, caracteres ambíguos ou espaços; não faz normalização silenciosa. Trecho vazio é uma representação válida sem informação. Posições de edição são inteiras iniciadas em 1, sembool oufloat; substituição precisa mudar uma base. Deleção deve estar inteiramente dentro do trecho e ter tamanho positivo. Apagar tudo produz trecho vazio, não evidência de viabilidade de organismo.

`read_coding_dna` recebe a fita codificante 5′→3′ e um quadro inicial 0 já fornecido. Não buscaAUG, genes, promotores ou sítios de processamento. Retorna resíduos, trincas lidas, `stop_offset` e `suffix`. Os campos de trincas e sufixo usam o alfabeto de RNA (U), pois vêm do decodificador reutilizado; a entrada continua sendoDNA (T). Ooffset da parada é iniciado em 0:3 corresponde à posição 4. Na substituição da posição 4, o sufixo de DNA TTTTAA aparece comoRNA UUUUAA na saída. Havendo parada, o sufixo é todo o restante após ela; sem parada, é só o restante incompleto de 0–2 bases. Não interpretar os dois casos da mesma forma.

Quatro testes selecionados verificam seis leituras exemplares,36 substituições possíveis no trecho e 78 deleções por posições identificadas, preservação de partes não alteradas, agrupamento/offsets, códons factuais e contratos. São verificações das representações e do software, não de modelos biológicos de reparo ou efeitos funcionais. Conferência da tabela factual não foi tratada como prova de expressão. Não se executaram todos os laboratórios da biblioteca.

## Revisão pessoal e lacunas

Duas sessões propostas de 20 min: desenhar informação antiga/nova e destinos do malpareamento; depois reconstruir a tabela com posições antes de executarPython. Dúvidas, avaliação e evidências pessoais permanecem em branco.

Continuam pendentes: mecanismos e especificidades das vias, reparo de quebras duplas, taxas e cinética, experimentos e controles reais, análise de dados com qualidade documentada e consequências fora da região codificante. O itemII.3 passa de lacuna para cobertura parcial; nenhum grupo do programa é declarado completo.
