# Indução forte e fatoração — laboratório original

Proposição: todo inteiro n≥2 é produto de um ou mais primos. Base n=2. No passo forte suponha todos os inteiros de 2 a n−1. Se n é primo, a fatoração é n. Se é composto, n=ab com 2≤a,b<n; aplique a hipótese a ambos e concatene os produtos. Isso prova existência. Unicidade exige argumento adicional, não demonstrado aqui. 1 não é primo e fica fora deste enunciado.

O algoritmo implementa divisão tentativa, diferente da decomposição abstrata da prova. Invariante: produto dos fatores emitidos vezes restante = entrada. Nenhum inteiro entre 2 e divisor−1 divide o restante. Assim, um divisor aceito é primo: se fosse composto teria um fator menor que também dividiria o restante. Após retirar o divisor, repita-o para capturar multiplicidade. No final, se restante>1 e divisor²>restante, ele é primo: um composto possuiria algum divisor não maior que sua raiz quadrada. A igualdade no while é essencial para quadrados de primos.

Terminação: a cada iteração, ou o restante inteiro positivo diminui ou o divisor aumenta. O divisor não passa da raiz da entrada enquanto a condição persiste; logo há finitas iterações. Esse argumento usa a limitação por inteiros, não a suposição de que todo laço termina. Custo didático, sem garantia de eficiência para grandes entradas; limite do laboratório em 10⁶, sem teste de primalidade probabilístico.

```sh
python3 labs/inducao-fatoracao/factor.py
python3 -m unittest discover -s labs/inducao-fatoracao -t .
```

Exemplo próprio: 72=2³3², com restantes36,18,9,3,1. Quatro testes com exemplos, 999 entradas, primalidade por todos os divisores menores como oráculo separado, invariantes de cada retirada, fronteira de quadrados e contratos. Nenhum teste finito prova o teorema universal ou unicidade.

Apoio consultado parcialmente em texto em29/10/2026: Apostol, Calculus I, 2ª ed.1967, §I4.2–I4.3, p.34/PDF54, princípios de indução e boa ordenação. O OCR imprime I4 como14; referência ao bloco introdutório I. Derivação da forma forte, fatoração e código originais; não se atribui ao livro este exemplo nem se reproduz exercício. Sem leitura integral, nova inspeção visual ou distribuição do PDF privado. Revisão pessoal pendente.
