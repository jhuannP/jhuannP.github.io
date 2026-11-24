# Microtúbulos: trajetória, eventos e exposição

Notas originais em rascunho,28/10/2026. Alberts et al.,Biologia Molecular da Célula,6ªed,Artmed2017,cap16 pp.927–928/PDF963–964: consulta textual parcial para GTP,polaridade,catástrofe e resgate. Legenda de p.929/PDF965 consultada como apoio textual;sem reprodução de figura. Seção farmacológica que apareceu na extração não usada. Sem nova inspeção visual/leitura integral ou distribuição do exemplar privado. ProgramaCCM0211 reaberto28/10/2026,ativação15/07/2025;versão ministrada não comprovada. https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211

Trajetória fornecida,com duas velocidades e uma ponta observada,outra tomada fixa. Não simula GTP,hidrólise,capas,nucleação,motores ou força. Comprimentos em μm,tempos em s. Trecho final acaba por observação,sem transição artificial. Retorna eventos/exposição,apenas estimativa sob hipótese adicional de hazard exponencial constante;nenhuma taxa foi medida em célula real. Exposição nula retornaNone;exposição positiva sem evento retornazero,sem afirmar taxa verdadeira nula.

Da raiz: `python3 -m unittest discover -s labs/microtubulo-trajeto -t .`; `python3 labs/microtubulo-trajeto/trace.py`.

Quatro testes:fixture/censura,54trajetórias com balanço e reexpressão da unidade de tempo,fronteira e contratos. Racionais exatos,até100trechos alternados. Rejeita cruzamento de comprimento zero;e zero só aceito no fim da observação,sem renucleação implícita. Não fornece modelo de sobrevivência do filamento.

Revisão20min:reconstrua(0,3),(10,5),(14,3),(19,4);conte eventos,tempos de exposição e explique por que o último trecho conta no denominador. Inferência com incerteza,experimento,motores,regulação e revisão pessoal pendentes.
