# Tolerâncias: comparar precisa de escala e propósito

A aula usa Δ=|a−b|, S=max(|a|,|b|) e critério Δ≤max(atol,rtol S), simétrico como math.isclose. Isso difere do erro relativo de uma aproximação frente a referência não nula a, que divide por |a|. A tolerância absoluta tem a unidade de a e b; a relativa é adimensional.

Zero versus 1e−8: com rtol=1e−6 e atol=0, o limite é 1e−14, insuficiente. atol=1e−7 aceita o par. Em escala grande, 1e9 versus 1e9+500 é aceito com rtol=1e−6, mesmo se atol=5; o máximo não exige respeitar os dois limites simultaneamente. Se a exigência é erro absoluto até 5, use rtol=0 e atol=5, que rejeitam esse par.

Converter metros para centímetros multiplica a e b e atol por 100; não muda rtol. Estar próximo não é transitivo: com rtol=0,01, 100≈101 e 101≈102 passam, mas 100≈102 falha. Os decimais ideais 1,0004 e 1,00049 têm diferença 0,00009 apesar de ambos aparecerem como 1,000 com três casas. Compare antes de formatar.

Na raiz do site:

    python3 -m labs.tolerancias-escala.comparison
    python3 -m unittest discover -s labs/tolerancias-escala -t .

within aceita somente int/float finitos após conversão, sem bool, e exige tolerâncias explícitas: 0≤rtol<1 e atol≥0. Usa math.isclose. O contrato é mais restrito que a função geral; não aceita infinitos e não afirma reproduzir suas regras especiais para eles. Conversão de int a float pode já arredondar a entrada, como em 2**53+1. Uma tolerância zero não recupera essa precisão.

Cinco testes conferem zero e próximo float além da fronteira absoluta, igualdade com tolerâncias zero, 3.468 configurações de uma grade binária contra desigualdade racional, simetria, conversão de unidades, não transitividade, apresentação e entradas/tolerâncias inválidas. O painel existente foi preservado. O critério de exercícios da plataforma é distinto e não foi alterado; novas questões pequenas têm tolerâncias explícitas suficientes para rejeitar zero como resposta a 1e−14.

Fontes consultadas parcialmente em 22/10/2026: [math.isclose](https://docs.python.org/3/library/math.html#math.isclose), [PEP 485](https://peps.python.org/pep-0485/) e [tutorial de ponto flutuante](https://docs.python.org/3/tutorial/floatingpoint.html). Contas, testes e implementação de interface próprios. Sem instalação, uso de dados reais ou validação da IC. Aula ampliada para onze seções/doze exercícios, em rascunho assistido por IA para revisão pessoal. Exemplo/desafio anteriores e painel preservados. Próxima revisão: explicar por que a combinação pelo máximo pode falhar em impor um limite absoluto obrigatório. Convergência e orçamento de erro científico continuam pendentes.

Verificação: cinco testes novos e 13 de catálogo aprovados; 543 estruturas MathML conferidas. No navegador, questão de limite relativo rejeitou zero e aceitou 1e-14. Painel testado por teclado com a=0, diferença 1e-8 e rtol=1e-6: atol=1e-12 rejeitou; atol=1e-7 aceitou. Leitura em 390 px e fórmulas conferidas, sem transbordamento horizontal ou erros de console observados. Linha antiga de apresentação compactada após detectar corte visual. Prévia: tolerancias-zero-mobile.jpg. Não houve revalidação integral da suíte global ou dos demais painéis. Total: 501 aulas/3138 exercícios em rascunho; nenhuma disciplina concluída. Saldo semanal após bloco: 92%; parada em 65%.
