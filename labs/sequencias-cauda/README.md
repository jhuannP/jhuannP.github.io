# Sequências: definição, cauda e fronteira

27/10/2026. Notas de aula originais assistidas por IA, em rascunho para revisão de Jhuann. Pré-requisitos: frações, módulo, desigualdades e índices inteiros. Código opcional; não comprova aprendizagem ou conclusão de Cálculo2.

Preservado a_n=n/(n+1), com erro exato1/(n+1). Para todos n≥N, erro<ε começa em N=max(1,⌊1/ε⌋); erro≤ε começa em max(1,⌈1/ε⌉−1). Tolerância1/10 dá10 versus9, e3/20 dá6 nos dois comparadores. A fórmula é específica desse erro e da convenção n≥N, não um detector geral de convergência.

A aula demonstra convergência monótona pelo supremo, separa limitação de monotonicidade, usa(−1)^n/n como exemplo convergente oscilatório e pares/ímpares para refutar convergência de(−1)^n. Recorrência d₁=1/2,d_(n+1)=(d_n+1)/2 é provada crescente e limitada antes de passar ao limite. Sua fórmula é1−2^(−n). A série dos termos n/(n+1) diverge, embora a sequência convirja. Prefixos finitos idênticos podem ter caudas com comportamentos diferentes.

## Fontes e alcance

Apostol, Calculus vol.I, 2ª ed.1967, §§10.2–10.3 pp.379–381/PDF399–401, consulta textual parcial em27/10/2026: função de índice inteiro, limites e convergência monótona. Páginas PDF contadas a partir de1. OCR com imperfeições; sem leitura integral ou nova inspeção visual. [OpenStax Calculus vol.2 §5.1](https://openstax.org/books/calculus-volume-2/pages/5-1-sequences), recortes sobre sequências, limites e critério monótono, consulta parcial. Exemplos, deduções, figura e código próprios; sem transcrição de exercícios ou distribuição do livro privado. Júpiter não reaberto; limites de versão curricular já registrados em CALCULO_2.md permanecem.

## Verificações

Execute `python3 labs/sequencias-cauda/sequences.py`. Cinco testes:400 tolerâncias racionais p/q com p,q de1..20, nos dois comparadores; primeiro índice e anterior, mais30 termos de cada cauda;70 identidades da recorrência e diferença de termos; prefixo finito/oscilações; contratos; cancelamento de ponto flutuante quando o ambiente tem base2 e53 bits de precisão. Testar30 termos não prova controle infinito: a monotonicidade explícita do erro faz esse papel na dedução.

Para n=2^54, o erro racional é1/18014398509481985, positivo; no formato testado, n/(n+1) arredonda para1 e a subtração dá0. A expressão direta1/(n+1) continua positiva, embora aproximada. Esse contraste explica cancelamento/arredondamento, não muda o limite matemático. O teste específico é omitido em outro formato, sem assumir equivalência entre todos os ambientes.

Próxima ação de20min: explicar10 versus9, reconstruir a prova pelo supremo e refutar o limite de(−1)^n por duas subsequências. Espaços gerais, Bolzano–Weierstrass e teoria completa de Cauchy continuam pendentes. Figura usa pontos discretos e faixa de erro, sem interpolação contínua.
