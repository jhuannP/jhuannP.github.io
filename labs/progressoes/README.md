# Progressões: índice, termo e soma

Aula original `em-progressoes`,12 seções/12 exercícios, em rascunho para revisão pessoal e futura preparação de reforço. Python opcional. Pré-requisitos: frações, potências e equações.

PA usa diferença d e PG usa fator q, por recorrências declaradas. Nesta convenção a₁ é primeiro termo; até a_n há n−1 transições. S_n soma n parcelas. Na PA, duas cópias invertidas justificam 2S_n=n(a₁+a_n). Na PG, subtrair qS_n de S_n deixa apenas os extremos; q=1 é tratado como soma de parcelas iguais. q=0 e termos nulos são tratados pela recorrência sem divisão indevida.

## Fontes e autoria

[OpenStax Algebra and Trigonometry2e §13.2](https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-2-arithmetic-sequences): definição e termo de PA parcialmente consultados em27/10/2026. [§13.4](https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-4-series-and-their-notations): notação e derivação das somas finitas parcialmente consultadas. §13.3 apareceu na busca, mas as duas aberturas diretas falharam; não se registra como leitura do corpo. Sem leitura integral ou reprodução de exemplos/figuras/exercícios. Sequências comparativas, casos, figura, explicações e código próprios.

Sem auditoria de BNCC/vestibular, sem equivalência com a disciplina universitária. A ponte para infinito usa limite das potências, aprofundado em Cálculo. Não se infere regra infinita de prefixo finito nem função contínua física dos índices. Juros, taxas/datas e dados reais não foram modelados.

## Conferência opcional

```sh
python3 labs/progressoes/progressions.py
```

Quatro testes:1470 prefixos contra recorrências com frações exatas, exemplos e extremos, incremento das somas e prefixo que muda no sexto índice, contratos. n≤1000 é limite do laboratório, não uma restrição matemática. Termos exigem n≥1; soma vazia S₀=0. O teste finito verifica implementação, não substitui as provas.

Exemplos a₁4: PA d3 tem a₅16 e S₅50; PG q3/2 tem a₅81/4 e S₅211/4. A PG a₁4,q1/2 tem S₄15/2 e soma infinita8. Casos a₁0, q0/1/negativo e produto vazio declarados. Revisão pessoal e uso com aluno pendentes.


## 27/10/2026 — PA/PG: índice, termo e soma

Nova `em-progressoes`,12 seções/12 exercícios, ligada à etapa de crescimento e à aula de exponencial existente. Convenção a₁, n−1 transições, PA por diferença/indução, PG por fator/recorrência, soma da PA por duas cópias e da PG por cancelamento. q0/1/negativo e sequência nula tratados sem divisão indevida; casos de sobreposição PA/PG, índice zero e soma vazia explícitos. Ponte para infinito com |q|<1 e exceção a₁0. Prefixo de cinco termos pode mudar depois: produto próprio demonstra limite da extrapolação.

Fontes parcialmente consultadas em27/10/2026: OpenStaxAlgebraTrig2e§13.2 https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-2-arithmetic-sequences , definição/termo PA; §13.4 https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-4-series-and-their-notations , notação e derivação de somas finitas. §13.3 localizado por busca, mas duas aberturas diretas falharam; não marcado como leitura do corpo. Sem leitura integral ou cópia de exemplos, exercícios ou figuras. PA4,7,10,13,16 e PG4,6,9,27/2,81/4 são comparações próprias. Sem auditoria BNCC/vestibular.

Quatro testes em `labs/progressoes/progressions.py`:1470 prefixos por recorrência versus termo/soma fechados, exemplos e casos extremos, diferença de somas e prefixo alternativo, contratos. Frações exatas, n≤1000 no laboratório; testes finitos não substituem as provas.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou81/4 e aceitou211/4 para S₅ da PG; documento390/390px, console sem erros observados. Figura inspecionada em `progressoes-termos-mobile.jpg`; viewport restaurada. Windows real, leitor de tela, revisão pessoal e uso com aluno pendentes.

Matemática escolar21 aulas/250 exercícios, sem introduções curtas e sem cobertura integral certificada. Global51 trilhas/576 aulas/5268 exercícios,143 introduções curtas. Próxima ação:duas sessões de20min para reconstruir os termos e somas e conferir as exceções. Próxima elaboração global:aprofundar uma introdução de ComputaçãoII após conferir conteúdo e referência, preservando a distinção do complemento com a disciplina oficial. Saldo semanal antes67%,depois66%; parada operacional65% preservada.
