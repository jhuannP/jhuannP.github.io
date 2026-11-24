# Acidez e transferência de próton

Material original em rascunho para revisão. Uma única reação ideal HA+B⇌A⁻+BH⁺, com reagentes neutros e produtos de cargas opostas. Não calcula pH, velocidade, sítio de protonação ou valores de pKa a partir da estrutura.

Os pKas devem corresponder ao mesmo solvente, temperatura e convenções. K=Ka(HA)/Ka(BH⁺)=10^ΔpKa. O painel usa diferenças hipotéticas −6..6, sem associar essas constantes a moléculas reais. Sem solvente prótico explícito, ionização própria, reações adicionais, pares iônicos, coeficientes de atividade ou precipitação.

Totais CA=[HA]+[A⁻], CB=[B]+[BH⁺]. Nesta família [A⁻]=[BH⁺]=x e [HA]=CA−x, [B]=CB−x. Define-se x a partir da referência sem produtos; escolher f=x/min(CA,CB) não é evoluir no tempo. As famílias e o inventário de próton dessa referência são conservados. Misturas com estoques independentes de sais/produtos podem exigir outros balanços.

Com r=CB/CA e u=x/CA, Q=u²/[(1−u)(r−u)]. A raiz física estável é u=2r/[1+r+sqrt((1−r)²+4r/K)], inclusive K=1. No caso equimolar, f_eq=sqrt(K)/(1+sqrt(K)). Em K=100, f_eq=10/11; em K=1 e r=4, x/CA=0,8 e x/CB=0,2. Diluir ambas as famílias preserva f neste modelo, porque há dois solutos de cada lado; isso não se generaliza à dissociação de HA em água.

ΔrG/(RT)=ln(Q/K) é energia livre molar de reação no estado escolhido, não mudança finita de G nem velocidade. Equilíbrio e composição escolhida ficam separados. O gráfico usa uma parametrização inversa exata da curva logQ(f), para resolver regiões próximas dos extremos; mostra somente a faixa vertical −8..8. f=0/1 não têm logQ finito: ponto omitido e limite explicado. Pequenas concentrações são exibidas em notação científica.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/acidez-transferencia/experiment.py
python3 labs/acidez-transferencia/verify_decimal.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
```

Quatro testes: quinze referências independentes em Decimal 70 dígitos por bisseção da equação polinomial; casos algébricos equimolares/K=1 e simetria dos totais; balanços de famílias/carga, domínio e escala; gradiente e mínimo de energia livre ideal em nove configurações. A função adimensional de comparação é g(u)=(1−u)ln(1−u)+(r−u)ln(r−u)+2u ln(u)−u ln K, a menos de constantes, com 0 ln0=0. Sua derivada é ln(Q/K); o mínimo é comparado a 101 composições por configuração. Não se afirma uma precisão universal fora do domínio.

O teste de balanço usa tolerância de arredondamento em unidades do último dígito para somas de ponto flutuante. `reference.json` contém 36 cenários JS/Python, e o teste JavaScript também compara as quinze raízes Decimal. O verificador grava `decimal_reference.json`, fornecido junto para reprodução. Nenhum arquivo é dado experimental.

## Fontes consultadas parcialmente — 16/10/2026

- Brown e Poon, *Introduction to Organic Chemistry*, sexta edição, Wiley 2016, exemplar privado do acervo. Trechos de 2.2–2.5, pp. impressas 43–50 (PDF 63–70); inspeção visual das páginas 46 e 49. Sem reprodução de páginas, figuras, tabelas de pKa ou exercícios. As ressalvas de edição/ano do mapa curricular continuam.
- [OpenStax Organic Chemistry 2.8](https://openstax.org/books/organic-chemistry/pages/2-8-acid-and-base-strength): definição de pKa e força relativa.
- [OpenStax Organic Chemistry 2.9](https://openstax.org/books/organic-chemistry/pages/2-9-predicting-acid-base-reactions-from-pka-values): pares conjugados e direção relativa de transferência.
- [OpenStax Chemistry 2e 16.4](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy), trecho Free Energy and Equilibrium: relação entre Q, ΔrG e K.

Exemplos e derivação do modelo finito originais. Não se declarou leitura integral dos capítulos. Pendentes: acidez de famílias específicas, efeitos de estrutura quantitativos, meios reais, protonações adicionais e revisão pessoal.
