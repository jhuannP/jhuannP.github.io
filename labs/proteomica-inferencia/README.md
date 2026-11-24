# Peptídeos compartilhados e coberturas

28/10/2026. Material original com apoio de IA, revisão pessoal pendente. Banco sintético A:{ACDF,GHIK},B:{GHIK,LMNP},C:{QRST}. Anotações fornecidas, sem previsão de digestão ou proteína real.

Para {GHIK}, coberturas {A},{B},{A,B},{A,C},{B,C},{A,B,C}. Menor cardinalidade1,duas soluções; não se atribui probabilidade ou composição verdadeira. Com {ACDF,GHIK}, única solução de uma entrada{A},mas{A,B} continua compatível. Não se usa a falta de LMNP para excluir B. Com {GHIK,QRST}, menores coberturas{A,C},{B,C}. Acrescentar D:{ACDF} muda a unicidade de ACDF,mesmo sem mudar a observação. VWYA não mapeado deve aparecer como tal,sem cobertura completa. Zero observações: cobertura mínima vazia,todos os oito subconjuntos compatíveis; não demonstra ausência de proteínas.

O código trata conjuntos e correspondência literal,até12entradas. Remove duplicatas de sequência; isso não é quantificação. Enumeração2^P,não pipeline estatístico ou ferramenta para bancos reais. Sem espectros,escores,proteólise,modificações,FASTA,probabilidades,FDR ou implementação de OpenMS.

## Fontes e limites

- Nelson/Cox,Lehninger6PT,Artmed2014: cap.3 p.100/PDF130,trecho inicial de espectrometria consultado parcialmente por texto/imagem em28/10. Razão massa/carga e contexto de fragmentos; tabela de clivagem,figuras e exemplos não reproduzidos. Não é a8ªedição do programa; edição ministrada não comprovada. PDF privado fora do site.
- [CompOmics ProteinInference](https://compomics.github.io/projects/compomics-utilities/wiki/ProteinInference),consulta parcial em28/10: definição,compartilhamento,grupos de ambiguidade e dependência do banco. Fonte apoia a distinção inferencial; dados e enumeração são próprios.
- [OpenMS ProteinInference](https://www.openms.org/documentation/html/TOPP_ProteinInference.html),consulta parcial em28/10: agregação de escores,peptídeos compartilhados,grupos e opção de FDR no nível de proteínas. Nenhuma ferramenta instalada ou executada; nenhum escore/FDR calculado.

A aula distingue identificação de peptídeos,identificação de proteínas e quantificação. O instrumento não fornece diretamente esta lista de conjuntos,que é uma entrada sintética já anotada. Dado real exigiria qualidade de atribuições,controles,banco/versão e pergunta experimental. Instrumentação,quantificação e validação pessoal permanecem pendentes; programa oficial não reaberto neste bloco,data e limitação do mapa preservadas.

## Executar

```sh
python3 labs/proteomica-inferencia/infer.py
python3 -m unittest discover -s labs/proteomica-inferencia -t .
```

Quatro testes: respostas originais;16subconjuntos de observações do banco e checagem de cobertura/ausência de solução menor;dependência do banco,peptídeo não mapeado e duplicatas;contratos. Sequências canônicas de1..100caracteres,são etiquetas didáticas,não justificativa de detectabilidade experimental. Revisão20min: enumerar GHIK,acrescentar ACDF e D,explicar por que parcimônia não prova composição real.
