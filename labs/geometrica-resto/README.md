# Série geométrica — laboratório de precisão

Definição: S_N soma N termos, expoentes0..N−1. Amplitude a, razão r reais; código racional. O painel, exemplo de quatro termos, Python e IDs s1/s2 anteriores foram preservados. Novo recorte em rascunho para revisão pessoal.

Apostol, CalculusI,2ª ed.1967,§10.8 p.388/PDF408: identidade finita, Teorema10.5 e necessidade do termo geral nulo. Cabeçalho impresso e página da extração textual conferidos em27/10/2026. Consulta parcial, sem nova inspeção visual ou leitura integral. Exemplos, figura, cotas de precisão e uniformidade, código e exercícios próprios; exemplar privado não distribuído.

Na raiz: `python3 labs/geometrica-resto/geometric.py`. Biblioteca padrão. int/Fraction, rejeita bool/float; N e orçamento0..1000. A soma finita aceita qualquer razão racional. Resto/busca exigem |r|<1 inclusive se a=0, contrato mais restrito que o critério matemático da série nula. Tolerância estritamente positiva, comparação de erro estrita. None significa orçamento esgotado, nunca prova de divergência. Frações podem ficar grandes; não é rotina genérica otimizada ou análise de estabilidade de float.

Script confere441 somas por recorrência contra fórmula fechada (3 amplitudes,7 razões,21 quantidades), restos onde definidos, fronteiras do critério de precisão e entradas inválidas. Verificações complementam a derivação; não certificam domínio pessoal. Próxima revisão20min: derivar identidade, justificar N11 e comparar somas pares/ímpares de razão negativa. Aplicações físicas precisam declarar se somam amplitude, energia ou outra grandeza.


## 27/10/2026 — série geométrica, resto e precisão

`serie-geometrica` ampliada de3 seções/2 exercícios para12/12. Preservados exemplo de quatro termos, Python, painel e IDs s1/s2. Derivação finita por cancelamento, definição por limite das parciais, condição de convergência com exceção a=0, resto com sinal versus erro absoluto, precisão estrita, orçamento de busca e cota uniforme em |r|≤ρ<1. Exemplos negativos e separação amplitude/energia; figura e laboratório originais. Não trata soma alternativa de séries divergentes como convergência usual.

Apostol, CalculusI,2ª ed.1967,§10.8 p.388/PDF408: identidade finita, Teorema10.5 e teste necessário do termo geral. Recorte textual parcialmente reconferido em27/10/2026, cabeçalho impresso/PDF da extração paginada; sem nova inspeção visual ou leitura integral. Exemplos, precisão, extensão uniforme, figura, código e exercícios próprios. Exemplar privado não distribuído.

Verificação:14 testes de catálogo aprovados;821 estruturas MathML do catálogo conferidas. Laboratório executado com441 somas (3 amplitudes×7 razões×21 quantidades) por recorrência comparadas à fórmula fechada, restos, fronteiras da busca e contratos. São exemplos executáveis, não441 testes unitários distintos. Para a=1,r=1/2, N=11 é o primeiro com erro<1/1000; para r=−1/2, resto após três termos é−1/12. Busca sem resultado retorna None por orçamento, não divergência. No navegador390px, exercício7 rejeitou10 e aceitou11 pelo Enter; figura inspecionada em `geometrica-resto-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela e revisão pessoal pendentes.

CálculoII:21 aulas/177 exercícios e6 introduções curtas; seis grupos curriculares parciais. Catálogo global51 trilhas,550 aulas/4475 exercícios e189 introduções curtas. Contagens não provam curso completo ou domínio pessoal. Próxima revisão20min: derivar identidade e resto, justificarN11 e comparar parciais para razão negativa. Próxima elaboração global: consultar a cobertura de BiologiaI e uma lacuna curricular ainda parcial antes de escolher novo recorte. Saldo semanal78%; parada65% preservada.
