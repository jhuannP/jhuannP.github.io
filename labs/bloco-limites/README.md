# Bloco: contato e atrito são restrições distintas

29/10/2026. Rascunho original para revisão de Jhuann; Python opcional.

Bloco rígido, baseB>0m, peso centralW>0N, força horizontalP≥0N aH≥0m, piso horizontal, coeficienteμ≥0, repouso inicial. N=W,f=−P,x=PH/W. LimitesP≤μW eP≤WB/(2H) seH>0. H0: este empurrão não tem momento em torno da base, limiar de tombamentoNone. Não há força vertical extra ou adesão.

Reações equivalentes nas bordasW/2±PH/B fecham forças/momentos. Não são uma medição ou modelo de pressão. Resultadoadmissible inclui a fronteira: no limite de tombamento o contato está na borda, sem certificar estabilidade robusta. Se falha, as reações retornadas são exigências algébricas impossíveis sob as hipóteses, não previsões de contato físico. Modelo não calcula movimento após falha, deformação, ruptura ou segurança de carga.

Referência original:W300N,B4/5m,H6/5m,μ2/5,P90N. x9/25m, margem à borda1/25m, margem de atrito30N; equivalentes15/285N. Limiar de tombamento100N, atrito120N. P110N pede normal fora da base. μ1/5 troca primeiro modo para deslizamento60N; μ1/3 simultâneos100N. Altura3/5m dá limite de tombamento200N e atrito primeiro120N.

Fonte complementar:[OpenStax CollegePhysics2e9.3](https://openstax.org/books/college-physics-2e/pages/9-3-stability), consulta textual parcial29/10/2026 de estabilidade/base de suporte. Nenhum experimento/figura/atividade copiado. Derivação e exemplos próprios. Não houve nova leitura doNussenzveig neste bloco ou auditoria de programa escolar.

```sh
python3 labs/bloco-limites/limits.py
python3 -B -m unittest discover -s labs/bloco-limites -t .
```

Cinco testes: referência/modos;54 configurações com somas de forças e torques em três origens independentes; fronteira e duas falhas distintas; escalas e altura/atrito zero; contratos. EntradasSI int/Fraction, sem bool/float. Testes não validam objeto real ou ensino com aluno.
