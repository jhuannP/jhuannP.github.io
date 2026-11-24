# Poço infinito — fronteiras, níveis e probabilidades

27/10/2026. Notas de aula originais com apoio de IA, em rascunho; revisão pessoal de Jhuann pendente. Aprofundamento de `f4-poco`, mantendo exemploE₃/E₁, ids de exercícios, Python/desafio e painel `wellDensity`. Não representa experiência experimental ou conclusão da disciplina.

## Contexto e referências

MapaCCM0222: FísicaIV, aprovação2026/1 segundo panorama dos históricos; não houve nova leitura desses documentos ou do programa neste bloco. Programa de ativação01/01/2025 já havia sido reconferido diretamente em27/10; compatibilidade não prova versão efetivamente ministrada. Óptica preparatória e organização do percurso continuam distintas de equivalência administrativa.

Nussenzveig, *Curso de Física Básica*, volume4, segunda edição2014, reimpressão2017/edição digital2018, exemplar autorizado já identificado. Consulta parcial em27/10/2026 a §10.3(a), pp.298–302/PDF299–303; p.300/PDF301 renderizada e inspecionada para espectro/energia. A fonte usa caixa centrada−a/2<x<a/2; nestas notas transladamos para0<x<L, comL=a. Não tratar os dois x como coordenadas de mesma origem. Livro privado não distribuído, sem copiar figuras/exercícios ou alegar leitura integral.

Apoio parcial: [OpenStax University Physics3 §7.4](https://openstax.org/books/university-physics-volume-3/pages/7-4-the-quantum-particle-in-a-box), fronteiras e normalização. As provas específicas, probabilidades, comparação de malhas e gráfico são próprios. Evolução de dois modos permanece detalhada em outra aula e não é recontada como novo resultado aqui.

## Hipóteses e solução

Uma partícula sem spin, uma dimensão, m>0,L>0, regime não relativístico; potencial interno zero, paredes fixas idealmente impenetráveis. φ(0)=φ(L)=0, função nula fora. Massa, largura eℏ nos cálculos de energia precisam ter unidades compatíveis; defaults do código são escalas reduzidas1, não constantes físicasSI.

No interior, −ℏ²φ″/(2m)=Eφ. Multiplicar porφ* e integrar por partes dáE∫|φ|²=(ℏ²/2m)∫|φ′|²≥0. E=0 exigiriaφ constante, e as fronteiras a fariam zero. Para um estado normalizado, E>0 no zero de potencial escolhido. Esse argumento usa as condições de fronteira do operador, sem resolver a parede infinita como uma região regular de potencial finito.

ParaE>0: k²=2mE/ℏ², φ=A sen(kx)+B cos(kx). φ(0)=0 dáB=0. φ(L)=0, A≠0, dákL=nπ. n=0 é nulo; negativos mudam apenas sinal global. Modos físicos distintos podem ser enumerados por n=1,2,3,… .

Integrar sen² pelo duplo ângulo dáL/2. Assim φₙ=√(2/L)sen(nπx/L), escolhendo uma fase global real positiva. Eₙ=π²ℏ²n²/(2mL²). Produtos de senos distintos integram zero; no caso do mesmo índice, a norma é1. Não se prova aqui completude geral de toda expansão.

E₁>0 relativamente ao potencial interno, E₂=4E₁,E₃=9E₁. DobrarL dá fator1/4; dobrar m dá1/2. DiferençaE₃−E₂=5E₁ não é razãoE₃/E₁=9. Uma transição real exige interação e condições adequadas, não apenas dois níveis escritos num gráfico. Somar constante a todo o potencial desloca energias sem alterar esses intervalos.

## Densidade e probabilidade

s=x/L eΦ=√Lφ; ρₙ(s)=|Φ|²=2sen²(nπs). A figura usa a mesma escala vertical nos três painéis, alturas não são energias. Nós internos: x=jL/n,j=1,…,n−1.

Para0≤a≤b≤1:

Pₙ(a,b)=(b−a)−[sen(2nπb)−sen(2nπa)]/(2nπ).

No intervalo central[1/4,3/4]:

| Modo | Probabilidade |
|---|---|
|1|1/2+1/π≈0,81831|
|2|1/2|
|3|1/2−1/(3π)≈0,39390|

Metade do comprimento não implica metade da massa para todo modo. Um ponto isolado tem massa zero, mesmo ondeρ₁(1/2)=2. φ dimensional tem unidadecomprimento⁻¹/², densidade dimensionalcomprimento⁻¹ e probabilidade é adimensional. O sinal global da autofunção não mudaρ.

Por simetriaρ(s)=ρ(1−s), a posição média éL/2. No segundo modo, essa média coincide com um nó. O estado estacionário tem faseexp(−iEₙt/ℏ), densidade constante e, para esse modo real, corrente zero; isso não representa uma trajetória de partícula em repouso.

Para intervalo fixo, |Pₙ(a,b)−(b−a)|≤1/(nπ), portanto a massa tende à fração de comprimento quando n cresce. A densidade não converge ponto a ponto para1: no centro alterna entre2 e0. Espaçamento absoluto(2n+1)E₁ cresce; espaçamento relativo porEₙ tende a zero. Distinguir as afirmações evita um limite clássico impreciso.

## Código e malha

`well.py` usa apenas Python padrão. Avalia modos analíticos, não resolve umaEDP em malha nem potencial geral. Modos inteiros1–1000 e malhas1–100000 são limites operacionais, não limites físicos do espectro. Entradasint/float finitas, sembool; parâmetros de energia positivos. Coordenadas fora do poço dão amplitude zero. Probabilidades pedem0≤a≤b≤1; intervalo degenerado dá zero. Energia não representável porfloat geraArithmeticError, sem tratá-la como energia física zero.

```sh
python3 -m labs.poco-infinito.well
python3 -m unittest discover -s labs/poco-infinito -t .
```

Probabilidade é avaliada numa forma que reduz cancelamento: d=b−a,z=nπd,θ=nπ(a+b), P=d[(1−cosθ)+cosθ(1−sen(z)/z)]. Usa1−cosθ=2sen²(θ/2) e expansão de1−sen(z)/z perto de zero. É cálculo emfloat, sem certificação completa de arredondamento. Resultados até10⁻¹² fora de[0,1] são recortados por arredondamento; desvios maiores geram erro. Não interpretar o recorte como validação de todo intervalo arbitrariamente estreito.

A norma analítica é1. Mas ponto médio comM=n amostra sen²[nπ(i+1/2)/M]=1 em cada célula e retorna2. Uma grade nos extremos amostraria zeros. Essa falha é da quadratura subamostrada, não da função. O desafio original comN=1000,n=3 permanece válido nesse recorte; não é uma regra universal para toda frequência.

Cinco testes: probabilidades por primitiva contra integração deSimpson separada, incluindo faixa estreita junto à parede; norma/ortogonalidade/nós; simetria, partições e limite por intervalos; escala de energia e caso de subamostragem; contratos. Não constituem comprovação física do potencial ideal, análise de erro de todo solver ou experimento pessoal.

## Resoluções dos12 exercícios

1. E₃/E₁=9, exemplo preservado.
2. n=0 não é um autofestado normalizado válido.
3. Modo3 tem2nós internos.
4. DobrarL multiplica energia por1/4.
5. Probabilidade central emn=1:1/2+1/π.
6. Probabilidade central emn=2:1/2.
7. Densidade reduzida do modo1 no centro:2.
8. Massa de um ponto isolado:0.
9. (E₃−E₂)/E₁=5.
10. Ponto médio comM=n=3 retorna2por subamostragem.
11. Média pode coincidir com nó, como emn=2.
12. Convergência de massas de intervalos não implica o limite pontual da densidade.

Revisão20min: derivar o inteiro e amplitude, calcular probabilidades centrais e explicar a norma2por malha inadequada. Dúvidas e avaliação pessoal pendentes. Paredes finitas, outros potenciais/geometrias, observáveis gerais e validação experimental continuam em preparação; nenhum grupo curricular é declarado completo.

Conferência da referência numérica: para n=7 e intervalo[0,3/4], Simpson com1200subintervalos diferiu da primitiva em7,21×10⁻¹¹; com2400, em4,51×10⁻¹², redução próxima de16. A referência foi refinada, mantendo conferência por limite de Simpson: (b−a)h⁴(2nπ)⁴/180 para essa densidade suave, mais margem numérica explícita no teste. Isso é distinto do caso de subamostragem M=n, cuja falha é muito maior.
