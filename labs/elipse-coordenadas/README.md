# Elipse: reduzir a equação antes de classificar

Notas próprias assistidas por IA, em rascunho para revisão de Jhuann. Primeira aula própria de MAT0112 no catálogo; aprovação no IF e materiais preparados não certificam domínio atual nem equivalência administrativa com disciplinas do CM.

## Fontes e vínculo curricular —26–27/10/2026

O [programa oficial MAT0112](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=MAT0112) inclui curvas planas/cônicas e noções de quádricas no item6. Página recuperada em26/10/2026, ativação01/01/1973 e captura indicada de quatro dias antes; versão efetivamente ministrada em2021 não recuperada. O histórico aprovado2021/1 continua sendo o registro anterior conferido, sem nova leitura do PDF escolar neste bloco.

Leituras complementares primárias parciais:

- [OpenStax Precalculus2e, §10.1](https://openstax.org/books/precalculus-2e/pages/10-1-the-ellipse): definição por focos, forma padrão e semieixos.
- [§10.4](https://openstax.org/books/precalculus-2e/pages/10-4-rotation-of-axes): equação geral, mudança de eixos e limite de identificar só pelos coeficientes quadráticos.

Consulta entre26 e27/10/2026, sem leitura integral do capítulo ou transcrição de figuras, exercícios e exemplos. O exemplo matricial e o algoritmo por frações são próprios. Boulos/Camargo é referência oficial; o inventário anterior encontrou título/autores, mas não confirmou segunda edição/1987. O corpo desse exemplar não foi consultado aqui; não há transferência de paginação ou substituição da edição curricular por uma presumida.

## Modelo e redução

P(x,y)=36x²−24xy+29y²−120x+140y+20. A matriz simétrica da parte quadrática tem diagonal36,29 e entradas fora da diagonal−12, não−24. Isso evita duplicar o termo misto.

Após x=h+X,y=k+Y, os termos lineares se anulam quando72h−24k−120=0 e−24h+58k+140=0. Resulta centro(1,−2), P no centro−180 e equação centrada wᵀQw=180.

As direções e_u=(3/5,4/5) e e_v=(−4/5,3/5) são ortonormais. Qe_u=20e_u e Qe_v=45e_v. Com u=e_u·(x−1,y+2),v=e_v·(x−1,y+2), a curva é20u²+45v²=180, isto é,u²/9+v²/4=1. Semieixos3,2; c_f²=5 e soma das distâncias aos focos6. O argumento por distâncias no texto confere positividade das raízes, evitando concluir apenas de uma igualdade de quadrados.

Transformação inversa: x=1+(3/5)u−(4/5)v; y=−2+(4/5)u+(3/5)v. O vértice(3,0) vira(14/5,2/5), resíduo zero no polinômio original. Centro não é ponto da elipse: seu resíduo é−180.

F=200, mantendo os demais coeficientes, deixa apenas o centro. F=201 deixa conjunto vazio. O discriminante B²−4AC é−3600 nos três casos. Seu sinal, sozinho, não distingue existência e degeneração. O laboratório recusa partes quadráticas singulares/indefinidas, incluindo parábolas/hipérboles; não é um classificador universal.

## Executar e conferir

Na raiz do site:

```sh
python3 -m labs.elipse-coordenadas.ellipse
python3 -m unittest discover -s labs/elipse-coordenadas -t .
```

Funções recebem int/Fraction, não bool/float. `reduce_definite` usa Δ=4AC−B²>0 e normaliza o sinal global se A<0. Recupera centro e constante por contas exatas; não calcula raízes/eixos de toda matriz. O rótulo elipse inclui circunferência como caso especial. Multiplicar a equação inteira por escalar não nulo preserva o conjunto, mas escala os coeficientes e a constante normalizada.

Cinco testes: exemplo/degenerações;324 equações construídas a partir de somas de quadrados, com centro e sinal conhecidos;22 pontos por parametrização racional e vértice limite, conferindo ida/volta e norma;49 pontos comparando polinômio original com expressão local, escala global; contratos/recusa de casos fora do escopo. A prova algébrica sustenta a redução, não apenas a amostragem de testes. Figura amostrada com ponto flutuante somente para exibição, na mesma escala por unidade de x/y.

## Revisão e próximos recortes

Em20min, encontre o centro, explique B/2, leve o vértice para x,y e compare F=20,200,201. Respostas dos dez exercícios numéricos:1;−2;−12;180;3;2;5;14/5;2/5;−180. Os dois conceituais distinguem ponto e vazio.

Parábolas, hipérboles, demais degenerações e classificação de quádricas ainda precisam de sequência. Produto vetorial sistemático e outras partes do programa também continuam parciais. Não duplicar automaticamente os apoios de Matemática do CM como se fossem a disciplina efetiva do IF.
