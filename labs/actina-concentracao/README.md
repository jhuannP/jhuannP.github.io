# Actina: concentração crítica e renovação das pontas

22/10/2026. Notas de aula, coeficientes e diagrama originais com apoio de IA; rascunho para revisão de Jhuann. A aula b3-actina-concentracao-critica abre o item 4 do programa de Biologia III CCM0211, aprovado em2025/2 conforme o panorama já registrado. Isso não é evidência de domínio atual ou de experimento pessoal.

## Roteiro de leitura

Compartimentos e organização celular → polaridade de actina → concentração livre → taxas de associação/dissociação → limiares de cada ponta → saldo total → diferença entre renovação estacionária e equilíbrio. A aula tem14 seções/12 exercícios; não fecha citoesqueleto, motores ou movimento celular.

## Modelo e unidades

O filamento já existe. A concentração livre c, em μM, é mantida por um reservatório; duas pontas acessíveis. k_on tem unidade μM⁻¹ s⁻¹ e k_off, s⁻¹; cada evento altera uma subunidade. v=k_on c−k_off é um saldo médio em subunidades/s, não uma velocidade espacial. Os sinais +/− identificam polaridade estrutural.

Coeficientes sintéticos:
- ponta mais: k_on=3 e k_off=3, limiar1 μM;
- ponta menos: k_on=1 e k_off=5, limiar5 μM.

Logo v_plus=3c−3, v_minus=c−5 e net=4c−8. O balanço total ocorre em c=2 μM. Ali a ponta mais recebe6 e perde3, saldo+3; a ponta menos recebe2 e perde5, saldo−3. Tamanho médio constante não significa ausência de trocas.

Para c=1,5: saldos+1,5 e−3,5, total−2. Para c=3: +6 e−2, total+4. Sinais opostos não bastam para tamanho constante. O limiar total (soma dos k_off)/(soma dos k_on) é média ponderada dos limiares de ponta, não a média simples.

## Estado estacionário e energia

Alberts distingue mesma afinidade e mesma concentração crítica nas pontas quando todas as subunidades estão no mesmo estado nucleotídico em polimerização simples de equilíbrio. Taxas absolutas diferentes não quebram essa restrição: coeficientes (3,3) e(1,1) têm o mesmo limiar1 e saldos de mesmo sinal.

Para os dois limiares diferentes do exemplo, os coeficientes são efetivos em um regime mantido fora do equilíbrio, representando contextos distintos das pontas. O papel de ATP/ADP é discutido como fundamento biológico, sem calcular hidrólise, estados de nucleotídeos, liberação de fosfato ou manutenção do reservatório. Não chamar esses limiares de constantes de equilíbrio de todo o ciclo.

Não há integração temporal, comprimento inicial, nucleação, barreira N=0, força, motores, migração celular ou microtúbulos. A taxa de perda em c=0 só é local enquanto existir filamento. Não extrapolar para tamanho negativo. Uma previsão de saldo médio não é uma trajetória de monômero, nem movimento rígido do filamento.

## Execução

Na raiz do site, com biblioteca padrão:
    python3 -m labs.actina-concentracao.experiment
    python3 -m unittest discover -s labs/actina-concentracao -t .

rates aceita int/Fraction, rejeita bool/float, concentrações ou dissociações negativas e associações não positivas. Aceita dissociação nula como limite matemático. balance_c calcula a concentração de saldo total zero; stationary_flow exige também um saldo de ponta não nulo. Esse nome descreve o balanço algébrico local e não comprova uma dinâmica estacionária completa. both_balanced significa saldos líquidos nulos em ambas as pontas, não ausência de entradas/saídas.

Cinco testes já existentes, reconferidos:25 concentrações em quartos;81 combinações de coeficientes para o balanço geral; caso de críticos iguais; conversão μM→M e escala comum de taxas; contratos e limite de dissociação nula. Para converter c para M, k_on aumenta um milhão. A correção do teste para Q(c)/1000000 foi feita no bloco anterior, sem alterar as equações. reference.json é referência numérica dos25 pontos, sem dados observacionais.

## Fontes e proveniência

Programa oficial: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211, aberto em22/10/2026; o retorno da ferramenta usa captura de seis dias antes. Ativação15/07/2025; versão efetivamente ministrada não comprovada. Item4 reúne movimento/citoesqueleto/proteínas motoras; Alberts5/6 consta da bibliografia.

Exemplar privado: Alberts e colaboradores, Biologia Molecular da Célula, sexta edição, tradução Artmed2017, capítulo16 pp.901–904 (PDF937–940), consulta parcial textual reconferida em22/10/2026. Trechos sobre taxas, concentração crítica, hidrólise e rolamento; painel16-2. P.904 foi usada até o início da seção seguinte, sem desenvolver substâncias químicas. Não houve leitura integral do capítulo nem nova renderização das páginas neste bloco. A paginação inglesa difere.

Coeficientes, questões e balanco-pontas.svg são próprios; não copiam taxas ou ilustrações do livro. PDFs privados não foram copiados para o site.

## Próxima ação

Recalcular as entradas e saídas em c=1,5;2;3 μM e explicar os três resultados. Depois: proteínas motoras e relação força/movimento com leitura específica. Organização do citoesqueleto e demais lacunas da disciplina continuam pendentes.

Verificação deste bloco:12 testes de catálogo/exemplos/correção e cinco testes do laboratório de actina aprovados;25 linhas da referência numérica comparadas ao cálculo racional.497 estruturas MathML conferidas. Suíte Python completa de864 testes passou no bloco anterior; nenhum código de laboratório foi alterado neste bloco, apenas aula, diagrama e registros. No navegador, resposta−3 aceita na questão4, imagem legível a390px, sem transbordamento horizontal ou erros de console observados. Prévia actina-concentracao-mobile.jpg; viewport restaurado. Catálogo494 aulas/2782 exercícios; todos em rascunho. Saldo semanal96%, parada65%. Próximo preparo global: revisar lacunas e referências de Cálculo II antes de escolher outro aprofundamento; motores seguem como próximo assunto curricular de Biologia III.
