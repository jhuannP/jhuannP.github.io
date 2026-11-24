# Densidade, grades e intervalos certificados

Construção original com `Fraction`, sem dependências. Execute `python3 labs/densidade-racional/grid.py` e `python3 -m unittest discover -s labs/densidade-racional -t .` na raiz do protótipo.

`between(a,b)` recebe apenas limites racionais e devolve n=floor(1/(b−a))+1, m=floor(na)+1 e m/n estritamente interno. Usa divisão inteira para piso, inclusive negativos; não truncamento em direção a zero. A prova matemática vale para limites reais, mas a rotina não representa reais arbitrários. A escolha de n é suficiente, não minimal. Numeradores/denominadores de entrada até10**12 e n≤10**6, com rejeição explícita fora do orçamento.

`sqrt2_bracket(k)` usa raiz inteira de 2×10**(2k), k=0..12, para construir dois racionais positivos cujos quadrados enquadram2. A prova de existência e irracionalidade de sqrt2 é matemática; o experimento só verifica intervalos finitos. Não infere racionalidade por número de casas exibidas. Todos os valores são adimensionais. SVG próprio: diagrama esquemático dos quadrados em três precisões, sem copiar figura de livro.

Referência complementar pública: Jiří Lebl, Basic Analysis I, seção1.2.2, Teorema1.2.4, https://www.jirka.org/ra/html/sec_setofreals.html, consulta parcial29/10/2026. Organização, construções computacionais, exemplos, redação, figura e exercícios próprios; nenhuma lista do livro reproduzida. ApostolI2ªed permanece referência curricular/acervo já confirmado, sem nova leitura de corpo neste bloco. EmentaCCM0113 reaberta29/10/2026:ativação15/07/2024, versão ministrada2023 não comprovada.

Quatro testes: exemplos/piso negativo;820 intervalos racionais, deslocamentos e reflexão;13 pares de limites por quadrados, aninhamento e Decimal independente;contratos. Esses testes não provam o teorema para todos os reais nem certificam domínio pessoal. Revisão de Jhuann pendente.
