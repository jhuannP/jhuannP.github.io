# Calor explícito: pesos,modos e erro

Modelo u_t=αu_xx em[0,L],α>0 constante,Dirichlet zero,sem fonte,malha uniforme M intervalos e tempoΔt. r=αΔt/Δx². Um passo FTCS é r u_(i−1)+(1−2r)u_i+r u_(i+1). Para0≤r≤1/2 os pesos não negativos somam1;cada valor está entre mínimo e máximo anteriores,incluindo bordas. Essa prova vale para qualquer perfil na malha,sem usar testes como demonstração.

Modo discreto sin(jπi/M),j=1,…,M−1,tem ganho g_j=1−4r sin²(jπ/(2M)). A matriz é simétrica e diagonalizada por esses modos;0≤r≤1/2 garante |g_j|≤1 e não crescimento da norma2 discreta. Para M finito,o limite modal exato é r≤1/[2sin²((M−1)π/(2M))],um pouco maior que1/2;isso não preserva necessariamente positividade. Não confundir critério suficiente uniforme com condição necessária para qualquer malha finita.

Exemplo próprio M=4,u=(0,1,0,1,0):r1/4 dá(0,1/2,1/2,1/2,0). Um passo de diagnóstico r3/5 dá(0,−1/5,6/5,−1/5,0):novos extremos impossíveis sob o argumento de média. O modo de maior frequência dessa malha tem ganho menor que−1 e cresce em módulo. A rotina aceita de evolução rejeita r>1/2;`diagnostic_step` é apenas a demonstração de um passo,sem aceitar esse resultado como aproximação confiável.

Outro exemplo: M=4,j=2,perfil(0,1,0,−1,0),r1/4. Cada passo multiplica por1/2;apósquatro,a amplitude é1/16. O valor negativo é uma perturbação/temperatura relativa,não temperatura absoluta negativa. Solução contínua na mesma frequência teria fator exp(−α(jπ/L)²t),diferente emmalha finita. O acordo com o modo discreto verifica a implementação,mas não zera o erro da EDP.

```sh
python3 labs/calor-pesos/heat.py
python3 -m unittest discover -s labs/calor-pesos -t .
```

Fraction na evolução,3–33 pontos/0–200 passos,sem dependências. r=0 só é caso matemático limite. Quatro testes:exemplos exatos/modo;108 perfis×r com8passos para máximo/norma;modos senoidais de três malhas com dois r;contratos. Teste float modal usa recorrência avaliada separadamente,sem solver daEDP geral. Não é solver escalável ou validação de transporte real.

Fontes consultadas parcialmente29/10/2026:
- [FNC11.3,Absolute stability](https://fncbook.com/julia/absstab-diffusion/):Euler escalar,autovalores e custo de refinamento emdifusão. Exemplos da fonte usam também condição periódica;nosso Dirichlet é derivado aqui.
- [ULB,MOOC,§10.2.1](https://aquaulb.github.io/book_solving_pde_mooc/solving_pde_mooc/notebooks/04_PartialDifferentialEquations/04_03_Diffusion_Explicit.html):FTCS,Dirichlet e espectro. Nosso limite finito refinado vem da fórmula modal;não foi copiado como enunciado dafonte. Rotina,perfis,provas redigidas,figura e exercícios próprios,sem transcrever código,tabela ou figura.

Burden10 permanece referência temática do percurso;nenhuma nova paginação/consulta privada confirmada nestebloco,sem presumir equivalência à7ª do programa. URLtentativaFNC/diffusion indisponível,não contada como leitura. Outrasfronteiras,fontes,dimensões e revisão pessoal pendentes.
