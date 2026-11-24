# Integrais trigonométricas: estrutura, sinal e cadeia

Rascunho original de `c2-trig-integral`,10 seções/10 exercícios. Potências inteiras não negativas de seno/cosseno, argumentos em radianos. Preserva exemplo de média, IDs, Python e desafio anteriores. Não cobre todas as integrais trigonométricas.

## Derivação e exemplos

Seno ímpar permite reservar sin x dx e usar u=cos x com sinal negativo; cosseno ímpar permite reservar cos x dx e usar u=sin x. Se ambas pares, identidades reduzem potências. As fórmulas são conferidas por diferenciação, não apenas por comparação de resultados numéricos.

Exemplo próprio sin³x cos⁴x: primitiva −cos⁵x/5+cos⁷x/7, integral de0 aπ/2 igual2/35. Produto sin²x cos²x tem média1/8 nesse intervalo, diferente de1/4 (produto das médias). Integral de sin x cos x em[0,π] é zero por cancelamento, não porque o integrando seja nulo. Cadeia em sin²(3x) dá denominador12 no seno da primitiva. Substituições por inversas/raízes têm cuidados de domínio além deste recorte.

## Fontes e limites

Apostol I,2ª ed.1967, §5.7 p.212/PDF232: regra da cadeia e substituição, consulta textual parcial em27/10/2026; sem nova inspeção visual ou leitura integral. [OpenStax Calculus2 §3.2](https://openstax.org/books/calculus-volume-2/pages/3-2-trigonometric-integrals), início sobre paridade/identidades consultado parcialmente. Exemplos resolvidos novos, figura e exercícios próprios, sem reproduzir os da referência. Modelo curricular já registrado; Júpiter não reaberto. Tangente/secante, redução geral e radicais permanecem pendentes.

## Laboratório opcional

```sh
python3 labs/integrais-trigonometria/integrals.py
```

Quatro testes:25 derivadas numéricas em pontos regulares, quadraturas independentes em três malhas, refinamento de diferença central e contratos. Simpson não é integrador simbólico; usa funções suaves dos exemplos. Erro/tolerância e refinamento não substituem identidades. O efeito de diminuir o passo não é garantido indefinidamente em float. Revisão pessoal pendente.

Duas sessões de20min: escolher a transformação e derivar a primitiva; depois calcular integrais/médias e explicar sinais/unidades. Não confundir integral com área sem sinal nem média com valor pontual.


## 27/10/2026 — integrais trigonométricas: paridade, sinal e cadeia

`c2-trig-integral` ampliada de3 seções/2 exercícios para10/10, preservando IDs, exemplo médio, Python e desafio. Potências inteiras não negativas: separar fator ímpar, transformar por identidade e integrar polinômio; ambas pares usam ângulo duplo. Casos próprios sin³cos⁴ e sin⁴cos³, derivação conferida; produto sin²cos² tem média1/8, diferente do produto das médias1/4. Integral com cancelamento de sinais não é área sem sinal; uso da cadeia não exige inversa global. Fator6 para sin²(3x), unidade angular e caso m=n0 explícitos. O período de sin² foi corrigido paraπ.

Fontes parciais em27/10/2026: Apostol I2§5.7 p.212/PDF232, cadeia/substituição, extração textual sem nova inspeção visual/leitura integral. OpenStaxCalculus2§3.2 https://openstax.org/books/calculus-volume-2/pages/3-2-trigonometric-integrals , início sobre paridade/identidades. Exemplos novos, figura e exercícios próprios; sem copiar problemas/figuras. Programa não reaberto. Tangente/secante, redução geral e radicais continuam pendentes; recorte complementar não amplia grupo oficial por inferência.

Quatro testes em `labs/integrais-trigonometria/integrals.py`:25 diferenças centrais, quadraturas independentes em três malhas, refinamento e contratos. Erros máximos h0,04/0,02/0,01:5,023578e−4;1,256196e−4;3,140678e−5. Integral ímpar por Simpson512=0,0571428571399 versus2/35=0,0571428571429. Conferências numéricas não substituem identidades; não se promete melhora indefinida ao reduzir passo float.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou1/4 e aceitou1/8 para média do produto; documento390/390px, console sem erros observados. Figura inspecionada em `integrais-trig-escolha-mobile.jpg`; viewport restaurada. Windows real, leitor de tela e revisão pessoal pendentes.

Cálculo2 mantém21 aulas/225 exercícios, uma introdução curta e seis grupos oficiais parciais. Global51 trilhas/577 aulas/5294 exercícios,141 introduções curtas; sem cobertura integral/domínio certificados. Próxima ação:duas sessões de20min para escolher transformação/derivar e comparar médias/sinais. Próxima elaboração global:conferir a lacuna de aprendizagem/memória em BiologiaIV e localizar a referência antes de desenvolver. Saldo semanal antes/depois66%; parada operacional65% preservada.
