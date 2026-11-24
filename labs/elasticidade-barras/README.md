# Elasticidade de barras axiais

Modelo original1D de tração quase estática e pequenas deformações. Não é dado de material medido, modelo de falha ou cálculo completo de uma peça real.

## Grandezas e hipóteses

Tensão nominalσ=F/A₀ em Pa; deformaçãoε=δ/L₀ adimensional. A relação constitutiva linearσ=Eε dá k=EA₀/L₀ em N/m. E é módulo do material na condição adotada; k depende da geometria. Comportamento reversível pode ser não linear. E não informa sozinho limite de proporcionalidade, escoamento ou ruptura.

Entradas do código: metros, m², Pa, N. F≥0, L/A/E>0, int/Fraction, sem bool/float. Comprimentos e áreas são os iniciais; mudanças geométricas de ordem superior são omitidas. O código calcula a fórmula declarada, mas não verifica limites físicos desconhecidos do material. Sem compressão/flambagem, flexão, torção, peso próprio ou transientes inerciais.

## Exemplos prescritos

Barra uniforme:F120N, L2m, A3mm²=3×10⁻⁶m², E40GPa. Resultadoσ40MPa, ε1/1000, δ2mm, k60000N/m, U0,12J. Módulo fictício, sem associação a material real.

Dois trechos, cada um comL1m eE40GPa, áreas2 e4mm²:

- Em série sob120N, mesma força; σ60 e30MPa, alongamentos1,5 e0,75mm. Total2,25mm, rigidez160000/3N/m e energia0,135J.
- Em paralelo sob placas ideais e força total120N, mesmo alongamento0,5mm; forças40 e80N, rigidez240000N/m e energia0,03J. A força total não é aplicada integralmente em cada ramo.

Flexibilidades L/(EA) somam em série. Rigidezes EA/L somam em paralelo. Efeitos3D de transições e apoios não são resolvidos. A média aritmética de áreas não preserva automaticamente a flexibilidade em série.

A energia U=F_finalδ/2 refere-se a carregamento linear quase estático desde zero. Um passo súbito de força exige dinâmica, que não foi calculada.

## Executar e verificar

Da raiz:

```sh
python3 labs/elasticidade-barras/bars.py
python3 -B -m unittest discover -s labs/elasticidade-barras -t .
```

Cinco testes:marcos literais SI; seis geometrias com comprimento/área duplicados; valores de série/paralelo e quatro partições da barra uniforme; referência independente de energia nodal com deslocamento total prescrito e equilíbrio; contratos inválidos. As funções devolvem resultados sem modificar entradas, aceitando até64 trechos.

No teste nodal, δ_total=9/4000m, u_junção=3/2000m e rigidezes80000/160000N/m. A energia tem mínimo0,135J; deslocar a junção por h aumenta U em120000h². Essa referência verifica compatibilidade e equilíbrio por outra descrição; não é evidência experimental de elasticidade.

## Fontes — 29/10/2026

Young/Freedman, FísicaI—Mecânica, Sears e Zemansky,14ª edição brasileira, Pearson2016, confirmada na CIP. Trechos§§11.4–11.5 pp384–386/388–391, PDF403–405/407–410, consultados parcialmente; p386/PDF405 visualmente conferida para Eq11.10. VolumeI é apoio complementar, diferente de FísicaII12ª citado na bibliografia atual do IF. Sem tabelas, figuras, aplicações biológicas ou exercícios reproduzidos. PDF privado não servido.

[OpenStaxUP1§12.3](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus), consulta parcial das definições, sem tabela/exemplos incorporados. As montagens e parâmetros são próprios.

[Júpiter4302112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=4302112) aberto diretamente29/10/2026, captura indicada de quatro dias antes, ativação2026. A tentativa de verdis1 não recuperou versão anterior. Conteúdo atual não comprova programa ou bibliografia da turma2022/2. A evidência institucional2022 já registrada permanece distinta do programa efetivo da turma.

Cisalhamento, compressão volumétrica, tensores, Poisson, plasticidade, outras geometrias e revisão pessoal continuam pendentes. Material assistido por IA não certifica domínio pessoal ou prática de laboratório.
