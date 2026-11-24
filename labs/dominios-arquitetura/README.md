# Domínios:anotações,arquitetura e evidência

Rascunho original assistido por IA,28/10/2026,revisão pessoal pendente.Não é busca,predição ou função experimental.

## Fontes

[USPCCM0121](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121),reaberto28/10/2026,ativação01/01/2025,captura de um mês antes:itemI.7domínios/evolução.Sem comprovar versão ministrada.
Lehninger6 em português,cap.4 p.137/PDF167 e recorte p.140/PDF170,consulta textual parcial28/10 para motivo/domínio e relação estrutural/evolutiva.Sem nova inspeção visual/leitura integral ou PDF servido;difere da8ªed.2021oficial.PatthyProteinEvolution2ed2008 continua não localizado.
[InterProEntryTypes/EMBL-EBI](https://www.ebi.ac.uk/training/online/courses/interpro-functional-and-structural-analysis/what-is-an-interpro-entry/interpro-entry-types/),consulta parcial28/10/2026:categorias,domínio,sítio/repetição.Sem imagens ou exemplos copiados.URL inicial genérica de domínio indisponível,não texto lido.

## Modelo fornecido

Coordenadas1-based,inclusivas,comprimento b−a+1.Anotações não significam fronteiras biológicas comprovadas.
P180:A11–60,B91–160 →120cobertos,2/3,ordemA–B.
Q220:A11–60,B91–160,B171–210 →160cobertos,8/11,ordemA–B–B.
R180:B11–80,A111–160 →120cobertos,2/3,ordemB–A.
Sem anotação não significa sem função ou desordem.São proteínas e rótulos fictícios.
Sobreposição20–80/60–100:61+41−21=81naunião,não102.Resultados sobrepostos não geram arquitetura linear única aqui;podem representar modelos relacionados/alternativos ou organização mais complexa.

## Executar

```sh
python3 labs/dominios-arquitetura/annotations.py
python3 -m unittest discover -s labs/dominios-arquitetura -t .
```

Comprimento1–10000,até64hits,rótulos textuais1–32,coordenadas inteiras inclusivas.Recebe intervalos,não sequência ou perfil.Ordena,calcula união,contagem de anotações e pares sobrepostos.Hits idênticos não aumentam cobertura,mas continuam duas anotações: não duas cópias biológicas comprovadas.ordered_labels ficaNone quando há sobreposição.Não resolve conflito,domínios descontínuos ou ambiguidade de bancos.Supor módulos contíguos é simplificação do exercício.

Quatro testes:exemplos/permutação de entradas;1296pares de intervalos contra conjunto de posições;vazio/duplicação de anotação;contratos.

## Revisão20min

Desenhe as três arquiteturas,confira as frações e a união81.Explique o que se perde ao usar conjunto sem ordem e por que arquitetura não prova função ou direção evolutiva.Pendentes:sequências reais,bancos/modelos versionados,filogenia,estruturas e revisão pessoal.
