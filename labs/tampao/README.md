# HA/NaA: base conjugada, espectadores e tampão

Material didático original em rascunho para revisão de Jhuann. Par hipotético, sem medições, preparo experimental ou resultado pessoal presumido.

## Referências consultadas em 16/10/2026

- Atkins/Jones/Laverman, Princípios de Química, 7ª edição, Bookman 2018: sumário e partes de 6G.1–6G.3, páginas impressas 499–500 e 505 (PDF 631–632 e 637). Não foi lido integralmente o tópico nem reproduzido exercício ou figura. A edição difere da terceira indicada pelo programa CCM0114.
- [OpenStax Chemistry 2e, 14.6](https://openstax.org/books/chemistry-2e/pages/14-6-buffers): par conjugado e efeitos de doses pequenas de ácido/base. Os dados numéricos, balanços, curvas e exercícios desta aula são próprios.

A noção qualitativa de reserva finita foi distinguida da capacidade diferencial beta, derivada para o cenário abaixo. Livros privados permanecem no acervo.

## Convenção e sistema

c°=1 mol/L; concentrações normalizadas. Ca e Cs são HA e NaA analíticos por volume final fixo, C=Ca+Cs. q>0 representa dose idealizada de NaOH; q<0, HCl. Na=Cs+max(q,0), Cl=max(-q,0) e S=Na-Cl=Cs+q. Não há volume de titulante ou simulação de uma bureta. Ka=10^-5 e Kw=10^-14 são constantes adotadas no cenário ideal a 25 °C; coeficientes de atividade e solvente aproximados por 1.

Massa C=a+u, carga h+Na=a+o+Cl, Ka=ha/u e Kw=ho. Eliminar espécies fornece g(h)=h+S-Kw/h-C Ka/(Ka+h)=0. g' é positivo. Como a está entre 0 e C, h fica entre as raízes positivas de h²+S h-Kw=0 e h²+(S-C)h-Kw=0. O código usa fórmulas estáveis para esses limites e bisseção em log h.

## HH e capacidade

No equilíbrio ideal, pH=pKa+log10(a/u) é uma identidade. Substituir a/u por (Cs+q)/(Ca-q) é uma aproximação de composição. É avaliada somente quando ambos os estoques superam um limiar numérico de 10^-12 C; esse critério evita logaritmo indefinido junto das bordas, mas não valida a aproximação. A solução completa continua física além dos estoques formais, com excesso de ácido ou base.

beta=dq/dpH, a C e volume fixos, é ln(10)[h+Kw/h+C Ka h/(Ka+h)^2]. Seu valor numérico multiplicado por c° tem unidade mol/L por pH. beta é local; não é uma quantidade total adicionável. O termo do par conjugado tem máximo ln(10)C/4 em h=Ka, mas isso não é máximo universal da capacidade total, que inclui água/excesso de ácido/base.

## Reprodução e referências independentes

Na raiz: `python3 -m unittest discover -s labs/tampao -t .`.

Quatro testes verificam:

- massa/carga, Ka/Kw e HH com espécies de equilíbrio em 45 composições;
- 12 configurações resolvidas por Newton na cúbica com Decimal de 80 dígitos: h³+(Ka+S)h²+[Ka(S-C)-Kw]h-KaKw=0;
- beta por diferenças finitas de dose, diluição extrema e ausência de HH fora dos estoques;
- limites de ácido sozinho, sal sozinho, água, ácido/base forte sem HA e entradas inválidas.

A referência Decimal parte do limite superior e usa a cúbica, não a bisseção como referência de si mesma. `reference.json` tem 45 configurações cruzadas JS/Python, incluindo ácido e sal puros.

## Exploração proposta

1. Ca=Cs=0,005 mol/L, q=0: pH do modelo aproximadamente 5,00173, não exatamente 5.
2. Adicione q=0,001 mol/L no cenário de volume fixo: HH por estoques aproximadamente 5,17609; equilíbrio com água aproximadamente 5,17729. Confira Na=0,006 mol/L.
3. Mantenha razão analítica 1 e dilua para Ca=Cs=5e-9: pH aproximadamente 6,98936. A identidade com a/u permanece válida; a estimativa por estoques deixa de acompanhar.
4. Ultrapasse um estoque formal. O modelo não deve produzir concentrações negativas ou logaritmos de valores negativos; HH por estoques fica ausente.
5. Compare Cs/C=0 e 1: ácido sozinho versus sal da base conjugada. Kb=Kw/Ka; o sal sozinho não é automaticamente neutro.

Bases neutras, volume variável, titulação experimental, polipróticos, não idealidade, força iônica e seleção de sistemas reais permanecem pendentes. Nenhum curso concluído ou competência pessoal certificada.
