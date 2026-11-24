# p-valor discreto: laboratório original

Modelo: cinco ensaios Bernoulli independentes, hipótese simples θ=1/2, alternativa θ>1/2 escolhida antes, estatística K e cauda superior inclusiva. Não é um teste bilateral nem um posterior da hipótese.

Execute da raiz do protótipo:

```sh
python3 labs/pvalor-discreto/exact.py
python3 -m unittest discover -s labs/pvalor-discreto -t .
```

Os p-valores em k=0,…,5 são 1,31/32,13/16,1/2,3/16,1/32. Para α=0,05 só k=5 rejeita: tamanho 1/32; no parâmetro alternativo θ=3/4 o poder é 243/1024. A probabilidade θ é parâmetro do modelo, diferente do p-valor calculado.

Dois experimentos independentes de cinco moedas produzem erro familiar 63/1024 ao comparar cada p-valor com 0,05. A enumeração das 1024 sequências verifica isso independentemente da fórmula de produto. Bonferroni compara cada teste com 0,025: aqui nenhuma rejeição é possível. O limite pela união dispensa independência; a fórmula de produto a exige.

A função de soma de rejeições calcula uma massa para p-valores fornecidos; não certifica sua validade. A calibração testada é a de `upper_pvalues` sob a lei que o gerou. A rotina limita n a 20 para manter o laboratório pequeno. Usa somente biblioteca padrão e frações exatas; sem dados pessoais, coleta, ajustes ou dependências.

Fonte de apoio: Magalhães e Lima, Noções de Probabilidade e Estatística, 7ª ed., §8.2, pp.264–266 (PDF279–281), consulta textual parcial em 29/10/2026 sobre erros, nível e região crítica. A extensão discreta, enumeração, contas e código são originais; não se atribui esse exemplo ao livro. Não houve leitura integral, reprodução de exercício ou distribuição do exemplar. Revisão pessoal pendente.
