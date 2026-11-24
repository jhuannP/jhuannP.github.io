# Interpolação de Lagrange — notas de aula

Aula existente aprofundada, com exemplo (0,0),(1,1),(2,4), Python, desafio e painel preservados. Rascunho original; revisão pessoal pendente.

N nós distintos determinam um polinômio de grau≤N−1, não uma função-alvo única. Bases cardinais Lᵢ e soma1; reprodução de polinômios. Sensibilidade a perturbação dos valores limitada por εΣ|Lᵢ(x)| com nós fixos. O erro de aproximação requer f∈Cᴺ e cota da derivada em intervalo que contém nós e avaliação. Arredondamento separado.

Fonte: Burden, Faires e Burden, Análise Numérica, tradução da10ª edição norte-americana, edição brasileira2016. Sumário PDF11 e recortes §3.1 pp.118–120 e122/PDF132–134 e136 inspecionados visualmente em27/10/2026; pp.117 e121/PDF131 e135 consultadas para contexto. Teoremas3.2/3.3: construção/unicidade e resto. Sem leitura integral, reprodução dos exemplos/figuras ou distribuição do livro. A bibliografia oficial cita7ª edição, sem correspondência de páginas presumida. Sensibilidade e forma baricêntrica deduzidas nestas notas.

Rodar na raiz: `python3 -m unittest discover -s labs/lagrange-bases -t .`. Biblioteca padrão, int/Fraction, nós distintos. Este laboratório separa a álgebra exata da rotina float do painel; não garante estabilidade ou precisão de pacote geral. Pesos recalculados por chamada O(N²), embora reutilizá-los permita O(N) operações por avaliação; contagem ignora custo em bits. Fora dos nós a razão baricêntrica equivale à forma direta; em um nó retorna seu valor.

Revisão proposta: derivar as bases, construir alvos f_c com os mesmos dados, e comparar Λ(3/2)=5/4 com Λ(3)=7. Todos os exemplos e exercícios são próprios.

## 27/10/2026 — Lagrange, unicidade e sensibilidade

Aula existente `interpolacao-lagrange` aprofundada de3 para14 seções e2 para12 exercícios. Preservados IDs il1/il2, exemplo(0,0),(1,1),(2,4), Python, desafio e painel. Bases cardinais, prova de unicidade com grau limitado, reprodução de quadrático, alvos f_c com os mesmos nós e erro arbitrário, perturbação dos valores em nós fixos, Λ(x), resto sob f∈Cᴺ e forma baricêntrica derivada. Laboratório racional separado da rotina float existente. Custo O(N) por avaliação exige pesos reutilizados; a chamada didática recalcula pesos O(N²), sem ignorar limitações de custo em bits/precisão float.

Fonte: Burden/Faires/Burden, tradução da10ª edição norte-americana, edição brasileira2016, §3.1 pp.118–120 e122/PDF132–134 e136 lidas parcialmente por imagem em27/10/2026; teoremas3.2/3.3. SumárioPDF11 e pp.117/121/PDF131/135 consultados para localização/contexto. Sem leitura integral ou reprodução de exemplos/figuras do livro. Bibliografia oficial cita7ª edição, sem equivalência de páginas presumida; Júpiter não reaberto nesta sessão. Sensibilidade e forma baricêntrica deduzidas nas notas; exemplos, figura e questões próprios.

Verificação:14 testes do catálogo e cinco locais aprovados;780 estruturas MathML conferidas. Laboratório:480 avaliações por reprodução polinomial em graus0–3, cardinalidade e soma das bases;27 conjuntos de dados comparados por diferenças divididas de Newton; perturbações que atingem a cota; alvos com dados iguais; reordenação, mudança afim, nós e contratos. No navegador390px, erro f_c−p rejeitou3 e aceitou−3 pelo Enter. Painel preservado respondeu a End/Home para trocar tipo de nós;9nós Chebyshev–Lobatto exibiram erro máximo observado≈0,20468 em401pontos, explicitamente sem cota global provada. Figura inspecionada em`lagrange-bases-mobile.jpg`, documento390px, console sem erros. Leitor de tela, Windows real e revisão pessoal pendentes.

ComputaçãoIII:33 aulas/207 exercícios,17 introduções curtas e11 grupos ainda parciais. Catálogo51 trilhas,544 aulas/4239 exercícios e205 introduções curtas. Nada declarado completo ou domínio pessoal demonstrado. Próxima ação: derivar bases e explicar a distinção entre interpolante único e alvo desconhecido em20min. Próximo bloco global: aprofundar uma introdução de CálculoIII com exemplo geométrico e hipóteses. Saldo semanal82%; parada operacional65% mantida.
