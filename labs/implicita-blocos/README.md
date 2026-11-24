# Função implícita por blocos

Rascunho original preparado com IA, revisão pessoal pendente. Material de MAT0216 sem alterar seu registro acadêmico RN2023/1.

## Modelo

F=(z²+w−s,z−w−t), parâmetros s,t e incógnitas z,w. Ponto base(1,1,1,0), F=0. A=−I e B com linhas(2z,1),(1,−1), det B=−(2z+1). Dg=−B⁻¹A tem linhas(1,1)/(2z+1) e(1,−2z)/(2z+1). Resolver B Dg=−A não prova existência sem as hipóteses do teorema.

Em s+t>−1/4, z=(−1±sqrt(1+4(s+t)))/2 e w=z−t. Duas soluções globais não contradizem unicidade local perto de uma delas. O ramo da raiz com sinal mais tem z>−1/2, não z>0 necessariamente. Na dobra z−1/2, A continua inversível: s=z²+w,t=z−w é outra representação regular.

Funções de restrição/blocos: int/Fraction sem bool/float. Raiz explícita: int/float finitos representáveis e discriminante positivo/finito; os ramos C¹ excluem a dobra. Não algoritmo de Newton ou solucionador geral. Cancelamento do ramo positivo perto de q=s+t=0 pode perder precisão. Coordenadas matemáticas sem unidade física; sem dados empíricos.

## Reconstruir

Da raiz:

    python3 -B labs/implicita-blocos/implicit.py
    python3 -B -m unittest discover -s labs/implicita-blocos -t .

Em s=t1: soluções(1,0) e(−2,−3); Dg no primeiro ramo tem linhas(1/3,1/3),(1/3,−2/3). Caminho t1,z1+h,w h exige s1+3h+h². Para h1/10, previsão31/300 e incremento real30/300; erro−1/300 em z e w.

Seis métodos de teste:21 estados de restrição/42 avaliações de ramos; relação por blocos em sete valores de z;12 componentes de derivada contra diferenças centrais Decimal70; cinco trajetórias racionais; dobra e posto via bloco alternativo; contratos. Testes finitos de implementação, não prova de existência para todo mapa. A figura é o corte t1, não superfície completa ou fenômeno medido.

## Fontes

Apostol, *Cálculo*,volumeII, tradução Reverté1996/reimpressão2004 previamente identificada. §9.6 pp.331–333/PDF345–347, consulta textual parcial29/10/2026; p.333/PDF347 visualmente conferida para sinal e ponto das derivadas. O trecho assume função diferenciável antes de derivar: não o usamos sozinho como prova de existência.

Jiří Lebl, *Basic Analysis*,§8.5.1,Teorema8.5.6 e recortes da prova por mapa aumentado, consulta parcial29/10/2026. Complementar ao programa, sem leitura integral:
https://www.jirka.org/ra/html/sec_svinvfuncthm.html

Enunciado e roteiro reescritos; exemplo,figura,código e exercícios próprios. Não são exercícios resolvidos da fonte. Programa oficial permanece conferido em29/10 no bloco anterior, ativação01/01/1985, versão da turma2023 não comprovada. Bibliografia e exemplares distintos preservados; PDFs privados não distribuídos.
