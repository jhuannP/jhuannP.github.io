# Equações equivalentes e conferência

Rascunho didático original para revisão de Jhuann e uso futuro nas aulas particulares. Percurso escolar próprio, sem equivalência curricular ou evidência de domínio pessoal.

## Fontes consultadas em 16/10/2026

- [OpenStax Elementary Algebra 2e 2.3](https://openstax.org/books/elementary-algebra-2e/pages/2-3-solve-equations-with-variables-and-constants-on-both-sides): trechos de operações nos dois lados e conferência.
- [OpenStax 2.4](https://openstax.org/books/elementary-algebra-2e/pages/2-4-use-a-general-strategy-to-solve-linear-equations): trechos de estratégia, identidade e contradição.

Não houve leitura integral do livro ou cópia de exercícios/figuras. Texto, sequências, exercícios e código próprios. O aquecimento 3x+2=14 foi preservado da aula existente.

## Modelo

Cinco casos sobre os reais, cada um com quatro etapas: 3x+2=14; 2(x−3)=x+1; 2x+1=2x+3; 3(x+2)=3x+6; (x−1)/2=3/4. Cada etapa usa uma operação reversível ou simplificação equivalente. No caso simples, a etapa final volta à original para conferência; nos demais termina na forma resolvida ou classificação.

Coeficientes a,b,c,d representam ax+b=cx+d. Quando a≠c, há solução única (d−b)/(a−c). Se a=c, b=d admite todo real e b≠d não admite nenhum. O candidato só é substituído, sem mudar a equação.

O gráfico compara Δ=lado esquerdo−lado direito da etapa e da original em −2≤x≤8; zero horizontal serve de referência. Curvas podem coincidir. A prova da classificação é algébrica; uma janela gráfica sozinha não prova ausência de solução. Não há balança física, massas negativas ou sensor.

## Verificação

Na raiz: `python3 -m unittest discover -s labs/equacoes-equivalentes -t .`.

Quatro testes: classificação e substituição racionais em vinte etapas; conservação de pertencimento às soluções em 820 avaliações de caso/etapa/candidato; operações reversíveis em 3125 configurações inteiras com quatro fatores não nulos, mais contraexemplos de cancelamento/divisão; domínio e solução fracionária. `reference.json` contém cem configurações JS/Python.

A rotina geral da aula usa Fraction para contas exatas a partir de inteiros ou strings. O painel usa casos pequenos com coeficientes dyádicos, sem análise genérica de erro de dados. Não é interpretador simbólico nem corretor de manipulações livres.

## Pendências

Equações racionais com domínio variável, sistemas, inequações, mais problemas de tradução, revisão pessoal e aplicação com aluno. Equivalência depende do domínio; operações não reversíveis exigem análise separada. Nenhum curso concluído.
