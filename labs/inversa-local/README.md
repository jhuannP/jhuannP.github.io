# Função inversa: um ramo explícito

Rascunho original preparado com IA, revisão de Jhuann pendente. MAT0216 foi cursada sem aprovação por nota; material não altera esse registro ou certifica domínio.

## Domínios e interpretação

F(x,y)=(x²+y,y). Para x>0, g+(u,v)=(sqrt(u−v),v), no aberto u>v; x<0 dá o ramo negativo. As duas composições são identidades nos domínios correspondentes. Det DF=2x, mas F(2,1)=F(−2,1)=(5,1). A restrição x≠0 tem dois componentes; nunca se conclui injetividade global dela apenas pelo determinante não nulo.

Teorema C¹ em aberto de dimensão finita enunciado na aula; prova geral apenas esboçada, com fonte para estudo. Inversa de matriz e regra da cadeia dão a derivada depois de estabelecida uma inversa diferenciável. O exemplo verifica diretamente existência e regularidade do ramo.

`forward`, `jacobian`, `inverse_jacobian`: int/Fraction, sem bool/float, valores exatos. A matriz inversa não existe em x0. `inverse_float`: int/float finitos representáveis, diferença u−v finita e positiva, sinal de ramo int±1. Resultados aproximados; cancelamento perto de u=v pode perder informação. Não é inversor geral, Newton, prova automática ou medição física. Coordenadas sem unidade atribuída.

## Conferir

Da raiz:

    python3 -B labs/inversa-local/inverse.py
    python3 -B -m unittest discover -s labs/inversa-local -t .

A=(2,1), F(A)=(5,1), Dg com linhas(1/4,−1/4),(0,1). Perturbação(h,k) dá resto direto(h²,0). Para alvo vindo de F(A+(h,k)), erro da previsão inversa é −h²/4 na coordenada x. Com h1/10,k0: previsão41/400 versus incremento real40/400, erro−1/400.

Cinco métodos de teste: seis pontos em duas ordens de produto de matrizes e diferenças simétricas exatas; quinze perturbações racionais para resto e erro;24 avaliações dos dois ramos e seis raízes comparadas com Decimal70; marcos/determinante versus ganho de cinco mapas diagonais; contratos/fronteira. Não há amostragem que prove um teorema para todo mapa. A figura mostra apenas o corte y=1, não a imagem inteira de um mapa em R².

## Fontes

Fonte complementar primária: Jiří Lebl, *Basic Analysis*, §8.5, Teorema8.5.1 e recortes da prova por contração/derivada, consulta parcial29/10/2026:
https://www.jirka.org/ra/html/sec_svinvfuncthm.html

Enunciado e roteiro reescritos; exemplos polinomiais, parâmetros, código, figura e exercícios próprios. Não resolve ou reproduz exercícios/figuras da fonte; não leitura integral da seção ou da parte de função implícita.

Programa oficial MAT0216 reaberto29/10/2026 (captura indicada de seis dias antes), ativação01/01/1985, sem desativação. Pede enunciados de inversa/implícita. Versão da turma2023 não comprovada. Bibliografia oficial e acervo seguem no mapa; esta fonte online é complementar, sem equivalência à edição de Apostol ou nova leitura pertinente daquele exemplar neste bloco.
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=MAT0216
