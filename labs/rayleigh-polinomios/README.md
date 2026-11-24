# Rayleigh–Ritz: cota, domínio e uma base de duas funções

27/10/2026. Aula existente ampliada para16 seções/12 exercícios, com apoio de IA, em rascunho. Três seções, dois exercícios, exemplo f=x(1−x), código e desafio de escala anteriores preservados. Revisão pessoal de Jhuann pendente. Trilha complementar de formação; não é disciplina formal concluída ou resultado de pesquisa.

## Problema e cota

Operador−u″ no intervalo adimensional[0,1], funções reais C² com u(0)=u(1)=0 e u não identicamente nula. É um recorte suave do domínio variacional; não se prova aqui extensão a H¹₀, auto-adjunticidade ou completude abstrata. R[u]=∫u′²/∫u². Integrar u(−u″) por partes dá numerador positivo sem termo de borda. Escala c≠0 multiplica ambas integrais por c², preservando R.

O problema de autovalor tem λn=n²π² e un=sin(nπx). λ=0 gera função linear nula pelas bordas; λ<0 gera combinação hiperbólica que também só satisfaz ambas bordas quando nula. O primeiro valor éπ².

Prova específica da cota sem assumir uma expansão espectral completa: φ=sinπx>0 no interior, u=φv. Expandir e usar φ″=−π²φ fornece

u′²−π²u²=φ²v′²+(φφ′v²)′.

Integre de ε a1−ε e passe ao limite. Para u C² com bordas zero, o termo u²φ′/φ tende a zero nas duas pontas e o restante é integrável. Portanto ∫u′²−π²∫u²=∫φ²[(u/φ)′]²≥0. A igualdade exige u=cφ. Dividir pela norma prova R≥π². A prova é delimitada a este operador e estas hipóteses, não copiada da rota espectral do handout.

## Tentativas e Ritz

f=x−x²:∫f′²=1/3,∫f²=1/30,R=10. Excesso≈0,130396, erro relativo≈1,32% no autovalor, não no perfil da função. g=f². Para f+g, integrais17/35 e31/630, R=306/31≈9,87096774.

Na base(f,g), u=c1f+c2g:

H=[[1/3,1/15],[1/15,2/105]],

M=[[1/30,1/140],[1/140,1/630]],

R=(cᵀHc)/(cᵀMc).

M é positiva definida pela norma quadrática de uma combinação não nula de funções independentes. Não é identidade; a base não é ortonormal. Restringir cᵀMc=1 produz elipse compacta, com extremos. Derivação por multiplicador dá Hc=λMc. O determinante, normalizado pelo coeficiente líder, é λ²−112λ+1008. Raízes56±4√133; a menor é≈9,86974962. É o mínimo de R nesse espaço finito, não a tentativa específica f+g ou o modo exato.

Como span{f}⊂span{f,g}, segue π²≤λRitz≤R[f+g]≤R[f]. A cadeia depende de integrais exatas e funções admissíveis. u=1 teria razão formal zero, mas viola as bordas. Uma quadratura não herda automaticamente o lado da desigualdade: é preciso controlar seus erros. A figura compara formas com pico1; essa mudança de escala não afeta R e proximidade visual não mede erro.

No intervalo físico de comprimento L, autovalores do operador−d²/dx² são n²π²/L² em comprimento⁻². Frequência ao quadrado ou energia exigem constantes do modelo físico. Aqui o intervalo é adimensional, sem previsão experimental.

## Laboratório e verificações

`ritz.py` usa polinômios em coeficientes crescentes int/Fraction, sem bool/float. Produto interno integra monômios exatamente. `rayleigh` rejeita função nula e violação de ambas bordas. `trial(a,b)` constrói af+bg. `matrices` calcula H/M pelas integrais, `normalized_characteristic` produz coeficientes exatos e `ritz_values` aproxima em float as duas raízes do problema específico2×2. Não é solver de Sturm–Liouville geral, de elementos finitos ou prova computacional de todos os casos.

Da raiz: `python3 -m unittest discover -s labs/rayleigh-polinomios -t .`.

Cinco testes: matrizes/quocientes/polinômio característico exatos; quadratura de polinômios por expressão separada das funções em quatro combinações; pares Ritz e resíduos generalizados; identidade positiva verificada por quadratura trigonométrica independente para f; escala, bordas, função nula e contratos. Quadraturas não são exatas para os integrandos gerais usados; comparam-se com referência racional/identidade. Testes finitos não substituem a prova de cota e não certificam erros em bases arbitrárias.

## Referência e alcance

[S.G.Johnson — The Min–Max/Variational Theorem and the Rayleigh Quotient,MIT18.303](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-analysis-and-numerics-fall-2014/resources/mit18_303f14_minmax/). Handout datado5/10/2011, disponível no curso de2014. pp.1–2 consultadas parcialmente em27/10/2026, para quociente, formulação variacional e Laplaciano Dirichlet; não se leu integralmente as quatro páginas ou reproduziu suas figuras/exercícios.

A fonte utiliza hipóteses espectrais. A prova por identidade positiva no intervalo, a base polinomial, matrizes, cálculos, figura e testes foram desenvolvidos separadamente. Não se atribui a esta fonte uma escolha desses parâmetros ou exemplo Ritz específico. A trilha é própria e não presume equivalência com Física MatemáticaI/II da USP. Nenhum livro privado foi distribuído.

## Exercícios e próxima revisão

Respostas dos12 itens:10; não;1/3;1/30;10;306/31;1/140;56−4√133; problema generalizado Hc=λMc; constante viola bordas; espaço maior não aumenta o mínimo; quadratura pode perder a cota. Dicas e resoluções completas na aula.

Duas sessões propostas de20min: refazer bordas, identidade e quociente; depois H/M, mínimo finito e cadeia de cotas. Dúvidas e avaliação pessoal em branco. Pendentes: espaços de Sobolev, operadores/pesos/bordas gerais, completude, elementos finitos, convergência de bases e revisão pessoal.

Conferência da entrega: cinco testes locais e14 de catálogo aprovados;734 estruturas MathML verificadas. Em390px, exercício9 rejeitou descartar M e aceitou o problema generalizado pelo Enter; figura inspecionada, sem transbordamento ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes. Saldo semanal85%, parada65%.
