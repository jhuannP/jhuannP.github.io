# Vizinhos, métrica e empates

Modelo binário1D, coordenadas int/Fraction e rótulos inteiros0/1. Distância absoluta; empate de distância usa índice original, empate de votos escolhe0. Preservados exemplo, Python, desafio e IDs kn1/kn2 da aula. O script novo racional não altera o algoritmo anterior nem o painel.

Fonte pública parcialmente consultada em27/10/2026: scikit-learn1.9.1, User Guide§1.6.2 e aviso de distâncias empatadas na fronteira de vizinhos, https://scikit-learn.org/stable/modules/neighbors.html . Sustenta votação uniforme, papel de k e efeito da ordenação em empates. Dados, regras específicas, figura, escala e diagnósticos são próprios. Sem instalar/executar scikit-learn ou reler Bishop nesta extensão.

Na raiz: `python3 labs/vizinhos-empates/knn.py`. Biblioteca padrão. N não vazio,1≤k≤N, sem bool/float. Retorna índices, distâncias, votos, fração e classe; não retorna risco estimado ou validação de calibração. Para q4,k3: índices2,3,1; rótulos1,1,0; voto2/3 e classe1. K5 prevê0. Em6,5/k1, permutar os dois últimos registros muda o resultado devido ao desempate por índice.

Conferência executável:25 rankings comparados a contagem independente de precedências por pares;120 permutações no caso sem empate de corte;36 transformações afins positivas comuns de treino/consulta preservam os vizinhos; consulta no treino, ponto distante, efeito de escala multidimensional por distâncias ao quadrado e contratos. A conta2D não é uma implementação de kNN multidimensional. Não certifica desempenho em dados futuros.

Próxima revisão20min: reconstruir os vizinhos e distinguir voto, distância e probabilidade calibrada. Uma fração igual em4 e100 não implica igual suporte local. Seleção de k, avaliação separada, calibração, métricas gerais e dados reais permanecem pendentes. Conteúdo em rascunho, revisão pessoal de Jhuann não realizada.


## 27/10/2026 — kNN: vizinhos, empates e suporte local

`ml-knn` ampliada de3 seções/2 exercícios para12/12. Exemplo/Python/desafio/painel e IDs kn1/kn2 preservados, inclusive desempate por índice original e voto empatado para0. Conjunto próprio de cinco registros, q4 com k3 prevê1 e k5 prevê0; q6,5/k1 depende da ordem de registros empatados. k ímpar não evita empate de distância. Fração de votos não prova calibração: q4 e100 compartilham2/3 com distâncias muito diferentes. Escala2D por distância quadrada, caso de consulta no treino, custo do algoritmo escolhido e fronteiras de avaliação. Sem dados reais ou estimativa de generalização.

Fonte pública parcialmente consultada em27/10/2026: scikit-learn1.9.1, User Guide§1.6.2 e aviso de empate no corte da seleção, https://scikit-learn.org/stable/modules/neighbors.html . Votação uniforme, papel de k e dependência da ordenação em empates. Exemplos, política específica, diagnóstico e figura próprios. Não houve instalação/execução de scikit-learn ou nova leitura de Bishop.

Verificação:14 testes de catálogo aprovados;821 estruturas MathML do catálogo conferidas. Script racional executado:25 rankings comparados a contagem de precedências por pares,120 permutações no caso sem empate de corte,36 transformações afins positivas comuns que preservam vizinhos, consultas no treino/longe, contraste de escala2D por conta explícita e contratos. Não é implementação2D, calibração ou avaliação de dados futuros. No navegador390px, exercício3 rejeitou0 e aceitou1 pelo Enter; figura inspecionada em `vizinhos-empates-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados; revisão pessoal pendente.

MachineLearning:25 aulas/150 exercícios,15 introduções curtas e dez recortes desenvolvidos. Catálogo global51 trilhas,552 aulas/4519 exercícios e187 introduções curtas; sem curso completo ou domínio pessoal certificado. Próxima revisão20min: enumerar vizinhos antes dos votos e explicar efeito de ordem/escala, distinguindo voto de probabilidade calibrada. Próxima elaboração global: conferir uma lacuna de MecânicaEstatística e seu suporte bibliográfico, preservando alternância. Saldo semanal78%; parada65% preservada.
