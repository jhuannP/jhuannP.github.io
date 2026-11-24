# Simpson adaptativo: auditar amostras e estimativas

29/10/2026. Material original em rascunho para revisão.

S0painel,S1duasmetades,δ=S1−S0. Sob expansão regular de quartaordem,E1≈δ/15;C=S1+δ/15. Indicador|δ|/15estima erro da regra fina,não é cota universal da corrigida. Orçamentos de folhas somamtolerância se divididos por2 em cada bifurcação;somar indicadores controla só o diagnóstico.

x⁴em[0,1]:S0=5/24,S1=77/384,δ=−1/128,indicador1/1920,C=1/5exato. Regra corrigida integra graus≤5; indicador pode serpositivo com erro corrigidozero.

Contraexemplo original:q=x(x−1/4)(x−1/2)(x−3/4)(x−1). Integral q²=5/1419264 por expansão e antiderivada;f=(1419264/5)q² tem integral1. Cinco valores iniciais são0,logo S0=S1=C=indicador0,erro real1. Polinômio suave não negativo; tolerância menor não revela zeros adicionais. Divisão prévia no meio revela oitavos neste caso,não cura universalmente funções desconhecidas.

`audit.py` usa int/Fraction para coeficientes e limites,1..21coeficientes. Audita apenas umpainel e conhece a integral polinomial,não substitui a rotina adaptativa float anterior. Gráfico gerado pela função conhecida,não inferido dos cinco zeros. Unidades abstratas; numa aplicação,tolerância/indicador têm unidades da integral.

Fonte: Burden/Faires/Burden,tradução10ªedição/terceira brasileiraCengage2016,§4.6 pp243–245/PDF257–259 visualmente consultadas29/10/2026,parcialmente. Sem cópia de figura/atividade/exemplo ouPDF privado. SumárioPDF12confirmou início243. Nova aberturaJúpiterCCM0218expirou;conferência anterior não substituída por tentativa malsucedida.7ªedição oficial não tem paginação presumida.

```sh
python3 labs/simpson-amostras/audit.py
python3 -B -m unittest discover -s labs/simpson-amostras -t .
```

Cinco testes: referência quartica;graus0..5 em trêsintervalos;polinômio invisível com33avaliações fatoradas independentes;rotina adaptativa anterior/cincozeros,limite deprofundidade,split conhecido e desafio anterior;contratos. Referências analíticas e contraprova,não garantia de integrador para função arbitrária. Código,exemplo e desafio anteriores preservados.
