# Volume molar parcial e adição finita

28/10/2026. Material original com apoio de IA; revisão pessoal pendente. Uma fase homogênea a T,P fixas, sem reação. Modelo fictício V=100n_A+60n_B−4n_A n_B/(n_A+n_B), quantidades em mol, V em cm³. Coeficientes100,60,−4 em cm³/mol. Não é ajuste de dados ou modelo de estabilidade de fases.

V̄_A=(∂V/∂n_A) com T,P,n_B fixos, e analogamente B. Derivar o termo racional dá x_B² para A e x_A² para B. Assim V̄_A=100−4x_B² e V̄_B=60−4x_A² cm³/mol. Não são volumes molares puros nem V/N.

A função é homogênea de grau1: V(λn)=λV(n). Derivar emλ dá V=Σn_i V̄_i. A T,P fixas, comparar o diferencial dessa soma com dV=ΣV̄_i dn_i dá Σn_i dV̄_i=0. Em x=x_B, as derivadas dos volumes parciais são−8x e8(1−x), com combinação ponderada zero. A identidade é de volume; não determina μ, atividades ou G. μ_i é definido como molar parcial de G, exigindo informação adicional.

Exemplo3mol A/1mol B: soma pura360cm³, mistura−3cm³,total357cm³. V/N89,25,V̄_A99,75,V̄_B57,75cm³/mol. Adicionar0,5mol de B dá final386cm³,ΔV29cm³; aproximação inicial28,875cm³,resto0,125cm³. Resto exato para δ≥0:4n_A²δ²/[N²(N+δ)] nas unidades adotadas; O(δ²) para N fixo. Limite B diluído em A:56cm³/mol, diferente de B puro60cm³/mol. Na fronteira, propriedade do componente ausente é limite de adição unilateral.

Fonte: Levine,Physical Chemistry,6ªed.2009,§9.2 pp.264–266/PDF282–284,consulta textual parcial em28/10; p.265/PDF283 renderizada e inspecionada para definição/diferencial/variáveis fixas. Sem leitura integral ou cópia de exemplos,figuras,exercícios. Números,função e diagrama próprios. PDF privado fora do site; edição efetivamente usada na turma não confirmada. Programa CCM0124 já mapeado, não reaberto neste bloco; data e limitação de versão da turma preservadas.

Da raiz:

```sh
python3 labs/molares-parciais/mixture.py
python3 -m unittest discover -s labs/molares-parciais -t .
```

Código int/Fraction,quantidades não negativas,total positivo; adição somente de B com δ≥0. Quatro testes: exemplo,24composições com Euler/Gibbs–Duhem e72escalas,9pares de quantidades com27incrementos e9quocientes de derivada,limites puros/contratos. Testes verificam o modelo prescrito, não física de uma mistura real.

Revisão20min: derivar as duas propriedades, reconstruir357, comparar adição exata/local e limite diluído/puro. Dados reais, determinação experimental, propriedades molares gerais e atividade não ideal permanecem pendentes.
