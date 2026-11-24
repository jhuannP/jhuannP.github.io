# Zeros de polinômios — primeiro laboratório

Rascunho didático, pendente da revisão de Jhuann. Exemplos adimensionais originais; não são dados de pesquisa.

## Fontes efetivamente consultadas em 16/10/2026

- Burden/Faires/Burden, tradução da 10ª edição: sumário e início da seção 2.6, páginas impressas 102–104 (PDF 116–118), lidos visualmente no acervo privado. Confirmam a seção sobre zeros/Müller, contagem de raízes, Horner e divisão com resto. Não houve leitura integral da seção nem reprodução de exemplos, imagens ou exercícios. A bibliografia oficial de CCM0218 aponta a 7ª edição, não a 10ª; a equivalência de páginas não é presumida.
- [NumPy polyroots](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html): convenção crescente, matriz companheira e limitações para raízes múltiplas. Não implementamos esse algoritmo.
- [NumPy polydiv](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html): divisão com quociente e resto na mesma convenção. O código do laboratório é próprio, sem NumPy.

Os arquivos dos livros permanecem privados. Esta página não contém caminhos do acervo.

## Reprodução e estudo

Na raiz: `python3 -m unittest labs.zeros-polinomios.test_experiment`. `experiment.py` implementa Horner com derivada, divisão por x-r, limite de Cauchy e Newton usual/modificado com diagnósticos. `reference.json` contém 36 configurações com m=1,2, quatro iniciais, 0/1/3 passos e fatores 1/m. Os testes JS cruzam resultados e identidade de reconstrução. O núcleo aceita até oito passos; os controles exibem até seis.

1. Expanda (x-1)^m(x+2), m=1,2. Identifique todas as raízes pela fatoração deste exemplo.
2. Compare três passos de Newton usual e modificado a partir de 2. O fator conhecido m se refere à raiz +1.
3. Confirme p=(x-r)q+resto, sem descartar o resto. Para (x-1)^2 e r=101/100, obtenha q=x-99/100 e resto=1/10000 usando frações.
4. Mostre exatamente que perturbar o termo constante de (x-1)^2 por -10^-8 desloca os zeros por +/-10^-4. Resíduo não é erro na raiz.
5. No código, experimente x²+1 com inicial 0: a derivada nula impede o passo real. Isso não exclui as raízes complexas.

## Leitura do gráfico e paradas

A curva foca x entre 0,5 e 2,5 e é avaliada na forma fatorada. O círculo acompanha somente Newton usual. Tabela e texto comparam os dois métodos; avaliações de Newton e resto usam Horner na forma expandida. Essa distinção importa perto de uma raiz múltipla. Mostramos erro verdadeiro porque +1 é conhecido nesta família; em um problema geral ele não está disponível. Valores x arredondados para cinco casas podem parecer iguais enquanto a coluna científica de erro ainda é positiva.

`computedZero` significa resíduo calculado zero, sem certificado de raiz exata; `derivativeZero`, `nonfinite`, `stagnation` e `limit` são motivos diferentes de parada. Não há tolerância de sucesso arbitrária. Os testes incluem identidades racionais, referência por soma direta e casos de falha, além da comparação entre linguagens.

## Cobertura parcial

Müller, aritmética complexa, isolamento geral, condicionamento quantitativo, agrupamentos e deflação sucessiva com controle de erro continuam pendentes. A aula não é um solver de todas as raízes, não conclui a disciplina e não certifica competência pessoal.
