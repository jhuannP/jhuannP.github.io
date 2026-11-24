# Covariância temporal: centragem, unidades e admissibilidade

O modelo finito tem três resultados equiprováveis Z∈{−1,0,1}. Duas posições fictícias X=10+Z e Y=3+2Z, em metros, têm médias 10 e 3, produto médio 94/3 m² e covariância 4/3 m². Variâncias 2/3 e 8/3 m², correlação de Pearson 1. A combinação 2X−Y=17 m é constante: a matriz é singular e válida.

O exemplo anterior adimensional Y=X² foi preservado: covariância zero, variâncias 2/3 e 2/9 e dependência demonstrada por P(X=0|Y=0)=1≠1/3. A figura é uma distribuição completa de três átomos de peso 1/3; não é uma amostra de dados observados.

Uma matriz de covariância tem aᵀCa=Var(aᵀX)≥0. A proposta [[1,2],[2,1]] falha para a=(1,−1), dando −2. A proposta de ordem três com variâncias unitárias e C12=C13=9/10, C23=−9/10 respeita limites de cada par, mas dá −12/5 na direção (1,−1,−1). Testar apenas limites por pares não basta. A rotina constrói C de um modelo finito ponderado e não certifica matrizes arbitrárias.

Covariância temporal K(s,t) usa pares da mesma realização. O produto bruto R(s,t)=E[XₛXₜ] é chamado autocorrelação em algumas fontes: não é Pearson. A relação é R=K+m(s)m(t). Reduzir a dependência aos tempos a uma função da defasagem exige hipótese de covariância estacionária.

Na raiz do site:

    python3 -m labs.covariancia-temporal.exact
    python3 -m unittest discover -s labs/covariancia-temporal -t .

Cinco testes verificam os exemplos, dependência por contagem, pesos não uniformes, translação/escala, variância nula, projeções em 125 direções de um vetor de três componentes, duas matrizes inválidas e contratos de entrada. A função aceita int/Fraction sem bool, pesos não negativos com soma positiva e normaliza-os. Os resultados são momentos populacionais do modelo fornecido, sem divisor amostral n−1. Não estima uma covariância a partir de uma trajetória ou usa amostras da IC.

Fonte específica de fundamentos: [MIT 6.432, Willsky/Wornell/Shapiro, capítulo 4](https://sia.mit.edu/wp-content/uploads/2015/04/chapter4.pdf), §4.3, PDF20–22 (páginas do PDF contadas a partir de 1), consulta textual parcial em 22/10/2026. Não houve leitura integral, reprodução de figuras ou exercício copiado. A conexão temática com Chorin–Hald/Pavliotis foi preservada, sem afirmar nova leitura desses livros.

Aula ampliada para onze seções/doze exercícios, em rascunho assistido por IA para revisão de Jhuann. Código, exemplo e desafio anteriores preservados. Próxima revisão pessoal: obter a matriz centrando os três pares e justificar por que singular não significa inválida. Estimação amostral dependente, certificador geral de positividade, processos gaussianos e previsão linear mais ampla continuam pendentes. Esta preparação não comprova domínio pessoal ou resultado de pesquisa.

Verificação: cinco testes novos e 13 de catálogo aprovados; 540 estruturas MathML conferidas. Em 390 px, figura, matriz e unidades legíveis; exercício da covariância rejeitou 94/3 e aceitou 4/3. Largura da página igual à tela e nenhum erro de console observado. Prévia: covariancia-temporal-mobile.jpg. Suíte global e modelos interativos preservados, sem nova revalidação integral. Catálogo: 501 aulas/3098 exercícios; trilha de Processos: 25 aulas/90 exercícios em rascunho. Saldo semanal após bloco: 92%; parada em 65%. Próxima revisão pessoal: reconstruir a matriz e a direção de variância zero. Próximo bloco editorial em outra trilha: contratos de funções científicas, para tornar hipóteses e unidades dos experimentos verificáveis em código.
