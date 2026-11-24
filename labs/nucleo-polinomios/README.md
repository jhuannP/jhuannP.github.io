# Núcleo da derivada em polinômios

Notas de aula e código originais assistidos por IA, para revisão pessoal. Não é resultado de pesquisa nem experiência experimental.

Em P₃, a base ordenada é (1,t,t²,t³). D:P₃→P₂ tem matriz [[0,1,0,0],[0,0,2,0],[0,0,0,3]], núcleo span(1) e imagem P₂. Posto 3 + nulidade 1 = dimensão 4. Com contradomínio P₃, a mesma regra não é sobrejetiva.

Para q(t)=2−2t+3t², Jq=2t−t²+t³. Toda solução de Dp=q é Jq+C. p(1)=5 determina C=3, e p(2)=11. DJ é identidade em P₂; JDp=p−p(0), portanto não é identidade em P₃. Reconstrução com valor inicial fixo não nulo é afim em q; não é inversa linear bilateral de D. Em variável adimensional t, os números são adimensionais; aplicação física exigiria escala temporal e unidades.

O código usa coeficientes crescentes e preserva zeros finais. Até 9 coeficientes racionais (grau máximo 8); primitiva aceita até 8. Não é derivação numérica, ajuste de dados ou sistema geral de álgebra simbólica. Racionais exatos não modelam ruído experimental.

Executar na raiz do protótipo:
```
python3 -m unittest discover -s labs/nucleo-polinomios -t .
python3 labs/nucleo-polinomios/polynomials.py
```

Testes: imagens da base; 625 polinômios e identidades/reconstrução em três pontos racionais; exemplo e não linearidade para condição não nula; contratos.

## Fontes e alcance

- USP CCM0213: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213 — reaberto em 28/10/2026, ativação 15/07/2024. Itens 1, 2 e ponte didática com 6; não comprova versão efetivamente ministrada em 2024/2.
- Elon Lages Lima, Álgebra Linear, IMPA 2014, referência complementar do acervo autorizado: §3 pp.26 e31/PDF37 e42 (base/dimensão de polinômios), §6 pp.58–60/PDF69–71 (imagem, derivação e inversa à direita), pp.65–66/PDF76–77 (teorema núcleo/imagem). Consulta textual parcial em 28/10/2026; sem nova inspeção visual ou leitura integral. Não consta da bibliografia oficial consultada; PDF privado não distribuído. O operador derivada é exemplo clássico também discutido na fonte, não descoberta original. Coeficientes, condição inicial, figura, cálculos e código deste roteiro são próprios.
- Georgia Tech, Interactive Linear Algebra §3.3: https://textbooks.math.gatech.edu/ila/linear-transformations.html — consulta parcial em 28/10/2026 à linearidade e obtenção da matriz por imagens da base; fórmulas ausentes da extração não tomadas como transcrição literal. Não é fonte de atribuição do exemplo polinomial específico.

Permanece pendente: outros espaços de funções, operadores diferenciais gerais, análise de ruído, revisão pessoal e cobertura integral dos programas.
