# PCR: pergunta, sinal e controles

22/10/2026. Proposta didática original, pendente de revisão de Jhuann. Tema de técnicas/aplicações de CCM0215; a fonte atual não enumera protocolos e não comprova que PCR integrou a turma. Não é relato de bancada ou protocolo operacional.

## Quadro de estudo

| Elemento | Pergunta a registrar |
|---|---|
| Pergunta | O que se pretende investigar sobre o alvo de DNA? |
| Técnica | Como separação, associação de iniciadores e extensão se relacionam à amplificação? |
| Observável | O sinal distingue identidade, tamanho, quantidade, ou apenas detecção? |
| NTC | O que um sinal sem molde permite questionar sobre o fundo? |
| Positivo externo | O sistema funciona fora da matriz da amostra? |
| Controle na matriz | A resposta do canal de controle foi validada e é distinguível do alvo? |
| Limite | Quais explicações ainda produzem os mesmos sinais? |
| Evidência adicional | Como verificar identidade do produto, extração e contribuição pessoal? |

Preencher com uma interpretação própria é uma entrega de estudo. Uma experiência no portfólio requer fonte pessoal autorizada, autoria, condições e limites; material assistido por IA não substitui isso.

## Fontes consultadas parcialmente

- Alberts e colaboradores, *Biologia Molecular da Célula*, sexta edição, Artmed 2017, pp. 473–475 (PDF 509–511): extração local para mecanismo de amplificação e distinção DNA/cDNA. Figuras/capítulos não foram reproduzidos; a tabela lógica abaixo não vem do livro. Quinta edição citada no programa não confirmada. Parâmetros históricos não transportados para um roteiro de bancada.
- [QIAGEN, Importance of PCR controls](https://www.qiagen.com/us/knowledge-and-support/knowledge-hub/bench-guide/pcr/reference-genes-and-controls/pcr-controls), consulta direta parcial em 22/10/2026, blocos de controles sem molde, positivo e interno. Fundamenta os papéis gerais; o canal na matriz e sua equivalência de resposta ao bloqueio são hipóteses do painel, não validação de desenho real. Controle de extração, competição e distinção de canais exigem tratamento próprio.
- [NEB, PCR Troubleshooting Guide](https://www.neb.com/en/tools-and-resources/troubleshooting-guides/pcr-troubleshooting-guide), consulta direta parcial em 22/10/2026, categorias de ausência de produto e produtos inespecíficos. Usado para separar observação e possíveis explicações, sem incorporar ajustes de reação ou recomendações de compra.

Nenhum documento privado ou página de livro integra os arquivos públicos do site.

## Modelo lógico próprio

Indicadores T (alvo), I (bloqueio na matriz), C (contaminação compartilhada), W (sistema funcional), O (produto inespecífico só na amostra), todos 0/1. Canais, nesta ordem:

1. Amostra S=W∧¬I∧(T∨C∨O).
2. NTC=W∧C.
3. Positivo externo=W.
4. Controle na matriz=W∧¬I.

É um sistema determinístico de portas lógicas, sem simular PCR química, quantidade, tamanho/intensidade de banda, limiar, Cq, competição, ruído, amostragem ou extração. O canal na matriz é distinguível e responde ao bloqueio como a reação-alvo, por hipótese forte. Isso pode falhar em um desenho real. A contaminação afeta todos os canais compatíveis; a inespecificidade é restrita à amostra, por construção, sem afirmar que seja assim na prática.

Estado padrão (1,0,0,1,0) dá sinais (1,0,1,1). O estado (0,0,0,1,1), sem alvo e com inespecificidade, produz exatamente os mesmos sinais. Um terceiro estado tem alvo e inespecificidade juntos. São três estados compatíveis, sem pesos; não resulta probabilidade 1/3 para cada estado. Se W=0, todos os sinais são zero e 16 estados ficam indistinguíveis. Com I=1, W=1 e sem contaminação, alvo pode estar presente sem sinal na amostra.

A lista de hipóteses é finita e incompleta em relação à biologia. Resultados de modelo não validam um diagnóstico, ensaio real ou ausência absoluta de molécula. “Detectado” é somente o estado de um canal inventado.

## Verificação e apresentação

`experiment.py` enumera os 32 estados. Três testes Python: seis casos conceituais fixos; equivalência alvo/inespecífico e classes de observação, incluindo os 16 estados ocultados por W=0; independência funcional dos controles em relação a parâmetros que não os afetam, bloqueio e contratos de entrada. `reference.json` contém todos os 32 estados com classes de compatibilidade, comparados com JavaScript.

Tese visual: quatro linhas de observação, sem imitar gel ou equipamento. Conteúdo: mecanismo → controles → contraexemplos → sinais → enumeração/Python → exercícios. Controles atualizam o padrão e o número de hipóteses; detalhe por teclado revela os estados equivalentes. Cor acompanha texto e símbolos ●/○, sem ser o único sinal de estado. Sem animação que sugira reação ou dado adquirido.

Próximo passo pessoal: preencher o quadro e explicar o contraexemplo sem consultar a resposta. Pendências: demais técnicas, controles de extração, identidade do produto, ruído/limiar, quantificação, RT-PCR, evidências pessoais e revisão didática. O recorte não completa o grupo de técnicas ou a disciplina.
