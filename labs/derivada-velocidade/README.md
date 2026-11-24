# Velocidade, passo e erro de posição

Experimento computacional original preparado com apoio de IA em 28/10/2026. Revisão pessoal de Jhuann pendente. Não é aquisição experimental nem resultado de IC.

## Modelo, unidades e comparação

Considere s(t)=s₀+v₀t+βt³, com s₀ em metros, v₀=2 m/s e β=1 m/s³. Queremos v(1 s)=5 m/s. Os números do código são valores nas unidades SI, não grandezas adimensionais somadas fisicamente.

Sem erro nos valores, a diferença central em t=1 é 5+h² nos valores numéricos SI. Ao reduzir h pela metade, o erro de truncamento cai por quatro. A derivada analítica 2+3t² fornece a referência, sem usar uma malha ainda menor como verdade.

Agora perturbe as posições por e₊ e e₋, ambos limitados em módulo por δ=1/4000 m. A diferença calculada muda por (e₊−e₋)/(2h), cujo módulo é no máximo δ/h. O limite combinado neste cúbico é B(h)=βh²+δ/h, com unidades de velocidade. Escolher e₊=δ e e₋=−δ faz as duas contribuições positivas e atinge o limite. É uma construção determinística de pior caso, sem hipótese de distribuição de ruído.

| h (s) | Erro sem perturbação (m/s) | Limite com δ (m/s) |
|---:|---:|---:|
| 1/5 | 1/25 | 33/800 = 0,04125 |
| 1/10 | 1/100 | 1/80 = 0,0125 |
| 1/20 | 1/400 | 3/400 = 0,0075 |
| 1/40 | 1/1600 | 17/1600 = 0,010625 |

No modelo de limite B, B′(h)=2βh−δ/h². Para β>0 e δ>0, o mínimo positivo ocorre em h=(δ/(2β))^(1/3)=1/20 s; B″(h)>0. Isso minimiza este limite, não descobre automaticamente o melhor passo de um instrumento real. δ=0 remove esse compromisso; β=0 exige outro modelo para o truncamento. Dados em instantes fixos não permitem inventar amostras intermediárias sem nova hipótese de interpolação.

## Executar e verificar

Com Python padrão, na pasta deste laboratório:

```sh
python3 velocity.py
python3 -m unittest test_velocity.py
```

`observed_velocity` e `error_bound` usam `Fraction`/inteiros, rejeitando float e bool, para separar identidade racional de arredondamento. `central` usa int/float finitos e rejeita passos não positivos, colapso dos pontos, valores não finitos e escalas que transbordam. Não verifica suavidade nem estima o erro; exceções da função avaliada propagam. Instantes próximos podem não ter afastamentos exatamente simétricos em float; não há garantia geral de estabilidade do quociente.

Cinco verificações: 486 combinações polinomiais/instantes/passos contra derivadas por coeficientes; 100 pares de perturbações dentro do limite e quatro casos que o atingem; invariância racional por translação e razão de erros quatro; cancelamento em valores de função apesar de tempos distintos; contratos e casos fora de escala. Em particular, para f(t)=10¹⁶+t, t=0 e h=2⁻³⁰, o quociente em float dá zero, embora a derivada matemática seja 1 e os tempos sejam distintos. Em t=1, os valores ficam em lados diferentes de uma fronteira de arredondamento e o quociente dá 2³⁰, também incorreto. Subtrair a origem depois que a informação foi perdida não a recupera.

A tabela float de `velocity.py` compara s₀=0 e 10⁸ m para passos decimais. Os valores dependem da representação e da avaliação. Não se testa que cada refinamento aumente o erro: a curva pode oscilar. O painel existente da aula usa sin(x) e cos(1) como referência; ele mostra outro experimento, não medições de posição.

## Fontes consultadas

Burden, Faires e Burden, *Análise Numérica*, tradução da 10ª edição norte-americana, 3ª edição brasileira, Cengage 2016, exemplar previamente identificado no acervo autorizado. Inspeção visual em 28/10/2026: sumário p.xiv/PDF12; §4.1 pp.193–194/PDF207–208, fórmula central e resto; pp.197–198/PDF211–212, instabilidade dos erros de arredondamento e limite com duas contribuições. Consulta parcial, sem leitura integral de §4.1. Páginas195–196/PDF209–210 vistas para localização/contexto; não foram copiadas tabelas, figuras ou exercícios.

A disciplina CCM0218 indica a 7ª edição, distinta da 10ª escolhida para estudo. Este laboratório é um apoio de análise numérica: não acrescenta ao programa oficial um item que não foi confirmado nele, nem prova que estes exemplos foram ministrados em 2024. A versão da turma continua sem comprovação. Trajetória, dados, deduções, gráfico e testes são próprios; livro privado não é distribuído.

## Revisão de 20 minutos

Antes do código, derive 5+h² usando o modelo cúbico. Depois reconstrua δ/h, calcule as quatro linhas e explique por que h=1/40 s piora o limite em relação a 1/20 s. Por fim mude apenas a origem s₀ no experimento float e explique por que uma invariância matemática pode se perder na avaliação. Registre explicação, ajuda utilizada e dúvidas; nada foi preenchido em nome de Jhuann.

Ficam pendentes: derivação em malhas não uniformes, filtros/regularização, estimativa empírica dos erros, dados reais, comparação com diferenciação automática e revisão pessoal. Usar um quociente central para |t| em zero dá zero, mas não cria uma derivada inexistente.
