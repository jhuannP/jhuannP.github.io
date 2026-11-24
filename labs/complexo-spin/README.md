# Complexos: momento efetivo, média e saturação

Modelo didático original assistido por IA para revisão. Um único multiplete de spin S, g escalar, equilíbrio térmico, centros independentes, sem desdobramento a campo zero, contribuição orbital, diamagnetismo ou estados eletrônicos excitados. Não identifica ou prevê quantitativamente um complexo real.

Convenção: r=-mS rotula orientação do momento eletrônico; momento projetado gμB r e energia -gμB B r. x=μB B/(kB T), com T>0. Probabilidades proporcionais a exp(gxr). Resultado `moment` é média por centro dividida por μB; `slope` é derivada desse número em relação a x, não suscetibilidade molar SI. Curie é tangente no zero: g²S(S+1)x/3. Saturação gS; momento efetivo g√S(S+1). Para S2,g2: inclinação8,saturação4,efetivo√24. Modelo S0 tem contribuição de spin zero, não suscetibilidade total zero.

Não converter o coeficiente 2,828 de convenções cgs para SI sem definir unidades. A aula deriva a resposta por centro em relação a B, evitando confundir H/B ou bases molares/volumétricas. Não implementa Curie–Weiss nem transição de fase. Ocupação d⁶ da aula anterior serve como ponte ideal, sem inferir spin real a partir da fórmula química.

Executar:
```
python3 -m unittest discover -s labs/complexo-spin -t .
python3 labs/complexo-spin/response.py
```
Biblioteca padrão, soma exponencial deslocada pelo maior expoente. Aceita 2S inteiro0–20,g real0<g≤10,|x|≤1000,sem bools/não finitos. Limites são operacionais. Campo/temperatura físicos não são fornecidos pelo código. Quatro testes: campo zero/níveis S1/2;525 casos de probabilidade/simetria/limites;derivada por flutuações e saturação;contratos.

## Fontes, consulta parcial em 28/10/2026

- USP CCM0214: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214 — programa reaberto, captura indicada de dois meses antes, ativação15/07/2024. Item9 inclui propriedades magnéticas; versão ministrada em2024/2 não comprovada.
- Miessler/Fischer/Tarr, Química Inorgânica5, Pearson2014, exemplar privado autorizado: §10.1.2 pp.351–352/PDF366–367, consulta textual parcial sobre suscetibilidade e aproximação de spin. Sem nova inspeção visual ou leitura integral; figuras,tabelas e exercícios não reproduzidos,PDF não distribuído. Escolhemos g=2 como hipótese, não como determinação de fator g real. Modelo d⁶ retoma aula anterior, sem nova atribuição de dados experimentais.
- Texas A&M/Hughbanks, material de curso634, Assignment4(2018), p.2/PDF2: https://www.chem.tamu.edu/rgroup/hughbanks/courses/634/homework/18probset4.pdf — consulta textual parcial à distinção entre momento efetivo e saturação; não usamos suas espécies ou solucionamos seus exercícios. Nenhuma leitura integral das11páginas.
- OpenStax Chemistry2e §19.3: https://openstax.org/books/chemistry-2e/pages/19-3-spectroscopic-and-magnetic-properties-of-coordination-compounds — consulta parcial sobre campo cristalino e ligação entre ocupação e magnetismo. Sem reproduzir figuras ou dados.

Derivação de soma de Boltzmann, exemplo, gráfico e código próprios. Pendente: interações, g anisotrópico, spin–órbita, termos, desdobramento de campo zero, dados reais, correções e revisão pessoal.
