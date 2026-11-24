# Sequência cis, fator trans e média de RNA — notas de aula

Recorte original em rascunho de regulação transcricional para BiologiaII. Não é um óperon real, resultado de IC ou evidência de prática de bancada. Pré-requisitos: transcrição, concentração, ligação reversível e balanço de produção/remoção.

## Separar os objetos

O operador é uma sequência reguladora cis-atuante do DNA associada ao alvo. O repressor é um produto proteico que pode agir em trans ao alcançar sítios compatíveis. Promotor e operador não são sinônimos; sobreposição é uma possibilidade de arquitetura. A posição distante de uma sequência não a torna uma proteína trans. Classificamos o efeito do produto regulador, não negamos que seu gene também esteja no DNA.

R designa a espécie ativa e competente para ligação, com concentração **livre** r. Ela pode já ser um complexo; ativação e dimerização não são modeladas. Total de proteína de um ensaio não substitui automaticamente r.

## Sítio livre e sítio ocupado

No modelo D+R⇌DR, um sítio possui probabilidade ocupadaθ e livre1−θ. O reservatório mantém r constante, sem depleção apreciável por ligação aos sítios. k_on tem unidade nM⁻¹·min⁻¹ e k_off tem min⁻¹. O balanço é

`θ′=k_on r(1−θ)−k_offθ`.

No regime estacionário da ligação reversível, igualar os fluxos dá θ=r/(K_d+r), com K_d=k_off/k_on em nM. A fração livre é K_d/(K_d+r). A meia ocupação ocorre em r=K_d. K_d menor aumenta ocupação ao mesmo r. Essa é uma hipótese de sítio único, sem cooperatividade; não é lei universal da expressão de genes.

O sítio ocupado bloqueia inteiramente a transcrição por hipótese. No estado livre, uma cópia produzαRNA/min. A síntese média é s=α(1−θ). Com remoção linearδ por minuto, a média m satisfaz m′=s−δm e m*=s/δ. Equilíbrio da ligação reversível não significa que o sistema de expressão inteira esteja em equilíbrio termodinâmico: há produção e remoção contínuas de RNA no estado estacionário.

## Exemplo e duas perturbações distintas

Adote k_on=0,1nM⁻¹·min⁻¹, k_off=1min⁻¹, r=30nM, α=8RNA/min eδ=0,5min⁻¹. São parâmetros inventados. Então K_d=10nM, θ=3/4, fração livre1/4, síntese2RNA/min e média4RNA por cópia. Uma média não precisa ser uma contagem inteira em cada célula.

| Construção/condição | Ocupação | Síntese média (RNA/min) | Média estacionária de RNA |
|---|---:|---:|---:|
| A: operador funcional, r=30 | 3/4 | 2 | 4 |
| B: sítio sem ligação, mesmo meio | 0 | 8 | 16 |
| A sem repressor ativo, r=0 | 0 | 8 | 16 |
| A com K_d=30nM, r=30 | 1/2 | 4 | 8 |

A e B compartilham o mesmo meio em um contraste ideal de repórteres. Eliminar a ligação no sítio B mantendoα eδ iguais é uma hipótese controlada, não consequência automática de uma mutação. A razão A/B é1/4. Mudar r é uma alteração do fator em trans; mudar a sequência/afinidade do sítio é uma alteração cis. B já não era sensível ao repressor no modelo; o fato de não mudar não prova ausência de outros efeitos celulares.

A condição r=0,α=8,δ=2 tem síntese8RNA/min e média4RNA, igual à condição reprimida que sintetiza2RNA/min e remove comδ=0,5. Assim, só a média estacionária não identifica qual parâmetro mudou, nem demonstra mecanismo ou causalidade. Proteína, fluorescência e atividade funcional exigem modelos adicionais.

## Transiente: uma fração de equilíbrio não muda instantaneamente

Após impor r constante, defina b=k_onr+k_off, θ*=k_onr/b, m*=α(1−θ*)/δ. A solução da primeira equação é θ(t)=θ*+(θ₀−θ*)exp(−bt). Inserindo em m′+δm=α(1−θ), um fator integrante dá

`m(t)=m*+(m₀−m*)exp(−δt)−α(θ₀−θ*)C(t)`.

A convolução C(t) é a integral de exp[−δ(t−u)]exp(−bu) de0 atét. Para b≠δ, ela vale [exp(−δt)−exp(−bt)]/(b−δ); quando b=δ, vale texp(−δt). O código usa uma expressão equivalente com expm1 para evitar cancelamento perto de taxas iguais.

No salto r=0→30nM, θ₀=0,m₀=16, a ligação relaxa em0,25min; o RNA, em2min. Em t=1min, a referência prevê θ≈0,736263 e m≈12,286737. No instante inicial, m′=8−0,5×16=0; substituir imediatamente θ=3/4 daria m′=−6RNA/min. Essa diferença mostra o limite da aproximação de ocupação instantânea no início. São médias do modelo linear, sem ruído de trajetórias individuais ou feedback sobre r.

## Código e verificação

Execute `python3 labs/repressor-cis-trans/regulation.py`. Seis testes:40 combinações racionais conferem os balanços de ligação e de RNA; previsões cis/trans e ambiguidade; escalas e derivada inicial; solução acoplada confrontada com RK4 em cinco tempos; caso de taxas iguais e próximas em quatro tempos; monotonicidade, produção zero e contratos. O tempo0–20min é intervalo didático do código, não domínio universal de regulação. O RK4 é uma integração numérica das duas equações, sem usar a solução fechada nos estágios; os testes têm tolerância10⁻⁷ nos estados. Isso verifica o código para exemplos, sem validar um circuito real.

O código racional de estado estacionário não gera um experimento aleatório. O modelo não ajusta K_d,α,δ ou r a dados. Para explicar uma observação real, seria preciso avaliar desenho, disponibilidade do fator, produção/degradação, cromatina e demais mecanismos pertinentes.

## Referências efetivamente consultadas

- [USP — CCM0121 BiologiaII](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0121), reaberto em27/10/2026; móduloII item4, transcrição/regulação, ativação01/01/2025. Compatibilidade com a turma registrada não comprova versão efetivamente ministrada.
- Alberts e colaboradores, *Biologia Molecular da Célula*,6ª ed., tradução2017 identificada no acervo, cap.7 pp.380–381/PDF416–417 e cap.8 pp.514–515/PDF550–551: consulta textual parcial em27/10/2026. Sequências cis, repressão, fração ocupada/livre e modelagem quantitativa. O livro emprega constante de associação K; aqui usamos K_d=1/K. O recorte quantitativo da fonte discute síntese de proteína, enquanto estas notas explicitam um modelo de **RNA**; não se transfere a variável ou parâmetro sem redefinição. Sem nova inspeção visual, leitura integral, cópia dos exemplos/figuras ou distribuição do livro.

A busca pública localizou o capítulo da4ª edição no NCBI, mas a abertura retornou verificação de navegador; não é contada como leitura integral ou usada para fingir conferência da6ª edição. O suporte efetivamente consultado vem do exemplar privado e do programa acima. Exemplos, repórteres, comparação, figura, deduções e exercícios próprios. Modelo de sítio único é uma construção clássica, sem alegação de descoberta original ou domínio pessoal de Jhuann.

## Próxima revisão — vinte minutos

Desenhe operador e proteína reguladora, marcando cis/trans. Reconstrua as médias4 e16 e explique os dois mecanismos que dão4. Depois interprete0,25min versus2min e diga por que a quantidade de RNA não muda instantaneamente. Registre uma dúvida antes de ampliar para cooperatividade ou cromatina.
