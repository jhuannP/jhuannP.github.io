# Gradiente, curvatura e parada

Quadrática prescritaΦ=(x²+4y²)/2 em coordenadas adimensionais, Hessiana diag(1,4), mínimo único(0,0). Rascunho assistido porIA,revisão pessoal pendente. Não é otimizador geral, treino deML ou resultado experimental.

Na raiz:

```sh
python3 -B -m labs.gradiente-espectro.descent
python3 -B -m unittest discover -s labs/gradiente-espectro -t .
```

Int/Fraction sem bool/float. `history` guarda todos os estados,k0incluído,passo0..2e0..200atualizações,sem parada automática. Aceitar passo instável serve à comparação, não recomenda seu uso. `inspect` devolve custo,gradiente e norma²,sem arredondamento. Fórmula fechada xk=x0(1−η)^k,yk=y0(1−4η)^k.

Estabilidade para todos os inícios exige0<η<1/2. Emη1/2,yoscila±1 no início(1,1),custo→2em vezde0;diferençaΦ10−Φ11=3/(8×4^10)<1e−6 enquanto norma do gradiente≥4. Um critério só de mudança no custo pode parar indevidamente. Norma²/8≤Φ≤norma²/2 neste modeloSPD, não cota universal sem hipóteses. Emη1,início(1,0)vai à origem apesar da instabilidade em outra direção;um início não demonstra estabilidade uniforme.

`contraction` calcula q=max(|1−η|,|1−4η|). Melhor passo constante para esse pior fator é2/5,q3/5;é propriedade espectral do modelo, não melhor primeiro passo para todo início. Em(1,1),η1/4dácusto9/32menor queη2/5dá9/10. `exact_line_step`minimiza apenas na direção−g corrente:η=(g·g)/(g·Hg),17/65nessa referência;origem retornaNone. Não é busca binária nem implementação genérica de line search. Coordenadas novas48/65,−3/65,custo234/845,gradiente novo ortogonal ao antigo.

Cinco testes:referência/line search;567estados fechados/nove gradientes por diferenças centrais;101amostras do piorfator e onze estados de custo;fronteira/subespaço invariante;snippet/desafio/contratos. As101amostras não provam minimaxreal;a aula fornece argumento analítico. Sem executar todas as suítes dos outros laboratórios.

Fontes:Burden/Faires/Burden,10ªedição/traduçãoCengage2016,§10.4pp730–731/PDF742–743visual,30/10/2026,gradiente/direção e conexão com sistemas. Primeira tentativaPDF751mostroup739,continuação,outro tema;offset12deste trecho conferido,sem transferir offset13/14de capítulos anteriores. D2L1.0.3§12.3.1.1/12.3.2 e menção12.3.3.4,corpo parcial30/10, https://d2l.ai/chapter_optimization/gd.html . Quadrática antiga,derivações adicionais,tabela e código locais;sem copiar atividade/figura ou executar frameworks. Não se universaliza condição estacionária como mínimo global.
