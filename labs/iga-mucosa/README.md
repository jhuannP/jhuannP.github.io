# Mucosas e IgA: rota e leitura quantitativa

Rascunho original assistido por IA,28/10/2026;revisão pessoal pendente. Não é protocolo,não há experimento realizado ou taxa fisiológica inferida.

## Fontes consultadas e proveniência

- [USP CCM0221](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221),consulta28/10/2026,ativação01/01/2025,captura indicada de dois meses antes. Item1.9 é sistema possível;não comprova seleção efetiva da turma.
- Janeway,Imunobiologia,8ª edição portuguesa,Artmed2014,exemplar privado autorizado. Folha de rostoPDF3 e copyrightPDF4 reconferidos textualmente;recortes de§10.15 p.409/PDF428,§12.3 p.468/PDF487 e§12.11 pp.482–483/PDF501–502. Legenda de organização p.470/PDF489 consultada textualmente. Sem leitura integral,nova inspeção visual ou PDF distribuído. Formas,compartimentos e rota do receptor apoiados nesses recortes;figura e contas próprias. Não adotamos as afirmações históricas/quantitativas específicas do livro sobre proporções,produção ou exclusividade de vias de indução.
- [Johansen et al.,1999,JEM190:915–922,DOI10.1084/jem.190.7.915](https://doi.org/10.1084/jem.190.7.915):resumo e metadados no editor consultados em28/10/2026. Relato em camundongos deficientes em pIgR de perda de transporte ativo e sinais de alteração de barreira. Sem métodos/figuras integrais;sem extrapolação humana. PubMed/PMC apresentaram verificação de acesso e não foram lidos como artigo.

## Executar

Na raiz do protótipo:

```sh
python3 labs/iga-mucosa/transport.py
python3 -m unittest discover -s labs/iga-mucosa -t .
```

O código aceita inteiros/Fraction,com unidades dadas pelos nomes dos argumentos. Rejeita bool,float,grandezas negativas,área/tempo/volume zero e concentração menor que branco. É uma calculadora exata deste cenário,não um modelo de pIgR ou análise estatística.

## Rota para reconstruir

Plasmócito na lâmina própria → IgA dimérica com cadeia J → ligação ao pIgR basolateral → endocitose/tráfego vesicular → liberação apical após clivagem → IgA associada ao componente secretor no lúmen.

Diferencie produção/transporte;cadeia J/fragmento do receptor;amostragem luminal por células M/exportação de IgA;presença/neutralização. Há heterogeneidade entre mucosas e vias adicionais,não desenvolvidas aqui.

## Dados inteiramente inventados

|Cenário|Medida μg/mL|Branco μg/mL|Volume mL|Área cm²|Tempo h|Massa μg|Taxa aparente μg/(cm²·h)|
|---|---:|---:|---:|---:|---:|---:|---:|
|A|12|2|0,5|1|2|5|2,5|
|B|7|2|0,5|1|2|2,5|1,25|
|B com outro volume|7|2|1|1|2|5|2,5|

Q=(C−branco)V;J_ap=Q/(AΔt). Branco aditivo e calibração linear válidos,volume final,mistura homogênea,massa apical inicial nula e nenhuma retirada anterior de amostras. Média de aparecimento não identifica fluxo instantâneo ou unidirecional.Nenhuma hipótese de linearidade temporal é necessária para essa média;perdas,retorno e degradação limitam sua interpretação como transporte.

20μg iniciais;12 no doador,5 no apical,1 celular:18 recuperados,90%,2 não contabilizados. Uma leitura total22 produziria110% e−2 não contabilizados:flag de excesso,sem truncar ou afirmar criação de massa. Código não incorpora incerteza da medida.

## Próximos20min

Desenhe a rota,refaça A/B e explique o contraexemplo de volumes. Liste quais controles testam pIgR,integridade,viabilidade,detecção e função. Trate resgate como evidência adicional,não prova isolada. Réplicas e incertezas ausentes;nenhuma significância inferida.

Pendentes:tolerância oral,microbiota,homing/indução detalhados,respostas independentes de T,outras mucosas,protocolo efetivo e revisão pessoal. Fonte curricular não comprova experiência de laboratório.
