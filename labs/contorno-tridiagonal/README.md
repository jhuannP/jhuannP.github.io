# Contorno tridiagonal — erros que precisam ser separados

29/10/2026. Rascunho assistido por IA; revisão pessoal pendente. −u″=f,[0,1],malha uniforme,Dirichlet. Sem dado experimental ou claim sobre pesquisa pessoal.

## Reconstruir

1. n subintervalos,h=1/n,n−1 incógnitas. T tem diagonal2,vizinhas−1. TU=h²f com bordas somadas ao primeiro/último lado direito; emn=2,ambas somam no mesmo ponto.
2. Derive o defeito central por TaylorC⁴:||A_hu−f||∞≤h²M/12. Identidade zᵀTz=Σ(z_{i+1}−z_i)² prova positividade/invertibilidade.
3. Pivôs da eliminação especial:d_k=(k+1)/k. Algoritmo temO(n)operações e armazenamento,nãoO(n)em bits para frações arbitrárias. Não é um solver tridiagonal geral com pivoteamento.
4. Referência fabricada u*=x²(1−x)²,f=−2+12x−12x². Erro nodal exatoU−u*=h²x(1−x). Para n par,erro máximo1/(4n²). Resíduo da matriz zero não elimina esse erro.
5. Princípio do máximo/barreiraB=x(1−x)/2 dá||e||∞≤||r||∞/8 paraA_he=r,bordas zero. Logo erro de discretização≤h²M/96. Resíduo não escalador̃=h²r exige dividir o limite porh². Erro entre nós depende de uma interpolação e análise adicionais.

## Execução

```sh
python3 labs/contorno-tridiagonal/boundary.py
python3 -B -m unittest discover -s labs/contorno-tridiagonal -t .
```

`solve` recebe h²f interior antes das bordas e retorna extremos e valores interiores. int/Fraction,até255 pontos interiores. `residual` usaA_h,portanto já está dividido porh². `quartic` oferece referência/source para n2..256. Sem arrays densos novos;Python/desafio antigos da aula mantidos.

Cinco testes:45 sistemas contra inversa explícita,sem mutação do lado direito;15 problemas quadráticos/bordas;sete malhas com identidade quártica;seis perturbações por limite de resíduo;contratos. T⁻¹(i,j)=min(i,j)[n−max(i,j)]/n é um oráculo independente da eliminação. Inclui verificação de todos os nós de cada caso;quantidades não certificam domínio ou teoria geral.

## Fontes realmente consultadas

- Burden,Faires,Burden,Análise Numérica10ª edição brasileira2016,§11.3:pp.767–770/PDF779–782,inspeção visual parcial29/10/2026. TOC p.xv/PDF13 foi localizador, não corpo. No trecho tardio,o deslocamentoPDF é+12,diferente do+14 observado emHermite;paginação conferida nos cabeçalhos. Fonte usaN pontos interiores;usamosn subintervalos. Corpo apoia diferenças centrais,matriz tridiagonal e ordem. Implementação,barreira discreta e exemplos próprios;sem copiar algoritmo,figuras,listas ou exemplo resolvido do livro. PDF privado não distribuído.
- [Driscoll/Braun,FNC10.3.2](https://fncbook.com/python/diffmats/),consulta textual parcial29/10/2026:segunda derivada/matriz de diferenciação. Tentativa anterior/fdmethod/indisponível,não usada como corpo. Não copiamos código ou dependências;matrizinteriorDirichlet é nosso recorte.
- ProgramaCCM0226 permanece com a conferência indexada22/10/2026;versão de2025 não confirmada,não reaberto aqui.

Revisão pessoal e extensões para coeficientes variáveis,outras bordas,outras dimensões,arredondamento e solvers esparsos permanecem pendentes. Este laboratório é referência clássica para estudo, não valida uma PINN ou demonstra um resultado da IC.
